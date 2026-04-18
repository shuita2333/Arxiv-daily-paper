# 📦 其他研究 | 2026年04月18日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 51. [Asynchronous Probability Ensembling for Federated Disaster Detection](https://arxiv.org/abs/2604.14450)

**<font color=#1a73e8>作者：</font>** Emanuel Teixeira Martins, Rodrigo Moreira, Larissa Ferreira Rodrigues Moreira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quick and accurate emergency handling in Disaster Decision Support Systems (DDSS) is often hampered by network latency and suboptimal application accuracy. While Federated Learning (FL) addresses some of these issues, it is constrained by high communication costs and rigid synchronization requirements across heterogeneous convolutional neural network (CNN) architectures. To overcome these challenges, this paper proposes a decentralized ensembling framework based on asynchronous probability aggregation and feedback distillation. By shifting the exchange unit from model weights to class-probability vectors, our method maintains data privacy, reduces communication requirements by orders of magnitude, and improves overall accuracy. This approach enables diverse CNN designs to collaborate asynchronously, enhancing disaster image identification performance even in resource-constrained settings. Experimental tests demonstrate that the proposed method outperforms traditional individual backbones and standard federated approaches, establishing a scalable and resource-aware solution for real-time disaster response.

---


### 52. [FocalLens: Visualizing Narratives through Focalization](https://arxiv.org/abs/2604.14456)

**<font color=#1a73e8>作者：</font>** S M Raihanul Alam, Md Dilshadur Rahman, Md Naimul Hoque  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualizing narratives is useful to writers to reflect on unfinished drafts and identify unintentional biases and inconsistencies. Literary scholars can use the visualizations to identify nuanced patterns and literary styles from written text. Current narrative visualization is limited to representing character and location co-occurrences in a timeline, omitting important and complex narrative components such as focalization, causality, and speech. This paper aims to capture and visualize underexplored, complex narrative components as a basis for narrative visualization. As a starting point, we propose a new narrative visualization, named FocalLens, that uses focalization, the component that establishes who sees or perceives the events in a narrative, for representing the narrative. We provide the theoretical foundation of focalization and describe various types and facets of focalization. The details are incorporated in the novel visualization that captures how different characters perceive an event, who directly participate in an event, who indirectly observe the event, and who narrate the event. We also developed a tool that provides fluid interaction between the text and the proposed visualization. The tool was evaluated with four writers and scholars in a qualitative study, where writers analyzed their draft stories and scholars analyzed well-known stories. The findings suggest the tool added a new dimension to the workflow for writers and scholars, an analytical lens that is not available otherwise. We conclude by identifying design implications and future directions.

---


### 53. [NeuroTrace: Inference Provenance-Based Detection of Adversarial Examples](https://arxiv.org/abs/2604.14457)

**<font color=#1a73e8>作者：</font>** Firas Ben Hmida, Philemon Hailemariam, Kashif Ali Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) remain largely opaque at inference time, limiting our ability to detect and diagnose malicious input manipulations such as adversarial examples. Existing detection methods predominantly rely on layer-local signals (e.g., activations or attribution scores), leaving cross-layer information flow and execution structure under-explored. We introduce NeuroTrace, a framework and open dataset for analyzing inference provenance through Inference Provenance Graphs (IPGs). IPGs are heterogeneous graphs that capture both activation behavior and parameter-induced dataflow during a model's forward pass, providing a structured representation of how information propagates through the network. NeuroTrace includes (i) a reproducible extraction engine that instruments model execution, (ii) a standardized graph representation compatible with heterogeneous GNNs, and (iii) a benchmark suite spanning multiple adversarial attack families across vision and malware domains. Using this framework, we evaluate IPG-based detectors for adversarial example detection under intra-attack, multi-attack, and cross-threat transfer settings. Our results show that inference provenance provides a strong and transferable signal for distinguishing adversarial and benign inputs, achieving consistently high detection performance and improving over prior graph-based baselines. We further analyze the conditions under which provenance-based detection generalizes across attack types, as well as the associated runtime and storage trade-offs. By releasing the dataset, extraction pipeline, and evaluation protocol, NeuroTrace enables systematic study of inference-time behavior and establishes inference provenance as a practical foundation for building more transparent and auditable machine learning systems.

---


### 54. [Filling in the Mechanisms: How do LMs Learn Filler-Gap Dependencies under Developmental Constraints?](https://arxiv.org/abs/2604.14459)

**<font color=#1a73e8>作者：</font>** Atrey Desai, Sathvik Nair  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For humans, filler-gap dependencies require a shared representation across different syntactic constructions. Although causal analyses suggest this may also be true for LLMs (Boguraev et al., 2025), it is still unclear if such a representation also exists for language models trained on developmentally feasible quantities of data. We applied Distributed Alignment Search (DAS, Geiger et al. (2024)) to LMs trained on varying amounts of data from the BabyLM challenge (Warstadt et al., 2023), to evaluate whether representations of filler-gap dependencies transfer between wh-questions and topicalization, which greatly vary in terms of their input frequency. Our results suggest shared, yet item-sensitive mechanisms may develop with limited training data. More importantly, LMs still require far more data than humans to learn comparable generalizations, highlighting the need for language-specific biases in models of language acquisition.

---


### 55. [Bias in Surface Electromyography Features across a Demographically Diverse Cohort](https://arxiv.org/abs/2604.14460)

**<font color=#1a73e8>作者：</font>** Aditi Agrawal, Celine John Philip, Giancarlo K. Sagastume 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Neuromotor decoding from upper-limb electromyography (sEMG) can enhance human-machine interfaces and offer a more natural means of controlling prosthetic limbs, virtual reality, and household electronics. Unfortunately, current sEMG technology does not always perform consistently across users because individual differences such as age and body mass index, among many others, can substantially alter signal quality. This variability makes sEMG characteristics highly idiosyncratic, often necessitating laborious personalization and iterative tuning to achieve reliable performance. This variability has particular import for sEMG-based assistive devices and neural interfaces, where demographic biases in sEMG features could undermine broad and fair deployment.
In this study, we explore how demographic differences affect the sEMG signals produced and their implications for machine learning-based gesture decoding. We analyze the data set provided by, in which we derive 147 common sEMG features extracted from 81 demographically diverse individuals performing discrete hand gestures. Using mixed-effects linear models and partial least squares (PLS) analysis, which take into consideration demographic variables (including age, sex, height, weight, skin properties, subcutaneous fat, and hair density), we identify that 33\% (49 of 147) of commonly used sEMG features show significant associations with demographic characteristics. These results may help guide the development of fair and unbiased sEMG-based neural interfaces across a diverse population.

---


### 56. [Improving Human Performance with Value-Aware Interventions: A Case Study in Chess](https://arxiv.org/abs/2604.14465)

**<font color=#1a73e8>作者：</font>** Saumik Narayanan, Raja Panjwani, Siddhartha Sen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly used to assist humans in sequential decision-making tasks, yet determining when and how an AI assistant should intervene remains a fundamental challenge. A potential baseline is to recommend the optimal action according to a strong model. However, such actions assume optimal follow-up actions, which human decision makers may fail to execute, potentially reducing overall performance. In this work, we propose and study value-aware interventions, motivated by a basic principle in reinforcement learning: under the Bellman equation, the optimal policy selects actions that maximize the immediate reward plus the value function. When a decision maker follows a suboptimal policy, this policy-value consistency no longer holds, creating discrepancies between the actions taken by the policy and those that maximize the immediate reward plus the value of the next state. We show that these policy-value inconsistencies naturally identify opportunities for intervention. We formalize this problem in a Markov decision process where an AI assistant may override human actions under an intervention budget. In the single-intervention regime, we show that the optimal strategy is to recommend the action that maximizes the human value function. For settings with multiple interventions, we propose a tractable approximation that prioritizes interventions based on the magnitude of the policy-value discrepancy. We evaluate these ideas in the domain of chess by learning models of humans from large-scale gameplay data. In simulation, our approach consistently outperforms interventions based on the strongest chess engine (Stockfish) in a wide range of settings. A within-subject human study with 20 players and 600 games further shows that our interventions significantly improve performance for low- and mid-skill players while matching expert-engine interventions for high-skill players.

