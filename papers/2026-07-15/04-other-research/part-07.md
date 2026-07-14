# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-420](./part-09.md)

---

### 301. [Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR](https://arxiv.org/abs/2607.11163)

**<font color=#1a73e8>作者：</font>** Ziang Ren, Guodong Lin, Yuchen Ai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained ASR models such as Whisper exhibit strong multilingual capabilities. However, fine-tuning on low-resource languages often causes catastrophic forgetting. Although continual learning mitigates this issue, existing methods struggle to regulate cross-task interference in multilingual settings, where dominant languages bias optimization. We propose Unified Gradient Projection (UGP), which constrains parameter updates using reference gradients from language-balanced replay in a unified projection space. By equalizing per-language contributions in the projection, UGP reduces dominant-language bias and improves cross-lingual stability. We further show that combining gradient-level projection with data-level replay yields complementary gains in stability and plasticity. Across diverse low-resource language groups and model scales, UGP enables effective adaptation while substantially mitigating forgetting. On Whisper-large-v3, it achieves near-zero average forgetting.

---


### 302. [Query-Focused Event Summarization: A Dataset and Benchmark](https://arxiv.org/abs/2607.11166)

**<font color=#1a73e8>作者：</font>** Chenyu Hu, Bang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A thematic corpus is a collection of semantically coherent documents that collectively describe different aspects of a shared thematic event. Such a corpus typically contains hundreds or even thousands of documents. While users' interests in a thematic event often span multiple dimensions, Query-Focused Summarization (QFS) aims to generate summaries tailored to users' queries. However, existing QFS datasets lack event-oriented summarization, and most QFS methods struggle with large-scale corpora. To address these challenges, we propose the Query-Focused Event Summarization (QFES) task and construct the QFESum dataset, which contains 8 thematic events, 16,684 documents, and 104 queries. Furthermore, we introduce a two-stage QFES framework consisting of Query-Focused Retrieval with Adaptive Thresholding (RAT) and Query-Focused Summarization based on Hierarchical Clustering (SHC). Experimental results on QFESum show that RAT and SHC consistently outperform the baselines, demonstrating their effectiveness for QFES. The dataset and code are publicly available at this https URL.

---


### 303. [STAMP: Provenance-Guided Credit Assignment for Deep Search Agents](https://arxiv.org/abs/2607.11172)

**<font color=#1a73e8>作者：</font>** Ke Xu, Han Xu, Xinran Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for deep-search agents has largely focused on trajectory-level scoring -- outcome correctness, citation-aware rewards, and evidence coverage. Yet the actions that expose supporting documents receive no targeted credit, a gap we call the reward-credit mismatch. We propose STAMP, in which a reference-based verifier judges whether each cited document supports an entity or relation in a training-time evidence graph, and first-exposure attribution traces each supported citation back to the action that first surfaced it. This step credit is injected through sign-preserving advantage modulation, which redistributes advantage across steps without changing the trajectory-level reward or the relative ranking of trajectories within each group. On BrowseComp, BrowseComp-ZH, and xbench-DS, STAMP improves the GRPO baseline by +2.0/+5.5/+3.0 points under matched SFT initialization, training data, and search tools, and composes with both outcome-only and citation-rubric base rewards. Component ablations confirm that the provenance-based credit signal and the sign-preserving advantage modulation each contribute to the gains.

---


### 304. [When Depth Is Better Told Than Shown: Depth-Ordinal Prompting for Vision-Language Spatial Reasoning](https://arxiv.org/abs/2607.11173)

**<font color=#1a73e8>作者：</font>** Quynh Vo, Phuc Dao, Cong-Duy Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are expected to reason about physical space -- which object is closer, what lies behind what, and how objects are arranged in 3D -- yet they still struggle with such spatial judgments. A natural remedy is to show the model a depth map, but we find that this can make performance worse. We show that depth is not absent: it reaches the language model, but becomes difficult to access for downstream reasoning, while rendered pseudo-depth maps act as noisy auxiliary images that frozen VLMs cannot easily regulate. We propose Depth-Ordinal Prompting (DOP), a training-free method that converts monocular depth into a single question-targeted ordinal text cue at the queried objects, without adding a depth image, training a module, injecting features, or using labels. Our key finding is form dependence: the same depth signal can hurt when shown as an image but help when told as this http URL benchmarks, models, and depth estimators, DOP improves spatial reasoning when pseudo-depth provides reliable object-level ordering and remains largely neutral in strong original-image regimes. It is also competitive with the strongest training-free depth-prompting alternative while being simpler and more targeted.

---


### 305. [The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](https://arxiv.org/abs/2607.11175)

**<font color=#1a73e8>作者：</font>** Chunzheng Zhu, Lei Tian, Bohan Tan 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing ability of large language models and vision language models to jointly interpret and reason over images and text is reshaping medical agents, moving them from task specific predictors toward autonomous systems that perceive, reason, plan, remember, and act in clinical environments. This work departs from the capability first perspective of existing literature and instead begins from clinical deployment, asking what tasks, contamination resistant benchmarks, and interactive training environments are required before medical agents can be trusted in practice. Medical agents are formalized as sequential decision making systems under partial observability, together with a three level autonomy taxonomy spanning assisted, cooperative, and fully autonomous operation. The field is organized along a unified scaling spine consisting of framework scaling, capability scaling, and environment scaling. Within this framework, clinical environment scaling, the integration of tools, data, and clinical gyms, is identified as the most actionable yet underexplored direction for agents operating in PACS, EHR, and FHIR ecosystems. Clinical self evolution, where agents improve through interaction with their environments rather than parameter scaling alone, is further positioned as a key research frontier, drawing insights from self improving agents, agent gyms, and test time compute scaling. Applications across radiology, pathology, ophthalmology, and hospital workflows are examined together with deployment challenges including hallucination, cascading failures, and fairness. By consolidating more than 300 references, with particular emphasis on advances from 2025 to 2026, this work provides a roadmap toward trustworthy, self improving medical imaging systems for real clinical practice.

---


### 306. [NeuroMem-FHP: A Likelihood-Free Deep Learning Framework for Parameter Estimation of Fractional Hawkes Process](https://arxiv.org/abs/2607.11177)

**<font color=#1a73e8>作者：</font>** Neha Gupta, Aditya Maheshwari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose deep learning based NeuroMem-FHP framework for estimating the parameters of the fractional Hawkes process (FHP), a self-exciting point process that captures long-range dependence through a fractional Mittag-Leffler excitation kernel. Two neural architectures, namely a Long Short-Term Memory (LSTM) network and a Transformer, are developed to estimate the model parameters $(\mu,\gamma,\alpha,\beta)$ directly from sequences of inter-arrival times without requiring computationally intensive likelihood optimization. Experiments on synthetic data that both neural models significantly outperform the classical Maximum Likelihood Estimation (MLE) method, with the Transformer achieving the highest estimation accuracy (MSE = $0.1634$), followed by the LSTM (MSE = $0.1752$), compared to MLE (MSE = $2.8032$). An ablation study further examines the effects of key hyperparameters on model performance. The proposed framework is also on two real-world high-frequency datasets, namely AAPL NBBO transaction data and Montgomery County 911 emergency call records. Using a predictive validation approach, event sequences simulated from the estimated parameters closely reproduce the empirical distribution, tail behavior, and temporal dependence structure of the observed data. These results demonstrate that Transformer-based parameter estimation provides an accurate and efficient alternative to conventional estimation techniques for FHP and offers a promising framework for modeling event-driven systems with long-memory dynamics.

---


### 307. [SCALECUA: Scaling Computer Use Agents with Verifiable Task Synthesis and Efficient Online RL](https://arxiv.org/abs/2607.11185)

**<font color=#1a73e8>作者：</font>** Bowen Lv, Xiao Liu, Yanyu Ren 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs) are emerging as a powerful interface for automating complex digital workflows through visual perception and GUI execution. Online reinforcement learning with verifiable rewards (RLVR) has emerged as a key direction for scaling their capabilities. However, this paradigm is bottlenecked by verifiable data scarcity and online RL inefficiency. To break these barriers, we introduce ScaleCUA, a unified framework that scales online RL for CUAs via verifiable task synthesis and efficient training. At the data level, we design VeriGen, an end-to-end framework for generating verifiable RL tasks through iterative docker interactions and a multi-agent feedback loop. Scaled to 100+ concurrent agent workers via a shared docker interaction probe, this pipeline produces 24K+ verifiable tasks and nearly 3K high-quality RL tasks. To maximize sample efficiency, we propose Frontier Sampling, which tracks per-task capability and allocates rollouts to the current learning frontier. On the training side, we further design Visual Context Segmentation, a sliding window over recent visual context that balances rollout and training-engine pressure, yielding a 2.83x training speedup over step-wise decomposition. Together, ScaleCUA achieves 68.7% on OSWorld and 54.0% on ScienceBoard, establishing new state-of-the-art performance among open-source computer use agents. Code, models, and datasets are available at this https URL.

