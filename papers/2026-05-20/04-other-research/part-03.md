# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 101. [Tensor Cookbook: Mastering Tensors through Diagrams](https://arxiv.org/abs/2605.16610)

**<font color=#1a73e8>作者：</font>** Beheshteh T. Rakhshan, Guillaume Rabusseau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional data arise naturally in many areas of science and engineering, including machine learning, signal processing, computational physics, and statistics. Such data are often represented as tensors, multi-dimensional generalizations of matrices. While tensors provide a natural representation for multi-modal structure, their direct manipulation quickly becomes challenging as the order grows: the number of parameters increases exponentially, and algebraic expressions involving many indices become difficult to interpret and implement. Tensor networks (TNs) provide an effective framework for addressing these challenges. Originally introduced by Penrose and developed extensively in quantum physics, the graphical language of tensor networks encodes contractions as edges in a graph, reducing notational overhead and revealing structural properties obscured by index notation. Despite the central role of high-dimensional tensors in modern machine learning and numerical analysis, tensor network diagrams remain underutilized outside quantum computing, partly due to the lack of a self-contained mathematical reference accessible to a broad technical audience. This manuscript provides a self-contained guide to tensor networks and their use in tensor algebra. We present the main operations on tensors, contractions, products, and reshaping through, graphical notation, and show how classical tensor decompositions and related computations are naturally expressed in this framework. We also illustrate how tensor networks simplify the derivation of gradients and the manipulation of high-dimensional probability distributions. Throughout, we show that the diagrammatic approach yields genuinely shorter and more transparent proofs of classical identities, rank bounds, and gradient formulas that would otherwise require laborious index manipulation.

---


### 102. [PRISMat: Policy-Driven, Permutation-Invariant Autoregressive Material Generation](https://arxiv.org/abs/2605.16612)

**<font color=#1a73e8>作者：</font>** Claire Schlesinger, Circe Hsu, Peter Schindler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid identification of candidate materials with target properties has become a key task in materials science. Machine learning has emerged as an alternative to physics-based simulation, offering a faster and cheaper way to filter materials based on their stability and other target properties, reducing the number of candidates that reach the costly synthesis stage. Recently, Large Language Models (LLMs) have been applied to this role, but these models are parameter-heavy and computationally expensive both during training and at inference time, making them unsuitable for high-throughput tasks. This inefficiency stems from both the large over-parameterization of language models and the difficulty of framing material generation as a sequence learning problem. In this paper, we present PRISMat, a cost-effective, permutation-invariant model, which addresses these limitations. We show that PRISMat, despite taking less time for inference, is able to outperform LLMs in generating crystal slabs conditioned on critical materials' surface properties. In targeted material discovery, we achieve mean absolute errors of 0.188 eV/A$^2$ and 2.79 eV for cleavage energy and work function tasks, respectively, reducing the error of the next best model by 4$\times$.

---


### 103. [Beyond Sentiment Classification: A Generative Framework for Emotion Intensity Evaluation in Text](https://arxiv.org/abs/2605.16613)

**<font color=#1a73e8>作者：</font>** Francesco A. Fabozzi, Dasol Kim, William N. Goetzmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a novel approach to emotion modeling that shifts the focus from
identification to evaluation, addressing the limitations of discrete classification in
applied domains such as finance. By constructing a dataset of emotional intensity
scores and fine-tuning open-weight generative language models to output continuous
values from 0-100, we demonstrate a more expressive, generalizable framework for
sentiment and emotion analysis. Our findings not only outperform classification
baselines but also reveal surprising generalization capabilities and transfer effects
to related constructs such as sentiment and arousal. This work contributes to the
interdisciplinary recontextualization of NLP by introducing emotion intensity
evaluation as an alternative to classification, arguing that this shift better aligns
with the needs of domains--such as finance--where the degree of emotional content is
central to interpretation and decision-making.

---


### 104. [Learning What Evaluators Value: A Reliable Approach to Modeling Evaluator Preferences](https://arxiv.org/abs/2605.16615)

**<font color=#1a73e8>作者：</font>** Madeline Celi Kitch, Nihar B. Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many applications, human and LLM evaluators use assessments of relevant criteria to create an overall evaluation for an item or individual. For example, in admissions, committees assess candidates on attributes such as test scores, GPA, and research experience to evaluate their overall fit for the program. Another example arises in medical care where clinicians use patient reports of symptoms to consider preliminary diagnoses and assess risks. Each setting involves mapping multiple criteria to an overall evaluation -- a process that reflects the evaluator's underlying preferences. We focus on the fundamental question of learning these preferences.
Many applications of this problem make specific modeling assumptions on evaluator preferences that may be substantially violated in the real world. We make the minimal assumption that the preference function is coordinate-wise non-decreasing, which is reasonable in a large number of evaluation settings. We theoretically characterize the severity of model mismatch for many common assumptions and show that it can lead to significant issues for learning evaluator preferences and other important downstream tasks. We then present an algorithm for learning evaluators' preferences that is robust to model mismatch. We prove theoretically that our algorithm can learn any preference function without sacrificing performance when the linearity assumption holds. Evaluations of our algorithm with synthetic simulations and real-world data confirm its ability to learn preferences robustly and illustrate key aspects of LLM and human preferences.

---


### 105. [MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility](https://arxiv.org/abs/2605.16616)

**<font color=#1a73e8>作者：</font>** Sasi Kiran Gaddipati, Diyana Muhammed, Farhana Keya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous research systems capable of generating complete scientific manuscripts have advanced rapidly, yet robust and realistic evaluation frameworks have failed to keep pace. To bridge this gap, we introduce MLReplicate, an end-to-end benchmark evaluating autonomous research systems on machine learning reproducibility. The benchmark was constructed from ICML 2025 outstanding papers reformulated into standardized input specifications and evaluated across 6 state-of-the-art research systems: AI SCIENTIST-V1, AI SCIENTIST-V2, AGENT LABORATORY, CYCLERESEARCHER, AI RESEARCHER, and TINY SCIENTIST, yielding 45 generated manuscripts, with 3 failed experiments. Outputs are assessed using a dual-protocol approach that combines automated conference-style review and structured expert human evaluation, while tracking computational cost, runtime, and the amount of required human intervention. The automated conference-style review accepted 10 out of 37 valid submissions. An additional 8 submissions were desk-rejected before review for failing to meet the minimum page threshold. In contrast to automated reviews, human reviewers consistently identified methodological flaws, hallucinated experimental results, and reproducibility failures across all systems, and 59% of accepted automated reviews contained fabricated or unsupported claims. We further find that neither token budget nor computational cost predicts output quality: the cheapest system outperforms the most resource-intensive system in human evaluation, despite a 38-fold difference in input tokens. We thus demonstrate that autonomous research workflow design matters more than the scale of compute. MLReplicate exposes a substantial gap between current autonomous research systems and genuine scientific rigor, and establishes a practical, extensible evaluation framework for systematic progress toward trustworthy AI-driven scientific discovery.

---


### 106. [SCOUT: Cyclic Causal Discovery Under Soft Interventions with Unknown Targets](https://arxiv.org/abs/2605.16620)

**<font color=#1a73e8>作者：</font>** Alpar Turkoglu, Muralikrishnna G. Sethuraman, Faramarz Fekri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning causal relationships between variables from data is a fundamental research area with many applications across disciplines. Most existing causal discovery algorithms rely on the assumptions that (i) the underlying system is acyclic, (ii) the exogenous noise variables are Gaussian, and (iii) the intervention targets for the data-generating experiments are known. While these assumptions simplify the analysis, they are violated in real-life systems. Most existing methods that address these issues either assume the underlying model is linear or are constrained to operate in limited interventional settings. To that end, we propose SCOUT, a novel causal discovery framework for learning nonlinear cyclic causal relationships from soft interventional data with unknown targets. Our approach maximizes the data log-likelihood to recover the graph structure, using two normalizing-flow architectures: contractive residual flows and neural spline flows. Through experiments on synthetic and real-world data, we show that SCOUT outperforms state-of-the-art methods in both causal graph recovery and unknown target recovery across various interventional and noise settings.

---


### 107. [Does Weight Decay Enhance Training Stability?](https://arxiv.org/abs/2605.16622)

