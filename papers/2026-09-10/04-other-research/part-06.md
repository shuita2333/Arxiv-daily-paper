# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 251. [Conditioned Initialization for Attention](https://arxiv.org/abs/2609.07086)

**<font color=#1a73e8>作者：</font>** Hemanth Saratchandran, Simon Lucey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are a dominant architecture in modern machine learning, powering applications across vision, language, and beyond. At the core of their success lies the attention layer, where the query, key, and value matrices determine how token dependencies are captured. While considerable work has focused on scaling and optimizing Transformers, comparatively little attention has been paid to how the weights of the queries, keys and values are initialized. Common practice relies on random initialization or alternatives such as mimetic initialization, which imitates weight patterns from converged models, and weight selection, which transfers weights from a teacher model. In this paper, we argue that initialization can introduce an optimization bias that fundamentally shapes training dynamics. We propose conditioned initialization, a principled scheme that initializes attention weights to improve the spectral properties of the attention layer. Theoretically, we show that conditioned initialization can potentially reduce the condition number of the attention Jacobian, leading to more stable optimization. Empirically, it accelerates convergence and improves generalization across diverse applications, highlighting conditioning as a critical yet underexplored area for advancing Transformer performance. Importantly, conditioned initialization is simple to apply and integrates seamlessly into a wide range of Transformer architectures.

---


### 252. [Ambient @ EgoProactive 2026 : Proactive Egocentric Assistance with Visually Grounded Supervision](https://arxiv.org/abs/2609.07099)

**<font color=#1a73e8>作者：</font>** Logesh Kumar Umapathi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our submission to the EgoProactive track of the ECCV 2026 Wearable AI Challenge, which ranked first in the large-model division and second in the <=2B division. The task requires a wearable assistant to decide after each eight-second segment of egocentric video whether to intervene or remain silent.
Our approach has two main components. First, we reformulate intervention timing as single-token classification. Rather than generating either $interrupt$<utterance> or $silent$, the model predicts yes or no, and we derive the decision from the renormalised probabilities of these two tokens. This formulation improved macro-F1 by 0.249 and G-mean by 0.30 over free-form generation. Second, because labelled data were limited to the released validation set, we generated additional supervision using a tool-calling video agent that inspects each clip and assigns intervention timestamps. A narration-only alternative was four times larger and ten times cheaper, but transferred worse than supervision from an unrelated real corpus, suggesting that visual grounding is more important than annotation volume for this task.

---


### 253. [Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection](https://arxiv.org/abs/2609.07100)

**<font color=#1a73e8>作者：</font>** Qinwen Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit card fraud detection typically relies on tabular features, while repeated attributes can also provide useful relational signals. This paper proposes THGT-FD, a Temporal Heterogeneous Graph Transformer for Fraud Detection. Each transaction is represented using one transaction token and six types of relation tokens and incorporates Time2Vec encoding into the transaction representation. A Transformer learns the interactions among these tokens within each individual transaction and then outputs a fraud probability. Experiments were conducted on 150,000 transactions sampled from the IEEE-CIS Fraud Detection dataset and chronologically partitioned according to TransactionDT. On the test set, THGT-FD achieved an AUC-ROC of 0.8536, an average precision of 0.4164, and a Recall@5% of 0.4708. The class-weighted histogram-based gradient-boosting baseline achieved an AUC-ROC of 0.8722. The results indicate that relation tokens provide useful information for fraud-risk ranking, although the current model does not yet incorporate entity-level historical aggregation.

---


### 254. [Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training](https://arxiv.org/abs/2609.07108)

**<font color=#1a73e8>作者：</font>** Zili Wang, Zhaopeng Qiu, Yuekai Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates rollout generation, which dominates the cost of reinforcement learning (RL) post-training. Online co-training can further increase the draft's accuracy, yielding greater speedups. However, scaling this approach to co-training on large models with long contexts poses two obstacles: (1) branch attention is unsupported by standard causal context-parallel (CP) implementations, and (2) target features span across pipeline-parallel (PP) stages. We address both with an end-to-end system for large-scale online draft co-training. For CP, we extend packed, load-balanced zigzag ring attention by merging rank-local branch attention with causal main-sequence attention. For PP, TapChannel transports intermediate target features across stages via a separate path, leaving the pipeline schedule unaffected. Experiments demonstrate that co-trained drafts closely track the policy baseline while delivering substantial rollout and end-to-end speedups across model scales up to 122B. Our CP design achieves strong scaling at 256K tokens with significant memory savings over prior work, and our PP transport incurs modest overhead. Code can be found at this https URL.

---


### 255. [A Two-Stage Framework for Ego-Centric Key Object Identification via Object State Prediction](https://arxiv.org/abs/2609.07125)

**<font color=#1a73e8>作者：</font>** Shihong Ling, Yue Wan, Xiaowei Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel framework designed to enhance key object identification in autonomous driving. Existing methods primarily focus on either detecting objects independently or leveraging visual relationships, but they do not explicitly consider the ego vehicle's perspective in determining object importance. To address this gap, we propose a structured approach that integrates a virtual ego-vehicle representation and a modular object state predictor, enabling a more accurate estimation of object behaviors relative to the ego-vehicle. Subsequently, our framework employs spatial-temporal reasoning to refine key object identification, prioritizing objects based on their states and relative spatial information rather than relying solely on visual relationships. Experimental results on real-world driving datasets demonstrate the effectiveness of our approach in accurately detecting critical objects in complex traffic environments.

---


### 256. [EEG-Driven Decoding Framework for Passenger Hazard Perception in Highly Automated Vehicles](https://arxiv.org/abs/2609.07128)

**<font color=#1a73e8>作者：</font>** Yingkai Yang, Ashton Yu Xuan Tan, Bowen Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable risk assessment remains a central challenge for Autonomous Vehicles (AVs). Despite advances in automation, passenger cognition provides a non-intrusive auxiliary signal that improves both objective and perceived safety without requiring active human intervention. We introduce an Electroencephalogram (EEG)-based Brain-Computer Interface (BCI) that decodes passenger neural responses for both Risk Prediction (RP) and Danger Identification (DI), explicitly modeling humans as passengers to match real-world AV use. To achieve this, we propose the Passenger Cognitive Model (PCM), Risk-aware Sequential Labeling (RSL), and the Passenger EEG Decoding Strategy (PEDS), which integrates a 3D Convolutional Recurrent Neural Network (3D-CRNN) model for joint EEG decoding. Experimental results show that 3D-CRNN achieves a Balanced Accuracy (BA) of $95.3\% \pm 2.7\%$ in RP and improves single-subject DI from $80.9\% \pm 3.9\%$ to $85.0\% \pm 3.2\%$ with RSL. Event-wise analyses further show that 3D-CRNN consistently outperforms other models across different event types in RP and DI. In generalization experiments, 3D-CRNN achieves $77.0\% \pm 5.3\%$ BA in cross-session DI and $77.4\% \pm 1.1\%$ BA on seen subjects in cross-subject evaluation, while maintaining a $64.9\% \pm 8.5\%$ BA on unseen subjects, demonstrating promising generalizability and transferability across both intra-subject and inter-subject variability. These findings establish an Electroencephalogram (EEG) decoding framework for AV passenger hazard perception and suggest that passenger cognitive signals can provide auxiliary supervision for future AV decision-making and Safety of the Intended Functionality (SOTIF) support.

---


### 257. [Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner's Expertise](https://arxiv.org/abs/2609.07139)

**<font color=#1a73e8>作者：</font>** Mika Okamoto, Gabriele Sarti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A transformer can make an attribute linearly decodable in its residual stream at a depth where that attribute does not yet influence the output. This gap between where information is readable and where it is used has been shown for attributes stated directly in the input. We ask whether it also holds for an attribute the model must infer gradually over a conversation, namely how expert its dialogue partner is. Using ExpertCollab, a corpus of multi-turn research-planning dialogues between model-played personas at four expertise levels, we find that partner expertise is most decodable in the early layers and falls to near chance before the midpoint of the network. Counterfactual patching shows that injecting the expertise difference at the layer of peak decodability barely changes a fixed late-layer readout, whereas the same difference injected past the midpoint propagates almost completely, a separation of more than an order of magnitude. A content-matched random control and a probe-free diagnostic place the transition at the same early layer, and a statically specified control attribute stays decodable throughout. An inferred relational attribute is therefore represented well before it becomes causally active, which bounds where any attempt to read out or steer partner-conditioned behavior must intervene. We use one model on a synthetic corpus as an initial demonstration.

