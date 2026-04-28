# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

---

### 101. [A Layer Separation Optimization Framework for Cross-Entropy Training in Deep Learning](https://arxiv.org/abs/2604.23225)

**<font color=#1a73e8>作者：</font>** Yaru Liu, Michael K. Ng, Yiqi Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates the deep learning optimization problem with softmax cross-entropy loss. We propose a layer separation strategy to alleviate the strong nonconvexity encountered during training deep networks. For cross-entropy models with fully connected and convolutional neural networks, we introduce auxiliary variables associated with hidden layer outputs and construct corresponding layer separation models, which decompose the original deeply nested optimization problem into a sequence of more manageable subproblems. We also conduct theoretical analyses, proving that the new layer separation loss provides an upper bound for the original cross-entropy loss. Moreover, we design alternating minimization algorithms and prove that, under appropriate conditions, these algorithms exhibit decreasing properties of the loss function. Numerical experiments validate the effectiveness of the proposed methods and indicate improved optimization behavior, especially for fully connected and convolutional neural networks.

---


### 102. [Toward Polymorphic Backdoor against Semantic Communication via Intensity-Based Poisoning](https://arxiv.org/abs/2604.23231)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Yuni Lai, Gaolei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic Communication (SC) backdoor attacks aim to utilize triggers to manipulate the system into producing predetermined outputs via backdoored shared knowledge. Current SC backdoors adopt monomorphic paradigms with single attack target, which suffers from limited attack diversity, efficiency, and flexibility in heterogeneous downstream scenarios. To overcome the limitations, we propose SemBugger, a polymorphic SC backdoor. By dynamically adjusting the trigger intensity, SemBugger finely-grained controls over the SC knowledge to generate diverse malicious results from the system. Specifically, SemBugger is realized through a multi-effect poisoning-training framework. It introduces graded-intensity triggers to poison training data and optimizes SC systems with hierarchical malicious loss. The trained system's knowledge dynamically adapts to trigger intensity in inputs to yield target outputs, all while preserving transmission fidelity for benign samples. Moreover, to augment SC security, we propose a provable robustness defense that resists SemBugger's homogeneous attacks through a controlled noise mechanism. It operates via strategically adding noise in SC inputs, and we formally provide a theoretical lower bound on the defense efficacy. Experiments across diverse SC models and benchmark datasets indicate that SemBugger attains high attack efficacy while maintaining the regular functionality of SC systems. Meanwhile, the designed defense effectively neutralizes SemBugger attacks.

---


### 103. [Protecting the Trace: A Principled Black-Box Approach Against Distillation Attacks](https://arxiv.org/abs/2604.23238)

**<font color=#1a73e8>作者：</font>** Max Hartman, Vidhata Jayaraman, Moulik Choraria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier models push the boundaries of what is learnable at extreme computational costs, yet distillation via sampling reasoning traces exposes closed-source frontier models to adversarial third parties who can bypass their guardrails and misappropriate their capabilities, raising safety, security, and intellectual privacy concerns. To address this, there is growing interest in building antidistillation methods, which aim to poison reasoning traces to hinder downstream student model learning while maintaining teacher performance. However, current techniques lack theoretical grounding, requiring either heavy fine-tuning or access to student model proxies for gradient based attacks, and often lead to a significant teacher performance degradation. In this work, we present a theoretical formulation of antidistillation as a Stackelberg game, grounding a problem that has so far largely been approached heuristically. Guided by the desired design properties our formulation reveals, we propose \texttt{TraceGuard}, an efficient, post-generation black-box method to poison sentences with high importance for teacher reasoning. Our work offers a scalable solution to share model insights safely, ensuring that the advancement of reasoning capabilities does not come at the cost of intellectual privacy or AI safety alignment.

---


### 104. [AdaMamba: Adaptive Frequency-Gated Mamba for Long-Term Time Series Forecasting](https://arxiv.org/abs/2604.23239)

**<font color=#1a73e8>作者：</font>** Xudong Jiang, Mingshan Loo, Hanchen Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate long-term time series forecasting (LTSF) requires the capture of complex long-range dependencies and dynamic periodic patterns. Recent advances in frequency-domain analysis offer a global perspective for uncovering temporal characteristics. However, real-world time series often exhibit pronounced cross-domain heterogeneity where variables that appear synchronized in the time domain can differ substantially in the frequency domain. Existing frequency-based LTSF methods often rely on implicit assumptions of cross-domain homogeneity, which limits their ability to adapt to such intricate variability. To effectively integrate frequency-domain analysis with temporal dependency learning, we propose AdaMamba, a novel framework that endogenizes adaptive and context-aware frequency analysis within the Mamba state-space update process. Specifically, AdaMamba introduces an interactive patch encoding module to capture inter-variable interaction dynamics. Then, we develop an adaptive frequency-gated state-space module that generates input-dependent frequency bases, and generalizes the conventional temporal forgetting gate into a unified time-frequency forgetting gate. This allows dynamic calibration of state transitions based on learned frequency-domain importance, while preserving Mamba's capability in modeling long-range dependencies. Extensive experiments on seven public LTSF benchmarks and two domain-specific datasets demonstrate that AdaMamba consistently outperforms state-of-the-art methods in forecasting accu racy while maintaining competitive computational efficiency. The code of AdaMamba is available at this https URL.

---


### 105. [Training Machine Learning Models on Encrypted Data: A Privacy-Preserving Framework using Homomorphic Encryption](https://arxiv.org/abs/2604.23245)

**<font color=#1a73e8>作者：</font>** Alexandre Marques, Beatriz Sá, Rui Botelho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The use of Machine Learning (ML) for data-driven decision-making often relies on access to sensitive datasets, which introduces privacy challenges. Traditional encryption methods protect data at rest or in transit but fail to secure it during processing, exposing it to unauthorized access. Homomorphic encryption emerges as a transformative solution, enabling computations on encrypted data without decryption, thus preserving confidentiality throughout the ML pipeline. This paper addresses the challenge of training ML models on encrypted data while maintaining accuracy and efficiency by proposing a proof-of-concept for a privacy-preserving framework that leverages Cheon-Kim-Kim-Song (CKKS) for approximate real-number arithmetic. Also, it demonstrates the feasibility of training K-Nearest Neighbors (KNN) and linear regression models on encrypted data, and evaluates encrypted inference for a basic Multilayer Perceptron (MLP) architecture. Experimental results show that models trained under Homomorphic encryption achieve performance metrics comparable to plaintext-trained models, validating the approach. However, challenges such as computational overhead, noise management, and limited support for non-polynomial operations persist. This work lays the groundwork for broader adoption of privacy-preserving ML in real-world applications, balancing security with computational feasibility.

---


### 106. [Micro-Expression-Aware Avatar Fingerprinting via Inter-Frame Feature Differencing](https://arxiv.org/abs/2604.23247)

**<font color=#1a73e8>作者：</font>** Masoumeh Chapariniya, Jean-Marc Odobez, Volker Dellwo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Avatar fingerprinting, i.e., verifying who drives a synthetic talking-head video rather than whether it is real, is a critical safeguard for authorized use of face-reenactment technology. Existing methods rely on a fixed, non-differentiable landmark extraction stage that prevents the fingerprinting model from being optimized end-to-end from raw pixels. We propose a preprocessing-free system built on a micro-expression-aware backbone operating on raw video frames, with inter-frame feature differencing as the core design principle: consecutive feature maps are subtracted in the learned deep feature space, so that temporally stable appearance dimensions contribute zero to the output while driver-specific motion dynamics are preserved. A controlled ablation on NVFAIR confirms that temporal motion accounts for the large majority of discriminative performance, and that raw appearance features actively degrade identity separation. Both the choice of backbone and the differencing principle are essential: differencing alone is insufficient when applied to a generic encoder, as appearance-dominated features collapse to near-identical representations across adjacent frames, while the micro-expression-aware F5C backbone retains measurable motion variation that the differencing operation can exploit. Without any external preprocessing, our model achieves an overall AUC of 0.877 on NVFAIR and matches or exceeds the landmark-based baseline on the majority of cross-generator pairs.

---


### 107. [PrivacyAssist: A User-Centric Agent Framework for Detecting Privacy Inconsistencies in Android Apps](https://arxiv.org/abs/2604.23248)

