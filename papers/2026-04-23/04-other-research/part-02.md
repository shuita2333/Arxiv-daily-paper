# 📦 其他研究 | 2026年04月23日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

---

### 51. [ParamBoost: Gradient Boosted Piecewise Cubic Polynomials](https://arxiv.org/abs/2604.18864)

**<font color=#1a73e8>作者：</font>** Nicolas Salvadé, Tim Hillel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalized Additive Models (GAMs) can be used to create non-linear glass-box (i.e. explicitly interpretable) models, where the predictive function is fully observable over the complete input space. However, glass-box interpretability itself does not allow for the incorporation of expert knowledge from the modeller. In this paper, we present ParamBoost, a novel GAM whose shape functions (i.e. mappings from individual input features to the output) are learnt using a Gradient Boosting algorithm that fits cubic polynomial functions at leaf nodes. ParamBoost incorporates several constraints commonly used in parametric analysis to ensure well-refined shape functions. These constraints include: (i) continuity of the shape functions and their derivatives (up to C2); (ii) monotonicity; (iii) convexity; (iv) feature interaction constraints; and (v) model specification constraints. Empirical results show that the unconstrained ParamBoost model consistently outperforms state-of-the-art GAMs across several real-world datasets. We further demonstrate that modellers can selectively impose required constraints at a modest trade-off in predictive performance, allowing the model to be fully tailored to application-specific interpretability and parametric-analysis requirements.

---


### 52. [HMR-Net: Hierarchical Modular Routing for Cross-Domain Object Detection in Aerial Images](https://arxiv.org/abs/2604.18866)

**<font color=#1a73e8>作者：</font>** Pourya Shamsolmoali, Masoumeh Zareapoor, Michael Felsberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in object detection, aerial imagery remains a challenging domain, as models often fail to generalize across variations in spatial resolution, scene composition, and semantic label coverage. Differences in geographic context, sensor characteristics, and object distributions across datasets limit the capacity of conventional models to learn consistent and transferable representations. Shared methods trained on such data tend to impose a unified representation across fundamentally different domains, resulting in poor performance on region-specific content and less flexibility when dealing with novel object categories. To address this, we propose a novel modular learning framework that enables structured specialization in aerial detection. Our method introduces a hierarchical routing mechanism with two levels of modularity: a global expert assignment layer that uses latent geographic embeddings to route datasets to specialized processing modules, and a local scene decomposition mechanism that allocates image subregions to region-specific sub-modules. This allows our method to specialize across datasets and within complex scenes. Additionally, the framework contains a conditional expert module that uses external semantic information (e.g., category names or textual descriptions) to enable detection of novel object categories during inference, without the need for retraining or fine-tuning. By moving beyond monolithic representations, our method offers an adaptive framework for remote sensing object detection. Comprehensive evaluations on four datasets highlight improvements in multi-dataset generalization, regional specialization, and open-category detection.

---


### 53. [Subgraph Concept Networks: Concept Levels in Graph Classification](https://arxiv.org/abs/2604.18868)

**<font color=#1a73e8>作者：</font>** Lucie Charlotte Magister, Alexander Norcliffe, Iulia Duta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The reasoning process of Graph Neural Networks is complex and considered opaque, limiting trust in their predictions. To alleviate this issue, prior work has proposed concept-based explanations, extracted from clusters in the model's node embeddings. However, a limitation of concept-based explanations is that they only explain the node embedding space and are obscured by pooling in graph classification. To mitigate this issue and provide a deeper level of understanding, we propose the Subgraph Concept Network. The Subgraph Concept Network is the first graph neural network architecture that distils subgraph and graph-level concepts. It achieves this by performing soft clustering on node concept embeddings to derive subgraph and graph-level concepts. Our results show that the Subgraph Concept Network allows to obtain competitive model accuracy, while discovering meaningful concepts at different levels of the network.

---


### 54. [From Natural Language to Executable Narsese: A Neuro-Symbolic Benchmark and Pipeline for Reasoning with NARS](https://arxiv.org/abs/2604.18873)

**<font color=#1a73e8>作者：</font>** Mina Gabriel, Pei Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are highly capable at language generation, but they remain unreliable when reasoning requires explicit symbolic structure, multi-step inference, and interpretable uncertainty. This paper presents a neuro-symbolic framework for translating natural-language reasoning problems into executable formal representations using first-order logic (FOL) and Narsese, the language of the Non-Axiomatic Reasoning System (NARS). To support this direction, we introduce NARS-Reasoning-v0.1, a benchmark of natural-language reasoning problems paired with FOL forms, executable Narsese programs, and three gold labels: True, False, and Uncertain. We develop a deterministic compilation pipeline from FOL to executable Narsese and validate retained examples through runtime execution in OpenNARS for Applications (ONA), ensuring that the symbolic targets are not only syntactically well formed but also behaviorally aligned with the intended answer. We further present Language-Structured Perception (LSP), a formulation in which an LLM is trained to produce reasoning-relevant symbolic structure rather than only a final verbal response. As an initial proof of concept, we also train and release a Phi-2 LoRA adapter on NARS-Reasoning-v0.1 for three-label reasoning classification, showing that the benchmark can support supervised adaptation in addition to executable evaluation. Overall, the paper positions executable symbolic generation and execution-based validation as a practical path toward more reliable neuro-symbolic reasoning systems.

---


### 55. [A Proxy Consistency Loss for Grounded Fusion of Earth Observation and Location Encoders](https://arxiv.org/abs/2604.18881)

**<font color=#1a73e8>作者：</font>** Zhongying Wang, Kevin Lane, Levi Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised learning with Earth observation inputs is often limited by the sparsity of high-quality labeled or in-situ measured data to use as training labels. With the abundance of geographic data products, in many cases there are variables correlated with - but different from - the variable of interest that can be leveraged. We integrate such proxy variables within a geographic prior via a trainable location encoder and introduce a proxy consistency loss (PCL) formulation to imbue proxy data into the location encoder. The first key insight behind our approach is to use the location encoder as an agile and flexible way to learn from abundantly available proxy data which can be sampled independently of training label availability. Our second key insight is that we will need to regularize the location encoder appropriately to achieve performance and robustness with limited labeled data. Our experiments on air quality prediction and poverty mapping show that integrating proxy data implicitly through the location encoder outperforms using both as input to an observation encoder and fusion strategies that use frozen, pretrained location embeddings as a geographic prior. Superior performance for in-sample prediction shows that the PCL can incorporate rich information from the proxies, and superior out-of-sample prediction shows that the learned latent embeddings help generalize to areas without training labels.

---


### 56. [Formally Verified Patent Analysis via Dependent Type Theory: Machine-Checkable Certificates from a Hybrid AI + Lean 4 Pipeline](https://arxiv.org/abs/2604.18882)

**<font color=#1a73e8>作者：</font>** George Koomullil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a formally verified framework for patent analysis as a hybrid AI + Lean 4 pipeline. The DAG-coverage core (Algorithm 1b) is fully machine-verified once bounded match scores are fixed. Freedom-to-operate, claim-construction sensitivity, cross-claim consistency, and doctrine-of-equivalents analyses are formalized at the specification level with kernel-checked candidate certificates. Existing patent-analysis approaches rely on manual expert analysis (slow, non-scalable) or ML/NLP methods (probabilistic, opaque, non-compositional). To our knowledge, this is the first framework that applies interactive theorem proving based on dependent type theory to intellectual property analysis. Claims are encoded as DAGs in Lean 4, match strengths as elements of a verified complete lattice, and confidence scores propagate through dependencies via proven-correct monotone functions. We formalize five IP use cases (patent-to-product mapping, freedom-to-operate, claim construction sensitivity, cross-claim consistency, doctrine of equivalents) via six algorithms. Structural lemmas, the coverage-core generator, and the closed-path identity coverage = W_cov are machine-verified in Lean 4. Higher-level theorems for the other use cases remain informal proof sketches, and their proof-generation functions are architecturally mitigated (untrusted generators whose outputs are kernel-checked and sorry-free axiom-audited). Guarantees are conditional on the ML layer: they certify mathematical correctness of computations downstream of ML scores, not the accuracy of the scores themselves. A case study on a synthetic memory-module claim demonstrates weighted coverage and construction-sensitivity analysis. Validation against adjudicated cases is future work.