---


### 258. [Fine-grained Distributed Backdoor Attacks in Federated Learning](https://arxiv.org/abs/2609.07147)

**<font color=#1a73e8>作者：</font>** Jian Wang, Hong Shen, Wei Ke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning, as a privacy-preserving distributed machine learning paradigm, faces significant threats from backdoor attacks. Compared to centralized attacks, distributed backdoor attacks are more harmful but require more poisoned samples to compensate for the loss of trigger strength due to decomposition. Fixed trigger patterns are also easily detected by robust aggregation algorithms, increasing the risk of attack exposure. To address these challenges, we propose a fine-grained distributed backdoor attack framework (FDBA). This framework uses dynamic trigger generation and embedding vector optimization to perform attacks with fewer poisoned samples. First, we design a dynamic trigger generation method based on image edge structures using the Canny algorithm to extract edge features, which are then injected with Laplacian noise. RGB channel decomposition is applied for covert adaptation of the distributed trigger, reducing detection chances. Second, we introduce an embedding vector contrastive learning strategy that forces poisoned samples to approach the target class center in the feature space, enhancing attack effectiveness. On CIFAR-10, piecewise-linear estimates for target ASRs between 70\% and 90\% show that FDBA reduces the required poisoning ratio by 37.4\%--48.4\% compared with DBA. In non-independent and identically distributed (Non-IID) scenarios, FDBA retains 84.7\% of its IID attack performance under extreme heterogeneity, whereas DBA drops to 73.5\%, and the framework successfully bypasses mainstream defense mechanisms.
This study offers new insights into federated learning security and emphasizes the potential threats and defense challenges posed by fine-grained distributed attacks.

---


### 259. [Mind the Approximation: Fisher-Weighted SVD Compression for ViTs](https://arxiv.org/abs/2609.07155)

**<font color=#1a73e8>作者：</font>** Moritz Thoma, Maximilian Groezinger, Maximilian Forstenhäusler 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model compression is key to mitigate deployment challenges of ever growing machine learning models. In this area of research, singular value decomposition (SVD)-based compression offers a compelling trade-off between computational efficiency and model accuracy. Fisher-weighted SVD in particular provides principled, loss-aware compression. However, we find that improving the fidelity of Fisher approximation used in the compression is poorly predictive of post-compression accuracy for Vision Transformers (ViTs). Motivated by this observation, we propose FACTS, a structured Fisher Approximation tailored to Compressing ViTs with Fisher-weighted SVD, which enforces token-local aggregation while preserving within-token activation-gradient dependence. Additionally, we introduce a fast Constrained Rank Search (CoRS), that optimizes layer-wise rank allocation while adhering to a fixed floating point operation (FLOP) constraint. Extensive experiments across ViTs and hybrid architectures demonstrate that FACTS consistently improves accuracy-efficiency trade-offs without requiring finetuning. Notably, it outperforms the strongest SVD baseline by up to +5.8 percentage points (p.p.) Top-1 on Swin-B, with further gains driven by our search method. Code is available at this https URL.

---


### 260. [Frequency-Domain Mixing Data Augmentation for Malicious Traffic Detection](https://arxiv.org/abs/2609.07156)

**<font color=#1a73e8>作者：</font>** Yuhao Yan, Bo Lang, Xiangyu Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The strong dynamics of network traffic often force malicious traffic detection models to handle out-of-distribution data. Typically, deep learning-based malicious traffic detection models require a large amount of high-quality training data. However, owing to challenges such as high labeling difficulty and resource consumption, existing datasets often suffer from insufficient diversity and fail to capture evolving traffic patterns, leading to poor out-of-distribution generalization ability of the trained models. Data augmentation has been widely adopted to improve data diversity and model generalization. Recently, frequency-domain mixing augmentation has shown promising performance because it effectively perturbs data while preserving key structural information. This approach shows potential for enhancing malicious traffic detection models. However, existing studies lack theoretical interpretation of the mixing mechanism, and do not adapt to the characteristics of network traffic. In this paper, we first conduct a theoretical analysis of the current frequency-domain mixing method, revealing its underlying principles and limitations. We further propose an improved frequency-domain mixing-based data augmentation method for network traffic data, which enhances the diversity of sequence features in network traffic and improves the out-of-distribution generalization of malicious traffic detection models. Extensive experiments on multiple artificial and real-world datasets demonstrate that our method substantially improves detection performance across diverse network environments and outperforms other data augmentation approaches.

---


### 261. [Unsupervised Domain Adaptation for Symbol Spotting in Historical Encrypted Manuscripts](https://arxiv.org/abs/2609.07159)

**<font color=#1a73e8>作者：</font>** Giuseppe De Gregorio, Alicia Fornés, Lei Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The decipherment of historical encrypted manuscripts poses a fundamental challenge in Digital Humanities: before any transcription can begin, the symbol inventory of the underlying cipher alphabet must first be identified and characterized. We address this challenge through symbol spotting: given a candidate alphabet specified as a set of rendered font glyphs, the task is to determine whether and where its characters appear in an unseen handwritten document, without any labeled examples from the target script. The main difficulty lies in the domain gap between clean, digitally rendered font queries and degraded handwritten manuscript symbols. We propose a three-stage pipeline that bridges this gap without manual annotation, combining a joint SimCLR+DANN encoder for domain-invariant glyph representations with an embedding-space style-adaptation mechanism applied at retrieval time, requiring no re-training. Experiments on fourteen pages from seven encrypted manuscript collections show that our method outperforms zero-shot foundation models, including CLIP and DINOv2, by a large margin ($+0.194$ P@1 over CLIP ViT-L/14), and surpasses task-specific trained baselines by $+0.138$ P@1. We further demonstrate that the Raw-Cover metric, computed in a fully unsupervised setting, provides a meaningful script-family fingerprint that identifies the underlying alphabet of an unknown document. This capability is of direct practical relevance to palaeographers, historians, and other researchers working with undeciphered manuscripts.

---


### 262. [Weakly-supervised Kidney Tumor Classification from CT Scans with Multi-Instance Learning and Anatomical Filtering](https://arxiv.org/abs/2609.07178)

**<font color=#1a73e8>作者：</font>** Joonas Ariva, Dmytro Fishman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for CT scan analysis are often limited by the scarcity of precise pixel-level annotations, which require significant radiologist effort to produce. Training on scan-level labels alone reduces annotation requirements but introduces challenges: low supervision ratios and large input volumes make models prone to overfitting and shortcut learning. In this work, we investigate two complementary methods to address these challenges: multi-instance learning (MIL) and anatomical filtering. MIL divides CT volumes into 2D slice instances, enabling efficient 2D architectures with ImageNet pretraining rather than computationally demanding 3D models. Anatomical filtering uses Compass, our self-supervised body part regression model, to crop scans to pathology-relevant subregions without requiring segmentation masks. We evaluate two MIL frameworks - Attention-based MIL (ABMIL) and FocusMIL - on kidney tumor classification across one internal dataset (TUH) and two external datasets (KiTS23 and TCGA-KiRC). Our best models achieve F1 = 0.83 on the internal test set using only scan-level labels. We further show that anatomical filtering with the Compass model is critical for the out-of-distribution generalization of embedding-based ABMIL, while instance-based FocusMIL demonstrates greater inherent robustness to distribution shift. While evaluated on kidney tumors, we consider this a proof-of-concept for a broader weakly supervised CT classification pipeline applicable to other organs and pathologies.

---


### 263. [Deep Learning for Biopsy-Free Subtyping of Basal Cell Carcinoma from Dermatoscopic Images](https://arxiv.org/abs/2609.07180)

**<font color=#1a73e8>作者：</font>** Alexandros Papadopoulos, Chrysa Episkopou, Ioannis Sarafis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Basal Cell Carcinoma (BCC) is the most common type of skin cancer, accounting for nearly 80% of skin cancer di- agnoses. Its optimal clinical management is guided by the distinct histopathologic subtype, with aggressive variants requiring more drastic measures. In current clinical practice, subtyping relies on skin biopsies, a procedure both costly and invasive. In this paper, we conduct a preliminary investigation into using deep learning for BCC subtyping, solely from a single dermatoscopic image of the lesion. Given the limited data at our disposal, we employ pre-trained vision transformers (ViTs), a state-of-the-art family of models highly effective for challenging downstream tasks with limited labeled data. Through repeated stratified k-fold cross-validation, we demonstrate that ViTs can achieve superior performance (AUC 0.784 on a dataset of 1271 dermatoscopic images of various BCC subtypes) over standard CNN-based baselines as well as previously-reported human reader perfor- mance, on the task of differentiating aggressive BCCs from other subtype families. These initial findings highlight the potential of combining deep learning and dermatoscopy to provide a biopsy- free alternative for BCC subtyping, thus aiding in improving treatment planning and patient outcomes.

