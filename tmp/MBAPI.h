#ifndef MBAPI_H_
#define MBAPI_H_

#include "Subscriber.h"
#include "ResponseHandler.h"
#include "Responder.h"
#include "Topic.h"

#include "json.h"

#include "Subscriber.h"

class MBAPI {
public:

	virtual ~MBAPI() = default;

	virtual void addSubscriber(PublishSubscribeTopic topic, Subscriber & handler) = 0;
	virtual void removeSubscriber(PublishSubscribeTopic topic, Subscriber & handler) = 0;

	virtual void setResponder(CommandResponseTopic topic, Responder & responder) = 0;
	virtual void removeResponder(CommandResponseTopic topic) = 0;

	virtual void publish(PublishSubscribeTopic topic, json message) = 0;

	virtual void getResponse(CommandResponseTopic topic, json message, ResponseHandler & callback, int timeout) = 0;
	virtual json getResponse(CommandResponseTopic topic, json message, int timeout) = 0;

};

#endif /* MBAPI_H_ */
