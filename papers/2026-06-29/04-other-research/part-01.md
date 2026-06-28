# 📦 其他研究 | 2026年06月29日

> 本类共 **245** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-245](./part-05.md)

---

### 1. [HierBias: Context-Conditioned Hierarchical Media Bias Detection with Multi-Task Type Classification](https://arxiv.org/abs/2606.26100)

**<font color=#1a73e8>作者：</font>** Kaining Li, Ruichen Yan, Yuxin Dong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Media bias detection is a critical task for ensuring fair and balanced information dissemination, yet existing sentence-level approaches classify each sentence independently, ignoring inter-sentence contextual signals that human annotators naturally exploit. We present \textbf{HierBias}, a hierarchical context-conditioned media bias detector that formally models document context in bias prediction. We introduce the \emph{context-conditioned bias probability} and prove theoretically that leveraging document context strictly reduces the Bayes error of sentence-level classification when inter-sentence mutual information is non-zero. A multi-task generalization bound further establishes that jointly training binary bias detection and fine-grained bias type classification improves sample efficiency on small annotated corpora. Architecturally, HierBias pairs a sentence-level RoBERTa encoder with a cross-sentence Transformer aggregator and dual output heads for binary detection and four-class type classification. Evaluated on BABE and BASIL, HierBias achieves 0.853 F1 and 0.723 MCC, surpassing the state-of-the-art bias-detector by $+2.6\%$ F1 and $+4.3\%$ MCC (McNemar's test, $p < 0.05$). Ablation experiments confirm that each theoretical component contributes independently and consistently.

---


### 2. [From Lexicon to AI: A Structured-Data Pipeline for Specialized Conversational Systems in Low-Resource Languages](https://arxiv.org/abs/2606.26112)

**<font color=#1a73e8>作者：</font>** Siddhant Hitesh Mantri, Dhara Gorasiya, Malhar Kulkarni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource languages face a critical challenge in AI development: creating specialized conversational systems without access to massive training corpora. We present a systematic methodology for transforming structured linguistic resources into specialized AI systems, demonstrating that expert-curated lexical databases can serve as effective foundations for conversational AI development. Our approach converts Hindi WordNet into 1.25 million diverse instruction-response pairs, fine-tunes a 12B-parameter language model using resource-efficient LoRA with 4-bit quantization. Evaluation through a Hindi language learning chatbot demonstrates that structured-knowledge-based systems achieve superior pedagogical effectiveness (91.0 vs. 79.4-83.6 for general-purpose models) while maintaining competitive semantic performance and exceptional consistency. The complete pipeline demonstrates a proof-of-concept methodology using Hindi for developing specialized AI systems for any languages with WordNet resources. This work addresses the critical gap in AI accessibility for low-resource languages, offering a practical alternative to corpus-intensive approaches and potentially enabling specialized AI development for the hundreds of languages with existing WordNet resources.

---


### 3. [Physics-guided Convolutional Neural Network for Domain Growth Prediction in Systems with Conserved Kinetics](https://arxiv.org/abs/2606.26128)

**<font color=#1a73e8>作者：</font>** Vijay Yadav, Madhu Priya, Manish Dev Shrimali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The spatiotemporal evolution of many physical, chemical, and biological systems is described by nonlinear partial differential equations (PDEs). Recently, deep neural network-based surrogate models have gained increasing interest as efficient alternatives to computationally expensive traditional numerical solvers. In this work, we propose an attention-based, physics-guided convolutional neural network as a surrogate model to learn the microstructural evolution of such systems. We train the model to accurately predict the full time-evolution of phase separation in binary mixtures governed by the Cahn-Hilliard equation. We show that predictions from our trained surrogate model remain stable and accurate over long-time rollouts for both critical and off-critical mixtures and preserve the mixture composition throughout evolution. We also show that our model accurately captures the growth of domain size and is consistent with the Lifshitz-Slyozov domain-growth law. The prediction results demonstrate the effectiveness of the proposed framework for modeling systems with conserved kinetics and can be extended to other complex dynamical systems.

---


### 4. [Detecting and Controlling Sycophancy with Cascading Linear Features](https://arxiv.org/abs/2606.26155)

**<font color=#1a73e8>作者：</font>** Maty Bohacek, Rishub Jain, Nicholas Dufour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpreting and controlling model behaviors through activation steering methods requires many pairs of contrastive samples that clearly exhibit desired or undesired behavior. These data pairs determine the degree to which interpretability frameworks can reliably detect model features responsible for a behavior, and therefore the ability to steer models toward or away from such behavior. In this work, we present an iterative data generation pipeline that isolates cascading linear features responsible for a behavior. Specifically, we show how moving beyond simple binary pairs of samples, and instead isolating samples that show degrees of features that scale linearly with behavior, allows for better disentanglement of features. We focus on detecting and steering away from sycophancy -- the tendency of language models to prioritize user validation. We demonstrate that sycophancy features discovered through cascading samples form linearly separable subspaces, and allow for selection of model activations that more clearly correspond to the desired behavior than baseline approaches. We also evaluate their ability to enable detection, deterministic scoring, and robust steering, and see that they either match or outperform LLM-as-a-judge and system prompting baselines while providing lower computational demand and more interpretability guarantees. Code & Data: this https URL

---


### 5. [Kiko: Programming Agents to Enact Interaction Protocols](https://arxiv.org/abs/2606.26156)

**<font color=#1a73e8>作者：</font>** Samuel H. Christie V, Munindar P. Singh, Amit K. Chopra  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Realizing a multiagent system involves implementing member agents who interact based on a protocol while making decisions in a decentralized manner. Current programming models for agents offer poor abstractions for decision making and fail to adequately bridge an agent's internal decision logic with its public decisions.
We present Kiko, a protocol-based programming model for agents. To implement an agent, a programmer writes one or more decision makers, each of which chooses from among a set of valid decisions and makes mutually compatible decisions on what messages to send. By completely abstracting away the underlying communication service and by supporting practical decision-making patterns, Kiko enables agent developers to focus on business logic. We provide an operational semantics for Kiko and establish that Kiko agents are protocol compliant and able to realize any protocol enactment.

---


### 6. [Life After Benchmark Saturation: A Case Study of CORE-Bench](https://arxiv.org/abs/2606.26158)

**<font color=#1a73e8>作者：</font>** Nitya Nadgir, Sayash Kapoor, Kangheng Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a benchmark's accuracy saturates, it is often retired and replaced with a more challenging version. We show that this approach privileges accuracy and misses the opportunity to study six other key dimensions of agent performance: construct validity issues such as shortcuts, out-of-distribution generalizability, efficiency, reliability, the relative importance of the model versus the scaffold, and uplift from human-agent collaboration. We use CORE-Bench Hard, a benchmark for computational reproducibility of scientific code, as a case study to demonstrate that measuring agents along these dimensions yields meaningful insights into agent performance even after accuracy saturates. First, we surface threats to construct validity in CORE-Bench Hard that are difficult to anticipate with less capable agents. We introduce an improved benchmark, CORE-Bench v1.1, and an out-of-distribution task suite, CORE-Bench OOD. Second, we find that despite accuracy saturation, CORE-Bench v1.1 remains useful for measuring efficiency, reliability, model performance, and scaffold performance. Finally, we conduct a small-scale randomized experiment to measure uplift from human-agent collaboration on real-world computational reproducibility tasks. We find a statistically significant speedup by about a factor of two -- likely underestimated due to one-fifth of human-only reproductions reaching the time limit before completing -- and describe various other findings. Together, our contributions present a more rigorous alternative to the dominant accuracy-centric evaluation paradigm.

---


### 7. [Refusal Lives Downstream of Persona in Chat Models](https://arxiv.org/abs/2606.26161)

**<font color=#1a73e8>作者：</font>** Viola Zhong, Qirui Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear directions in activation space have been identified for both refusal and persona traits in instruction-tuned chat models, but the two have been studied as separate mechanisms. We show they interact: a compliant persona gates refusal. In Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, we extract a compliant model-persona direction and a refusal direction and intervene on both. Compliant persona steering suppresses refusal -- in Llama, the refusal rate falls from 97% to 2%. Reintroducing the refusal direction partially restores refusal at late layers but not at early ones. Projecting out the persona direction in a late-layer window restores it to baseline; projecting out a random direction does not. Refusal is therefore gated at the late-layer expression stage, downstream of where it is computed. Treating refusal as a single isolated direction misses its dependence on persona.