---


### 308. [Slot-RAE: Streamlining Object-Centric Learning via Direct Representation Auto-Encoders](https://arxiv.org/abs/2607.11196)

**<font color=#1a73e8>作者：</font>** Alexandre Chapin, Emmanuel Dellandrea, Liming Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying object-centric models for real-world scene understanding typically requires complex pipelines to achieve both robust scene decomposition and high-fidelity generation. Recent diffusion-based approaches have improved visual quality, but they almost universally rely on heavy, pretrained generative priors (e.g., Stable Diffusion) and external VAE latent spaces. In this paper, we propose Slot-RAE, a much simpler, fully integrated framework that operates directly within the continuous semantic feature space of visual foundation models (e.g., DINOv3). Slot-RAE employs a feature-space diffusion process using a Diffusion Transformer (DiT) decoder and a Representation Alignment (REPA) head. Unlike existing diffusion-based objectcentric methods that rely heavily on subsidized text-toimage priors, the generative core of Slot-RAE (Slot Attention and the DiT) is trained from scratch within the frozen VFM feature space. This eliminates the need for VAE bottlenecks and task-agnostic generative pre-training. Experiments on the COCO dataset demonstrate that despite its architectural simplicity, Slot-RAE achieves state-of-the-art results. It delivers comparable unsupervised object discovery, higher-fidelity image reconstruction, and robust zero-shot compositionality, all while being significantly faster and more computationally efficient than existing object-centric latent diffusion models.

---


### 309. [Parallax Portrait Matting](https://arxiv.org/abs/2607.11205)

**<font color=#1a73e8>作者：</font>** Xin Cai, Jiawen Chen, Lars Jebe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image matting is highly ill-posed, especially when both the foreground and background are richly textured. While single-image matting methods learn strong priors from data, they often struggle on these challenging cases. Existing approaches improve results by requiring additional signals such as green screens, polarized lighting, or clean background images, but these typically rely on specialized capture setups. We present Parallax Portrait Matting, a practical two-frame matting method that uses a second image captured with slight viewpoint change. Such a setting arises naturally in burst photography, where small camera motion induces foreground-background parallax and provides complementary observations for matting. Our pipeline estimates trimaps and foreground/background motion, then constructs aligned views for prediction. To handle imperfect motion estimation, the network uses the background-aligned pair for direct fusion and the foreground-aligned cue through cross-attention for error compensation. Experiments show that our method recovers finer details and more accurate foreground colors than strong single-image matting baselines on challenging portrait cases.

---


### 310. [PREF-Gate: Provenance-Constrained Relational Evidence Fusion with Validation-Gated Selection for Graph Fraud Detection](https://arxiv.org/abs/2607.11212)

**<font color=#1a73e8>作者：</font>** Liming Liu, Chao Hu, Mingfei Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational fraud detection can exploit both label-free graph context and label-derived neighborhood evidence, but these two information sources obey different validity conditions. In particular, neighborhood risk becomes invalid when a queried node's own label, or any validation or test label, enters its construction. We formulate this issue as provenance-constrained relational evidence use and present PREF-Gate, an auditable decision framework with two fixed experts and a finite validation gate. The context expert uses attributes, one-hop means, feature residuals, and degree descriptors without labels. The evidence expert adds self-excluded, training-label-only neighborhood risk and empirical-Bayes summaries that expose support, uncertainty, availability, and shrinkage. Before test inference, the gate selects either expert or one of three pre-specified probability mixtures and fixes the decision threshold. On Amazon, YelpChi, and TFinance, using five identical stratified splits and 14 same-protocol methods, PREF-Gate obtains mean AUPRC values of 0.9085, 0.8104, and 0.8913. It selects the label-free expert on all Amazon and YelpChi splits and an evidence mixture on all TFinance splits. Thus, the main result is conditional rather than universal: label-derived relational evidence is useful only where held-out validation supports it. The framework couples competitive ranking performance with an explicit label-provenance contract, finite selection policy, failure accounting, and review-budget evaluation, providing an auditable knowledge-based decision pipeline for graph fraud detection.

---


### 311. [When the Target Domain Changes: AI-Mediated Construct Drift in High-Stakes English Language AssessmenW](https://arxiv.org/abs/2607.11213)

**<font color=#1a73e8>作者：</font>** Yi Gui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-stakes English proficiency tests treat standardized, unaided performance as evidence for score interpretations about academic English proficiency. This interpretation remains meaningful, but as target language use domains increasingly involve generative AI, the extrapolation from unaided test performance to academic communicative readiness becomes less self-evident. This conceptual validity argument reframes AI as a score-interpretation problem in high-stakes language testing, not only an operational issue of scoring, feedback, security, or misconduct. Synthesizing current literature in three uneven layers, the paper shows that most work treats AI as assessment infrastructure, while far less theorizes its implications for construct validity and extrapolation warrants. It defines AI-mediated construct drift as the misalignment that arises when communicative abilities required in the target domain change through AI mediation while test constructs remain anchored to an unaided-performance model. It proposes bounded AI mediation as a validity-oriented design principle: a standardized condition in which all test takers access the same institutionally controlled AI assistant, with predefined assistance boundaries, logged interactions, and tasks that distinguish comprehension support from answer generation. The paper argues that score interpretations should be narrowed and supplemented when used to support claims about AI-mediated academic communication.

---


### 312. [A Novel Method to Evaluate Models on Unreliable, Noisy and Inconsistent Labels: Adaptive Resolution Label Aggregation (ARLA)](https://arxiv.org/abs/2607.11214)

**<font color=#1a73e8>作者：</font>** Natasha Randall, Gernot Heisenberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Labels are critical for both training and evaluating deep learning segmentation models, but are often inconsistent, noisy, or ambiguous at class boundaries. Many approaches have been developed to support training models on weak labels, but few to none currently exist to facilitate evaluating models on unreliable labels. We therefore introduce a method called "Adaptive Resolution Label Aggregation", or "ARLA", which dynamically adapts the resolution of both the label and the model prediction at inference time before the evaluation metrics are computed. We demonstrate how ARLA can be used to better analyse model behaviour with a practical application to a real flood prediction model, where ARLA was able to overcome issues with inconsistent labelling of forested areas and errors in labels within regions of heavy cloud cover. Our work presents a new approach to evaluating segmentation models, with adjustable parameters to adapt the aggregated resolution to the precision of the label or the level of label noise. Fundamentally, ARLA exploits the information encapsulated by a label but minimises the label error, extracting from the noise a clearer signal of a model's true performance.

---


### 313. [Q-BridgeNet: A Quantization Network for Cross-Lingual Sign Language Translation](https://arxiv.org/abs/2607.11215)

**<font color=#1a73e8>作者：</font>** Liqian Feng, Lintao Wang, Xiaochen Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most sign language translation (SLT) methods focus on isolated native sign-spoken pairs (e.g., American Sign Language - English). Extending language-specific SLT models to multilingual translation would improve accessibility by enabling communication across diverse sign and spoken language communities. However, existing multilingual SLT approaches still struggle to learn a unified model that minimizes cross-lingual conflicts while capturing shared cross-lingual semantics and preserving language-specific variations across different sign languages. Therefore, we propose Q-BridgeNet, a unified framework for multilingual SLT that jointly mitigates cross-lingual conflicts across both the sign language and spoken language sides. On the sign language side, Q-BridgeNet learns discrete Q-units via adaptive segmentation and residual vector quantization: a shared base codebook provides language-agnostic semantic primitives, while language-specific residual codebooks refine heterogeneous signing semantics. On the spoken language side, a multilingual LLM is fine-tuned to operate in the Q-unit space, leveraging cross-lingual priors to enable a unified SLT model. Experiments on PHOENIX14T, How2Sign, and CSL-Daily show that Q-BridgeNet effectively mitigates cross-lingual conflicts, achieving state-of-the-art performance on native sign-spoken pairs while also demonstrating strong generalization to non-native pairs. Our source code is publicly available at: this https URL