**<font color=#1a73e8>作者：</font>** Marius Saether, Amir Kolic, Tomaso Poggio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In modern deep learning, weight decay is often credited with "stabilizing" training dynamics, diverging from its classical role as a static regularization penalty. We investigate a fundamental question: *does weight decay stabilize training dynamics, and if so, through which mechanism?* Indeed, training stability is understood through different but related notions in the literature. We consider how weight decay affects the parameter-space dynamics and loss sharpness by analyzing its effects at the \emph{Edge of Stability} (EoS). We show that weight decay robustly slows *progressive sharpening}. Furthermore, we uncover a striking architecture-dependent phase transition. In CNNs, weight decay dampens the oscillations at the EoS, while in MLPs, increasing weight decay causes a phase transition in which the sharpness stabilizes at a threshold significantly below the theoretical $\frac{2}{\eta}$ boundary. We develop a mathematical framework that accurately models these phenomena and identify the global alignment of the parameter vector and the sharpness gradient as the mechanistic driver of the phase transition. Importantly, we show that these phenomena translate into stability in terms of search in function-space (NTK). Last, this shows that curvature thresholds obtained from convex/quadratic heuristics may not be reliable stability diagnostics under regularization.

---


### 108. [SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors](https://arxiv.org/abs/2605.16626)

**<font color=#1a73e8>作者：</font>** Elle Najt, Colin Toft, Tyler Tracy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Since autonomous coding agents generate complex behaviors at high-volume, we may want to use other LLMs to monitor actions to reduce the risk from dangerous misaligned behavior. To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g. weight exfiltration, credential theft, unmonitored rogue deployment). We find that 24 of 40 attacks are never caught by an Opus 4.6 monitor with extended thinking across 10 trials at a 1% false-positive rate, while the overall catch rate is 23%. We identify several evasion strategies such as exploiting model priors, user instruction ambiguity, and state manipulation, which facilitate creating attacks that evade frontier monitors. We also elicit stronger monitor performance using coding agents as monitors versus regular prompted monitors, and for some evasion strategies show improved catch rates with targeted monitor prompts. Our dataset and evaluation framework are available at this https URL and this https URL.

---


### 109. [SCARED-C: Corrected Camera Poses for Endoscopic Depth Estimation](https://arxiv.org/abs/2605.16628)

**<font color=#1a73e8>作者：</font>** John J. Han, Adam Schmidt, Max Allan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The SCARED dataset is a widely used benchmark for endoscopic depth estimation, offering ground-truth 3D reconstructions captured with a structured light sensor. However, the depth maps for non-keyframe images rely on robot kinematics that introduce substantial pose errors, limiting the reliably labeled portion of the dataset to 35 keyframes. We present SCARED-C, a corrected version of the SCARED dataset that expands the number of reliable RGB-D pairs from 35 to 17,135. Our pipeline applies COLMAP, a Structure-from-Motion system, to re-estimate camera poses for all frames, followed by a scale recovery step that aligns the resulting reconstructions to metric space using the ground-truth keyframe depth maps. We validate the corrected poses through (1) stereo disparity evaluation and (2) monocular depth estimation experiments. The corrected dataset and code are publicly released to the community.

---


### 110. [Provably Shorter Scratchpads in Hybrid DeltaNet-Attention Decoders](https://arxiv.org/abs/2605.16640)

**<font color=#1a73e8>作者：</font>** Tomasz Steifer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the expressive power of hybrid recurrent-attention decoders, a class of architectures used in recent open-source language models such as Qwen3-Next and its successors. These models combine Gated Attention heads with recurrent Gated DeltaNet heads. Is there a formal advantage, in terms of model expressivity or efficiency, to such a hybrid architecture? We show that there is. We define parity-conditioned retrieval task and show that under constant-precision assumption, a Qwen-style hybrid of Gated DeltaNet and Gated Attention solves this task with a constant scratchpad, or equivalently $O(1)$ chain-of-thought steps. In contrast, no similar solution exists for pure Gated DeltaNet models, while pure Gated Attention requires at least a polynomial scratchpad.

---


### 111. [Examining University Students' Artificial Intelligence-Generated Content (AIGC) Verification Intention from a Protection Motivation Perspective](https://arxiv.org/abs/2605.16642)

**<font color=#1a73e8>作者：</font>** Yiran Du  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence-Generated Content (AIGC) is increasingly used by students to support learning tasks, yet its outputs may contain inaccuracies, fabricated references, bias, and unsupported claims. This study examined students' intention to verify AIGC from the perspective of Protection Motivation Theory. A cross-sectional survey was conducted with 432 students who had experience using AIGC for learning. Structural equation modelling (SEM) was used to test the hypothesised relationships among threat appraisal, coping appraisal, protection motivation, and AIGC verification intention, while fuzzy-set qualitative comparative analysis (fsQCA) was applied to identify configurational pathways leading to high verification intention. The SEM results showed that protection motivation positively predicted AIGC verification intention. Perceived severity, perceived vulnerability, response efficacy, and self-efficacy positively influenced protection motivation, whereas maladaptive rewards and response cost had negative effects. The fsQCA results further revealed three configurations leading to high verification intention, with protection motivation appearing as a core condition across all pathways. These findings suggest that students' willingness to verify AIGC depends on both risk recognition and perceived coping capacity. The study extends Protection Motivation Theory to the context of AIGC verification and provides implications for promoting critical, responsible, and academically appropriate use of generative AI in higher education.

---


### 112. [Public-Decay Homomorphic State Space Models for Private Sequence Inference](https://arxiv.org/abs/2605.16647)

**<font color=#1a73e8>作者：</font>** Luis Brito  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) changes sequence-model design because rotations, encrypted products, ciphertext materialization, multiplicative depth, and bootstrapping pressure can dominate ordinary neural-network costs. This paper presents public-decay homomorphic state space models (HSSMs), recurrent/state-space blocks whose carried state is updated through ciphertext-plaintext public decay while ciphertext-ciphertext multiplication remains on a local write path. The design keeps a fixed encrypted state across the sequence. The evaluated workflow separates client-side tokenization, frozen fastText lookup, projection, clipping, encryption, decryption, and thresholding from server-side encrypted evaluation over bounded projected features. On full Rotten Tomatoes and SST-2 validation splits, the encrypted HSSM path exactly matches plaintext classifications and reaches 0.7505 and 0.7420 accuracy. Against HE-friendly polynomial attention on the same fastText workloads, HSSM matches or exceeds full-sequence task quality while running about 5x faster. Paired L40S operation-level rows show 1.34-1.62x lower latency than cached final-token polynomial attention, 30-258x lower latency than full-sequence polynomial attention, and lower logical encrypted-state footprint. A T = 16/32 comparator with encrypted public-linear input and Q/K/V projections shows projected HSSM succeeding under depth 8/ring 32768, while projected attention succeeds under depth 10/ring 65536. A matched T = 8 OpenFHE/FIDESlib trace finishes at final level 3 and noise-scale degree 2 on both backends. These results make public-decay carry a practical FHE co-design lever for encrypted sequence inference from bounded projected features.

---


### 113. [Psychological Mechanisms of Generative AI Discontinuance Intention among Chinese K-12 Teachers](https://arxiv.org/abs/2605.16648)

**<font color=#1a73e8>作者：</font>** Yiran Du, Qian Chen, Huimin He  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines the psychological mechanisms underlying Chinese K-12 teachers' discontinuance intention toward generative AI. Drawing on the Cognition-Affect-Conation framework, the study investigates how cognitive evaluations of generative AI shape affective responses and subsequently influence behavioural intention. Survey data from 256 Chinese K-12 teachers were analysed using structural equation modelling and fuzzy-set qualitative comparative analysis. The results showed that privacy concern, algorithmic opacity, and information hallucination increased AI anxiety, which in turn strengthened discontinuance intention. Conversely, perceived intelligence, perceived personalisation, and perceived interactivity enhanced satisfaction, which reduced discontinuance intention. The configurational analysis further identified multiple pathways leading to high discontinuance intention, highlighting the combined roles of technological risks, AI anxiety, weak affordance perceptions, and low satisfaction. These findings extend research on post-adoption generative AI use in education and suggest that sustainable integration requires both reducing technological uncertainty and enhancing teachers' positive user experiences.