---


### 264. [CHILD: Human-in-the-Loop OOD Detection for Safe Clinical Deployment](https://arxiv.org/abs/2609.07188)

**<font color=#1a73e8>作者：</font>** Jinlun Ye, Kaiyue Lu, Runhe Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection is critical for safe deployment of medical AI systems. Recently, test-time adaptation (TTA) has emerged as a new paradigm for OOD detection, automatically adjusting detector behavior during deployment. However, such automatic adaptation mechanisms may raise safety concerns in safety-critical clinical environments. While physician oversight can mitigate these risks, it is resource-intensive and must be judiciously allocated. To reconcile safety with efficiency, we propose CHILD, a training-free framework designed to enhance streaming OOD detection via sparse human feedback. Operating under strict budget constraints, CHILD employs an adaptive risk-aware sample selection mechanism to pinpoint only the most decision-uncertain samples for review. Crucially, it maximizes the utility of this sparse feedback through a retrieval-based score calibration module, which refines model predictions using a compact feature cache without any parameter updates. Extensive experiments on four medical benchmarks demonstrate that CHILD turns limited supervision into significant reliability gains: with a sparse feedback budget of only 5%, it reduces the average FPR95 from 72.63% to 60.26% and improves AUROC from 75.53% to 81.85%, consistently outperforming state-of-the-art baselines. Our code is publicly available at this https URL.

---


### 265. [FedRAW: Preserving Rare-Label Influence in Asynchronous Federated Learning](https://arxiv.org/abs/2609.07192)

**<font color=#1a73e8>作者：</font>** Prashant Bajpai, Divya Saxena, Philippe Lalanda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous federated learning improves scalability by updating the global model from a server-side buffer of client updates as they arrive, rather than waiting for all selected clients to finish. While efficient, this arrival-driven aggregation can silently distort representation learning under heterogeneous participation. We identify silent rarity failure, a hidden failure mode in which clients holding rare labels contribute too weakly to the global model even though its overall accuracy appears largely unaffected. This failure arises from two coupled effects: rare-label clients may submit updates less frequently when they are slower or less available, creating participation bias; and once their updates enter the buffer, standard asynchronous aggregation assigns them no compensating influence, creating aggregation bias. We propose FedRAW, a fully server-side aggregation method that preserves rare-label influence without changing local training, client objectives, or communication protocols. FedRAW combines client-level update deduplication, which prevents frequently arriving clients from repeatedly dominating the update buffer, with rare-label-aware weighting, which increases the influence of clients carrying low-coverage labels. We formalize silent rarity failure through participation and aggregation bias, and show that FedRAW increases rare-label client influence over uniform aggregation while preserving convergence. Across EMNIST Balanced, CIFAR-10, HAM10000, and ISIC-2019, FedRAW improves rarelabel accuracy while preserving comparable global accuracy and adding negligible server-side computation.

---


### 266. [Protocol effects on feature-based hardware-Trojan detection across Trust-Hub families](https://arxiv.org/abs/2609.07199)

**<font color=#1a73e8>作者：</font>** Hang Xiao, Chuhong Xu, Kainan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trust-Hub reuses host circuits: several files differ mainly in the inserted Trojan. When gates from sibling variants enter both training and test folds, a detector can benefit from host logic it has already seen. We measure that effect instead of proposing another classifier. The corpus contains 49,124 gates from 16 netlists grouped into five host families. We left the parser, 36 gate features, class weighting, model settings, threshold, and family-level aggregation unchanged and altered one choice: the test boundary. The three settings draw test gates from the pooled corpus, withhold a complete netlist, or withhold every variant of one host. The choice matters. Random forest records F1/AP of 0.914/0.978 with pooled gates, 0.636/0.851 with one netlist held out, and 0.460/0.577 with a host family held out. XGBoost falls from 0.946/0.976 to 0.464/0.544 across the same comparison. Logistic regression loses AP, although its fixed-threshold F1 is not monotonic. Each family shows the same pooled-to-family direction. Feature removal, repeated model and simulator seeds, score normalization, parser-related exclusions, and a smaller sample change the size of the gap without reversing it. Aggregation also matters: a gate-weighted average is dominated by the larger ISCAS files, so the headline values give each host family one vote. Bootstrap and jackknife summaries keep the gap positive, but their folds reuse training families. We treat the five family rows as descriptive evidence rather than independent trials. Five host families are too few for a population claim, and the experiment says nothing about transfer to a new cell library or an industrial design. It supports a narrower conclusion: sibling benchmark variants can inflate apparent transfer. Benchmarks with several variants of one host circuit should report family-aware holdouts and all five family results beside pooled scores.

---


### 267. [REFINE: Trajectory Representation Learning via Closed-Loop Transcription -- Extended Version](https://arxiv.org/abs/2609.07206)

**<font color=#1a73e8>作者：</font>** Sean Bin Yang, Ying Sun, Jilin Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory representation learning underpins a wide range of trajectory analytics tasks; however, most existing self-supervised approaches, whether discriminative or generative, adopt an open-loop paradigm, relying on fixed data augmentations or random masking without feedback, which limits their ability to generalize and scale.
We propose REFINE, a simple yet effective Representation lEarning Framework vIa closed-loop traNscription rEfinement for trajectory data. Drawing upon feedback control theory, REFINE tightly couples road-network-aware generative reconstruction with feedback-driven contrastive learning, enabling the model to capture fine-grained local movement semantics and global spatio-temporal dependencies without manually designed augmentation views. We further provide a control-theoretic analysis that establishes convergence guarantees for the proposed closed-loop optimization.
Extensive experiments on four real-world datasets demonstrate that REFINE consistently outperforms state-of-the-art methods across multiple downstream tasks while remaining computationally efficient and scalable.
This paper is an extended version of REFINE: Trajectory Representation Learning via Closed-Loop Transcription, to appear in KDD 2026.

---


### 268. [Unraveling the Real Working Mechanism and Inherent Flaws of GAE: A Method for Interpreting Transformer Processes from an Economic Perspective](https://arxiv.org/abs/2609.07213)

**<font color=#1a73e8>作者：</font>** Yongjin Cui, Xiaohui Fan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We observe a phenomenon that current algorithmic research in the field of explainable artificial intelligence primarily pursues better performance on several proxy metrics. On the one hand, these proxy metrics themselves are more or less flawed and cannot properly measure the quality of methods. On the other hand, metric-oriented research approaches often lead to the neglect of the rationality and interpretability of the methods themselves. Explainable artificial intelligence is abbreviated as XAI. The metric-driven research paradigm has resulted in a lack of interpretability of the relevant XAI methods themselves. Accordingly, there is a need for interpretability research on XAI methods, which can be playfully referred to as XXAI. This paper is one of our works on XXAI. This paper takes Generic Attention-model Explainability (GAE), a widely influential model interpretation method , or rather, XAI method that represents an important technical route, as the research object, and explores the real working mechanism and flaws of this method as well as the technical route it represents. Based on the conclusions of this study, it may be necessary to re-examine or verify GAE-related methods and their domain applications. We argue that GAE is an interpretation method that focuses on the attention process. After pointing out the working mechanism and flaws of GAE, we propose Cumulative Asset Holdings (CAH), a more reasonable Transformer interpretation method integrating both process-based and feature-based ideas from an economic zero-sum games perspective. In addition, it is worth noting that our method is applicable to models with special tokens, where existing methods may suffer from limitations. The model simplification research method and the analysis of additive operations adopted in this study may provide inspiration for other research works in XAI.

---


### 269. [Enhancing Privacy, Neglecting Harms: An Analysis of Real-World Digital Privacy Incidents](https://arxiv.org/abs/2609.07217)