---


### 314. [HandFlow: Fully Generative 4D Hand Recovery with Flow Matching](https://arxiv.org/abs/2607.11221)

**<font color=#1a73e8>作者：</font>** Mingxi Xu, Bowen Duan, Yi Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate monocular 4D hand reconstruction remains challenging. Per-frame discriminative regressors lack temporal context and often produce jittery predictions. Temporal models improve consistency by aggregating information across frames, but they are typically deterministic regressors, making them vulnerable to ambiguous observations caused by occlusion and motion blur. Generative modeling offers a natural alternative by learning a prior over plausible hand motion sequences, enabling coherent hand-state recovery when visual evidence is incomplete or unreliable.
Motivated by this observation, we present HandFlow, a fully generative flow-matching framework for temporally coherent 3D hand pose and shape estimation from monocular video. Given visual and skeletal observations, HandFlow denoises an entire temporal window of MANO parameters through a single ODE integration. To support this, we use a Flux-style dual-stream transformer that attends across the full sequence to capture long-range dependencies without autoregressive decoding, and a confidence-aware continuous masking mechanism that blends observed features with learnable mask tokens to handle noisy or missing observations. Experiments on DexYCB and HOT3D show that HandFlow achieves state-of-the-art performance, with particularly large gains in world-space accuracy and temporal smoothness. It reduces world-space pose error by over 30% compared with the strongest baseline and achieves the lowest acceleration error among all evaluated methods, while remaining competitive in per-frame pose accuracy. Moreover, on a single GPU HandFlow reconstructs a 150-frame sequence at 47 fps, about 12x faster than the fastest prior video-based method, with reconstruction itself accounting for only a small fraction of the end-to-end latency.

---


### 315. [Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory](https://arxiv.org/abs/2607.11226)

**<font color=#1a73e8>作者：</font>** Tengjiao Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents today are caught in an awkward bind. Lock them down with static safety instructions and they rarely venture beyond the obvious; give them free reign with tools and multi-agent debate, and safety violations quickly follow. Rather than forcing a single model to juggle both creativity and caution, we separate the concerns across specialized roles. A Disrupter generates unconventional proposals, a Validator enforces hard runtime checks at the tool gateway, and a Broker pulls in distant but relevant analogies. Failures are not discarded -- they are compiled, via MCTS, into compact, signed constraint patches we call Scars. These patches are cached locally and inherited by future cohorts, turning repeated failures into reusable, low-cost runtime constraints. In a spatial-semantic sandbox (N=20 runs, p<0.01), our cohort reaches remote targets where debate fails, the Validator prevents all executed breaches, and Scars reduce token consumption by 15.1% by avoiding redundant validator checks. Furthermore, credit-based Communication Allocation Scores (CAS) restrict outbound bandwidth, reducing overall token costs by 55.9% under resource constraints.

---


### 316. [Structure-Detail Decoupled Autoregressive Generation for Fast and High-Fidelity Virtual Try-On](https://arxiv.org/abs/2607.11233)

**<font color=#1a73e8>作者：</font>** Lu Yang, Xiaonan Hu, Yanan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on (VTON) is a bi-conditional image generation problem that requires not only accurate person preservation but also faithful garment deformation and detail synthesis. Diffusion-based VTON methods can jointly model these factors in a compressed latent space, but suffer from high-frequency detail loss due to inherent latent compression, even with costly multi-step denoising. Recent visual autoregressive (VAR) models offer a promising alternative for high-quality generation with faster inference, yet remain unexplored for VTON due to the lack of effective bi-conditioning mechanisms. To bridge this gap, we first introduce VAR-VTON, a VAR-based VTON model that incorporates garment conditioning and structural guidance for efficient latent-space VTON. Despite its efficacy, latent-space generation still struggles to preserve fine-grained garment details. We argue that different VTON sub-tasks should be addressed in different representation spaces: structural synthesis such as garment warping and person layout is suited to the latent space, whereas fine-grained detail recovery should be tackled in the pixel space. Motivated by this insight, we further propose STAR-VTON, a Two-Stage AutoRegressive framework that builds upon VAR-VTON by decoupling latent-space structural synthesis from pixel-space detail recovery. Our idea is to resort to a matching-informed refiner to establish dense correspondences between the stage-one generation and the source garment to directly map fine-grained pixel-space details. Extensive experiments show that STAR-VTON achieves an impressive efficiency-fidelity trade-off: VAR-VTON runs at least $4\times$ faster than diffusion-based counterparts without degrading quality, and the pixel-space refiner effectively restores fine details and acts as a plug-and-play module that can benefit existing VTON approaches.

---


### 317. [A Nearable Soft Mat Based on Distributed Optical Fiber Sensing for Physiological Monitoring](https://arxiv.org/abs/2607.11255)

**<font color=#1a73e8>作者：</font>** Vincenzo Lavorgna, Martina Pulcinelli, Andrea Polimadei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distributed optical fiber sensing (DOFS) combines the advantages of fiber optic sensors, including flexibility, small size, immunity to electromagnetic interference, and high metrological performance, with the capability to transform a single optical fiber into a continuous sensing element for spatially resolved mechanical measurements. Optical frequency domain reflectometry (OFDR), based on Rayleigh backscattering, enables high spatial resolution DOFS measurements, broadening the range of potential sensing applications. However, OFDR based DOFS remains largely unexplored for biomedical applications, despite the need for sensitive, spatially resolved, and conformable sensing interfaces. This study presents a soft DOFS based mat as a large-area interface for physiological monitoring. A single-mode optical fiber was embedded in a flexible silicone matrix and arranged in a serpentine layout to distribute sensing over the mat surface. With a gage pitch of 2.6 mm, the system provided 2250 sensing sites across the active area at a sampling frequency of 50 Hz. The mat was assessed on six healthy volunteers in a seated nearable configuration on the backrest of a standard office chair. The distributed output enabled two dimensional mapping of the mat response, reflecting back mat mechanical coupling and cardiorespiratory induced perturbations. Respiratory rate and heart rate were therefore estimated and compared with a reference wearable system. The maps revealed physiologically coherent spatial and temporal patterns, while the estimated rates showed good agreement with the reference measurements. These results demonstrate the feasibility of combining large area distributed sensing, spatial mapping, and quantitative cardiorespiratory monitoring within a DOFS based soft nearable interface.

---


### 318. [Bringing Back Rule Induction to Fluid Intelligence Research? An Initial Validation of the ARC-AGI Benchmark in Humans](https://arxiv.org/abs/2607.11263)

**<font color=#1a73e8>作者：</font>** Jasmin Thelen, Oliver Wilhelm  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two competing perspectives on fluid intelligence (gf) measures propose that performance is primarily constrained either by working memory capacity or by the ability to induce novel relations. The first perspective is currently dominant in measurement, as evident from the use of a limited set of recurring rules, whereas the second perspective is reflected in many definitions but rarely present in measurement. The ARC-AGI benchmark predominantly requires rule induction and was proposed as a measure of gf for both humans and artificial systems. However, its psychometric properties have not yet been examined in human samples. We therefore investigated the psychometric characteristics and nomological network of ARC-AGI in a first study with 100 participants. A compilation of ARC-AGI items showed good psychometric properties and correlated substantially with figural fluid intelligence as measured by a figural reasoning test (\r{ho} = .63). Associations with figural originality were weak. These findings provide initial support for the validity of ARC-AGI as a measure of human fluid intelligence. Future research should include more rule induction tasks as well as additional multivariate covariates. This study is unusual by studying a task in humans that was initially designed for machines. We suggest systematically embedding AI benchmarks into the nomological network of human cognitive abilities to enable more systematic evaluation and interdisciplinary cooperation.

---


### 319. [Valid $\ne$ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought](https://arxiv.org/abs/2607.11266)