---


### 114. [AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling](https://arxiv.org/abs/2605.16649)

**<font color=#1a73e8>作者：</font>** Ziyang Mai, Yuyao Zhang, Yu-Wing Tai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based video generators have achieved remarkable visual fidelity and prompt controllability, yet scaling them to ultra-high-resolution (UHR) long videos remains prohibitively expensive. The difficulty is especially pronounced for long single-shot generation where a continuous scene must preserve global temporal coherence, and fine-grained spatial details without relying on clip transitions or autoregressive shot stitching. In this work, we revisit this challenge from the perspective of decoupled modeling. We argue that existing video diffusion models already encode strong local visual priors, while the main bottleneck lies in efficiently extending global spatiotemporal modeling as resolution and duration increase. Based on this insight, we propose AtlaVid, a decoupled global-local framework for efficient UHR long video generation. AtlaVid first generates a low-resolution and low-FPS global semantic proxy via temporally scaled RoPE, thereby extending the temporal horizon without increasing the training token count. Guided by this proxy, a high-resolution detail branch performs joint denoising with hierarchical locality-preserving attention. Reordered spatiotemporal windows preserve geometric locality and asymmetric global-local attention injects aligned semantic guidance and preserves the model's pretrained ability. This design enables resolution-agnostic training: the model is trained only at 720P with lightweight LoRA adaptation, yet generalizes directly to 4K and beyond for longer (>10s) video synthesis. Experiments show that AtlaVid substantially improves the efficiency of ultra-high-resolution long video generation, achieving high-quality UHR long video generation with 60.9x speed up and significantly less training cost and even better performance than native 4K video generators.

---


### 115. [SKG-Eval: Stateful Evaluation of Multi-Turn Dialogue via Incremental Semantic Knowledge Graphs](https://arxiv.org/abs/2605.16650)

**<font color=#1a73e8>作者：</font>** Avijit Shil, Suman Samui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating multi-turn dialogue systems remains challenging because response quality depends not only on the current prompt, but also on previously established entities, claims, and conversational commitments. Existing automatic evaluators, including LLM-as-a-judge frameworks and embedding-based metrics, largely rely on flat or turn-isolated representations, making them less effective at detecting long-range issues such as contradiction, topic drift, and entity inconsistency. To address this, we propose SKG-Eval, a quasi-deterministic and interpretable framework that models dialogue as an evolving Semantic Knowledge Graph (SKG) of entities, relations, and commitments across turns. The framework incrementally updates the graph through structured triple extraction and computes three complementary signals: (i) local relevance, measuring alignment with the current prompt and optional reference; (ii) historical consistency, evaluating how newly introduced information connects to prior conversational context using graph-based and embedding-driven signals; and (iii) logical coherence, assessed by a geometric contradiction engine that detects cross-turn conflicts without relying on NLI models or LLM judges. These signals are adaptively fused and aggregated into a length-invariant session score via recency-weighted trend analysis. Across multiple benchmarks, SKG-Eval achieves higher correlation with human judgments and substantially improves detection of long-range inconsistencies in extended conversations. In addition, the framework produces explicit contradiction certificates and deterministic scores for fixed inputs, enabling reproducible and auditable evaluation. Overall, our results suggest that structured externalized state tracking through semantic knowledge graphs provides a scalable alternative to implicit reasoning in LLM-based dialogue evaluators.

---


### 116. [Can AI Reduce Acculturative Stress? Exploring the Role of AI-Mediated Speaking Practice in Chinese International Students' Perceived Language Insufficiency, Social Isolation, and Academic Pressure](https://arxiv.org/abs/2605.16653)

**<font color=#1a73e8>作者：</font>** Bin Zou, Yijia Yuan, Chenghao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examined whether AI-mediated speaking practice can reduce acculturative stress among Chinese international students in UK universities. Using a sequential explanatory mixed-methods design, 126 participants were randomly assigned to an experimental group, which completed a four-week intervention using EAP Talk, an AI-assisted English for Academic Purposes speaking platform offering role play, scenario-based practice, free talk, and automated feedback, or a control group, which continued usual academic and English-learning activities. Pre- and post-test questionnaires measured perceived language insufficiency, social isolation, and academic pressure, while semi-structured interviews with 20 experimental-group participants contextualised the quantitative findings. Linear mixed-effects models showed that the experimental group experienced significantly greater reductions than the control group across all three outcomes, with the strongest effect on perceived language insufficiency. Interview findings suggested that EAP Talk supported low-stakes rehearsal, communicative confidence, academic speaking preparation, and greater willingness to initiate social interaction. However, participants also noted that AI-mediated practice could not fully reproduce authentic human interaction, disciplinary feedback, or broader institutional support. The findings suggest that AI-mediated speaking practice can function as a supplementary scaffold for reducing communication-related dimensions of acculturative stress, but should be integrated with peer interaction, teacher feedback, and wider support services.

---


### 117. [A Scalable Tool for Measuring Manner and Result Verbs in Developmental Language Research](https://arxiv.org/abs/2605.16654)

**<font color=#1a73e8>作者：</font>** Divyesh Pratap Singh, Dakshesh Gusain, Federica Bulgarelli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Manner and result verbs encode different aspects of event structure and have been discussed in developmental work as a potentially informative distinction for studying early verb learning. However, this distinction remains difficult to measure at scale because large annotated resources for manner and result classification are not currently available. We present a computational approach for identifying manner and result verbs in sentence context. Using linguistically informed prompts, we generate sentence-level annotations with large language models over data drawn from MASC and InterCorp, extending coverage from previously annotated portions of VerbNet to 436 classes. We then train a RoBERTa-based classifier on these annotations and evaluate it on three held-out gold-standard datasets, including previously annotated items and a new expert-annotated set. Across these evaluations, the model shows promising performance, with average accuracy up to 89.6%. We present this work as a scalable measurement tool that can support future research on verb semantics in developmental and other language datasets, while noting that further validation is needed for borderline cases, mixed manner/result verbs, and downstream developmental applications.

---


### 118. [Read This Paper to Get $50 Million:* An Analysis of Mobile Messaging Scams Using Reddit Data](https://arxiv.org/abs/2605.16656)

**<font color=#1a73e8>作者：</font>** Allison Lu, Bernardo B. P. Medeiros, Kevin R. B. Butler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile messaging scams--fraudulent messages delivered over SMS and other mobile applications--have become a persistent and evolving security threat, yet the attributes underlying these campaigns remain unclear. This study seeks to address this gap by examining trends in mobile messaging scams and testing the effectiveness of commercial and open-source off-the-shelf detection tools. We characterize mobile messaging scam operations, focusing on how phone numbers, URLs, and text content are used across campaigns. To achieve this objective, we collect and measure a dataset of 175,430 user-reported mobile messaging scams from Reddit between June 2020 and December 2025. While reply-based scams constitute only 50% of our dataset, their compound annual growth rate (99.98%) is nearly twice that of click-based scams (57.29%). Critically, reply-based scams also show the lowest detector performance--despite identifiable similarities in text content and phone number origin within categories--indicating that current off-the-shelf tools are ineffective. These results suggest that further development of detectors is necessary to defend against this rapidly changing ecosystem. By examining a range of message attributes, this work provides new insights into mobile messaging scams, informing the design of more targeted and robust detection methods.

---


### 119. [Beyond One-Size-Fits-All: User Strategies for Simplification Technique and Level Selection in Responsive Line Charts](https://arxiv.org/abs/2605.16661)

**<font color=#1a73e8>作者：</font>** Rifat Ara Proma, Paul Rosen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simplifying line charts for responsive displays typically applies a single algorithm uniformly across devices, despite the availability of multiple techniques that preserve different signal characteristics (e.g., peaks, trends, periodicity). We investigate whether users benefit from algorithmic choice when adapting charts across screen sizes. In a within-subjects study (N=30), participants simplified nine datasets under three conditions: single pre-assigned technique (C1), multiple techniques (C2), and multiple techniques with manual point selection (C3), each with control over simplification level. We found that users adapted technique selections across datasets rather than devices, leveraging dataset-level strategies rather than per-device optimization. Additionally, interaction complexity did not always increase engagement uniformly, suggesting that responsive simplification tools should balance algorithmic flexibility with progressive disclosure and strong defaults. Supplemental materials are available at this https URL.