---


### 57. [Choose Your Own Adventure: Non-Linear AI-Assisted Programming with EvoGraph](https://arxiv.org/abs/2604.18883)

**<font color=#1a73e8>作者：</font>** Vassilios Exarhakos, Jinghui Cheng, Jin L.C. Guo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current AI-assisted programming tools are predominantly linear and chat-based, which deviates from the iterative and branching nature of programming itself. Our preliminary study with developers using AI assistants suggested that they often struggle to explore alternatives, manage prompting sequences, and trace changes. Informed by these insights, we created EvoGraph, an IDE plugin that integrates AI interactions and code changes as a lightweight and interactive development graph. EvoGraph automatically records a branching AI-assisted coding history and allows developers to manipulate the graph to compare, merge, and revisit prior collaborative AI programming states. Our user study with 20 participants revealed that EvoGraph addressed developers' challenges identified in our preliminary study while imposing lower cognitive load. Participants also found the graph-based representation supported safe exploration, efficient iteration, and reflection on AI-generated changes. Our work highlights design opportunities for tools to help developers make sense of and act on their problem-solving progress in the emerging AI-mediated programming context.

---


### 58. [AC-SINDy: Compositional Sparse Identification of Nonlinear Dynamics](https://arxiv.org/abs/2604.18889)

**<font color=#1a73e8>作者：</font>** Peter Racioppo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present AC-SINDy, a compositional extension of the Sparse Identification of Nonlinear Dynamics (SINDy) framework that replaces explicit feature libraries with a structured representation based on arithmetic circuits. Rather than enumerating candidate basis functions, the proposed approach constructs nonlinear features through compositions of linear functions and multiplicative interactions, yielding a compact and scalable parameterization and enabling sparsity to be enforced directly over the computational graph. We also introduce a formulation that separates state estimation from dynamics identification by combining latent state inference with shared dynamics and multi-step supervision, improving robustness to noise while preserving interpretability. Experiments on nonlinear and chaotic systems demonstrate that the method recovers accurate and interpretable governing equations while scaling more favorably than standard SINDy.

---


### 59. [Gradient-Based Program Synthesis with Neurally Interpreted Languages](https://arxiv.org/abs/2604.18907)

**<font color=#1a73e8>作者：</font>** Matthew V. Macfarlane, Clément Bonnet, Herke van Hoof 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in program induction has long been the trade-off between symbolic and neural approaches. Symbolic methods offer compositional generalisation and data efficiency, yet their scalability is constrained by formalisms such as domain-specific languages (DSLs), which are labour-intensive to create and may not transfer to new domains. In contrast, neural networks flexibly learn from data but tend to generalise poorly in compositional and out-of-distribution settings. We bridge this divide with an instance of a Latent Adaptation Network architecture named Neural Language Interpreter (NLI), which learns its own discrete, symbolic-like programming language end-to-end. NLI autonomously discovers a vocabulary of primitive operations and uses a novel differentiable neural executor to interpret variable-length sequences of these primitives. This allows NLI to represent programs that are not bound to a constant number of computation steps, enabling it to solve more complex problems than those seen during training. To make these discrete, compositional program structures amenable to gradient-based optimisation, we employ the Gumbel-Softmax relaxation, enabling the entire model to be trained end-to-end. Crucially, this same differentiability enables powerful test-time adaptation. At inference, NLI's program inductor provides an initial program guess. This guess is then refined via gradient descent through the neural executor, enabling efficient search for the neural program that best explains the given data. We demonstrate that NLI outperforms in-context learning, test-time training, and continuous latent program networks on tasks that require combinatorial generalisation and rapid adaptation to unseen tasks. Our results establish a new path toward models that combine the compositionality of discrete languages with the gradient-based search and end-to-end learning of neural networks.

---


### 60. [Collaborative Contextual Bayesian Optimization](https://arxiv.org/abs/2604.18912)

**<font color=#1a73e8>作者：</font>** Chih-Yu Chang, Qiyuan Chen, Tianhan Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering optimal designs through sequential data collection is essential in many real-world applications. While Bayesian Optimization (BO) has achieved remarkable success in this setting, growing attention has recently turned to context-specific optimal design, formalized as Contextual Bayesian Optimization (CBO). Unlike BO, CBO is inherently more challenging as it must approximate an entire mapping from the context space to its corresponding optimal design, requiring simultaneous exploration across contexts and exploitation within each. In many modern applications, such tasks arise across multiple potentially heterogeneous but related clients, where collaboration can significantly improve learning efficiency. We propose CCBO, Collaborative Contextual Bayesian Optimization, a unified framework enabling multiple clients to jointly perform CBO with controllable contexts, supporting both online collaboration and offline initialization from peers' historical beliefs, with an optional privacy-preserving communication mechanism. We establish sublinear regret guarantees and demonstrate, through extensive simulations and a real-world hot rolling application, that CCBO achieves substantial improvements over existing approaches even under client heterogeneity. The code to reproduce the results can be found at this https URL

---


### 61. [MORPHOGEN: A Multilingual Benchmark for Evaluating Gender-Aware Morphological Generation](https://arxiv.org/abs/2604.18914)

**<font color=#1a73e8>作者：</font>** Mehul Agarwal, Aditya Aggarwal, Arnav Goel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While multilingual large language models (LLMs) perform well on high-level tasks like translation and question answering, their ability to handle grammatical gender and morphological agreement remains underexplored. In morphologically rich languages, gender influences verb conjugation, pronouns, and even first-person constructions with explicit and implicit mentions of gender. We introduce MORPHOGEN, a morphologically grounded large-scale benchmark dataset for evaluating gender-aware generation in three typologically diverse grammatically gendered languages: French, Arabic, and Hindi. The core task, GENFORM, requires models to rewrite a first-person sentence in the opposite gender while preserving its meaning and structure. We construct a high-quality synthetic dataset spanning these three languages and benchmark 15 popular multilingual LLMs (2B-70B) on their ability to perform this transformation. Our results reveal significant gaps and interesting insights into how current models handle morphological gender. MORPHOGEN provides a focused diagnostic lens for gender-aware language modeling and lays the groundwork for future research on inclusive and morphology-sensitive NLP.

---


### 62. [Error-free Training for MedMNIST Datasets](https://arxiv.org/abs/2604.18916)

**<font color=#1a73e8>作者：</font>** Bo Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce a new concept called Artificial Special Intelligence by which Machine Learning models for the classification problem can be trained error-free, thus acquiring the capability of not making repeated mistakes. The method is applied to 18 MedMNIST biomedical datasets. Except for three datasets, which suffer from the double-labeling problem, all are trained to perfection.

---


### 63. [AutomationBench](https://arxiv.org/abs/2604.18934)

**<font color=#1a73e8>作者：</font>** Daniel Shepard, Robin Salimans  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing AI benchmarks for software automation rarely combine cross-application coordination, autonomous API discovery, and policy adherence. Real business workflows demand all three: a single task may span a CRM, inbox, calendar, and messaging platform - requiring the agent to find the right endpoints, follow a policy document, and write correct data to each system. To address this gap, we introduce AutomationBench, a benchmark for evaluating AI agents on cross-application workflow orchestration via REST APIs. Drawing on real workflow patterns from Zapier's platform, tasks span Sales, Marketing, Operations, Support, Finance, and HR domains. Agents must discover relevant endpoints themselves, follow layered business rules, and navigate environments with irrelevant and sometimes misleading records. Grading is programmatic and end-state only: whether the correct data ended up in the right systems. Even the best frontier models currently score below 10%. AutomationBench provides a challenging, realistic measure of where current models stand relative to the agentic capabilities businesses actually need.

