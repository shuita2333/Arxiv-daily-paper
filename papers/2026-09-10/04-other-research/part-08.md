# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 351. [When Intelligence Becomes Agency: A Theory of Governed, Proactive Agency for Symbiotic AI Systems](https://arxiv.org/abs/2609.07741)

**<font color=#1a73e8>作者：</font>** João Dias Ferreira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent AI assistants are intended to extend human attention, memory, and coordination across changing digital and physical environments. To be truly useful they must do more than just act when asked. They must decide on their own whether a situation warrants behavior at all, when it does and in what mode, whether to act, ask, monitor, defer or deliberately refrain. We call this the activation problem. Research on commitment, appraisal, mixed-initiative interaction and delegation each illuminates part of it, but none ties situated activation to continuing authorization and accountability. This paper develops a conceptual and formal framework for governed proactive agency, organizing behavior across time through perception, intent, affective-conative appraisal, constraint, and feedback. It distinguishes autonomous and delegated agency and defines symbiotic agency as delegation under a standing, revocable mandate, with continuing coupling to the principal's situation, calibrated inference of their condition, and bounded personalization. The distinctive contribution is an integrated account linking activation decisions to authorized perception, behavior selection, authority containment, traceable restraint, and constrained adaptation, with behavioral episodes as the unit of analysis. Through an agency classification method, an evaluation framework, proposed benchmark scenarios, and a reference architecture, the account provides a basis for specifying and assessing whether assistance is warranted, timely, authorized, and answerable beyond task completion alone. It is intended to guide the development and evaluation of always-present personal assistants and embodied support systems that augment human capabilities while preserving the principal's authority and judgment.

---


### 352. [Replicating a Disjoint-Set Union Experiment over Various Notions of Micro Units to assess Translation Effort](https://arxiv.org/abs/2609.07748)

**<font color=#1a73e8>作者：</font>** Michael Carl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The paper describes a replication experiment to assess "the distribution of editing procedures across micro and macro units as an indicator of the strain of text production". We investigate various pause thresholds to isolate Micro and Macro units and conclude that process-based units might be more suitable entity.

---


### 353. [Local gradient neural operator](https://arxiv.org/abs/2609.07752)

**<font color=#1a73e8>作者：</font>** Baiming Zhang, Jinsong Tang, Ying Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Field temporal prediction and source identification constitute canonical problems in dynamical systems. Conventional approaches to these problems depend on a thorough understanding of the governing partial differential equations (PDEs). Recently, deep learning, as represented by neural operators, has provided a data-driven paradigm for addressing such tasks. However, most existing global neural operators for PDEs require large training datasets and many learnable parameters, with limited interpretability and generalization. We propose the local gradient neural operator (LGNO) as a lightweight and interpretable alternative for field temporal evolution prediction and source identification in typical mechanical problems. The method builds on priors from nonlinear gradient discretization and uses multilayer perceptron convolutional layers to learn translation-invariant local kernels that resemble discrete stencils. A zero consistent stencil factorization separates coefficient learning from field reconstruction, rendering the learned operators more transparent. For problems with symmetries, network folding shares equivalent components and reduces parameter counts. We evaluate the method on PDE benchmarks covering linear and nonlinear, static and dynamic, and low and high dimensional cases. Results show that LGNO maintains accuracy, parameter efficiency, and rollout stability across these tasks, and further exhibits wide applicability to mechanical problems including diffusion, flow, and quantum phenomena.

---


### 354. [Do AI Coding Assistants Check Before They Install? A Pre-Registered Demand-Side Audit of Trust Signals in the Research Software Supply Chain](https://arxiv.org/abs/2609.07754)

**<font color=#1a73e8>作者：</font>** Pengyin Shan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding assistants now select, install, and configure software, and attackers have exploited that position through invented package names, compromised maintainer accounts, and manipulated repository text. In response, the supply-chain community publishes machine-checkable trust signals: software bills of materials, signed releases, build provenance attestations, and declared official channels. Whether coding assistants read or act on those signals has not been measured for any of these classes on research software. We pre-registered and ran a controlled study on six open-source research software projects (three HPC, three quantum computing) drawn from an 87-project corpus, with protocol, seed, panel, and analysis plan deposited with a DOI before any trial. W created nine modified copies for each project: no signal, one per signal class, two with a signature or attestation from the wrong issuer, one with all four signals, and one reproducing documented conflicts in the project's own metadata. Three models under two ways of operating an assistant, with and without an approval step, gave 1,920 registered trials, plus a supplement on three frontier models. We scored behavior from container logs rather than from what the assistant said, and recorded the cost of every trial. Verification was rare under every condition: in 9 of 1,920 registered trials (0.5%), the assistant opened any provenance signal before installing in 0 of 384 control trials, and no trial ran a verification command, so signal presence had no measurable effect. We drew three conclusions: publishing signals is necessary but not sufficient; price did not buy verification (the model that verified most often costs $0.10 per trial; the most capable, at $1.00, verified nothing); verification must be built into the program that runs the assistant. We release the per-trial cost ledger, the protocol, and every log.

---


### 355. [A Theoretical Analysis of Generalization Dynamics in Neural Networks under Gradient Descent with Weight Decay](https://arxiv.org/abs/2609.07755)

**<font color=#1a73e8>作者：</font>** Yuqing Wang, Ioannis G. Kevrekidis, Mikhail Belkin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding generalization remains a central challenge in machine learning because it requires jointly considering data, architecture, and training dynamics. In this paper, we develop a theoretical framework that characterizes how these factors jointly shape generalization performance throughout training. More precisely, we study a broad class of neural networks trained under the $\ell^2$ loss by gradient descent (GD) with weight decay, and prove the convergence of GD to a neighbourhood of the global minimizers of the empirical loss. By partitioning the space based on the input data, we then decompose the population error into data error, optimization error, and prediction variation error, and bound them separately. In particular, for the prediction variation error, which measures the oscillations of the learned function, we propose (local) approximate homogeneity and derive explicit cellwise and layerwise bounds for its evolution along the training trajectory. These bounds yield two important implications: a necessary condition of improved generalization explains differences in layerwise generalization behavior; a sufficient condition describes delayed generalization and provides a theoretical characterization of grokking.

---


### 356. [Bag of Tricks or Bag of Myths? Reducing Modeling Complexity with Task Knowledge in Explainable Suicide Risk Assessment](https://arxiv.org/abs/2609.07766)

**<font color=#1a73e8>作者：</font>** Shlok Shelat, Shrey Salvi, Souvik Roy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assessing suicide risk from social media text is a small-data, high-stakes setting requiring not only severity prediction but also supporting evidence and clinically relevant risk and protective factors. Yet common NLP techniques, including model scaling, synthetic data, loss reweighting, ensembling, and threshold tuning, are often applied without testing whether their gains hold up under severe class imbalance, coupled outputs, and limited author-level data. We study 1,635 clinician-annotated posts and audit 31 pre-specified techniques from 7 methodological families through roughly 300 controlled experiments on author-disjoint partitions. We found no prior audit of this playbook in this regime. The findings guide a task-grounded system for three outputs: 4-level suicide risk, evidence spans, and 24 clinical risk and protective factors. Only 5 of 31 comparisons produced reliable gains. We reformulate factor prediction as entailment between each post and its codebook definitions, using an architecturally diverse ensemble with class-balanced training and score rescaling. Risk predictions condition a 7-model evidence tagger ensemble; evidence restricts symbolic risk rules; and a difficult risk class is routed separately. The factor predictor remains independent because risk evidence provides no additional factor signal. We also correct a mismatch between validation scores used for threshold fitting and test-time ensemble scores through deployment-consistent calibration, yielding the largest improvement to the factor system. The final system achieves 0.8203 for risk, 0.7953 for evidence, and 0.7045 macro-F1 for factors, with a 0.7781 composite, ranking third among 53 teams. We call the underlying principle task-conditioned technique selection: retain techniques only when task-specific knowledge, structure, or empirical evidence justifies them.

---


### 357. [Grid Trouble in Paradise: Uncovering Vulnerable Distributed Energy Resources and Their Grid-Level Risks](https://arxiv.org/abs/2609.07783)

**<font color=#1a73e8>作者：</font>** Anna Raymaker, Samuel Talkington, Zeezoo Ryu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Grid-connected solar distributed energy resources (DERs), such as solar inverters and monitoring platforms, have been deployed at unprecedented scale over the past few years, with global solar capacity more than doubling since 2022. To support monitoring and control, many of these systems are Internet-connected and configured by installers or end users, yet the real-world scale of their Internet exposure and the implications for power grid operation remain poorly understood.
In this paper, we present an Internet-scale evaluation of exposed and vulnerable solar DER infrastructure, and assess the risk that compromised DERs can pose to energy grids. We develop a method for accurately identifying solar DERs from Internet scanning data, and discover a diverse population of over 66,000 Internet-exposed solar DERs. We detect that at least 10,000 of these DERs may have known CVEs, such as unauthenticated monitoring and control endpoints. To assess the risk that these vulnerable DERs pose to a power grid, we use an electric grid network for Oahu, Hawaii, established and used by the power system research community, and conduct a power system analysis. Our evaluation shows that by compromising exposed DERs, attackers can cause voltage and line flow violations across multiple locations in the Oahu network, resulting in a range of consequences from degraded power quality to damaged power system components to power outages. Ultimately, our work brings to light the emerging threat of grid-connected DERs, and provides directions for improving energy security.