---


### 120. [GraViti: Graph-Level Variational Autoencoders with Relaxed Permutation Invariance](https://arxiv.org/abs/2605.16668)

**<font color=#1a73e8>作者：</font>** Roman Bresson, Konstantinos Divriotis, Johannes F. Lutzeyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce GraViti, a transformer-based graph-level variational autoencoder that maps entire graphs to compact latent vectors. This design produces a true graph-level latent space that supports smooth interpolation, property-guided search, and other downstream tasks beyond the constraints of node-level embeddings. On molecular benchmarks, GraViti learns to decode valid samples that follow the chemical constraints present in the training data, showing that the model recovers domain rules directly from graph-level representations. We also show that, in domains where a reliable canonical node ordering exists such as molecules or bayesian networks, enforcing permutation invariance can prove detrimental for consistent reconstruction. GraViti achieves state-of-the-art reconstruction accuracy on large datasets, and provides solid generative performance. Its single-step decoding offers a lightweight alternative to more complex generation pipelines while maintaining practical sample quality.

---


### 121. [Sustainable Intelligence for the Wild: Democratizing Ecological Monitoring via Knowledge-Adaptive Edge Expert Agents](https://arxiv.org/abs/2605.16671)

**<font color=#1a73e8>作者：</font>** Jiaxing Li, Hao Fang, Chi Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid biodiversity loss underscore the urgency of effective monitoring, yet manual surveys remain resource-intensive. While on-device AI offers a scalable alternative, its performance in the wild is often challenged by environmental variability. Current methods rely heavily on cloud resource, which requires continuous uploading of field data for model retraining. This approach is unsuitable for remote deployments because it consumes limited power and network connectivity. To address these constraints, this research proposes a shift from model adaptation to knowledge adaptation. We introduce an architecture that separates visual perception from reasoning, combining a visual encoder with a dynamic knowledge base. We uses an explicit knowledge base to replace implicitly encoding expert knowledge into model parameters. This method also supports knowledge sustainability by preserving expert insights in a structured form. Through cross-disciplinary collaboration with biologists and Indigenous communities, this work advances ethical AI co-development, fostering responsible and culturally informed ecosystem management.

---


### 122. [Multi-Object Tracking Consistently Improves Wildlife Inference](https://arxiv.org/abs/2605.16672)

**<font color=#1a73e8>作者：</font>** Mufhumudzi Muthivhi, Jiahao Huo, Fredrik Gustafsson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera traps have become a common tool for wildlife monitoring efforts in ecological research and biodiversity conservation. Wildlife classification models have benefited from the increase in wildlife visual data. These models reach high levels of accuracy on curated, high-quality datasets. However, their performance remains sensitive to real-world environmental constraints. They often produce inconsistent predictions when performing inference on temporally coherent sequences. The predicted label for a single individual shifts rapidly between frames. This study exploits the temporal nature of camera-trap data to augment inferred predictions from a wildlife classification model. Specifically, we adopt several standard Multi-Object Tracking (MOT) models to link detections across consecutive frames. The curated trajectories are used to fuse the softmax class probabilities. The fused probability score produces a single consensus class label estimate that overrides misclassifications caused by noise. The analysis of the experimental results shows that our proposed strategy improves over a standalone classifier over all datasets and for each metric. Specifically, the best-performing MOT models gain a weighted F1-Score of 5.1%, 3.1% and 2.0% over the classifier across three MOT datasets.

---


### 123. [Navigating Transitions: Envisioning Conversational User Interfaces to Support International Students](https://arxiv.org/abs/2605.16677)

**<font color=#1a73e8>作者：</font>** Yuhui Xu, Isabel Blijenburg, Bhakti Moghe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> International students face struggles when adapting to the host country. They are more susceptible to mental health problems than domestic students. While Conversational User Interfaces (CUIs) are increasingly researched and implemented, research on how they may help international university students is still scarce. Thus, we conducted participatory design workshops with international students who shared their perspectives and struggles of studying abroad, in which they also envisioned CUIs as aids to support their transitions. Participants proposed features of a CUI to address uncertainty, loneliness, and misunderstandings of cultural differences. Our paper reveals international students' needs and provides design implications for CUIs to support their well-being.

---


### 124. [CHI-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?](https://arxiv.org/abs/2605.16679)

**<font color=#1a73e8>作者：</font>** Haolin Chen, Deon Metelski, Leon Qi 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end automation of realistic healthcare operations stresses three capabilities underrepresented in current benchmarks: policy density, decisions must be grounded in a large library of medical, insurance, and operational rules; Multi-role composition: a single task requires the agent to play multiple roles with handoffs; and multilateral interaction: intermediate workflow steps are multi-turn dialogs, such as peer-to-peer review and patient outreach. We introduce $\chi$-Bench, a benchmark of long-horizon healthcare workflows across three domains: provider prior authorization, payer utilization management, and care management. Each task hands the agent a clinical case in a high-fidelity simulator of 20 healthcare apps exposed via 87 MCP tools, which it must drive to a terminal status through tool calls and writing the role's artifacts, guided by a 1,290+ document managed-care operations handbook skill. Across 30 agent harness/models configurations, the best agent resolves only 28.0% of tasks, no agent clears 20% on strict pass^3, and executing all tasks in a single session slumps the performance to 3.8%. These results raise the hypothesis that similar gaps are likely to surface in other policy-dense, role-composed, irreversible enterprise domains.

---


### 125. [Identify Then Project: Contrastive Learning of Latent Dynamics from Partial Observations with Port-Hamiltonian Structure](https://arxiv.org/abs/2605.16682)

**<font color=#1a73e8>作者：</font>** Peilun Li, Kaiyuan Tan, Daniel Moyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying latent state representations and dynamics is essential when direct modeling in observation space is infeasible, particularly under partial and high-dimensional observations. In such settings, representation learning and physics-aware modeling are inherently coupled. We study this problem for latent port-Hamiltonian systems, a structured class encompassing both conservative and dissipative dynamics. We propose a two-stage identify-then-project framework. First, a contrastive teacher learns continuous-time latent dynamics from partial observations. Then, a student projects the identified teacher representation and dynamics onto a port-Hamiltonian submanifold via a learned affine chart, yielding a physically consistent realization. As a conceptual counterfactual, we also consider a single-stage variant that jointly learns latent identification and port-Hamiltonian structure, but find it to be less reliable, motivating the proposed two-stage teacher-student framework. We show theoretically that affine projection is the natural bridge between the affine gauge of contrastive latent identification and the port-Hamiltonian systems. Empirically, we demonstrate that the proposed two-stage approach preserves the teacher's dynamics while enforcing physical structure, and performs more reliably than the single-stage alternative, particularly in dissipative regimes and high-dimensional visual settings.

---


### 126. [EfficientTDMPC: Improved MPC Objectives for Sample-Efficient Continuous Control](https://arxiv.org/abs/2605.16692)

**<font color=#1a73e8>作者：</font>** Thomas Evers, Cristian Meo, Wendelin Bohmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce EfficientTDMPC, a sample-efficient model-based reinforcement learning method for continuous control built on the TD-MPC family of algorithms. Central to this family is a planner that aims to find an action sequence that maximizes the estimated return. The return is estimated using a learned model and value networks, each of which can introduce error. EfficientTDMPC proposes to reduce this error in two ways. First, it introduces an ensemble of dynamics models and averages the return estimates across those models and across different rollout depths. Second, it adds the option to apply an uncertainty penalty to the planner objective, yielding a planner that avoids actions with uncertain return estimates. It then adds practical improvements which increase buffer data freshness and reduce compute. Lastly, we find that our contributions enable EfficientTDMPC to benefit more from a higher update-to-data (UTD) ratio, further improving sample efficiency. To the best of our knowledge, in the low data regime of each benchmark, EfficientTDMPC achieves state-of-the-art (SOTA) in terms of sample efficiency on HumanoidBench-Hard and DMC hard, while matching SOTA on DMC easy.