---


### 64. [TabEmb: Joint Semantic-Structure Embedding for Table Annotation](https://arxiv.org/abs/2604.18939)

**<font color=#1a73e8>作者：</font>** Ehsan Hoseinzade, Ke Wang, Anandharaju Durai Raju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Table annotation is crucial for making web and enterprise tables usable in downstream NLP applications. Unlike textual data where learning semantically rich token or sentence embeddings often suffice, tables are structured combinations of columns wherein useful representations must jointly capture column's semantics and the inter-column relationships. Existing models learn by linearizing the 2D table into a 1D token sequence and encoding it with pretrained language models (PLMs) such as BERT. However, this leads to limited semantic quality and weaker generalization to unseen or rare values compared to modern LLMs, and degraded structural modeling due to 2D-to-1D flattening and context-length constraints. We propose TabEmb, which directly targets these limitations by decoupling semantic encoding from structural modeling. An LLM first produces semantically rich embeddings for each column, and a graph-based module over columns then injects relationships into the embeddings, yielding joint semantic-tructural representations for table annotation. Experiments show that TabEmb consistently outperforms strong baselines on different table annotation tasks. Source code and datasets are available at this https URL

---


### 65. [Localization-Guided Foreground Augmentation in Autonomous Driving](https://arxiv.org/abs/2604.18940)

**<font color=#1a73e8>作者：</font>** Jiawei Yong, Deyuan Qu, Qi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems often degrade under adverse visibility conditions-such as rain, nighttime, or snow-where online scene geometry (e.g., lane dividers, road boundaries, and pedestrian crossings) becomes sparse or fragmented. While high-definition (HD) maps can provide missing structural context, they are costly to construct and maintain at scale. We propose Localization-Guided Foreground Augmentation (LG-FA), a lightweight and plug-and-play inference module that enhances foreground perception by enriching geometric context online. LG-FA: (i) incrementally constructs a sparse global vector layer from per-frame Bird's-Eye View (BEV) predictions; (ii) estimates ego pose via class-constrained geometric alignment, jointly improving localization and completing missing local topology; and (iii) reprojects the augmented foreground into a unified global frame to improve per-frame predictions. Experiments on challenging nuScenes sequences demonstrate that LG-FA improves the geometric completeness and temporal stability of BEV representations, reduces localization error, and produces globally consistent lane and topology reconstructions. The module can be seamlessly integrated into existing BEV-based perception systems without backbone modification. By providing a reliable geometric context prior, LG-FA enhances temporal consistency and supplies stable structural support for downstream modules such as tracking and decision-making.

---


### 66. [A Mechanism and Optimization Study on the Impact of Information Density on User-Generated Content Named Entity Recognition](https://arxiv.org/abs/2604.18944)

**<font color=#1a73e8>作者：</font>** Jiang Xiaobo, Dinghong Lai, Song Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition (NER) models trained on clean, high-resource corpora exhibit catastrophic performance collapse when deployed on noisy, sparse User-Generated Content (UGC), such as social media. Prior research has predominantly focused on point-wise symptom remediation -- employing customized fine-tuning to address issues like neologisms, alias drift, non-standard orthography, long-tail entities, and class imbalance. However, these improvements often fail to generalize because they overlook the structural sparsity inherent in UGC. This study reveals that surface-level noise symptoms share a unified root cause: low Information Density (ID). Through hierarchical confounding-controlled resampling experiments (specifically controlling for entity rarity and annotation consistency), this paper identifies ID as an independent key factor. We introduce Attention Spectrum Analysis (ASA) to quantify how reduced ID causally leads to ``attention blunting,'' ultimately degrading NER performance. Informed by these mechanistic insights, we propose the Window-Aware Optimization Module (WOM), an LLM-empowered, model-agnostic framework. WOM identifies information-sparse regions and utilizes selective back-translation to directionally enhance semantic density without altering model architecture. Deployed atop mainstream architectures on standard UGC datasets (WNUT2017, Twitter-NER, WNUT2016), WOM yields up to 4.5\% absolute F1 improvement, demonstrating robustness and achieving new state-of-the-art (SOTA) results on WNUT2017.

---


### 67. [Relationships Between Trust, Compliance, and Performance for Novice Programmers Using AI Code Generation](https://arxiv.org/abs/2604.18948)

**<font color=#1a73e8>作者：</font>** Nicholas Gardella, Matthew L. Bolton, Sara L. Riggs  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Objective. To explore how novice programmers' trust in Artificial Intelligence-driven Development Environments (AIDEs) relates to their coding performance and AI compliance while programming under time pressure. Background. Computer programming has undergone rapid upheaval due to state-of-the-art AIDEs, which provide clever automation for many aspects of software development. A longstanding interest of researchers of automation more generally has been the attitude of trust. Decades of research seek to explain how influencing trust can help to achieve desirable outcomes in different domains, but very limited work has provided similar focus on trust in AIDEs. Method. We collected subjective measures of trust along with objective measures of performance and AIDE compliance from a diverse group of 27 novice programmers between two study locations. Results. Our results corroborated traditional understandings of how trust changes through experiences. However, we did not find a relationship between trust and subsequent compliance during programming tasks. Greater compliance was associated with strong performance, and strong performance led to greater subsequent trust. Conclusion. Our findings raise new questions about the utility of trust in the context of interacting with AIDEs and generative AI. We call for further research into the effect of trust on compliance to recommendations from imperfect AI. Application. This work can inform the design of training and educational content for generative AI use within and beyond software development. Instructional designers should consider risks of AI misuse and disuse and focus on promoting desirable interaction outcomes, regardless of trust's connection to them.

---


### 68. [Superficial Success vs. Internal Breakdown: An Empirical Study of Generalization in Adaptive Multi-Agent Systems](https://arxiv.org/abs/2604.18951)

**<font color=#1a73e8>作者：</font>** Namyoung So, Seokgyu Jang, Taeuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Adaptive multi-agent systems (MAS) are increasingly adopted to tackle complex this http URL, the narrow task coverage of their optimization raises the question of whether they can function as general-purpose this http URL address this gap, we conduct an extensive empirical study of adaptive MAS, revealing two key findings: (1) topological overfitting -- they fail to generalize across different domains; and (2) illusory coordination -- they achieve reasonable surface-level accuracy while the underlying agent interactions diverge from ideal MAS behavior, raising concerns about their practical this http URL findings highlight the pressing need to prioritize generalization in MAS development and motivate evaluation protocols that extend beyond simple final-answer correctness.

---


### 69. [FlowForge: A Staged Local Rollout Engine for Flow-Field Prediction](https://arxiv.org/abs/2604.18953)

**<font color=#1a73e8>作者：</font>** Xiaowen Zhang, Ziming Zhou, Fengnian Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning surrogates for CFD flow-field prediction often rely on large, complex models, which can be slow and fragile when data are noisy or incomplete. We introduce FlowForge, a staged local rollout engine that predicts future flow fields by compiling a locality-preserving update schedule and executing it with a shared lightweight local predictor. Rather than producing the next frame in a single global pass, FlowForge rewrites spatial sites stage by stage so that each update conditions only on bounded local context exposed by earlier stages. This compile-execute design aligns inference with short-range physical dependence, keeps latency predictable, and limits error amplification from global mixing. Across PDEBench, CFDBench, and BubbleML, FlowForge matches or improves upon strong baselines in pointwise accuracy, delivers consistently better robustness to noise and missing observations, and maintains stable multi-step rollout behavior while reducing per-step latency.