**<font color=#1a73e8>作者：</font>** Shannon Veitch, C. Shem, Lena Csomor 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-enhancing technologies (PETs) have emerged as a technical means for providing individuals with greater control over their information. Yet despite the growing deployment of PETs, people continue to experience privacy harms. In this work, we revisit our understanding of privacy incidents and the realities of those experiencing privacy harms, to assess whether the goals and abilities of PETs are misaligned with the harms people face.
For our study, we collect news articles that correspond to a sample of 257 real-world privacy incidents. We employ content analysis over the articles to develop a new information flow model that encompasses the complexity of data flows and their relation to resulting harms. We demonstrate that our model captures both established and novel aspects of privacy incidents and their mitigations. In particular, it captures why consent is often insufficient to prevent privacy violations, how harms emerge from complex interactions among multiple entities and actions, and reveals a flaw in our understanding of PETs: a focus on enabling functionalities still permits the harms inherent in those functionalities. Moreover, we find that the entities best positioned to implement harm-preventing measures for the incidents in our sample are the least incentivized to do so. Overall, our model and analysis identify limitations of privacy technology research for harm prevention and further identifies paths for transforming how we approach the advancement of these technologies.

---


### 270. [Robust Decentralized Federated Distillation via Multi-Modality Knowledge Collaboration](https://arxiv.org/abs/2609.07230)

**<font color=#1a73e8>作者：</font>** Xiao Ma, Hong Shen, Hui Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper propose a robust decentralized federated distillation method that enables clients with heterogeneous models to collaborate through predictions on shared unlabeled public data. In the proposed method, each client first evaluates the received predictions in three modalities of class prediction, boundary decision, and prediction correlation. It then filters unreliable clients, assigns reliability-based weights to the retained clients, and constructs a teacher for each type of knowledge. Finally, the corresponding distillation gradients are validated using a supervised gradient computed from private data. Conflicting prediction and boundary gradients are removed, and conflicting relation gradients are suppressed before the final model update. We prove the convergence of the proposed method by showing stable local optimization for honest clients under Byzantine distillation. Particularly, we show that our method ensures a bounded Byzantine influence on both distillation gradients and individual client private gradients after cross-modality fusion, thereby enabling stable local optimization for honest clienunder Byzantine distillation. Extensive experiments on CIFAR-10 and CIFAR-100 demonstrate that the proposed method improves the prediction accuracy of heterogeneous models of clients under non-IID data and Byzantine attacks. As the booming demands of federated learning in decentralized environments such as edge computing and mission-oriented UAV collaborations, our method has a great potential for adoption of DFL in unreliable real-world scenarios where clients are exposed to receiver-specific Byzantine messages of malicious predictions.

---


### 271. [Kolmogorov--Arnold stability for discontinuous functions](https://arxiv.org/abs/2609.07240)

**<font color=#1a73e8>作者：</font>** Sviatoslav V. Dzhenzher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Here we investigate the stability of the Kolmogorov--Arnold representation theorem (KART) under adversarial reparameterisations of the hidden layer for multivariate discontinuous and unbounded functions. Our results provide a rigorous mathematical foundation for the structural robustness of modern deep learning architectures, such as Kolmogorov--Arnold Networks (KANs), under adversarial configurations.

---


### 272. [Living with AI Companions: Sustained AI Companionship Predicts Lower Well-Being Through Lower Human Interaction](https://arxiv.org/abs/2609.07243)

**<font color=#1a73e8>作者：</font>** Yutong Zhang, Dora Zhao, Yixin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI chatbots are increasingly used for companionship, emotional support, and personal self-disclosure; however, how social engagement with these systems unfolds over time and shapes users' well-being remains unclear. To address this, we conducted a two-wave longitudinal study of CharacterAI users, surveying 1,182 participants at baseline and 439 after a mean follow-up of 12 months. We examined how social engagement with AI companions evolves and how these longitudinal engagement patterns may influence well-being through two hypothesized pathways: sustained social engagement over time and the displacement of human social interaction. We found that interaction intensity, companionship use, and self-disclosure all showed substantial continuity over time. Greater interaction intensity at baseline predicted greater subsequent interaction intensity, companionship use, and self-disclosure. Consistent with the longitudinal engagement pathway, sustained social engagement across these dimensions was consistently associated with lower well-being. Results further support the social displacement pathway, indicating that these links were mainly explained by lower in-person social interaction. These findings highlight the importance of designing AI companions that support human social relationships without displacing them

---


### 273. [Towards a Resilience-Theoretic Foundation for Adversarial Robustness in Industrial Control System Anomaly Detection](https://arxiv.org/abs/2609.07244)

**<font color=#1a73e8>作者：</font>** Branka Stojanović, Andreas Flatscher, Michael Somma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anomaly-based intrusion detection systems in industrial control systems (ICS) and operational technology (OT) environments are increasingly required to meet formal resilience criteria: absorbed adversarial disturbances, graceful degradation under sustained attack, and certified system-level guarantees. Existing resilience frameworks for cyber-physical systems define absorb-recover-adapt trajectories at the architectural level but do not treat machine learning anomaly detectors as first-class components, leaving a gap between component-level robustness evaluation and system-level resilience certification.
In this paper, we establish that adversarial robustness in ICS anomaly detection is a specific instantiation of system resilience, and formalise this connection by mapping four resilience constructs, i.e. disturbance class, absorption capacity, recovery trajectory, and degradation function, onto the adversarial machine learning setting. We derive a compositional resilience bound for heterogeneous ICS detection networks, showing that the binding constraint on system-level resilience is the coupling-adjusted absorption capacity of each node along the attack path, not the per-node capacity -- so the binding node need not be the weakest one. Empirical validation on the BATADAL water distribution system benchmark demonstrates that the resulting metrics surface operationally significant phenomena invisible to standard benchmarks: the absorption-degradation divergence under adversarial training, and the paradox that hardening the binding node in isolation reduces system-level resilience. Implications for ICS architecture design and certification standards are discussed.

---


### 274. [Dense Structural Compression of Transformers via Gauge-Correct Channel Removal](https://arxiv.org/abs/2609.07264)

**<font color=#1a73e8>作者：</font>** Jed A. Duersch, Naïm Es-Sebbani, Nathanaël Haas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference energy per token drives the cost and carbon footprint of deployed transformers. It is dominated by dense matrix products that incur fused multiply-accumulate (FMA) operations and memory traffic. To reduce these computations while retaining dense tensors for high GPU throughput, we develop a methodology from first principles to adapt structural complexity during training to maximize inference utility per unit compute. Channel penalties drive entire tensor slices to zero to enable physical removal while preserving density and the network function.
The natural approach, penalizing the norm of operator components acting through each channel, is provably destabilized by gauge freedom. We resolve this pathology with GaugeLasso: additive symmetric group-lasso penalties that recover a monotone function of product-norms when the network converges to gauge balance. Our equilibrium analysis enables per-channel calibration to correctly suppress slices that under-perform in inference utility per unit compute.
Under adaptive pressure, the network reorganizes into depth-dependent structural profiles that can be far smaller than the architecture required to learn the task. On polynomial long division over $\mathbb{F}_{31}$, compute compresses from 148 to 255 times with perfect accuracy. On character-level language modeling, compressed models outperform the hand-designed baseline at equal FMA. On masked autoencoding, a compression trial exposes which axes were over-provisioned and which saturated, guiding a better second design. Compaction also accelerates training monotonically as the model progresses. Post-hoc pruning with the same utility ranking cannot reach these structures, showing that sustained pressure is central to discovery of efficient models. Retraining a discovered architecture recovers baseline quality on our statistical tasks, but fails on our exact algorithmic task.

---


### 275. [Constitutive State-Space Modeling of Path-Dependent Plasticity: A Resolution-Consistent and Parallelizable Computational Framework](https://arxiv.org/abs/2609.07294)

**<font color=#1a73e8>作者：</font>** Rui Barreira, Taylan Soydan, Francesco Scipione 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven constitutive models for path-dependent plasticity are commonly formulated using nonlinear recurrent neural networks, whose sequential state evolution limits parallel training and whose predictions may depend on the discretization of the applied strain path. We introduce a Constitutive State Space (CSS) model that reformulates structured state-space dynamics as an incremental constitutive operator. The strain increment is decomposed into magnitude and direction: the loading direction drives the latent state-space system, while the increment magnitude enters the zero-order-hold discretization of its continuous-time linear recurrence. This mechanics-tailored construction guarantees stationarity under zero increments, strongly reduces sensitivity to strain-path resolution, and retains the parallel-scan structure of S5 for efficient training on long constitutive histories. The CSS and Minimal State Cell (MSC) architectures are compared for four multiaxial path-dependent material models including isotropic J2 plasticity, pressure-sensitive foam plasticity, and combined isotropic-kinematic hardening. CSS matches or exceeds the prediction accuracy of the MSC, including one order of magnitude lower validation losses for the plastically incompressible materials. Importantly, CSS maintains low errors across large changes in strain-path discretization, whereas the MSC error increases substantially when evaluated at coarser resolutions than used for training. CSS trains substantially faster and requires fewer strain-stress pairs to attain comparable or better accuracy. Analysis of the learned state further reveals latent structure consistent with the dimensionality of the underlying physical constitutive models. These results establish mechanics-tailored structured state-space dynamics as a computational framework for efficient and discretization-robust data-driven constitutive modeling.

