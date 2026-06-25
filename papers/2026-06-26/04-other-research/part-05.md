# 📦 其他研究 | 2026年06月26日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-222**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-222**

---

### 201. [Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound](https://arxiv.org/abs/2606.25978)

**<font color=#1a73e8>作者：</font>** Thiago Thomas, Gabriel de Oliveira Ramos, Felipe Meneguzzi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent goal recognition asks an observer to jointly infer which agents act together and what each team is trying to achieve, so the hypothesis space grows combinatorially with the number of team partitions and goals per team. Real applications such as drone surveillance and collaborative robotics expose only the agents' trajectory, which forces the observer to rank team-goal hypotheses from behavior alone. Multi-Agent Goal Recognition with Branch-and-Bound (MAGR-BB) addresses this setting with a shared team- and goal-conditioned policy used as the scoring model inside a factorized branch-and-bound search. On a controlled multi-agent Blocksworld benchmark, MAGR-BB returns the same top-ranked hypothesis as exhaustive search throughout the trajectory while cutting hypothesis materialization by orders of magnitude and reducing cumulative recognition runtime substantially.

---


### 202. [The Inference-Compute Frontier and a Latency-Efficient Architecture for Limit Order Book Prediction](https://arxiv.org/abs/2606.25986)

**<font color=#1a73e8>作者：</font>** C. Evans Hedges  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether a scaling-law-style inference-compute frontier appears in limit order book prediction. Using FI-2010 and a suite of models ranging from small decision trees to neural LOB architectures, we find that the realized empirical frontier of predictive loss versus structural forward work is well summarized by a power law. In particular, with MLPLOB held out as an architecture family, a power-law fit to the low- and mid-compute non-MLPLOB frontier extrapolates across multiple orders of magnitude and attains $R^2=0.941$ on the excluded high-compute MLPLOB target frontier.
A similar exercise in latency space gives substantially weaker results, showing that latency is not merely noisy compute. We use this gap to motivate FastBiNLOB, a dense axis-separable LOB mixer built from hardware-friendly temporal and feature mixing operations. In a five-seed experiment, FastBiNLOB exceeds the published $y_{10}$ and $y_{100}$ macro-F1 targets at notably lower latency than existing published SOTA architectures.

---


### 203. [Taxonomy-aware deep learning for hierarchical marine species classification in underwater imagery](https://arxiv.org/abs/2606.25989)

**<font color=#1a73e8>作者：</font>** Dan Zimmerman, Dimitris A. Pados, George Sklivanitis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classification of marine species from underwater imagery is essential for scalable ocean biodiversity monitoring and conservation policy. Existing approaches struggle with severe domain shift across collection platforms, fine-grained visual similarity between closely related species, and uneven annotation granularity, where many specimens can only be identified to genus or a coarser taxonomic rank. We present a taxonomy-aware deep learning framework that aligns both the training loss and the inference rule with the hierarchical structure of biological classification, combining a taxonomy-weighted loss, minimum-risk Bayesian inference, multi-scale feature encoding, and independent per-rank classification heads. Evaluated on the FathomNet 2025 dataset1 (79 marine classes across seven taxonomic ranks), the system achieves a mean taxonomic distance of 1.581, within 3% of the 1st-place solution (1.535), with the largest gains from metric-aligned inference and simple, decoupled components that generalize better than learned dependencies under distribution shift.

---


### 204. [SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models](https://arxiv.org/abs/2606.25990)

**<font color=#1a73e8>作者：</font>** Liang-Yuan Wu, Zih-Ching Chen, Tongshuang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As multimodal conversational systems increasingly engage in spoken interaction, their ability to navigate paralinguistic social cues has become a critical bottleneck for natural human-AI communication. However, existing evaluations of machine emotional intelligence assess reasoning exclusively through isolated text or passive acoustic perception, overlooking the complex cross-modal reasoning required for active, multi-turn dialogue. We introduce \textsc{SpeechEQ}, a comprehensive framework designed to evaluate the sociolinguistic reasoning of Speech-Language Models (SLMs). The framework includes a validated dataset of 2,265 dialogues across 15 Emotional Quotient (EQ) subscales grounded in EQ-i 2.0 theory, along with a multi-turn evaluation protocol measured by our proposed Spoken EQ (SEQ) score inspired by human EQ assessments. Experiments show limitations in how both existing Speech Emotion Recognition and end-to-end Speech-Language Models understand and apply paralinguistic cues through speech. While end-to-end architectures outperform cascaded systems, \textsc{SpeechEQ} reveals that current multimodal models remain bottlenecked by a text-reliant ``modality shortcut,'' an alignment-induced ``safety trap,'' and ``contextual amnesia,'' highlighting the barriers to truly emotionally aware AI. Our benchmark can be accessed at this https URL and demo page at this https URL