---


### 70. [Physical and Augmented Reality based Playful Activities for Refresher Training of ASHA Workers in India](https://arxiv.org/abs/2604.18959)

**<font color=#1a73e8>作者：</font>** Arka Majhi, Satish B. Agnihotri, Aparajita Mondal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent health surveys in India highlight the alarming child malnutrition levels and lower rates of complete child immunization in many parts of India. Previous researches report that the conventional training pedagogy of the CHWs (Community Healthcare Workers) or the ASHAs (Accredited Social Health Activists) in India is ineffective in enhancing their capacity. Considering that the CHWs are getting equipped with smartphones, it calls for a rethinking of their training pedagogy using the ICT approach. Two refresher training tools were developed to make learning the child immunization schedule more exciting and conceptually engaging for ASHAs. The physical and AR (Augmented Reality) versions of designed card games were compared for effectiveness and knowledge retention, pre, and post-intervention through questionnaire tests conducted immediately before and after playing multiple sessions. The AR-based play was found to be better in learning and knowledge retention with more engagement, mainly due to its interactive and intuitive nature of play.

---


### 71. [Toward Clinically Acceptable Chest X-ray Report Generation: A Qualitative Retrospective Pilot Study of CXRMate-2](https://arxiv.org/abs/2604.18967)

**<font color=#1a73e8>作者：</font>** Aaron Nicolson, Elizabeth J. Cooper, Hwan-Jin Yoon 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray (CXR) radiology report generation (RRG) models have shown rapid progress, yet their clinical utility remains uncertain due to limited evaluation by radiologists. We present CXRMate-2, a state-of-the-art CXR RRG model that integrates structured multimodal conditioning and reinforcement learning with a composite reward for semantic alignment with radiologist reports. Across the MIMIC-CXR, CheXpert Plus, and ReXgradient datasets, CXRMate-2 achieves statistically significant improvements over strong benchmarks, including gains of 11.2% and 24.4% in GREEN and RadGraph-XL, respectively, on MIMIC-CXR relative to MedGemma 1.5 (4B).
To directly compare CXRMate-2 against radiologist reporting, we conduct a blinded, randomised qualitative retrospective evaluation. Three consultant radiologists compare generated and radiologist reports across 120 studies from the MIMIC-CXR test set. Generated reports were deemed acceptable (defined as preferred or rated equally to radiologist reports) in 45% of ratings, with no statistically significant difference in preference rates between radiologist reports and acceptable generated reports for seven of the eight analysed findings. Preference for radiologist reports was driven primarily by higher recall, while generated reports were often preferred for readability.
Together, these results suggest a credible pathway to clinically acceptable CXR RRG. Improvements in recall, alongside better detection of subtle findings (e.g., pulmonary congestion), are likely sufficient to achieve non-inferiority to radiologist reporting. With these targeted advances, CXR RRG systems may be ready for prospective evaluation in assistive roles within radiologist-led workflows.

---


### 72. [Mechanistic Anomaly Detection via Functional Attribution](https://arxiv.org/abs/2604.18970)

**<font color=#1a73e8>作者：</font>** Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We can often verify the correctness of neural network outputs using ground truth labels, but we cannot reliably determine whether the output was produced by normal or anomalous internal mechanisms. Mechanistic anomaly detection (MAD) aims to flag these cases, but existing methods either depend on latent space analysis, which is vulnerable to obfuscation, or are specific to particular architectures and modalities. We reframe MAD as a functional attribution problem: asking to what extent samples from a trusted set can explain the model's output, where attribution failure signals anomalous behavior. We operationalize this using influence functions, measuring functional coupling between test samples and a small reference set via parameter-space sampling. We evaluate across multiple anomaly types and modalities. For backdoors in vision models, our method achieves state-of-the-art detection on BackdoorBench, with an average Defense Effectiveness Rating (DER) of 0.93 across seven attacks and four datasets (next best 0.83). For LLMs, we similarly achieve a significant improvement over baselines for several backdoor types, including on explicitly obfuscated models. Beyond backdoors, our method can detect adversarial and out-of-distribution samples, and distinguishes multiple anomalous mechanisms within a single model. Our results establish functional attribution as an effective, modality-agnostic tool for detecting anomalous behavior in deployed models.

---


### 73. [Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft Game](https://arxiv.org/abs/2604.18975)

**<font color=#1a73e8>作者：</font>** HuaDong Jian, Chenghao Li, Haoyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In long-horizon open-world multi-agent systems, existing methods often treat local anomalies as automatic triggers for communication. This default design introduces coordination noise, interrupts local execution, and overuses public interaction in cases that could be resolved locally. To address this issue, we propose a partitioned information architecture for MLLM agents that explicitly separates private execution states from public coordination states. Building on this design, we introduce two key mechanisms. First, we develop an event-triggered working memory based on system-verified outcomes to maintain compact and low-noise local state representations. Second, we propose a cost-sensitive gated escalation mechanism that determines whether cross-region communication should be initiated by jointly considering node criticality, local recovery cost, and downstream task impact. In this way, communication is transformed from a default reaction into a selective decision. Experiments conducted on long-term construction tasks in open environments demonstrate that, compared to baseline models based on strong communication and planned structures, the introduction of gated communication and a partitioned information architecture results in superior performance in terms of blueprint completion quality and execution chain length. It also improves local self-recovery, reduces ineffective escalations, and increases the utility of public communication.

---


### 74. [Low-Rank Adaptation for Critic Learning in Off-Policy Reinforcement Learning](https://arxiv.org/abs/2604.18978)

**<font color=#1a73e8>作者：</font>** Yuan Zhuang, Yuexin Bian, Sihong He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling critic capacity is a promising direction for enhancing off-policy reinforcement learning (RL). However, larger critics are prone to overfitting and unstable in replay-buffer-based bootstrap training. This paper leverages Low-Rank Adaptation (LoRA) as a structural-sparsity regularizer for off-policy critics. Our approach freezes randomly initialized base matrices and solely optimizes low-rank adapters, thereby constraining critic updates to a low-dimensional subspace. Built on top of SimbaV2, we further develop a LoRA formulation, compatible with SimbaV2, that preserves its hyperspherical normalization geometry under frozen-backbone training. We evaluate our method with SAC and FastTD3 on DeepMind Control locomotion and IsaacLab robotics benchmarks. LoRA consistently achieves lower critic loss during training and stronger policy performance. Extensive experiments demonstrate that adaptive low-rank updates provide a simple, scalable, and effective structural regularization for critic learning in off-policy RL.

---


### 75. [AdaGScale: Viewpoint-Adaptive Gaussian Scaling in 3D Gaussian Splatting to Reduce Gaussian-Tile Pairs](https://arxiv.org/abs/2604.18980)

**<font color=#1a73e8>作者：</font>** Joongho Jo, Hyerin Lim, Hanjun Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing the number of Gaussian-tile pairs is one of the most promising approaches to improve 3D Gaussian Splatting (3D-GS) rendering speed on GPUs. However, the importance difference existing among Gaussian-tile pairs has never been considered in the previous works. In this paper, we propose AdaGScale, a novel viewpoint-adaptive Gaussian scaling technique for reducing the number of Gaussian-tile pairs. AdaGScale is based on the observation that the peripheral tiles located far from Gaussian center contribute negligibly to pixel color accumulation. This suggests an opportunity for reducing the number of Gaussian-tile pairs based on color contribution. AdaGScale efficiently estimates the color contribution in the peripheral region of each Gaussian during a preprocessing stage and adaptively scales its size based on the peripheral score. As a result, Gaussians with lower importance intersect with fewer tiles during the intersection test, which improves rendering speed while maintaining image quality. The adjusted size is used only for tile intersection test, and the original size is retained during color accumulation to preserve visual fidelity. Experimental results show that AdaGScale achieves a geometric mean speedup of 13.8x over original 3D-GS on a GPU, with only about 0.5 dB degradation in PSNR on city-scale scenes.