**<font color=#1a73e8>作者：</font>** Tran Thanh Lam Nguyen, Edoardo Di Tullio, Barbara Carminati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile apps offer significant benefits, but their privacy protections often remain ineffective and confusing for users. While prior work mainly analyzes app privacy vulnerabilities, few approaches help users understand, set, and enforce their privacy preferences. This paper presents PrivacyAssist, a multi-agent LLM-based platform that detects inconsistencies between user-granted permissions and developers' declared sensitive data collection and sharing practices. Using Retrieval-Augmented Generation (RAG), PrivacyAssist provides concise explanations and real-time on-device warnings to support informed installation decisions. We evaluate PrivacyAssist with 200 users and 2,347 Android apps, finding that only 16% of apps are fully consistent between granted permissions and declared data practices.

---


### 108. [MotionHiFlow: Text-to-motion via hierarchical flow matching](https://arxiv.org/abs/2604.23264)

**<font color=#1a73e8>作者：</font>** Heng Li, Xiaotong Lin, Ling-An Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation aims to generate 3D human motions that are tightly aligned with the input text while remaining physically plausible and rich in fine-grained detail. Although recent approaches can produce complex and natural movements, they usually operate at only one temporal scale, which limits both semantic alignment and temporal coherence. Inspired by the fact that complex motions are conceptualized hierarchically rather than at a single temporal scale in the human cognitive system, we propose \textit{MotionHiFlow}, a hierarchical flow matching framework to generate motion progressively by constructing flow path from low to high temporal scales. The flows at lower scales capture high-level semantics and coarse motion structures, while flows at higher scales refine temporal details. To link the flows across scales, we introduce a novel cross-scale transition process, ensuring continuity and preserving noise consistency. Furthermore, by integrating a Text-Motion Diffusion Transformer and a topology-aware Motion VAE, MotionHiFlow explicitly models structural dependencies among joints via joint-aware positional encoding and skeletal topology, enabling precise semantic alignment alongside fine-grained motion details. Extensive experiments on HumanML3D and KIT-ML benchmarks demonstrate state-of-the-art performance, with ablation studies confirming the effectiveness of the hierarchical design and key components. Code is available at this https URL.

---


### 109. [LatentBurst: A Fast and Efficient Multi Frame Super-Resolution for Hexadeca-Bayer Pattern CIS images](https://arxiv.org/abs/2604.23268)

**<font color=#1a73e8>作者：</font>** Sangwook Baek, Vin Van Duong, Karam Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a novel multi frame super-resolution network (MFSR) for burst hexadeca Bayer pattern Contact Image Sensor (CIS) images, which includes demosaicing, denoising, multi-frame fusion, and super-resolution. Designing a high-quality reconstruction network poses several challenges as follows: 1) Unlike the Bayer color filter array (CFA) pattern, it is hard to interpolate hexadeca-Bayer pattern since the pixel distance between the same color groups increases; 2) Due to large object motion and camera movements, the final fusion result usually suffers the misalignment resulting a blurry image or ghosting artifacts; 3) The proposed network should be fast and efficient enough to operate in real-time on mobile devices. To overcome these challenges, we propose a novel network, called LatentBurst, which contains: 1) a pyramid align and fusion approach in latent feature to deal with large motion scenario; 2) an efficient UNet-based structure which can run efficiently on mobile device; 3) fine-tuned optical flow estimation and two-step knowledge distillation to reduce domain-gap more effectively. Experimental results in various scenarios demonstrate the effectiveness of our proposed method compared with other state-of-the-art methods.

---


### 110. [A Hierarchical Ensemble Inference Pipeline for Robust White Blood Cell Classification Under Domain Shifts](https://arxiv.org/abs/2604.23271)

**<font color=#1a73e8>作者：</font>** Ruyi Dai, Tingkwong Ng, Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated white blood cell (WBC) classification is essential for scalable leukaemia screening. However, real-world deployment is challenged by domain shifts caused by staining protocols, scanner characteristics, and inter-laboratory variability, which often degrade model performance. The White Blood Cell Classification Challenge (WBCBench) at ISBI 2026 aims to advance robust WBC recognition, with a focus on accurately identifying blast cells and other clinically critical rare subtypes. We propose a memory-augmented, hierarchical ensemble pipeline for WBC classification under domain shifts, leveraging a feature bank and a DinoBloom backbone fine-tuned with LoRA. Our three-stage inference hierarchy combines k-nearest neighbors (kNN) retrieval at each level, reducing over-reliance on any single decision. Evaluated on the WBCBench dataset, our method ranks within the top ten by macro F1-score in the final testing phase.

---


### 111. [Active Inference: A method for Phenotyping Agency in AI systems?](https://arxiv.org/abs/2604.23278)

**<font color=#1a73e8>作者：</font>** Philip Wilson, Axel Constant, Mahault Albarracin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of agentic artificial intelligence has outpaced the conceptual tools needed to characterize agency in computational systems. Prevailing definitions mainly rely on autonomy and goal-directedness. Here, we argue for a minimal notion open to principled inspection given three criteria: intentionality as action grounded in beliefs and desires, rationality as normatively coherent action entailed by a world model, and explainability as action causally traceable to internal states; we subsequently instantiate these as a partially observable Markov decision process under a variational framework wherein posterior beliefs, prior preferences, and the minimization of expected free energy jointly constitute an agentic action chain. Using a canonical T-maze paradigm, we evidence how empowerment, formulated as the channel capacity between actions and anticipated observations, serves as an operational metric that distinguishes zero-, intermediate-, and high-agency phenotypes through structural manipulations of the generative model. We conclude by arguing that as agents engage in epistemic foraging to resolve ambiguity, the governance controls that remain effective must shift systematically from external constraints to the internal modulation of prior preferences, offering a principled, variational bridge from computational phenotyping to AI governance strategy

---


### 112. [AI Identity: Standards, Gaps, and Research Directions for AI Agents](https://arxiv.org/abs/2604.23280)

**<font color=#1a73e8>作者：</font>** Takumi Otsuka, Kentaroh Toyoda, Alex Leung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are now running real transactions, workflows, and sub-agent chains across organizational boundaries without continuous human supervision. This creates a problem no current infrastructure is equipped to solve: how do you identify, verify, and hold accountable an entity with no body, no persistent memory, and no legal standing? We define AI Identity as the continuous relationship between what an AI agent is declared to be and what it is observed to do, bounded by the confidence that those two things correspond at any given moment. Through a structured survey of industry trends, emerging standards, and technical literature, we conduct a gap analysis across the full agent identity lifecycle and make three contributions: (1) a structural comparison of human and AI identity across four dimensions (substrate, persistence, verifiability, and legal standing) showing that the asymmetry is fundamental and that extending human frameworks to agents without structural modification produces systematic failures; (2) an evaluation of current technical and regulatory documents against the identity requirements of autonomous agents, finding that none adequately address the challenge of governing nondeterministic, boundary-crossing entities; and (3) identification of five critical gaps (semantic intent verification, recursive delegation accountability, agent identity integrity, governance opacity and enforcement, and operational sustainability) that no current technology or regulatory instrument resolves. These gaps are structural; more engineering effort alone will not close them. Foundational research on AI identity is the central conclusion of this report.

---


### 113. [MetaErr: Towards Predicting Error Patterns in Deep Neural Networks](https://arxiv.org/abs/2604.23289)

**<font color=#1a73e8>作者：</font>** Varun Totakura, Shayok Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the unprecedented success of deep learning, it has become an integral component in several multimedia computing applications in todays world. Unfortunately, deep learning systems are not perfect and can fail, sometimes abruptly, without prior warning or explanation. While reducing the error rate of deep neural networks has been the primary focus of the multimedia community, the problem of predicting when a deep learning system is going to fail has received significantly less research attention. In this paper, we propose a simple yet effective framework, MetaErr, to address this under-explored problem in deep learning research. We train a meta-model whose goal is to predict whether a base deep neural network will succeed or fail in predicting a particular data sample, by observing the base models performance on a given learning task. The meta-model is completely agnostic of the architecture and training parameters of the base model. Such an error prediction system can be immensely useful in a variety of smart multimedia applications. Our empirical studies corroborate the promise and potential of our framework against competing baselines. We further demonstrate the usefulness of our framework to improve the performance of pseudo-labeling-based semi-supervised learning, and show that MetaErr outperforms several strong baselines on three benchmark computer vision datasets.

---


### 114. [An Analysis of Active Learning Algorithms using Real-World Crowd-sourced Text Annotations](https://arxiv.org/abs/2604.23290)