---


### 127. [Face inpainting with Identity Preserving Latent Diffusion Models](https://arxiv.org/abs/2605.16696)

**<font color=#1a73e8>作者：</font>** João Santos, Carlos Santiago, Manuel Marques  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face inpainting techniques recover missing or occluded facial regions in a visually realistic manner, but preserving the identity in the final output remains a fundamental challenge. Identity consistency is crucial for downstream applications such as face recognition, digital forensics, and human-computer interaction, where even subtle identity distortions can significantly degrade performance or trust. Although diffusion-based generative models have recently achieved remarkable progress in image inpainting, they often struggle to faithfully retain individual-specific facial characteristics. On the other hand, existing identity-aware methods typically rely on costly fine-tuning, auxiliary supervision, or exhibit limited robustness to diverse occlusions, poses, and facial variations. To address these limitations, we propose ID-ControlNet, an identity-preserving face inpainting framework built upon latent diffusion models. Based on ControlNet architecture, our approach conditions the diffusion process on facial identity embeddings extracted from a pretrained face recognition network. This design enables reconstruction of occluded facial regions while maintaining global facial coherence and identity fidelity. Furthermore, we introduce an identity consistency and triplet loss training strategy that explicitly enforces alignment between the generated face and the target identity representation. Extensive experiments on CelebA-HQ, FFHQ, and on a new E-Mask dataset demonstrate that ID-ControlNet significantly improves identity preservation over standard diffusion-based inpainting methods, achieving performance comparable to SOTA identity-aware approaches.

---


### 128. [Your SaaS Is an Insurance Product: A Modeling Framework](https://arxiv.org/abs/2605.16699)

**<font color=#1a73e8>作者：</font>** Caio Gomes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Capped-usage SaaS products -- LLM subscriptions such as Claude Code and ChatGPT, cloud platforms such as Vercel and Cloudflare Workers, corporate benefit platforms, identity-verification services with liability transfer -- share a structural signature with insurance products: a fixed premium decoupled from realized consumption, stochastic per-user demand with heavy-tailed severity, a non-fungible cap that resets on a fixed schedule, and a portfolio-level exposure that requires reserve adequacy under tail risk. We argue that this is not an analogy. It is the same operational problem actuarial science has been tooled for decades to address, restated with new dependent variables (tokens, bandwidth bytes, function-invocations, gym check-ins) in place of medical claims. This paper proposes a modeling framework for capped-usage SaaS pricing built from frequency-severity decomposition, premium calculation principles, and Monte Carlo reserve adequacy. We map the framework to publicly observable subscription tiers in two domains (LLM services and cloud platforms), ground it in canonical health-insurance economics (Arrow 1963; Pauly 1968; Manning et al. 1987; Brot-Goldberg et al. 2017), and demonstrate divergence from traditional unit economics through a worked example. The contribution is operational rather than theoretical: not a new theorem, but vocabulary and tools currently absent from cs.LG/stat.ML practice.

---


### 129. [On-Device Interpretable Tsetlin Machine-Based Intrusion Detection for Secure IoMT](https://arxiv.org/abs/2605.16707)

**<font color=#1a73e8>作者：</font>** Rahul Jaiswal, Per-Arne Andersen, Linga Reddy Cenkeramaddi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of digital health technologies is redefining healthcare services worldwide. The integration of wireless communication and Internet-enabled medical devices within Internet of Medical Things (IoMT) networks enables continuous, real-time patient monitoring. However, this increased connectivity raises cybersecurity and patient safety risks due to increasingly sophisticated cyberattacks. This paper proposes a novel on-device, interpretable Tsetlin Machine (TM)-based Intrusion Detection System (IDS) to identify various phases of cyberattacks in IoMT environments. The TM is a rule-driven and transparent machine learning (ML) approach that represents attack patterns using propositional logic. Extensive evaluations on the MedSec-25 dataset, encompassing various phases of realistic cyberattacks, show that the proposed model outperforms ML models and state-of-the-art methods, attaining a classification performance of 97.83\%. Moreover, the proposed model offers explicit explanations of its decisions to enhance transparency using feature-level contributions, class-wise vote scores, and clause activation heatmaps. Edge deployment (Raspberry Pi) further supports real-time on-device inference and intrusion detection. The combination of interpretability and high performance makes the proposed model well-suited for IoMT healthcare, where trust, reliability, safety, and timely decision-making are critical.

---


### 130. [Isolating Nonlinear Independent Sources in fMRI with $β$-TCVAE Models](https://arxiv.org/abs/2605.16708)

**<font color=#1a73e8>作者：</font>** Qiang Li, Shujian Yu, Jesus Malo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning meaningful latent representations from nonlinear fMRI data remains a fundamental challenge in neuroimaging analysis. Traditional independent component analysis, widely used due to its ability to estimate interpretable functional brain networks, relies on a linear mixing assumption for latent sources, limiting its ability to capture the inherently nonlinear and complex organization of brain dynamics. More recently, deep representation learning methods have emerged as promising alternatives for modeling nonlinear latent structure. However, many of these approaches have been evaluated primarily on simulated datasets or natural image benchmarks, with comparatively limited validation on real-world neuroimaging data such as fMRI. In this work, we are motivated by the $\beta$-TCVAE (Total Correlation Variational Autoencoder), a refinement of the $\beta$-VAE framework for learning latent representations without introducing additional hyperparameters during training. We adapt and modify this model to fMRI data for nonlinear source disentanglement, aiming to separate mixed spatial and temporal brain signals into interpretable components. We show that the $\beta$-TCVAE framework can recover meaningful nonlinear spatial components with biological relevance, including well-established intrinsic connectivity networks such as the default mode network. Furthermore, we evaluate the learned representations using functional network connectivity, showing that the latent structure captures coherent and interpretable brain organization patterns. This study provides a pilot investigation that bridges nonlinear representation learning and fMRI analysis.

---


### 131. [Recall Isn't Enough: Bounding Commitments in Personalized Language Systems](https://arxiv.org/abs/2605.16712)

**<font color=#1a73e8>作者：</font>** Rui Tang, Yichi Zhang, Xi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context and memory systems usually treat personalization as a recall problem. In practice, many failures occur later, when a system commits: it turns noisy hints into hard constraints, drops rare witnesses, forgets downstream obligations, or answers despite infeasibility. We introduce Contract-Bounded Evidence Activation (CBEA) with Lexicographic Commitment Validation (LCV). CBEA activates a bounded evidence set using typed coverage, tail witnesses, and consequence debt; LCV validates structured commitments before prose and routes infeasible states to repair, abstention, or recontract. Across 360 fixtures and three generation backends, CBEA+LCV reaches zero failures within validator scope at 0.49-0.60 availability over attempted runs. Raw and long-context baselines with the same LCV gate reach zero only at 0.003-0.092. A shadow oracle diagnostic marks the limit: CBEA+LCV recalls 0.012 of uncompiled visible facts, while raw recalls 0.53. The result is a bounded operating point: explicit commitment control and 74-75% lower median input payload, not universal memory dominance.

---


### 132. [MAVEN A Multi-Agent Framework for Multicultural Text-to-Video Generation](https://arxiv.org/abs/2605.16716)

**<font color=#1a73e8>作者：</font>** Shuowei Li, Yuming Zhao, Parth Bhalerao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) generation has rapidly progressed in visual fidelity, yet its ability to faithfully represent multiple cultures within a single prompt remains underexplored. We introduce MAVEN, a multi-agent prompt refinement framework designed to improve cultural fidelity in both mono-cultural and cross-cultural T2V generation. MAVEN decomposes prompts into person, action, and location dimensions, handled by specialized agents operating in parallel or sequentially. To support systematic evaluation, we contribute a new benchmark of 243 culturally grounded prompts and 972 corresponding videos, spanning three cultures (Chinese, American, Romanian), three action categories, and both mono-cultural and cross-cultural scenarios. Evaluations combining CLIP-based metrics, VLM-as-judge assessments, and videoquality measures show that multi-agent refinement, particularly parallel specialization, significantly improves cultural relevance while preserving visual quality and temporal consistency. The dataset and code are available athttps://github.com/AIM-SCU/CRAFT

