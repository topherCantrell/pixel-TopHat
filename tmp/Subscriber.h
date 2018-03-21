#ifndef SUBSCRIBER_H_
#define SUBSCRIBER_H_

#include "Topic.h"
#include "json.h"

class Subscriber {
public:

	virtual ~Subscriber() = default;

	virtual void handleMessage(PublishSubscribeTopic topic, std::string message) = 0;
};

#endif /* SUBSCRIBER_H_ */