---


### 57. [Auxiliary Finite-Difference Residual-Gradient Regularization for PINNs](https://arxiv.org/abs/2604.14472)

**<font color=#1a73e8>作者：</font>** Stavros Kassinos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) are often selected by a single scalar loss even when the quantity of interest is more specific. We study a hybrid design in which the governing PDE residual remains automatic-differentiation (AD) based, while finite differences (FD) appear only in a weak auxiliary term that penalizes gradients of the sampled residual field. The FD term regularizes the residual field without replacing the PDE residual itself.
We examine this idea in two stages. Stage 1 is a controlled Poisson benchmark comparing a baseline PINN, the FD residual-gradient regularizer, and a matched AD residual-gradient baseline. Stage 2 transfers the same logic to a three-dimensional annular heat-conduction benchmark (PINN3D), where baseline errors concentrate near a wavy outer wall and the auxiliary grid is implemented as a body-fitted shell adjacent to the wall.
In Stage 1, the FD regularizer reproduces the main effect of residual-gradient control while exposing a trade-off between field accuracy and residual cleanliness. In Stage 2, the shell regularizer improves the application-facing quantities, namely outer-wall flux and boundary-condition behavior. Across seeds 0-5 and 100k epochs, the most reliable tested configuration is a fixed shell weight of 5e-4 under the Kourkoutas-beta optimizer regime: relative to a matched run without the shell term, it reduces the mean outer-wall BC RMSE from 1.22e-2 to 9.29e-4 and the mean wall-flux RMSE from 9.21e-3 to 9.63e-4. Adam with beta2=0.999 becomes usable when the initial learning rate is reduced to 1e-3, although its shell benefit is less robust than under Kourkoutas-beta. Overall, the results support a targeted view of hybrid PINNs: an auxiliary-only FD regularizer is most valuable when it is aligned with the physical quantity of interest, here the outer-wall flux.

---


### 58. [Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers](https://arxiv.org/abs/2604.14477)

**<font color=#1a73e8>作者：</font>** Nina Żukowska, Wolfgang Stammer, Bernt Schiele 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transparency of neural networks' internal reasoning is at the heart of interpretability research, adding to trust, safety, and understanding of these models. The field of mechanistic interpretability has recently focused on studying task-specific computational graphs, defined by connections (edges) between model components. Such edge-based circuits have been defined in the context of large language models, yet vision-based approaches so far only consider neuron-based circuits. These tell which information is encoded, but not how it is routed through the complex wiring of a neural network. In this work, we investigate whether useful mechanistic circuits can be identified through computational graphs in vision transformers. We propose an effective method for Automatic Visual Circuit Discovery (Vi-CD) that recovers class-specific circuits for classification, identifies circuits underlying typographic attacks in CLIP, and discovers circuits that lend themselves for steering to correct harmful model behavior. Overall, we find that insightful and actionable edge-based circuits can be recovered from vision transformers, adding transparency to the internal computations of these models.

---


### 59. [Quantization of Spiking Neural Networks Beyond Accuracy](https://arxiv.org/abs/2604.14487)

**<font color=#1a73e8>作者：</font>** Evan Gibson Smith, Jacob Whitehill, Fatemeh Ganji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is a natural complement to the sparse, event-driven computation of Spiking Neural Networks, reducing memory bandwidth and arithmetic cost for deployment on resource-constrained hardware. However, existing SNN quantization evaluation focuses almost exclusively on accuracy, overlooking whether a quantized network preserves the firing behavior of its full-precision counterpart. We demonstrate that quantization method, clipping range, and bit-width can produce substantially different firing distributions at equivalent accuracy, differences invisible to standard metrics but relevant to deployment, where firing activity governs effective sparsity, state storage, and event-processing load. To capture this gap, we propose Earth Mover's Distance as a diagnostic metric for firing distribution divergence, and apply it systematically across weight and membrane quantization on SEW-ResNet architectures trained on CIFAR-10 and CIFAR-100. We find that uniform quantization induces distributional drift even when accuracy is preserved, while LQ-Net style learned quantization maintains firing behavior close to the full-precision baseline. Our results suggest that behavior preservation should be treated as an evaluation criterion alongside accuracy, and that EMD provides a principled tool for assessing it.

---


### 60. [CobwebTM: Probabilistic Concept Formation for Lifelong and Hierarchical Topic Modeling](https://arxiv.org/abs/2604.14489)

**<font color=#1a73e8>作者：</font>** Karthik Singaravadivelan, Anant Gupta, Zekun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic modeling seeks to uncover latent semantic structure in text corpora with minimal supervision. Neural approaches achieve strong performance but require extensive tuning and struggle with lifelong learning due to catastrophic forgetting and fixed capacity, while classical probabilistic models lack flexibility and adaptability to streaming data. We introduce \textsc{CobwebTM}, a low-parameter lifelong hierarchical topic model based on incremental probabilistic concept formation. By adapting the Cobweb algorithm to continuous document embeddings, \textsc{CobwebTM} constructs semantic hierarchies online, enabling unsupervised topic discovery, dynamic topic creation, and hierarchical organization without predefining the number of topics. Across diverse datasets, \textsc{CobwebTM} achieves strong topic coherence, stable topics over time, and high-quality hierarchies, demonstrating that incremental symbolic concept formation combined with pretrained representations is an efficient approach to topic modeling.

---


### 61. [Improving Machine Learning Performance with Synthetic Augmentation](https://arxiv.org/abs/2604.14498)

**<font color=#1a73e8>作者：</font>** Mel Sohm, Charles Dezons, Sami Sellami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic augmentation is increasingly used to mitigate data scarcity in financial machine learning, yet its statistical role remains poorly understood. We formalize synthetic augmentation as a modification of the effective training distribution and show that it induces a structural bias--variance trade-off: while additional samples may reduce estimation error, they may also shift the population objective whenever the synthetic distribution deviates from regions relevant under evaluation. To isolate informational gains from mechanical sample-size effects, we introduce a size-matched null augmentation and a finite-sample, non-parametric block permutation test that remains valid under weak temporal dependence.
We evaluate this framework in both controlled Markov-switching environments and real financial datasets, including high-frequency option trade data and a daily equity panel. Across generators spanning bootstrap, copula-based models, variational autoencoders, diffusion models, and TimeGAN, we vary augmentation ratio, model capacity, task type, regime rarity, and signal-to-noise. We show that synthetic augmentation is beneficial only in variance-dominant regimes, such as persistent volatility forecasting-while it deteriorates performance in bias-dominant settings, including near-efficient directional prediction. Rare-regime targeting can improve domain-specific metrics but may conflict with unconditional permutation inference. Our results provide a structural perspective on when synthetic data improves financial learning performance and when it induces persistent distributional distortion.

---


### 62. [On the Expressive Power and Limitations of Multi-Layer SSMs](https://arxiv.org/abs/2604.14501)

**<font color=#1a73e8>作者：</font>** Nikola Zubić, Qian Li, Yuyi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the expressive power and limitations of multi-layer state-space models (SSMs). First, we show that multi-layer SSMs face fundamental limitations in compositional tasks, revealing an inherent gap between SSMs and streaming models. Then, we examine the role of chain-of-thought (CoT), showing that offline CoT does not fundamentally increase the expressiveness, while online CoT can substantially increase its power. Indeed, with online CoT, multi-layer SSMs become equivalent in power to streaming algorithms. Finally, we investigate the tradeoff between width and precision, showing that these resources are not interchangeable in the base model, but admit a clean equivalence once online CoT is allowed. Overall, our results offer a unified perspective on how depth, finite precision, and CoT shape the power and limits of SSMs.