---


### 76. [AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993)

**<font color=#1a73e8>作者：</font>** Jiagao Hu, Daiguo Zhou, Danzhen Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception robustness under adverse weather remains a critical challenge for autonomous driving, with the core bottleneck being the scarcity of real-world video data in adverse weather. Existing weather generation approaches struggle to balance visual quality and annotation reusability. We present AutoAWG, a controllable Adverse Weather video Generation framework for Autonomous driving. Our method employs a semantics-guided adaptive fusion of multiple controls to balance strong weather stylization with high-fidelity preservation of safety-critical targets; leverages a vanishing point-anchored temporal synthesis strategy to construct training sequences from static images, thereby reducing reliance on synthetic data; and adopts masked training to enhance long-horizon generation stability. On the nuScenes validation set, AutoAWG significantly outperforms prior state-of-the-art methods: without first-frame conditioning, FID and FVD are relatively reduced by 50.0% and 16.1%; with first-frame conditioning, they are further reduced by 8.7% and 7.2%, respectively. Extensive qualitative and quantitative results demonstrate advantages in style fidelity, temporal consistency, and semantic--structural integrity, underscoring the practical value of AutoAWG for improving downstream perception in autonomous driving. Our code is available at: this https URL

---


### 77. [When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains](https://arxiv.org/abs/2604.19001)

**<font color=#1a73e8>作者：</font>** Ishita Kakkar, Enze Zhang, Rheeya Uppaal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) produce complex, multi-step reasoning traces, yet safety evaluation remains focused on final outputs, overlooking how harm emerges during reasoning. When jailbroken, harm does not appear instantaneously but unfolds through distinct behavioral steps such as suppressing refusal, rationalizing compliance, decomposing harmful tasks, and concealing risk. However, no existing benchmark captures this process at sentence-level granularity within reasoning traces -- a key step toward reliable safety monitoring, interventions, and systematic failure diagnosis. To address this gap, we introduce HarmThoughts, a benchmark for step-wise safety evaluation of reasoning traces. \ourdataset is built on our proposed harm taxonomy of 16 harmful reasoning behaviors across four functional groups that characterize how harm propagates rather than what harm is produced. The dataset consists of 56,931 sentences from 1,018 reasoning traces generated by four model families, each annotated with fine-grained sentence-level behavioral labels. Using HarmThoughts, we analyze harm propagation patterns across reasoning traces, identifying common behavioral trajectories and drift points where reasoning transitions from safe to unsafe. Finally, we systematically compare white-box and black-box detectors on the task of identifying harmful reasoning behaviours on HarmThoughts. Our results show that existing detectors struggle with fine-grained behavior detection in reasoning traces, particularly for nuanced categories within harm emergence and execution, highlighting a critical gap in process-level safety monitoring. HarmThoughts is available publicly at: this https URL

---


### 78. [Debating the Unspoken: Role-Anchored Multi-Agent Reasoning for Half-Truth Detection](https://arxiv.org/abs/2604.19005)

**<font color=#1a73e8>作者：</font>** Yixuan Tang, Yirui Zhang, Hang Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Half-truths, claims that are factually correct yet misleading due to omitted context, remain a blind spot for fact verification systems focused on explicit falsehoods. Addressing such omission-based manipulation requires reasoning not only about what is said, but also about what is left unsaid. We propose RADAR, a role-anchored multi-agent debate framework for omission-aware fact verification under realistic, noisy retrieval. RADAR assigns complementary roles to a Politician and a Scientist, who reason adversarially over shared retrieved evidence, moderated by a neutral Judge. A dual-threshold early termination controller adaptively decides when sufficient reasoning has been reached to issue a verdict. Experiments show that RADAR consistently outperforms strong single- and multi-agent baselines across datasets and backbones, improving omission detection accuracy while reducing reasoning cost. These results demonstrate that role-anchored, retrieval-grounded debate with adaptive control is an effective and scalable framework for uncovering missing context in fact verification. The code is available at this https URL.

---


### 79. [Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning](https://arxiv.org/abs/2604.19009)

**<font color=#1a73e8>作者：</font>** Linwei Dong, Ruoyu Guo, Ge Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion distillation, exemplified by Distribution Matching Distillation (DMD), has shown great promise in few-step generation but often sacrifices quality for sampling speed. While integrating Reinforcement Learning (RL) into distillation offers potential, a naive fusion of these two objectives relies on suboptimal raw sample evaluation. This sample-based scoring creates inherent conflicts with the distillation trajectory and produces unreliable rewards due to the noisy nature of early-stage generation. To overcome these limitations, we propose GDMD, a novel framework that redefines the reward mechanism by prioritizing distillation gradients over raw pixel outputs as the primary signal for optimization. By reinterpreting the DMD gradients as implicit target tensors, our framework enables existing reward models to directly evaluate the quality of distillation updates. This gradient-level guidance functions as an adaptive weighting that synchronizes the RL policy with the distillation objective, effectively neutralizing optimization divergence. Empirical results show that GDMD sets a new SOTA for few-step generation. Specifically, our 4-step models outperform the quality of their multi-step teacher and substantially exceed previous DMDR results in GenEval and human-preference metrics, exhibiting strong scalability potential.

---


### 80. [Accelerating trajectory optimization with Sobolev-trained diffusion policies](https://arxiv.org/abs/2604.19011)

**<font color=#1a73e8>作者：</font>** Théotime Le Hellard, Franki Nguimatsia Tiofack, Quentin Le Lidec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory Optimization (TO) solvers exploit known system dynamics to compute locally optimal trajectories through iterative improvements. A downside is that each new problem instance is solved independently; therefore, convergence speed and quality of the solution found depend on the initial trajectory proposed. To improve efficiency, a natural approach is to warm-start TO with initial guesses produced by a learned policy trained on trajectories previously generated by the solver. Diffusion-based policies have recently emerged as expressive imitation learning models, making them promising candidates for this role. Yet, a counterintuitive challenge comes from the local optimality of TO demonstrations: when a policy is rolled out, small non-optimal deviations may push it into situations not represented in the training data, triggering compounding errors over long horizons. In this work, we focus on learning-based warm-starting for gradient-based TO solvers that also provide feedback gains. Exploiting this specificity, we derive a first-order loss for Sobolev learning of diffusion-based policies using both trajectories and feedback gains. Through comprehensive experiments, we demonstrate that the resulting policy avoids compounding errors, and so can learn from very few trajectories to provide initial guesses reducing solving time by $2\times$ to $20 \times$. Incorporating first-order information enables predictions with fewer diffusion steps, reducing inference latency.

---


### 81. [Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis](https://arxiv.org/abs/2604.19012)

**<font color=#1a73e8>作者：</font>** Yongchao Wang, Zhiqiu Huang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning for vulnerability detection has shown promising results on early benchmarks, but recent evaluations reveal catastrophic degradation: models achieving F1 > 0.68 on legacy datasets collapse to 0.031 under strict deduplication. We identify the root cause as the semantic ambiguity problem: identical code can be secure or vulnerable depending on project-specific behavioral contracts, rendering global classification fundamentally inadequate. We propose Phoenix, a training-free multi-agent framework that resolves this ambiguity through Behavioral Contract Synthesis. Phoenix decomposes detection into three stages: a Semantic Slicer extracting minimal vulnerability-relevant context, a Requirement Reverse Engineer synthesizing Gherkin behavioral specifications encoding the security contract, and a Contract Judge evaluating code against these specifications via strict compliance checking. On PrimeVul Paired, Phoenix achieves F1 = 0.825 and Pair-Correct = 64.4%, surpassing RASM-Vul (F1 = 0.668) and VulTrial (F1 = 0.563) while using open-source models up to 48x smaller (7-14B vs. 671B). Ablation across 25 configurations demonstrates Gherkin specifications as the decisive driver (+0.09 to +0.35 F1). Error analysis reveals 18% of "False Positives" identify genuine security concerns in patched code, demonstrating that security is a relative property defined against behavioral contracts, not an absolute property of code syntax.