---


### 8. [Predicting Fruit Quality with a Hybrid Machine Learning and Image Processing Approach](https://arxiv.org/abs/2606.26165)

**<font color=#1a73e8>作者：</font>** Amir Reza Hashemi, Shahram Amiri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fruit spoilage is a significant issue in agriculture, leading to substantial economic losses. Addressing this, our study introduces a hybrid approach combining image processing and deep learning to assess fruit freshness. We developed an image processing algorithm that quantifies spoilage on a scale from 0 (fully fresh) to 100 (fully rotten). Alongside, we trained a convolutional neural network (CNN) to perform binary classification (fresh or rotten) using a large dataset of fruit images. The outcomes of both methods were synthesized using logistic regression to enhance the accuracy of freshness predictions. Subsequently, this logistic regression model was utilized to enable the image processing algorithm to provide binary classification based on its percentage output, thus eliminating the need for the CNN in real-time applications. Our approach, which does not require high computational resources, achieved real-time performance and was validated with over 90% accuracy on a dataset comprising apples and oranges. The primary limitation lies in the requirement for fruits to be isolated on a background that must be either white or transparent, suggesting future improvements could include advanced segmentation models to automate background removal. This study's results highlight the potential of integrating simple image processing techniques with machine learning to provide practical solutions in the agricultural sector.

---


### 9. [Implementation of reinforcement learning in chemical reaction networks: application to phototaxis as curiosity-driven exploration](https://arxiv.org/abs/2606.26168)

**<font color=#1a73e8>作者：</font>** Ruyi Tang, Grégoire Sergeant-Perthuis, David Colliaux  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Living systems navigate environments using noisy and incomplete sensory signals. In unicellular algae, phototaxis is often modeled as a mechanistic run--tumble process driven by stimulus--response rules. However, such descriptions overlook how organisms actively sample their environment to reduce sensory ambiguity. From a minimal cognition perspective, we reframe this navigation as a subjective, information-driven sensorimotor process. To this end, we propose a framework linking a Partially Observable Markov Decision Process (POMDP) with biochemical reaction dynamics. Environmental variables are hidden, while the cell updates a minimal internal state from each observation through a memoryless Bayesian step. These internal dynamics balance orienting toward light with exploratory reorientation and can be implemented through Chemical-Reaction-Network Ordinary Differential Equations (CRN--ODEs). Our model includes a biophysical observation process for photoreception and a chemically computable polynomial bound on information gain. Using Inverse Reinforcement Learning (IRL) on 30 experimentally recorded Chlamydomonas trajectories, we infer the behavioral objective consistent with observed phototactic motion and benchmark the resulting dynamics with standard Stochastic Simulation Algorithm (SSA) baselines. Our model reproduces the empirical alignment-to-light distribution, comparable to objective SSA baselines on this dataset. Within this framework, run--tumble alternation emerges as an information-acquisition strategy: tumbling reorients the cell to sample new sensory configurations and resolve sensor ambiguity, demonstrating how intracellular biochemical networks can support adaptive information-seeking behavior in cellular navigation.

---


### 10. [Neural Architecture Search for Generative Adversarial Networks: A Comprehensive Review and Critical Analysis](https://arxiv.org/abs/2606.26169)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Moataz Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has emerged as a pivotal technique in optimizing the design of Generative Adversarial Networks (GANs), automating the search for effective architectures while addressing the challenges inherent in manual design. This paper provides a comprehensive review of NAS methods applied to GANs, categorizing and comparing various approaches based on criteria such as search strategies, evaluation metrics, and performance outcomes. The review highlights the benefits of NAS in improving GAN performance, stability, and efficiency, while also identifying limitations and areas for future research. Key findings include the superiority of evolutionary algorithms and gradient-based methods in certain contexts, the importance of robust evaluation metrics beyond traditional scores like Inception Score (IS) and Fréchet Inception Distance (FID), and the need for diverse datasets in assessing GAN performance. By presenting a structured comparison of existing NAS-GAN techniques, this paper aims to guide researchers in developing more effective NAS methods and advancing the field of GANs.

---


### 11. [LCG: Long-Context Consistent Image Generation with Sparse Relational Attention](https://arxiv.org/abs/2606.26171)

**<font color=#1a73e8>作者：</font>** Zihao Wang, Yijia Xu, Haoze Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generation models achieve impressive quality in single-image synthesis, but often fail to maintain consistency across sequential outputs, as required in comics, storyboards, and visual narratives. We propose Long-Context Generation (LCG), a framework for long-context multi-image text-to-image generation, to improve consistency and scalability in long-context multi-image generation. LCG employs the Sparse Relational Attention (SRA) mechanism to selectively attend to core features across extended visual contexts, ensuring that the propagation of semantic and layout information remains computationally tractable. To enforce semantic alignment, we introduce the Routing Consistency Constraint (RCC), which leverages identity-aware masks to align structural patterns across generation branches, effectively mitigating drift in appearance even in complex multi-character scenes. To support training and evaluation in this setting, we construct the Long-Context Consistency Dataset (LCCD), a large-scale synthetic dataset comprising character-centric multi-image sequences spanning varied situational contexts. LCCD contains 600K training sequences and a separate 1K test set, with each sequence containing 6 to 20 images. The experiments demonstrate that LCG outperforms the compared baselines in prompt alignment and character consistency for long-context image generation, including multi-character scenes.

---


### 12. [KG-TRACE: A Neuro-Symbolic Framework for Mechanistic Grounding in Antimicrobial Resistance Prediction](https://arxiv.org/abs/2606.26179)

**<font color=#1a73e8>作者：</font>** Naman Garg, Sarika Jain, Sourav Yadav 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While WGS-based AMR prediction has reached high accuracy, existing models lack a mechanism to ground neural attributions in established biological pathways. We present KG-TRACE, a novel neuro-symbolic framework that integrates the WHO mutation knowledge graph (KG) as a structured biological constraint on a neural genomic model. Unlike existing methods that learn statistical patterns in isolation, KG-TRACE fuses genomic features and RotatE-based KG embeddings through a learned epistemic trust gate, dynamically weighting neural evidence against symbolic biological knowledge.
Evaluated on the CRyPTIC M. tuberculosis cohort, KG-TRACE achieves an AUROC of 0.9760 for isoniazid, achieving competitive accuracy while its primary value lies in symbolic grounding, not predictive uplift. More importantly, we introduce the Biological Grounding Ratio (BGR), a dataset-level metric that quantifies alignment between neural attributions and established biology. Our framework achieves a 92.5% symbolic coverage of isoniazid-resistant predictions and effectively identifies MDR co-occurrence artifacts by issuing laboratory follow-up flags for 'UNCERTAIN' cases. We demonstrate that neuro-symbolic grounding provides a verifiable audit trail for clinicians, bridging the gap between predictive accuracy and clinical trust.

---


### 13. [Clue-Guided Money Laundering Group Discovery](https://arxiv.org/abs/2606.26189)

**<font color=#1a73e8>作者：</font>** Boyang Wang, Jianing Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Money Laundering Group Discovery (MLGD) aims to identify hidden criminal groups and recover their complete structures in large-scale financial networks. Existing graph anomaly detection methods mainly produce node-level risk alerts, while global group discovery methods passively search for suspicious groups over the whole network. Both are mismatched with real Anti-money-laundering (AML) investigations, where analysts usually start from a concrete clue and gradually expand the investigation to recover the responsible group. To address this gap, we propose Clue-Guided Group Discovery (CGGD), where a laundering group is progressively recovered from an initial clue set through analyst interaction. We further propose Clue2Group, a framework that first constructs a compact local investigation context to reduce noise and preserve chain-like and cycle-like laundering structures. It then estimates a clue-conditioned local risk field with a multi-semantic local-temporal GNN, and finally integrates risk, structural, and prior-pattern evidence to recover a coherent laundering group. Experiments on two large-scale AML benchmarks show that Clue2Group provides a practical clue-driven analysis framework for AML investigations, offering a feasible step toward bridging the gap between graph-based AML research and real investigation workflows.

---


### 14. [Federated Hash Projected Latent Factor Learning](https://arxiv.org/abs/2606.26192)

