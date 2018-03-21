#ifndef RESPONDER_H_
#define RESPONDER_H_

#include "json.h"

class Responder {
public:

	virtual ~Responder() = default;

	virtual json handleRequest(json request) = 0;

};

#endif /* RESPONDER_H_ */