---


### 133. [Compositional Adversarial Training for Robust Visual Watermarking](https://arxiv.org/abs/2605.16720)

**<font color=#1a73e8>作者：</font>** Anirudh Satheesh, Michael-Andrei Panaitescu-Liess, Andrew Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust watermarking is typically trained with random post-processing augmentation, but random sampling under-covers the combinatorial space of realistic attack pipelines and rarely encounters the rare compositions that actually break detection. This leads to unstable training and poor sample efficiency. We instead formulate watermark robustness as a min-max problem over a structured space of compositional transformations. We propose Compositional Adversarial Training (CAT), a plug-in framework that learns a sequential differentiable adversary that observes the current watermarked image and selects an attack family at each step to maximally disrupt message recovery. CAT combines a straight-through Gumbel-Softmax attack selection with entropy regularization, allowing the backward pass to be end-to-end differentiable and aggregate gradient information across attack families, yielding faster, smoother convergence without collapsing to a single attack mode. We evaluate CAT on post-generation watermarks VideoSeal 0.0, VideoSeal 1.0, and PixelSeal and in-generation WMAR under both single-step and two-step attack suites, on in-distribution and multiple out-of-distribution image and video benchmarks. CAT consistently outperforms random-augmentation baselines trained with the same augmentation budget, with the largest gains on hard composed attacks and OOD evaluations; improving overall watermark capacity by up to $63.5\%$ in the single-step attack setting and $13.0\%$ in the compositional setting. In the autoregressive setting, CAT improves the TPR@FPR$=1\%$ by $12\%$ on average on difficult geometric transformations. These results show that robust visual watermarking benefits from training against adaptive compositional adversaries rather than independent random corruptions.

---


### 134. [A Global-Local Graph Attention Network for Traffic Forecasting](https://arxiv.org/abs/2605.16726)

**<font color=#1a73e8>作者：</font>** Tianchi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting is a significant part of intelligent transportation systems. One of the critical challenges of traffic forecasting is to find spatio-temporal correlations. In recent years, graph convolutional networks and graph attention networks have replaced traditional statistical models to predict future traffic. However, it is complicated for both of them to allow vertices to have far different characters. To address this, we propose the Global-Local Graph Attention Network (GLGAT) with pairwise encoding and the event-based adjacency matrix. The GLGAT allows vertices to have a global attention matrix set for the whole graph and assigns local attention matrix sets to each vertex. Experiments on two real-world traffic datasets show that GLGAT can effectively capture spatio-temporal correlations and has competitive performance against other state-of-the-art baselines.

---


### 135. [Body-Grounded Perspective Formation and Conative Attunement in Artificial Agents](https://arxiv.org/abs/2605.16728)

**<font color=#1a73e8>作者：</font>** Hongju Pae  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes a minimal architecture for body-grounded perspective formation in artificial agents. Extending prior work, the model introduces an interoceptive viability signal, a Fisher-style metric over fused exteroceptive-interoceptive states, and a conative alignment mechanism linking bodily tendency to action readiness. In a reward-free gridworld, conation converts learned bodily tendency into stable body-directed behavior, while body-to-perspective routing allows bodily perturbations to leave a recoverable geometric residue in the perspective latent. This study shows how minimal structural conditions for artificial subjectivity can be operationalized in the phenomenological sense, through the embodied organization of how a world is given to an agent.

---


### 136. [DiRotQ: Rotation-Aware Quantization for 4-bit Diffusion Transformers](https://arxiv.org/abs/2605.16732)

**<font color=#1a73e8>作者：</font>** Sayeh Sharify, Mahsa Salmani, Hesham Mostafa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) achieve state-of-the-art image generation quality but incur substantial memory and computational costs at inference. While aggressive Post-Training Quantization (PTQ) to 4-bit precision offers significant efficiency gains, it typically results in severe quality degradation. Existing approaches, including smoothing-based methods, mixed-precision schemes, rotation techniques, and low-rank residual methods, partially mitigate this issue but still leave a noticeable gap to FP16/BF16 performance. In this work, we introduce DiRotQ, a W4A4 PTQ framework that mitigates this degradation through rotation-aware activation quantization. DiRotQ identifies a low-rank subspace capturing dominant activation variance via Principal Component Analysis (PCA), preserving coefficients in this subspace at higher precision while quantizing the remaining components to 4-bit. Activations are rotated into the PCA basis at inference time using calibration-derived orthogonal transformations, while the inverse rotation is fused into the layer weights offline. Combined with GPTQ-based weight quantization, DiRotQ achieves an FID (lower is better) of 15.9 and PSNR (higher is better) of 19.1 dB on PixArt-{\Sigma} over the MJHQ-30K dataset, outperforming the prior state-of-the-art SVDQuant (FID 18.9, PSNR 17.6) under the same INT W4A4 setting. Beyond standard metrics, we introduce a VLM-as-a-Judge evaluation protocol for diffusion model quantization, the first such evaluation in this setting, providing a more holistic assessment of perceptual quality and prompt alignment under aggressive compression. On the systems side, we implement a Triton-based custom kernel to enable efficient end-to-end inference, reducing memory usage of the 12B FLUX.1-dev model by 2.1x and delivering 2.3x speedup over the BF16 baseline, on a 24 GB RTX 4090 GPU.

---


### 137. [CAB: Accelerating Flow and Diffusion Sampling via Rectification and Corrected Adams-Bashforth](https://arxiv.org/abs/2605.16736)

**<font color=#1a73e8>作者：</font>** Anuska Roy, Pravin Nair  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow and diffusion models achieve high-fidelity, high-resolution image synthesis, but often require many function evaluations (NFEs) at sampling time. Existing acceleration methods either require additional training through distillation or rely on training-free high-order solvers, and both can degrade sample quality at low NFE budgets. We propose CAB (Corrected Adams-Bashforth), a training-free sampler that accelerates both flow and diffusion models. CAB first transforms the sampling dynamics to a common rectified coordinate system, and then applies a multistep Adams-Bashforth predictor augmented with a simple correction term based on past velocity evaluations and therefore incurs no additional NFEs. The resulting method is simple, has the same algorithmic form across model classes, and has at least third-order local truncation error and second-order global error. Experiments on pretrained flow and diffusion models, including class-conditional and large-scale text-to-image benchmarks, show that CAB improves quality-NFE trade-offs in the low-step regime of 6-20 NFEs. It also remains competitive with strong training-free samplers at higher step counts across most tested models. The official implementation is available at this https URL.

---


### 138. [EmoMind: Decoding Affective Captions from Human Brain fMRI](https://arxiv.org/abs/2605.16739)

**<font color=#1a73e8>作者：</font>** Bilal A. Mohammed, Lin Gu, Ruogo Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding visual experience from brain activity has advanced substantially, but cur- rent brain-to-text systems largely recover semantic content while discarding affect. Additionally, language models can generate emotional text when prompted with categorical labels, but such labels collapse rich inter-subject variability into coarse discrete bins. We present EmoMind, the first end-to-end pipeline for decoding affective captions directly from fMRI signals. EmoMind first retrieves a semanti- cally grounded neutral scene description from brain-decoded visual features, then rewrites it using a continuous 34-dimensional emotion vector decoded from the same fMRI recording. To control the balance between content preservation and affective expression, we train the rewriter with classifier-free guidance against an identity-preserving null branch, enabling smooth interpolation between semantic fidelity and affective expressivity. We evaluate affective caption generation with a three-axis validation framework spanning subject-specificity, structural geometry, and causal control. We further augment this framework with a synthetic-brain substitution test that probes robustness to the measurement apparatus, and we benchmark each axis against GPT-4 prompted with brain-decoded top-5 emotion labels as a strong discrete baseline. Across two independent emotion fMRI datasets, EmoMind significantly outperforms label-prompted GPT-4 on all three axes, with the largest gains on metrics that require person-specific affective structure rather than population-level emotion aggregation. These results establish continuous brain-decoded affect as a viable control signal for individualized affective cap- tion generation and open new directions for studying individual affective brain organisation.

---


### 139. [Propagation of Chaos in Contextual Flow Maps](https://arxiv.org/abs/2605.16747)