---


### 82. [FG$^2$-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control](https://arxiv.org/abs/2604.19021)

**<font color=#1a73e8>作者：</font>** Pingwei Sun, Yuxuan Hu, Jianchao Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention mechanisms have emerged as promising alternatives to softmax attention, offering linear-time complexity during inference. Recent advances such as Gated DeltaNet (GDN) and Kimi Delta Attention (KDA) have demonstrated that the delta rule, an online gradient descent update, enables superior associative recall compared to simple additive updates. While KDA refined the coarse head-wise decay gate into channel-wise decay, the learning rate $\beta_t$ in the delta update remains a scalar, limiting the model's capacity for dimension-specific adaptation. We introduce FG$^2$-GDN, which replaces the scalar $\beta_t$ with a channel-wise vector analogous to the transition from SGD to per-coordinate adaptive optimizers such as AdaGrad and Adam. We further propose FG$^2$-GDN+, which decouples the scaling for keys and values, enabling independent control of erasure strength and write strength. Experiments on synthetic and real-world benchmarks show that FG$^2$-GDN and its variant improve associative recall and long-context understanding over GDN and KDA, with comparable computational efficiency.

---


### 83. [On Accelerating Grounded Code Development for Research](https://arxiv.org/abs/2604.19022)

**<font color=#1a73e8>作者：</font>** Santosh Ganji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A major challenge for niche scientific and technical domains in leveraging coding agents is the lack of access to up-to-date, domain- specific knowledge. Foundational models often demonstrate limited reasoning capabilities in specialized fields and cannot inherently incorporate knowledge that evolves through ongoing research and experimentation. Materials scientists exploring novel compounds, communication engineers designing and evaluating new protocols, and bioengineering researchers conducting iterative experiments all face this limitation. These experts typically lack the resources to fine-tune large models or continuously embed new findings, creating a barrier to adopting AI-driven coding agents. To address this, we introduce a framework that gives coding agents instanta- neous access to research repositories and technical documentation, enabling real-time, context-aware operation. Our open-source im- plementation allows users to upload documents via this http URL and includes zed-fork, which enforces domain-specific rules and workflows. Together, these tools accelerate the integration of coding agents into specialized scientific and technical workflows

---


### 84. [Policy Gradient Primal-Dual Method for Safe Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2604.19024)

**<font color=#1a73e8>作者：</font>** Qiang Liu, Adrienne Kline, Ermin Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe Reinforcement Learning from Human Feedback (Safe RLHF) has recently achieved empirical success in developing helpful and harmless large language models by decoupling human preferences regarding helpfulness and harmlessness. Existing approaches typically rely on fitting fixed horizon reward models from human feedback and have only been validated empirically. In this paper, we formulate safe RLHF as an infinite horizon discounted Con- strained Markov Decision Process (CMDP), since humans may interact with the model over a continuing sequence of interactions rather than within a single finite episode. We propose two Safe RLHF algorithms that do not require reward model fitting and, in contrast to prior work assuming fixed-length trajectories, support flexible trajectory lengths for training. Both algo- rithms are based on the primal-dual method and achieve global convergence guarantees with polynomial rates in terms of policy gradient iterations, trajectory sample lengths, and human preference queries. To the best of our knowledge, this is the first work to study infinite horizon discounted CMDP under human feedback and establish global, non-asymptotic convergence.

---


### 85. [Analysis of AWW (Anganwadi Workers) Training Content, ILA (Incremental Learning Approach) Modules Following CDT (Component Display Theory)](https://arxiv.org/abs/2604.19032)

**<font color=#1a73e8>作者：</font>** Arka Majhi, Satish B. Agnihotri  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> POSHAN Abhiyan envisages capacity building of AWWs or frontline health workers through 21 training modules of ILA (Incremental Learning Approach), modularising the net learning content into smaller learning topics to help them perform their daily activities. It envisions building skilled AWWs, strengthening supervisory hierarchies, and improving coordination between AWWs (ICDS) services and health programs to achieve common goals such as increasing awareness, improving access to health and nutrition services, and reducing deaths and malnutrition. To better understand the contents of ILA literature, we conducted a content analysis by further breaking down the modules into content types such as facts, concepts, procedures, and principles. Then we framed learning objectives for teaching AWWs. We applied CDT (Component Display Theory by David Merrill) to map the contents with the desired learning objective, following the Specification of Objective chart. In this way, one can easily develop pedagogies from a new training literature. The challenges in framing learning objectives and pedagogies are: The AWWs do not have a (formal/scientific) nutrition and epidemiology background. Therefore, it is important to teach them through examples, familiar to them. AWWs are not evenly and structurally trained across districts. Training materials should be customized based on language, location, and prior knowledge. Delayed refresher courses render them underprepared for their jobs. To overcome these problems, we are developing an Android app based on gamified learning to provide refresher training to AWWs. Conducting content analysis, framing learning objectives, and developing pedagogical approaches will help conceptualize the gamified application.

---


### 86. [Intentional Updates for Streaming Reinforcement Learning](https://arxiv.org/abs/2604.19033)

**<font color=#1a73e8>作者：</font>** Arsalan Sharifnassab, Mohamed Elsayed, Kris De Asis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In gradient-based learning, a step size chosen in parameter units does not produce a predictable per-step change in function output. This often leads to instability in the streaming setting (i.e., batch size=1), where stochasticity is not averaged out and update magnitudes can momentarily become arbitrarily big or small. Instead, we propose intentional updates: first specify the intended outcome of an update and then solve for the step size that approximately achieves it. This strategy has precedent in online supervised linear regression via Normalized Least Mean Squares algorithm, which selects a step size to yield a specified change in the function output proportional to the current error. We extend this principle to streaming deep reinforcement learning by defining appropriate intended outcomes: Intentional TD aims for a fixed fractional reduction of the TD error, and Intentional Policy Gradient aims for a bounded per-step change in the policy, limiting local KL divergence. We propose practical algorithms combining eligibility traces and diagonal scaling. Empirically, these methods yield state-of-the-art streaming performance, frequently performing on par with batch and replay-buffer approaches.

---


### 87. [Explore Like Humans: Autonomous Exploration with Online SG-Memo Construction for Embodied Agents](https://arxiv.org/abs/2604.19034)

**<font color=#1a73e8>作者：</font>** Xu Chen, Shichao Xie, Zhining Gu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Constructing structured spatial memory is essential for enabling long-horizon reasoning in complex embodied navigation tasks. Current memory construction predominantly relies on a decoupled, two-stage paradigm: agents first aggregate environmental data through exploration, followed by the offline reconstruction of spatial memory. However, this post-hoc and geometry-centric approach precludes agents from leveraging high-level semantic intelligence, often causing them to overlook navigationally critical landmarks (e.g., doorways and staircases) that serve as fundamental semantic anchors in human cognitive maps. To bridge this gap, we propose ABot-Explorer, a novel active exploration framework that unifies memory construction and exploration into an online, RGB-only process. At its core, ABot-Explorer leverages Large Vision-Language Models (VLMs) to distill Semantic Navigational Affordances (SNA), which act as cognitive-aligned anchors to guide the agent's movement. By dynamically integrating these SNAs into a hierarchical SG-Memo, ABot-Explorer mirrors human-like exploratory logic by prioritizing structural transit nodes to facilitate efficient coverage. To support this framework, we contribute a large-scale dataset extending InteriorGS with SNA and SG-Memo annotations. Experimental results demonstrate that ABot-Explorer significantly outperforms current state-of-the-art methods in both exploration efficiency and environment coverage, while the resulting SG-Memo is shown to effectively support diverse downstream tasks.