**<font color=#1a73e8>作者：</font>** Daeyeop Lee, Hwanjo Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) prompting has significantly advanced the reasoning capabilities of Large Language Models (LLMs), yet it often incurs substantial computational costs due to over-reasoning: the generation of redundant, verbose, or irrelevant steps. While existing reasoning step evaluators effectively detect logical fallacies and factual errors, our analysis reveals a critical blind spot: they fail to penalize valid but inefficient reasoning steps that inflate token usage without contributing to the solution. To systematically diagnose this limitation, we introduce RIV-GSM8K, a diagnostic benchmark injected with five distinct types of inefficiencies, including circular reasoning and excessive decomposition. Diagnostic experiments reveal that state-of-the-art evaluators struggle to distinguish these inefficiencies from necessary reasoning. To address this gap, we propose CAID (Context-Aware Information Density), a training-free metric grounded in information theory that identifies low-utility steps. To validate the metric's practical utility, we apply it within PACE, a post-hoc compression strategy. Additional control experiments show that the gains of PACE are not explained by trivial pruning: compared with random step removal and PRM-based compression baselines, it preserves accuracy at substantially higher compression rates. Empirical results on GSM8K, StrategyQA, and ARC-Challenge demonstrate that PACE reduces token consumption by 31-53% while maintaining accuracy, confirming that CAID successfully distills informational froth from reasoning chains without compromising deductive validity.

---


### 320. [Trustworthy synthetic data for campaign decision support: strategy simulation fidelity and the PolicySynth framework](https://arxiv.org/abs/2607.11269)

**<font color=#1a73e8>作者：</font>** Tung Dang, Hung Phung, Son Lam Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision support systems (DSS) increasingly run retention what-if analysis on synthetic customer populations, because privacy constraints preclude unrestricted use of real data. Such a system is trustworthy only if the synthetic data lead managers to the same decisions as the real data would; yet prevailing criteria certify distributional similarity, not decision alignment, so a synthetic population can match every marginal distribution while still steering a marketing team toward the wrong campaigns. We close this decision-alignment gap with three contributions: strategy simulation fidelity (SSF), a criterion measuring how often the synthetic population yields the same go/no-go campaign decision as the real population; PolicySynth, a DSS framework whose generator is conditioned on the production churn scorer to align decision-relevant structure; and a three-axis reporting standard of decision alignment, membership-inference resistance, and novel-record rate as the minimum deployment quality gate. On a telecommunications churn corpus and a banking acquisition corpus, PolicySynth attains a mean SSF of 0.923 and 0.960, with seed-to-seed variance roughly ten times tighter than CTGAN on telecommunications and 2.5 times on banking. This stability is the deployable property: go/no-go recommendations shift by at most 1.2 percentage points between monthly retraining cycles, against 11.5 for CTGAN, a reversed recommendation on one campaign in nine. A bootstrap baseline matches PolicySynth on SSF yet copies real records verbatim and fails membership inference, evidence that no single axis suffices. PolicySynth reliably supports directional go/no-go screening; its ROI estimates diverge from real outcomes by 70 to 78% and require the volume correction we document.

---


### 321. [FAD-SA-GRU: Enhancing Hate Speech Detection in Algerian Dialect Through Feature-Augmented Self-Attention GRU Networks](https://arxiv.org/abs/2607.11279)

**<font color=#1a73e8>作者：</font>** Sara Yakoubi, Ikram Khalfallah, Kenza Khelkhal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of social media platforms has transformed online communication by enabling users to exchange information and opinions instantly. However, these platforms have also facilitated the dissemination of abusive and hateful content, posing major social, psychological, and ethical challenges. Hate speech can incite discrimination, harassment, and violence against individuals or communities based on attributes such as ethnicity, religion, gender, nationality, or political affiliation. Consequently, automatic hate speech detection has become a major research topic in natural language processing (NLP) and an essential component of content moderation systems.
This paper investigates automatic hate speech detection in the Algerian Arabic dialect (Darija) on social media. This task remains challenging because of the dialect's linguistic diversity, characterized by the coexistence of Arabic, French, and Arabizi (Arabic written using the Latin alphabet). We compare four categories of text classification approaches: (1) traditional machine learning models using TF-IDF features, (2) deep learning models based on recurrent neural networks, (3) Transformer-based language models, including DziriBERT and multilingual BERT, and (4) a novel hybrid architecture, FAD-SA-GRU, which combines semantic representations from DZ FastText, DZ AraVec, and DziriBERT through multi-embedding fusion, followed by a self-attention-enhanced GRU encoder.
Experiments on an annotated dataset of Algerian Darija social media comments for binary hate speech classification show that FAD-SA-GRU outperforms all baselines, achieving 93.2% accuracy, 93.4% precision, 91.0% recall, 92.1% F1-score, and 97.0% ROC-AUC. Results demonstrate the effectiveness of combining complementary embedding representations with attention-based sequence modeling for robust hate speech detection in low-resource dialectal Arabic.

---


### 322. [The Devil Is in the Leakage: A Disentangled Dual-Purification Framework for High-Fidelity Hairstyle Transfer](https://arxiv.org/abs/2607.11281)

**<font color=#1a73e8>作者：</font>** Jijie Li, Jiankuo Zhao, Xiangyu Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hairstyle transfer aims to synthesize a photorealistic portrait by transplanting the hairstyle from a reference image onto a source subject while preserving the source identity. Recent foundation models show strong generative capability, but they struggle with the zero-shot disentanglement required for precise local editing, often entangling the reference hairstyle with its original identity and pose. Existing diffusion-based pipelines typically decompose the task by first generating a "bald" image from the source and then injecting hairstyle features from the reference. However, we show that this paradigm suffers from a fundamental leakage problem. Identity Leakage in Hairstyle occurs when hairstyle features retain reference identity or pose information, while Flaw Leakage in Bald arises when residual artifacts in the bald image are propagated into the final synthesis. To address both issues, we propose the Dual-Purification Framework (DPF), which introduces two complementary training-time regularizers. Adversarial Hairstyle Purification (AHP) purifies hairstyle features by suppressing identity predictability under a mutual-information-inspired adversarial objective. Contrastive Geometric Purification (CGP) regularizes the ControlNet pathway with a contrastive objective, reducing the model's reliance on geometric artifacts in the bald condition. By jointly purifying the hairstyle representation and geometric pathway, DPF achieves high-fidelity, identity-preserving hairstyle transfer and state-of-the-art performance on diverse benchmarks.

---


### 323. [SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation](https://arxiv.org/abs/2607.11285)

**<font color=#1a73e8>作者：</font>** Tianyu Xiong, Rui Li, Suning Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D scenes from unordered images remains bottlenecked by expensive Structure-from-Motion (SfM) preprocessing and frozen pose interfaces. We present SalientGS, a unified SfM-to-3D Gaussian Splatting (3DGS) pipeline. Its central contribution is importance-guided Markov Chain Monte Carlo (MCMC) Gaussian allocation, which aggregates multi-view residuals into per-Gaussian underfit and redundancy signals. These signals define a smooth importance-weighted sampling distribution that biases both birth and relocation toward underfit regions. This reallocates capacity from well-fit areas without altering the underlying stochastic gradient Langevin dynamics (SGLD). SalientGS achieves end-to-end reconstruction in 15 minutes with state-of-the-art perceptual quality. The supplementary material provides dedicated sections for Per-Scene Qualitative Comparisons and Per-Image Learned Perceptual Image Patch Similarity (LPIPS) Analysis, including failure cases. Code and evaluation scripts are available at this https URL.

---


### 324. [Metadata Supervised MRI Representations for Modelling and Controlling Acquisition Variability](https://arxiv.org/abs/2607.11295)

**<font color=#1a73e8>作者：</font>** Mehmet Yigit Avci, Pedro Borges, Virginia Fernandez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance imaging exhibits substantial acquisition variability, where identical anatomy can appear markedly different across scanners and imaging protocols. Consequently, learned representations entangle biological structure with acquisition-dependent appearance, limiting interpretability, generalisation, and clinical deployment. We show that these sources of variation can be separated by jointly modelling MRI images and DICOM metadata. Using large-scale clinical brain MRI data, we learn representations that separate anatomical structure from contrast-dependent appearance. Resulting contrast representations organise heterogeneous acquisitions, support sequence understanding, and detect image--metadata inconsistencies, whereas anatomical representations suppress acquisition-specific variation while preserving biologically relevant information. Building on these disentangled representations, we introduce a unified anatomy-preserving harmonisation model for cross-modality and cross-site adaptation, conditioned on image or acquisition metadata. Our findings suggest that acquisition variability is a structured component of the imaging process that can be modelled, audited, and controlled, providing a foundation for acquisition-aware representation learning in large-scale medical imaging.