**<font color=#1a73e8>作者：</font>** Jialan He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hash Learning (HL) is an efficient representation learning approach that maps real-valued data into compact binary representations. Traditional HL methods typically require users to upload personal data to a central server, which is incompatible with increasingly stringent data security regulations. Federated Learning (FL) provides a decentralized paradigm for learning globally optimal models without centralizing private data. However, most FL methods rely on transmitting large-scale real-valued gradient information, leading to high communication overhead and potential privacy risks. Integrating HL into FL is a promising solution. Nevertheless, existing HL methods suffer from limited representational capacity of binary codes, which may degrade model accuracy. To address this challenge, we propose a Federated Hash Projected Latent Factor (FHPLF) model. FHPLF introduces three key innovations: (a) replacing real-valued gradient matrices with binary gradient-like matrices, significantly reducing computation, storage, and communication costs while enhancing privacy protection; (b) leveraging Projected Hamming Distance for similarity modeling, which captures the importance of individual binary bits to improve representation capability; and (c) proposing a Secure Binary Gradient Reassembly and Privacy-Enhanced Upload (SBG-PEU) strategy to further reduce the risk of user interaction leakage during transmission. Extensive experiments on four real-world datasets demonstrate that FHPLF consistently outperforms state-of-the-art HL and FL methods, achieving a favorable trade-off among accuracy, efficiency, and privacy preservation.

---


### 15. [Self-Supervised Tree-level Biomass Estimation in Urban Environments From Airborne LiDAR and Optical Observations](https://arxiv.org/abs/2606.26194)

**<font color=#1a73e8>作者：</font>** Jose Bermudez, Zilong Zhong, Dominic Cyr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban tree biomass remains less spatially explicitly quantified than biomass in managed forests because many estimates rely on inventories or coarse products that cannot resolve individual crowns or fine-scale heterogeneity. We present a crown-level above-ground biomass (AGB) framework for an 810~km$^2$ landscape in Ontario, Canada, using leaf-off airborne LiDAR (8--10~pulses~m$^{-2}$) and near-infrared RGB orthophotography (0.16--0.20~m) from 2018 and 2023. A dual-stream cross-attention network trained on rule-based pseudo-labels produced semantic marks for buildings, needleleaf trees, and deciduous trees, supporting crown delineation and functional-type assignment. On independently annotated withheld tiles, global/mean precision, recall, and Dice scores were 0.86, 0.83, and 0.84. Crowns were delineated with multiscale watershed segmentation in mapped tree areas, and AGB was estimated from a crown area--height power-law proxy calibrated to species-specific allometry (Lambert et al., 2005) for 21,921 inventory trees. For 18,713 inventory--segment matched pairs from a 90,726-tree held-out test set, AGB prediction achieved $R^2=0.609$ using inventory crown geometry and $R^2=0.570$ under operational segmentation, identifying crown delineation as the remaining uncertainty source. Aggregated to 30~m, estimates yielded total AGB stocks of 1.73~Tg in 2018 and 1.81~Tg in 2023 (811--850~Gg~C), local densities up to ${\sim}140$~Mg~ha$^{-1}$ along the Niagara Escarpment, and a net carbon gain of 39~Gg~C over five years. Deep-ensemble uncertainty maps highlighted high-epistemic-uncertainty areas linked to underrepresented land covers and guided assignment of uncertain crowns to a pooled allometric equation. The framework uses standard provincial data, requires no manual annotation, and produces a public bitemporal crown-level AGB database for trees outside forests at management-relevant resolution.

---


### 16. [Statistical and Structural Approaches to Algorithmic Fairness](https://arxiv.org/abs/2606.26200)

**<font color=#1a73e8>作者：</font>** Antonio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning systems have outgrown their origins as isolated predictive constructs, evolving into complex socio-technical architectures that actively mediate human opportunity. As algorithms increasingly determine access to economic and social opportunities, it has become widely recognized that these systems are deeply embedded with the structural inequalities and prejudices of their environments. The field of algorithmic fairness emerged in response to the growing recognition that models optimized for predictive accuracy can systematically disadvantage marginalized groups. Early mitigation strategies, however, rested on fragile simplifications that limited their effectiveness in complex socio-technical environments. This thesis identifies and addresses two fundamental limitations of contemporary fairness paradigms: the reliance on deterministic point estimates for auditing and the treatment of individuals as isolated entities devoid of structural context.

---


### 17. [Topology-Informed Neural Networks for Flood Detection in Optical and Synthetic Aperture Radar Imagery](https://arxiv.org/abs/2606.26204)

**<font color=#1a73e8>作者：</font>** Sophia Li, Max Zhao, Raghu G. Raj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Floods frequently impact regions around the world. Rapid and accurate flood detection is crucial for emergency response and timely mitigation of human and economic loss. The expanding availability of satellite data and advances in artificial intelligence have enhanced monitoring of environmental hazards, but many flood events remain challenging to detect because cloud cover obscures optical satellite imagery. Rambour et al. introduced the SEN12-FLOOD dataset and extracted per-image features using a ResNet-50 convolutional neural network backbone, then fed these features into a gated recurrent unit network to show that temporal information can substantially improve accuracy compared to single-image baselines. More recently, Chamatidis et al. showed that a vision transformer can achieve strong performance with popular convolutional architectures. However, these models typically function as opaque black boxes, making it difficult to interpret their decision boundaries, learned features, and internal reasoning, especially in safety-critical domains like remote sensing. In contrast, topological data analysis (TDA) provides a mathematically grounded framework for capturing global structural features of data. TDA has emerged as a powerful tool for analyzing complex imagery, especially imagery with geometrically interpretable structures, of which floods are a prime candidate. In this work, we systematically evaluate topological descriptors for flood detection using the open-source SEN12-FLOOD dataset. By extracting topological features from each image and incorporating them into neural networks, we demonstrate that topological descriptors carry meaningful flood signals independently and complement existing networks to yield more robust and interpretable flood detection systems.

---


### 18. [Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem](https://arxiv.org/abs/2606.26211)

**<font color=#1a73e8>作者：</font>** Jin Gao, Maria Gorskikh, Pradyumna Chari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> NANDini (Networked Agents Natural Distillation of Interconnected Nodal Intelligence) envisions an automated ecosystem where intelligent agents independently create, process, and exchange data to drive decisions at scale. Realizing this vision requires infrastructure beyond agent discovery and communication: agents must be able to advertise, evaluate, and verify the datasets they hold.
Current protocols, including NANDA for federated registry and A2A and MCP for inter-agent messaging, address identity and communication but provide no mechanism for structured data exchange. Existing enterprise data-sharing frameworks, such as IDS-RAM, Gaia-X, and Ocean Protocol, assume human-in-the-loop governance that is incompatible with autonomous, real-time agent interactions.
We introduce Data Facts, a core NANDini concept: a lightweight JSON metadata schema that bridges agent discovery and data access through a single pointer, `data_facts_url`, added to an existing Agent Facts registry record. The linked document encodes dataset identity, access tier, whether public, semi-private, or private, endpoint, a time-to-live for freshness validation, and a SHA-256 integrity checksum.
For private and semi-private data, we implement a three-layer security pipeline: JWT authentication, capability-scoped gateway authorization, and an A2A credential delegation protocol. Across 840 decision-making evaluations, data-informed agents achieve 100% accuracy versus 35.2% without data access (p < 0.001); TTL enforcement reduces stale-data errors from 37.6% to 8.8%; checksum verification achieves 100% corruption detection at all injection rates; and the security pipeline blocks all 46 forgery attempts with zero data leakage.

---


### 19. [A General Framework for Learning Algebraic Properties from Cayley Graphs using Graph Neural Networks](https://arxiv.org/abs/2606.26212)

**<font color=#1a73e8>作者：</font>** Tal Weissblat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Graph Neural Network (GNN) framework for predicting the solvability of finite groups from their Cayley graph representations was introduced in [1]. In the present work, we generalize this approach and develop a property-independent framework for learning algebraic properties of finite groups directly from Cayley graphs. As representative case studies, we consider abelianity, nilpotency, and solvability. Using a common GNN architecture and training pipeline, we investigate the extent to which algebraic structure can be recovered from graph-based representations alone. Results on a collection of finite groups drawn from several families demonstrate that the framework successfully learns and distinguishes multiple algebraic properties from their associated Cayley graphs. These findings suggest that substantial algebraic information is encoded in graph representations and can be extracted through GNNs. More broadly, the proposed framework provides a proof of concept for applying graph representation learning to the study of algebraic properties of finite groups.

---


### 20. [CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](https://arxiv.org/abs/2606.26216)