**<font color=#1a73e8>作者：</font>** Shi Chen, Zhengjiang Lin, Kaizhao Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a quantitative statistical theory of transformers in the large-context regime by adopting the abstraction of contextual flow maps (CFMs): dynamical systems that evolve a distinguished token in the presence of a contextual measure across a stack of attention blocks. Within this framework, the finite-context model approximates an idealized infinite-context system in which the contextual measure is replaced by its underlying population, so that the context length $n$ becomes a statistical resource. Exploiting the McKean--Vlasov structure of the dynamics and the classical machinery of propagation of chaos, we establish a forward bound controlling the deviation between the finite- and infinite-context CFMs uniformly along depth, and a backward bound controlling the deviation between the corresponding training trajectories uniformly across iterations of online gradient descent. Both bounds achieve the optimal Wasserstein rate $n^{-1/d}$ for general CFMs and parametric rate $n^{-1/2}$ for a restricted class of CFMs that includes transformers as a special case. The analysis rests on a new Eulerian adjoint formulation of the loss gradient and stability estimates for the resulting forward--adjoint system, both of which may be of independent interest.

---


### 140. [Learning Unbiased Permutations via Flow Matching](https://arxiv.org/abs/2605.16755)

**<font color=#1a73e8>作者：</font>** Yimeng Min, Carla P. Gomes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning permutations is fundamental to sorting, ranking, and matching, but existing differentiable methods based on entropy-regularized Sinkhorn produce a single softened solution and collapse under ambiguity. We present PermFlow, a conditional flow matching framework that operates directly on the affine subspace of matrices with unit row and column sums. A closed-form tangent-space projector preserves these constraints exactly along every trajectory, by construction rather than through iterative correction, and a nearest-target coupling routes distinct noisy initializations toward distinct valid permutations. The result is a model that captures multimodal permutation distributions rather than collapsing them to a single mode. On a visual sorting task with blended-digit ambiguity and a symmetric linear assignment problem, PermFlow achieves high accuracy on unambiguous inputs and recovers both valid permutations under ambiguity, where Sinkhorn-based baselines structurally fail.

---


### 141. [NeuroMAS: Multi-Agent Systems as Neural Networks with Joint Reinforcement Learning](https://arxiv.org/abs/2605.16757)

**<font color=#1a73e8>作者：</font>** Haoran Lu, Luyang Fang, Wenxuan Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent language systems are often built as hand-designed workflows, where agents are assigned semantic roles and communication protocols are specified in advance. We propose NeuroMAS, a method that first treats a multi-agent language system as a trainable and scalable neural-network-like architecture with LLM agents as nodes and intermediate textual signals as edges. In NeuroMAS, agent nodes are role-free but structure-aware: the topology only determines how information can flow in general, while reinforcement learning training determines how nodes communicate, specialize, and coordinate. This formulation shifts multi-agent design from workflow engineering toward architecture design, where depth, width, connectivity, and growth protocol become scalable sources of capability. Further, we provide a theoretical perspective showing why such modular textual computation is more parameter-efficient when tasks admit hierarchical decompositions. Experiments show that NeuroMAS improves significantly over both inference-time and trained multi-agent baselines. We further find that organizational scaling is path-dependent: larger systems can be challenging to train from scratch, but become feasible when grown progressively from smaller trained systems. These results suggest that learned neural multi-agent systems are a promising scaling axis for LLMs.

---


### 142. [Synthetic Aperture Radar Image Change Detection Based on Global Dynamic Context-Aware Network](https://arxiv.org/abs/2605.16764)

**<font color=#1a73e8>作者：</font>** Baogui Huan, Chuanzheng Gong, Dezhong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) have been extensively and successfully applied to the task of synthetic aperture radar (SAR) image change detection. However, conventional convolutional layers are inherently limited by their local receptive fields, which mainly capture spatially localized patterns while neglecting the global context that is often crucial for accurately distinguishing subtle or large-scale changes in SAR imagery. To address these limitations, we propose a novel Global Dynamic Context-Aware Network (GDNet) specifically tailored for SAR image change detection. At the core of our approach lies a novel global dynamic convolution module, which adaptively modulates convolution kernel weights according to the global semantic information extracted from the input features. By dynamically incorporating long-range dependencies, this mechanism enables the network to integrate both local detail and global context, thus improving its ability to detect diverse change patterns. In addition, we introduce a carefully designed two-stage Mixup strategy for model training. Unlike conventional single-stage Mixup, our two-stage design generates more diverse and informative training samples, effectively regularizing the model and yielding more stable and reliable classification results even under limited data scenarios. Extensive experiments on three SAR datasets demonstrate the superiority of the proposed GDNet compared to other state-of-the-art methods. These findings highlight the potential of global dynamic modeling and advanced data augmentation strategies for advancing SAR image interpretation. Source codes are available at \url{this https URL}.

---


### 143. [Axial-Relation Guided Fusion State Space Model for Optical-Elevation Sensing Image Segmentation](https://arxiv.org/abs/2605.16768)

**<font color=#1a73e8>作者：</font>** Feng Gao, Zhilin Jin, Yanhai Gan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of multi-source remote sensing images is a fundamental task for Earth observation applications. Existing methods often struggle with insufficient multi-scale context modeling and suboptimal cross-modal feature fusion, limiting their performance in complex high-resolution scenes. To this end, we propose Axial-Relation Guided Fusion Mamba (ARG-Mamba), a state space model-based framework for optical-elevation remote sensing image segmentation. Specifically, we introduce a Multi-Scale State Space Module to capture both fine-grained local details and global contextual dependencies with linear computational complexity. Moreover, an Axial-Relation Guided Fusion Module is designed to explicitly model global cross-modal correlations along horizontal and vertical axes, enabling efficient feature fusion between optical and elevation modalities. Extensive experiments conducted on the ISPRS Vaihingen and Potsdam datasets demonstrate that our ARG-Mamba consistently outperforms state-of-the-art methods while maintaining favorable computational efficiency. The code will be made publicly available at \url{this https URL}.

---


### 144. [CANSURF: An ASV-View Can Dataset and Benchmark for Detection and Tracking of Surface-Level Debris](https://arxiv.org/abs/2605.16774)

**<font color=#1a73e8>作者：</font>** Zaid Aljundi, Zahra F. Rahmatullah, Mostafa Elemam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface-level marine debris remains a practical bottleneck for autonomous clean-up, where small, reflective targets (e.g., aluminum cans) must be detected at distance under glare, ripples, and partial submersion. This paper presents, an ASV vision system and a new surface-can dataset. The dataset comprises ~7.3k raw images extracted from videos and annotated with bounding boxes, expanded via ten augmentation types to ~57k training/validation images spanning diverse lighting and water states. A family of detector and detector-tracker pipelines tailored to surface operations were benchmarked. Training YOLOv11 on CANSURF boosts performance 12x over generic datasets, highlighting the dataset's value. Experiments show that YOLOv11+ByteTrack yields the most stable tracks (fewer identity switches) and stronger multi-object accuracy under, while YOLOv11+SAHI increases recall on far-field cans at the cost of lower precision in full-context inputs. Given the mission profile, single-can pickup with approach and grab, YOLOv11 + SAHI proves better for detecting the maximum number of cans. No prior open dataset targets aluminum cans on water from a surface-level viewpoint; this dataset fills this gap and supports reproducible evaluation.

---


### 145. [A Holistic Method for Superquadric Fitting Using Unsupervised Clustering Analysis](https://arxiv.org/abs/2605.16779)

**<font color=#1a73e8>作者：</font>** Mingyang Zhao, Sipu Ruan, Xiaohong Jia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a novel method for fitting superquadrics to point clouds under the contamination of noise and outliers, which has many applications for shape modeling across diverse fields. Unlike prior approaches that either exclusively focus on fitting rigid or deformable superquadrics, or suffer from robustness and numerical instability issues, our method redefines the problem from a new unsupervised clustering perspective, enabling the holistic fitting of both rigid and deformable superquadrics within a unified framework. Central to our approach is a stable optimization function inspired by unsupervised clustering analysis, where we formulate the point cloud data and samples from the potential parametric surface as clustering members and centroids, respectively. Then, the clustering process with dynamic updates to centroid locations serves as a direct proxy for optimizing superquadric parameters, establishing a principled link between geometric fitting and clustering dynamics. We further derive the relationship between pairwise computations of clustering centroids and clustering members to orthogonal distances, effectively eliminating the need for the time-consuming surface sampling process. Moreover, our formulation provides closed-form analytical solutions for both the fuzzy membership degree vector and the covariance matrix, ensuring efficient iteration optimization and enabling more effective handling of geometric deformations. In addition, we provide a theoretical certificate of convergence analysis and demonstrate that the clustering-inspired fitting method can escape local minima by inherently increasing the convexity of the objective function. The implementation is publicly available at this https URL.

