#include "TestMessageBus.h"

using namespace std;

void TestMessageBus::addSubscriber(PublishSubscribeTopic topic, Subscriber & handler) {
	oneSubscriber = &handler;
}

void TestMessageBus::removeSubscriber(PublishSubscribeTopic topic, Subscriber & handler) {
	// TODO
}

void TestMessageBus::setResponder(CommandResponseTopic topic, Responder & responder) {
	oneResponder = &responder;
}

void TestMessageBus::removeResponder(CommandResponseTopic topic) {
	// TODO
}

void TestMessageBus::publish(PublishSubscribeTopic topic, json message) {
	oneSubscriber->handleMessage(topic,message);
}

void TestMessageBus::getResponse(CommandResponseTopic topic, json message, ResponseHandler & callback, int timeout) {
	json reply = oneResponder->handleRequest(message);
	callback.handleResponse(reply);
}

json TestMessageBus::getResponse(CommandResponseTopic topic, json message, int timeout) {
	return oneResponder->handleRequest(message);
}