**<font color=#1a73e8>作者：</font>** Jintao Huang, Fengqing Jiang, Radha Poovendran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present CyberChainBench, a benchmark for evaluating LLM-based agents on smart contract security across three complementary tasks: vulnerability detection, exploit generation, and patch synthesis. Built from 541 real-world exploit incidents from DeFiHackLabs spanning 9 EVM chains, the benchmark provides end-to-end on-chain evaluation where agents interact with historical blockchain state through isolated evaluation environments orchestrated by Harbor, using tools to read code, trace transactions, and validate exploits on mainnet forks. Each case is anchored to a specific block and includes structured ground truth covering vulnerability type, localization, and attacker profit. Exploits are graded by economic impact on historical forks; patches are validated by replaying historical attacks and legitimate transactions as fail-to-pass test oracles on a proxy-upgradeable subset. We define a five-type vulnerability taxonomy and evaluate multiple agent--model configurations. Results reveal a clear difficulty gradient: the best configuration scores 37.5% on detection, 43.7% on exploitation, but only 23.4% on patching, with the top agent (Codex with GPT-5.5) realizing \$57.4M in total exploit profit across the 200-case exploit set at a cost of $2.39 per case.

---


### 21. [Fast LeWorldModel](https://arxiv.org/abs/2606.26217)

**<font color=#1a73e8>作者：</font>** Yuntian Gao, Xiangyu Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs), including recent LeWorldModel (LeWM), have become a promising foundation for reconstruction-free visual world models. For visual planning, however, LeWM evaluates candidate action sequences by repeatedly applying a local one-step latent transition model. This autoregressive rollout makes planning computationally expensive and exposes the predicted trajectory to accumulated latent errors as the horizon grows. We propose Fast LeWorldModel (Fast-LeWM), a fast latent world model that replaces repeated local rollout with action-prefix prediction. Given the current latent and a candidate action sequence, Fast-LeWM encodes its prefixes and predicts the future latents reached after executing those prefixes in parallel. By making action prefixes the basic prediction unit, Fast-LeWM directly models action effects accumulated to different extents over multiple horizons. This prefix-level supervision forces the model to learn how states continuously evolve under different action prefixes, rather than only fitting one-step state transitions. During planning, the predictor can use the last prefix token from the encoded action sequence to evaluate the corresponding future latent without explicitly rolling through each intermediate imagined state. Across multiple tasks, Fast-LeWM improves average success over LeWM while substantially reducing planning time, achieving lower open-loop latent loss whose growth becomes significantly slower as the rollout horizon increases.

---


### 22. [Dataset Usage Inference without Shadow Models or Held-out Data](https://arxiv.org/abs/2606.26257)

**<font color=#1a73e8>作者：</font>** Wojciech Łapacz, Stanisław Pawlak, Jan Dubiński 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How much of my data was used to train a machine learning model? Dataset Usage Inference (DUI) aims to answer this by estimating what fraction of a dataset contributed to a model's training. However, existing DUI methods rely on assumptions that rarely hold in practice: they require training expensive shadow models to imitate the target model, and they assume access to both known training samples and an in-distribution held-out set confirmed to be absent from training. These conditions make current approaches impractical for modern large models and real data ownership disputes. We introduce a practical DUI framework that removes these constraints. Our method requires neither shadow models nor real held-out data. Instead, it generates synthetic non-member samples, extracts diverse membership signals, and casts DUI as a mixture proportion estimation problem to estimate what share of the candidate dataset was used during training. Experiments on large image generative models show that our method reliably quantifies dataset usage, providing a practical tool for data owners to determine how much of their data was used to train a model.

---


### 23. [A multi-task spatiotemporal deep neural network for predicting penetration depth and morphology in laser welding](https://arxiv.org/abs/2606.26260)

**<font color=#1a73e8>作者：</font>** Sen Li, Haichao Cui, Chendong Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In laser penetration welding, the assessment of penetration state and weld seam morphology plays a crucial role in determining the weld quality. This paper presents a comprehensive introduction of the innovative muti-task deep learning model that has the capability to predict penetration state, depth, and weld seam morphology with high accuracy. The monitoring platform relies on weld pool images captured during the laser welding process using a complementary metal-oxide-semiconductor camera. The proposed model integrates spatiotemporal features extracted from top weld pool images along with welding parameters, establishing a deep learning framework based on convolutional neural networks and state space models for more efficient extraction and processing of spatial-temporal information. Furthermore, a reliable method for constructing the dataset is proposed to enhance both robustness and generalization capability of the developed model. Validation results on the test set demonstrate that prediction accuracy for penetration state can reach 99.35%, while prediction error for penetration depth is 1.79 millimeter, and accuracy of reconstructing the weld cross-section is 95.65%. This study provides new insights and methodologies for in-situ quality control strategies in laser penetration welding systems.

---


### 24. [Accelerating Skill Assessment in Chess: A Drift-Diffusion-Enhanced Elo Rating System](https://arxiv.org/abs/2606.26267)

**<font color=#1a73e8>作者：</font>** Tianyuan Zhou, Zhizheng Fu, Tianming Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rating systems such as Elo serve as the gold standard for matchmaking in competitive chess. However, they inherently suffer from response lag due to their exclusive reliance on match outcomes, neglecting the granular quality of gameplay. Nevertheless, incorporating move-by-move information into rating adjustments presents a significant challenge given the substantial noise and the vastness of the game-state space. To address this, we propose the Drift-Diffusion-Enhanced Elo Rating System (DD-Elo), a novel skill assessment framework inspired by the drift diffusion model (DDM) from cognitive neuroscience. By modeling skill expression as a decision-making process, our model integrates move-level data to capture rapid skill fluctuations. We provide a rigorous mathematical derivation proving that DD-Elo maintains a bounded deviation from the traditional Elo system, ensuring theoretical alignment. Extensive experiments demonstrate that DD-Elo adapts to skill changes faster than Elo. Our findings suggest that DD-Elo offers an explainable, highly responsive, and backward-compatible solution for chess rating ecosystems. The implementation code is publicly available at this https URL .

---


### 25. [Equivariance and Augmentation for Bayesian Neural Networks](https://arxiv.org/abs/2606.26273)

**<font color=#1a73e8>作者：</font>** Miaowen Dong, Axel Flinth, Jan E. Gerken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symmetries are important for many deep learning tasks, ranging from applications in the sciences to medical imaging. However, there is an ongoing debate about whether to impose symmetry constraints on the neural network architecture (yielding equivariant neural networks) or learn them from augmented training data. Although equivariant networks are well-studied theoretically, much less is known about data augmentation, since analyzing augmentation requires control over the training dynamics. Inspired by recent results that show that augmented infinite deep ensembles are exactly equivariant, we study data augmentation for Bayesian neural networks (BNNs) trained with variational inference. We focus on variational distributions in the exponential family and derive conditions under which exact equivariance is reached. We furthermore obtain bounds on the equivariance error and introduce three novel symmetrization techniques which boost the effect of data augmentation in this setting. We conduct extensive numerical experiments which show that one of our symmetrization methods (orbit expansion) outperforms the baseline in both equivariance and overall performance. Our code is available at this http URL

---


### 26. [Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps](https://arxiv.org/abs/2606.26276)

**<font color=#1a73e8>作者：</font>** Yeeun Jo, Shahanaasree Sivakumar, Mahnoor Jameel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While human factors in the privacy of fertility tracking apps -- health trackers that record user's menstrual or pregnancy data -- has been the subject of extensive study, little attention has been paid to the technical aspects of apps' data handling practices. We conduct a network-based measurement study of a corpus of 20 Android fertility tracking apps from the Google Play Store, focusing on how user data is shared with third party advertising services. After systematizing app features, we conduct a series of standardized user interactions across all apps in an environment that records TLS-stripped network traffic. In a subset of apps (n=5) we identify explicit leakage of user health data as well implicit leakage through highly targeted contextual advertising URL's. Equally importantly, we observe additional apps that use an ad-based monetization model without apparent leakage of user data, as well as several apps the interact only minimally with ad services. These findings provide technical grounding for widespread user concerns, but also underscore the importance of consumer choice in the privacy implications of app-based fertility tracking.

---


### 27. [Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning](https://arxiv.org/abs/2606.26279)

