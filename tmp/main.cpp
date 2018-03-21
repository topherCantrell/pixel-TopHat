#include <iostream>
using namespace std;

#include "TestMessageBus.h"
#include "MBAPI.h"

class ReverseStringHandler : public Responder {
public:

	virtual json handleRequest(json request) {
		json response;
		// TODO flip the response
		return response;
	}

};

TestMessageBus mb;

class StringOpSubscriber : public Subscriber {
public:

	virtual void handleMessage(PublishSubscribeTopic topic, std::string message) {
		cout << "On topic " << topic << " message :" << message << ":" << endl;
	}

};
StringOpSubscriber handler;
void mainSubscribe() {

	mb.addSubscriber(PublishSubscribeTopic::STRING_OP, handler);

}

void mainPublish() {

	json message;

	mb.publish(PublishSubscribeTopic::STRING_OP, message);

}

ReverseStringHandler rsh;
void mainServer() {

	mb.setResponder(CommandResponseTopic::REV_STRING, rsh);

}

void mainClient() {

	json request = "SyncClient";

	json response = mb.getResponse(CommandResponseTopic::REV_STRING, request, 0);

	cout << "Got Response:" << response << ":" << endl;
}

class MyHandler : public ResponseHandler {
	virtual void handleResponse(json message) {
		cout << "Response is :" << message << ":" << endl;
	}
};
MyHandler responder;
void mainAsyncClient() {

	json request = "AsyncClient";
	mb.getResponse(CommandResponseTopic::REV_STRING, request, responder, 0);
}


int main() {

	mainSubscribe();
	mainPublish();
	mainServer();
	mainClient();
	mainAsyncClient();

}