---


### 276. [KODAMA: Multimodal Digital Twin Reconstruction for Urban RF Propagation Modelling](https://arxiv.org/abs/2609.07298)

**<font color=#1a73e8>作者：</font>** Maximiliano Wardle, A. Ryo Koblitz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction typically strives for geometric fidelity or visual plausibility. Radio frequency digital twins (RFDT) are instead judged by whether communication channels behave in them as they do in the real world. RFDTs promise site-specific channel prediction but current practice forces a choice between coarse automated scenes and hand-built, measurement-calibrated models that take weeks to construct per-site. We present KODAMA, an automated pipeline that reconstructs ray tracing-ready RFDTs at city scale from off-the-shelf geospatial data alone: aerial imagery, LiDAR, and photogrammetry yield terrain and watertight building meshes, while exposure-weighted multi-view fusion of street-level imagery recovers façade relief, electromagnetic materials, and clutter---all without site visits or calibration. Across three sites spanning 3.6 to 28 GHz, KODAMA's uncalibrated predictions achieve single-digit RMSE, reducing point-to-point error by up to 5.35 dB over automated baselines and coming within 0.22 dB of a measurement-calibrated, hand-built RFDT.

---


### 277. [World Models Under Asynchronous Sensor Observations](https://arxiv.org/abs/2609.07299)

**<font color=#1a73e8>作者：</font>** Akash Anand, Abhay Anand, Yash Vishe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned world models typically assume that observations arrive synchronously, an abstraction inherited from simulators that return a complete state vector at each environment step. Physical sensing instead operates at heterogeneous rates, leaving most observation channels stale at any given instant. Interpolating stale channels introduces measurements that were never observed, while downsampling to the slowest sensor discards valid measurements. A natural alternative is to zero-order-hold the most recent reading and provide the known sampling schedule to the model through two features, staleness and time-to-refresh. We test this prediction using transformer world models across three regimes of increasing causal coupling: open-loop rollouts in continuous-control locomotion, closed-loop model-predictive planning in which each learned model serves as the planner dynamics, and a linear latched-actuator system in which refresh events apply a zero-order-held command to the plant. Our findings show that the effectiveness of time-to-refresh depends on the causal role of the sampling schedule, specifically when refresh events affect the system rather than merely report its state. These results establish when sampling schedules provide useful information for predictive world models operating under asynchronous physical observations.

---


### 278. [PCFlow: Physics-Conditioned Flow Matching for GPR B-Scan Image Synthesis](https://arxiv.org/abs/2609.07300)

**<font color=#1a73e8>作者：</font>** Zhijie Shen, Chenchen Fu, Xuanhao Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ground-penetrating radar (GPR) B-scan image synthesis is important for data augmentation, algorithm validation, and simulation acceleration, yet generating radargrams with both visual realism and physical consistency remains challenging. Existing learning-based generative models often emphasize visual appearance but provide limited control over response geometry. In this paper, we propose PCFlow, a physics-conditioned flow matching framework for fast GPR B-scan image synthesis. The core of PCFlow is a Maxwell-informed dense physical condition field constructed from the parameterized physical model used for electromagnetic simulation, including material properties, target geometry, propagation cues, and response-domain priors. This condition field provides an interpretable interface between physical scene parameters and radar response geometry, and guides conditional flow matching in the VAE latent space toward physically feasible generation paths. We evaluate PCFlow on a gprMax-based buried-pipeline dataset with both in-distribution and out-of-distribution test cases. Experimental results show that PCFlow generates images with more accurate response geometry and high visual fidelity, demonstrating its effectiveness for controllable and physically faithful radar image synthesis.

---


### 279. [Marginal Fidelity Does Not Establish User Simulation in Demographic Synthetic Survey Panels: Response Contracts, Support Collapse and Conditioning Failure](https://arxiv.org/abs/2609.07305)

**<font color=#1a73e8>作者：</font>** Alexander Doudkin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Demographic synthetic survey panels are often validated by matching aggregate answers to published surveys. We test what that certificate establishes across six multiselect batteries from four survey organisations in three countries. The headline analysis is restricted to three instruments whose synthetic cohort and human target share the stated population frame; three other batteries remain sensitivity analyses.
The response contract dominates measured fidelity. In the aligned instruments, committed sets leave 66 of 128 model-battery option slots empty in panels of up to 500 respondents, versus 0 of 128 under per-option probability elicitation. Across eight uncapped model-instrument comparisons, probabilities reduce option-marginal MAE by 4.53 to 7.30 points. The capped instrument reverses on two models until the vectors are projected onto its stated maximum. These are measurement effects: human targets are realised check-all responses, whereas the vectors are latent inclusion propensities.
Published marginal agreement also fails to discriminate respondent simulation from direct population estimation. On nine aligned model-battery pairs, a no-persona population-prevalence query averages 6.27 MAE versus 12.39 for committed panels and wins all nine comparisons. Constraint-aware probability vectors average 5.34 and beat the query on four of nine, so the baseline challenges the validation criterion rather than proving direct estimation uniformly best. On three unpublished demographic cells, neither approach beats reciting the national distribution. Population-marginal agreement is therefore evidence about an elicitation contract and an estimand obtainable without simulated respondents, not evidence of individual simulation.

---


### 280. [RouteRelay: Event-Triggered Cross-Layer Route Reuse for Efficient Dynamic Sparse Attention](https://arxiv.org/abs/2609.07306)

**<font color=#1a73e8>作者：</font>** Bin Li, Sisi Liu, Chenyang Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic sparse attention reduces long-context prefill cost by routing each query chunk to a small set of key chunks at every Transformer layer. The sparse attention kernel avoids most token interactions, but the router still rebuilds a chunk--chunk score matrix layer after layer, even when the selected routes change little. We introduce RouteRelay, a router-agnostic method that reuses only route metadata across depth while continuing to compute attention with the current layer's queries, keys, and values. Anchor layers perform full routing. Intermediate layers rescore the previous top-$k$ route and a compact sentinel set of near-miss and randomly probed chunks. A query row is rerouted only when a sentinel challenges its weakest selected chunk. We give a top-$k$ stability condition, a probabilistic bound on missed challengers, and a row-selective GPU execution design. In a reproducible empirical evaluation, RouteRelay retains at least 99.99% route recall while rerouting 25.0%, 55.4%, and 78.2% of rows under low, moderate, and high cross-layer drift, respectively. Across routing scales, RouteRelay retains 100.0% recall while evaluating 38.4--51.6% of full-routing score pairs as the key-chunk count grows from 128 to 1024. Its unfused CPU execution remains slower than dense matrix multiplication, exposing row compaction and ledger updates as the main kernel-engineering targets.

---


### 281. [Robust Decentralized Personalized Federated Learning via Prediction-Constrained Neighborhood Collaboration](https://arxiv.org/abs/2609.07312)

**<font color=#1a73e8>作者：</font>** Xiao Ma, Hong Shen, Hui Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a robust decentralized personalized federated learning method R-DPFL, that enables clients to reduce the impact of Byzantine attacks via robust neighborhood direction estimation and history-based update trend prediction, rather than purely aggregating client models as in the existing work. In R-DPFL, each client first computes the current-round model update by aggregating the received neighborhood update vectors. It then predicts what this update should be based on its historical values and local model changes. Finally, R-DPFL computes the difference between these two quantities, adaptively clips this difference, and adds it to the local update. We prove convergence of the learning process through rigorous analysis and show that honest clients maintain stable personalized descent dynamics under Byzantine neighbor perturbations without requiring consensus among neighboring models. Extensive experiments on CIFAR-10 demonstrate that RDPFL consistently outperforms state-of-the-art decentralized and personalized federated learning baselines under heterogeneous and adversarial settings.

---


### 282. [Weakly supervised neural network: segmentation of complex structures in X-ray microCT](https://arxiv.org/abs/2609.07313)

