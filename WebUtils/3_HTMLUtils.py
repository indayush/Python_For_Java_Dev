# 
# Example file for parsing and processing HTML
#

# import the HTMLParser module
# in Python 3 you need to import from html.parser
from html.parser import HTMLParser

metacount = 0

# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):
  # function to handle an opening tag in the doc
  # this will be called when the closing ">" of the tag is reached
  def handle_starttag(self, tag, attrs):
    global metacount
    if tag == "meta":
      metacount += 1

    print ("Encountered a start tag:", tag)                                         # Start tag is the opening bracket in a tag i.e.
    pos = self.getpos() # returns a tuple indication line and character             # ">" in a tag like "<html>" & end tag is </html>
    print ("\tAt line: ", pos[0], " position ", pos[1])

    # Checking if attributes & their values are resent, then traverse & print them -
    if attrs.__len__() > 0:
      print ("\tAttributes:")
      for a in attrs:
        print ("\t", a[0],"=",a[1])
      
  # function to handle the ending tag
  def handle_endtag(self, tag):
    print ("Encountered an end tag:", tag)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])
    
  # function to handle character and text data (tag contents)
  def handle_data(self, data):
    if (data.isspace()):
      return
    print ("Encountered some text data:", data)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])
  
  # function to handle the processing of HTML comments
  def handle_comment(self, data):
    print ("Encountered comment:", data)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])

def main():
  # instantiate the parser object and feed it some HTML data
  parser = MyHTMLParser()
    
  # open the sample HTML file and read it
  f = open("samplehtml.html","r")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)
  
  print ("%d meta tags encountered" % metacount)

if __name__ == "__main__":
    main()

'''
    Encountered a start tag: html
            At line:  2  position  0
            Attributes:
            lang = en
    Encountered a start tag: head
            At line:  3  position  2
    Encountered a start tag: meta
            At line:  4  position  4
            Attributes:
            charset = utf-8
    Encountered an end tag: meta
            At line:  4  position  4
    Encountered a start tag: title
            At line:  5  position  4
    Encountered some text data: Sample HTML Document
            At line:  5  position  11
    Encountered an end tag: title
            At line:  5  position  31
    Encountered a start tag: meta
            At line:  6  position  4
            Attributes:
            name = description
            content = This is a sample HTML file
    Encountered an end tag: meta
            At line:  6  position  4
    Encountered a start tag: meta
            At line:  7  position  4
            Attributes:
            name = author
            content = Administrator
    Encountered an end tag: meta
            At line:  7  position  4
    Encountered a start tag: meta
            At line:  8  position  4
            Attributes:
            name = viewport
            content = width=device-width; initial-scale=1.0
    Encountered an end tag: meta
            At line:  8  position  4
    Encountered comment:  Replace favicon.ico & apple-touch-icon.png in the root of your domain and delete these references
            At line:  9  position  4
    Encountered a start tag: link
            At line:  10  position  4
            Attributes:
            rel = shortcut icon
            href = /favicon.ico
    Encountered an end tag: link
            At line:  10  position  4
    Encountered a start tag: link
            At line:  11  position  4
            Attributes:
            rel = apple-touch-icon
            href = /apple-touch-icon.png
    Encountered an end tag: link
            At line:  11  position  4
    Encountered an end tag: head
            At line:  12  position  2
    Encountered a start tag: body
            At line:  14  position  2
    Encountered a start tag: div
            At line:  15  position  4
    Encountered a start tag: header
            At line:  16  position  6
    Encountered a start tag: h1
            At line:  17  position  8
    Encountered some text data: HTML Sample File
            At line:  17  position  12
    Encountered an end tag: h1
            At line:  17  position  28
    Encountered an end tag: header
            At line:  18  position  6
    Encountered a start tag: nav
            At line:  19  position  6
    Encountered a start tag: p
            At line:  20  position  8
    Encountered a start tag: a
            At line:  21  position  10
            Attributes:
            href = /
    Encountered some text data: Home
            At line:  21  position  22
    Encountered an end tag: a
            At line:  21  position  26
    Encountered an end tag: p
            At line:  22  position  8
    Encountered a start tag: p
            At line:  23  position  8
    Encountered a start tag: a
            At line:  24  position  10
            Attributes:
            href = /contact
    Encountered some text data: Contact
            At line:  24  position  29
    Encountered an end tag: a
            At line:  24  position  36
    Encountered an end tag: p
            At line:  25  position  8
    Encountered an end tag: nav
            At line:  26  position  6
    Encountered a start tag: div
            At line:  27  position  6
    Encountered an end tag: div
            At line:  29  position  6
    Encountered a start tag: footer
            At line:  30  position  6
    Encountered a start tag: p
            At line:  31  position  8
    Encountered some text data: © Copyright by Administrator
            At line:  31  position  11
    Encountered an end tag: p
            At line:  31  position  44
    Encountered an end tag: footer
            At line:  32  position  6
    Encountered an end tag: div
            At line:  33  position  4
    Encountered an end tag: body
            At line:  34  position  2
    Encountered an end tag: html
            At line:  35  position  0
    4 meta tags encountered
'''