---


### 205. [BlowLive: Blow-Based Multi-Factor Biometrics with Liveness Detection and Revocability](https://arxiv.org/abs/2606.25998)

**<font color=#1a73e8>作者：</font>** Eyasu Getahun Chekole, Howard Halim, Daniël Reijsbergen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Biometric authentication systems are increasingly deployed in security-critical applications, yet existing physiological and behavioral biometrics suffer from fundamental limitations: 1) they are vulnerable to spoofing attacks due to unreliable liveness detection, 2) biometric templates may leak privacy-sensitive information 3) intra-user variability results in accuracy degradation, and 4) it is difficult to revoke physiological biometrics and safeguard them over long-term use. To address these challenges, we propose BlowLive, a robust multi-factor biometric (MFB) framework that integrates blow-acoustic signals and facial biometrics as complementary behavioral and physiological modalities. BlowLive incorporates advanced spectral feature extraction and multimodal fusion techniques, achieving high authentication accuracy even for behavioral modalities. Instead of relying on conventional biometric approaches that utilize raw biometric templates for authentication, the proposed framework adopts a fuzzy-extractor-based biometric authentication scheme, wherein stable cryptographic keys are derived from inherently noisy biometric inputs and subsequently used for authentication. To defend against playback, synthetic, and deepfake attacks, BlowLive further integrates a novel Doppler shift-based liveness detection mechanism. We implement the complete BlowLive framework and experimentally evaluate its effectiveness using biometric data collected from 50 participants. The experimental results demonstrate high authentication accuracy (99.56% for blow-acoustics and 100% for facial and fusion modalities), robust liveness detection (99.42% accuracy), strong template protection and revocability, non-invasiveness, and high usability.

---


### 206. [Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization](https://arxiv.org/abs/2606.26002)

**<font color=#1a73e8>作者：</font>** Kamar Hibatallah Baghdadi, Kawther Guoual Belhamidi, Sara Belhadj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present HiReLC, a hierarchical ensemble-reinforcement learning framework for automated joint quantization and structured pruning of deep neural networks. The framework decomposes the compression search across two levels of abstraction: low-level agents (LLAs) operate independently per block, selecting per-kernel configurations over a multi-discrete action space spanning bitwidth, pruning keep-ratio, quantization type, and granularity, while high-level agents (HLAs) coordinate global budget allocation via ensemble voting guided by Fisher Information-based sensitivity estimates. To mitigate the computational cost of policy evaluation, an iterative active learning loop interleaves surrogate-guided RL optimization with post-compression fine-tuning, using a lightweight MLP surrogate to amortize expensive evaluations and a logit-MSE proxy during cold-start. The surrogate is used for reward shaping rather than as a replacement for final post-compression evaluation. The controller is architecture-agnostic by design, with a modular layer abstraction decoupling the RL environment from the underlying network topology. Experiments across Vision Transformer and CNN benchmarks demonstrate effective parameter-storage compression ratios of 5.99 - 6.72$\times$ with a 3.83 % gain in one setting and 0.55 - 5.62 % accuracy drops elsewhere, supporting hierarchical policy decomposition and sensitivity-aware guidance as practical design choices for joint neural network compression.

---


### 207. [Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect](https://arxiv.org/abs/2606.26003)

**<font color=#1a73e8>作者：</font>** Dihia Lanasri, Fairouz Taki, Asma Kemmoum  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.

---


### 208. [From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007)