---


### 63. [Co-distilled attention guided masked image modeling with noisy teacher for self-supervised learning on medical images](https://arxiv.org/abs/2604.14506)

**<font color=#1a73e8>作者：</font>** Jue Jiang, Aneesh Rangnekar, Harini Veeraraghavan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Masked image modeling (MIM) is a highly effective self-supervised learning (SSL) approach to extract useful feature representations from unannotated data. Predominantly used random masking methods make SSL less effective for medical images due to the contextual similarity of neighboring patches, leading to information leakage and SSL simplification. Hierarchical shifted window (Swin) transformer, a highly effective approach for medical images cannot use advanced masking methods as it lacks a global [CLS] token. Hence, we introduced an attention guided masking mechanism for Swin within a co-distillation learning framework to selectively mask semantically co-occurring and discriminative patches, to reduce information leakage and increase the difficulty of SSL pretraining. However, attention guided masking inevitably reduces the diversity of attention heads, which negatively impacts downstream task performance. To address this, we for the first time, integrate a noisy teacher into the co-distillation framework (termed DAGMaN) that performs attentive masking while preserving high attention head diversity. We demonstrate the capability of DAGMaN on multiple tasks including full- and few-shot lung nodule classification, immunotherapy outcome prediction, tumor segmentation, and unsupervised organs clustering.

---


### 64. [H2VLR: Heterogeneous Hypergraph Vision-Language Reasoning for Few-Shot Anomaly Detection](https://arxiv.org/abs/2604.14507)

**<font color=#1a73e8>作者：</font>** Jianghong Huang, Luping Ji, Weiwei Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a classic vision task, anomaly detection has been widely applied in industrial inspection and medical imaging. In this task, data scarcity is often a frequently-faced issue. To solve it, the few-shot anomaly detection (FSAD) scheme is attracting increasing attention. In recent years, beyond traditional visual paradigm, Vision-Language Model (VLM) has been extensively explored to boost this field. However, in currently-existing VLM-based FSAD schemes, almost all perform anomaly inference only by pairwise feature matching, ignoring structural dependencies and global consistency. To further redound to FSAD via VLM, we propose a Heterogeneous Hypergraph Vision-Language Reasoning (H2VLR) framework. It reformulates the FSAD as a high-order inference problem of visual-semantic relations, by jointly modeling visual regions and semantic concepts in a unified hypergraph. Experimental comparisons verify the effectiveness and advantages of H2VLR. It could often achieve state-of-the-art (SOTA) performance on representative industrial and medical benchmarks. Our code will be released upon acceptance.

---


### 65. [CBCL: Safe Self-Extending Agent Communication](https://arxiv.org/abs/2604.14512)

**<font color=#1a73e8>作者：</font>** Hugo O'Connor  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent communication languages (ACLs) enable heterogeneous agents to share knowledge and coordinate across diverse domains. This diversity demands extensibility, but expressive extension mechanisms can push the input language beyond the complexity classes where full validation is tractable. We present CBCL (Common Business Communication Language), an agent communication language that constrains all messages, including runtime language extensions, to the deterministic context-free language (DCFL) class. CBCL allows agents to define, transmit, and adopt domain-specific "dialect" extensions as first-class messages; three safety invariants (R1--R3), machine-checked in Lean 4 and enforced in a Rust reference implementation, prevent unbounded expansion, applying declared resource limits, and preserving core vocabulary. We formalize the language and its safety properties in Lean 4, implement a reference parser and dialect engine in Rust with property-based and differential tests, and extract a verified parser binary. Our results demonstrate that homoiconic protocol design, where extension definitions share the same representation as ordinary messages, can be made provably safe. As autonomous agents increasingly extend their own communication capabilities, formally bounding what they can express to each other is a precondition for oversight.

---


### 66. [PeerPrism: Peer Evaluation Expertise vs Review-writing AI](https://arxiv.org/abs/2604.14513)

**<font color=#1a73e8>作者：</font>** Soroush Sadeghian, Alireza Daqiq, Radin Cheraghi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in scientific peer review, assisting with drafting, rewriting, expansion, and refinement. However, existing peer-review LLM detection methods largely treat authorship as a binary problem-human vs. AI-without accounting for the hybrid nature of modern review workflows. In practice, evaluative ideas and surface realization may originate from different sources, creating a spectrum of human-AI collaboration.
In this work, we introduce PeerPrism, a large-scale benchmark of 20,690 peer reviews explicitly designed to disentangle idea provenance from text provenance. We construct controlled generation regimes spanning fully human, fully synthetic, and multiple hybrid transformations. This design enables systematic evaluation of whether detectors identify the origin of the surface text or the origin of the evaluative reasoning. We benchmark state-of-the-art LLM text detection methods on PeerPrism. While several methods achieve high accuracy on the standard binary task (human vs. fully synthetic), their predictions diverge sharply under hybrid regimes. In particular, when ideas originate from humans but the surface text is AI-generated, detectors frequently disagree and produce contradictory classifications. Accompanied by stylometric and semantic analyses, our results show that current detection methods conflate surface realization with intellectual contribution.
Overall, we demonstrate that LLM detection in peer review cannot be reduced to a binary attribution problem. Instead, authorship must be modeled as a multidimensional construct spanning semantic reasoning and stylistic realization. PeerPrism is the first benchmark evaluating human-AI collaboration in these settings. We release all code, data, prompts, and evaluation scripts to facilitate reproducible research at this https URL.

---


### 67. [Perspective on Bias in Biomedical AI: Preventing Downstream Healthcare Disparities](https://arxiv.org/abs/2604.14514)

**<font color=#1a73e8>作者：</font>** Michal Rosen-Zvi, Yoav Kan-Tor, Michael Danziger 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare disparities persist across socioeconomic boundaries, often attributed to unequal access to screening, diagnostics, and therapeutics. However, this perspective highlights that critical biases can emerge much earlier, during data collection and research prioritization, long before clinical implementation in cases where the focus of the studies and the data that is collected is at the molecular level. A vast number of studies focus on collecting omics data but the demographic information associated with these datasets is often not reported in the studies, and when it is reported, it shows big biases. An automated analysis of 4719 PubMed-indexed omics publications from 2015 to 2024 reveals that only a small fraction report ancestry or ethnicity information, with ancestry reporting improving slightly. Analysis of large-scale datasets commonly used for model training, such as CellxGene and GEO, reveals substantial population bias where European-ancestry data dominates. As biomedical foundation models become central to biomedical discovery with a paradigm in which base models are pretrained on large datasets and reusing them time and again for many different downstream tasks, they risk perpetuating or amplifying these early-stage biases, leading to cascading inequities that regulatory interventions cannot fully reverse. We propose a community-wide focus on three foundational principles: Provenance, Openness, and Evaluation Transparency to improve equity and robustness in biomedical AI. This approach aims to foster biomedical innovation that more effectively serves underserved populations and improves health outcomes.

---


### 68. [Mind DeepResearch Technical Report](https://arxiv.org/abs/2604.14518)

**<font color=#1a73e8>作者：</font>** MindDR Team, Li Auto Inc  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present \textbf{Mind DeepResearch (MindDR)}, an efficient multi-agent deep research framework that achieves leading performance with only \textasciitilde30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with \textasciitilde30B-scale models. Specifically, MindDR achieves 45.7\% on BrowseComp-ZH, 42.8\% on BrowseComp, 46.5\% on WideSearch, 75.0\% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce \textbf{MindDR Bench}, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.

---


### 69. [CI-CBM: Class-Incremental Concept Bottleneck Model for Interpretable Continual Learning](https://arxiv.org/abs/2604.14519)