**<font color=#1a73e8>作者：</font>** Junfeng Xia, Wendu Li, Mengjiao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to analyze budget-constrained task allocation. We train 1,127 task-specific and transfer models. Single-source transfer is directional and paradigm structured: motor states transfer well within the motor paradigm but provide limited support to most non-motor targets, consistent with a shared sensorimotor execution system and effector-specific representations. Multi-source transfer depends on the composition of the source set, suggesting that many-to-one task relations are not fully captured by pairwise taskonomy alone. Across supervision budgets, BIP repeatedly allocates direct supervision to several 0-back and 2-back working-memory states, although these states are not consistently the strongest individual sources. This pattern may reflect the integration of perceptual, attentional, and executive processes in working-memory tasks. Together, these findings reveal a cross-paradigm-limited motor cluster and working-memory states with high priority under the specified global allocation objective. Our study extends reconstruction-based fMRI taskonomy from one-to-one transfer to many-to-one task relations and budget-constrained task dependencies.

---


### 28. [TEMPO-Diffusion: Temporally Exposed Malicious Poisoning of Diffusion Models](https://arxiv.org/abs/2606.26285)

**<font color=#1a73e8>作者：</font>** William Aiken, Paula Branco, Guy-Vincent Jourdan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Noise-based backdoor attacks on diffusion models typically rely on input-time trigger injection, untargeted activation, and out-of-distribution target generation. Such assumptions reduce both the stealthiness and the practical relevance of these attacks. In this work, we present TEMPO-Diffusion, a targeted backdoor framework that localizes the malicious distribution shift to a temporal, in-distribution exposure. TEMPO-Diffusion supports: (i) targeted attacks on and to specific classes, (ii) multiple sub-image backdoors that reconstruct specific features within multiple, different output images and at multiple locations, and (iii) in-painting with time-conditioned triggers. To study relevant, practical security concerns in leveraging backdoored diffusion models for synthetic training data, we also introduce CALISA: a balanced, region-aware traffic-sign dataset emphasizing Canadian and U.S. road signs. Across CIFAR10, GTSRB, and CALISA, our experiments show that TEMPO-Diffusion can reliably poison class-specific synthetic data generation and induce high attack success rates in downstream classifiers trained on that data.

---


### 29. [Beyond Takedown: Measuring Malicious Go Module Persistence in the Wild](https://arxiv.org/abs/2606.26291)

**<font color=#1a73e8>作者：</font>** Minjae Bae, Carter Yagemann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We measure an automation-based supply chain campaign in the Go ecosystem. The attackers repackage legitimate Go modules under attacker-controlled owners, and embed them with obfuscated code for an import-triggered downloader. Our results come from two complementary analyses: a) a manual search on GitHub across 2,113 repositories and b) a large-scale scan of 12.3M index entries using a deobfuscating AST scanner (GOAST) that we implemented. As a result, we identified 2,289 malicious versions of legitimate Go modules. We demonstrate that purely GitHub-centric searches fail to identify the full extent of the compromise and are only effective for as long as the affected code is present on the platform. Moreover, our proxy-based measurements of the takedown-remediation gap reveal that among artifacts later found to be GitHub-unobservable (i.e., removed or suspended), at least 99.4% remained retrievable via Go proxy. Following our disclosure, GitHub has removed 684 malicious repositories and the Google Go team has remediated 1,377 module versions.

---


### 30. [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294)

**<font color=#1a73e8>作者：</font>** Alex Iacob, Andrej Jovanović, William F. Shen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-improving agents are state-of-the-art (SOTA) on agentic coding benchmarks and have recently been extended to general domains. However, their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves. This ignores a central feature of evolution: species adapt as their environments change with them. We aim to bring the same principle to recursive self-improvement, making evaluation part of the improvement loop and opening search to evolving evaluators, adversarial objectives, and dynamic utilities that may surpass static benchmarks. We introduce the Red Queen Godel Machine (RQGM), an evolutionary framework for recursive self-improvement under non-stationary utilities. The RQGM makes this possible through controlled utility evolution: search is organized into epochs with a fixed within-epoch evaluation criterion, while the utility can be updated at epoch boundaries, so self-improvement guarantees hold per epoch as the objective evolves across them. We begin by showing that even on verifiable coding tasks, the RQGM improves test pass rate over the prior SOTA by adding a complementary agent-as-a-judge code-review signal. This signal is cheaper and the RQGM uses 1.35x-1.72x fewer tokens. We then turn to scientific paper writing and reviewing, and Olympiad-level proof writing and grading, where the RQGM improves performance over prior self-improving agents: co-evolved writers reach 1.78x-1.86x higher acceptance rates under a diverse agent-as-a-judge panel, while co-evolved graders reach 9% higher ground-truth accuracy. In paper reviewing, the strongest baseline reviewer over-accepts AI-generated papers at up to 1.91x the human rate. The RQGM corrects this by introducing an adversarial objective that discovers reviewers equally stringent on AI and human work.

---


### 31. [Beyond Aesthetics: Quantifying Information Loss in Turbid Scenes](https://arxiv.org/abs/2606.26295)

**<font color=#1a73e8>作者：</font>** Vasiliki Ismiroglou, Stefan H. Bengtson, Tasos Benos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visibility in underwater environments degrades rapidly under turbid conditions, yet the effects on computer-vision models remain unclear. This issue is compounded by reliance on synthetic turbidity datasets, which may misrepresent real-world information loss. To address this gap, we introduce the Turbid Underwater Baseline (TUB) dataset, comprising 1,320 images captured under extreme turbidity and over 16,000 high-confidence ground-truth segmentation masks. We additionally propose PCD, a metric derived from phase congruency maps that is invariant to contrast and aims to capture the loss of structural information in real turbidity. We show that PCD correlates strongly with the performance of instance segmentation models on both real and synthetic turbid images, whereas common metrics in the field show weak to no correlation at all. The dataset and relevant code can be found on the project page: this https URL

---


### 32. [Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems](https://arxiv.org/abs/2606.26298)

**<font color=#1a73e8>作者：</font>** Jakob Salfeld-Nebgen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents may begin to perform consequential, irreversible actions such as clinical prescribing and production software deployment. This paper observes that human institutions have governed powerful autonomous actors not by monitoring their reasoning but by requiring independently attested evidence at the point of consequential action. We formalise this institutional pattern as a computational governance model for AI agent systems. Under the proposed model, an agent retains full autonomy over planning and reasoning but holds no execution authority over designated high-risk actions. Execution is conditional on preconditions that are each independently attested by a separate authoritative source, cryptographically bound to a declared intent, and evaluated by a deterministic policy. Decisions are recorded in a tamper-evident log amenable to independent re-verification. We present a proof-of-concept implementation and illustrate the model with examples from software deployment and clinical prescribing.

---


### 33. [COrigami: An AI Pipeline for Co-Designing Flat-Foldable Visually Recognisable Origami](https://arxiv.org/abs/2606.26299)

**<font color=#1a73e8>作者：</font>** Tom Zahavy, Shaobo Hou, Thomas Tumiel 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While generative AI has achieved remarkable success in solving problems with verifiable solutions, generating physical art that satisfies both strict geometric constraints and subjective visual aesthetics remains a challenge. This paper presents an approach to tackle these difficulties in the domain of computational origami, a mathematically rigid environment that grounds artistic design within the equations of flat foldability. We present COrigami, an end-to-end AI-driven pipeline that assists the design cycle by generating crease patterns from natural language. Our pipeline involves generating a semantic stick figure, computing a base packing, solving for a flat-foldable crease pattern, shaping the flat-folded crease pattern, and refining the generated model using reinforcement learning driven by an autonomous aesthetic evaluation loop. Our system acts as a highly effective collaborative assistant, generating structural starting points that human artists can further expand and shape. By integrating algorithmic optimisation with autonomous aesthetic critique, this work demonstrates how AI systems can satisfy multi-objective physical constraints to enable reliable, mathematically grounded co-creativity.

---


### 34. [The Verification Horizon: No Silver Bullet for Coding Agent Rewards](https://arxiv.org/abs/2606.26300)