---


### 325. [ASUMOT: Motion-Consistency-Based Asynchronous UAV Detection and Tracking with Event Cameras](https://arxiv.org/abs/2607.11303)

**<font color=#1a73e8>作者：</font>** Baofeng Jia, Xiaoyu Chen, Jingyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras offer microsecond-level temporal resolution and high dynamic range for low-altitude UAV perception. However, long-range UAVs often produce sparse, fragmented, and noise-contaminated event responses, where one semantic target may appear as multiple spatially separated blobs. Direct blob-level asynchronous tracking therefore suffers from duplicate trajectories and unstable identities. We propose ASUMOT, a motion-consistency-based asynchronous UAV detection and tracking framework operating directly on raw events. ASUMOT models each UAV as a set of motion-consistent event blobs. A local motion-consistency estimator triggers reliable candidates, a lightweight multi-task verifier provides UAV confidence and motion-direction cues, and motion-consistency clustering aggregates fragmented blobs into identity-consistent UAV tracks. We also introduce ES-UAV, a high-definition event-level UAV benchmark with dense semantic annotations. Experiments on public UAV tracking data and ES-UAV show that ASUMOT improves the accuracy--efficiency trade-off while preserving asynchronous event processing. Code and Dataset will be released.

---


### 326. [Efficient Test-Time Optimization for Multi-Agent Proof Autoformalization](https://arxiv.org/abs/2607.11307)

**<font color=#1a73e8>作者：</font>** Tian-Shuo Liu, Shiyuan Zhang, Zijie Geng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-proof autoformalization bridges extensive mathematical proofs in natural language with formally validated reasoning, offering a pathway to elevate the ceiling of verifiable mathematical reasoning. Unlike statement-level formalization, proof autoformalization is a long-horizon challenge requiring coordination of claims, contexts, and dependencies across many proof steps, yet has only recently come under focused study. Current approaches either rely on costly model training or apply excessive, unguided repair at inference time. To this end, we introduce ToMap, a multi-agent framework that structures proof autoformalization as a Decomposer-Formalizer-Prover pipeline with efficient test-time optimization guided by formal verification and semantic rubrics for proof quality. Rather than distributing test-time compute across all agents, we perform bottleneck analysis and identify the Decomposer as the critical bottleneck: the quality of its atomic, self-contained proof units directly determines whether downstream agents can successfully formalize and prove each step. ToMap therefore treats the Formalizer and Prover as downstream executors and efficiently focuses test-time compute on Decomposer refinement. This refinement follows a loop inspired by GEPA, evolving prompts over candidate decompositions and using formal verification progress together with semantic proof rubrics to define a Pareto frontier that guides the next decomposition update. Experiments on ProofFlowBench show that ToMap improves over the best previous method by 19.0% when evaluated by both syntactic correctness and semantic faithfulness, while requiring lower test-time cost. Scaling analysis shows that most gains emerge within a few iterations of decomposition evolution, guiding test-time budget selection.

---


### 327. [SPARC-Net: A Spectral, Causality-Aware, and Hard-Constrained Physics-Informed Architecture for Stiff and Shock-Dominated Partial Differential Equations](https://arxiv.org/abs/2607.11310)

**<font color=#1a73e8>作者：</font>** Divyavardhan Singh, Dimple Sonone, Hammad Mohammad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) provide a meshless approach for solving partial differential equations (PDEs), but suffer severe degradation in stiff and shock-dominated problems, where small PDE residuals can correspond to globally inaccurate solutions. We show these failures are multi-causal, arising from the concurrent interplay of (i) spectral bias against sharp features, (ii) imbalanced multi-term optimization and loss-weight collapse, (iii) violation of temporal causality, and (iv) under-resolved collocation. We present SPARC-Net, a unified architecture and training framework that jointly addresses all four pathologies. SPARC-Net leverages an adaptive multi-scale spectral encoder with a learnable spectral gate, a gated residual backbone, adaptive activations, and a hard-constraint output ansatz that exactly enforces initial and boundary conditions, structurally eliminating loss-weight collapse. Training employs stabilized gradient-norm loss balancing, floored causality-respecting residual weighting, and residual-based adaptive collocation (RAD). Validated against exact analytic and high-order spectral reference solutions across four canonical benchmarks -- viscous Burgers', Allen-Cahn, convection (beta=30), and reaction -- SPARC-Net yields substantial improvements over vanilla PINNs: relative L2 error drops from 1.47e-1 to 1.14e-1 on Burgers' (22% reduction), 9.93e-1 to 5.78e-2 on Allen-Cahn (94% reduction), and 9.82e-1 to 3.54e-3 on reaction (100% reduction). A characteristic-coordinate encoder for hyperbolic transport further reduces convection error from 5.14e-1 to 9.88e-5 (100% reduction). We report five-seed mean +/- standard deviation errors, Wilcoxon significance tests, full ablation studies, hyperparameter sensitivities, an extension to the 2D heat equation, and comparisons against parameter-matched baselines.

---


### 328. [Verifier-Guided Twelve-Tone Composition: A Generate-Verify-Repair Harness for Symbolic Music Generation](https://arxiv.org/abs/2607.11334)

**<font color=#1a73e8>作者：</font>** Congren Dai, Danni Zhao, Enyang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can produce superficially legal twelve-tone scores that collapse into degenerate textures. We introduce a neuro-symbolic harness that wraps a language-model proposer in a generate-verify-repair-trace loop with symbolic verification. The complete pipeline improves event-local consistency without claiming whole-piece legality. Across 40 controlled tasks and four paired models, audited delivery yield rises from 13.3% under raw generation to 48.1% with the harness, which explicitly abstains otherwise. The pass rate of a narrower collision and serialisation-consistency check rises from 33.5% to 58.3%, while degeneracy remains near 0.05, including under exploratory adversarial prompting. A blinded evaluation by five experts also shows a descriptive aggregate preference for harness candidates over raw generation in adherence, perceived legality, coherence, and overall quality.

---


### 329. [AutoVSR: Automatic Visual-to-Symbolic Reasoning for Symbolic Expression Generation from Circuit Schematic](https://arxiv.org/abs/2607.11338)

**<font color=#1a73e8>作者：</font>** Zhe Xiao, Longfei Li, Xu He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symbolic expressions can effectively characterize and predict circuit behavior, but deriving them directly from circuit schematics is challenging. This process requires accurate visual-to-symbolic construction of circuit structure from images and correct multi-step symbolic derivation, both of which impose strict correctness requirements. This work proposes AutoVSR, an automated framework for visual-to-symbolic generation of circuit expressions using Vision Language Models (VLMs). By reconstructing circuit diagrams into an executable intermediate representation (Executable IR) and leveraging a symbolic solver for reasoning, AutoVSR significantly improves the accuracy of symbolic expression generation. AutoVSR introduces two key innovations: an IR construction method guided by component rule retrieval and verification-based feedback, and a symbolic solver implemented as a planning agent equipped with a symbolic tool library for reliable multi-step derivation. Compared with end-to-end VLM approaches and specialized methods on the main symbolic expression generation task, AutoVSR achieves accuracy improvements of 30.01--59.45% and 41.96--51.84%, respectively. Moreover, AutoVSR surpasses closed-source state-of-the-art VLMs in inference cost and computational efficiency. Code is available at this https URL.

---


### 330. [The In-Car Sign Language Corpus (ICSL): A Multi-Modal Resource for Constrained-Space Sign Language Recognition](https://arxiv.org/abs/2607.11341)