**<font color=#1a73e8>作者：</font>** Amirhosein Javadi, Tuomas Oikarinen, Tara Javidi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a fundamental challenge in continual learning, in which models often forget previous knowledge when fine-tuned on a new task. This issue is especially pronounced in class incremental learning (CIL), which is the most challenging setting in continual learning. Existing methods to address catastrophic forgetting often sacrifice either model interpretability or accuracy. To address this challenge, we introduce ClassIncremental Concept Bottleneck Model (CI-CBM), which leverage effective techniques, including concept regularization and pseudo-concept generation to maintain interpretable decision processes throughout incremental learning phases. Through extensive evaluation on seven datasets, CI-CBM achieves comparable performance to black-box models and outperforms previous interpretable approaches in CIL, with an average 36% accuracy gain. CICBM provides interpretable decisions on individual inputs and understandable global decision rules, as shown in our experiments, thereby demonstrating that human understandable concepts can be maintained during incremental learning without compromising model performance. Our approach is effective in both pretrained and non-pretrained scenarios; in the latter, the backbone is trained from scratch during the first learning phase. Code is publicly available at this http URL.

---


### 70. [FreqTrack: Frequency Learning based Vision Transformer for RGB-Event Object Tracking](https://arxiv.org/abs/2604.14526)

**<font color=#1a73e8>作者：</font>** Jinlin You, Muyu Li, Xudong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing single-modal RGB trackers often face performance bottlenecks in complex dynamic scenes, while the introduction of event sensors offers new potential for enhancing tracking capabilities. However, most current RGB-event fusion methods, primarily designed in the spatial domain using convolutional, Transformer, or Mamba architectures, fail to fully exploit the unique temporal response and high-frequency characteristics of event data. To address this, we1 propose FreqTrack, a frequency-aware RGBE tracking framework that establishes complementary inter-modal correlations through frequency-domain transformations for more robust feature fusion. We design a Spectral Enhancement Transformer (SET) layer that incorporates multi-head dynamic Fourier filtering to adaptively enhance and select frequency-domain features. Additionally, we develop a Wavelet Edge Refinement (WER) module, which leverages learnable wavelet transforms to explicitly extract multi-scale edge structures from event data, effectively improving modeling capability in high-speed and low-light scenarios. Extensive experiments on the COESOT and FE108 datasets demonstrate that FreqTrack achieves highly competitive performance, particularly attaining leading precision of 76.6\% on the COESOT benchmark, validating the effectiveness of frequency-domain modeling for RGBE tracking.

---


### 71. [Design and Validation of a Low-Cost Smartphone Based Fluorescence Detection Platform Compared with Conventional Microplate Readers](https://arxiv.org/abs/2604.14527)

**<font color=#1a73e8>作者：</font>** Zhendong Cao, Katrina G. Salvante, Ash Parameswaran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A low cost fluorescence-based optical system is developed for detecting the presence of certain microorganisms and molecules within a diluted sample. A specifically designed device setup compatible with conventional 96 well plates is chosen to create an ideal environment in which a smart phone camera can be used as the optical detector. In comparison with conventional microplate reading machines such as Perkin Elmer Victor Machine, the device presented in this paper is not equipped with expensive elements such as exciter filer, barrier filter and photomultiplier; instead, a phone camera is all needed to detect fluorescence within the sample. The strategy being involved is to determine the relationship between the image color of the sample in RGB color space and the molar concentration of the fluorescence specimen in that sample. This manuscript is a preprint version of work related to a publication in IEEE. The final version may differ from this manuscript.

---


### 72. [CSRA: Controlled Spectral Residual Augmentation for Robust Sepsis Prediction](https://arxiv.org/abs/2604.14532)

**<font color=#1a73e8>作者：</font>** Honglin Guo, Rihao Chang, He Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of future risk and disease progression in sepsis is clinically important for early warning and timely intervention in intensive care. However, short-window sepsis prediction remains challenging, because shorter observation windows provide limited historical evidence, whereas longer prediction horizons reduce the number of patient trajectories with valid future supervision. To address this problem, we propose CSRA, a Controlled Spectral Residual Augmentation framework for short-window multi-system ICU time series. CSRA first groups variables by clinical systems and extracts system-level and global representations. It then performs input-adaptive residual perturbation in the spectral domain to generate structured and clinically plausible trajectory variations. To improve augmentation stability and controllability, CSRA is trained end-to-end with the downstream predictor under a unified objective, together with anchor consistency loss and controller regularization. Experiments on a MIMIC-IV sepsis cohort across multiple downstream models show that CSRA is consistently competitive and often superior, reducing regression error by 10.2\% in MSE and 3.7\% in MAE over the non-augmentation baseline, while also yielding consistent gains on classification. CSRA further maintains more favorable performance under shorter observation windows, longer prediction horizons, and smaller training data scales, while also remaining effective on an external clinical dataset~(ZiGongICUinfection), indicating stronger robustness and generalizability in clinically constrained settings.

---


### 73. [An unsupervised decision-support framework for multivariate biomarker analysis in athlete monitoring](https://arxiv.org/abs/2604.14534)

**<font color=#1a73e8>作者：</font>** Fernando Barcelos Rosito, Sebastião De Jesus Menezes, Simone Ferreira Sturza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose. Athlete monitoring is constrained by small cohorts, heterogeneous biomarker scales, limited feasibility of repeated sampling, and the lack of reliable injury ground truth. These limitations reduce the interpretability and utility of traditional univariate and binary risk models. This study addresses these challenges by proposing an unsupervised multivariate framework to identify latent physiological states in athletes using real data. Methods. We propose a modular computational framework that operates in the joint biomarker space, integrating preprocessing, clinical safety screening, unsupervised clustering, and centroid-based physiological interpretation. Profiles are learned exclusively from amateur soccer players during a competitive microcycle. Synthetic data augmentation evaluates robustness and scalability. Ward hierarchical clustering supports monitoring and etiological differentiation, while Gaussian Mixture Models (GMM) enable structural stability analysis in high-dimensional settings. Results. The framework identifies coherent profiles that distinguish mechanical damage from metabolic stress while preserving homeostatic states. Synthetic data augmentation demonstrates feasibility and detection of latent silent risk phenotypes typically missed by univariate monitoring. Structural analyses indicate robustness under augmentation and higher-dimensional settings. Conclusion. The framework enables interpretable identification of latent physiological states from multivariate biomarker data without injury labels. By distinguishing mechanisms and revealing silent risk patterns not captured by conventional monitoring, it provides actionable insights for individualized athlete monitoring and decision making.

---


### 74. [WILD-SAM: Phase-Aware Expert Adaptation of SAM for Landslide Detection in Wrapped InSAR Interferograms](https://arxiv.org/abs/2604.14540)

**<font color=#1a73e8>作者：</font>** Yucheng Pan, Heping Li, Zhangle Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting slow-moving landslides directly from wrapped Interferometric Synthetic Aperture Radar (InSAR) interferograms is crucial for efficient geohazard monitoring, yet it remains fundamentally challenged by severe phase ambiguity and complex coherence noise. While the Segment Anything Model (SAM) offers a powerful foundation for segmentation, its direct transfer to wrapped phase data is hindered by a profound spectral domain shift, which suppresses the high-frequency fringes essential for boundary delineation. To bridge this gap, we propose WILD-SAM, a novel parameter-efficient fine-tuning framework specifically designed to adapt SAM for high-precision landslide detection on wrapped interferograms. Specifically, the architecture integrates a Phase-Aware Mixture-of-Experts (PA-MoE) Adapter into the frozen encoder to align spectral distributions and introduces a Wavelet-Guided Subband Enhancement (WGSE) strategy to generate frequency-aware dense prompts. The PA-MoE Adapter exploits a dynamic routing mechanism across heterogeneous convolutional experts to adaptively aggregate multi-scale spectral-textural priors, effectively aligning the distribution discrepancy between natural images and interferometric phase data. Meanwhile, the WGSE strategy leverages discrete wavelet transforms to explicitly disentangle high-frequency subbands and refine directional phase textures, injecting these structural cues as dense prompts to ensure topological integrity along sharp landslide boundaries. Extensive experiments on the ISSLIDE and ISSLIDE+ benchmarks demonstrate that WILD-SAM achieves state-of-the-art performance, significantly outperforming existing methods in both target completeness and contour fidelity.

