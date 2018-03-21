#ifndef RESPONSEHANDLER_H_
#define RESPONSEHANDLER_H_

#include "json.h"

class ResponseHandler {
public:

	virtual ~ResponseHandler() = default;

	virtual void handleResponse(json message) = 0;
};

#endif /* RESPONSEHANDLER_H_ */