**<font color=#1a73e8>作者：</font>** Daniele Rusconi, Michela Ascolese, Stephanie Fest-Santini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Segmentation of complex structures in X-ray tomographic data is a fundamental task in biomedical research, but it often requires large amounts of precisely annotated data, making fully supervised approaches costly and difficult to scale. In this study, weakly supervised deep learning is investigated as a strategy to reduce annotation effort while maintaining accurate segmentation. A two-dimensional convolutional neural network based on the nnU-Net framework was adapted to a weak supervision setting using sparse dot-based annotations, complemented by a limited number of fully segmented images. The approach was evaluated on high-resolution microCT slices of rat kidneys, targeting the segmentation of renal glomeruli, which are small, low-contrast anatomical structures. Results indicate that weak supervision provides a meaningful learning signal, enabling reliable localization of glomeruli even in the absence of dense labels. Incorporating a small set of high-quality annotations substantially improves segmentation performance, approaching that of a fully supervised model. These findings highlight the potential of weakly supervised learning as an annotation-efficient strategy for the analysis of complex structures in X-ray tomographic data, and suggest that alternative loss formulations tailored to sparse annotations may further enhance performance.

---


### 283. [Content-Based Addressing for Long Context](https://arxiv.org/abs/2609.07314)

**<font color=#1a73e8>作者：</font>** Mahesh Godavarti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rotary position embedding (RoPE) uses each token's integer position to determine the rotation applied inside attention. This works well for local token order, but increasing context length creates a positional train-test mismatch: RoPE produces relative rotations at offsets not seen during training. Methods that rescale, interpolate, randomize, or bias positions specify how attention handles those offsets, but still derive positional information from a growing token counter. We instead divide a token stream into units, retain ordinary RoPE positions within each unit, and assign every completed unit an address computed from its content. Adding units then applies the same learned map to new content rather than extending a positional range or an identifier table. We prove that this construction preserves local RoPE exactly, leaves the attention comparison between two fixed tokens unchanged when other units are inserted or reordered, and does not create new relative rotations merely because more units are added. In a character-level Tiny Shakespeare diagnostic, a model trained on 256-character contexts has validation perplexity 4.04 at 256 characters and 3.82 at 4096, while continuous RoPE changes from 4.71 to 12.09. A second diagnostic shows that content-based addressing can retrieve and use information from multiple serialized facts. These are controlled shallow experiments, not scale benchmarks, but they support a direct prescription: use position to address locally and content to address across units.

---


### 284. [DGCPath: Distribution-Aware Generative Contrastive Framework for Self-supervised Path Representation Learning -- Extended Version](https://arxiv.org/abs/2609.07316)

**<font color=#1a73e8>作者：</font>** Sean Bin Yang, Hao Miao, Zongyi Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Due to the proliferation of vehicle trajectory data enabled by advanced sensing technologies, path representation learning has become a pivotal task in intelligent transportation systems. Although existing self-supervised approaches have achieved promising performance, their dependence on deterministic contrastive learning paradigms and handcrafted view augmentation strategies inherently restricts their cross-scenario generalization capabilities. To address these limitations, we present DGCPath, an innovative Distribution-aware Generative Contrastive learning framework for Path representation. This framework establishes a synergistic connection between generative modeling and distributional contrastive learning, enabling the acquisition of robust and transferable feature embeddings. Specifically, our framework incorporates: (1) a diffusion-based view generator that autonomously produces semantically coherent yet diverse trajectory views from Gaussian noise; (2) a variational contrastive mechanism that enforces latent feature alignment at the distribution level, transcending conventional instance-wise consistency; and (3) a novel generative cross-supervision module that reinforces view-level consistency through cross-view reconstruction learning. Comprehensive evaluations on three real-world trajectory datasets demonstrate that DGCPath outperforms state-of-the-art baselines on two distinct downstream tasks, validating its enhanced generalization capability and representation effectiveness.

---


### 285. [CRISP: Corneal Confocal Microscopy Real-Time Image Stitching Pipeline](https://arxiv.org/abs/2609.07336)

**<font color=#1a73e8>作者：</font>** Qincheng Qiao, Puli Zhang, Jian Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Morphology of the sub-basal nerve plexus (SNP) reflects peripheral nerve health, and corneal confocal microscopy (CCM) provides an important means for in vivo, real-time, non-invasive observation of the SNP. However, mainstream CCM devices offer a limited field of view per frame, whereas the SNP is spatially non-uniform; discrete image sampling is therefore sensitive to sampling location and frame selection, which limits the reproducibility and clinical adoption of CCM as a quantitative assessment tool. Wide-field stitching can reconstruct larger SNP mosaics by integrating sequentially acquired CCM images, but existing methods largely rely on offline post-processing, additional hardware, or specific acquisition protocols, and lack open-source real-time solutions for conventional CCM video streams.
This paper presents CRISP (Corneal confocal microscopy Real-time Image Stitching Pipeline), an open-source real-time SNP wide-field stitching framework for conventional CCM examination video streams. CRISP excludes defocused and discontinuous segments via focus-aware gating, propagates poses through local pairwise registration, and maintains non-redundant spatial coverage with a sparse anchor map; when local temporal continuity is interrupted, the system completes relocalization and subgraph merging through global appearance retrieval followed by geometric verification. The framework prioritizes low-latency coverage feedback during examination while outputting accepted frames, poses, and anchor information to initialize offline fine stitching.
To our knowledge, CRISP is the first open-source real-time SNP wide-field stitching framework released for conventional CCM video streams. By lowering the barrier to adoption and reproduction of wide-field stitching, CRISP may help move SNP wide-field imaging from a research tool into routine clinical examination workflows.

---


### 286. [From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment](https://arxiv.org/abs/2609.07346)

**<font color=#1a73e8>作者：</font>** Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiance field representations such as 3D Gaussian Splatting (3DGS) enable high-quality novel view synthesis but can introduce complex, view-dependent artifacts from reconstruction, rendering, and compression. Reliable perceptual quality assessment (QA) is thus essential for evaluating rendered views and guiding the design of perceptually faithful scene representations. Existing full-reference QA metrics require an aligned reference image, while recent cross-reference metrics relax this requirement by comparing a test view with non-aligned references. However, under wide-baseline radiance field settings, selecting a reliable nearby reference can be difficult, particularly when evaluating views along arbitrary trajectories and poses. We propose SCODA, a lightweight scene-conditioned objective QA method that shifts QA from explicit image-to-image comparison to scene-manifold modeling. High-quality observations of each scene are represented as a multivariate Gaussian distribution in deep feature space, producing a semantic fidelity score that measures deviation from the scene distribution. A weakly-supervised distortion-aware patch discriminator provides a complementary realism signal, and both cues are combined through an unsupervised bounded fusion strategy. Experiments on multiple benchmarks show strong agreement with human judgments and robust generalization across GS- and NeRF-generated views and trajectories. Code is publicly available at this https URL.

---


### 287. [Inferring Urban Mobility Interactions from Aggregated Dynamics](https://arxiv.org/abs/2609.07349)

**<font color=#1a73e8>作者：</font>** Yi Wang, Jing Li, Jinliang Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time urban governance depends not only on knowing where people are, but on how they move between places, directional flows that could be conventionally resolved by tracking individuals through space, i.e., expensive to sustain and built on traces that are highly unique and readily re-identifiable. Here we show that this directional structure need not be observed to be known: aggregated counts which cities already collect retain enough information to reconstruct the temporal evolution of origin-destination (OD) matrix. Using an uncertainty-aware physics-informed framework, we infer future OD flows from area-level counts alone across twelve mobility datasets from cities in the United States and China, reaching accuracy comparable to models that take historical OD matrices as input. Probabilistic modeling corrects the systematic underestimation of sparse, high-value corridors and yields calibrated predictions consistent with observed flows. Architectures that respect the generation-before-assignment logic of transport planning recover interactions more faithfully, indicating that location-level spatial heterogeneity should be preserved before pairwise interactions are reconstructed. Because inference requires only aggregated observations after training, recovering interactions this way reduces reliance on continuous individual-level tracking, pointing toward a more deployable and less exposure-heavy basis for real-time urban intelligence.

---


### 288. [5GDescrambler: Locating, Descrambling, and Decoding 5G Scheduling Information (long version)](https://arxiv.org/abs/2609.07367)