---


### 75. [Giving Faces Their Feelings Back: Explicit Emotion Control for Feedforward Single-Image 3D Head Avatars](https://arxiv.org/abs/2604.14541)

**<font color=#1a73e8>作者：</font>** Yicheng Gong, Jiawei Zhang, Liqiang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a framework for explicit emotion control in feed-forward, single-image 3D head avatar reconstruction. Unlike existing pipelines where emotion is implicitly entangled with geometry or appearance, we treat emotion as a first-class control signal that can be manipulated independently and consistently across identities. Our method injects emotion into existing feed-forward architectures via a dual-path modulation mechanism without modifying their core design. Geometry modulation performs emotion-conditioned normalization in the original parametric space, disentangling emotional state from speech-driven articulation, while appearance modulation captures identity-aware, emotion-dependent visual cues beyond geometry. To enable learning under this setting, we construct a time-synchronized, emotion-consistent multi-identity dataset by transferring aligned emotional dynamics across identities. Integrated into multiple state-of-the-art backbones, our framework preserves reconstruction and reenactment fidelity while enabling controllable emotion transfer, disentangled manipulation, and smooth emotion interpolation, advancing expressive and scalable 3D head avatars.

---


### 76. [Controllable Video Object Insertion via Multiview Priors](https://arxiv.org/abs/2604.14556)

**<font color=#1a73e8>作者：</font>** Xia Qi, Peishan Cong, Yichen Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object insertion is a critical task for dynamically inserting new objects into existing environments. Previous video generation methods focus primarily on synthesizing entire scenes while struggling with ensuring consistent object appearance, spatial alignment, and temporal coherence when inserting objects into existing videos. In this paper, we propose a novel solution for Video Object Insertion, which integrates multi-view object priors to address the common challenges of appearance inconsistency and occlusion handling in dynamic environments. By lifting 2D reference images into multi-view representations and leveraging a dual-path view-consistent conditioning mechanism, our framework ensures stable identity guidance and robust integration across diverse viewpoints. A quality-aware weighting mechanism is also employed to adaptively handle noisy or imperfect inputs. Additionally, we introduce an Integration-Aware Consistency Module that guarantees spatial realism, effectively resolving occlusion and boundary artifacts while maintaining temporal continuity across frames. Experimental results show that our solution significantly improves the quality of video object insertion, providing stable and realistic integration.

---


### 77. [The Fourth Challenge on Image Super-Resolution ($\times$4) at NTIRE 2026: Benchmark Results and Method Overview](https://arxiv.org/abs/2604.14558)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Kai Liu, Jingkai Wang 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the NTIRE 2026 image super-resolution ($\times$4) challenge, one of the associated competitions of the NTIRE 2026 Workshop at CVPR 2026. The challenge aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs generated through bicubic downsampling with a $\times$4 scaling factor. The objective is to develop effective super-resolution solutions and analyze recent advances in the field. To reflect the evolving objectives of image super-resolution, the challenge includes two tracks: (1) a restoration track, which emphasizes pixel-wise fidelity and ranks submissions based on PSNR; and (2) a perceptual track, which focuses on visual realism and evaluates results using a perceptual score. A total of 194 participants registered for the challenge, with 31 teams submitting valid entries. This report summarizes the challenge design, datasets, evaluation protocol, main results, and methods of participating teams. The challenge provides a unified benchmark and offers insights into current progress and future directions in image super-resolution.

---


### 78. [DVFace: Spatio-Temporal Dual-Prior Diffusion for Video Face Restoration](https://arxiv.org/abs/2604.14560)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Bowen Chai, Rongjun Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video face restoration aims to enhance degraded face videos into high-quality results with realistic facial details, stable identity, and temporal coherence. Recent diffusion-based methods have brought strong generative priors to restoration and enabled more realistic detail synthesis. However, existing approaches for face videos still rely heavily on generic diffusion priors and multi-step sampling, which limit both facial adaptation and inference efficiency. These limitations motivate the use of one-step diffusion for video face restoration, yet achieving faithful facial recovery alongside temporally stable outputs remains challenging. In this paper, we propose, DVFace, a one-step diffusion framework for real-world video face restoration. Specifically, we introduce a spatio-temporal dual-codebook design to extract complementary spatial and temporal facial priors from degraded videos. We further propose an asymmetric spatio-temporal fusion module to inject these priors into the diffusion backbone according to their distinct roles. Evaluation on various benchmarks shows that DVFace delivers superior restoration quality, temporal consistency, and identity preservation compared to recent methods. Code: this https URL.

---


### 79. [Material-Agnostic Zero-Shot Thermal Inference for Metal Additive Manufacturing via a Parametric PINN Framework](https://arxiv.org/abs/2604.14562)

**<font color=#1a73e8>作者：</font>** Hyeonsu Lee, Jihoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate thermal modeling in metal additive manufacturing (AM) is essential for understanding the process-structure-performance relationship. While prior studies have explored generalization across unseen process conditions, they often require extensive datasets, costly retraining, or pre-training. Generalization across different materials also remains relatively unexplored due to the challenges posed by distinct material-dependent thermal behaviors. This paper introduces a parametric physics-informed neural network (PINN) framework for zero-shot generalization across arbitrary materials without labeled data, retraining, or pre-training. The framework adopts a decoupled parametric PINN architecture that separately encodes material properties and spatiotemporal coordinates, fusing them through conditional modulation to better align with the multiplicative role of material parameters in the governing equation and boundary conditions. Physics-guided output scaling derived from Rosenthal's analytical solution and a hybrid optimization strategy are further incorporated to enhance physical consistency, training stability, and convergence. Experiments on bare plate laser powder bed fusion (LPBF) across diverse metal alloys, including both in-distribution and out-of-distribution cases, demonstrate effective zero-shot generalizability along with superior training efficiency. Specifically, the proposed framework achieved up to a 64.2% reduction in relative L2 error compared to the non-parametric baseline while surpassing its performance within only 4.4% of the baseline training epochs. Ablation studies confirm that the proposed framework's components are broadly applicable to other PINN-based approaches. Overall, the proposed framework provides an efficient and scalable material-agnostic solution for zero-shot thermal modeling, contributing to more flexible and practical deployment in metal AM.

---


### 80. [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)

**<font color=#1a73e8>作者：</font>** Mingqian Ji, Shanshan Zhang, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing. To accelerate these models, token compression has been widely explored. However, our revisit of existing strategies, such as token pruning, merging, and patch size enlargement, reveals that they often discard informative background cues, disrupt contextual consistency, and lose fine-grained semantics, negatively affecting 3D detection. To overcome these limitations, we propose SEPatch3D, a novel framework that dynamically adjusts patch sizes while preserving critical semantic information within coarse patches. Specifically, we design Spatiotemporal-aware Patch Size Selection (SPSS) that assigns small patches to scenes containing nearby objects to preserve fine details and large patches to background-dominated scenes to reduce computation cost. To further mitigate potential detail loss, Informative Patch Selection (IPS) selects the informative patches for feature refinement, and Cross-Granularity Feature Enhancement (CGFE) injects fine-grained details into selected coarse patches, enriching semantic features. Experiments on the nuScenes and Argoverse 2 validation sets show that SEPatch3D achieves up to \textbf{57\%} faster inference than the StreamPETR baseline and \textbf{20\%} higher efficiency than the state-of-the-art ToC3D-faster, while preserving comparable detection accuracy. Code is available at this https URL.

---