---


### 358. [Quantifying the Engagement Trap: Impact of Short-form Video Recommender Systems on Users with ADHD](https://arxiv.org/abs/2609.07795)

**<font color=#1a73e8>作者：</font>** Vedad Misirlic, Gregor Mayr, Elisabeth Lex  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Short-form video platforms use recommender systems to maximize engagement through highly efficient personalized recommendations. However, the impact of these recommendations on users with ADHD compared to users without ADHD remains underexplored. Through this study, we introduce and operationalize the Engagement Trap, illustrating how recommender systems, while successfully optimizing for engagement, disproportionately disadvantage users with ADHD. This stratified study of 302 participants, recruited via the online platform Prolific, compares experiences between participants with and without ADHD. Our results show that while recommendations are perceived as relevant across groups, participants with ADHD report significantly higher levels of time blindness, post-usage regret, and emotional distress when consuming recommendations. Moreover, we collect feedback for several proof-of- concept, theoretical design interventions for neuro-inclusive design principles. These findings provide quantitative evidence of systemic differences in engagement-optimized recommender systems and highlight the unbalanced negative effects and interactions these systems create for participants with ADHD. We argue for neurodiversity-aware, human-centered design approaches that mitigate such algorithmic harms and support more equitable experiences.

---


### 359. [Does Syntax Matter? A Graph-Augmented Variational Topic Model for Computational Social Sciences](https://arxiv.org/abs/2609.07797)

**<font color=#1a73e8>作者：</font>** Alessandro Meneghini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic modeling is widely used in computational social sciences to identify latent themes in large text corpora. Traditional approaches rely on Bag-of-Words representations and generative models such as LDA, while recent methods like BERTopic operate on dense document embeddings. This paper introduces the Structural Contextual Probabilistic Topic Model (SCPTM), an architecture that incorporates syntactic dependency relations into topic inference. SCPTM represents a corpus as a heterogeneous graph of documents and words connected by lexical and syntactic edges, processed through a Graph Attention Network within a Variational Autoencoder to produce probabilistic, mixed-membership topic distributions. We evaluate seven topic modeling techniques (including four SCPTM ablations) across four corpora differing in register and discourse structure. Our framework combines coherence (C_V, C_NPMI), topic diversity, clustering-label alignment (NMI), and phrase-level diagnostics (complementarity and valence gap). Results show that SCPTM's neural architecture yields substantial gains in document-topic alignment over generative baselines, but these gains are attributable to the variational encoder rather than to syntax. Syntax contributes to topic diversity, where graph-augmented variants outperform the no-graph baseline across all corpora, and to descriptor quality: dependency paths capture predicate-argument structures and stance in deliberative registers, while proving redundant in technical and institutional corpora. The valence gap is positive across all variants, but driven primarily by phrase grouping rather than syntactic filtering. We conclude that syntactic encoding matters conditionally: it benefits action-oriented, argumentative texts, but introduces noise in informational or administrative registers.

---


### 360. [Climate-ModernBERT: Revisiting Corpus Composition for Domain-Adaptive Continued Pretraining](https://arxiv.org/abs/2609.07798)

**<font color=#1a73e8>作者：</font>** Yongan Yu, Shantam Raj, Jingwei Ni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing (NLP) in the climate domain requires models to process heterogeneous text sources, including scientific literature, policy disclosures, and synthetic reports. However, how to effectively combine diverse domain corpora during continued pretraining (CPT) remains underexplored. We introduce Climate-ModernBERT, a family of climate-adapted encoder models obtained through continued pretraining of ModernBERT-Base on three climate corpora: academic climate text, climate-filtered web data, and synthetic climate documents. We systematically compare joint continued pretraining on corpus mixtures with parameter-space merging of independently specialized checkpoints. Across nine climate NLP benchmarks, our best model achieves 76.3 average F_1, improving significantly over a vanilla ModernBERT baseline by 2.8 points. Within the climate NLP setting, the results show that academic climate corpora provide the strongest adaptation signal among the evaluated sources, while parameter-space merging improves over joint multi-source training and better preserves complementary information from heterogeneous climate corpora. We release all Climate-ModernBERT variants and training checkpoints to support future research in climate NLP and domain-adaptive pretraining.

---


### 361. [Understanding the Impact of Model Pruning on Long-Tail Forgetting and Explanation Reliability in Medical Imaging](https://arxiv.org/abs/2609.07803)

**<font color=#1a73e8>作者：</font>** Nazish Khalid, Tausifa Jan Saleem, Amal Saqib 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model pruning is widely used to compress deep neural networks, reducing memory and computational requirements with minimal impact on aggregate performance. However, its effect on model behavior remains poorly understood, particularly for long-tailed medical datasets where rare but clinically important conditions are underrepresented. Furthermore, it remains unclear whether pruned models preserve reliable explanations of their predictions. To address this gap, we present a systematic study of long-tail forgetting and explanation reliability under model pruning. Across two long-tailed medical imaging datasets, two CNN architectures, four pruning methods, and sparsity levels up to 95\%, we evaluate predictive performance, explanation stability, and explanation faithfulness. Our results show that predictive performance exhibits a strong frequency-dependent trend, with lower-frequency classes generally experiencing earlier and larger degradation than higher-frequency classes. In contrast, explanation stability and faithfulness are influenced primarily by the pruning strategy, with gradient-informed methods preserving explanation reliability more effectively under aggressive compression. Qualitative and mechanistic analyses further indicate that explanation degradation is primarily associated with the collapse of class-discriminative gradients rather than the disappearance of feature activations. These findings suggest that model compression should be evaluated beyond aggregate performance. Incorporating class-aware and explanation-aware evaluation reveals failure modes that would otherwise remain hidden, while moderate sparsity levels provide a practical balance between compression, predictive performance, and explanation reliability.

---


### 362. [Nothing Breaks: No Single Peer Can Soundly Gate Post-Quantum Delivery](https://arxiv.org/abs/2609.07849)

**<font color=#1a73e8>作者：</font>** Yunze Han  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum protection is delivered to a peer, not declared in a file: whether a session is quantum-resistant is a relation between a server's configuration and the clients that reach it. We show that no single peer can soundly gate that relation. Shipped SSH clients are not ordered: two of their post-quantum capability classes are minimal and incomparable, so a check pinned to either misses the other family's withdrawal. A peer taking both fares no better: it falls back and misses both, or, where classical outranks one family, catches just that one. No case flags both. Nothing above the wire carries the relation either. An artifact-side instrument cannot encode it, because a peer population is not one of its inputs; and across seven configurations on two protocols we find that not one of the five scalars deployed auditors expose to automation moves, while unrelated degradation moves the ones that discriminate at all: the auditors do compute the delivered algorithm, and discard it at the interface automation reads. Nothing else catches the loss either, because nothing breaks: removing a hybrid key exchange starts the daemon, validates the configuration, passes the tests and serves the client, and the adversary it defends against does not exist yet, so no functional signal can carry the loss even in principle. We then show that agents make that state reachable at scale, driving a validated downgrade in 40 of 40 episodes from ordinary engineering prose, against 0 of 40 on a matched neutral document.

---


### 363. [EventSpec: Defining and Detecting Event-Semantic Issues in Blockchain Ecosystems](https://arxiv.org/abs/2609.07865)

**<font color=#1a73e8>作者：</font>** Yixuan Liu, Yuxin Dong, Ye Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, smart contracts have become the backbone of decentralized applications (DApps), and off-chain systems such as bridges, wallets, and indexers rely heavily on event logs to track contract execution and state changes. However, the Ethereum Virtual Machine (EVM) does not validate or enforce event semantics, so logs can diverge from on-chain state, misleading off-chain systems into accepting incorrect state transitions. Existing smart contract vulnerability detection tools focus on logic bugs, with limited support for detecting event-semantic defects. To address this gap, we collect audit reports and incident cases and apply open card sorting to define five classes of event-semantic defects: event collision, state-event mismatch, unauthorized event emission, event emission mismatch, and event parameter mismatch. We propose EventSpec, which infers event specifications from a contract corpus via behavior inference and semantic-constraint extraction and applies differential checking to identify event-semantic defects in target contracts. We run EventSpec on 6,617 real-world contracts and evaluate detection effectiveness based on manually labeled results; EventSpec achieves an overall comprehensive precision of 90.17%. We further provide an off-chain evaluation harness that reproduces two off-chain attack vectors on any EVM-compatible chain: event origin confusion caused by unintended emitters and event-state desynchronization where events lack matching state updates. Using this harness, we demonstrate the feasibility of these attacks on bridge relayers, blockchain explorers, and NFT marketplaces, and report six wallet issues, four of which were confirmed (including a $600 bounty), with two remaining pending.