**<font color=#1a73e8>作者：</font>** Fritz Windisch, Thorsten Strufe  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tracking users in 5G NR has recently been successfully demonstrated by exploiting various side-channels. This allows for identification of individuals, classification of user activity in real time as well as tracking by fingerprinting, affecting billions of users with a 5G subscription and companies with private 5G deployments. However, previous work relies on weak operator configurations that leak networking parameters--either the radio network temporary identifier (RNTI) or scrambling factor ($N_{ID}$) during handshake--or to inefficiently brute-force Downlink Control Information (DCI).
In this paper we present a novel technique exploiting algebraic structure to reverse DCI scrambling, fully integrated into an open-source end-to-end binary DCI sniffing pipeline. It provides enabling input for subsequent attacks like live tracking of users and supports automatic detection of control channel configurations used. We demonstrate the robustness and performance of our approach with measurement campaigns against deployments of srsRAN, OpenAirInterface5G, and two commercial vendors. It reaches block error rates of less than $1\%$ at SNRs below expected values for efficient communication, while performing significantly faster on a reference sample than a previously suggested passive technique brute-forcing the required parameters. In addition, it is entirely passive and does not rely on any side-channel leakage.

---


### 289. [DF26: We Cannot Tell Fake From Real Anymore](https://arxiv.org/abs/2609.07369)

**<font color=#1a73e8>作者：</font>** Severyn Shykula, Andrii Yermakov, Ivan Samarskyi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce DF26, a novel benchmark for detecting AI-generated videos containing fully synthetic clips produced by recent text-to-video and image-to-video models. The videos capture single-person public-speaking scenarios, spanning direct-to-camera recordings, official statements, and studio interviews - 271 real and 2,420 synthetic videos generated by seven modern video models. The study on DF26 shows that human performance in detecting AI-generated videos, as well as state-of-the-art deepfake detectors, is close to random chance. Our results highlight the limitations of current evaluation protocols and motivate the need for benchmarks that explicitly measure robustness to modern generative model distribution shifts.

---


### 290. [TRAIL: Trajectory-Aware Visual Place Recognition against Unordered Databases](https://arxiv.org/abs/2609.07373)

**<font color=#1a73e8>作者：</font>** Dominik A. Kloepfer, Patrick Wenzel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Visual Place Recognition (VPR) methods excel on standard benchmarks yet remain brittle in feature-poor environments. By treating each query image in isolation, they discard the sequential context in any real trajectory. We formalize a task that exploits this context: given a query sequence, localize the final image against an unordered reference database -- which, unlike sequence-to-sequence methods, requires no sequential structure in the database. We propose TRAIL (TRajectory-Aware Image Localization), a principled framework based on Conditional Random Fields (CRF) that combines learned functions for visual similarity and for camera-motion consistency, refining a distribution over candidate references as each query arrives. A lightweight post-processing layer atop any pre-trained VPR backbone, TRAIL improves a state-of-the-art baseline by up to 8.3 percentage points on our primary benchmark, transfers to unseen datasets without retraining, and delivers its largest gains where visual cues are scarce.

---


### 291. [Impact of canny edge detection preprocessing on performance of machine learning models for Parkinson's disease classification](https://arxiv.org/abs/2609.07408)

**<font color=#1a73e8>作者：</font>** Sameer Bhat, Piotr Szczuko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study investigates the classification of individuals as healthy or at risk of Parkinson's disease using machine learning (ML) models, focusing on the impact of dataset size and preprocessing techniques on model performance. Four datasets are created from an original dataset: DS_0, (normal dataset), DS_1 (DS_O subjected to Canny edge detection and Hessian filtering), DS_2 (augmented DS_0), and DS_3 (augmented DS_1). We evaluate a range of ML models-Logistic Regression (LR), Decision Tree (DT), Random Forest (RF), Gradient Boosting (GB), XGBoost (XBG), Naive Bayes (NB), Support Vector Machine (SVM), and AdaBoost (AdB)-on these datasets, analyzing prediction accuracy, model size, and prediction latency. The results show that while larger datasets lead to increased model memory footprints and prediction latencies, the Canny edge detection preprocessing supplemented by Hessian filtering (used in DS_1 and DS_3) degrades the performance of most models. In our experiment, we observe that Random Forest (RF) maintains a stable memory footprint of 61 KB across all datasets, while models like KNN and SVM show significant increases in memory usage, from 5.7-7 KB on DS_0 to 102-220 KB on DS_2, and similar increases in prediction time. Logistic Regression, Decision Tree, and Naive Bayes show stable memory footprints and fast prediction times across all datasets. XGBoost's prediction time increases from 180-200 ms on DS_0 to 700-3000 ms on DS_2 (truncated)

---


### 292. [RAFM-SER++: A Lightweight Multimodal Emotion Recognition Framework for Real-Time Behavioral Monitoring in Surveillance Systems](https://arxiv.org/abs/2609.07409)

**<font color=#1a73e8>作者：</font>** Ngo Truong Dinh, Tung-Lam Bui, Chi-Trung Duong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multimodal Speech Emotion Recognition (SER) systems achieve high accuracy through interaction-heavy cross-modal transformers, but their computational cost limits deployment in latency-sensitive and resource-constrained surveillance systems. To address this challenge, we propose RAFM_SER++, a lightweight multimodal SER framework featuring an asymmetric Residual Attention Fusion Mechanism (RAFM). Rather than relying on computationally expensive bidirectional interactions, RAFM injects affective speech cues into semantic text representations through a one-directional residual attention pathway. Combined with a BYOL-inspired cross-modal alignment objective and attention-guided pooling, the proposed framework improves multimodal representation learning while maintaining low computational overhead.
Experiments on the IEMOCAP and ESD benchmarks demonstrate that RAFM_SER++ consistently outperforms the HuBERT-Base baseline and achieves a superior accuracy-efficiency trade-off compared with the state-of-the-art MemoCMT. Specifically, RAFM_SER++ reduces trainable parameters by more than 60%, achieves faster inference (79.60 it/s), and attains BACC scores of 81.10% on IEMOCAP and 95.39% on ESD. These results indicate that lightweight asymmetric multimodal fusion is an effective alternative to interaction-heavy cross-modal transformers for real-time surveillance applications.

---


### 293. [Multi-label versus multi-class classification of blood cells and their aggregates in microfluidic channels](https://arxiv.org/abs/2609.07410)

**<font color=#1a73e8>作者：</font>** Igor Zingman, Shada Abuhattum, Sara Kaliman 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformability cytometry (DC) is a type of imaging flow cytometry, which uses a camera-equipped device to measure cellular stiffness in addition to other cellular properties at high throughput. Cellular properties such as area and elongation can identify cell types, but this requires prior knowledge of distinguishing properties and cannot be applied to clinically important cell aggregates. Using DC data, we evaluated conventional multi-class (MC) classification and introduced a multi-label (ML) approach for identifying blood cells and their aggregates. In particular, an ML classifier can simultaneously assign multiple cell-type labels to a single imaged event. We show that, unlike MC classification, ML classification can identify cell aggregates not represented in the training data. It also avoids the need for exhaustive, strictly defined aggregate labels, thereby simplifying and speeding up annotation. Since automated blood analyzers do not reliably analyze cell aggregates, our approach may help address this clinical gap.

---


### 294. [RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting](https://arxiv.org/abs/2609.07414)

**<font color=#1a73e8>作者：</font>** Hejun Wang, Jinxi Li, Junwei Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image relighting is traditionally tackled via complex inverse rendering pipelines, which suffer from ill-posed optimization, or single-image generative models that ignore crucial multi-view cues necessary for understanding 3D geometry and material interactions. To address these limitations, we introduce a feed-forward generative Transformer for direct single- and multi-view image relighting that entirely bypasses explicit intrinsic property estimation. Adapted from a video foundation model, our architecture features a latent illumination module that dynamically injects target environment maps into spatial features via cross-attention. Furthermore, we employ permutation-invariant positional encodings to symmetrically process unordered multi-view inputs without sequential bias. To train this robust data-driven model, we construct the massive Laval Objaverse Dataset (LOD), comprising 90K objects and 39K unique illuminations. Extensive experiments demonstrate state-of-the-art visual quality, photorealistic relighting quality, and strong zero-shot generalization across single-view, multi-view, and novel-view relighting tasks.

---


### 295. [Self-Supervised Multi-View 3D Gaze Target Estimation via Probabilistic Ray Marching](https://arxiv.org/abs/2609.07415)