**<font color=#1a73e8>作者：</font>** Varun Totakura, Ankita Singh, Yushun Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning algorithms automatically identify the most informative samples from large amounts of unlabeled data and tremendously reduce human annotation effort in inducing a machine learning model. In a conventional active learning setup, the labeling oracles are assumed to be infallible, that is, they always provide correct answers (in terms of class labels) to the queried unlabeled instances, which cannot be guaranteed in real-world applications. To this end, a body of research has focused on the development of active learning algorithms in the presence of imperfect / noisy oracles. Existing research on active learning with noisy oracles typically simulate the oracles using machine learning models; however, real-world situations are much more challenging, and using ML models to simulate the annotation patterns may not appropriately capture the nuances of real-world annotation challenges. In this research, we first collect annotations of text samples (from 3 benchmark text classification datasets) from crowd-sourced workers through a crowd-sourcing platform. We then conduct extensive empirical studies of 8 commonly used active learning techniques (in conjunction with deep neural networks) using the obtained annotations. Our analyses sheds light on the performance of these techniques under real-world challenges, where annotators can provide incorrect labels, and can also refuse to provide labels. We hope this research will provide valuable insights that will be useful for the deployment of deep active learning systems in real-world applications. The obtained annotations can be accessed at this https URL.

---


### 115. [Human-1 by Josh Talks: A Full-Duplex Conversational Modeling Framework in Hindi using Real-World Conversations](https://arxiv.org/abs/2604.23295)

**<font color=#1a73e8>作者：</font>** Bhaskar Singh, Shobhit Banga, Pranav Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue systems can model natural conversational behaviours such as interruptions, overlaps, and backchannels, yet such systems remain largely unexplored for Indian languages. We present the first open, reproducible full-duplex spoken dialogue system for Hindi by adapting Moshi, a state-of-the-art duplex speech architecture, using a custom Hindi tokeniser and training on 26,000 hours of real spontaneous conversations collected from 14,695 speakers with separate speaker channels, enabling direct learning of turn-taking and overlap patterns from natural interactions. To support Hindi text generation, we replace the original English tokeniser and reinitialise text-vocabulary-dependent parameters while retaining the pre-trained audio components. We propose a two-stage training recipe -- large-scale pre-training followed by fine-tuning on 1,000 hours of conversational data. Evaluation through the prompted dialogue continuation paradigm with both automatic metrics and human judgments demonstrates that the resulting model generates natural and meaningful full-duplex conversational behaviour in Hindi. This work serves as a first step toward real-time duplex spoken dialogue systems for Hindi and other Indian languages.

---


### 116. [Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation](https://arxiv.org/abs/2604.23299)

**<font color=#1a73e8>作者：</font>** Can Liu, Sizhe Cheng, Feng Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rise of mobile-first consumption, users increasingly engage with data visualizations on mobile devices. However, the vast majority of existing visualizations are originally authored for desktop environments. Due to significant differences in viewport size and interaction paradigms, directly scaling desktop charts often results in illegible text, information loss, and interaction failures. To bridge this gap, we propose an automated framework to adapt desktop-based visualizations for mobile screens. By systematically categorizing the operations involved in the adaptation process, we establish a multi-level design space. This space defines evolution rules spanning from the global topology level, through the reference frame level, down to the visual elements level. Guided by this theoretical framework, we developed Proteus, a large language model-driven multi-agent system that automatically parses online visualizations, predicts optimal transformation strategies within the design space, and generates equivalent, highly readable visualizations for mobile devices. Case studies and an in-depth user study with 12 participants demonstrate the effectiveness and usability of Proteus.

---


### 117. [CombiMOTS: Combinatorial Multi-Objective Tree Search for Dual-Target Molecule Generation](https://arxiv.org/abs/2604.23307)

**<font color=#1a73e8>作者：</font>** Thibaud Southiratn, Bonil Koo, Yijingxiu Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dual-target molecule generation, which focuses on discovering compounds capable of interacting with two target proteins, has garnered significant attention due to its potential for improving therapeutic efficiency, safety and resistance mitigation. Existing approaches face two critical challenges. First, by simplifying the complex dual-target optimization problem to scalarized combinations of individual objectives, they fail to capture important trade-offs between target engagement and molecular properties. Second, they typically do not integrate synthetic planning into the generative process. This highlights a need for more appropriate objective function design and synthesis-aware methodologies tailored to the dual-target molecule generation task. In this work, we propose CombiMOTS, a Pareto Monte Carlo Tree Search (PMCTS) framework that generates dual-target molecules. CombiMOTS is designed to explore a synthesizable fragment space while employing vectorized optimization constraints to encapsulate target affinity and physicochemical properties. Extensive experiments on real-world databases demonstrate that CombiMOTS produces novel dual-target molecules with high docking scores, enhanced diversity, and balanced pharmacological characteristics, showcasing its potential as a powerful tool for dual-target drug discovery. The code and data is accessible through this https URL.

---


### 118. [CODA: Coordination via On-Policy Diffusion for Multi-Agent Offline Reinforcement Learning](https://arxiv.org/abs/2604.23308)

**<font color=#1a73e8>作者：</font>** Marcel Hedman, Kale-ab Abebe Tessera, Juan Claude Formanek 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-agent reinforcement learning (MARL) enables policy learning from fixed datasets, but is prone to coordination failure: agents trained on static, off-policy data converge to suboptimal joint behaviours because they cannot co-adapt as their policies change. We introduce CODA (Coordination via On-Policy Diffusion for Multi-Agent Reinforcement Learning), a diffusion-based multi-agent trajectory generator for data augmentation that samples conditioned on the current joint policy, producing synthetic experience which reflects the evolving behaviours of the agents, thereby providing a mechanism for co-adaptation. We find that previous diffusion-based augmentation approaches are insufficient for fostering multi-agent coordination because they produce static augmented datasets that do not evolve as the current joint policy changes during training; CODA resolves this by more closely simulating on-policy learning and is a meaningful step toward coordinated behaviours in the offline setting. CODA is algorithm-agnostic and can be layered onto both model-free and model-based offline reinforcement learning pipelines as an augmentation module. Empirically, CODA not only resolves canonical coordination pathologies in continuous polynomial games but also delivers strong results on the more complex MaMuJoCo continuous-control benchmarks.

---


### 119. [STAND: Semantic Anchoring Constraint with Dual-Granularity Disambiguation for Remote Sensing Image Change Captioning](https://arxiv.org/abs/2604.23309)

**<font color=#1a73e8>作者：</font>** Yanpei Gong, Beichen Zhang, Hao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image change captioning (RSICC) aims to describe the difference between two remote sensing images. While recent methods have explored video modeling, they largely overlook the inherent ambiguities in viewpoint, scale, and prior knowledge, lacking effective constraints on the encoder. In this paper, we present STAND, a Semantic Anchoring Constraint with Dual-Granularity Disambiguation for RSICC, to progressively resolve these ambiguities. Specifically, to establish a reliable feature foundation, we first introduce an interpretable constraint to regularize temporal representations. Operating on these purified features, a dual-granularity disambiguation module resolves spatial uncertainties by coupling macro-level global context aggregation for viewpoint confusion with micro-level frequency-refocused attention for small-object scale enhancement. Ultimately, to translate these visually disambiguated features into precise text, a semantic concept anchoring module leverages language categorical priors to tackle knowledge ambiguity during decoding. Extensive experiments verify the superiority of STAND and its effectiveness in addressing ambiguities.

---


### 120. [GIFT: Global stabilisation via Intrinsic Fine Tuning](https://arxiv.org/abs/2604.23312)

**<font color=#1a73e8>作者：</font>** Rory Young, Nicolas Pugeault  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning policies achieve strong performance in complex continuous control environments with nonlinear contact forces. However, these policies often produce chaotic state dynamics, with trivially small changes to the initial conditions significantly impacting the long-term behaviour of the control system. This high sensitivity to initial conditions limits the application of Deep RL to real-world control systems where performance and stability guarantees are often required. To address this issue, we propose Global stabilisation via Intrinsic Fine Tuning (GIFT), a general-purpose training framework which directly optimises the global stability of existing high-performing deep RL policies using a custom reward function. We demonstrate that GIFT increase the stability of the control interaction while maintaining comparable task performance, thereby improving the suitability of deep RL policies for real-world control systems.

---


### 121. [Learning from Noisy Prompts: Saliency-Guided Prompt Distillation for Robust Segmentation with SAM](https://arxiv.org/abs/2604.23314)