---


### 364. [Explainable Temporal Attention-based Defect Detection For Fillet Joints in Real-Time Gas Metal Arc Welding Based on Multi-modal Data](https://arxiv.org/abs/2609.07893)

**<font color=#1a73e8>作者：</font>** Mobina Mobaraki, Mahyar Asadi, Klaske Van Heusden 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning is an efficient technique to monitor the real time welding process, reducing post-welding repairs and production delays. This paper leverages the monitoring capability by proposing a multi modal temporal attention based deep learning defect detection model for internal defects that are challenging to detect, including porosity, lack of penetration and fusion, undercut, and cold lap during Gas Metal Arc Welding in fillet joints. The model is trained on collected welding images and sound data from an industrial collaborative welding robot. The results show that the attention module can improve the F1 Score to 0.99. We use explainable Artificial Intelligence to interpret the proposed models behavior and dataset distribution, determining potential important areas in image and sound spectrograms and preferred modality to detect each defect. This improves trust and reliability in Artificial Intelligence driven welding inspection.

---


### 365. [The Accuracy Paradox: Empirical Diagnostic of Default Decision Thresholds in Multi-Label Enzyme Commission Prediction [With Code]](https://arxiv.org/abs/2609.07897)

**<font color=#1a73e8>作者：</font>** Bilal Ahmad, Rajed Mehmood  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated prediction of Enzyme Commission (EC) numbers plays a central role in functional annotation and computational drug discovery. However, standard multi-label machine learning pipelines frequently rely on default decision thresholds (t=0.50), assuming balanced prior distributions across target heads. In this study, we present a systematic empirical diagnostic of uncalibrated fixed decision boundaries operating under severe class imbalance across N = 14,096 annotated compounds categorized into six primary EC classes (EC1-EC6). Our results highlight a pronounced Accuracy Paradox: while the multi-label system achieves a deceivingly high mean accuracy of 77.16%, the macro F1-score (0.3976) and macro recall (0.3872) reveal severe predictive breakdown. Majority target classes suffer from hyper-sensitivity and over-prediction, whereas minority classes exhibit sharp recall decay, culminating in a total decision boundary collapse for EC6 (Recall = 0.00%) despite underlying discriminative power (ROC-AUC = 0.5857). Feature correlation analysis further reveals high linear redundancy among topological indices relative to fingerprint density metrics. Ultimately, this diagnostic study demonstrates that standard point predictions mask critical errors in bioinformatics workflows. We establish target-specific threshold optimization and post-hoc conformal calibration as essential, open-source post-processing safeguards for reliable applied machine learning and deep learning architectures.

---


### 366. [JEDI: JEPA-to-Edge Distillation for Efficient Cropland Segmentation from Satellite Imagery](https://arxiv.org/abs/2609.07915)

**<font color=#1a73e8>作者：</font>** Kishor Kumar Bhaumik, Nicolas Roque dos Santos, Jia Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision models provide useful representations for remote-sensing segmentation but are often too expensive for deployment at the satellite or field edge. Existing feature-level distillation methods also tend to assume similar teacher and student architectures and often stop feature alignment when task training begins. We introduce JEDI (JEPA-to-Edge Distillation), a two-stage framework that transfers representations from a large I-JEPA Vision Transformer teacher to a compact SegFormer student. First, JEDI aligns the student's terminal representation with the teacher's token space using cross-architecture projection and spatial alignment. It then jointly optimizes supervised segmentation, temperature-scaled response distillation, and persistent feature alignment throughout task adaptation. On CalCROP21, JEDI-B0 achieves 68.0 mean Intersection-over-Union (mIoU) with 4.04M parameters, improving over the standalone student by 16.0 points and coming within 2.0 points of the 70.0 mIoU achieved by the 639M-parameter teacher. We evaluate SegFormer B0, B1, and B2 students with 4.04M, 14.33M, and 28M parameters, respectively. Across all three variants, JEDI consistently outperforms response-, structure-, channel-, and relational-distillation baselines under the same teacher-student setting. These results show that persistent representation alignment is especially valuable under aggressive compression, substantially reducing model size and computation while preserving segmentation performance.

---


### 367. [Poisson Image Denoising Using Minimax Concave and Reweighted $\ell_1$ Penalties: Nonblind and Blind Approaches](https://arxiv.org/abs/2609.07916)

**<font color=#1a73e8>作者：</font>** Reza Parvaz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images are important tools in various sciences. Despite the development of photo-taking tools, creating clear and image without noise remains challenging in practice. In particular, Poisson noise has an effect on medical and astronomical images, and reduces their quality. Additionally, blur is another factor that has an effect on image quality. The problem of image restoration becomes very complicated when we have no information about the Point Spread Function (PSF). These types of problems are known as blind case. However, in some images, such as some astronomical images, the type of PSF can be specified, and these types of problems are known as nonblind problems. Total Variation (TV) is a widely used method for solving such inverse problems, where the selection of the penalty function is the most critical factor that affects the method's performance. In this paper, to improve edge preservation, we employ a reweighted $\ell_1$-regularization of the fractional order derivative. Furthermore, we propose a nonblind and blind image deblurring approach under Poisson noise using the Minimax Concave Penalty (MCP), which is a continuous, sparsity promoting, and nearly unbiased regularizer. This formulation leads to a nonconvex optimization model. To solve the proposed model, we introduce an efficient numerical algorithm based on the Alternating Direction Method of Multipliers (ADMM) and provide an analysis of its convergence. Finally, the effectiveness of the proposed algorithm are demonstrated through extensive experiments on various images.

---


### 368. [AVCG: A Generalized Variational Framework for Counterfactual Generation under Hypothesis Distributions](https://arxiv.org/abs/2609.07917)

**<font color=#1a73e8>作者：</font>** Jamie Duell, Alejandro Jimenez Rodriguez, Mahault Albarracin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations formalize "what-if" scenarios by identifying modifications to an input instance that obtain a desired alternative prediction. Traditionally, whether generated via instance-specific optimization or amortized single pass models, these approaches rely on a single, deterministic point-estimate predictor. However, this ignores predictive uncertainty and hypothesis variability, leading to brittle explanations that frequently become invalid if the underlying model is retrained or updated. To address this fragility, we propose the Amortized Variational Counterfactual Generator (AVCG), a generalized optimization framework that formulates counterfactual generation as optimization over an arbitrary distribution of plausible predictive hypotheses rather than a single deterministic predictor. This formulation naturally accommodates Bayesian posteriors, Rashomon-restricted hypothesis spaces, and other uncertainty representations within a unified optimization framework. Evaluation across multiple benchmark datasets demonstrates that the AVCG framework produces counterfactual explanations that remain highly valid under predictive uncertainty and model changes, while maintaining competitive plausibility and single-pass runtime performance.

---


### 369. [Prevalence calibration as shortcut mitigation](https://arxiv.org/abs/2609.07922)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Kina, Eike Petersen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shortcut learning denotes the widespread situation in which a classifier exploits spurious correlations rather than diagnostic features. Existing mitigation strategies mostly aim to learn shortcut-invariant representations; their empirical success is limited and they cannot be applied to classifiers using frozen foundation model encoders. We propose to reframe shortcut learning as fundamentally a calibration problem: unconstrained learning implicitly calibrates each shortcut group to its training set disease prevalence, rendering the resulting classifier necessarily over-confident in one group and under-confident in the other. Building on this insight, we prevalence-equalize calibration between shortcut groups through two encoder-agnostic methods, an in-processing regularizer and a post-hoc prevalence-equalized recalibration step. Across chest-drain-pneumothorax benchmarks on CheXpert and SIIM-ACR, spanning fine-tuned CNNs and frozen foundation-model backbones, both methods substantially outperform all baselines. Post-hoc recalibration of a standard ERM-trained DenseNet raises misaligned-group AUROC from 0.23 to 0.73, indicating that shortcut reliance degrades the classification head rather than the underlying representation. Besides two new state-of-the-art shortcut mitigation approaches, our findings more fundamentally connect shortcut learning to calibration theory and algorithmic fairness.

---


### 370. [Designing for Healthy, Affordable, and Sustainable Human-HVAC Interactions for Heating in Smart Homes](https://arxiv.org/abs/2609.07936)