**<font color=#1a73e8>作者：</font>** Long Cao, Zhongquan Wang, Jie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image priors can synthesize target conditions for 3D Gaussian street scenes, but independently edited views do not define a coherent 3D target. Direct fitting can propagate view-specific noise, while existing pipelines do not jointly handle imperfect sparse anchors and standard-rasterizer deployment. To address this gap, teacher-relative appearance residual distillation is introduced for appearance baking. A structured space for frequency decomposition, confidence estimation, and primitive-level lifting is formed by residuals between teacher anchors and original renders. The direct optimization signal is supplied by renderer-space matching, while primitive assignment is regularized by support-aware Gaussian-space aggregation. Supported detail is admitted and unsupported noise is suppressed through confidence-gated coarse-to-fine optimization, after which all residuals are baked into fixed-geometry spherical-harmonic coefficients. The teacher and auxiliary training modules are discarded at inference. Evaluation across Waymo street assets, Tanks and Temples scenes, and multiple target conditions shows a favorable overall balance of target alignment, content preservation, artifact suppression, and cross-view consistency over editing-based baselines. Ablations confirm the effectiveness of the main components. Code will be released at this https URL.

---


### 209. [Is Variational Monte Carlo Robust? Sharp Moment Thresholds and Heavy-tailed Stochastic Optimization](https://arxiv.org/abs/2606.26009)

**<font color=#1a73e8>作者：</font>** Philipp Grohs, Davide Nobile  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational Monte Carlo (VMC) is a central algorithm in electronic structure theory and has gained renewed importance through modern neural-network ansätze such as FermiNet. At its core, VMC seeks ground states by minimizing the Rayleigh quotient by stochastic optimization. In this work, we show that the resulting stochastic optimization problem is intrinsically governed by the nodal geometry of the underlying wave function. More precisely, we establish that properties of the nodal set determine the integrability of the local energy and gradient estimators that drive VMC. For broad and practically relevant ansatz classes, including Slater-Jastrow wave functions with variable-exponent Slater-type orbitals, we prove that these estimators are generically heavy-tailed and fail to admit higher moments. At the same time, for general analytic ansätze, we prove weak moment bounds for the relevant estimators and identify precise low-moment regimes, showing how generic and degenerate nodal structures lead to different integrability thresholds. Building on this analysis, we introduce a new robust variant of VMC $\unicode{x2013}$ coined PS-Clip-VMC $\unicode{x2013}$ which is based on clipping both the local energy and the gradient random variable. We prove that PS-Clip-VMC converges both in expectation and with high probability in the weak moment regime of VMC. Preliminary experiments for training FermiNet on Atoms with up to 18 electrons suggest that PS-Clip-VMC is significantly more robust than standard methods.

---


### 210. [The Tatoxa System for Text Detoxification in Low-Resource Languages: The Case of Tatar](https://arxiv.org/abs/2606.26015)

**<font color=#1a73e8>作者：</font>** Ilseyar Alimova, Bogdan Monogov, Artyom Mazur 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text detoxification, the automated detection and mitigation of abusive and harmful content, is essential for ensuring the safety of online communities and protecting users. However, low resource languages such as Tatar have received little research attention. In this paper we present Tatoxa, a novel state-of-the-art system for text detoxification in the Tatar language. Comparative experiments show that the proposed approach outperforms existing open source and proprietary commercial LLMs on key quality metrics. We also introduce a new dataset for text detoxification in Tatar, designed for fine tuning and evaluation in low resource settings. Finally, cross lingual transfer experiments indicate that transfer from other languages, including the culturally close Russian, performs significantly worse than training on native Tatar data even when a large Russian corpus is available.

---


### 211. [MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation](https://arxiv.org/abs/2606.26016)

**<font color=#1a73e8>作者：</font>** Yang Chen, Xiaowei Xu, Shuai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Normalizing Flows (NFs) are powerful generative models capable of exact density estimation and sampling. However, their strict invertibility often forces the model to exhaust its capacity on low-level pixel details, hindering the capture of high-level semantic structures. While Masked Image Modeling (MIM) has excelled in representation learning, its integration into generative pipelines has remained largely modular and disjointed. In this paper, we propose MIMFlow, a unified end-to-end framework that jointly optimizes latent semantics, pixel reconstruction, and generative flow. By employing a VAE encoder to infer semantic latent from masked images, MIMFlow achieves a principled decoupling of the generative task: the Normalizing Flow focuses on modeling a simplified, low-frequency semantic manifold, while a specialized decoder handles high-frequency synthesis. This design effectively resolves the inherent capacity bottleneck of NFs, allowing the model to prioritize global structural coherence over redundant noise. Empirical results on ImageNet 256$\times$256 show that MIMFlow-L reaches 71.3\% linear probing accuracy and an FID of 2.50. Despite using only 128 tokens (50\% fewer than standard models), it yields a 32.8\% performance gain over similar-scale NF baselines. Our code is available at this https URL.