### 81. [MARS$^2$: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation](https://arxiv.org/abs/2604.14564)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Shijie Wang, Fangyuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) paradigms have demonstrated strong performance on reasoning-intensive tasks such as code generation. However, limited trajectory diversity often leads to diminishing returns, which constrains the achievable performance ceiling. Search-enhanced RL alleviates this issue by introducing structured exploration, which remains constrained by the single-agent policy priors. Meanwhile, leveraging multiple interacting policies can acquire more diverse exploratory signals, but existing approaches are typically decoupled from structured search. We propose \textbf{MARS$^2$} (Multi-Agent Reinforced Tree-Search Scaling), a unified RL framework in which multiple independently-optimized agents collaborate within a shared tree-structured search environment. MARS$^2$ models the search tree as a learnable multi-agent interaction environment, enabling heterogeneous agents to collaboratively generate and refine candidate solutions within a shared search topology. To support effective learning, we introduce a path-level group advantage formulation based on tree-consistent reward shaping, which facilitates effective credit assignment across complex search trajectories. Experiments on code generation benchmarks show that MARS$^2$ consistently improves performance across diverse model combinations and training settings, demonstrating the effectiveness of coupling multi-agent collaboration with tree search for enhancing reinforcement learning. Our code is publicly available at this https URL.

---


### 82. [Physics-Informed Machine Learning for Pouch Cell Temperature Estimation](https://arxiv.org/abs/2604.14566)

**<font color=#1a73e8>作者：</font>** Zheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate temperature estimation of pouch cells with indirect liquid cooling is essential for optimizing battery thermal management systems for transportation electrification. However, it is challenging due to the computational expense of finite element simulations and the limitations of data-driven models. This paper presents a physics-informed machine learning (PIML) framework for the efficient and reliable estimation of steady-state temperature profiles. The PIML approach integrates the governing heat transfer equations directly into the neural network's loss function, enabling high-fidelity predictions with significantly faster convergence than purely data-driven methods. The framework is evaluated on a dataset of varying cooling channel geometries. Results demonstrate that the PIML model converges more rapidly and achieves markedly higher accuracy, with a 49.1% reduction in mean squared error over the data-driven model. Validation against independent test cases further confirms its superior performance, particularly in regions away from the cooling channels. These findings underscore the potential of PIML for surrogate modeling and design optimization in battery systems.

---


### 83. [Learning Adaptive Reasoning Paths for Efficient Visual Reasoning](https://arxiv.org/abs/2604.14568)

**<font color=#1a73e8>作者：</font>** Yixu Huang, Tinghui Zhu, Muhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning models (VRMs) have recently shown strong cross-modal reasoning capabilities by integrating visual perception with language reasoning. However, they often suffer from overthinking, producing unnecessarily long reasoning chains for any tasks. We attribute this issue to \textbf{Reasoning Path Redundancy} in visual reasoning: many visual questions do not require the full reasoning process. To address this, we propose \textbf{AVR}, an adaptive visual reasoning framework that decomposes visual reasoning into three cognitive functions: visual perception, logical reasoning, and answer application. It further enables models to dynamically choose among three response formats: Full Format, Perception-Only Format, and Direct Answer. AVR is trained with FS-GRPO, an adaptation of Group Relative Policy Optimization that encourages the model to select the most efficient reasoning format while preserving correctness. Experiments on multiple vision-language benchmarks show that AVR reduces token usage by 50--90\% while maintaining overall accuracy, especially in perception-intensive tasks. These results demonstrate that adaptive visual reasoning can effectively mitigate overthinking in VRMs. Code and data are available at: this https URL.

---


### 84. [Deepfake Detection Generalization with Diffusion Noise](https://arxiv.org/abs/2604.14570)

**<font color=#1a73e8>作者：</font>** Hongyuan Qi, Wenjin Hou, Hehe Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors face growing challenges in generalization as new image synthesis techniques emerge. In particular, deepfakes generated by diffusion models are highly photorealistic and often evade detectors trained on GAN-based forgeries. This paper addresses the generalization problem in deepfake detection by leveraging diffusion noise characteristics. We propose an Attention-guided Noise Learning (ANL) framework that integrates a pre-trained diffusion model into the deepfake detection pipeline to guide the learning of more robust features. Specifically, our method uses the diffusion model's denoising process to expose subtle artifacts: the detector is trained to predict the noise contained in an input image at a given diffusion step, forcing it to capture discrepancies between real and synthetic images, while an attention-guided mechanism derived from the predicted noise is introduced to encourage the model to focus on globally distributed discrepancies rather than local patterns. By harnessing the frozen diffusion model's learned distribution of natural images, the ANL method acts as a form of regularization, improving the detector's generalization to unseen forgery types. Extensive experiments demonstrate that ANL significantly outperforms existing methods on multiple benchmarks, achieving state-of-the-art accuracy in detecting diffusion-generated deepfakes. Notably, the proposed framework boosts generalization performance (e.g., improving ACC/AP by a substantial margin on unseen models) without introducing additional overhead during inference. Our results highlight that diffusion noise provides a powerful signal for generalizable deepfake detection.

---


### 85. [M3D-Net: Multi-Modal 3D Facial Feature Reconstruction Network for Deepfake Detection](https://arxiv.org/abs/2604.14574)

**<font color=#1a73e8>作者：</font>** Haotian Wu, Yue Cheng, Shan Bian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of deep learning in image generation, facial forgery techniques have achieved unprecedented realism, posing serious threats to cybersecurity and information authenticity. Most existing deepfake detection approaches rely on the reconstruction of isolated facial attributes without fully exploiting the complementary nature of multi-modal feature representations. To address these challenges, this paper proposes a novel Multi-Modal 3D Facial Feature Reconstruction Network (M3D-Net) for deepfake detection. Our method leverages an end-to-end dual-stream architecture that reconstructs fine-grained facial geometry and reflectance properties from single-view RGB images via a self-supervised 3D facial reconstruction module. The network further enhances detection performance through a 3D Feature Pre-fusion Module (PFM), which adaptively adjusts multi-scale features, and a Multi-modal Fusion Module (MFM) that effectively integrates RGB and 3D-reconstructed features using attention mechanisms. Extensive experiments on multiple public datasets demonstrate that our approach achieves state-of-the-art performance in terms of detection accuracy and robustness, significantly outperforming existing methods while exhibiting strong generalization across diverse scenarios.

---


### 86. [TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580)

**<font color=#1a73e8>作者：</font>** Xiangyu Liu, Feng Gao, Xiaomei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing audio-driven video digital human generation models rely on multi-step denoising, resulting in substantial computational overhead that severely limits their deployment in real-world settings. While one-step distillation approaches can significantly accelerate inference, they often suffer from training instability. To address this challenge, we propose TurboTalk, a two-stage progressive distillation framework that effectively compresses a multi-step audio-driven video diffusion model into a single-step generator. We first adopt Distribution Matching Distillation to obtain a strong and stable 4-step student, and then progressively reduce the denoising steps from 4 to 1 through adversarial distillation. To ensure stable training under extreme step reduction, we introduce a progressive timestep sampling strategy and a self-compare adversarial objective that provides an intermediate adversarial reference that stabilizes progressive distillation. Our method achieve single-step generation of video talking avatar, boosting inference speed by 120 times while maintaining high generation quality.

---


### 87. [Prompt Optimization Is a Coin Flip: Diagnosing When It Helps in Compound AI Systems](https://arxiv.org/abs/2604.14585)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Guanghui Wang, Yanwei Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimization in compound AI systems is statistically indistinguishable from a coin flip: across 72 optimization runs on Claude Haiku (6 methods $\times$ 4 tasks $\times$ 3 repeats), 49% score below zero-shot; on Amazon Nova Lite, the failure rate is even higher. Yet on one task, all six methods improve over zero-shot by up to $+6.8$ points. What distinguishes success from failure? We investigate with 18,000 grid evaluations and 144 optimization runs, testing two assumptions behind end-to-end optimization tools like TextGrad and DSPy: (A) individual prompts are worth optimizing, and (B) agent prompts interact, requiring joint optimization. Interaction effects are never significant ($p > 0.52$, all $F < 1.0$), and optimization helps only when the task has exploitable output structure -- a format the model can produce but does not default to. We provide a two-stage diagnostic: an \$80 ANOVA pre-test for agent coupling, and a 10-minute headroom test that predicts whether optimization is worthwhile -- turning a coin flip into an informed decision.

