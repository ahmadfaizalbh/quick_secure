Quick Secure
============

String encryption


Install
=======

.. code:: sh

    pip install quick-secure



Usage
=====

.. code:: python


    import quick_secure

    message = "sample message for encryption"
    password = "confidential"

    # Encrypt message
    encrypted*message = quick_secure.encrypt(message, password)
    print(encrypted_message)

    # Decrypt message
    decrypted*message = quick_secure.decrypt(encrypted_message, password)
    print(decrypted_message)