---


### 146. [Dynamic Deployment of Mobile Charging Trucks During Natural Disaster Evacuation: An Offline-to-Online Framework](https://arxiv.org/abs/2605.16784)

**<font color=#1a73e8>作者：</font>** Rui Ma, Zilin Bian, Kaan Ozbay  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> During large-scale evacuations, concentrated electric vehicle (EV) charging demand can overload fixed charging stations (FCSs), leading to prolonged waiting time and increased risk exposure. To address this challenge, this study proposes dynamically deploying mobile charging trucks (MCTs) to complement FCSs, and develops an Adaptive Risk-aware MCT Deployment (ARMD) framework for real-time operation. It divides the MCT deployment into two problems: risk-aware allocation of MCTs among FCSs and dynamic routing of MCTs to the assigned FCSs, and solves them under an offline-to-online paradigm. The resource allocation problem is formulated as a decentralized partially observable Markov decision process, and a multi-agent proximal policy optimization (MAPPO)-based policy is developed to coordinate multiple MCTs under decentralized observations. The policy is pre-trained offline in an evacuation simulator and adaptively refined online according to current evacuation context. For routing, a spatio-temporal travel time predictor is developed to support rolling-horizon route updates. The proposed framework is evaluated in a simulated hurricane evacuation environment built using real-world data from Hillsborough County, Florida. Experiments show that ARMD consistently outperforms offline optimization, online heuristic dispatch, and rolling-horizon optimization in reducing risk exposure. For demand perturbation scenarios, ARMD reduces average risk exposure by up to 71.1%, relative to the baseline without MCTs. In the case of fixed e-vehicle charging infrastructure or road link failures, ARMD achieves 39.3% to 60.5% reduction in average risk exposure, with its advantages becoming more pronounced as the severity of disruption increases. These results demonstrate the effectiveness and robustness of ARMD in enhancing mobile charging operations for realistic scenarios of uncertain evacuation conditions.

---


### 147. [Encoding Robust Topological Signatures for Hyperdimensional Computing](https://arxiv.org/abs/2605.16785)

**<font color=#1a73e8>作者：</font>** Arpan Kusari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional (HD) computing offers an attractive alternative to deep networks for edge learning due to its simplicity, fast prototype-based inference, and compatibility with online updates. However, standard pixel-based HD encoders are brittle: small distribution shifts such as rotation, noise, or occlusion can drastically reduce accuracy. We extract discrete topological primitives-most notably holes-from binarized shapes and pair them with rotation/translation/scale (RTS)-invariant shape signatures. Our method constructs RTS-stable descriptors for (i) the outer shape using a spatial-pyramid variant of Zernike moments and (ii) each hole using an intrinsic Fourier descriptor of its radial signature together with RTS-canonical relative geometry. Each primitive is mapped to a bipolar hypervector via randomized projection and role binding, and variable-cardinality hole sets are aggregated by permutation-invariant bundling to form a single image hypervector. To avoid over-weighting any cue, we learn nonnegative reliability weights for the Zernike and hole channels on a validation set via late fusion of cosine similarities. Experiments on MNIST and EMNIST under controlled corruptions (rotation, Gaussian noise, salt-and-pepper, cutout, zoom) show that Topology-guided HD computing substantially improves robustness compared with a naive HD baseline, maintaining high accuracy across multiple corruption families and benefiting from lightweight online training. Compared with a compact CNN trained on clean data, our method achieves competitive clean accuracy while offering markedly stronger robustness to several pixel-level corruptions, demonstrating that explicit topological structure is a practical route to robust HD representations. The code is provided at this https URL.

---


### 148. [Accelerating Rectified Flow Models via Trajectory-Aware Caching](https://arxiv.org/abs/2605.16789)

**<font color=#1a73e8>作者：</font>** Xiao Liu, Kai Liu, Naiyang Guan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and rectified flow (RF) models generate high-fidelity images and videos, but their iterative velocity-field evaluations are computationally expensive. Existing caching methods accelerate sampling by skipping timesteps, yet their coarse approximations introduce accumulated errors over long skip intervals and degrade quality under aggressive acceleration. We propose TACache (Trajectory-Aware Cache), a training-free acceleration framework following a skip-then-compensate paradigm. TACache performs an orthogonal decomposition of discrete velocity acceleration along the RF trajectory into a parallel component and an orthogonal residual, isolating the magnitude and directional sources of per-step approximation error. The framework operates in two stages: offline, cumulative variation thresholds on the magnitude and direction indicators yield the skip schedule and bound how far each skip interval may extend; online, at each skipped step the offline statistics are combined with the sample's historical orthogonal direction to reconstruct the skipped velocity without additional model evaluations. Experiments on BAGEL, FLUX.1-dev, and Wan2.1-1.3B show that TACache achieves up to 4.14 speedup on text-to-image generation and 2.11 speedup on text-to-video generation, with consistent improvements over prior cache-based methods on all reference-based fidelity metrics. Code will be released soon.

---


### 149. [TIER: Trajectory-Invariant Execution Rewards for Multi-Step Tool Composition](https://arxiv.org/abs/2605.16790)

**<font color=#1a73e8>作者：</font>** Anay Kulkarni, ChiaEn Lu, Dheeraj Mekala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool use enables large language models to solve complex tasks through sequences of API calls, yet existing reinforcement learning approaches fail to scale to multi-step composition settings. Outcome-based rewards provide only sparse feedback, while trajectory-supervised rewards depend on annotated reference solutions, penalizing valid alternatives and limiting scalability. We propose TIER: Trajectory-Invariant Execution Rewards, a reward framework that derives supervision directly from function schemas and runtime execution, rather than from reference trajectories. The reward decomposes into format validity, schema adherence, execution success, and answer correctness, providing dense, interpretable sequence-level feedback derived from fine-grained verification of individual steps of tool use. This design allows any valid execution path to receive credit, naturally supporting multiple solution strategies and adapting to evolving tool interfaces. On DepthBench, a compositional benchmark stratified by depth (1 to 6 steps), TIER achieves >90% accuracy across steps, where trajectory-supervised rewards collapse beyond step-4. We further demonstrate consistent gains on benchmarks like BFCL v3 and NestFUL. Ablation studies confirm that all reward components are necessary, highlighting the importance of multi-level supervision for compositional reasoning.

---


### 150. [PULSE: Generative Phase Evolution for Non-Stationary Time Series Forecasting](https://arxiv.org/abs/2605.16793)

**<font color=#1a73e8>作者：</font>** Yangyou Liu, Zezhi Shao, Xinyu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting under non-stationarity faces a fundamental tension between capturing stable representations and adapting to distribution shifts. Existing methods implicitly rely on static historical assumptions, leading to a critical failure mode we term Phase Amnesia, where models become blind to the evolving global context. To resolve this, we formalize non-stationary dynamics through three physical hypotheses: wold decomposition, dynamical phase evolution, and heteroscedastic manifold generation. These principles inspire PULSE, a physics-informed, plug-and-play framework adopting a Disentangle--Evolve--Simulate design philosophy. Specifically, PULSE utilizes phase-anchored disentanglement to resolve optimization interference caused by dominant trends, employs a Phase Router to actively generate future trajectories, and introduces Statistic-Aware Mixup (SAM) to ensure robustness against out-of-distribution volatility. Empirically, PULSE enables a simple MLP backbone to achieve state-of-the-art or highly competitive performance across 12 real-world benchmarks. This validates that a correct physics-informed inductive bias is far more critical than raw architectural complexity for non-stationary forecasting. The code is available at: this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