**<font color=#1a73e8>作者：</font>** Jingxuan Kang, Ziqi Zhang, Shaoming Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation is central to clinical diagnosis and monitoring, yet the reliability of modern foundation models in medical imaging still depends on the availability of precise prompts. The Segment Anything Model (SAM) offers powerful zero-shot capabilities, although it collapses under the weak, generic, and noisy prompts that dominate real clinical workflows. In practice, annotations such as centerline points are coarse and ambiguous, often drifting across neighboring anatomy and misguiding SAM toward inconsistent or incomplete masks. We introduce SPD, a Saliency-Guided Prompt Distillation framework that converts these unreliable cues into robust guidance. SPD first learns data-driven anatomical priors through a lightweight saliency head to obtain confident localization maps. These priors then drive Contextual Prompt Distillation, which validates and enriches noisy prompts using cues from anatomically adjacent slices, producing a consensus prompt set that matches the behavior of expert reasoning. A Pairwise Slice Consistency objective further enforces local anatomical coherence during segmentation. Experiments on four challenging MRI and CT benchmarks demonstrate that SPD consistently outperforms existing SAM adaptations and supervised baselines, delivering large gains in both region-based and boundary-based metrics. SPD provides a practical and principled path toward reliable foundation model deployment in clinical environments where only imperfect prompts are available.

---


### 122. [Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance](https://arxiv.org/abs/2604.23318)

**<font color=#1a73e8>作者：</font>** Xinzhu Chen, Wei He, Huichuan Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) performs coarse-grained credit assignment in reinforcement learning with verifiable rewards (RLVR) by assigning the same advantage to all tokens in a rollout. Process reward models can provide finer-grained supervision, but they require step-level annotation or additional reward modeling. We show that hidden-state distributions contain a useful signal for local reasoning quality that can be extracted using only outcome-level correctness labels available in RLVR. Specifically, within each GRPO group, the Wasserstein distance between span-level hidden state distributions of correct and incorrect rollouts increases around regions where their local reasoning quality diverges. This association holds both across examples and within individual trajectories, suggesting that hidden-state distributional divergence can serve as a self-supervision signal for fine-grained credit assignment. We formalize this observation with a separation theorem showing that, under mild structural assumptions, post-divergence spans have larger Wasserstein distances than pre-divergence spans whenever the population-level distributional gap exceeds finite-sample noise. Motivated by this result, we propose \textbf{S}pan-level \textbf{H}idden state \textbf{E}nabled \textbf{A}dvantage \textbf{R}eweighting (SHEAR), which modifies GRPO by using span-level Wasserstein distances to scale token-level advantages, amplifying updates on tokens whose hidden states are more separated from the opposing group. The method requires no additional model and only minimal changes to the training pipeline. Experiments on five mathematical reasoning benchmarks and five code generation benchmarks show improvements over standard GRPO and strong performance relative to supervised process reward models, while requiring no additional annotation or reward model training.

---


### 123. [KAConvNet: Kolmogorov-Arnold Convolutional Networks for Vision Recognition](https://arxiv.org/abs/2604.23320)

**<font color=#1a73e8>作者：</font>** Zhaoxiang Liu, Zhicheng Ma, Kaikai Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Convolutional Neural Networks (CNNs) have been the dominant and effective approach for general computer vision tasks. Recently, Kolmogorov-Arnold neural networks (KANs), based on the Kolmogorov-Arnold representation theorem, have shown potential to replace Multi-Layer Perceptrons (MLPs) in deep learning. KANs, which use learnable nonlinear activations on edges and simple summation on nodes, offer fewer parameters and greater explainability compared to MLPs. However, there has been limited exploration of integrating the Kolmogorov-Arnold representation theorem with convolutional methods for computer vision tasks. Existing attempts have merely replaced learnable activation functions with weights, undermining KANs' theoretical foundation and limiting their potential effectiveness. Additionally, the B-spline curves used in KANs suffer from computational inefficiency and a tendency to overfit. In this paper, we propose a novel Kolmogorov-Arnold Convolutional Layer that deeply integrates the Kolmogorov-Arnold representation theorem with convolution. This layer provides stronger method interpretability because it is based on established mathematical theorems and its design has theoretical alignment. Building on the Kolmogorov-Arnold Convolutional Layer, we design an efficient network architecture called KAConvNet, which outperforms existing methods combining KAN and convolution, and achieves competitive performance compared to mainstream ViTs and CNNs. We believe that our work offers valuable insight into the field of artificial intelligence and will inspire the development of more innovative CNNs in the 2020s. The code is publicly available at this https URL.

---


### 124. [Robust Audio-Text Retrieval via Cross-Modal Attention and Hybrid Loss](https://arxiv.org/abs/2604.23323)

**<font color=#1a73e8>作者：</font>** Meizhu Liu, Matthew Rowe, Amit Agarwal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio-text retrieval enables semantic alignment between audio content and natural language queries, supporting applications in multimedia search, accessibility, and surveillance. However, current state-of-the-art approaches struggle with long, noisy, and weakly labeled audio due to their reliance on contrastive learning and large-batch training. We propose a novel multimodal retrieval framework that refines audio and text embeddings using a cross-modal embedding refinement module combining transformer-based projection, linear mapping, and bidirectional attention. To further improve robustness, we introduce a hybrid loss function blending cosine similarity, $\mathcal{L}_{1}$, and contrastive objectives, enabling stable training even under small-batch constraints. Our approach efficiently handles long-form and noisy audio (SNR 5 to 15) via silence-aware chunking and attention-based pooling. Experiments on benchmark datasets demonstrate improvements over prior methods.

---


### 125. [Layer Embedding Deep Fusion Graph Neural Network](https://arxiv.org/abs/2604.23324)

**<font color=#1a73e8>作者：</font>** Taihua Xu, Genhao Tian, Jicong Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have demonstrated impressive performance in learning representations from graph-structured data. However, their message-passing mechanism inherently relies on the assumption of label consistency among connected nodes, limiting their applicability to low-homophily settings. Moreover, since message passing operates as a hierarchical diffusion process, GNNs face challenges in capturing long-range dependencies. As network depth increases, the structural noise along heterophilic edges tends to be amplified, resulting in over-smoothing. This issue becomes especially prominent in highly heterophilic graphs, where the propagation of inconsistent semantics across the topology continually exacerbates misaggregation. To address this issue, we propose a novel framework named Layer Embedding Deep Fusion Graph Neural Network (LEDF-GNN). Specifically, we design a Layer Embedding Deep Fusion (LEDF) operator that nonlinearly fuses multi-layer embeddings to capture inter-layer dependencies and effectively alleviate deep propagation degradation. Meanwhile, to mitigate structural heterophily, LEDF-GNN employs a Dual-Topology Parallel Strategy (DTPS) that simultaneously leverages the original and reconstructed topologies, allowing for adaptive structure-semantics co-optimization under diverse homophily conditions. Extensive semi-supervised classification experiments on the citation and image benchmarks demonstrate that, under both homophilic and heterophilic settings, LEDF-GNN consistently outperforms state-of-the-art baselines, validating its effectiveness and generalization capability across diverse graph types.

---


### 126. [EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325)

**<font color=#1a73e8>作者：</font>** Yahui Li, Yinfeng Yu, Liejun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotionally talking head video generation aims to generate expressive portrait videos with accurate lip synchronization and emotional facial expressions. Current methods rely on simple emotional labels, leading to insufficient semantic information. While introducing high-level semantics enhances expressiveness, it easily causes lip-sync degradation. Furthermore, mainstream generation methods struggle to balance computational efficiency and global motion awareness in long videos and suffer from poor temporal coherence. Therefore, we propose an \textbf{E}motion-\textbf{A}ware \textbf{D}iffusion model-based \textbf{Net}work, called \textbf{EAD-Net}. We introduce SyncNet supervision and Temporal Representation Alignment (TREPA) to mitigate lip-sync degradation caused by multi-modal fusion. To model complex spatio-temporal dependencies in long video sequences, we propose a Spatio-Temporal Directional Attention (STDA) mechanism that captures global motion patterns through strip attention. Additionally, we design a Temporal Frame graph Reasoning Module (TFRM) to explicitly model temporal coherence between video frames through graph structure learning. To enhance emotional semantic control, a large language model is employed to extract textual descriptions from real videos, serving as high-level semantic guidance. Experiments on the HDTF and MEAD datasets demonstrate that our method outperforms existing methods in terms of lip-sync accuracy, temporal consistency, and emotional accuracy.

---


### 127. [Branch Landing: Bloom Filter-Based Source Authorization for Forward-Edge CFI on RISC-V](https://arxiv.org/abs/2604.23331)

