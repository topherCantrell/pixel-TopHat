#ifndef TESTMESSAGEBUS_H_
#define TESTMESSAGEBUS_H_

#include "MBAPI.h"
#include <vector>
#include <map>
#include "Topic.h"
#include "json.h"

class TestMessageBus : public MBAPI {

	 Subscriber * oneSubscriber;
	 Responder * oneResponder;

public:
	virtual void addSubscriber(PublishSubscribeTopic, Subscriber & handler);
	virtual void removeSubscriber(PublishSubscribeTopic topic, Subscriber & handler);
	virtual void setResponder(CommandResponseTopic topic, Responder & responder);
	virtual void removeResponder(CommandResponseTopic topic);
	virtual void publish(PublishSubscribeTopic topic, json message);
	virtual void getResponse(CommandResponseTopic topic, json message, ResponseHandler & callback, int timeout);
	virtual json getResponse(CommandResponseTopic topic, json message, int timeout);
};

#endif /* TESTMESSAGEBUS_H_ */
