import tornado.ioloop
import tornado.web
import os
import glob
UPLOADS_DIR = "uploads"
os.makedirs(UPLOADS_DIR, exist_ok=True)

class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload.html")

    def post(self):
        # Get text metadata fields
        title = self.get_body_argument("title", default="Untitled")
        description = self.get_body_argument("description", default="")

        # Get file
        fileinfo = self.request.files.get("file")[0]
        filename = fileinfo["filename"]
        file_body = fileinfo["body"]

        # Save the uploaded file
        filepath = os.path.join(UPLOADS_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(file_body)

        # Response (confirmation)
        self.write(f"""
        <h3>Upload Successful!</h3>
        <p><b>Title:</b> {title}</p>
        <p><b>Description:</b> {description}</p>
        <p><b>Uploaded File:</b> {filename}</p>
        """)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # List uploaded images
        images = [os.path.basename(f) for f in glob.glob(f"{UPLOADS_DIR}/*")]
        self.render("index.html", images=images)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/upload", UploadHandler),
        (r"/uploads/(.*)", tornado.web.StaticFileHandler, {"path": UPLOADS_DIR}),
        ],
        template_path="templates",
    )
    app.listen(8888)
    print("Listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