---


### 88. [Plausible Reasoning and First-Order Plausible Logic](https://arxiv.org/abs/2604.19036)

**<font color=#1a73e8>作者：</font>** David Billington  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Defeasible statements are statements that are likely, or probable, or usually true, but may occasionally be false. Plausible reasoning makes conclusions from statements that are either facts or defeasible statements without using numbers. So there are no probabilities or suchlike involved. Seventeen principles of logics that do plausible reasoning are suggested and several important plausible reasoning examples are considered. There are 14 necessary principles and 3 desirable principles, one of which is not formally stated. A first-order logic, called Plausible Logic (PL), is defined that satisfies all but two of the desirable principles and reasons correctly with all the examples. As far as we are aware, this is the only such logic. PL has 8 reasoning algorithms because, from a given plausible reasoning situation, there are different sensible conclusions. This article is a condensation of my book `Plausible Reasoning and Plausible Logic' (PRPL), which is to be submitted. Each section of this article corresponds to a chapter in PRPL, and vice versa. The proofs of all the results are in PRPL, so they are omitted in this article.

---


### 89. [Generative Texture Filtering](https://arxiv.org/abs/2604.19039)

**<font color=#1a73e8>作者：</font>** Rongjia Zheng, Shangwei Huang, Lei Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a generative method for texture filtering, which exhibits surprisingly good performance and generalizability. Our core idea is to empower texture filtering by taking full advantage of the strong learned image prior of pre-trained generative models. To this end, we propose to fine-tune a pre-trained generative model via a two-stage strategy. Specifically, we first conduct supervised fine-tuning on a very small set of paired images, and then perform reinforcement fine-tuning on a large-scale unlabeled dataset under the guidance of a reward function that quantifies the quality of texture removal and structure preservation. Extensive experiments show that our method clearly outperforms previous methods, and is effective to deal with previously challenging cases. Our code is available at this https URL.

---


### 90. [Learning Lifted Action Models from Unsupervised Visual Traces](https://arxiv.org/abs/2604.19043)

**<font color=#1a73e8>作者：</font>** Kai Xi, Stephen Gould, Sylvie Thiébaux  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient construction of models capturing the preconditions and effects of actions is essential for applying AI planning in real-world domains. Extensive prior work has explored learning such models from high-level descriptions of state and/or action sequences. In this paper, we tackle a more challenging setting: learning lifted action models from sequences of state images, without action observation. We propose a deep learning framework that jointly learns state prediction, action prediction, and a lifted action model. We also introduce a mixed-integer linear program (MILP) to prevent prediction collapse and self-reinforcing errors among predictions. The MILP takes the predicted states, actions, and action model over a subset of traces and solves for logically consistent states, actions, and action model that are as close as possible to the original predictions. Pseudo-labels extracted from the MILP solution are then used to guide further training. Experiments across multiple domains show that integrating MILP-based correction helps the model escape local optima and converge toward globally consistent solutions.

---


### 91. [RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora](https://arxiv.org/abs/2604.19047)

**<font color=#1a73e8>作者：</font>** Hanjun Cho, Jay-Yoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing QA benchmarks typically assume distinct documents with minimal overlap, yet real-world retrieval-augmented generation (RAG) systems operate on corpora such as financial reports, legal codes, and patents, where information is highly redundant and documents exhibit strong inter-document similarity. This mismatch undermines evaluation validity: retrievers can be unfairly undervalued even when they retrieve documents that provide sufficient evidence, because redundancy across documents is not accounted for in evaluation. On the other hand, retrievers that perform well on standard benchmarks often generalize poorly to real-world corpora with highly similar and redundant documents. We present RARE (Redundancy-Aware Retrieval Evaluation), a framework for constructing realistic benchmarks by (i) decomposing documents into atomic facts to enable precise redundancy tracking and (ii) enhancing LLM-based data generation with CRRF. RAG benchmark data usually requires multiple quality criteria, but LLMs often yield trivial outputs. CRRF scores criteria separately and fuses decisions by rank, improving the reliability of generated data. Applying RARE to Finance, Legal, and Patent corpora, we introduce RedQA, where a strong retriever baseline drops from 66.4% PerfRecall@10 on 4-hop General-Wiki to 5.0-27.9% PerfRecall@10 at 4-hop depth, revealing robustness gaps that current benchmarks fail to capture. RARE enables practitioners to build domain-specific RAG evaluations that faithfully reflect real-world deployment conditions.

---


### 92. [CHRONOS: A Hardware-Assisted Phase-Decoupled Framework for Secure Federated Learning in IoT](https://arxiv.org/abs/2604.19053)

**<font color=#1a73e8>作者：</font>** Hung Dang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose CHRONOS, a hardware-assisted framework that decouples the cryptographic setup required for private gradient aggregation from the active training phase. CHRONOS executes a once-per-epoch server-relayed Diffie-Hellman key exchange during a device's idle window. It generates ephemeral keypairs and derives PRG keys entirely within an ARM TrustZone enclave, ensuring private keys never exist in Normal World memory. Pairwise secrets are sealed in the enclave, and Shamir secret shares of the ephemeral private key are distributed to peers. During training, clients mask gradients with a single stream-cipher evaluation and transmit them in one communication round. A hardware-backed round counter enforces single-use freshness. If clients drop out mid-round, the server reconstructs their masks from peer-held Shamir shares, preserving correct aggregation without repeating the round.
Evaluation on Rock Pi 4 devices using OP-TEE demonstrates that CHRONOS achieves OS-level compromise resistance and thwarts state-of-the-art gradient inversion attacks. It reduces active-phase aggregation latency by up to 74% compared to synchronous secure aggregation for 20 clients. The system maintains a persistent Secure World storage footprint of fewer than 700 bytes per device, scaling independently of model dimension.

---


### 93. [Evaluation of Winning Solutions of 2025 Low Power Computer Vision Challenge](https://arxiv.org/abs/2604.19054)

**<font color=#1a73e8>作者：</font>** Zihao Ye, Yung Hsiang Lu, Xiao Hu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The IEEE Low-Power Computer Vision Challenge (LPCVC) aims to promote the development of efficient vision models for edge devices, balancing accuracy with constraints such as latency, memory capacity, and energy use. The 2025 challenge featured three tracks: (1) Image classification under various lighting conditions and styles, (2) Open-Vocabulary Segmentation with Text Prompt, and (3) Monocular Depth Estimation. This paper presents the design of LPCVC 2025, including its competition structure and evaluation framework, which integrates the Qualcomm AI Hub for consistent and reproducible benchmarking. The paper also introduces the top-performing solutions from each track and outlines key trends and observations. The paper concludes with suggestions for future computer vision competitions.

---


