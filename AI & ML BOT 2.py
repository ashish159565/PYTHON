from nltk.chat.util import Chat, reflections
pairs = [
        [
            r"my name is (.*)",
            ["Hello %1. What can i do for you today?"]
        ],
        [
            r"what is ai & ml",
            ["Artificial intelligence(AI) is the use of technology to mimic the human brain.\nMachine Learning(ML) is defined as the acquistion of knowledge or skill."]
        ],
        [
            r"how is ai & ml useful",
            ["AI & ML are useful in various ways in various sectors such as healthcare, IT, etc. For more details visit \nhttps://usmsystems.com/ai-and-ml-apps-for-startup-sme/ \nhttps://www.process.st/applications-of-ai/ "]
        ],
        [
            r"how are ai & ml related",
            ["Machine Learning (ML) is commonly used along with AI but it is a subset of AI. Most AI works involves ML because intelligent behaviour requires considerable knowledge."]
        ],
        [
            r"main purpose of using ai & ml",
            ["Artificial intelligence is rapidly growing technology in modern world. The AI machines has the ablities to learn from its past experiences and feels comforts for new inputs and perform those tasks which a human want to perform."]
        ],
        [
            r"main programming languages used for ai & ml?",
            ["The main programming languages used for AI are:\n1) Python\n2) LISP\n3) Haskell\n4) Prolog\n5) C++\nThe main programming languages used for ML are:\n1) Python\n2) R\n3) JAVA and JavaScript\n4) LISP\n5) Julia"]
        ],
        [
            r"job opportunities after completing an ai & ml course",
            ["After completing an AI & ML course you can work as a Ml engineer, Iot Architect, Big Data & AI Architect, Buisness Intelligence Developer, Big Data Scientist, AI Engineer, ML Architect, Deep Learning Expert, Data & AI consultant, Robotics Professional, Research Engineer - AI"]
        ],
        [
            r"what to do after getting an ai & ml degree",
            ["Take an online course in Machine Learning/AI (Udacity/Coursera are good sources from what I hear) \nNetwork with engineers working in the field. Go to meetups/conferences to meet engineers working in the field. \nLook at various graduate programs that might interest you, see what kind of problems the professors there working on. Read their research.\nDabble around with various ML/AI frameworks. Like with most things in SE, some frameworks can be better for solving certain kinds of problems."]
        ],
        [
            r"any certification course to add value to the degree",
            ["There are several courses online on Coursera and other MOOCs. Tech giants like Google and Microsoft also offer AI and ML courses which will help take one’s career one step further.\nBelow are listed some of the popular courses:\nhttps://digitaldefynd.com/best-machine-learning-and-deep-learning-courses/"]
        ],
        [
            r"where is ai & ml used in daily life",
            ["Travel & Commute - Ex: Google Maps\nEmail Communication - Ex: Email filters, Gmail smart replies\nSocial Media\nWeb search\nOnline shopping\nSmart Personal Assistants"]
        ],
        [
            r"what can we do to improve our ml skills",
            ["You can improve your ML skills by following the steps in the following link:\nhttps://www.dummies.com/programming/big-data/data-science/10-ways-improve-machine-learning-models/"]
        ],
        [
            r"what are the benefits of choosing ai & ml",
            ["Error Reduction\nFaster Decision\nDigital Assitance\nWorks 24 x 7 without any break\nAutomating customer interactions\nReal - time assitance\nData Mining\nRapid Innovation"]
        ],
        [
            r"tools used for ai & ml",
            ["Top AI tools:- https://www.jigsawacademy.com/blogs/tools/artificial-intelligence-tools/ \nTop ML tools:- https://www.softwaretestinghelp.com/machine-learning-tools/"]
        ],
        [
            r"what are the main challenges with ai tech",
            ["Let’s think of AI as an iceberg. What you see as a user is just the tip — but beneath the surface lurks a behemoth support system of data scientists and engineers, massive amounts of data, labor-intensive extraction, preparation of the data, and a huge technology infrastructure. \nIt takes a specialized team of data scientists and developers to access the correct data, prepare the data, build the correct models, and then integrate the predictions back into an end-user experience application."]
        ],
        [
            r"what is deep learning",
            ["Deep learning is AI that uses complex algorithms to perform tasks in domains where it actually learns the domain with little or no human supervision. In essence, the machine learns how to learn.\nWhile there’s lots of exciting experimentation happening with deep learning, most practical applications you’re familiar with are based on image analysis. \nWith image analysis, a computer learns to classify random images by analysing thousands or millions of other images and their data points. For example, consumer apps like Google Photos and Facebook use deep learning to power face recognition in photos."]
        ],
        [
            r"what is natural language processing",
            ["NLP is AI that recognizes language and its many usage and grammar rules by finding patterns within large datasets.\nOne application of NLP that’s gaining traction is sentiment analysis within social media. Computers use algorithms to look for patterns in user posts across Twitter, Facebook, or other social networks to understand how customers feel about a specific brand or product."]
        ],
        [
            r"companies hiring for ai role",
            ["Google\nIBM\nFacebook\nAmazon\nPhilips\nSnapdeal\nMicrosoft\nAccenture\nAdobe\nLennovo\nIntel\nSamsung"]
        ],
        [
            r"why do we need ai",
            ["Some of the main reasons for choosing AI are:-\nDigitalization\nNew algorithms are continuosly being developed for data utilization\nShortage of skilled professionals\nGlobal Competitive Edge\nEthical Development"]
        ],
        [
            r"how to get started with ai & ml",
            ["Alright! So by this point, you are hopefully fascinated by the various features of Artificial Intelligence, and you are excited to look for a great place to get started with Artificial Intelligence.\nArtificial Intelligence is a vast and humungous field. But, don’t worry! There are tons of valuable resources and productive material that you can utilize to produce the best possible results. \nYou can gain a wide arena of knowledge just by analyzing and studying the materials on the internet.\nWebsites like Stack overflow, Data stack exchange, and GitHub, are some of the most popular sites to receive in-depth solutions and answers to the problems or errors that you are encountering with the running or installation of your program or the respective code blocks."]
        ],
        [
            r"what is turing's test",
            ["The turing test, named after Alan Turing is a method of testing a machine's human-level intelligence. \nFor more details check http://www2.psych.utoronto.ca/users/reingold/courses/ai/turing.html"]
        ],
        [
            r"what is tensor flow",
            ["TensorFlow is an open-source framework dedicated to ML. Its comprehensive and highly adaptable ecosystem of libraries, tools, and community resources that help developers build and deploy ML powered applications. \nFor more details check https://appliedmachinelearning.blog/2018/12/26/tensorflow-tutorial-from-scratch-building-a-deep-learning-model-on-fashion-mnist-dataset-part-1/"]
        ],
        [
            r"what are the different algorithm techniques you can use in ai & ml",
            ["Some algorithm techniques that can be leveraged are Learning to learn, Reinforcement learning, Semi-supervised learning, Transduction, Unsupervised learning"]
        ],
        [
            r"steps to evaluate the effectiveness of your ml model",
            ["You have to first split the data set into training and test sets. You also have the option of using a cross-validation technique to further segment the data set into a composite of training and test sets within the data. \nThen you have to implement a choice selection of the performance metrics like the following: \nConfusion matrix \nAccuracy \nPrecision \nRecall or sensitivity \nSpecificity \nF1 score \nFor the most part, you can use measures such as accuracy, confusion matrix, or F1 score. However, it’ll be critical for you to demonstrate that you understand the nuances of how each model can be measured by choosing the right performance measure to match the problem. For more details check https://medium.com/@MohammedS/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b"]
        ],
        [
            r"dangers of ai",
            ["RISKS OF ARTIFICIAL INTELLIGENCE:- \nAutomation-spurred job loss \nPrivacy violations \n'Deepfakes' \nAlgorithmic bias caused by bad data \nSocioeconomic inequality \nMarket volatility \nWeapons automatization \nFor more information check https://builtin.com/artificial-intelligence/risks-of-artificial-intelligence)"]
        ],
        [
            r"how can ai be used in detecting fraud",
            ["Leveraging AI for fraud prevention has helped companies to enhance internal security and in streamlining business processes. Thus, by driving improved efficiency, Artificial Intelligence has emerged as a major technology for preventing financial frauds. \nFor more information check https://dev.to/praveen__pkm/how-ai-helps-in-fraud-detection-3972"]
        ],
        [
            r"in python's standard library, what packages would you say are the most useful for data scientists?",
            ["Numpy, Pandas, Scipy"]
        ],
        [
            r"quit",
            ["Bye take care. See you soon :)"]
        ],
        ]

def Friday():
  print("Hi, I'm Friday and I'm here to clear your doubts about AI & ML.\nPlease type lowercase english language to start a conversation. Type quit to leave\nWhat should I call you?")
  chat = Chat(pairs, reflections)
  chat.converse()

if __name__ == "__main__":
    Friday()