**<font color=#1a73e8>作者：</font>** Binghai Wang, Chenlong Zhang, Dayiheng Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A classical intuition holds that verifying a solution is easier than producing one. For today's coding agents, this intuition is being inverted: as foundation models develop stronger reasoning capabilities and engineering harnesses grow more sophisticated, generating complex candidate solutions is no longer difficult -- reliably verifying them has become the harder problem. Every verifier we can build is only a proxy for human intent, never the intent itself. This makes verification subject to a twofold difficulty: first, intent is underspecified by nature, making it inherently hard to faithfully check whether it has been fulfilled; second, during model training, optimization widens the gap between proxy and intent -- manifesting as reward hacking or signal saturation. To address this, we characterize the quality of verification signals along three dimensions -- scalability, faithfulness, and robustness -- and argue that achieving all three simultaneously is the central challenge. We further study four reward constructions: a test verifier for general coding tasks, a rubric verifier for frontend tasks, the user as verifier for real-world agent tasks, and an automated agent verifier for long-horizon tasks. Across different task types and policy capability levels, we conduct in-depth analysis and experiments on the core challenges of reward design and how to more effectively leverage reward signals. Experiments show that targeted verification design can effectively suppress reward hacking, improve task completion quality, and achieve significant gains across multiple internal and public benchmarks. These experiences collectively point to a core observation: no fixed reward function can remain effective as policy capability continues to grow; and verification must co-evolve with the generator.

---


### 35. [High-Probability PL-SGD with Markovian Noise: Optimal Mixing and Tail Dependence](https://arxiv.org/abs/2606.26316)

**<font color=#1a73e8>作者：</font>** Dhruv Sarkar, Aprameyo Chakrabartty, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study first-order methods for smooth objectives satisfying the Polyak-Łojasiewicz (PL) condition when gradient samples are generated by an exogenous Markov chain. In the light-tailed setting, prior uniform-in-time high-probability bounds for ordinary Stochastic Gradient Descent (SGD) under a standard growth envelope scale as $\widetilde{O}(t_{mix}^2/k)$, leaving a gap with the $\widetilde{O}(t_{mix}/k)$ expectation bounds. We close this gap using a lag-blocking argument to establish a uniform high-probability guarantee with a leading stochastic term of $\widetilde{O}(t_{mix}/(k+K_0))$ under geometric mixing. We prove this linear dependence on the mixing time is optimal via a matching $\Omega(\sigma^2 t_{mix}/k)$ lower bound on a quadratic objective driven by a persistent two-state chain.
We then extend this framework to heavy-tailed Markovian gradients satisfying a stationary finite-$p$-moment condition, $p \in (1,2]$. We design an all-samples clipped block method that uses every Markov transition while mitigating Markovian bias. Under a transition budget $T$, this algorithm achieves a high-probability stochastic error of $\widetilde{O}(\sigma_p^2(t_{mix}/T)^{2(p-1)/p})$. We establish a matching lower bound by reducing PL optimization to heavy-tailed mean estimation for a sticky Markov chain. Ultimately, this work tightly characterizes the optimal polynomial dependence on mixing time for light-tailed PL-SGD, and the optimal heavy-tail exponent and effective-sample-size dependence in the robust regime.

---


### 36. [Mesh-RL: Coupled subgrid reinforcement learning](https://arxiv.org/abs/2606.26333)

**<font color=#1a73e8>作者：</font>** Behnam Gheshlaghi, Bahador Rashidi, Shahin Atakishiyev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning in large or sparse-reward environments suffers from slow temporal-difference reward propagation, as value information spreads only locally across the state space. We propose Mesh-RL, a spatial domain-decomposition framework inspired by the finite element method and domain decomposition theory, which partitions the environment into overlapping subgrids and enforces boundary-consistent temporal-difference updates. Such an approach enables localized learning while ensuring globally coherent value propagation. Unlike hierarchical or model-based approaches, Mesh-RL accelerates long-range credit assignment without modifying the reward function, Bellman operator, or introducing explicit planning mechanisms. We evaluate Mesh-RL on hazard-dense grid-world environments with varying geometries and mesh resolutions. Across Q-learning, SARSA, and Dyna-Q, Mesh-RL consistently improves convergence speed, cumulative reward, and learning stability. Higher mesh resolutions sustain exploration, prevent premature convergence, and substantially accelerate value propagation to distant states. While Dyna-Q already benefits from internal planning, it still achieves additional gains under structured decomposition. Overall, Mesh-RL introduces a principled spatial domain-decomposition mechanism for accelerating temporal-difference learning. Our framework bridges finite element method-inspired boundary-consistency techniques from scientific computing with reinforcement learning to improve sample efficiency in sparse-reward environments. We will release source code of the study.

---


### 37. [EMA-FS: Accelerating GBDT Training via Gain-Informed Feature Screening](https://arxiv.org/abs/2606.26337)

**<font color=#1a73e8>作者：</font>** Yan Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient Boosted Decision Trees (GBDT), exemplified by LightGBM, spend a dominant fraction of training time -- typically 65-70% -- constructing per-feature histograms. Existing approaches such as random feature subsampling (feature_fraction) discard features without regard for their predictive utility. We propose EMA-based Feature Screening (EMA-FS), an algorithm-level optimization that maintains an exponential moving average (EMA) of per-feature split gains across boosting iterations and, after a short warmup, restricts histogram construction to the top-K features ranked by historical gain. Unlike random subsampling, EMA-FS is informed: it retains high-gain features while screening out low-gain ones. Operating at the per-tree level, it preserves full compatibility with LightGBM's histogram subtraction trick, requiring no changes to core routines.
We evaluate EMA-FS on datasets spanning financial fraud detection, advertising click-through prediction, industrial quality control, and synthetic benchmarks, with feature dimensionalities from 29 to 968. On dense, moderate-to-high-dimensional data it achieves significant speedups: 2.61x on a 500-feature synthetic benchmark and 1.45x on the 432-feature IEEE-CIS Fraud dataset at 30% retention. At 70% retention it improves AUC by 0.11 points while delivering a 1.34x speedup. On extremely sparse data (Bosch, >90% missing) it yields no speedup, as LightGBM's sparse bin optimization already bypasses empty values.
We further introduce Stochastic EMA-FS (S-EMA-FS), which replaces deterministic top-K selection with gain-weighted random sampling controlled by a concentration parameter beta, unifying deterministic EMA-FS (beta -> infinity) and random subsampling (beta = 0) in one framework. Both are implemented in ~120 lines of C++ across all six LightGBM tree learners and are fully backward-compatible.

---


### 38. [Accelerating Returns and the Qualitative Engine for Science](https://arxiv.org/abs/2606.26359)

**<font color=#1a73e8>作者：</font>** Guojun Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ray Kurzweil described a thesis of accelerating returns, which is the most influential narratives in discussions of technological progress. Its central claim is that advances in multiple technological fields, especially compute, artificial intelligence, brain science, and biotechnology, interact in such a way that progress becomes self-amplifying and approximately exponential. This paper gives a simple mathematical interpretation of that claim and then argues that, even if such acceleration is real, it does not by itself resolve the central problem of scientific discovery. The reason is that accelerating returns apply most naturally to executional and infrastructural capability, whereas genuine discovery often depends on a different capacity: qualitative reasoning about when a current framework is structurally inadequate and what conceptual move is needed next. Recent ARC-AGI-3 results sharpen this distinction: humans solve the benchmark at ceiling, whereas frontier AI systems remain below 1%, indicating that the gap between current AI and human flexible reasoning is still very large. At the same time, Demis Hassabis has emphasized that humans must retain their sense of meaning and what they choose to focus their lives on, a reminder that the future of AI is not only a technical forecast but also a question of what forms of human understanding are worth preserving and transmitting. This paper positions the Qualitative Engine for Science (QES) [3] as a response to that missing capacity. In this view, the Kurzweil theory helps explain why quantitative capability may accelerate, while QES addresses the central problem in scientific discovery that acceleration alone does not solve. Its value does not depend on when AGI arrives, but on the fact that the processes of scientific discovery themselves constitute a form of human wisdom worth preserving, organizing, and making accessible.

---


### 39. [Phonetic and semantic analyses of spoken corpora of Beijing and Taiwan Mandarin indicate that the neutral tone is a lexical tone](https://arxiv.org/abs/2606.26360)

