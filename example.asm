;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Author: alexeev-prog                                                                                               ;;
;; Example ASM Program                                                                                                ;;
;; Program generated by FLEXPASM (github.com/alexeev-pro/flexpasm)                                                    ;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

format ELF executable 3	   ; ELF EXECUTABLE
entry start	 ; Set Start Entry

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Using PrintStringTemplate: Printing the string 'Hello, World!' to stdout ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Segment readable executable in FASM is a directive for defining a section of code with readable and executable attributes.
segment readable executable
start:
	MOV EAX, 4	; Loading 4 value into EAX register.
	MOV ECX, msg	; Loading msg value into ECX register.
	MOV EDX, msg_size	; Loading msg_size value into EDX register.
	INT 128	; Call software interrupt 128: SYSCALL
	MOV EAX, 1	; Loading 1 value into EAX register.
	XOR EBX, EBX	 ; Zeroing the EBX register using XOR
	INT 128	; Call software interrupt 128: SYSCALL


;; Segment readable writeable in FASM is a definition of a segment of program data codes, where the attributes readable (the contents of the segment can be read) and writeable (program commands can both read codes and change their values) are specified for it.
segment readable writeable
msg db 'Hello, World!', 0xA

msg_size = $-msg