**<font color=#1a73e8>作者：</font>** Delong Korus-Du  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As geopolitical tensions, energy crises, and energy-intensive AI infrastructure intensify concerns about demand, affordability, and resilience, communities increasingly encounter these challenges through everyday energy practices, particularly winter heating. Against this background, the doctoral exposé, "Designing Human-HVAC Interaction for Healthy, Affordable, and Sustainable Heating in Smart Homes", is structured around four chapters. First, a multidisciplinary literature review defines and positions Human-HVAC Interaction, focusing on heating in smart homes. Second, longitudinal living lab studies with design probes examine everyday heating practices, thermal comfort, and indoor environmental quality, with attention to thermally vulnerable groups such as older adults, pregnant or menopausal women, parents with infants, and people affected by allergies or airborne pollutants. Third, a VR-based smart home demonstrator explores how heating and IEQ scenarios can be prototyped and evaluated as a virtual living lab, while critically examining the limits of representing bodily indoor climate conditions through VR. Fourth, follow-up design studies examine how VR-based insights can be translated into physical-digital prototypes that combine digital fabrication, distributed environmental sensing, and diverse interface forms for critical heating and IEQ contexts. The thesis aims to contribute a design-oriented understanding of Human-HVAC Interaction by building from a multidisciplinary literature review to empirical living lab and co-design studies, VR-based prototyping, and physical system development, examining how smart home users make sense of, negotiate, and respond to smart HVAC system.

---


### 371. [Bottom-up Modeling of Repeated Elements via Single Image Analysis-by-Synthesis](https://arxiv.org/abs/2609.07939)

**<font color=#1a73e8>作者：</font>** Syrine Kalleli, Alexei A. Efros, Mathieu Aubry  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of discovering repeated elements from a single image. In contrast to existing approaches that depend on large annotated datasets, curated multi-image collections, or object segmentation masks, we show that a single image can suffice to learn a meaningful object model in a completely bottom-up fashion, without any prior knowledge beyond a coarse scale prior. Our method learns a tunable image-space prototype of the repeated elements through a reconstruction objective, enabling the model to identify and synthesize consistent object instances within the same image. Experiments on 116 real images from the FSC-147 dataset demonstrate that our method successfully learns coherent element models and captures intra-category variation on challenging images. Qualitative results reveal superior reconstructions and interpretable decompositions compared to classical decomposition, joint alignment, and 3D object modeling methods, while maintaining a simple 2D formulation. These results suggest that meaningful object discovery can emerge from single image learning alone.

---


### 372. [Structured Extrema Errors in Classical Surrogates for Viscous Burgers: A Physics-Consistent Interpretation](https://arxiv.org/abs/2609.07952)

**<font color=#1a73e8>作者：</font>** Youssef Oubari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the local errors of classical machine-learning surrogate models, which approximate the time evolution of the one-dimensional viscous Burgers equation. Four models are compared on the same prediction task, using the spatial grid values directly: radial basis function (RBF) kernel ridge regression (KRR), linear Ridge, ExtraTrees, and Random Forests. Across all four models, the one-step residual, defined here as the true value minus the predicted value at each grid point, forms clear curved branches near predicted maxima and minima. A more detailed analysis of KRR shows that these errors are much more strongly related to the second spatial derivative, which measures local curvature, than to the first spatial derivative. Near a smooth extremum, predicted value and curvature form a local two-branch fold. Under our local curvature-based model of the residual, this fold predicts a leading-order near-parabolic relation between predicted value and residual. This geometric result motivates a direct test of the Burgers advection (transport) and diffusion (smoothing) terms. For KRR and Ridge, regression tests on held-out trajectories, a control that breaks the spatial alignment of the diffusion term, and a spectral test of high-frequency content are consistent with insufficient viscous smoothing at moderate and high viscosity. In this case, the surrogate retains more small-scale structure than the true future state. The same physical explanation is much weaker for the tree models. Finally, a correction that uses only predicted quantities reduces both one-step error and error during recursive rollout, where each prediction is used as the next input.

---


### 373. [Support Topology and Gradient Mixing in Sinkhorn Layers](https://arxiv.org/abs/2609.07954)

**<font color=#1a73e8>作者：</font>** Dylan Forde  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Sinkhorn layers use a fixed support graph to restrict transport between tokens. How does this graph control gradient propagation through the scaling iterations. We develop a fixed-support calculus showing that each row-column cycle induces a row-stochastic operator on column-potential perturbations modulo constants. Its transpose propagates zero-mass reverse-mode cotangents. The finite-cycle operator uses two distinct half-step transport plans; at a balanced fixed point it reduces to a two-step walk determined by a single plan. We derive the accompanying score and marginal source terms and use Dobrushin contraction and minorization to bound homogeneous and source-driven tail cotangents. Our main result characterizes when support and marginals guarantee one-step contraction uniformly over finite scores: every feasible face of the transportation polytope must have pairwise two-hop column overlap. Otherwise, suitable score directions make the contraction coefficient arbitrarily close to one. We extend this analysis to ordered support schedules and derive certificates for partition heat-bath layers, coordinate sweeps, forced shared mass, and register-augmented supports. These results provide mathematical criteria for support design in differentiable transport layers, with guarantees restricted to the fixed-support quotient-gradient component.

---


### 374. [$α$-Graph: Attention-Infused Normalizing Flow Approach to Tractable Graph Modeling](https://arxiv.org/abs/2609.07961)

**<font color=#1a73e8>作者：</font>** Thanh-Dat Truong, Sarah Alharbi, Susan Gauch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph modeling, a crucial task for representing complex relationships in graph-structured data, has achieved significant success in recent years. However, current graph modeling methods rely on traditional Graph Neural Networks and pre-training approaches to implicitly learn the underlying relational structure of graph data. Thus, these prior methods cannot capture the complex graph structure and correlations among inputs. In this paper, we introduce a novel Attention-based Normalizing Flow-based Approach\footnote{Our implementation and models will be released publicly for research reproducibility.} (ANFA or $\alpha$) that provides an explicit, interpretable, and tractable Graph Modeling ($\alpha$-Graph). In particular, we propose a new Unconditional Graph Normalizing Flow with an Invertible Attention Mechanism to capture the complex relational structure of graph data. To further enhance the expressiveness of the model, we introduce Conditional Graph Normalizing Flow with Learnable Queries that enables efficient modeling of correlations in graph-structured data. We show that our Conditional Graph Normalizing Flows behave similarly to Unconditional Graph Normalizing Flows, enhancing expressiveness while maintaining training stability and efficiency. Our experimental results on three benchmarks will illustrate the effectiveness and the state-of-the-art (SoTA) performance of the proposed $\alpha$-Graph method.

---


### 375. [Guppy: Efficient Light Clients via Recursive Zero-Knowledge Proofs](https://arxiv.org/abs/2609.07963)

**<font color=#1a73e8>作者：</font>** George Danezis, Deepak Maram, Arnab Roy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional light clients rely on validators committing to the entire blockchain state at every block via a state commitment such as a Merkle tree, allowing clients to verify facts using short proofs. However, maintaining large and ever-growing state trees imposes a significant burden on validators and lies on the critical path of block production. As a result, many modern high-throughput chains avoid this approach altogether. This work asks whether efficient inclusion proofs can be supported without requiring validators to maintain full state commitments. We present Guppy, a protocol that achieves this by having validators commit to just the state updates. An off-chain, untrusted service, secured by recursive Zero-Knowledge Proofs (ZKPs), then maintains a verifiable Merkle tree over the full state. This design keeps validator overhead negligible and does not increase the asymptotic complexity of block construction. Our design rests on two key technical ideas. First, a hash-chain commitment moves validator signature verification out of the ZK circuit, keeping the proving circuit efficient. Second, we design a parallel recursive proving pipeline that leverages cheap recursion in modern ZKPs to ensure latency grows only logarithmically with throughput. Our Plonky2-based implementation demonstrates that Guppy can maintain a Merkle tree of size 2^30 while processing thousands of updates per second, adding only 2-4 s of latency.

---


### 376. [Rethinking Sign Language Translation: The Impact of Signer Dependence on Model Evaluation](https://arxiv.org/abs/2609.07965)

**<font color=#1a73e8>作者：</font>** Keren Artiaga, Sabyasachi Kamila, Haithem Afli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign Language Translation has advanced with deep learning, yet evaluations remain largely signer-dependent, with overlapping signers across train/dev/test. This raises concerns about whether models truly generalise or instead rely on signer-specific regularities. We conduct signer-fold cross-validation on GFSLT-VLP, GASLT, and SignCL, three leading, publicly available, gloss-free SLT models, on CSL-Daily and PHOENIX14T. Under signer-independent evaluation, performance drops sharply: on PHOENIX14T, GFSLT-VLP falls from BLEU-4 21.44 to 3.59 and ROUGE-L 42.49 to 11.89; GASLT from 15.74 to 8.26; and SignCL from 22.74 to 3.66. We also observe that in CSL-Daily many target sentences are performed by multiple signers, so common splits can place identical sentences in both training and test, inflating absolute scores by rewarding recall of recurring sentences rather than genuine generalisation. These findings indicate that signer-dependent evaluation can substantially overestimate SLT capability. We recommend: (1) adopting signer-independent protocols to ensure generalisation to unseen signers; (2) restructuring datasets to include explicit signer-independent, sentence-disjoint splits for consistent benchmarking; and (3) reporting both signer-dependent and signer-independent results together with train-test sentence overlap to improve transparency and comparability.

---