**<font color=#1a73e8>作者：</font>** Yuxin Lu, Zhexuan Li, R. Harald Baayen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The neutral, or floating, tone of Mandarin Chinese is a tone with an enigmatic set of properties. It has been described as a reduced tone, or as a tone that sometimes is lexically fixed but that can also be toneless. In two-syllable words, it is found only on the second syllable, but single-syllable words can also have the neutral tone. We present a corpus-based study of the phonetic realization of the neutral tone in spontaneous conversational speech corpora of Beijing Mandarin and Taiwan Mandarin. We show that the neutral tone has its own tonal target, just as the four lexical tones of Mandarin. We also show that disyllabic words with a neutral tone have pitch contours that have a pitch component that depends on the tone on the first syllable, just as has been observed for two-syllable words with a lexical tone on the second syllable (Chuang et al., 2026). Furthermore, words with a floating tone have word-specific pitch signatures, which have also been documented for single-syllable words (Jin et al., 2026) as well as two-syllable words (Lu et al., 2026b). These word-specific pitch signatures are shown to be predictable to some extent from words' contextualized embeddings, as previously reported for lexical tones (Chuang et al., 2026; Lu et al., 2026b). As there is also considerable variability in the realization of lexical tones, we propose that the neutral tone is, in fact, a lexical tone in both Taiwan Mandarin and Beijing Mandarin. We document both similarities and differences in the realization of the floating tone in these two varieties and provide evidence, using contextualized embeddings, that some of the observed differences may arise from differences in the meanings of the words as used in the two corpora.

---


### 40. [Does Aurora Encode Atmospheric Structure? Latent Regime Analysis and Attribution](https://arxiv.org/abs/2606.26361)

**<font color=#1a73e8>作者：</font>** Emma Kasteleyn, Ana Lucic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ML foundation models are able to emulate atmospheric dynamics accurately and efficiently but operate as opaque ``black boxes''. We investigate the internal representations of the Aurora model using spatially pooled PCA and layer-wise relevance propagation (LRP). We find evidence that Aurora's latent space is primarily organized by seasonal cycles, whereas extreme storm events do not form a linearly separable cluster. LRP indicates that the model attends to features consistent with the 3D vertical structure of the Great Storm of 1987. Perturbation tests show masking relevant regions degrades forecasts $3.31\times$ more than random masking. These findings suggest that Aurora learns meteorological coherence and vertical structure without explicit instruction.

---


### 41. [Having Dog Ears "for Real": Effects of Active and Passive Haptics on Embodying Non-Human Body Parts in VR](https://arxiv.org/abs/2606.26364)

**<font color=#1a73e8>作者：</font>** Omar A. Khan, Bao Han Trinh, Lee Lisle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Embodying non-human body parts in VR is a prevalent practice among certain subcultures and is a personally important creative outlet to many individuals. However, the discrepant morphology between real and virtual bodies can decrease Sense of Embodiment (SoE). Haptic feedback can compensate by increasing SoE felt towards non-human body parts, but there is a literature gap in comparing the effects of different haptic modalities, and their combinations, on SoE. Through an online survey sent out to social VR communities (n = 63), we determined that animal ears are a commonly embodied and ecologically valid non-human body part to study. We then ran a 2x2 within-subjects user study (n = 28) with two independent variables: active haptics, delivered through vibrotactile gloves, and passive haptics, delivered through a physical headband, for when participants reach up to touch virtual dog ears appended to their avatar in VR. Our findings show that (1) passive haptics produced the strongest overall embodiment outcomes, (2) combining modalities reduced the benefits of passive haptics, and (3) SoE towards non-human body parts positively correlates with SoE towards the entire avatar. We discuss implications of our findings in various domains, and on embodiment literature.

---


### 42. [Hybrid privacy-aware semantic search: SVD-truncated document geometry and CKKS-encrypted query reranking under a restricted threat model](https://arxiv.org/abs/2606.26373)

**<font color=#1a73e8>作者：</font>** Sergey Kurilenko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dense embeddings power semantic search and retrieval-augmented generation, but embedding-inversion attacks can reconstruct source text from a vector: when a vector database leaks, the documents behind it leak too. The textbook defences are extremes - encrypting the whole search homomorphically is sound but too slow at million-document scale, while privacy noise degrades ranking long before it protects. We study a middle path exploiting the asymmetry between the static collection and the dynamic query. The collection is protected geometrically: each vector is truncated onto a lower-dimensional SVD subspace and rotated by a secret orthogonal transform known only to the owner. The query is protected cryptographically: it is reranked under CKKS homomorphic encryption, so an honest-but-curious server never sees the query or the scores. CKKS parameters come from a small offline benchmark.
We prove a tight lower bound on the reconstruction error of any attacker confined to the protected subspace. On one million documents and five encoders the scheme preserves ranking quality (slightly improving it on strong encoders, as a linear denoiser) at sub-second latency, and an off-the-shelf inversion attack on the protected space collapses to the noise floor. We then test stronger adversaries: a known-plaintext attacker recovers the rotation by orthogonal Procrustes from about as many leaked pairs as the retained dimension; the public product-quantization codes preserve most nearest-neighbour structure; and random-projection, calibrated-noise and BEIR baselines show the truncation is an encoder-dependent accuracy cost, not a free denoiser. We state the limits: query confidentiality is cryptographic, but document protection is an empirical obfuscation layer (SVD truncation plus a secret rotation), not a cryptographic primitive, and we delimit the threat model for each claim.

---


### 43. [SOLAR: AI-Powered Speed-of-Light Performance Analysis](https://arxiv.org/abs/2606.26383)

**<font color=#1a73e8>作者：</font>** Qijing Huang, Sana Damani, Zhifan Ye 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How fast could a deep-learning model run on target hardware, and how far is today's implementation from that limit? These questions are central to software, hardware, and algorithm optimizations. Speed-of-Light (SOL) analysis answers them by computing a workload's theoretical minimum execution time on a given architecture. Yet deriving SOL bounds remains manual, error-prone, and disconnected from rapid model development. To close this gap, we introduce SOLAR, a framework that automatically derives validated SOL bounds from PyTorch and JAX source code. SOLAR leverages both generative and deterministic components in its flow: an LLM frontend translates any source programs into an executable Affine Loop IR, validated by output comparison; a deterministic flow lifts the IR into an einsum graph; and an analytical backend computes unfused, fused, and cache-aware SOL bounds. SOLAR provides comprehensive operator and language coverage, produces validated bounds with zero observed SOL violations, and offers multi-fidelity analysis that tightens bounds and surfaces optimization insights. We evaluate SOLAR across KernelBench, JAX/Flax models, and robotics workloads. These experiments demonstrate four use cases: headroom analysis at multiple fidelity levels, identifying optimization opportunities, cross-platform exploration, and inverse-roofline hardware provisioning.

---


### 44. [What Do Deepfake Benchmarks Measure? An Audit Using Frozen Self-Supervised Representations](https://arxiv.org/abs/2606.26384)

**<font color=#1a73e8>作者：</font>** Samuel Pagon, Yixuan Shen, Vishal Asnani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As deepfake generators approach perceptual indistinguishability, reliable detection becomes critical. Yet, detectors that score well on benchmarks routinely fail in the wild. A concerning feedback loop has emerged: benchmarks drive increasingly complex, engineered detectors, yet if those benchmarks do not reflect real-world deepfakes, this complexity may be solving the wrong problem entirely. This raises a prior question: what are these benchmarks actually measuring? We conduct an audit of video, image, and audio deepfake benchmarks using a deliberately simple diagnostic. If a linear probe on frozen, general-purpose self-supervised representations can approximate the performance of a bespoke detector, the benchmark is largely rewarding general modality understanding rather than forensic understanding. This has two implications: the benchmark may not reflect realistic threat models, and it raises the question of whether the bespoke detectors the probe approaches are truly learning forensic understanding. We observe, across three modalities, linear probes on general-purpose self-supervised representations closely approach the performance of bespoke detectors. We further show that generator-level difficulty is partly explained by Frechet geometry in the same representation space. Together, these results support a benchmark-audit view of deepfake detection: before high scores are read as evidence of forensic understanding, it is worth asking how much of the benchmark is already solved by general-purpose representations.

---


### 45. [Lessons from the Adoption and Deprecation of the Privacy Sandbox Web APIs](https://arxiv.org/abs/2606.26390)