**<font color=#1a73e8>作者：</font>** You Wu, Peter Beerel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jump-Oriented Programming (JOP) attacks exploit indirect control transfers to bypass backward-edge defenses, yet existing forward-edge CFI mechanisms lack precise source-domain authorization: type-based CFI admits all same-signature callers, while tag-based hardware CFI is limited by fixed-width register storage that caps the number of simultaneously authorized sources. We propose Branch Landing (BRL), a landing-based forward-edge CFI framework for RISC-V that replaces fixed-capacity checks with Bloom filter membership queries. Two lightweight ISA extensions, bld and brl, propagate a source Section Identifier (SID) through a dedicated BRState register and validate it at each landing site with fixed-probe latency that is independent of the number of authorized sources under a chosen filter configuration. Section granularity is configurable, supporting policies from type-based to CFG-derived authorization within a single mechanism. We implement Branch Landing in the LLVM RISC-V backend and evaluate it on 81 BEEBS benchmarks under two representative policy configurations: a function-level, type-based policy and a basic-block-level, CFG-derived policy. Under a 3-cycle brl latency model, the two configurations incur average runtime overheads of only 0.210% and 0.421%, with mean code size growth of 0.46% and 0.52% respectively. The CFG-derived policy reduces the average equivalence class size by 32.5% compared to the type-based policy, and all evaluated executions complete without BRL enforcement failures.

---


### 128. [Advanced Anomaly Detection and Threat Intelligence in Zero Trust IoT Environments Using Machine Learning](https://arxiv.org/abs/2604.23332)

**<font color=#1a73e8>作者：</font>** Muhammad Umair Basharat, Jawad Hussain, Waqas Khalid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing adoption of IoT and cloud computing, combined with rapid advancements in digital technologies, has considerably increased the cyber-attack surface, resulting in increasingly complex and persistent attacks. Traditional security methods, primarily based on perimeter defenses, are insufficient to meet these developing threats, especially within the context of a Zero Trust Security (ZTS) architecture. This study investigates the application of sophisticated artificial intelligence (AI) and machine learning (ML) techniques, including the use of the Synthetic Minority Oversampling Technique (SMOTE), to improve anomaly detection and threat intelligence systems. This study focuses on how Support Vector Machine (SVM), Random Forest (RF), and Decision Tree (DT) classifiers might increase threat detection accuracy in IoT environments. The research endeavors to improve cybersecurity resilience by mitigating false positives and providing actionable intelligence through supervised learning algorithms. The KDD Cup 1999 dataset is used in the study to assess how well these models perform in simulating various network intrusions and regular traffic. The application of SMOTE significantly enhanced the performance of these models by addressing class imbalance, leading to improved detection accuracy. Furthermore, as supplementary methods for detecting malicious URLs and advanced persistent threats (APTs), edge-based machine learning and blockchain technology are investigated. This study addresses the shortcomings of conventional security systems and supports the growing demand for reliable threat detection in a world that is becoming more interconnected. It also advances the creation of more proactive and adaptable cybersecur

---


### 129. [H-SemiS: Hierarchical Fusion of Semi and Self-Supervised Learning for Knee Osteoarthritis Severity Grading](https://arxiv.org/abs/2604.23335)

**<font color=#1a73e8>作者：</font>** Chandravardhan Singh Raghaw, Anushka Parwal, Shahid Shafi Dar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knee osteoarthritis (KOA) is a degenerative joint disease that can lead to chronic pain, reduced mobility, and long-term disability. Automated severity grading from knee radiographs can support early assessment, but current methods heavily depend on large labeled datasets and remain sensitive to class imbalance, noisy samples, and variability in clinical annotations. To alleviate these limitations, we propose a Hierarchical fusion of Semi-Supervised framework with Self-Supervision (H-SemiS) for KOA severity grading in knee X-ray samples using limited annotated data. Rather than treating severity grading as a flat multi-class problem, H-SemiS decomposes the task into a sequence of binary sub-tasks within a semi-supervised teacher-student architecture, directly mitigating the impact of class imbalance. To further enhance feature learning from unlabeled data, the framework integrates an adversarial self-supervised reconstruction module that encourages the network to capture robust anatomical structures. In parallel, a teacher-student design with quantum-inspired feature mixing improves discrimination boundaries between adjacent grades when pseudo-labels are noisy. We comprehensively evaluate H-SemiS on two challenging multi-class datasets and assess its generalizability on two binary-class datasets. Our experimental results demonstrate the superiority of the proposed H-SemiS framework across multiple evaluation metrics, consistently outperforming several competing baselines and state-of-the-art methods. The code is publicly available at this https URL.

---


### 130. [Exploring Hierarchical Consistency and Unbiased Objectness for Open-Vocabulary Object Detection](https://arxiv.org/abs/2604.23344)

**<font color=#1a73e8>作者：</font>** Sanghoon Lee, Geon Lee, Hyekang Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional object detectors typically operate under a closed-set assumption, limiting recognition to a predefined set of base classes seen during training. Open-vocabulary object detection (OVD) addresses this limitation by leveraging vision-language models (VLMs) to generate pseudo labels for novel object classes. However, existing OVD methods suffer from two critical drawbacks: (1) inaccurate class label assignments, as VLMs are optimized for image-level predictions rather than the region-level predictions required for pseudo labeling, and (2) unreliable objectness scores from region proposal networks (RPNs) trained exclusively on base object classes. To address these issues, we propose a novel pseudo labeling framework for OVD. Our approach introduces a hierarchical confidence calibration (HCC) technique, which ensures reliable class label estimation by assessing consistency across hierarchical semantic levels (class, super- and sub-category). We also present LoCLIP, a parameter-efficient adaptation of CLIP that incorporates an objectness token to mitigate base class bias problem of RPNs and provide reliable objectness estimations for novel object classes. Extensive experiments on standard OVD benchmarks, including COCO and LVIS, demonstrate that our approach clearly sets a new state of the art, validating the effectiveness of our approach. Project site: this https URL

---


### 131. [When Chain-of-Thought Fails, the Solution Hides in the Hidden States](https://arxiv.org/abs/2604.23351)

**<font color=#1a73e8>作者：</font>** Houman Mehrafarin, Amit Parekh, Ioannis Konstas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether intermediate reasoning is computationally useful or merely explanatory depends on whether chain-of-thought (CoT) tokens contain task-relevant information. We present a mechanistic causal analysis of CoT on GSM8K using activation patching: transferring token-level hidden states from a CoT generation to a direct-answer run for the same question, then measuring the effect on final-answer accuracy. Across models, generating after patching yields substantially higher accuracy than both direct-answer prompting and the original CoT trace, revealing that individual CoT tokens can encode sufficient information to recover the correct answer, even when the original trace is incorrect. This task-relevant information is more prevalent in correct than incorrect CoT runs and is unevenly distributed across tokens, concentrating in mid-to-late layers and appearing earlier in the reasoning trace. Moreover, patching language tokens such as verbs and entities carry task-solving information that steers generation toward correct reasoning, whereas mathematical tokens encode answer-proximal content that rarely succeeds. Patched outputs are often shorter and yet exceed the accuracy of a full CoT trace, suggesting complete reasoning chains are not always necessary. Together, these findings demonstrate that CoT encodes recoverable, token-level problem-solving information, offering new insight into how reasoning is represented and where it breaks down.

---


### 132. [TEMPO: Transformers for Temporal Disease Progression from Cross-Sectional Data](https://arxiv.org/abs/2604.23368)

**<font color=#1a73e8>作者：</font>** Hongtao Hao, Joseph L. Austerweil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event-Based Models (EBMs) infer biomarker progression from cross-sectional data but typically only as ordinal sequences and rely on rigid model assumptions. We propose \textsc{Tempo}, a Transformer architecture that learns both ordinal and continuous event sequences through simulation-based supervised learning. \textsc{Tempo} uses two Transformer modules: one treats biomarkers as tokens to infer event sequencing; the other treats patients as tokens, representing each by their per-biomarker abnormality profile, to infer patients' disease stages. On synthetic benchmarks, \textsc{Tempo} reduces normalized Kendall's Tau distance by 52.89\% and staging MAE by 25.33\% compared to state-of-the-art SA-EBM, with larger reductions in high-dimensional settings (58.88\% and 61.10\%). Applied to ADNI, \textsc{Tempo} recovers a biologically plausible Alzheimer's progression: early medial temporal atrophy, followed by amyloid accumulation and cognitive decline, and late-stage tau pathology with terminal acceleration of global neurodegeneration -- broadly consistent with established disease models. \textsc{Tempo} also eliminates the need to derive custom inference algorithms and enables rapid empirical comparison of generative hypotheses.

---


### 133. [Hierarchical Spatio-Channel Clustering for Efficient Model Compression in Medical Image Analysis](https://arxiv.org/abs/2604.23375)