---


### 212. [Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem](https://arxiv.org/abs/2606.26028)

**<font color=#1a73e8>作者：</font>** Xihan Xiong, Zelin Li, Wei Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation. Despite its rapid adoption, the protocol has not been studied empirically, leaving it unclear whether the information it records provides a trustworthy basis for decision-making. To address this gap, we present the first empirical study of ERC-8004 across three chains: Ethereum, BNB Smart Chain (BSC), and Base, covering the period from protocol deployment through May 13, 2026. We crawl on-chain Identity and Reputation events, off-chain files, and x402 payment transactions.
On the identity side, we find that most registrations are placeholders rather than active agents, with only a small fraction (3%, 4%, and 15% across Ethereum, BSC, and Base) exposing a valid ERC-8004 registration file with at least one live service endpoint. On the reputation side, we show that the Registry, as currently deployed, cannot function as a trust signal: values are not commensurable, feedback records are rarely grounded in verifiable interactions, and reputation can be manipulated at minimal cost. Consistent with these design weaknesses, we find that a substantial fraction of reviewers (73.6%, 59.2%, and 90.6% across Ethereum, BSC, and Base) exhibit coordinated Sybil behavior. After removing Sybil-flagged feedback, 15.5%, 72.3%, and 89.4% of rated agents, respectively, are left with no valid feedback. We then turn these findings into concrete recommendations for future revisions of ERC-8004. Our study yields actionable protocol-design implications and establishes an empirical baseline for research on AI agent markets.

---


### 213. [Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining](https://arxiv.org/abs/2606.26050)

**<font color=#1a73e8>作者：</font>** Juliana Li, Diya Sreedhar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Midway through an ordinary pretraining run, a small language model learns the pronoun-gender rule: cued with a girl's name ("Sue cried because"), it resolves the next pronoun to she, generalizing to held-out probes (0.94 by step 925). By step 3,500 the same model scores near zero on the same probes, although the rule's evidence is still in the training data. We call this within-run reversal natural ungrokking: the corpus decides, with no trace in the loss curve, which learned rules a model keeps.
Which rules survive is predictable from one corpus statistic: how often the training stream shows the rule winning. Across un-intervened runs (two corpora, three budgets, three seeds), support frequency decides a rule's fate; the data-to-parameter ratio only modulates how deeply a doomed rule falls. The same emerge-then-collapse dynamics appear in public Pythia checkpoints, collapse depth ordered by model scale as predicted. The forgetting is a displacement: a competing surface pattern out-competes the rule, and the log-probability margin between them crosses zero within 100 training steps of the behavioral collapse.
Control over this fate is asymmetric: the same edit that destroys a rule on demand cannot restore it. Flipping support to counter-evidence in place kills the rule with monotone dose-response in two unrelated rules; but injecting support back, even to 450 times the level that naturally sustains it, buys no recovery. Every confirmatory threshold and prediction was pre-registered before the data it governed was read.

---


### 214. [DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation](https://arxiv.org/abs/2606.26058)

**<font color=#1a73e8>作者：</font>** Nan Chen, Yiyang Cai, Rongchang Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.

---


### 215. [A welding penetration prediction model for laser welding process based on self-supervised learning using physics-informed neural networks](https://arxiv.org/abs/2606.26059)

**<font color=#1a73e8>作者：</font>** Sen Li, Xiaoying Liu, Xiaojian Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is therefore essential for ensuring weld quality. To this end, this paper introduces SimPhysNet, a novel algorithm that achieves high classification accuracy in laser welding penetration prediction using only a limited number of labelled images. This approach effectively overcomes the limitations of supervised learning classification algorithms, which are hindered in industrial applications by their dependence on extensive, high-quality labelled data. The core of SimPhysNet is a unique self-supervised learning paradigm that embeds physical priors into a contrastive learning framework. By incorporating a physics-informed neural network (PINN), the model is guided to extract physically meaningful features of the molten pool and keyhole from a large set of unlabelled data, while three image augmentation tasks further enhance its generalization capabilities. Subsequently, a few-shot learning strategy, based on prototypical networks, enables robust classification by constructing class representations from a minimal set of labelled images. Experimental results demonstrate that SimPhysNet achieves a classification accuracy of 96.06% using only 200 labelled images (approximately 5% of the total labelled dataset), which is comparable to the performance of conventional supervised learning algorithms that utilize the entire labelled dataset. This work presents a new, efficient, and highly accurate method, providing the way for the intelligent automation of laser welding.

