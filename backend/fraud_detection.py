import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

module_url = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"

# Import the Universal Sentence Encoder's TF Hub module
embed = hub.Module(module_url)

# sample text
"""messages = ["there's no coffee because you forgot to buy it",
           "there is no coffee because you forgot to buy it",
           "there is coffee because you forgot to buy it",
           "there's no coffee because you forget to buy it",
           "because there's forgot but to it you no"]"""


def fraud_score(list_of_outputs):
    # Import the Universal Sentence Encoder's TF Hub module
    embed = hub.Module(module_url)
    similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
    similarity_message_encodings = embed(similarity_input_placeholder)
    graph = tf.get_default_graph() 
    with tf.Session() as session:
        with graph.as_default():
            session.run(tf.global_variables_initializer())
            session.run(tf.tables_initializer())
            print(list_of_outputs)
            message_embeddings_ = session.run(similarity_message_encodings,
                                              feed_dict={similarity_input_placeholder: list_of_outputs})

            corr = np.inner(message_embeddings_, message_embeddings_)
            fraud_score = ((np.sum(corr, axis=1) - np.ones(len(list_of_outputs))) / np.full(len(list_of_outputs),
                                                                                            len(list_of_outputs) - 1))

            # utils.heatmap(messages, messages, corr)
            result  = list()
            for val in fraud_score:
                if val > 0.5:
                    result.append(True)
                else:
                    result.append(False)

            # return [str(round(i)) for i in fraud_score]
            return result