**<font color=#1a73e8>作者：</font>** Sisipho Hamlomo, Marcellin Atemkeng, Habte Tadesse Likassa 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) have become increasingly difficult to deploy in resource-constrained environments due to their large memory and computational requirements. Although low-rank compression methods can reduce this burden, most existing approaches compress spatial and channel redundancy independently and therefore do not fully exploit the localised structure within convolutional feature maps. This paper proposes a hierarchical spatio-channel low-rank compression framework for CNNs that exploits redundancy across spatial regions and channel activations. Unlike conventional methods, which apply a uniform decomposition across an entire layer, the proposed approach first partitions feature maps into spatial regions, then groups channels according to their co-activation patterns within each region, and finally applies rank-adaptive SVD to each resulting spatio-channel cluster. The method is evaluated on an AlexNet-based brain tumour MRI classification model and compared with Global SVD and Tucker decomposition under \(3\times\) and \(6\times\) compression budgets. Our method outperforms both baselines, reducing FLOPs from \(8.21\,\mathrm{G}\) to \(1.55\,\mathrm{G}\) (\(81.1\%\) reduction), achieving a \(1.38\times\) inference speed-up, and increasing classification accuracy from \(87.76\%\) to \(89.80\%\). The method also improves the macro \(F_1\)-score and performance on challenging classes such as meningioma. A hyper-parameter trade-off analysis demonstrates that the framework provides Pareto-optimal configurations, enabling control over the balance between compression and predictive performance. Moderate clustering with adaptive rank selection yields strong results. Bootstrap standard errors are reported for all classification metrics.

---


### 134. [Constraint-Based Analysis of Reasoning Shortcuts in Neurosymbolic Learning](https://arxiv.org/abs/2604.23377)

**<font color=#1a73e8>作者：</font>** Akihiro Takemura, Katsumi Inoue, Masaaki Nishino  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic systems can satisfy logical constraints during learning without achieving the intended concept-label correspondence; this is a problem known as reasoning shortcuts. We formalize reasoning shortcuts as a constraint satisfaction problem and investigate under which conditions concept mappings are uniquely determined by the constraints. We prove that a discrimination property (requiring that no valid concept mapping can be transformed into another valid mapping by swapping two concept values) is necessary for shortcut-freeness under bijective mappings, but demonstrate via a counterexample that it is insufficient even when the constraint graph is connected. We develop an ASP-based algorithm that verifies whether a given constraint set uniquely determines the intended concept mapping, with proven soundness and completeness. When shortcuts are detected, a greedy repair algorithm eliminates them by augmenting the constraint set, converging in at most $k$ iterations, where $k$ is the number of alternative valid mappings. We further provide a complexity classification: deciding shortcut-freeness is coNP-complete, counting shortcuts is #P-complete, and finding minimal repairs is NP-hard. We also establish sample complexity bounds showing that logarithmically many label queries suffice for disambiguation in favorable cases, while querying all ambiguous positions suffices in the worst case. Experiments across eight benchmark domains validate our approach.

---


### 135. [V-GRPO: Online Reinforcement Learning for Denoising Generative Models Is Easier than You Think](https://arxiv.org/abs/2604.23380)

**<font color=#1a73e8>作者：</font>** Bingda Tang, Yuhui Zhang, Xiaohan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning denoising generative models with human preferences or verifiable rewards remains a key challenge. While policy-gradient online reinforcement learning (RL) offers a principled post-training framework, its direct application is hindered by the intractable likelihoods of these models. Prior work therefore either optimizes an induced Markov decision process (MDP) over sampling trajectories, which is stable but inefficient, or uses likelihood surrogates based on the diffusion evidence lower bound (ELBO), which have so far underperformed on visual generation. Our key insight is that the ELBO-based approach can, in fact, be made both stable and efficient. By reducing surrogate variance and controlling gradient steps, we show that this approach can beat MDP-based methods. To this end, we introduce Variational GRPO (V-GRPO), a method that integrates ELBO-based surrogates with the Group Relative Policy Optimization (GRPO) algorithm, alongside a set of simple yet essential techniques. Our method is easy to implement, aligns with pretraining objectives, and avoids the limitations of MDP-based methods. V-GRPO achieves state-of-the-art performance in text-to-image synthesis, while delivering a $2\times$ speedup over MixGRPO and a $3\times$ speedup over DiffusionNFT.

---


### 136. [Keypoint-based Dynamic Object 6-DoF Pose Tracking via Event Camera](https://arxiv.org/abs/2604.23387)

**<font color=#1a73e8>作者：</font>** Zhe Wang, Qijin Song, Zihao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 6-DoF pose estimation of objects is critical for robots to perform precise manipulation tasks. However, for dynamic object pose estimation, conventional camera-based approaches face several major challenges, such as motion blur, sensor noise, and low-light limitation. To address these issues, we employ event cameras, whose high dynamic range and low latency offer a promising solution. Furthermore, we propose a keypoint-based detection and tracking approach for dynamic object pose estimation. Firstly, a keypoint detection network is constructed to extract keypoints from the time surface generated by the event stream. Subsequently, the polarity and spatial coordinates of the events are leveraged, and the event density in the vicinity of each keypoint is utilized to achieve continuous keypoint tracking. Finally, a hash mapping is established between the 2D keypoints and the 3D model keypoints, and the EPnP algorithm is employed to estimate the 6-DoF pose. Experimental results demonstrate that, whether in simulated or real event environments, the proposed method outperforms the event-based state-of-the-art methods in terms of both accuracy and robustness.

---


### 137. [Breaking the Resource Wall: Geometry-Guided Sequence Modeling for Efficient Semantic Segmentation](https://arxiv.org/abs/2604.23399)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan, Xin-Jui Pan, Chun-Po Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-performance semantic segmentation has achieved significant progress in recent years, often driven by increasingly large backbones and higher computational budgets. While effective, such approaches introduce substantial computational overhead and limit accessibility under constrained hardware settings. In this paper, we propose DGM-Net (Directional Geometric Mamba Network), an efficient architecture that improves modeling capability through structural design rather than increasing model capacity. We introduce Directional Geometric Mamba (G-Mamba), a linear-complexity O(N) operator as an alternative to conventional context modeling modules such as ASPP and PPM. To further enhance structural awareness in state space model (SSM)-based modeling, we design the DGM-Module, which extracts centripetal flow fields and topological skeletons to guide the scanning process and improve boundary preservation. Without relying on large-scale pretraining or heavy backbone scaling, DGM-Net achieves 80.8% mIoU within 28k iterations, 82.3% mIoU on Cityscapes test set, and 45.24% mIoU on ADE20K. In addition, the model maintains stable performance under constrained hardware settings (e.g., batch size of 2 on 8GB VRAM), highlighting its efficiency and practicality. These results demonstrate that incorporating geometric guidance into SSM-based architectures provides an effective and resource-efficient direction for semantic segmentation.

---


### 138. [Otherness as a Quality in Designing Expressive Robotic Touch](https://arxiv.org/abs/2604.23402)

**<font color=#1a73e8>作者：</font>** Ran Zhou, Laurens Boer, Daniel Leithinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Haptic technologies have advanced rapidly, yet exploration of robotic touch remains dominated by replicating realistic environmental cues or hand gestures, which narrows the design space and risks social resistance. This paper argues for alternatives: grounded in the notion of "otherness" from human-robot interaction (HRI), we propose treating robotic touch's inherent otherness as a design quality. Instead of being a limitation in pursuing realism, otherness can be embraced to elicit ambiguity and provoke alternative interpretations, fostering expressive and evocative robotic touch design. To develop this perspective, we analyze inspirational art and design precedents and four design research cases through a reflective Research through Design (RtD) approach. Through this analysis, we articulate a set of design languages structured around why otherness matters for touch meaning-making, how it can be shaped through design strategies, and where it can be embedded within robotic touch systems. We conclude by reflecting on the tensions and risks involved in designing robotic touch with otherness in mind.

---


### 139. [Learn&Drop: Fast Learning of CNNs based on Layer Dropping](https://arxiv.org/abs/2604.23403)

**<font color=#1a73e8>作者：</font>** Giorgio Cruciata, Luca Cruciata, Liliana Lo Presti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a new method to improve the training efficiency of deep convolutional neural networks. During training, the method evaluates scores to measure how much each layer's parameters change and whether the layer will continue learning or not. Based on these scores, the network is scaled down such that the number of parameters to be learned is reduced, yielding a speed up in training. Unlike state-of-the-art methods that try to compress the network to be used in the inference phase or to limit the number of operations performed in the backpropagation phase, the proposed method is novel in that it focuses on reducing the number of operations performed by the network in the forward propagation during training. The proposed training strategy has been validated on two widely used architecture families: VGG and ResNet. Experiments on MNIST, CIFAR-10 and Imagenette show that, with the proposed method, the training time of the models is more than halved without significantly impacting accuracy. The FLOPs reduction in the forward propagation during training ranges from 17.83\% for VGG-11 to 83.74\% for ResNet-152. These results demonstrate the effectiveness of the proposed technique in speeding up learning of CNNs. The technique will be especially useful in applications where fine-tuning or online training of convolutional models is required, for instance because data arrive sequentially.