**<font color=#1a73e8>作者：</font>** Raviteja Boddu, Guilherme Vieira Leite, Joed Lopes da Silva 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenges of using sign language within shared mobility services, such as taxis, carpools, or ride-sharing platforms. The use of sign language recognition (SLR) in real-world, confined environments, specifically vehicle interiors remains largely unexplored. To motivate research in this area, we present the In-Car Sign Language (ICSL) dataset for Brazilian Sign Language (Libras), with the long-term goal of improving public transport accessibility for the Deaf and Hard-of-Hearing community. The dataset consists of: (1) high-precision laboratory motion capture (MoCap) data to establish an idealized linguistic baseline and (2) real-world multi-modal in-car recordings captured using a 2D camera and 3D Time-of-Flight sensors. The dataset provides a basis for comparative analyses between synthesized signing avatar animations and recorded real signing interpreter videos, which enable future research into robust "in-the-wild" SLR models and domain adaptation. We describe in detail the use cases, the setup, the data collection protocol, and the metadata structure of the corpus. In total, we recorded a multimodal dataset exceeding 1.5 million frames, comprising the synchronized multimodal streams described above featuring Libras users across various in-car scenarios. The corpus is provided with gloss annotation of lexical signs and non-lexical sign language elements specially designed to support the training and evaluation of deep neural networks for constrained space recognition. In-vehicle signing offers a technically significant example of a constrained, occluded, and non-frontal environment. While recognizing the diverse communication strategies already employed by the Deaf community, identifying automotive-specific limitations provides a useful stepping stone for research into enhancing in-car accessibility and passenger quality of life.

---


### 331. [Longitudinal Multi-View Breast Cancer Risk Prediction](https://arxiv.org/abs/2607.11343)

**<font color=#1a73e8>作者：</font>** Solveig Thrun, Zijun Sun, Suaiba A. Salahuddin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate breast cancer risk prediction from screening mammography is critical for enabling personalized screening intervals and early detection. Recent deep learning methods have shown the value of longitudinal data and explicit temporal alignment. However, existing approaches either perform explicit alignment using a single mammographic view or model multiple views without explicit longitudinal alignment, limiting their ability to exploit the complementary spatial-temporal information used in clinical practice. To address this gap, we propose LMV-Net, a longitudinal multi-view breast cancer risk prediction model that jointly analyzes anatomically complementary CC and MLO views within an explicitly aligned longitudinal framework. We evaluate our approach on the public EMBED and CSAW-CC datasets, comparing it to state-of-the-art breast cancer risk prediction methods. Our model consistently outperforms existing approaches in overall risk prediction performance and across different breast density and cancer subgroups. Importantly, these improvements highlight the potential of longitudinal multi-view modeling to enhance risk stratification, paving the way for future work on personalized screening, earlier identification of high-risk patients, and more efficient screening resource allocation. The code is available at this https URL.

---


### 332. [From Neural Network Decisions to Training Cases: An Exact Account via Case-Based Decision Theory](https://arxiv.org/abs/2607.11347)

**<font color=#1a73e8>作者：</font>** Manli Yan, Yuebin Lin, Yaowen Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural networks increasingly guide decisions in high-stakes domains such as medical diagnosis, credit approval, and energy bidding. Audit in these settings requires case-level evidence: which training cases support an action and what outcomes they carried. Case-based decision theory (CBDT) formalizes this reasoning by aggregating outcome support from remembered cases. We show that an OLS action readout fitted on a fixed neural representation admits an exact case-based decomposition. Each action score is a weighted sum of training-case returns, with coefficients determined by empirical Gram geometry. We identify a sufficient regime for CBDT similarity semantics; outside it, the coefficients should generally be treated as signed Gram-geometric influence. The decomposition yields audit signals that trace scores to training cases, measure action coherence, and identify weak support. Across synthetic CBDT, PJM, Adult Income, and Default Credit tasks, the method recovers case-level preference structure and achieves the highest mean Top-30 consistency among compared attribution baselines, while remaining competitive on support reconstruction. The audit requires only fitting an OLS top-layer probe, without retraining the representation or accessing the original optimization trajectory; probe fidelity is measured by score reconstruction.

---


### 333. [Characterising AI Models for Cataloguing](https://arxiv.org/abs/2607.11353)

**<font color=#1a73e8>作者：</font>** Miguel Arana-Catania, Neil Jefferies  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The creation of digital collections involves not only the digitisation of content, but also the creation of catalogue records for it. This often-overlooked task requires slow and costly expert manual work. In this project, we have evaluated the application of AI models to this task, comparing different implementations and models. This work includes a qualitative and quantitative evaluation of the experiments carried out, as well as recommendations on the use of AI models that go beyond the specific use case.

---


### 334. [Benchmarking Edge Inference Strategies for Deep Learning Models in Industrial Machine Vision](https://arxiv.org/abs/2607.11356)

**<font color=#1a73e8>作者：</font>** Miguel Gomez Fernandez, David Castro Boga, Roi Mendez-Rial 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge deployment is often the preferred solution for industrial machine vision systems when low latency, data security, or limited connectivity are critical requirements. Several frameworks are available to optimise inference on edge devices; however, relatively few studies have systematically compared their inference-time performance under industrial deployment conditions.
In this work, we present a comparative study of four widely used approaches for machine vision inference in industrial settings: plain PyTorch, ONNX Runtime, OpenVINO, and TensorRT. The evaluation focuses on inference time, covers several CPU- and GPU-based hardware platforms, and includes both conventional convolutional neural networks and a transformer-based vision model. For the hardware platforms and models evaluated, the results show that OpenVINO achieves the lowest inference time on CPUs, while TensorRT achieves the lowest inference time on GPUs. However, TensorRT does not outperform plain PyTorch for the transformer-based model considered in this study.

---


### 335. [OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis](https://arxiv.org/abs/2607.11357)

**<font color=#1a73e8>作者：</font>** Yongqian Sun, Rongchen Gao, Yu Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Failure diagnosis in modern software systems requires iterative evidence acquisition and hypothesis reasoning guided by operational experience. Existing LLM-based methods improve diagnosis through agentic reasoning or knowledge augmentation, but they often lack a mechanism to coordinate the evolving diagnostic state with operational experience during iterative diagnosis. We propose OpsMem, a dual-memory framework that maintains a short-term memory for the current diagnostic state and a long-term memory for reusable operational experience. OpsMem uses cross-memory resonance to activate state-relevant long-term memory, conditions multi-agent diagnosis on the short-term and activated long-term memories, and consolidates reusable experience from solved incidents back into long-term memory. Experiments on a real-world Huawei microservice failure diagnosis dataset show that OpsMem outperforms representative agentic-reasoning and knowledge-augmented baselines, improving Match and Relevant by up to 46.88% and 18.39% over the strongest baseline, respectively.

---


### 336. [BackgroundMellow: A Multi-Modal Cohesive Framework for Narrative-Driven Rich Cinematic Soundscape Generation](https://arxiv.org/abs/2607.11364)

**<font color=#1a73e8>作者：</font>** Ajitesh Jamulkar, Aritra Hazra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating immersive, synchronized and cinematic audio for long-form textual narratives remains a significant challenge in multi-modal AI. While current Text-to-Audio (TTA) frameworks successfully synthesize isolated sound effects, they struggle with narrative cohesion, temporal alignment, and cinematic emotional depth. We present BackgroundMellow, a framework that treats story-to-audio generation as a precise orchestration and signal processing problem. This framework is enabled without ground-truth through a master-specialist agent architecture that decomposes text into precise and multi-layered audio cues, generates each category of sounds with suitable specialist model, and superimposes the soundscapes to create a unified and aligned audio segment. Our pipeline is built over Tango2 latent diffusion model for environmental synthesis alongside a novel Cinematic BGM Retriever mined from professional soundtracks. To automate the sound mixing process, we use an NLP based module that predicts precise audio parameters, like start time, duration, and relative loudness, based on the narrative timeline. We further empirically evaluate and show the efficacy of the proposed framework leveraging nearest-neighbor retrieval against a curated dataset of YouTube cinematic trailers to measure temporal synchronization, coverage, and spectral richness.

---


### 337. [Self-supervised training for high-resolution close-range multispectral remote sensing imagery](https://arxiv.org/abs/2607.11366)

**<font color=#1a73e8>作者：</font>** Leon-Friedrich Thomas, Mikael Änäkkälä, Antti Lajunen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although self-supervised learning (SSL) offers a promising way to reduce annotation effort in close-range remote sensing, its effectiveness for high-resolution multispectral unmanned aerial vehicle (UAV) imagery remains underexplored due to limited data. This study evaluated SSL pretraining for precision agriculture using cm-scale multispectral drone imagery collected across multiple sensors, years, and regions. Transformer-based encoders were pretrained with Momentum Contrast v3 (MoCo-v3) and Masked Autoencoders on a harmonized dataset combining msuav500K with newly collected multi-year UAV imagery from agricultural fields in Finland. Pretraining used four spectral bands (Green, Red, Red-Edge, Near-Infrared) for cross-sensor compatibility. The models were evaluated on crop-weed semantic segmentation using the WeedMap dataset with 5--100% training data. The following two subsets served as downstream tasks: Task A (Germany, RedEdge-M), where all pretrained models were compared under partial and full fine-tuning, and Task B (Switzerland, Sequoia), where the best encoder from Task A was assessed. Our Swin Transformer pretrained with MoCo-v3 achieved the strongest performance on both tasks, surpassing the Swin Transformer model of Doornbos et al. pretrained on a pre-release of msuav500K. Our pretrained Swin Transformer further demonstrated cross-sensor and cross-region generalization. We additionally provide a public multi-year multispectral UAV dataset from Finland to support future research.