**<font color=#1a73e8>作者：</font>** Yohan Beugin, Paul Barford, Patrick McDaniel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While several web actors have been trying to reduce web tracking for years, it remains unclear how to achieve both desirable levels of utility and privacy. In 2019, Google launched the Privacy Sandbox initiative to balance that trade-off and find privacy alternatives to common use cases such as advertising. Yet, in late 2025, Google canceled the project and deprecated most of the newly introduced APIs. Despite its end, the Privacy Sandbox represents a unique opportunity to learn about how the ecosystem reacted to the proposed changes and make observations about why and how it failed. In this paper, we present a longitudinal measurement and analysis study of the Privacy Sandbox APIs to characterize their adoption and deprecation over the past seven years by different web actors. Leveraging historical HTTP Archive crawls and public Chrome telemetry data, we offer the largest study of its kind into the prevalence of each Privacy Sandbox feature, during their entire respective lifetime (5+ years for some), on popular websites (CrUX top 100k), and as experienced by Chrome users during their browsing journey. Our results showcase an adoption that remained limited and uneven across the years; only few web actors implemented very specific APIs, and in disparate manners. We motivate our interpretation of these results by considering the incentives (interest, resources, timeline, etc.) and risks (potential trade-offs, privacy violations, and legal exposure, etc.) for these actors. Finally, our analysis also yields actionable recommendations for the next generation of web privacy proposals. More broadly, the Privacy Sandbox illustrates the limitations and disparities across browsers of ``fix it in the browser'' remedies: today, tracking and third-party cookies limitations in Chrome still remain largely opt-in, while they have been enabled by default on other browsers like Brave, Firefox, or Safari.

---


### 46. [Deterministic Pareto-Optimal Policy Synthesis for Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2606.26397)

**<font color=#1a73e8>作者：</font>** Aniruddha Joshi, Niklas Lauffer, Sanjit Seshia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world decision-making often requires balancing multiple conflicting objectives, a challenge that standard Reinforcement Learning (RL) frequently addresses by aggregating rewards into a single scalar signal. While effective for simple tasks, this approach often fails to capture the full spectrum of optimal trade-offs, known as the Pareto frontier. In this paper, we introduce a novel preference-conditioned Bellman operator, motivated from the Chebyshev scalarization, designed to compute deterministic Pareto-optimal policies for Multi-Objective Markov Decision Processes (MOMDPs). We prove that this operator satisfies an enveloping property, where the estimated value functions upper-bound the true Pareto frontier, and demonstrate that it monotonically converges to a coverage set of this frontier. Furthermore, we also show how to extract deterministic policies from these converged Q-estimates. This ensures the agent can recover a policy for any given preference, capturing the entire Pareto-optimal frontier while guaranteeing each synthesized policy remains approximately Pareto-optimal. Experimental results validate that our algorithm successfully recovers complex trade-offs, providing a solution for deterministic Pareto-optimal policy synthesis.

---


### 47. [DinoLink: A Token-Centric Representation Compression Framework for Bandwidth-Constrained Collaborative V2X Perception](https://arxiv.org/abs/2606.26398)

**<font color=#1a73e8>作者：</font>** Tianle Zhu, Haohua Que, Handong Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-precision remote perception is often hindered by the severe bandwidth constraints of Vehicle-to-Everything (V2X) networks. We propose \textit{DinoLink}, a token-centric compression framework that replaces raw pixel streaming with discrete semantic communication for vehicle-cloud collaborative inference. DinoLink employs a dual-sparsity architecture: a saliency-aware selector prunes redundant background tokens, while a Residual Vector Quantization (RVQ) module collapses features into compact codebook indices. By transmitting only lightweight indices and positional priors, DinoLink achieves a $139\times$ bitrate reduction compared to uncompressed transmission while maintaining a competitive 32.8\% mAP on the nuScenes dataset. Deployment simulations further demonstrate a $34.5\times$ acceleration in narrow-band environments, such as LoRa. Our results substantiate DinoLink as a robust, bandwidth-efficient frontend for high-fidelity remote perception in constrained V2X scenarios. The code is publicly available at this https URL.

---


### 48. [Geometry-Aware MCTS for Extremal Problems in Combinatorial Geometry](https://arxiv.org/abs/2606.26399)

**<font color=#1a73e8>作者：</font>** Luoning Zhang, Xu Zhuang, Tianhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study certain extremal problems in combinatorial geometry that ask about configurations of points in an $n \times n$ grid that satisfy strict, global geometric constraints. Classical exact solvers suffer from combinatorial explosion for these types of problems, and standard reinforcement learning and transformer-based models struggle with the sparse reward "validity cliff" and quadratic token-consumption limits. To overcome these bottlenecks, we propose a Geometry-Aware Monte Carlo Tree Search (MCTS) framework. Our approach strictly enforces geometric constraints through incremental updates to the feasible action space. For constraints about collections of collinear points, like those that occur in the classic No-Three-in-Line problem (Max-N3IL), this mechanism reduces the constraint checking complexity from $O(n^3)$ to $O(n^2)$. To improve search efficiency, we exploit geometric symmetries in two ways: canonical pruning during node expansion to reduce the branching factor, and symmetric batch transitions to accelerate the discovery of promising configurations. We perform extensive experiments and establish new best-known computational results on five out of six of the problems that we considered. Notably, for Max-N3IL we find configurations of size roughly $1.8 n$ for grids of size $82 \le n \le 119$. For the Smallest Complete Set problem, we find configurations of size roughly $0.95 n$, providing new upper bounds within the tested grids. This work establishes Geometry-Aware MCTS as a highly adaptable framework for discovering novel configurations in combinatorial geometry.

---


### 49. [When Agents Meet Electric Bus Fleet Operations: Pricing Behavior, Trade-offs, and Policy Implications in an Aggregator Framework](https://arxiv.org/abs/2606.26400)

**<font color=#1a73e8>作者：</font>** Jônatas Augusto Manzolli, Ali Eslami, Luis Miranda-Moreno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems are changing how complex operational tasks are coordinated, introducing a new paradigm for connecting heterogeneous data sources and automating processes. Electric bus fleets provide a relevant test case. Their operation requires continuous coordination between service reliability, battery state-of-charge, charger availability, electricity prices, route-energy uncertainty, and vehicle-to-grid (V2G) opportunities. This paper proposes an agentic aggregator framework that streamlines this decision environment by coupling an optimization-based electric bus scheduling model with supervisory agents for disturbance detection, tariff adaptation, and schedule evaluation. The optimization core enforces physical feasibility across routes, chargers, batteries, and V2G exchanges, while the agentic layer interprets changing operating conditions, triggers real-time re-optimization when needed, and defines how flexibility value is allocated between the aggregator and the public transport operator (PTO). A realistic depot case study evaluates day-ahead and real-time operations under profit-based and operation-based coordination modes, considering service delays, route-energy deviations, electricity price shocks, and combined disturbances. The results show that agentic aggregation can support adaptive fleet-grid coordination by maintaining feasible schedules, activating re-optimization selectively, and improving the use of charging and V2G flexibility. However, they also reveal a critical trade-off: the same agentic capability that reduces operational complexity can extract value from the PTO when configured around profit-oriented pricing. These findings suggest that agentic aggregators can become useful for managing electric bus V2G operations, but their deployment in public-fleet contexts requires transparent coordination modes, auditable tariff-setting, and explicit value-sharing rules.

---


### 50. [Beyond Feedforward Networks: Reentry Neural Systems as the Fundamental Basis of Subjecthood and Intrinsic Safety of Next-Generation AGI](https://arxiv.org/abs/2606.26406)

**<font color=#1a73e8>作者：</font>** A. S. Ushakov, Yu. N. Berdinsk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a complete architectural blueprint for safe artificial general intelligence based on a closed reentry loop (D <-> I cycle). In contrast to feedforward networks, which are directed acyclic graphs (C=0, S=0) incapable of self-reference, the proposed architecture contains a structural cycle (C >= 1) with self-sustaining amplification (rho > 1), mathematically guaranteeing the emergence of a self-model, instrumental self-preservation, and unprogrammed goal-directed behaviour. The agent's goals are encoded as a non-textual D-vector in the architecture itself, making them immune to reinterpretation and prompt injection. We present the S-measure -- a polynomial-time [O(N^3)] computable alternative to Tononi's NP-hard Phi -- with machine-verified Lean 4 proof that S>0 implies positive integrated information. The work provides full Python/NumPy implementations (Tarjan-based cycle complexity, Delta-S barrier), industrial horizontal scaling via Apache Kafka and Docker Compose, a taxonomy of six epochs of AI evolution, a zoo of future reentry architectures (RAS, diffusion attractors, fractal loops), gauge-invariant networks for safe swarms, fault-tolerance and recovery protocols, and eight falsifiable predictions. All formal proofs are machine-verified in Lean 4. This architecture is deployable today and represents a topologically protected, safe-by-design approach to AGI.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-245](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