---


### 140. [PushupBench: Your VLM is not good at counting pushups](https://arxiv.org/abs/2604.23407)

**<font color=#1a73e8>作者：</font>** Shengzhi Li, Jiarun Chen, Karun Sharma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) can recognize \textit{what} happens in video but fail to count \textit{how many} times. We introduce \textbf{PushupBench}, 446 long-form clips (avg. 36.7s) for evaluating repetition counting. The best frontier model achieves 42.1\% exact accuracy; open-source 4B models score $\sim$6\%, matching supervised baselines. We show that accuracy alone misleads -- weaker models exploit the modal count rather than reason temporally. Fine-tuning on counting with 1k samples transfers to general video understanding: MVBench (+2.15), PerceptionTest (+1.88), TVBench (+4.54), suggesting counting is a proxy for broader temporal this http URL incorporated in \texttt{lmms-eval} (this https URL) and hosted on (this http URL)

---


### 141. [Overcoming Copyright Barriers in Corpus Distribution Through Non-Reversible Hashing](https://arxiv.org/abs/2604.23412)

**<font color=#1a73e8>作者：</font>** Arthur Amalvy, Vincent Labatut, Xavier Bost 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While annotated corpora are crucial in the field of natural language processing (NLP), those containing copyrighted material are difficult to exchange among researchers. Yet, such corpora are necessary to fully represent the diversity of data found in the wild in the context of NLP tasks. We tackle this issue by proposing a method to lawfully and publicly share the annotations of copyrighted literary texts. The corpus creator shares the annotations in clear, along with a non-reversible hashed version of the source material. The corpus user must own the source material, and apply the same hash function to their own tokens, in order to match them to the shared annotations. Crucially, our method is robust to reasonable divergences in the version of the copyrighted data owned by the user. As an illustration, we present alignment experiments on different editions of novels. Our results show that our method is able to correctly align 98.7 to 99.79% of tokens depending on the novel, provided the user version is sufficiently close to the corpus creator's version. We publicly release novelshare, a Python implementation of our method.

---


### 142. [A Heterogeneous Two-Stream Framework for Video Action Recognition with Comparative Fusion Analysis](https://arxiv.org/abs/2604.23415)

**<font color=#1a73e8>作者：</font>** Md. Afzalur Rahaman, Tahmid Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most two-stream action recognition networks apply the same convolutional backbone to both RGB and optical flow streams, ignoring the fact that the two modalities have fundamentally different structural properties. Optical flow captures fine-grained motion patterns, while RGB frames carry rich appearance and scene context - treating them identically discards this distinction. We propose DualStreamHybrid, a heterogeneous two-stream architecture that assigns each stream a backbone suited to its input: a pretrained ViT-Tiny/16 for RGB frames, and a MobileNetV2 trained from scratch on a 20-channel stacked optical flow representation. A learned projection layer maps the two differently-sized feature vectors to a common dimensionality before fusion, enabling the two streams to interact without forcing architectural symmetry. We design five fusion strategies within a unified framework - late fusion, concatenation, cross-attention, weighted fusion, and gated fusion - and evaluate them on UCF11 (1,600 videos, 11 classes) and UCF50 (6,681 videos, 50 classes) to study how fusion behaviour scales with dataset size. On UCF11, cross-attention achieves 98.12% test accuracy, outperforming the RGB-only ViT-Tiny baseline of 95.94%, which suggests that explicit inter-modal attention is particularly effective on smaller, less complex datasets. On UCF50, weighted fusion reaches 96.86% and proves the most consistent strategy across both benchmarks. The learned stream weights reveal an interesting pattern: UCF11 sees near-equal modality contribution (RGB: 0.507, flow: 0.493), while UCF50 favours the RGB stream slightly more (RGB: 0.554, flow: 0.446) - arguably reflecting the larger and more visually diverse action space. Taken together, these results suggest that even a lightweight motion stream meaningfully complements a strong appearance encoder, and that the optimal fusion strategy depends on dataset scale.

---


### 143. [Approximating Uniform Random Rotations by Two-Block Structured Hadamard Rotations in High Dimensions](https://arxiv.org/abs/2604.23418)

**<font color=#1a73e8>作者：</font>** Tomer Zilca, Gal Mendelson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform random rotations are a useful primitive in applications such as fast Johnson-Lindenstrauss embeddings, kernel approximation, communication-efficient learning, and recent AI compression pipelines, but they are computationally expensive to generate and apply in high dimensions. A common practical replacement is repeated structured random rotations built from Walsh-Hadamard transforms and random sign diagonals.
Applying the structured random rotation twice has been shown empirically to be useful, but the supporting theory is still limited. In this paper we study the approximation quality achieved when using this two-block structured Hadamard rotation. Our results are both positive and negative. On the positive side, we prove that every fixed coordinate of the two-block transform converges uniformly, over all inputs, to the corresponding coordinate of a uniformly rotated vector, with an explicit Kolmogorov-distance bound of order $d^{-1/5}$. On the negative side, we prove an explicit lower bound on the Wasserstein distance between the full vector distributions, showing that the two-block transform is not a globally accurate surrogate for a uniform random rotation in the worst case. For the extremal input used in the lower bound, we also prove a matching asymptotic upper bound, showing that the lower-bound scale is sharp for that input.
Taken together, the results identify a clear separation between one-dimensional marginal behavior, where approximation improves with dimension, and full high-dimensional geometry, where a nonvanishing discrepancy remains. This provides a partial theoretical explanation for the empirical success of structured Hadamard rotations in some algorithms, while also clarifying the limitations of treating them as drop-in replacements for true uniform random rotations.

---


### 144. [Enhanced Privacy and Communication Efficiency in Non-IID Federated Learning with Adaptive Quantization and Differential Privacy](https://arxiv.org/abs/2604.23426)

**<font color=#1a73e8>作者：</font>** Emre Ardıç, Yakup Genç  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a distributed machine learning method where multiple devices collaboratively train a model under the management of a central server without sharing underlying data. One of the key challenges of FL is the communication bottleneck caused by variations in connection speed and bandwidth across devices. Therefore, it is essential to reduce the size of transmitted data during training. Additionally, there is a potential risk of exposing sensitive information through the model or gradient analysis during training. To address both privacy and communication efficiency, we combine differential privacy (DP) and adaptive quantization methods. We use Laplacian-based DP to preserve privacy, which is relatively underexplored in FL and offers tighter privacy guarantees than Gaussian-based DP. We propose a simple and efficient global bit-length scheduler using round-based cosine annealing, along with a client-based scheduler that dynamically adapts based on client contribution estimated through dataset entropy analysis. We evaluate our approach through extensive experiments on CIFAR10, MNIST, and medical imaging datasets, using non-IID data distributions across varying client counts, bit-length schedulers, and privacy budgets. The results show that our adaptive quantization methods reduce total communicated data by up to 52.64% for MNIST, 45.06% for CIFAR10, and 31% to 37% for medical imaging datasets compared to 32-bit float training while maintaining competitive model accuracy and ensuring robust privacy through differential privacy.

---


### 145. [Sphere-Depth: A Benchmark for Depth Estimation Methods with Varying Spherical Camera Orientations](https://arxiv.org/abs/2604.23432)

**<font color=#1a73e8>作者：</font>** Soulayma Gazzeh, Giuseppe Mazzola, Liliana Lo Presti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable depth estimation from spherical images is crucial for 360° vision in robotic navigation and immersive scene understanding. However, the onboard spherical camera can experience unintentional pose variations in real-world robotic platforms that, along with the geometric distortions inherent in equirectangular projections, significantly impact the effectiveness of depth estimation. To study this issue, a novel public benchmark, called Sphere-Depth, is introduced to systematically evaluate the robustness of monocular depth estimation models from equirectangular images in a reproducible way. Camera pose perturbations are simulated and used to assess the performance of a popular perspective-based model, Depth Anything, and of spherical-aware models such as Depth Anywhere, ACDNet, Bifuse++, and SliceNet. Furthermore, to ensure meaningful evaluation across models, a depth calibration-based error protocol is proposed to convert predicted relative depth values into metric depth values using supervised learned scaling factors for each model. Experiments show that even models explicitly designed to process spherical images exhibit substantial performance degradation when variations in the camera pose are observed with respect to the canonical pose. The full benchmark, evaluation protocol, and dataset splits are made publicly available at: this https URL