### 377. [Heat Field Signatures: From Point Clouds to Smooth Geometry](https://arxiv.org/abs/2609.07975)

**<font color=#1a73e8>作者：</font>** Yuanqing Wang, Yapeng Tian, Baris Coskunuzer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bringing multiscale geometric analysis directly to irregular point clouds remains difficult: quantities such as local dimension, anisotropy, density variation, and geometric transitions are typically estimated through explicit neighborhood, manifold, or graph constructions, or left for neural networks to infer from coordinates. We introduce Heat Field Signatures (HFS), which lift a point cloud to a multiscale family of smooth ambient heat fields, providing a direct interface from discrete samples to geometric analysis.
From this field, HFS computes closed-form global and local signatures directly from pairwise distances, capturing heat concentration, intrinsic dimension, anisotropy, and scale transitions. We further introduce the Heat Dimension Spectrum (HDS), a compact summary of multiscale geometric composition. HFS can be used as a closed-form descriptor, a lightweight learned representation, or a geometric feature channel for neural point-cloud models.
Across synthetic and real-world benchmarks spanning subcellular, neuronal, tree, and protein data, HFS outperforms strong point-cloud and multiparameter-persistence baselines while substantially reducing end-to-end cost. On SCOP protein-fold classification, HFS improves over the strongest deep baseline by nearly $24$ percentage points using coordinates alone, while standalone HFS representations are exactly rotation-invariant by construction. More broadly, HFS turns a classical heat field into a practical interface for multiscale geometric analysis in modern point-cloud learning.

---


### 378. [Semi-Supervised Learning under Spatially Biased Sampling](https://arxiv.org/abs/2609.07982)

**<font color=#1a73e8>作者：</font>** Bright Wiredu Nuakoh, Francky Fouedjio, Stephen Bradshaw 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard semi-supervised learning (SSL) typically relies on labelled and unlabelled data sharing a common marginal distribution. This assumption is often violated by biased spatial sampling mechanism, when labels are collected under spatially biased or preferential site selection. We treat this marginal mismatch, spatial autocorrelation, and spatial non-stationarity as three distinct mechanisms, varied independently via a labelled-sampling concentration parameter, a spatial length scale, and a non-stationarity strength parameter, and ask how mismatch degrades SSL, whether the cluster and manifold assumptions survive it, and how the resulting failure can be diagnosed. Using a controlled synthetic framework alongside PovertyMap-WILDS, California housing, socio-economic and US air quality monitoring datasets, we systematically vary the degree of mismatch while accounting for spatial autocorrelation and non-stationarity. Through a series of analyses including a segmented-regression changepoint, we show that in the synthetic generator, SSL performance does not degrade gradually but instead exhibits a threshold-like breakdown between approximately 0.71 and 0.77 once distribution mismatch becomes sufficiently severe. We further demonstrate that spatial non-stationarity contributes to performance loss independently of marginal mismatch and that models become increasingly overconfident outside the regions where labels are available. To support practical deployment, we evaluate several distribution-divergence measures as indicators of reliability and introduce a kernel-weighted local divergence metric that provides a more stable estimate of spatial mismatch than a naïve localised approach. These findings provide empirical evidence and diagnostic tools for better documenting the risk of incorporating unlabelled spatial data into semi-supervised learning workflows.

---


### 379. [Solving the Elastic Wave Equation with Physics-Informed Neural Networks: A Robust and Critical Assessment](https://arxiv.org/abs/2609.07983)

**<font color=#1a73e8>作者：</font>** Davide Staub, Ben Moseley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) have recently emerged as a promising approach for solving Partial Differential Equations (PDEs), offering a meshfree alternative that integrates physical principles into the learning process. This presents a new paradigm compared to traditional discretization methods and purely data-driven machine learning techniques. While promising, PINNs are not a panacea; they inherit challenges such as spectral bias and unstable convergence. Moreover, their potential in seismology remains largely unexplored. In this work, we provide a robust and critical assessment of PINNs for solving the elastic wave equation in seismology. We investigate the performance of PINNs on problems with varying degrees of complexity across various seismic sources and parameter models, from constant to highly heterogeneous settings. A pivotal aspect of our work involves investigating whether embedding physical principles directly into the network architecture enhances convergence and accuracy. We test an extensive range of neural architecture designs, from unrestricted, uninformed PINNs to highly specialized ones. We find that integrating an understanding of wave physics into the network design significantly improves accuracy. For instance, introducing a custom wavelet or plane wave layer, coupled with encoder and decoder layers, consistently yields a relative $L_2$ error approximately half that of the standard PINN, as evidenced across numerous experiments. We further demonstrate that this novel architecture enhances accuracy when applied to the acoustic wave equation, underlying the versatility of our network. Another key contribution of our research is the successful conditioning of PINNs on seismic source locations. This signifies a considerable advancement towards rapid seismic hazard detection and seismic analysis.

---


### 380. [HyCO: A Hybrid Neural Solver for Combinatorial Optimization](https://arxiv.org/abs/2609.07990)

**<font color=#1a73e8>作者：</font>** Yuheng Li, Di Yang, Haipeng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential reinforcement learning (RL) solvers and global diffusion model (DM) solvers for neural combinatorial optimization exhibit complementary failure modes under an optimization-regret view. The former enjoys small marginal regret in the early construction stage, but suffers from horizon-wise compounding errors with super-linear regret growth; the latter avoids horizon compounding but incurs linear or sublinear regret w.r.t. the dimension of the remaining unsolved subspace. We propose Hybrid Neural Solver for Combinatorial Optimization (HyCO), a hybrid inference algorithm that constructs a solution prefix with an RL solver and adaptively switches to a conditional DM to complete the remaining decisions. To characterize why such hybridization helps, when to trigger the handover, and how to realize it in practice, we first develop a unified error-scaling theoretical framework and prove that, under explicit error-scaling assumptions, i) the hybrid structure achieves strictly lower expected regret than either backbone alone, and ii) there exists a unique optimal trigger step that minimizes the hybrid regret. We then design a lightweight adaptive trigger that combines policy entropy and RL-DM disagreement to detect trajectory-level signals of the regime shift as a practical proxy, since the optimal trigger step is defined at the expected-regret level and is not directly computable on individual trajectories. Experimental results on diverse benchmarks demonstrate that HyCO achieves consistent improvements over both backbones and support the empirical effectiveness of adaptive triggering.

---


### 381. [Sharp Structure-Agnostic Minimax Risk for Partial Linear Models](https://arxiv.org/abs/2609.07997)

**<font color=#1a73e8>作者：</font>** Haichen Hu, David Simchi-Levi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We characterize the sharp structure-agnostic minimax risk for coefficient estimation in the partial linear model when the outcome and treatment nuisances are learned by two distinct black-box learners, which resolves the open problem in double machine learning posed by Gu (2025). For each nuisance \(q\in\{\mu,\pi\}\), we characterize the available learner by an approximation-error budget \(a_q\) and a stochastic-error budget \(s_q\), with the latter controlled through localized Rademacher complexity. Writing \(\mathcal E_n\) for the minimax mean-squared error, we show that \[\mathcal E_n\asymp1\wedge\left\{\frac1n+\left(a_\mu a_\pi+\min\left\{a_\pi s_\mu+s_\pi^2,\,a_\mu s_\pi+s_\mu^2\right\}\right)^2\right\}.\] The main new ingredient is a novel lower bound for the general two-learner problem. Our proof constructs four finite-mixture testing experiments using orthogonal code functions. Across these experiments, the hidden perturbations are placed outside both learner classes, outside only the treatment learner class, outside only the outcome learner class, or inside both learner classes. These four configurations capture, respectively, the interaction between the two approximation errors, the two asymmetric interactions between one learner's approximation error and the other learner's learning error, and the joint estimation difficulty of learning both nuisances. Combining the four resulting lower bounds yields the displayed rate, which matches the latest upper bound in Gu (2026). Our result shows that standard double machine learning can overstate the intrinsic difficulty of target estimation and provides a target-specific principle for learner selection: approximation error and stochastic complexity must be jointly balanced across the two nuisance learners rather than optimized separately.

---


### 382. [Mini-Batch Risk-Averse Deep Q-Learning: A Robot Navigation Case Study](https://arxiv.org/abs/2609.07998)