### 94. [The Essence of Balance for Self-Improving Agents in Vision-and-Language Navigation](https://arxiv.org/abs/2604.19064)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Yuhan Liu, Jinjun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In vision-and-language navigation (VLN), self-improvement from policy-induced experience, using only standard VLN action supervision, critically depends on balancing behavioral diversity and learning stability, which governs whether the agent can extract a reliable learning signal for improvement. Increasing behavioral diversity is necessary to expose alternative action hypotheses but can destabilize policy-induced learning signals, whereas overly conservative stability constraints suppress exploration and induce early commitment, making reliable self-improvement difficult. To address this challenge, we propose Stability-Diversity Balance (SDB), a plug-and-play mechanism for balanced self-improvement in VLN. SDB expands each decision step into multiple latent behavioral hypotheses by applying controlled shifts in the instruction-conditioned hidden states, and then performs reliability-aware soft evaluation and aggregation to retain diverse yet instruction-consistent alternatives during learning. An explicit regularizer further constrains hypothesis interactions, preventing excessive drift or premature collapse of hypothesis diversity and stabilizing self-improvement without discarding training signals. Experiments on R2R, SOON, and REVERIE show consistent improvements; for example, on REVERIE val-unseen, SDB improves SPL from 33.73 to 35.93 and OSR from 51.07 to 54.25.

---


### 95. [Age-Dependent Heterogeneity in the Association Between Physical Activity and Mental Distress: A Causal Machine Learning Analysis of 3.2 Million U.S. Adults](https://arxiv.org/abs/2604.19066)

**<font color=#1a73e8>作者：</font>** Yuan Shan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical activity (PA) is widely recognized as protective against mental distress, yet whether this benefit varies systematically across population subgroups remains poorly understood. Using pooled data from ten consecutive annual waves of the U.S. Behavioral Risk Factor Surveillance System (2015-2024; n = 3,242,218), we investigate heterogeneity in the association between leisure-time PA and frequent mental distress (FMD, >=14 days/month) across age groups. Survey-weighted logistic regression reveals a striking age gradient: the adjusted odds ratio for PA ranges from 0.89 among young adults (18-24) to 0.50 among adults aged 55-64, with the protective association strengthening monotonically with age. Temporal analysis across all ten years shows that the young-adult PA effect has been eroding over the past decade, with the 18-24 OR reaching 1.01 (null) in both 2018 and 2024 -- paralleling the deepening youth mental health crisis. Causal Forest via Double Machine Learning independently identifies age as the dominant driver of treatment effect heterogeneity (feature importance = 0.39, 2.5x the next predictor). E-value sensitivity analysis, propensity score overlap checks, placebo tests, and imputation comparisons confirm the robustness of the findings. These results suggest that the well-documented exercise--mental health link may not generalize to the youngest adult population, whose distress appears increasingly driven by stressors that PA alone cannot mitigate.

---


### 96. [Product-of-Experts Training Reduces Dataset Artifacts in Natural Language Inference](https://arxiv.org/abs/2604.19069)

**<font color=#1a73e8>作者：</font>** Aby Mammen Mathew  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural NLI models overfit dataset artifacts instead of truly reasoning. A hypothesis-only model gets 57.7% in SNLI, showing strong spurious correlations, and 38.6% of the baseline errors are the result of these artifacts. We propose Product-of-Experts (PoE) training, which downweights examples where biased models are overconfident. PoE nearly preserves accuracy (89.10% vs. 89.30%) while cutting bias reliance by 4.71% (bias agreement 49.85% to 45%). An ablation finds lambda = 1.5 that best balances debiasing and accuracy. Behavioral tests still reveal issues with negation and numerical reasoning.

---


### 97. [S2MAM: Semi-supervised Meta Additive Model for Robust Estimation and Variable Selection](https://arxiv.org/abs/2604.19072)

**<font color=#1a73e8>作者：</font>** Xuelin Zhang, Hong Chen, Yingjie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning with manifold regularization is a classical framework for jointly learning from both labeled and unlabeled data, where the key requirement is that the support of the unknown marginal distribution has the geometric structure of a Riemannian manifold. Typically, the Laplace-Beltrami operator-based manifold regularization can be approximated empirically by the Laplacian regularization associated with the entire training data and its corresponding graph Laplacian matrix. However, the graph Laplacian matrix depends heavily on the prespecified similarity metric and may lead to inappropriate penalties when dealing with redundant or noisy input variables. To address the above issues, this paper proposes a new \textit{Semi-Supervised Meta Additive Model (S$^2$MAM) based on a bilevel optimization scheme that automatically identifies informative variables, updates the similarity matrix, and simultaneously achieves interpretable predictions. Theoretical guarantees are provided for S$^2$MAM, including the computing convergence and the statistical generalization bound. Experimental assessments across 4 synthetic and 12 real-world datasets, with varying levels and categories of corruption, validate the robustness and interpretability of the proposed approach.

---


### 98. [Cultural Newcomers Dining Across Borders: Need-Based Design Envision of Mixed Media Integration in MR for Foreign Menu Understanding and Ordering](https://arxiv.org/abs/2604.19088)

**<font color=#1a73e8>作者：</font>** Ying Zhang, Daoxin Chen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cultural newcomers (CNs), including new immigrants and international students, often encounter cognitive barriers and social anxiety, exacerbated by unfamiliar cultural terminology in daily interactions. This research examines these challenges in the context of ordering in foreign restaurants. Current translation tools have significant limitations in their information delivery with current media presentation methods. This research investigates the challenges and needs of CNs in ordering scenarios in a foreign restaurant through interview sessions (N = 13) and explored their expectation of mixed media integration (Image, Video, 3D Model) through a participatory design session that featured an immersive restaurant experience to support brainstorming. Based on qualitative analysis of participants' needs and expectations, the mixed media ordering assistant is conceptualized across 4 key dimensions: Key Features, User interaction, Media hierarchy, and Information presentation, with the objective of alleviating cultural barrier, linguistic barrier, cognitive load and improving the dining experience for CNs.

---


### 99. [Towards Scalable Lifelong Knowledge Editing with Selective Knowledge Suppression](https://arxiv.org/abs/2604.19089)

**<font color=#1a73e8>作者：</font>** Dahyun Jung, Jaewook Lee, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) require frequent knowledge updates to reflect changing facts and mitigate hallucinations. To meet this demand, lifelong knowledge editing has emerged as a continual approach to modify specific pieces of knowledge without retraining the entire model. Existing parameter editing methods struggle with stability during sequential edits due to catastrophic forgetting. While retrieval-based approaches are proposed to alleviate this issue, their applicability remains limited across various datasets because of high training costs. To address these limitations and enhance scalability in lifelong settings, we propose LightEdit. Our framework first selects relevant knowledge from retrieved information to modify the query effectively. It then incorporates a decoding strategy to suppress the model's original knowledge probabilities, thereby enabling efficient edits based on the selected information. Extensive experiments on ZSRE, Counterfact, and RIPE benchmarks demonstrate that LightEdit outperforms existing lifelong knowledge editing methods. Furthermore, by minimizing training costs, LightEdit achieves cost-effective scalability, enabling easy adaptation to various datasets.

---


### 100. [Dual-Guard: Dual-Channel Latent Watermarking for Provenance and Tamper Localization in Diffusion Images](https://arxiv.org/abs/2604.19090)

**<font color=#1a73e8>作者：</font>** JinFeng Xie, Chengfu Ou, Peipeng Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of diffusion-based generative models has intensified concerns over the attribution and integrity of AI-generated content (AIGC). Existing single-domain watermarking methods either fail under regeneration, remain vulnerable to black-box reprompting that enables adversarial framing, or provide no spatial evidence for tampered regions. We propose Dual-Guard, a dual-channel latent watermarking framework for practical provenance verification, framing resistance, and region-level tamper localization. Dual-Guard combines two complementary anchors: a Gaussian Shading watermark in the initial diffusion noise as a global provenance signal, and a Latent Fingerprint Codec in the final denoised latent as a structured content anchor. Reprompting tends to preserve the former while breaking the latter, whereas localized edits disturb the content anchor only in tampered regions. In Full mode on a 2,400-sample benchmark, Dual-Guard keeps clean-image authentication false rejection and tamper false alarm below one half of one percent, while maintaining near-complete detection under reprompting, diffusion editing, and eight local tampering attacks.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
