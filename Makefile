PROTO_DIR := ./api.kiyotaka.ai/proto
DIST := ./kiyotaka

IMPORTS := -I $(PROTO_DIR)/service/ -I $(PROTO_DIR)/lib/ -I $(PROTO_DIR)/types/
FILES := $(PROTO_DIR)/lib/timestamp/timestamp.proto \
		$(PROTO_DIR)/types/*.proto \
		$(PROTO_DIR)/service/api/*.proto

.PHONY: $(DIST)

all: clean $(DIST)

api.kiyotaka.ai/proto:
	wget --recursive https://api.kiyotaka.ai/proto/
	find $(PROTO_DIR) -type f -name index.html -delete
	find $(PROTO_DIR) -type f -name '*.proto' -exec sed -r -i 's/^(\s+)optional\s+/\1/' {} \;

$(DIST): $(PROTO_DIR)
	mkdir -p $(DIST)
	protoc $(IMPORTS) \
		--python_betterproto_opt=debug \
		--python_betterproto_out=$(DIST) \
		$(FILES)

clean:
	rm -rf $(DIST) $(PROTO_DIR)