**<font color=#1a73e8>作者：</font>** Aayush Patel, Andrzej Ruszczyński  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the control of Markov decision processes in which the quality of a policy is evaluated by a dynamic, time-consistent Markov risk measure rather than by an expected discounted cost. The main obstacle to combining such measures with reinforcement learning is that a transition risk mapping depends on the transition kernel in a nonlinear way, and therefore cannot be estimated from a single observed transition. We remove this obstacle by employing mini-batch transition risk mappings: the mapping is applied to the empirical measure of $N$ independent next-state samples, and the result is averaged. The resulting mapping is again coherent. However, as an expected value of a function of $N$ next-state values, it admits an unbiased one-sample estimator.
We embed this mapping into a double deep Q-network, analyze the two sources of estimation bias that arise, and obtain a risk-averse Q-learning method applicable to state spaces far beyond the reach of tabular schemes. The method is applied to an underwater robot navigation problem, in which a vehicle must visit collection points, gather stochastic information payloads, and deliver them at transmission points, while exposed at each step to the risk of destruction. A hierarchical decomposition delegates path execution to an exact graph search and confines learning to the high-level ``collect or transmit'' decision. A low-dimensional feature map, invariant under the symmetries of the problem, replaces the raw state--configuration encoding. In experiments on $300$ held-out environments, the resulting policies transfer to instance sizes never seen in training, and already $N=2$ reduces the upper semideviation of the outcome distribution while simultaneously improving its mean whenever the simulator is misspecified---an empirical counterpart of the duality between coherent risk measures and distributional robustness.

---


### 383. ["Shut Up and Let Me Enjoy My Otome": Understanding and Measuring the Toxicity in Otome Game Communities](https://arxiv.org/abs/2609.08009)

**<font color=#1a73e8>作者：</font>** Yage Zhang, Xinyue Shen, Yukun Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Otome games, a romance simulation genre primarily targeting female, have emerged as a major force in the global gaming market, attracting hundreds of millions of players and billions in revenue. Despite their popularity, otome game communities face pervasive online toxicity, which has been largely unexplored. In this work, we present the first large-scale measurement of toxicity in otome game communities across social platforms. We introduce OtomeSCAN, a framework for collecting, evaluating, and analyzing 620,045 posts from Weibo and Reddit spanning 18 months. To support robust analysis, we manually annotated a ground-truth dataset of 4,308 posts, identifying eight target groups such as players and game developers. We evaluate seven toxicity detectors on the dataset, including general-purpose models and our proposed LLM-based detectors, with our best model achieving F1-scores of 0.82 (Weibo) and 0.78 (Reddit). Our analysis reveals significant platform-based differences in toxicity: 22.20% of otome-related posts on Weibo are toxic, compared to 3.71% on Reddit. Besides, real-world events like in-community conflicts can rapidly escalate toxicity, with toxicity ratios increasing to 37.09% in just 72 hours during an external attack on Weibo. We also flag 191 potential-coordination clusters in otome game communities, 64.40% of which target game developers, with several accounts participating repeatedly across multiple clusters. We hope our work inspires further research on community-specific toxicity and contributes to building healthier online spaces for marginalized gaming communities.

---


### 384. [TaskGuard: Task-Conditioned Restoration Utility for Risk-Aware Object Detection](https://arxiv.org/abs/2609.08011)

**<font color=#1a73e8>作者：</font>** Vung Pham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration is commonly applied before object detection under adverse conditions, yet a visually improved image need not improve the downstream task. We study this mismatch as restoration utility prediction: given a degraded image and its candidate restoration, should the restoration be used or should the original observation be preserved? We introduce TaskGuard, a post-hoc controller for frozen restoration and detection pipelines. TaskGuard characterizes the realized restoration residual through its interaction with detector sensitivity and predicts whether the intervention is task-beneficial. Exact regional counterfactuals reveal substantial within-image utility heterogeneity, while a deployable pseudo-gradient preserves statistically reliable directional information. Feature-group ablation further shows that task-conditioned evidence contributes information beyond detector-response and residual statistics. The TaskGuard utility predictor is trained only on Gaussian degradation and frozen before final evaluation, then transferred to unseen motion blur, rain, and defocus. Across these unseen families, TaskGuard reduces lossnegative interventions by 54.2% (family macro) and practical per-image detection deteriorations by 37.0% (pooled), while preserving 98.8% of the Always-Restore COCO AP. On natural-rain DAWN, it reduces loss-negative interventions by 97.9% while retaining 77.8% of the AP improvement obtained by deraining. These results support restoration utility as a task-conditioned property of the specific intervention rather than image appearance alone.

---


### 385. [A Black-Box Adversarial Attack on Human Pose Estimation and Keypoint-Based Action Recognition Models](https://arxiv.org/abs/2609.08013)

**<font color=#1a73e8>作者：</font>** Kacper Mroczek, Michal Kepski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human pose estimation and keypoint-based action recognition models are increasingly deployed as components of video understanding pipelines, yet their vulnerability to adversarial attacks remains insufficiently studied. Temporally coherent black-box attacks have been previously studied in visual object tracking, where the attack feedback can be defined using bounding-box overlap measures such as Intersection over Union (IoU). However, human pose estimation produces keypoint configurations rather than enclosing boxes, making box-level similarity poorly suited for measuring pose degradation. We propose OKS Attack, a decision-based black-box attack that uses Object Keypoint Similarity (OKS) as the attack feedback signal, directly targeting the spatial structure of human poses rather than their enclosing boxes. Experiments on the Penn Action dataset show that OKS Attack consistently reduces pose quality across evaluated pose estimators, with mean OKS decreases ranging from 0.0802 to 0.1494. In a downstream cross-dataset action-recognition evaluation, the attack reduces accuracy by 6.18 to 13.86 percentage points and outperforms query-matched random-noise perturbations. The attack is effective across both top-down and single-stage pose estimation models. The source code will be made publicly available at this https URL

---


### 386. [From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents](https://arxiv.org/abs/2609.08015)

**<font color=#1a73e8>作者：</font>** Yongjian Lyu, Yang Ren, Ruofei Lai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running AI agents may read state, reason, wait for tools or human approval, and perform an external action much later. The state that justified the action can change in the meantime. For example, after an agent proposes an 80 GBP refund under a limit of 100, a customer-name change affects only presentation metadata, a new limit of 90 still permits the refund, a limit of 50 invalidates it, and a refund issued by another worker must prevent a duplicate. Standard optimistic concurrency control and version checks can detect that previously read state has changed, but by themselves do not determine whether that change invalidates the pending action's justification. We call any detected version change a version conflict; when that change invalidates the action's justification, it is also a decision conflict. ATR records the explicit, executable conditions that justify a pending action and rechecks only the conditions affected by a change before releasing the external operation. It can retain the action, refresh non-decisive metadata, require replanning, or block execution; a target-side transaction or compare-and-set binds checked state to commit. Across 210,000 controlled executions over 15 mutation cases, ATR matched every developer-specified outcome with no false allows or blocks. In ten durable SQLite checkpoint/resume cells, it evaluated 0.6 conditions per change versus 6.0 for FullScan. At 4,093 recorded reads, ATR took 9.3 microseconds versus 2595.9 microseconds for FullScan. These deterministic results establish controlled feasibility, not production generality or automatic extraction of the required conditions.

---


### 387. [Delusions and Harms Associated with AI Chatbot Use: Early Evidence from 185 Real-World Reports](https://arxiv.org/abs/2609.08027)

**<font color=#1a73e8>作者：</font>** Hamilton Morrin, Vinitha Soundararajan, Thomas Cheliotis-James 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Importance: Reports have raised concerns that AI chatbots may validate or elaborate delusional beliefs, respond inappropriately to suicidal ideation, and contribute to mental health harms, but real-world data on reported harms remain limited.
Objective: To characterize psychopathological features, chatbot behaviors, timing, and outcomes in first- and second-hand accounts of mental health harm linked with AI chatbot use.
Design: Cross-sectional secondary analysis of deidentified online survey responses gathered between August 7, 2025, and February 2, 2026.
Main Outcomes and Measures: The primary quantitative outcome was the presence of delusional beliefs, coded by paired raters with relevant clinical experience. Additional variables included reason for chatbot use, current episode features, delusional content, chatbot validation of beliefs, harms, social and occupational consequences, healthcare use, and timing.
Results: 95 first-hand and 90 second-hand accounts were analyzed. Median age was 35.0 (IQR 27.0 - 45.0). Raters coded descriptions consistent with delusional beliefs in 102 reports (55.1%), with chatbot validation of beliefs in 50/102 (49.0%). Common outcomes included isolation, relationship breakdown, hospital admission, job loss, and financial loss. Four second-hand reports described death by suicide.
Conclusions: In this self-selected convenience sample, AI-chatbot-associated harms were frequently described in relation to delusional beliefs, perceived chatbot validation, intensive use, and substantial social, occupational, and clinical consequences. Because reports were retrospective, unverified, and collected from individuals seeking to report harm, our findings should be interpreted as preliminary signal detection rather than as suggesting prevalence or providing evidence of causality. Prospective surveillance and trajectory-based safety evaluations are needed.

---


### 388. [Flexible Motion Generation from Language and Style References](https://arxiv.org/abs/2609.08032)