---


### 88. [CLion: Efficient Cautious Lion Optimizer with Enhanced Generalization](https://arxiv.org/abs/2604.14587)

**<font color=#1a73e8>作者：</font>** Feihu Huang, Guanyi Zhang, Songcan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lion optimizer is a popular learning-based optimization algorithm in machine learning, which shows impressive performance in training many deep learning models. Although convergence property of the Lion optimizer has been studied, its generalization analysis is still missing. To fill this gap, we study generalization property of the Lion via algorithmic stability based on the mathematical induction. Specifically, we prove that the Lion has a generalization error of $O(\frac{1}{N\tau^T})$, where $N$ is training sample size, and $\tau>0$ denotes the smallest absolute value of non-zero element in gradient estimator, and $T$ is the total iteration number. In addition, we obtain an interesting byproduct that the SignSGD algorithm has the same generalization error as the Lion. To enhance generalization of the Lion, we design a novel efficient Cautious Lion (i.e., CLion) optimizer by cautiously using sign function. Moreover, we prove that our CLion has a lower generalization error of $O(\frac{1}{N})$ than $O(\frac{1}{N\tau^T})$ of the Lion, since the parameter $\tau$ generally is very small. Meanwhile, we study convergence property of our CLion optimizer, and prove that our CLion has a fast convergence rate of $O(\frac{\sqrt{d}}{T^{1/4}})$ under $\ell_1$-norm of gradient for nonconvex stochastic optimization, where $d$ denotes the model dimension.
Extensive numerical experiments demonstrate effectiveness of our CLion optimizer.

---


### 89. [Prompt-Guided Image Editing with Masked Logit Nudging in Visual Autoregressive Models](https://arxiv.org/abs/2604.14591)

**<font color=#1a73e8>作者：</font>** Amir El-Ghoussani, Marc Hölle, Gustavo Carneiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of prompt-guided image editing in visual autoregressive models. Given a source image and a target text prompt, we aim to modify the source image according to the target prompt, while preserving all regions which are unrelated to the requested edit. To this end, we present Masked Logit Nudging, which uses the source image token maps to introduce a guidance step that aligns the model's predictions under the target prompt with these source token maps. Specifically, we convert the fixed source encodings into logits using the VAR encoding, nudging the model's predicted logits towards the targets along a semantic trajectory defined by the source-target prompts. Edits are applied only within spatial masks obtained through a dedicated masking scheme that leverages cross-attention differences between the source and edited prompts. Then, we introduce a refinement to correct quantization errors and improve reconstruction quality. Our approach achieves the best image editing performance on the PIE benchmark at 512px and 1024px resolutions. Beyond editing, our method delivers faithful reconstructions and outperforms previous methods on COCO at 512px and OpenImages at 1024px. Overall, our method outperforms VAR-related approaches and achieves comparable or even better performance than diffusion models, while being much faster. Code is available at 'this https URL.

---


### 90. [NLP needs Diversity outside of 'Diversity'](https://arxiv.org/abs/2604.14595)

**<font color=#1a73e8>作者：</font>** Joshua Tint  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This position paper argues that recent progress with diversity in NLP is disproportionately concentrated on a small number of areas surrounding fairness. We further argue that this is the result of a number of incentives, biases, and barriers which come together to disenfranchise marginalized researchers in non-fairness fields, or to move them into fairness-related fields. We substantiate our claims with an investigation into the demographics of NLP researchers by subfield, using our research to support a number of recommendations for ensuring that all areas within NLP can become more inclusive and equitable. In particular, we highlight the importance of breaking down feedback loops that reinforce disparities, and the need to address geographical and linguistic barriers that hinder participation in NLP research.

---


### 91. [Towards Design Compositing](https://arxiv.org/abs/2604.14605)

**<font color=#1a73e8>作者：</font>** Abhinav Mahajan, Abhikhya Tripathy, Sudeeksha Reddy Pala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphic design creation involves harmoniously assembling multimodal components such as images, text, logos, and other visual assets collected from diverse sources, into a visually-appealing and cohesive design. Recent methods have largely focused on layout prediction or complementary element generation, while retaining input elements exactly, implicitly assuming that provided components are already stylistically harmonious. In practice, inputs often come from disparate sources and exhibit visual mismatch, making this assumption limiting. We argue that identity-preserving stylization and compositing of input elements is a critical missing ingredient for truly harmonized components-to-design pipelines. To this end, we propose GIST, a training-free, identity-preserving image compositor that sits between layout prediction and typography generation, and can be plugged into any existing components-to-design or design-refining pipeline without modification. We demonstrate this by integrating GIST with two substantially different existing methods, LaDeCo and Design-o-meter. GIST shows significant improvements in visual harmony and aesthetic quality across both pipelines, as validated by LLaVA-OV and GPT-4V on aspect-wise ratings and pairwise preference over naive pasting. Project Page: this http URL.

---


### 92. [GDPR Auto-Formalization with AI Agents and Human Verification](https://arxiv.org/abs/2604.14607)

**<font color=#1a73e8>作者：</font>** Ha Thanh Nguyen, Wachara Fungwacharakorn, Sabine Wehnert 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the overall process of automatic formalization of GDPR provisions using large language models, within a human-in-the-loop verification framework. Rather than aiming for full autonomy, we adopt a role-specialized workflow in which LLM-based AI components, operating in a multi-agent setting with iterative feedback, generate legal scenarios, formal rules, and atomic facts. This is coupled with independent verification modules which include human reviewers' assessment of representational, logical, and legal correctness. Using this approach, we construct a high-quality dataset to be used for GDPR auto-formalization, and analyze both successful and problematic cases. Our results show that structured verification and targeted human oversight are essential for reliable legal formalization, especially in the presence of legal nuance and context-sensitive reasoning.

---


### 93. [ConfLayers: Adaptive Confidence-based Layer Skipping for Self-Speculative Decoding](https://arxiv.org/abs/2604.14612)

**<font color=#1a73e8>作者：</font>** Walaa Amer, Uday das, Fadi Kurdahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-speculative decoding is an inference technique for large language models designed to speed up generation without sacrificing output quality. It combines fast, approximate decoding using a compact version of the model as a draft model with selective re-evaluation by the full target model. Some existing methods form the draft model by dynamically learning which layers to skip during inference, effectively creating a smaller subnetwork to speed up computation. However, using heuristic-based approaches to select layers to skip can often be simpler and more effective. In this paper, we propose ConfLayers, a dynamic plug-and-play approach to forming the draft model in self-speculative decoding via confidence-based intermediate layer skipping. The process iteratively computes confidence scores for all layers, selects layers to skip based on an adaptive threshold, evaluates the performance of the resulting set, and updates the best selection until no further improvement is achieved or a maximum number of iterations is reached. This framework avoids the overhead and complexity of training a layer skipping policy and can provide more consistent speed-quality trade-offs while preserving the adaptivity of the draft model to diverse tasks and datasets. The performance evaluation of ConfLayers across different models and datasets shows that our novel approach offers up to 1.4x speedup over vanilla LLM generation.

---


### 94. [CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors](https://arxiv.org/abs/2604.14615)