---


### 146. [When Does Removing LayerNorm Help? Activation Bounding as a Regime-Dependent Implicit Regularizer](https://arxiv.org/abs/2604.23434)

**<font color=#1a73e8>作者：</font>** Lucky Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic Tanh (DyT) removes LayerNorm by bounding activations with a learned tanh(alpha x). We show that this bounding is a regime-dependent implicit regularizer, not a uniformly beneficial replacement. Across GPT-2-family models spanning 64M to 3.78B parameters and 1M to 118M tokens, with Llama and ViT cross-checks, DyT improves validation loss by 27.3% at 64M/1M but worsens it by 18.8% at 64M/118M; the 1M benefit vanishes with capacity (+1.7% at 3.78B), while the 118M penalty reaches +27.9%. The mechanism is measurable: 49% of DyT activations saturate at 1M versus 23% at 118M, and a 500-step saturation heuristic classifies DyT's sign with 75% raw in-sample accuracy on the 12-cell GPT-2 calibration set (AUC 0.75; 64% when adding Scale 5 stress cells), correctly labels 3/3 Llama checks, but only reaches 50% raw leave-one-scale-out accuracy. Three interventions support the bounding explanation: HardTanh reproduces the regime pattern, increasing alpha at 118M monotonically reduces DyT's penalty, and vanilla+dropout(p=0.5) matches DyT's data-rich loss. We also localize Llama-DyT collapse to SwiGLU gating, where saturation separates collapse from convergence in a 3-seed component ablation (r=0.94). Scope: all experiments are compute-limited (T/P < 1.84), below Chinchilla-optimal training.

---


### 147. [Knee-xRAI: An Explainable AI Framework for Automatic Kellgren-Lawrence Grading of Knee Osteoarthritis](https://arxiv.org/abs/2604.23435)

**<font color=#1a73e8>作者：</font>** Azmul A. Irfan, Nur Ahmad Khatim, Alfan Alfian Irfan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiographic grading of knee osteoarthritis (KOA) with the Kellgren-Lawrence (KL) system is limited by inter-reader variability and the opacity of current deep learning approaches, which predict KL grades directly from images without decomposing structural features. We present Knee-xRAI, a modular framework that independently quantifies the three cardinal radiographic features of KOA (joint space narrowing [JSN], osteophytes, and subchondral sclerosis) and integrates them into an explainable KL grade classification. The pipeline combines U-Net++ segmentation for contour-based JSN measurement, an SE-ResNet-50 network for per-site osteophyte grading (OARSI scale), and a hybrid texture-CNN classifier for binary sclerosis quantification. The resulting 50-dimensional structured feature vector feeds two complementary classification paths. An XGBoost path supports SHAP-based feature attribution. A ConvNeXt hybrid path combines the structured vector with a full-image encoder for enhanced predictive performance. Evaluated on 8,260 radiographs from an OAI-derived dataset, the JSN module achieved a Dice coefficient of 0.8909 and an mJSW intraclass correlation of 0.8674 against manual annotations. The ConvNeXt hybrid path reached a test quadratic weighted kappa (QWK) of 0.8436 and AUC of 0.9017. The transparent XGBoost path achieved a test QWK of 0.6294 with full feature-level audit capability. Ablation confirmed JSN as the dominant predictor (QWK = 0.6103 alone), with osteophyte features providing consistent incremental gain (+0.0183) and sclerosis contributing marginally. Inference-time ablation of Path B confirmed the structured pathway contributes materially beyond the image encoder, with QWK drops of 0.098 (feature zeroing) and 0.284 (feature-image permutation). Knee-xRAI explicitly quantifies all three KL-defining radiographic features within a single auditable pipeline.

---


### 148. [Scalable and Verifiable Federated Learning for Cross-Institution Financial Fraud Detection](https://arxiv.org/abs/2604.23437)

**<font color=#1a73e8>作者：</font>** Prajwal Panth, Nishant Nigam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The global financial ecosystem confronts a critical asymmetry: while fraud syndicates operate as borderless, distributed networks, banking institutions remain constrained by regulatory data silos, limiting visibility into cross-institutional threat patterns under strict privacy laws such as GDPR. Although Federated Learning (FL) enables collaborative training, existing protocols impose a trade-off among scalability, privacy, and integrity. Homomorphic encryption schemes are computationally expensive, while pairwise masking protocols require O(N^2) key exchanges and lack mechanisms to detect malformed updates. Existing defenses also remain vulnerable to gradient inversion attacks that can reconstruct sensitive transaction data.
To address these limitations, we propose Dynamic Sharded Federated Learning (DSFL), a verifiable secure aggregation framework for cross-institution financial fraud detection. DSFL replaces mesh topologies with Dynamic Stochastic Sharding, reducing communication complexity from O(N^2) to O(N m), where m is a fixed shard size, achieving linear scalability. To mitigate insider threats, we introduce Linear Integrity Tags, an additive-homomorphic commitment mechanism that enables probabilistic verification of submitted updates without the overhead of zero-knowledge proofs, while not enforcing semantic correctness. Additionally, the Active Neighborhood Recovery protocol ensures robust aggregation under participant dropouts. Empirical evaluation on the Credit Card Fraud Detection Dataset (ULB) demonstrates an approximately 33x latency reduction compared to Paillier-based secure aggregation, while maintaining strong resilience under simulated failures. These results position DSFL as a practical foundation for scalable and privacy-preserving collaborative fraud detection.

---


### 149. [Resource-Constrained UAV-Based Weed Detection for Site-Specific Management on Edge Devices](https://arxiv.org/abs/2604.23442)

**<font color=#1a73e8>作者：</font>** Linyuan Wang, Haibo Yao, Te-Ming Tseng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weeds compete with crops for light, water, and nutrients, reducing yield and crop quality. Efficient weed detection is essential for site-specific weed management (SSWM). Although deep learning models have been deployed on UAV-based edge systems, a systematic understanding of how different model architectures perform under real-world resource constraints is still lacking. To address this gap, this study proposes a deployment-oriented framework for real-time UAV-based weed detection on resource-constrained edge platforms. The framework integrates UAV data acquisition, model development, and on-device inference, with a focus on balancing detection accuracy and computational efficiency. A diverse set of state-of-the-art object detection models is evaluated, including convolution-based YOLO models (v8-v12) and transformer-based RT-DETR models (v1-v2). Experiments on three edge devices (Jetson Orin Nano, Jetson AGX Xavier, and Jetson AGX Orin) demonstrate clear trade-offs between accuracy and inference latency across models and hardware configurations. Results show that high-capacity models achieve up to 86.9% mAP50 but suffer from high latency, limiting real-time deployment. In contrast, lightweight models achieve 66%-71% mAP50 with significantly lower latency, enabling real-time performance. Among all models, RT-DETRv2-R50-M achieves competitive accuracy (79% mAP50) with improved efficiency, while YOLOv10n provides the fastest inference speed. YOLOv11s and RT-DETRv2-R50-M offer the best balance between accuracy and speed, making them strong candidates for real-time UAV deployment.

---


### 150. [IndustryAssetEQA: A Neurosymbolic Operational Intelligence System for Embodied Question Answering in Industrial Asset Maintenance](https://arxiv.org/abs/2604.23446)

**<font color=#1a73e8>作者：</font>** Chathurangi Shyalika, Dhaval Patel, Amit Sheth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial maintenance environments increasingly rely on AI systems to assist operators in understanding asset behavior, diagnosing failures, and evaluating interventions. Although large language models (LLMs) enable fluent natural-language interaction, deployed maintenance assistants routinely produce generic explanations that are weakly grounded in telemetry, omit verifiable provenance, and offer no testable support for counterfactual or action-oriented reasoning that undermine trust in safety-critical settings. We present IndustryAssetEQA, a neurosymbolic operational intelligence system that combines episodic telemetry representations with a Failure Mode Effects Analysis Knowledge Graph (FMEA-KG) to enable Embodied Question Answering (EQA) over industrial assets. We evaluate on four datasets covering four industrial asset types, including rotating machinery, turbofan engines, hydraulic systems, and cyber-physical production systems. Compared to LLM-only baselines, IndustryAssetEQA improves structural validity by up to 0.51, counterfactual accuracy by up to 0.47, and explanation entailment by 0.64, while reducing severe expert-rated overclaims from 28% to 2% (approximately 93% reduction). Code, datasets, and the FMEA-KG are available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