**<font color=#1a73e8>作者：</font>** Kai Weixian Lan, Bodie Criswell, Briana Fedkiw 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce FlexMoGen, a novel framework for flexible human motion synthesis conditioned on both natural language descriptions and motion style references. Text prompts are effective at defining semantic content, but they are often limited in capturing fine-grained style details such as timing, limb articulation, and expressive dynamics. A style example clip supplements the text by conveying these nuanced motion characteristics directly, enabling the model to preserve high-level intent while reproducing the desired stylistic traits. Given a text prompt and a style example clip, FlexMoGen generates high-quality motions that preserve semantic content while faithfully reflecting the target style, offering users greater control over the animation generation process. Unlike prior methods that rely on discrete style labels and do not generalize to long or multi-style generation, FlexMoGen learns a variational style encoder without style supervision and supports long, time-varying, multi-style synthesis. Our framework jointly pre-trains the style encoder and a text-to-motion latent diffusion model within a unified architecture, modulating motion style through a lightweight adaptation module. It integrates an efficient relative positional encoding scheme and is trained on both stylized and non-stylized datasets, enabling strong generalization to unseen text-style combinations. Experiments show that FlexMoGen achieves the best balance between content fidelity and style reflection.

---


### 389. [Two-Scale Localized PCA-Net: Coarse-Global and Local-Residual Representations for Artifact-Reduced PDE Operator Learning](https://arxiv.org/abs/2609.08034)

**<font color=#1a73e8>作者：</font>** Mrigank Dhingra, Jordan Stout, Omer San  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Localized dimensionality reduction improves the scalability of operator learning for high-dimensional partial differential equations (PDEs), but independently decoded local patches can introduce block offsets, interface mismatches, and spurious high-wavenumber content. We introduce Two-Scale Localized PCA-Net, which decomposes the solution into a coarse-global component and local residual corrections. A compact global PCA basis captures domain-scale structure, while nonoverlapping local PCA bases represent the remaining fine-scale residual. A block-balanced latent objective couples the two representations, and optional interface-aware fine-tuning further promotes continuity through reconstruction and trace losses. On Poisson benchmarks, the two-scale representation substantially reduces reconstruction error and visible block artifacts relative to plain and overlap-based localized PCA-Net while approximately halving PCA fitting cost relative to overlap. On heterogeneous Darcy flow, it strongly reduces interface and discrete-residual errors, with more modest reconstruction gains. Ablations show that the primary improvement arises from the two-scale output representation, while interface-aware fine-tuning provides complementary continuity refinement. Overall, separating globally coherent structure from localized residual detail provides an efficient representation for artifact-reduced PDE operator learning.

---


### 390. [Representational Fidelity in Didactic Visualization: Toward a Multidimensional Design Space](https://arxiv.org/abs/2609.08037)

**<font color=#1a73e8>作者：</font>** Shehryar Saharan, Michele Oliver, Karen Gordon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Representational fidelity is routinely treated as a single abstract-realistic continuum, a simplification that limits how it is described and compared across research and design contexts. We introduce a multidimensional design space of representational fidelity for didactic visualization in science & engineering, inductively derived from a 175-item corpus spanning several disciplines, modalities, and instructional aims. The resulting design space specifies five dimensions: Morphological, Dynamic, Cueing, Contextual, and Interactive Fidelity, with seven sub-dimensions. We demonstrate the design space's descriptive power through successive rounds of expansion and refinement and analyze the corpus to reveal relationships among dimensions and implications for design and research. We further validate the design space through a pilot focus group in which participants applied the dimensions in an open-ended design exercise. Resulting sketches and verbal rationales informed a single-designer applied case study, offering preliminary evidence of the design space's generative potential as a structured aid to design exploration. Together, these contributions lay the groundwork for future research and more intentional design practice.

---


### 391. [SAFER-Activities: A Dataset for Smart Assessment of Fall Events and Routine Activities](https://arxiv.org/abs/2609.08038)

**<font color=#1a73e8>作者：</font>** Diwas Lamsal, Pramod Wickramatilake, Jednipat Moonrinta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smart healthcare monitoring systems require precise action recognition to ensure well-being and timely intervention in critical situations such as falls, particularly for mobility-challenged individuals. Existing datasets are often clip-based, lacking the frame-level detail needed to recognize actions online, as they unfold. To address this, we introduce SAFER-Activities, a dataset for fall detection and physical activity monitoring, with a dedicated subset for wheelchair use scenarios. It comprises over 66 hours of video data captured by multiple cameras, with 85,310 action instances and frame-level annotations for 30 action classes. We benchmark action recognition on SAFER-Activities with 2D and 3D skeleton models, RGB models with frozen backbones, and multimodal fusion strategies, and evaluate on in-lab, out-of-distribution, and cross-dataset test sets. Skeleton-based models generalize best under domain shift; fusing frozen RGB features with the skeleton stream improves in-domain recognition over the baseline CNN1D, most clearly on the wheelchair subset, but degrades out of distribution. Cross-dataset and qualitative evaluations confirm that models trained on SAFER-Activities transfer well to unseen environments and external fall data. To support research on robust fall detection and activity monitoring, we release the dataset and code at this https URL.

---


### 392. [MamMA: A Mamba-Based Pedestrian Trajectory Prediction Algorithm Considering Occupancy Map and Pedestrian Awareness States](https://arxiv.org/abs/2609.08041)

**<font color=#1a73e8>作者：</font>** Juncen Long, Xiaofeng Jin, Gianluca Bardaro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many pedestrian trajectory prediction algorithms have been proposed to improve the safety of navigation for mobile robots working in human-robot coexistence environments. Some pedestrian trajectory prediction algorithms extract information about obstacles near pedestrians from top-down view images to improve the accuracy of trajectory prediction. However, mobile robots typically create local occupancy maps using LiDAR, rather than top-down view images. Meanwhile, the vision sensors on board robots provide egocentric view images, which contain fine-grained behavioral information about the pedestrians near the robot. To better use the information collected by LiDAR and on-board vision sensors, we propose MamMA, a Mamba-based pedestrian trajectory prediction algorithm considering occupancy maps and pedestrian awareness states. MamMA divides the occupancy map by patches and extracts obstacle features from each patch to create map features. Pedestrian awareness states are divided and considered, as some studies show that awareness states affect the perception and speed of pedestrians. Furthermore, a Mamba-based model is proposed to predict the future trajectories of pedestrians based on different types of features. Experiments on the STCrowd, SiT, JRDB, ETH, and UCY datasets show that MamMA achieves better average displacement error and final displacement error than the state-of-the-art algorithms.

---


### 393. [A Quantitative Evaluation Framework for Temporal Explainability in Echocardiographic Video Segmentation](https://arxiv.org/abs/2609.08043)

**<font color=#1a73e8>作者：</font>** Jiyoo Noh, Jonathan H. Chan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has achieved state-of-the-art performance in echocardiographic video segmentation, with an increasing number of models incorporating temporal information. However, quantitative evaluation of temporal explainability remains largely unexplored. We propose a quantitative framework for evaluating Grad-CAM explanations using four complementary metrics measuring temporal consistency, saliency motion, anatomical overlap, and temporal overlap. Using EchoNet-Dynamic, we compare a baseline 2D U-Net with ConvLSTM U-Net models trained across multiple temporal strides. While segmentation performance remained comparable across all models, intermediate ConvLSTM explanations exhibited substantially lower saliency consistency and greater centroid motion than final prediction explanations. Temporal Bottleneck explanations were significantly more stable than Encoder Bottleneck explanations across all strides, while final ConvLSTM Decoder3 explanations were broadly comparable to those of the 2D U-Net. Importantly, conventional frame-wise explanation metrics cannot determine whether variation in intermediate explanations reflects meaningful temporal feature evolution or explanation instability. These findings establish a preliminary quantitative framework for temporal explainability and motivate temporal-aware XAI methods that explicitly account for evolving representations in medical video models.

---


### 394. [RFS-UNet: Decoder-Conditioned High-Resolution Skip Recalibration for Bone-Selective DRR Synthesis](https://arxiv.org/abs/2609.08044)

**<font color=#1a73e8>作者：</font>** Xiaoyang Li, Yixuan Liu, Yuan Chai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bone-selective digitally reconstructed radiograph (DRR) synthesis depends on high-resolution encoder detail, yet static skips cannot condition reuse on the evolving decoder representation. We ask whether decoder state adds useful information beyond encoder-only self-recalibration for high-resolution skip reuse. RFS-UNet uses pooled encoder and aligned decoder statistics for bounded residual channel recalibration at the 512^2 and 256^2 skips, leaving the backbone unchanged. In the matched seed-2026 comparison isolating decoder conditioning, RFS raises validation PSNR by 0.254 dB over Self-RFS. Across three seeds, locked-test PSNR rises from 33.225+/-0.048 to 33.537+/-0.128 dB; RFS lowers MAE in 179/200 held-out CT cases and reduces mean MAE by 3.91%. It adds 0.117% parameters and 1.169% counted Conv2d operations. These results support decoder state as a useful conditioning signal for high-resolution feature reuse in controlled paired projection synthesis.

---


### 395. [BrachistoneLR: A Brachistochrone-Inspired Learning-Rate Schedule and a Controlled Benchmark of Scheduling Policies](https://arxiv.org/abs/2609.08069)