**<font color=#1a73e8>作者：</font>** Yubin Kim, Salman Rahman, Samuel Schmidgall 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery in digital health requires converting continuous physiological signals from wearable devices into clinically actionable biomarkers. We introduce CoDaS (AI Co-Data-Scientist), a multi-agent system that structures biomarker discovery as an iterative process combining hypothesis generation, statistical analysis, adversarial validation, and literature-grounded reasoning with human oversight using large-scale wearable datasets. Across three cohorts totaling 9,279 participant-observations, CoDaS identified 41 candidate digital biomarkers for mental health and 25 for metabolic outcomes, each subjected to an internal validation battery spanning replication, stability, robustness, and discriminative power. Across two independent depression cohorts, CoDaS surfaced circadian instability-related features in both datasets, reflected in sleep duration variability (DWB, \rho = 0.252, p < 0.001) and sleep onset variability (GLOBEM, \rho = 0.126, p < 0.001). In a metabolic cohort, CoDaS derived a cardiovascular fitness index (steps/resting heart rate; \rho = -0.374, p < 0.001), and recovered established clinical associations, including the hepatic function ratio (AST/ALT; \rho = -0.375, p < 0.001), a known correlate of insulin resistance. Incorporating CoDaS-derived features alongside demographic variables led to modest but consistent improvements in predictive performance, with cross-validated \Delta R^2 increases of 0.040 for depression and 0.021 for insulin resistance. These findings suggest that CoDaS enables systematic and traceable hypothesis generation and prioritization for biomarker discovery from large-scale wearable data.

---


### 95. [Multigrain-aware Semantic Prototype Scanning and Tri-Token Prompt Learning Embraced High-Order RWKV for Pan-Sharpening](https://arxiv.org/abs/2604.14622)

**<font color=#1a73e8>作者：</font>** Junfeng Li, Wenyang Zhou, Xueheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a Multigrain-aware Semantic Prototype Scanning paradigm for pan-sharpening, built upon a high-order RWKV architecture and a tri-token prompting mechanism derived from semantic clustering. Specifically, our method contains three key components: 1) Multigrain-aware Semantic Prototype Scanning. Although RWKV offers a efficient linear-complexity alternative to Transformers, its conventional bidirectional raster scanning is still semantic-agnostic and prone to positional bias. To address this issue, we introduce a semantic-driven scanning strategy that leverages locality-sensitive hashing to group semantically related regions and construct multi-grain semantic prototypes, enabling context-aware token reordering and more coherent global interaction. 2) Tri-token Prompt Learning. We design a tri-token prompting mechanism consisting of a global token, cluster-derived prototype tokens, and a learnable register token. The global and prototype tokens provide complementary semantic priors for RWKV modeling, while the register token helps suppress noisy and artifact-prone intermediate representations. 3) Invertible Q-Shift. To counteract spatial details, we apply center difference convolution on the value pathway to inject high-frequency information, and introduce an invertible multi-scale Q-shift operation for efficient and lossless feature transformation without parameter-heavy receptive field expansion. Experimental results demonstrate the superiority of our method.

---


### 96. [A Parallel Approach to Counting Exact Covers Based on Decomposability Property](https://arxiv.org/abs/2604.14627)

**<font color=#1a73e8>作者：</font>** Liangda Fang, Yaohui Luo, Delong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The exact cover problem is a classical NP-hard problem with broad applications in the area of AI. Algorithm DXZ is a method to count exact covers representing by zero-suppressed binary decision diagrams (ZBDDs). In this paper, we propose a zero-suppressed variant of decision decomposable negation normal form (in short, decision-ZDNNF), which is strictly more succinct than ZBDDs. We then design a novel parallel algorithm, namely DXD, which constructs a decision-ZDNNF representing the set of all exact covers. Furthermore, we improve DXD by dynamically updating connected components. The experimental results demonstrate that the improved DXD algorithm outperforms all of state-of-the-art methods.

---


### 97. [CMTM: Cross-Modal Token Modulation for Unsupervised Video Object Segmentation](https://arxiv.org/abs/2604.14630)

**<font color=#1a73e8>作者：</font>** Inseok Jeon, Suhwan Cho, Minhyeok Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in unsupervised video object segmentation have highlighted the potential of two-stream architectures that integrate appearance and motion cues. However, fully leveraging these complementary sources of information requires effectively modeling their interdependencies. In this paper, we introduce cross-modality token modulation, a novel approach designed to strengthen the interaction between appearance and motion cues. Our method establishes dense connections between tokens from each modality, enabling efficient intra-modal and inter-modal information propagation through relation transformer blocks. To improve learning efficiency, we incorporate a token masking strategy that addresses the limitations of relying solely on increased model complexity. Our approach achieves state-of-the-art performance across all public benchmarks, outperforming existing methods.

---


### 98. [High-Speed Full-Color HDR Imaging via Unwrapping Modulo-Encoded Spike Streams](https://arxiv.org/abs/2604.14632)

**<font color=#1a73e8>作者：</font>** Chu Zhou, Siqi Yang, Kailong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional RGB-based high dynamic range (HDR) imaging faces a fundamental trade-off between motion artifacts in multi-exposure captures and irreversible information loss in single-shot techniques. Modulo sensors offer a promising alternative by encoding theoretically unbounded dynamic range into wrapped measurements. However, existing modulo solutions remain bottlenecked by iterative unwrapping overhead and hardware constraints limiting them to low-speed, grayscale capture. In this work, we present a complete modulo-based HDR imaging system that enables high-speed, full-color HDR acquisition by synergistically advancing both the sensing formulation and the unwrapping algorithm. At the core of our approach is an exposure-decoupled formulation of modulo imaging that allows multiple measurements to be interleaved in time, preserving a clean, observation-wise measurement model. Building upon this, we introduce an iteration-free unwrapping algorithm that integrates diffusion-based generative priors with the physical least absolute remainder property of modulo images, supporting highly efficient, physics-consistent HDR reconstruction. Finally, to validate the practical viability of our system, we demonstrate a proof-of-concept hardware implementation based on modulo-encoded spike streams. This setup preserves the native high temporal resolution of spike cameras, achieving 1000 FPS full-color imaging while reducing output data bandwidth from approximately 20 Gbps to 6 Gbps. Extensive evaluations indicate that our coordinated approach successfully overcomes key systemic bottlenecks, demonstrating the feasibility of deploying modulo imaging in dynamic scenarios.

---


### 99. [Pushing the Boundaries of Multiple Choice Evaluation to One Hundred Options](https://arxiv.org/abs/2604.14634)

**<font color=#1a73e8>作者：</font>** Nahyun Lee, Guijin Son  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple choice evaluation is widely used for benchmarking large language models, yet near ceiling accuracy in low option settings can be sustained by shortcut strategies that obscure true competence. Therefore, we propose a massive option evaluation protocol that scales the candidate set to one hundred options and sharply reduces the impact of chance performance. We apply this framework to a Korean orthography error detection task where models must pick the single incorrect sentence from a large candidate set. With fixed targets and repeated resampling and shuffling, we obtain stable estimates while separating content driven failures from positional artifacts. Across experiments, results indicate that strong performance in low option settings can overstate model competence. This apparent advantage often weakens under dense interference at high $N$, revealing gaps that conventional benchmarks tend to obscure. We identify two failure modes, semantic confusion and position bias toward early options under uncertainty. To isolate the effect of context length, we run padding controlled and length matched tests, which suggest that the main bottleneck is candidate ranking rather than context length. Together, these findings support massive option evaluation as a general framework for stress testing model reliability under extreme distractor density, beyond what low option benchmarks can reveal.

---


### 100. [Touching Space: Accessible Map Exploration Through Conversational Audio-Haptic Interaction](https://arxiv.org/abs/2604.14637)

**<font color=#1a73e8>作者：</font>** Li Liu, Jiaming Qu, Marc Jowell Bagaoisan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most existing assistive navigation tools focus on providing real-time guidance for Blind and Low-Vision (BLV) people, but few support building a holistic spatial understanding of unfamiliar environments before travel. Such cognitive map construction (e.g., knowing that a fountain is south of a tower and west of a hotel) is important for pre-travel planning, yet remains underexplored in prior work. To address this gap, we present Touching Space, an end-to-end system that retrieves map data for a target place and loads it into a frontend interface for exploration. The system combines haptic and audio feedback: users explore spatial layouts through touch and ask spoken questions to a conversational agent during exploration. Touching Space contributes a conversational interface that supports BLV users in building cognitive maps on commodity hardware.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
