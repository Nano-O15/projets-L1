#  Makefile 
#  Auteur : OUKHEMANOU Mohand

CC = gcc
CFLAGS = -std=c99 -Wall -Wextra
SRCDIR = src
BUILDDIR = build
TARGET = jeu

SRCS = $(wildcard $(SRCDIR)/*.c)
OBJS = $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SRCS))

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $^

$(BUILDDIR)/%.o: $(SRCDIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -c -o $@ $<

all: $(TARGET)

clean:
	rm -rf $(BUILDDIR) $(TARGET)

.PHONY: all clean