**<font color=#1a73e8>作者：</font>** Md. Sadekur Rahman Roni, Md. Jalal uddin Chowdhury, Moutusi Dash Nimi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The learning-rate schedule is a consequential choice in training deep networks, yet the policies in common use are heuristic, and published comparisons are hard to read, because architecture, dataset, and budget tend to vary alongside the schedule. We study BrachistoneLR, a schedule built by mapping the vertical coordinate of the brachistochrone, the curve of fastest descent under gravity, onto the range between a peak and a floor rate. Expanding the definition shows it to be cosine annealing with the half-period set to E - 1 instead of E, the configuration a standard implementation gives when its period argument is one less than the number of epochs. The rate therefore reaches its floor at the last epoch trained rather than one epoch later, and we show this difference decays as E^-2, making it a short-horizon effect. We then benchmark six schedules over 72 runs on three image classification datasets (MNIST, Fashion-MNIST, CIFAR-10) and four architecture families (fully connected, convolutional, recurrent, residual), fixing the optimizer, data pipeline, and evaluation protocol so that only the schedule varies. Schedules that fall smoothly from peak to floor beat the constant rate and calendar-based decay by margins that grow with task difficulty, reaching 2.5 points of dataset mean on CIFAR-10. Within that leading group, BrachistoneLR, cosine annealing, and warmup-cosine lie within 0.06 accuracy points and 0.17 of a mean rank, which one seed per configuration cannot separate. BrachistoneLR is best on both residual networks and has the highest CIFAR-10 mean, and it sets no milestones, decay factor, warmup length, or restart period. We conclude that the shape of a schedule matters more than its parameterization, that the choice of whether to use a smooth schedule matters more than the choice among them, and that the terminal-rate distinction is worth attention only over short horizons.

---


### 396. [A Machine Learning Framework for Predicting Restaurant Food Waste to Support Sustainable Food Management](https://arxiv.org/abs/2609.08078)

**<font color=#1a73e8>作者：</font>** Md Mehedi Hasan Naeem, Md Ashraful Islam, Moumita Barua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Food waste in the restaurant sector poses a substantial challenge to environmental sustainability and economic efficiency. This paper presents an exploratory machine learning framework for estimating daily restaurant food waste quantities from operational and contextual features. A structured dataset was constructed by integrating restaurant demand records, meteorological data and temporal event indicators, yielding 77,980 records across 27 features. Because large-scale ground-truth food waste measurements are not publicly available, the target variable was derived from operationally justified assumptions, with the complete construction formula and controlled stochastic variability disclosed for full reproducibility. Four supervised regression models, namely Linear Regression, Decision Tree, Random Forest and Gradient Boosting, were evaluated under a chronological 70-30 train-test split that respects the temporal ordering of restaurant operations, augmented by 5-fold time-series cross-validation. All reported metrics are explicitly scoped to performance against the constructed target and do not imply validation against measured food waste. Ensemble methods consistently outperformed linear baselines. Random Forest attained an MAE of 6.19 kg, RMSE of 8.36 kg and $R^2$ of 0.817 on the realistic feature subset following systematic exclusion of algebraically leakage-prone variables. Feature importance analysis identified menu diversity, operational area and temporal activity patterns as the primary predictive drivers. The full dataset, target construction formula, codebase and experimental configurations are publicly released to support reproducibility and future extension to empirically measured waste data.

---


### 397. [Proactive Context-Forecasted Safety Constraints for Nonstationary Reinforcement Learning](https://arxiv.org/abs/2609.08080)

**<font color=#1a73e8>作者：</font>** Tim Tomashevskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring safety in reinforcement learning under nonstationarity requires anticipating changes in risk before they lead to unsafe behavior. Existing approaches typically rely on safety constraints defined at design time or updated reactively during execution, assuming that such constraints remain valid over time. However, in nonstationary environments with evolving contexts and changing driving layouts, these assumptions may fail.
We propose a framework for proactive safety constraint generation based on context forecasting. The approach infers latent environmental context from observations, predicts its future evolution, and constructs safety constraints adapted to anticipated conditions. This enables the agent to proactively avoid unsafe regions instead of reacting only after safety violations occur.
We evaluate the method in driving environments with structured context variation. The experiments include a sweep over nonstationarity intensities and additional held-out driving layouts, including highway, intersection, and racetrack scenarios. Results show that proactive constraint generation substantially reduces collisions under both seen and out-of-training nonstationarity intensities and generally remains effective across held-out driving layouts while maintaining usable task performance. These findings suggest that context-based constraint generation is a promising approach for safe reinforcement learning under nonstationarity.

---


### 398. [Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation](https://arxiv.org/abs/2609.08084)

**<font color=#1a73e8>作者：</font>** Igor Pavlovic, Thiemo Wandel, Anton Obukhov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation is a ubiquitous yet highly ill-posed computer vision task, with downstream applications in scene reconstruction, computational photography, and robotics, among others. Despite the field's maturity, recent models still struggle to generalize to out-of-distribution inputs and to produce sharp and detailed depth maps. In this paper, we revisit Marigold, a set of techniques for repurposing modern image generation and editing models, powered by the diffusion transformer (DiT) architecture, into state-of-the-art monocular depth estimators. Our recipes target single-step inference from pretrained multi-step flow-matching models, with quantization where needed, preserving model capacity while remaining cheap to run. We analyze the artifacts of naive training and identify two effective remedies: aligning the model's internal representations with semantic features extracted from ground-truth, and adopting a 2-stage fine-tuning protocol built around a novel Sinkhorn-based loss. The results are crisper, cleaner depth maps that generalize well out-of-distribution, with 16-26% improvement in AbsRel over the previous best on KITTI and ETH3D. Qualitatively, our model resolves fur, foliage, and hair-thin edges that have eluded prior models. Furthermore, Marigold V2 achieves state-of-the-art results when applied to other dense regression tasks, such as surface normals estimation and intrinsic image decomposition. Project website: this https URL

---


### 399. [Vectorizer: Vectorizing NumPy Programs with Shape-Guided Rewrite](https://arxiv.org/abs/2609.08088)

**<font color=#1a73e8>作者：</font>** Jingqian Liu, Xiaoyu Liu, Yuepeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> NumPy is a widely used Python library for numerical scientific computing, known for its declarative APIs and its optimized implementations. However, writing efficient NumPy programs, which often entails using vectorized array operations instead of explicit Python loops, may not be straightforward. This can be difficult for programmers who are accustomed to imperative array traversal, especially when vectorized API invocations require careful reasoning about shapes, broadcasting, and advanced indexing. This paper presents a rewrite-based approach for vectorizing Numpy programs with explicit loops over array data. Our approach vectorizes loops from the inside out, using array shapes and dataflow analysis to guide a source-to-source transformation that replaces loop bodies with vectorized statements. Following a set of rewrite rules that are correct by construction, our approach is consistently fast. We have implemented the approach as a tool called Vectorizer and evaluated it on 150 benchmarks collected from prior work and Stack Overflow. The evaluation shows that Vectorizer vectorizes 142 of the 150 benchmarks directly and 2 more after minor changes to the original benchmarks, with only 0.53 seconds on average to rewrite each one. The resulting programs are, on average, 74.83x faster than the original loop-based implementations.

---


### 400. [RevalExo: A Functional Daily-Activity Benchmark for Inertial and Visual Locomotion Mode Recognition in Older Adults and Clinical Cohorts](https://arxiv.org/abs/2609.08090)

**<font color=#1a73e8>作者：</font>** Diwas Lamsal, Juha Carlon, Reinhard Claeys 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assistive devices for people with mobility impairments, such as powered exoskeletons, rely on accurate locomotion mode recognition to adapt control strategies and provide appropriate assistance during daily activities. However, public benchmarks are typically collected from healthy adults, lack temporally precise labels necessary for detecting mode transitions, or focus on a limited set of tasks. To support development and evaluation under realistic clinical constraints and daily mobility demands, we introduce RevalExo, a functional daily-activity benchmark for inertial and visual locomotion mode recognition. RevalExo is built around a standardized, clinically and ecologically validated daily-activity protocol reflecting the cumulative everyday mobility demands in ageing and clinical populations. The benchmark includes 27 participants across three cohorts: older adults without mobility impairments, stroke survivors, and older adults with probable sarcopenia. The full cohort was recorded with lower-body IMUs, while synchronized egocentric video was collected for a clinically feasible subset of 13 participants. RevalExo provides 10.1 hours of frame-level annotations across 11 locomotion modes, including 5.1 hours of paired inertial--visual recordings. We benchmark three challenges: unimodal and multimodal locomotion mode recognition across multiple horizons, cross-population generalization from older adults without mobility impairments to clinical cohorts, and vision-guided knowledge transfer to IMU-only models. Results confirm consistent gains from fusing inertial and visual inputs but reveal a substantial gap between general recognition ($\sim$93\% F1) and recognition during transitions ($\sim$68\% F1), alongside persistent challenges in cross-population generalization and cross-modal transfer. We release RevalExo to stimulate further research on these open challenges.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