**<font color=#1a73e8>作者：</font>** Keqi Chen, Vinkle Srivastav, Nicolas Padoy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a self-supervised approach, Self-MVGTE, for estimating 3D gaze targets from multiple camera views. Unlike existing methods that independently estimate 2D gaze targets per camera view, Self-MVGTE predicts gaze targets directly in 3D space for the first time. Moreover, it does not require any ground-truth annotations from the target scene and uses only the multi-view input images from a calibrated camera setup, pseudo 2D gaze target labels from a monocular gaze target estimation model, and 3D gaze vectors from a monocular 3D gaze estimation model. A key challenge is that these pseudo labels are inherently noisy and multi-view inconsistent. To address this, we propose a probabilistic ray marching framework, which models the uncertainty of these pseudo labels and exploits 3D gaze vectors as geometric priors. Specifically, these gaze vectors are first integrated into the monocular gaze target estimation model to improve its generalization to unseen scenes, producing higher-quality pseudo labels. Then, for 3D gaze target estimation, we construct a 3D gaze cone by casting a bundle of rays from the eye position around the gaze vector to strictly constrain the solution space. Within this cone, we propose a depth-guided feature sampling strategy using off-the-shelf DINOv2 and Depth-Anything-3 models, and estimate a spatial likelihood distribution of the gaze target. Finally, we convert the pseudo gaze target labels into a target distribution and softly optimize the network. Extensive experiments on the MVGT dataset show that Self-MVGTE achieves state-of-the-art performance, surpassing existing fully-supervised baselines.

---


### 296. [Revisiting Thinning Methods for Kernel Learning Problems](https://arxiv.org/abs/2609.07432)

**<font color=#1a73e8>作者：</font>** Blanca Cano-Camarero, Yago R. Aguado-Carrillo-de-Albornoz, Ángela Fernández-Pascual 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel methods are widely used because of their strong theoretical guarantees and empirical performance. However, their high computational cost limits their applicability to large-scale datasets. To address this shortcoming, several approaches use Maximum Mean Discrepancy to construct representative subsets that preserve the properties of the full dataset in a Reproducing Kernel Hilbert Space. We introduce Backward Kernel Herding, an algorithm that addresses this problem by iteratively removing points from the dataset, achieving results comparable to current state-of-the-art approaches while accelerating the subsampling process in realistic scenarios where the reduced size is less than half of the dataset. Moreover, we overcome a limitation of Kernel Thinning by proposing an extension that enables the construction of subsets of arbitrary size rather that restricting to successive halvings. Finally, we conduct an extensive experimental comparison focusing on the most relevant kernel learning procedures: Gaussian Processes and Kernel Support Vector Machines. The results show that Backward Kernel Herding consistently achieves competitive performance with the most favorable training-time efficiency, while the proposed Flexible Kernel Thinning frequently achieves the best predictive performance. These gains become especially pronounced for moderate compression ratios, highlighting the benefits of incorporating supervised information into the thinning process. In terms of memory consumption, Flexible Kernel Thinning is also competitive, whereas Backward Kernel Herding remains an alternative when computational efficiency is the primary objective. Overall, no single method dominates across all scenarios, underscoring the importance of selecting the reduction strategy according to the desired trade-off between predictive performance, training cost, and memory requirements.

---


### 297. [AFID: A Unified Open Framework for Automated Fingermark Identification, Quality Assessment and Feature Extraction](https://arxiv.org/abs/2609.07439)

**<font color=#1a73e8>作者：</font>** Tim Oblak, Rudolf Haraksim, Peter Peer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated fingermark identification is the foundation of forensic investigation, yet progress in the field is held back by fragmented, closed-source solutions trained on private or discontinued data. We present AFID, a unified open-source framework for friction ridge image processing that performs recognition, quality assessment, and feature extraction based on a single shared encoder, trained exclusively on publicly available data. At its core is a fixed-length representation learned for identity discrimination, trained under heavy augmentation. Despite applying essentially no preprocessing beyond resizing and padding at inference, AFID sets a new state of the art in fixed-length fingermark recognition, leading identification across NIST SD 27 (67.6% rank-1) , SD 302 (54.9% rank-1), and SD 303 (67.6% rank-1), surpassing a commercial matcher on fingermarks. From the same frozen backbone, a quality assessment module predicts recognition utility more accurately than any compared baseline and generalizes across independent matchers, while lightweight decoders recover minutiae, ridge orientation, and segmentation competitive with dedicated methods. The framework proves that a single, efficiently trained encoder can support the full fingermark processing pipeline, from recognition through quality assessment all the way to feature extraction. To accelerate research on fingermark analysis even further, we release the code, models, and annotations to the community.

---


### 298. [TabBench-Bio: A Living Benchmark for Machine Learning on High-Dimensional Biomedical Tables](https://arxiv.org/abs/2609.07441)

**<font color=#1a73e8>作者：</font>** Jules Kreuer, Sofiane Ouaari, Julia Hellmig 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biomedical tables often combine thousands of measured variables with only tens or hundreds of labelled samples, a regime that is poorly represented in general-purpose tabular benchmarks. We introduce TabBench-Bio, a living and interactive benchmark of 43 biomedical datasets spanning multiple domains. Under a shared cross-validation protocol, we compare classical estimators, neural networks, and tabular foundation models across 28 feature-by-sample operating points. At the reference cell of 10,000 features and 100 training samples, RealTabPFN v2.5 has the highest point estimate, followed by Logistic Regression and TabDPT, whose point estimates are nearly identical. A paired bootstrap over the target pool separates RealTabPFN v2.5 from Logistic Regression by 145 Elo (95% interval [59, 232]). Tabular foundation models generally occupy the leading ranks, while the strongest configuration depends on the operating point and biomedical modality. The AutoML framework AutoGluon, using its one-hour "extreme" preset, is configured as a separate resource-intensive reference and is reported here at the reference cell. Fold-level predictions, run status, and deterministic aggregations make every reported result reproducible and reusable.
We invite the community to contribute: TabBench-Bio is designed to grow, and we welcome submissions of new biomedical tabular datasets, particularly from underrepresented assays and clinical endpoints, for inclusion in future releases.
The interactive leaderboard is available at: this https URL

---


### 299. [TASTE: Throughput-Aware Batch Size Tuning for On-Device Edge Learning](https://arxiv.org/abs/2609.07444)

**<font color=#1a73e8>作者：</font>** Avik Bhatnagar, Federico Nicolas Peccia, Oliver Bringmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rise of privacy-preserving artificial intelligence (AI) has shifted the focus of model adaptation and personalization towards on-device learning, where deep learning models are finetuned directly on edge hardware using local user data. However, this shift requires optimization of deep learning training on resource-constrained hardware to maximize throughput while maintaining predictive accuracy. This paper introduces a novel technique for on-device model training that incorporates an efficient Bayesian optimization-based batch size tuning approach to maximize hardware throughput. To evaluate the impact of this hyperparameter on the learning dynamics, we investigated two distinct paradigms: standard supervised learning (SL) and online continual learning (CL). Experimental results across various edge devices demonstrate a throughput ceiling, beyond which increasing the batch size yields no additional throughput gains. The proposed tuning approach identifies the optimal batch size, which, when combined with gradient accumulation and linear learning rate scaling, achieves up to a 2X increase in training throughput on platforms such as Raspberry Pi 4 compared to maximum batch sizes, without compromising model accuracy. Furthermore, in the CL paradigm, we demonstrate that optimal batch sizes maintain the stability-plasticity balance required for incremental learning, effectively mitigating catastrophic forgetting while maximizing computational efficiency on edge-hardware.

---


### 300. [Latent-to-Latent Flow for Volumetric Stochastic Segmentation](https://arxiv.org/abs/2609.07460)

**<font color=#1a73e8>作者：</font>** Omar Todd, Sooha Kim, Raghav Mehta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncertainty arising from inter-observer variability in medical image segmentation plays an important role in developing treatment plans. Research in this area is inhibited by the lack of multiple annotations for large-scale medical datasets, especially for volumetric data, which suffers from additional scaling and computational complexity challenges. Flow matching has emerged as a powerful framework for generative modelling and has also been demonstrated to maintain strong performance when working with latent representations of images. In this work, we introduce a latent-to-latent flow technique for stochastic segmentation of medical volumes via encoded representations of both the image and label space. We evaluate our method on two challenging applications covering delineation uncertainty for radiotherapy planning and multiple organ structure segmentation, improving efficiency up to 14x compared with full resolution models while maintaining clinically relevant performance.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