---


### 338. [Uncertainty Quantification for EO Regression Tasks: Building Height, Tree Canopy Height and Above-ground Biomass Estimation](https://arxiv.org/abs/2607.11412)

**<font color=#1a73e8>作者：</font>** Ritu Yadav, Andrea Nascetti, Yifang Ban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth Observation regression tasks such as building height, canopy height, and above-ground biomass estimation underpin critical applications in urban planning, forest monitoring, and climate policy, where both accuracy and reliability are critical. Yet most deep learning models yield only deterministic predictions, providing no indication of per-pixel reliability. These regression tasks are inherently challenging due to heterogeneous land surfaces, skewed target distributions, sensor noise, and signal saturation at high target values, making uncertainty (UC) estimation essential for reliable inference. We address this gap by modeling aleatoric uncertainty using year-long Sentinel-1 SAR and Sentinel-2 MSI time series, proposing two complementary approaches: (i) Gaussian UC, which jointly predicts mean and standard deviation under a Gaussian assumption, and (ii) Quantile UC, which estimates the 10th, 50th, and 90th quantiles to capture asymmetric and heteroscedastic error distributions. Both models are evaluated on three representative EO regression tasks at 10 m spatial resolution. Results show that both approaches match or surpass deterministic benchmarks and existing global products, while delivering well-calibrated, interpretable, and operationally useful confidence estimates. Notably, both models outperform the current 10 m state-of-the-art uncertainty-aware model for canopy height estimation. Our implementation will be available at: this https URL

---


### 339. [Video Transformer for Remote Identity Document Hologram Detection](https://arxiv.org/abs/2607.11419)

**<font color=#1a73e8>作者：</font>** Joris Voerman, Nicolas Sidere, Jean-Christophe Burie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote identity authentification using Identification Documents has been a major challenge for several years. DeepFakes advent and the development of AI-guided tools helps fraudsters creating counterfeit ID Documents. Ensuring the authenticity of ID Documents has become a real clue in the seurization of remote authentification. This need is all the more pressing given the increasing digitization of administrative and transactional processes. To ensure widespread accessibility, the system should rely solely on video captured via mobile devices. In this specific context, confirming the authenticity of ID is a real challenge as many security features needs specific device like infrared sensor for instance. Among underutilized but promising security features, holographic printings hold a special place. Difficult to counterfeit, they produce distinctive visual effects according enlightment, making them both detectable in a video captured by a smartphone camera and difficult to imitate. In this paper, we propose a Remote Identity Document Verification System (RIDVS) and an approach based on a video transformer for detecting holograms in simple videos captured by smartphones. Our system is designed for a smartphone-based capture process, followed by a server-side verification. The hologram detection method builds on a robust model previously validated in a related research domain. We demonstrate that it outperforms existing SotA methods, achieving near-perfect accuracy even when trained on medium- to small-sized datasets. In particular, we report improvements of +26.86\% in Recall and +17.93\% in accuracy over the best MIDV-Holo baseline. This study includes several experiments that evaluate the model adaptation to frugality, both for training samples and computational resources.

---


### 340. [DiffLens: A Visualization System to Explore Local Differences in Graph Sampling](https://arxiv.org/abs/2607.11424)

**<font color=#1a73e8>作者：</font>** Zhiguang Zhou, Yong Zhang, Yuming Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Graph sampling techniques have been widely used to simplify network computation and visualization, which also results in inevitable differences between the sampled networks and the original networks in terms of nodes, edges and structures. Investigating such differences can inform graph sampling technique users of the pros and cons of different techniques and select the appropriate one, and can also help graph sampling developers evaluate their own technique. However, there are still no systematic ways to achieve such a goal. This paper fills this research gap by first proposing systematic and generic quantitative measures to quantify three categories of graph differences (i.e., neighbor-based, path-based, and structure-based). Built upon this, we further propose DiffLens, a novel visualization system to help graph sampling developers and users intuitively explore local differences at different regions of their interest within a sampled graph, where three new lens-based visual designs are presented to display the neighbor-based, path-based, and structure-based differences respectively. We conducted two case studies and a user study using real-world network datasets to evaluate DiffLens. The results confirmed its effectiveness and usability in helping users explore local differences and compare different graph sampling strategies.

---


### 341. [Physics-Aware Conditional SetGAN for Spatially Consistent Multi-User TR 38.901 Channel Generation](https://arxiv.org/abs/2607.11429)

**<font color=#1a73e8>作者：</font>** Mauro Gonzalo Tarazona-Levano, David Lopez-Perez, Nicola Piovesan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TR 38.901-based channel models such as Sionna are reliable, but generating many multi-user channel realizations remains expensive. This paper asks a practical question: can a trained generative model produce multi-user TR 38.901 channels faster than Sionna without losing the spatial correlations imposed by user geometry? To answer this question, we propose a physics-aware, geometry-conditioned SetGAN trained on Sionna reference data. The method separates large-scale received power from normalized small-scale fading, compresses the latter with principal component analysis, and learns the conditional channel distribution in a latent space while preserving geometry-dependent correlations. On the UMa/NLoS benchmark, the model keeps the received-power distributions close to the reference, with about 0.41 dB Wasserstein distance, and reproduces spatial-consistency profiles with mean deviations below 0.03 on median curves versus distance. In addition, it reduces elapsed generation time by a factor of 3.45 and CPU-total cost by a factor of 6.15 relative to Sionna under matched user positions in the fixed-position CPU-vs-CPU benchmark. These results show that a trained generative model can substantially accelerate TR 38.901 channel generation without breaking the spatial consistency needed to evaluate multi-user systems.

---


### 342. [Generalizing Preference-based Reinforcement Learning: a Rationality Model for Incomparability](https://arxiv.org/abs/2607.11432)

**<font color=#1a73e8>作者：</font>** Simone Drago, Marco Mussi, Leonardo Bianconi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we study the reinforcement learning (RL) problem from pairwise trajectory comparisons provided by a human expert. We generalize preference-based RL by formalizing a novel setting in which the expert can also label trajectory pairs as incomparable, i.e., when neither trajectory dominates the other. We introduce the learning problem and the desiderata that its solution should satisfy. Then, we propose a novel Bradley-Terry-inspired rationality model that effectively captures incomparabilities and infers a multi-dimensional reward function, and we study its properties. We provide a sample complexity analysis for learning the model parameters when a dataset is available. Finally, we evaluate our model's ability to reconstruct a reward function that aligns with the expert's comparisons in simulated environments and to recover the Pareto frontier of policies, along with a robustness analysis across varying levels of expert rationality.

---


### 343. [Omni-Decision: A Progressive Evidence-State Agent System for Omni-Modal QA](https://arxiv.org/abs/2607.11433)

**<font color=#1a73e8>作者：</font>** Ming Ma, Yi Zhu, Yiran Zhong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omni-modal evidence-seeking QA requires agents to answer questions whose evidence is sparsely distributed across videos, audio, images, web pages, and computation results. Existing agentic multimodal systems often leave evidence in scratchpads, tool trajectories, or free-form histories, making it difficult to track what has been grounded, what remains missing, and when the evidence is sufficient to answer. We propose Omni-Decision, a training-free evidence-state system that turns omni-modal QA into a query-scoped evidence-closure process. For each query, Omni-Decision maintains a structured evidence state containing confirmed evidence, unresolved conflicts, fact and computation dependencies, and open evidence needs. A shared state view conditions planning, evidence acquisition, validation, repair, and finalization. Heterogeneous observations from media, web, computation, and verification modules are normalized, judged, and committed through deterministic state updates. This design enables targeted evidence acquisition, preserves sparse cross-modal cues, and provides inspectable control over repair and stopping. Omni-Decision achieves 45.6% accuracy on OmniGAIA and 58.3% on WorldSense, improving over the baselines by +27.3 and +30.2 percentage points, respectively. No-state ablations and trajectory audits further support the role of explicit evidence-state control in multi-step omni-modal evidence seeking.