---


### 216. [When Certainty Is an Artifact: Keyword Lexicon Blindness and the (Mis)Measurement of Rhetorical Stance](https://arxiv.org/abs/2606.26062)

**<font color=#1a73e8>作者：</font>** Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a statistically significant, large-effect-size finding in computational social science be entirely an artifact of the measurement instrument? We present a case where the answer appears to be yes. Analyzing 85 interviews across four public intellectuals (2016--2026), we find a robust negative-affect/emphatic-certainty lexical co-occurrence pattern under keyword-based scoring ($r = 0.72$--$0.93$, $p < 0.01$ for all four speakers). Replacing keyword counting with LLM-based zero-shot semantic classification on the complete diarized corpus (32,625 sentences) dramatically reduces this correlation: Dalio's $r = 0.851$ drops to $r = 0.206$, with two speakers showing negative $r(\text{neg}, \text{emphatic})$ and one showing null. In contrast, the LLM reveals a strong negative-hedging coupling across speakers -- Rogoff's $r(\text{neg}, \text{hedged}) = 0.875$ ($p = 0.001$) and Zeihan's $r(\text{neg}, \text{hedged}) = 0.722$ ($p = 0.008$) -- consistent with the conventional expectation that pessimistic discourse attracts hedging, not certainty. Sentence-level error analysis traces this discrepancy to three structural failure modes in keyword lexicons -- syntactic blindness, polysemy blindness, and categorical absence -- illustrated through cases where keyword counting inverts semantic meaning (e.g., ''never absolutely totally confident'' scored as high-certainty). We argue that keyword lexicons measure a universal lexical co-occurrence tendency -- negative discourse naturally attracts emphatic vocabulary -- that is orthogonal to, and can systematically invert, rhetorical stance. Treating keyword counts as measurements of epistemic certainty is a category error: a finding that appears to be about a speaker's psychology may be entirely about the counting of words.

---


### 217. [A cross-process welding penetration status prediction algorithm based on unsupervised domain adaptation in laser and TIG welding](https://arxiv.org/abs/2606.26078)

**<font color=#1a73e8>作者：</font>** Sen Li, Haichao Cui, Chendong Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised deep learning has been widely used for weld penetration state classification; however, its performance often degrades significantly under domain shift, such as when transferring models between welding processes with distinct physical mechanisms:for instance, from arc-dominated tungsten inert gas (TIG) welding to keyhole-based laser welding. To overcome this limitation, we propose an unsupervised domain adaptation (UDA) framework integrated with a gradual source domain expansion (GSDE) strategy. Evaluated on dedicated TIG and laser welding datasets, our approach achieves high accuracy in both same-process and cross-process transfer tasks. Specifically, it attains average accuracies of 90.65% on TIGFH and 90.72% on LSPS in same-process settings, surpassing a supervised baseline by 35.83% and 38.87%, respectively. More notably, in cross-process scenarios, it reaches 80.48% for TIG to Laser and 81.13% for Laser to TIG, improving upon the baseline by 43.39% and 43.40%. UMAP visualizations verify that the model learns domain-invariant features while maintaining discriminative class boundaries. This method considerably lowers the relabeling cost for new welding processes and enhances the versatility of intelligent monitoring across different welding systems.

---


### 218. [Real-Time Voice AI Hears but Does Not Listen](https://arxiv.org/abs/2606.26083)

**<font color=#1a73e8>作者：</font>** Martijn Bartelds, Federico Bianchi, James Zou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.

---


### 219. [MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation](https://arxiv.org/abs/2606.26087)

**<font color=#1a73e8>作者：</font>** JoungBin Lee, Jaewoo Jung, Jongmin Lee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.

---


### 220. [On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity](https://arxiv.org/abs/2606.26091)

**<font color=#1a73e8>作者：</font>** Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.

---


### 221. [TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092)

**<font color=#1a73e8>作者：</font>** Hao Sun, Hao Yan, Mengting Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.

---


### 222. [RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments](https://arxiv.org/abs/2606.26094)

**<font color=#1a73e8>作者：</font>** Babak Rahmani, Sebastian Dziadzio, Joschka Strüber 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.

---


> [!TIP]
> 当前位于：**201-222**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-222**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