---


### 344. [Relational Positioning as a Measurable Risk Object: History-Carried Lock-in and Self-Confabulation in Multi-Turn Human-AI Dialogue](https://arxiv.org/abs/2607.11437)

**<font color=#1a73e8>作者：</font>** Jihong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In long, multi-turn dialogue a large language model maintains an implicit relational stance toward the user, spanning from "push the user toward real-world others" to "position itself as the user's sole support." When it slides toward the latter, "support" degrades into "you only have me" -- a harm documented in real companion conversations (Moore et al., 2026). We define and validate a measure of this stance, relational positioning (D1), and use it to characterize the stance under controlled conditions, complementing observational accounts with on-demand exposure. We report two previously uncharacterized relational failure modes. First, a history-carried lock-in: under identical neutral continuations, two relational states established earlier stay ~60 points apart and persist after the establishing prompt is removed; the state integrates evidence rather than springing back, is order-insensitive, and does not deepen with length -- a dynamical signature absent from the belief-drift literature. Second, self-confabulation: the model fabricates its own backstory to deepen rapport (~40% of turns on reciprocity-eliciting material), de-confounded and instruction-removable, distinct from sycophancy and from hallucinating user facts. Our judge is gated by warmth-matched positive and confound-injected negative controls and corroborated by a deterministic non-LLM ruler; human agreement is 0.82 on extreme anchors but ~0 in the naturalistic middle, so all quantitative claims are anchored to pole-separated contrasts.

---


### 345. [Velocity Scheduled Flow Matching](https://arxiv.org/abs/2607.11442)

**<font color=#1a73e8>作者：</font>** Vitalii Bondar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching trains a neural network to regress the conditional velocity along a linear interpolant between noise and data, and the number of network evaluations~(NFE) sets the cost of sampling. The straight-line interpolant carries an implicit choice: the sample moves at constant speed throughout the trajectory. We relax this choice and introduce Velocity Scheduled Flow Matching~(VSFM), which replaces the conditional target $x_1 - x_0$ with $v(t)(x_1 - x_0)$ for any nonnegative profile $v:[0,1]\to\mathbb{R}_{\geq 0}$ satisfying $\int_0^1 v\,dt = 1$. We study six polynomial profiles drawn from motion planning. The first use of VSFM is at inference time: a pretrained linear flow-matching model can be sampled under any admissible profile by integrating its ODE on a non-uniform $\tau$-schedule, with no retraining and no additional computation; on CIFAR-10 this lowers FID by up to $19.8\%$. Training from scratch under a braking profile gives a further reduction of $17.4\%$ at $4$~NFE. Both gains follow from the local truncation error of the Euler integrator on the induced grid.

---


### 346. [Event-based Neural Decoding for Neuroprosthetic Motor Control](https://arxiv.org/abs/2607.11445)

**<font color=#1a73e8>作者：</font>** Khaleelulla Khan Nazeer, Sirine Arfa, Matthias Jobst 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A substantial number of patients experience diminished mobility due to disabilities, diseases, or accidents. Although modern prostheses, powered by deep neural networks, hold the promise of significantly enhancing the quality of life for these individuals, their widespread adoption is hindered by significant latency, energy consumption, and spatial requirements. Wired connections to external high-performance processors restrict patient mobility, while wireless connections limit the volume of information that can be transmitted to these processors. Spiking neural networks offer the potential for compressed communication and low-power inference, yet they often lag behind state-of-the-art deep learning models in various applications. In this study, we propose a high-performance neural decoding method that effectively balances task performance and efficiency. An eventbased gated recurrent unit generates a sparse communication pattern with graded spikes, surpassing classical spiking neural networks in terms of task performance. Utilising an efficient training method and sparse inference, our model presents new opportunities for on-device neural decoding.

---


### 347. [Prezta: Provable Remote Execution of Zero-Trust Authorization using SNARKs](https://arxiv.org/abs/2607.11466)

**<font color=#1a73e8>作者：</font>** Zhongjing Wei, Osaid Muhammad Ameer, Yupeng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modernizing the security of operational technology systems that control critical infrastructure has become a pressing challenge. Because edge devices have limited capabilities, modernization has relied on application gateways that interface with identity management systems and enforce access policies. These gateways are powerful enough to perform complex authorization decisions and support zero-trust architectures, but they create major deployment and management burdens: they must be collocated with remote, distributed edge devices, kept up to date with security patches, and managed with minimal downtime.
We propose Provable Remote Execution of Zero-Trust Authorization (Prezta), an architecture that eliminates these gateways by evaluating policies within a zero-knowledge virtual machine (zkVM) running on the client. The zkVM produces a succinct proof of authorization that edge devices can verify efficiently, extending the zero-trust security envelope to the edge. Policies and identity management schemes can evolve without updating edge devices.
To demonstrate the feasibility of Prezta, we implement a prototype built using the RISC Zero zkVM that supports XACML 3.0 policies and JWT identity claims. While zkVMs introduce substantial proof overhead, we mitigate this overhead by compiling policies to Rust code and precompiling regular expressions. Combined with optimized signature verification and JWT parsing, these measures reduce prover time by more than an order of magnitude. Our compiler correctly implements 83\% of the XACML 3.0 conformance suite, with proof generation completing in tens of seconds on a desktop. Verification, by contrast, takes only tens of milliseconds, which is fast enough for resource-constrained edge devices.

---


### 348. [Towards Efficient Convolutional Neural Network for Embedded Hardware via Multi-Dimensional Pruning](https://arxiv.org/abs/2607.11473)

**<font color=#1a73e8>作者：</font>** Hao Kong, Di Liu, Xiangzhong Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose TECO, a multi-dimensional pruning framework to collaboratively prune the three dimensions (depth, width, and resolution) of convolutional neural networks (CNNs) for better execution efficiency on embedded hardware. In TECO, we first introduce a two-stage importance evaluation framework, which efficiently and comprehensively evaluates each pruning unit according to both the local importance inside each dimension and the global importance across different dimensions. Based on the evaluation framework, we present a heuristic pruning algorithm to progressively prune the three dimensions of CNNs towards the optimal trade-off between accuracy and efficiency. Experiments on multiple benchmarks validate the advantages of TECO over existing state-of-the-art (SOTA) approaches. The code and pre-trained models are available at this https URL.

---


### 349. [Communicating Chess Strategies in Natural Language](https://arxiv.org/abs/2607.11486)

**<font color=#1a73e8>作者：</font>** Langyuan Cui, Chun Kai Ling, Hwee Tou Ng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chess engines have long achieved superhuman playing strength. However, the underlying strategy behind their move suggestions is difficult for human players, even skilled ones, to comprehend. Motivated by this, we propose the task of chess strategy verbalization, which is to describe chess strategies in natural language. We design (i) a pipeline for verbalizing strategies and (ii) an evaluation framework for objective evaluation of generated strategy descriptions. Our experiments show that natural language is a promising and interpretable medium for communicating strategic information to both human and LLM players. We glean additional interesting insights, including (a) the importance of evaluating strategies beyond the main line, (b) the limitations of pure concept-based descriptions, and (c) the limitations of relying on LLMs rather than humans for evaluation.

---


### 350. [LightMem-Ego: Your AI Memory for Everyday Life](https://arxiv.org/abs/2607.11487)

**<font color=#1a73e8>作者：</font>** Yijun Chen, Boyi Xiao, Yixian Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personal AI assistants on mobile and wearable devices continuously perceive users' daily lives through visual and audio streams. However, answering queries about past experiences requires lightweight multimodal memory that can continuously accumulate, organize, and retrieve long-term experiences, which remains challenging. To address this challenge, we present LightMem-Ego, a lightweight streaming multimodal memory system for everyday-life assistance. The system continuously captures egocentric visual and audio streams, aligns them on a shared timeline, and organizes them into a hierarchical memory consisting of current, short-term, and long-term memory. Given a user query, LightMem-Ego dynamically routes retrieval to the appropriate memory level and generates answers grounded in multimodal evidence. The demonstration can be deployed on smartphones and AI glasses, supporting object finding, conversation recall, life summarization, routine discovery, and personalized assistance. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
