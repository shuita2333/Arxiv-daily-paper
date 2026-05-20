# 📦 其他研究 | 2026年05月21日

> 本类共 **338** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-338**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-338**

---

### 301. [AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration](https://arxiv.org/abs/2605.20025)

**<font color=#1a73e8>作者：</font>** Jiaqi Liu, Shi Qiu, Mairui Li 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating scientific discovery requires more than generating papers from ideas. Real research is iterative: hypotheses are challenged from multiple perspectives, experiments fail and inform the next attempt, and lessons accumulate across cycles. Existing autonomous research systems often model this process as a linear pipeline: they rely on single-agent reasoning, stop when execution fails, and do not carry experience across runs. We present AutoResearchClaw, a multi-agent autonomous research pipeline built on five mechanisms: structured multi-agent debate for hypothesis generation and result analysis, a self-healing executor with a \textsc{Pivot}/\textsc{Refine} decision loop that transforms failures into information, verifiable result reporting that prevents fabricated numbers and hallucinated citations, human-in-the-loop collaboration with seven intervention modes spanning full autonomy to step-by-step oversight, and cross-run evolution that converts past mistakes into future safeguards. On ARC-Bench, a 25-topic experiment-stage benchmark, AutoResearchClaw outperforms AI Scientist v2 by 54.7%. A human-in-the-loop ablation across seven intervention modes reveals that precise, targeted collaboration at high-leverage decision points consistently outperforms both full autonomy and exhaustive step-by-step oversight. We position AutoResearchClaw as a research amplifier that augments rather than replaces human scientific judgment. Code is available at this https URL.

---


### 302. [Training-Free Bayesian Filtering with Generative Emulators](https://arxiv.org/abs/2605.20028)

**<font color=#1a73e8>作者：</font>** Thomas Savary, François Rozet, Gilles Louppe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian filtering is a well-known problem that aims to estimate plausible states of a dynamical system from observations. Among existing approaches to solve this problem, particle filters are theoretically exact for non-linear dynamics and observations, but suffer from poor scalability in high dimensions. In this work, we show that diffusion-based emulators of dynamical systems can be used to implement, without additional training, an optimal variant of particle filters that has remained largely unexplored due to implementation challenges with classical numerical solvers. Experiments on nonlinear chaotic systems, including atmospheric dynamics, demonstrate that the proposed approach successfully scales particle filtering to high-dimensional settings.

---


### 303. [Take It or Leave It: Intent-Controlled Partial Optimal Transport](https://arxiv.org/abs/2605.20030)

**<font color=#1a73e8>作者：</font>** Salil Parth Tripathi, Bertrand Chapron, Fabrice Collard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While optimal transport (OT) enforces a rigid constraint by requiring two measures to be matched exactly, partial optimal transport relaxes this requirement by allowing mass to remain unmatched through a global budget, scalar rebate, or uniform rejection rule. However, many applications call for more structured, pointwise rejection mechanisms, where the decision to leave mass unmatched depends on side-specific reliability, support geometry, or external information about which components should participate in the comparison. We introduce \emph{intent-controlled partial optimal transport} (IC-POT), a targeted generalization of partial transport that replaces the global rejection paradigm with pointwise rejection costs over both measures. We show that the resulting optimization problem admits a dual interpretation in terms of local acceptance thresholds and can be solved by recasting it as a balanced Kantorovich OT problem on an augmented support. Beyond theoretical analysis, we demonstrate the practical relevance of IC-POT in settings where rejection is driven by side information. In positive-unlabeled learning and open-partial domain adaptation, incorporating pointwise rejection rules that encode statistical structure improves fixed baseline pipelines. Finally, we motivate the use of IC-POT with a geophysical practical case: multi-modal satellite ocean measurements, for which physical and sensors priors naturally inform the rejection mechanism and define the retrieved comparable signal information.

---


### 304. [CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph Fraud Detection](https://arxiv.org/abs/2605.20032)

**<font color=#1a73e8>作者：</font>** Junjun Pan, Yixin Liu, Yu Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-attributed graph fraud detection (TAGFD) plays a critical role in preventing fraudulent activities on online social and e-commerce platforms. However, to evade detection, fraudsters continuously evolve their camouflaging strategies by deliberately mimicking textual responses of benign users, thereby concealing their malicious purposes. This phenomenon, referred to as semantic camouflage, fundamentally undermines commonly relied assumptions on how structural and attribute cues can be exploited to identify fraudsters, and makes it difficult to spot fraudsters with unsupervised TAGFD. To bridge the gaps, we propose a Case-Adaptive Multi-cue Expert fRAmework (CAMERA) for unsupervised TAGFD. CAMERA employs an ego-decoupled mixture-of-experts architecture, where each expert specializes in modeling a distinct type of fraud-indicative cue. A context-informed gating model is introduced to jointly consider the ego node representation and its local neighborhood context for adaptive integration of cues learned by different experts. Furthermore, CAMERA leverages the inherent rarity of fraudsters to support unsupervised one-class learning with expert-level objectives that encourage modeling dominant benign patterns, thereby enabling reliable unsupervised detection of camouflaged fraudsters. Experiments on 4 challenging datasets show that CAMERA consistently outperforms competitors, showing its effectiveness against semantically camouflaged fraudsters. Code available at this https URL

---


### 305. [D$^3$-Subsidy: Online and Sequential Driver Subsidy Decision-Making for Large-Scale Ride-Hailing Market](https://arxiv.org/abs/2605.20036)

**<font color=#1a73e8>作者：</font>** Taijie Chen, Rui Su, Siyuan Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ride-hailing platforms like DiDi Chuxing operate in highly dynamic environments where balancing driver supply and passenger demand is critical. Although driver-side subsidies serve as a primary lever to align these forces and improve key KPIs like completed rides (\texttt{Rides}) and gross merchandise value (\texttt{GMV}), optimizing them in production requires simultaneously meeting three constraints: (i) responsiveness to stochastic shocks, (ii) strict subsidy-rate caps, and (iii) low-latency execution at city scale. These requirements rule out expensive per-order optimization, calling for a forward-looking, constraint-aware city-level controller for online sequential decision making. To meet these requirements, we introduce D$^3$-Subsidy (Dynamic Driver-side Diffusion-based Subsidy), a hierarchical diffusion-based framework for deployable city-wide subsidy control. To bridge the train-inference gap, D$^3$-Subsidy employs a prefix-conditioned diffusion model that samples plausible future trajectories from immutable historical observations, ensuring the training protocol aligns with the fixed-history nature of online deployment. These generated plans are then decoded by a context-conditioned inverse module into low-dimensional city-level control signals. For scalable execution, we bridge the gap between city-level planning and fine-grained dispatch via a Lagrangian-dual-derived mapping, which embeds subsidy-rate caps directly into order-driver incentives without iterative optimization. Additionally, a multi-city pretraining strategy with parameter-efficient fine-tuning enables robust transfer across heterogeneous cities. Extensive offline evaluations demonstrate that D$^3$-Subsidy improves \texttt{Rides} and \texttt{GMV} while enhancing cap compliance, and a real-world A/B test confirms significant uplift while keeping budget-related violation metrics within operational thresholds.

---


### 306. [When Critics Disagree: Adaptive Reward Poisoning Attacks in RIS-Aided Wireless Control System](https://arxiv.org/abs/2605.20037)

**<font color=#1a73e8>作者：</font>** Deemah H. Tashman, Soumaya Cherkaoui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-poisoning attacks present a significant risk to learning-based wireless control systems. Given this, we propose a Disagreement-Guided Reward Poisoning (DGRP) adaptive attack on a Soft Actor-Critic (SAC) agent. In a Cognitive Radio Network (CRN) environment assisted by Reconfigurable Intelligent Surfaces (RIS), the SAC agent is tasked with maximizing the long-term secondary users' (SUs) rate by simultaneously optimizing the transmission power of the SU transmitter and the RIS phase shifts. DGRP corrupts rewards, particularly when the SAC dual critics exhibit substantial disagreement-especially in high-leverage, high-uncertainty states-resulting in distorted value estimations and guiding the policy towards suboptimal actions. Our findings demonstrate that DGRP substantially diminishes the performance improvements typically provided by RIS and degrades transmission quality. We further investigate key attack parameters and determine their impact on learning. In comparison to periodic-timing and exploration-triggered baselines, DGRP consistently causes greater damage, highlighting the necessity of considering disagreement-aware threats when evaluating the robustness of Deep Reinforcement Learning (DRL) in RIS-assisted networks.

---


### 307. [Active Context Selection Improves Simple Regret in Contextual Bandits](https://arxiv.org/abs/2605.20040)

**<font color=#1a73e8>作者：</font>** Mohammad Shahverdikondori, Jalal Etesami, Negar Kiyavash  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the contextual multi-armed bandit problem with a finite context space (a.k.a. subpopulations), where the learner recommends a best action for each context and is evaluated by context-weighted simple regret. Our guarantees are worst-case over the reward distributions, while remaining instance-dependent with respect to the context distribution vector $p$. Akin to experimental design problems where the population of interest is fixed but the sampled subpopulation can be controlled, we allow the learner to actively choose which context to sample from. For a known $p$, we characterize tight regret rates: passive sampling where contexts are randomly revealed achieves regret of order $\sqrt{n/T \, \lVert p \rVert_{1/2}}$, whereas active sampling with allocation $q_j \propto p_j^{2/3}$ achieves the tight rate $\sqrt{n/T} \, \lVert p \rVert_{2/3}$. The resulting improvement can be as large as $\Theta(k^{1/4})$, where $k$ is the number of contexts. We further extend the analysis to budgeted active sampling, characterize the corresponding tight rate, and identify when a limited active budget suffices to recover the fully active rate. When $p$ is unknown, we propose the Explore-Explore-Then-Commit (EETC) algorithm, which optimally balances estimating the context distribution and the time to switch to active allocation, such that for large horizons, it matches the known-$p$ active rate up to constants. Experiments on synthetic and real-world data support our theoretical findings.

---


### 308. [Mind Your Moras: Orthography-Aware Error Analysis of Neural Japanese Morphological Generation](https://arxiv.org/abs/2605.20043)

**<font color=#1a73e8>作者：</font>** Wen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an orthography-aware error analysis of Japanese past-tense morphological inflection, treating hiragana not merely as a transcriptional medium, but as a representational system encoding morphophonological distinctions that may influence model generalization. We evaluate two character-level sequence-to-sequence architectures on past-tense formation using datasets formatted according to the SIGMORPHON 2020 and 2023 shared task conventions. Despite high aggregate accuracy, models exhibit systematic, linguistically interpretable errors that cluster around specific orthographic properties of hiragana. We introduce a concise error taxonomy capturing seven primary failure modes and provide both quantitative and qualitative analyses. Gemination-related errors dominate residual failures, accounting for 75-80% of errors, particularly in verbs whose stems end in the vowel e and require gemination before the past-tense suffix. Error patterns remain highly consistent across architectures and random seeds, suggesting a robust interaction between orthographic representation, morphological structure, and data frequency effects in shaping model generalization. These results underscore the necessity of orthography-aware evaluation for understanding neural generalization in morphologically complex languages.

---


### 309. [OP2GS: Object-Aware 3D Gaussian Splatting with Dual-Opacity Primitives](https://arxiv.org/abs/2605.20044)

**<font color=#1a73e8>作者：</font>** Guiyu Liu, Niklas Vaara, Janne Mustaniemi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) provides an explicit and efficient scene representation, but its primitives lack inherent object-level identity, hindering downstream tasks such as open-vocabulary scene understanding. Existing methods typically address this by either distilling high-dimensional feature embeddings into Gaussians or by lifting 2D mask labels into 3D via heuristic refinement. However, feature-based approaches incur heavy storage and decoding overhead, while lifting-based pipelines remain vulnerable to label contamination: Gaussians necessary for appearance reconstruction often receive incorrect object labels during 2D-to-3D projection. We propose OP2GS, an object-aware Gaussian representation that augments each primitive with an explicit instance identity and a dedicated instance opacity $\sigma^{*}$ for object-mask rendering. The original opacity $\sigma$ remains responsible for visual reconstruction, while $\sigma^{*}$ models whether a Gaussian should contribute to a particular object mask. This dual-opacity formulation decouples visual existence from instance occupancy: mislabeled Gaussians can remain available for image rendering while becoming transparent in the object-mask branch. To learn this representation, we introduce a random object loss that optimizes the 1D instance occupancy field using the standard transmittance-based visibility of 3DGS. Semantic descriptors are then attached at the object level through multi-view aggregation, eliminating per-Gaussian feature storage. Compared with feature-training approaches, OP2GS achieves competitive open-vocabulary performance while significantly reducing computational overhead. Compared with training-free pipelines, it leverages physically consistent occupancy learning to resolve visibility ambiguities.

---


### 310. [Taking Cryptography Out of the Data Path via Near-Memory Processing in DRAM](https://arxiv.org/abs/2605.20047)

**<font color=#1a73e8>作者：</font>** Nicola Barcarolo, Brahmaiah Gandham, Mohammad Sadrosadati 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic algorithms such as AES-128 and SHA-256 are fundamental to ensuring data security and integrity. Although these algorithms are computationally efficient, their performance is often constrained by the processor-centric architectures (e.g., CPUs, GPUs), primarily due to the memory bottleneck. This constraint leads to increased latency and higher energy consumption, particularly when handling large volumes of data. To overcome these challenges, Processing-in-Memory (PIM) has emerged as a promising architectural paradigm, allowing computation to occur directly within or near memory units. By minimizing data movement between the processor and memory units, PIM can significantly accelerate cryptographic algorithms while improving energy efficiency. Several pieces of prior work have demonstrated the effectiveness of PIM at fundamentally accelerating cryptographic algorithms. However, none of the prior works have extensively demonstrated the potential of a real-world PIM system. In this paper, we want to investigate the potential and limitations of real-world PIM in accelerating cryptographic algorithms. As part of our methodology, the UPMEM PIM architecture is used to assess the scalability of cryptographic algorithms. When these algorithms operate on a single rank, their performance remains below that of modern CPUs. However, distributing the computation across multiple ranks significantly enhances performance. When all available ranks are utilized, real-world PIM can accelerate cryptographic algorithms more effectively.

---


### 311. [Language Mutations Sustain the Persistences of Conspiracy Theories on Social Media](https://arxiv.org/abs/2605.20050)

**<font color=#1a73e8>作者：</font>** Calvin Yixiang Cheng, Dorian Quelle, Scott A. Hale  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates how language mutations affect the persistent diffusion of conspiracy theories on social media. Drawing on a three-year dataset of conspiracy-related posts from X, and applying computational linguistic analysis alongside survival modelling, we find that conspiracy claims with greater semantic mutations have substantially longer lifespans. Mutations in psycholinguistic properties, including pronouns, social reference words, cognitive process terms, risk- and health- related vocabularies, are associated with extended lifespans. Mutations in actor, action and target (AAT) categories are associated with longer lifespans as well. Qualitative analysis identifies two predominant mutation patterns: simplification and assimilation, at both linguistic and AAT structural levels. Taken together, the results advance our understanding of how language mutations contribute to conspiracy persistence online and shed lights on longitudinal content moderation strategies. We argue that content moderation should consider the mutability of conspiracy claims and focus on the core claims that can address their potential variations.

---


### 312. [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/abs/2605.20051)

**<font color=#1a73e8>作者：</font>** Tian Dong, Yanjun Chen, Shoufeng Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI infra has become a shared execution layer for model training, deployment, and agent orchestration. Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design. Yet the prevalence and detectability of these variants remain poorly understood. This paper presents a measurement study of vulnerability variants in AI infra. Analyzing 688 GitHub repositories and 251 publicly disclosed vulnerabilities, we find that AI infra projects frequently share overlapping functionality and recurrent vulnerable patterns, creating a concrete basis for cross-repository variants. Building on this finding, we study how to automatically identify such variants from known disclosures. We propose INFRASCOPE, a reference-driven multi-agent framework that extracts transferable vulnerability semantics from known cases and uses them to locate and validate variants in new repositories. Evaluating INFRASCOPE on 20 real-world AI infra repositories, we uncover over 20 vulnerabilities, including 11 acknowledged cases and 4 cases that have been assigned CVEs so far.

---


### 313. [PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling](https://arxiv.org/abs/2605.20052)

**<font color=#1a73e8>作者：</font>** Ying-Jia Lin, Tzu-Chin Lo, Ping-Chien Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic report labeling facilitates the identification of clinical findings from unstructured text and enables large-scale annotation for medical imaging research. Existing rule-based labelers struggle with the diverse descriptions in clinical reports, while fine-tuning pre-trained language models (PLMs) requires large amounts of labeled data that are often unavailable in clinical settings. In this paper, we propose PromptRad, a knowledge-enhanced multi-label \textbf{prompt}-tuning approach for \textbf{rad}iology report labeling under low-resource settings. PromptRad reformulates multi-label classification as masked language modeling and incorporates synonyms from the UMLS Metathesaurus into a multi-word verbalizer to enrich category representations. By fine-tuning the PLM without additional classification layers, PromptRad requires substantially less labeled data than conventional fine-tuning. Experiments on liver CT reports show that PromptRad outperforms dictionary-based and fine-tuning baselines with only 32 labeled training examples, and achieves competitive performance with GPT-4 despite using a much smaller model. Further analysis demonstrates that PromptRad captures complex negation patterns more effectively than existing methods, making it a promising solution for report labeling in data-scarce clinical scenarios. Our code is available at this https URL.

---


### 314. [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents](https://arxiv.org/abs/2605.20061)

**<font color=#1a73e8>作者：</font>** Wenjie Tang, Minne Li, Sijie Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) is a promising paradigm for improving large language model (LLM) agents on long-horizon interactive tasks. However, in partially observable environments, incomplete observations cause agent beliefs to drift over time, while delayed rewards obscure the causal impact of intermediate decisions, exacerbating temporal credit assignment challenges. To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning. ReBel introduces belief-consistency supervision, converting discrepancies between predicted beliefs and observed feedback into dense self-supervised signals without requiring external step-wise annotations or verifiers. It also employs belief-aware grouping to compare trajectories under similar belief states, yielding more robust and lower-variance advantage estimates. We evaluate ReBel on challenging long-horizon benchmarks, including ALFWorld and WebShop. ReBel improves task success by up to $20.4$ percentage points over the episode-level baseline GRPO and increases sample efficiency by $2.1\times$. These results suggest that belief-aware self-supervision is a promising direction for reliable long-horizon decision-making under partial observability. Code is available at: this https URL.

---


### 315. [Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network](https://arxiv.org/abs/2605.20064)

**<font color=#1a73e8>作者：</font>** Guilherme Santos da Silva, Dalcimar Casanova, Jefferson Tales Oliva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, research has highlighted the association between increased adipose tissue surrounding the human heart and elevated susceptibility to cardiovascular diseases such as atrial fibrillation and coronary heart disease. However, the manual segmentation of these fat deposits has not been widely implemented in clinical practice due to the substantial workload it entails for medical professionals and the associated costs. Consequently, the demand for more precise and time-efficient quantitative analysis has driven the emergence of novel computational methods for fat segmentation. This study presents a novel deep learning-based methodology that offers autonomous segmentation and quantification of two distinct types of cardiac fat deposits. The proposed approach leverages the pix2pix network, a generative conditional adversarial network primarily designed for image-to-image translation tasks. By applying this network architecture, we aim to investigate its efficacy in tackling the specific challenge of cardiac fat segmentation, despite not being originally tailored for this purpose. The two types of fat deposits of interest in this study are referred to as epicardial and mediastinal fats, which are spatially separated by the pericardium. The experimental results demonstrated an average accuracy of 99.08% and f1-score 98.73 for the segmentation of the epicardial fat and 97.90% of accuracy and f1-score of 98.40 for the mediastinal fat. These findings represent the high precision and overlap agreement achieved by the proposed methodology. In comparison to existing studies, our approach exhibited superior performance in terms of f1-score and run time, enabling the images to be segmented in real time.

---


### 316. [Text-to-SPARQL Generation with Reinforcement Learning: A GRPO-based Approach on DBLP](https://arxiv.org/abs/2605.20066)

**<font color=#1a73e8>作者：</font>** Jann Pfeifer, Debayan Banerjee, Ricardo Usbeck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering seeks to translate natural language questions into executable queries over knowledge graphs, but existing approaches often rely on large models or full supervision in the form of gold query annotations. This study examines whether reinforcement learning with outcome-based rewards can train a small instruction-tuned language model to perform zero-shot Text-to-SPARQL generation in the scholarly domain. Group-Relative Policy Optimization (GRPO) is applied to the Qwen3-1.7B model on DBLP-QuAD, using prompts that combine natural language questions with symbolic hints about entities and relations. Training relies on execution feedback, structural constraints, and answer-level rewards, with an additional variant that incorporates gold-query-based shaping. The resulting models are compared to the unmodified zero-shot baseline and to a supervised DoRA-finetuned baseline across answer-level accuracy, execution accuracy, category-wise scores, and generalization to held-out templates. GRPO substantially improves over the zero-shot baseline and exhibits competitive generalization, while supervised DoRA finetuning achieves higher overall accuracy on the same model scale. Ablation analyses indicate that execution-based rewards account for most gains, with additional shaping yielding limited additional benefit, suggesting that outcome-based reinforcement learning is a viable training strategy when gold queries are unavailable for token-level supervision.

---


### 317. [Smooth Partial Lotteries for Stable Randomized Selection](https://arxiv.org/abs/2605.20069)

**<font color=#1a73e8>作者：</font>** Alexander Goldberg, Giulia Fanti, Nihar B. Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Competitive selection processes, from scientific funding to admissions and hiring, use evaluations to score candidates, and eventually choose a subset of them based on those scores. Recently, many organizations have adopted partial lotteries, which randomize selection based on evaluation scores. However, existing lottery designs are inherently unstable, as a small change to a single candidate's score can cause large shifts in their selection probabilities. This instability undermines a key goal of lotteries: reducing the influence of fine-grained score distinctions near the decision boundary. We propose smoothness as a design principle for partial lotteries, formalizing it as a Lipschitz condition on the mapping from review scores over candidates to selection probabilities. We introduce the Clipped Linear Lottery, a simple mechanism in which selection probabilities scale linearly with estimated quality between an upper threshold, above which we always accept, and a lower threshold, below which we always reject. We prove that the Clipped Linear Lottery's worst-case regret matches a lower bound for any smooth selection rule up to a factor of $(1 - k/n)$, where $k/n$ is the acceptance rate. We compare smooth selection to other stability notions like Individual Fairness and Differential Privacy, showing that the Clipped Linear Lottery achieves a better smoothness-regret tradeoff than alternatives. Experiments on real peer review data from ICLR 2025, NeurIPS 2024, and the Swiss National Science Foundation demonstrate that existing lottery designs are highly unstable in practice even under perturbations to a single score. Our experiments also confirm the tightness of our theoretical analysis and show that our proposed Clipped Linear Lottery achieves a better smoothness-utility tradeoff than alternatives in practice.

---


### 318. [X-Ray cardiac angiographic vessel segmentation based on pixel classification using machine learning and region growing](https://arxiv.org/abs/2605.20073)

**<font color=#1a73e8>作者：</font>** E O Rodrigues, L O Rodrigues, J J Lima 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work proposes a pixel-classification approach for vessel segmentation in x-ray angiograms. The proposal uses textural features such as anisotropic diffusion, features based on the Hessian matrix, mathematical morphology and statistics. These features are extracted from the neighborhood of each pixel. The approach also uses the ELEMENT methodology, which consists of creating a pixel-classification controlled by region-growing where the result of the classification affects further classifications of pixels. The Random Forests classifier is used to predict whether the pixel belongs to the vessel structure. The approach achieved the best accuracy in the literature (95.48%) outperforming unsupervised state-of-the-art approaches.

---


### 319. [Probability-Conserving Flow Guidance](https://arxiv.org/abs/2605.20079)

**<font color=#1a73e8>作者：</font>** Parsa Esmati, Junha Hyung, Amirhossein Dadashzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-based generative models dominate visual synthesis, with guidance aligning samples to user input and improving perceptual quality. However, Classifier-Free Guidance (CFG) and extrapolation-based methods are heuristic linear combinations of velocities/scores that ignore the generative manifold geometry, breaking probability conservation and driving samples off the learned manifold under strong guidance. We analyse guidance through the continuity equation and show its effect decomposes into a divergence term and a score-parallel term defined invariantly across parameterisations. We prove the divergence term blows up structurally as sampling approaches the data manifold, motivating a time-dependent schedule alongside score-parallel attenuation. The resulting plug-and-play rule, Adaptive Manifold Guidance (AdaMaG), bounds both terms at no additional inference cost. Finally, we show that most empirical heuristics for reducing saturation or improving generation quality correspond directly to the two terms in our decomposition. Across image generation benchmarks, AdaMaG improves realism, reduces hallucinations, and induces controlled desaturation in high-guidance regimes.

---


### 320. [VL-DPO: Vision-Language-Guided Finetuning for Preference-Aligned Autonomous Driving](https://arxiv.org/abs/2605.20082)

**<font color=#1a73e8>作者：</font>** Zhefan Xu, Ghassen Jerfel, Marina Haliem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of autonomous driving datasets has enabled the scaling of powerful motion forecasting models. While large-scale pretraining provides strong performance, the standard imitation objective may not fully capture the complex nuances of human driving preferences. Meanwhile, recent advances in vision-language models (VLMs) have demonstrated impressive reasoning and commonsense understanding. Building on these capabilities, this paper presents VL-DPO, a vision-language-guided framework that aligns ego-vehicle motion forecasting models with human preferences. Our approach leverages a VLM as a zero-shot reasoner to automatically generate preference pairs from a pretrained model's rollouts, which are then used to finetune the model via Direct Preference Optimization (DPO). We finetune our models on the Waymo Open End-to-End Driving Dataset (WOD-E2E) and evaluate performance against held-out human preference annotations using rater feedback score (RFS) and average displacement error (ADE). Our experiments confirm that the VLM's trajectory selection is a high-quality proxy for human preference. Our final model, VL-DPO, yields an 11.94% increase in RFS and a 10.01% reduction in ADE over the pretrained model.

---


### 321. [Spatially Prompted Visual Trajectory Prediction for Egocentric Manipulation](https://arxiv.org/abs/2605.20085)

**<font color=#1a73e8>作者：</font>** Yifan Li, Xinyu Zhou, Yunhao Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic manipulation is often specified through language instructions or task identifiers, yet cluttered environments with similar objects are better handled by spatially indicating what to move and where to place it. Addressing the vision-centric challenge of object and goal specification, we present, to the best of our knowledge, the first formalization of Spatially Prompted Visual Trajectory Prediction (SP-VTP). This novel setting utilizes initial spatial prompts (like bounding boxes or points) to define task objectives, tasking the model with forecasting future end-effector trajectories from egocentric streams. To study this problem, we collect and annotate EgoSPT, a dataset of egocentric spatially prompted manipulation trajectories with first-frame object and target grounding annotations and recovered 3D end-effector motion. SP-VTP is challenging because the task specification is static, while the scene configuration evolves over time. To solve this problem, we propose SPOT(Spatially Prompted Object-Target Policy), which combines a task encoder for first-frame visual and coordinate spatial prompts, an observation encoder for current visual and history context, and a trajectory generator for future end-effector motion. Experiments under strict scene-level splits show that SPOT improves cross-scene trajectory prediction over non-prompted or single-source prompted baselines. Together, EgoSPT and SPOT establish a new spatial prompting problem SP-VTP, as a simple and scalable task condition for egocentric manipulation.

---


### 322. [INSHAPE: Instance-Level Shapelets for Interpretable Time-Series Classification](https://arxiv.org/abs/2605.20088)

**<font color=#1a73e8>作者：</font>** Seongjun Lee, Seokhyun Lee, Changhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering shapelets -- i.e., discriminative temporal patterns within time series -- has been widely studied to address the inherent complexity of time-series classification (TSC) and to make model decision-making processes more transparent. However, existing methods primarily focus on population-level shapelets optimized across the entire dataset, which leads to two fundamental limitations: (i) population-level patterns often misalign with instance-specific features, resulting in suboptimal performance and potentially misleading interpretations, and (ii) most methods treat shapelets as independent entities, overlooking important temporal dependencies and interactions among multiple patterns. To address these limitations, we propose INSHAPE, an interpretable TSC framework that discovers variable-length, discriminative temporal patterns specific to each time series. INSHAPE identifies these patterns as non-overlapping segments and models their temporal dependencies, thereby providing clear instance-level interpretations while achieving strong predictive performance. Furthermore, INSHAPE bridges local and global interpretability through a bottom-up approach, aggregating instance-level shapelets into prototypical (population-level) shapelets. Extensive experiments on 128 UCR and 30 UEA benchmark datasets show that INSHAPE consistently outperforms state-of-the-art shapelet-based methods while providing more intuitive and interpretable insights.

---


### 323. [Neurosymbolic Learning for Inference-Time Argumentation](https://arxiv.org/abs/2605.20098)

**<font color=#1a73e8>作者：</font>** Gabriel Freedman, Adam Dejl, Adam Gould 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Claim verification is an important problem in high-stakes settings, including health and finance. When information underpinning claims is incomplete or conflicting, uncertain answers may be more appropriate than binary true or false classifications. In all cases, faithful explanations of the considerations determining the final verdict are crucial. We introduce inference-time argumentation (ITA), a trainable neurosymbolic framework for ternary claim verification in which a formal argumentation semantics giving the strength of claims is used both (i) to guide LLM training as models learn to generate arguments and assign them base scores (representing intrinsic strengths) and (ii) to compute ternary (true/false/uncertain) predictions from generated, scored arguments. As a result, at training time, argument generation and scoring can be optimised according to the quality of the induced argumentative predictions. Moreover, at inference time, the final prediction is faithful, by construction, to the arguments and scores determining the verdict, rather than being justified by a potentially unfaithful post-hoc reasoning trace as in conventional reasoning models. We finally show that, on two datasets for ternary claim verification, ITA improves upon argumentative baselines and can perform competitively against non-argumentative direct-prediction baselines, while providing verdicts that are computed deterministically from explicit, inspectable argumentative structures.

---


### 324. [Optimal Representation Size: High-Dimensional Analysis of Pretraining and Linear Probing](https://arxiv.org/abs/2605.20105)

**<font color=#1a73e8>作者：</font>** Valentina Njaradi, Clémentine Dominé, Rachel Swanson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning to generalise from limited data is a fundamental challenge for both artificial and biological systems. A common strategy is to extract reusable structure from abundant unlabelled data, enabling efficient adaptation to new tasks from limited labelled data. This two-stage paradigm is now standard in modern training pipelines, where pretraining is followed by fine-tuning or linear probing. We provide an analytical model of this process: structure extraction is formalized as principal component analysis on unlabelled data, and downstream learning as linear regression on a separate labelled dataset. In the high-dimensional regime, we derive exact expressions for training and generalisation error showcasing their dependence on representation dimensionality, unlabelled and labelled sample sizes, and task alignment. Our results show that pretrained representations strongly influence downstream generalisation, and we characterize the optimal representation size as a function of task parameters: with abundant pretraining data but scarce downstream data, maximally compressed representations are optimal, whereas with limited pretraining data, higher-dimensional representations generalise better. Furthermore, we establish an exact trade-off between pretraining and supervision, quantifying how much unlabelled data is required to replace a single labelled sample. Beyond our idealised model, we observe similar phenomenology in autoencoders and pretrained LLMs. Altogether, we highlight that optimising representation size is critical, giving conditions for when compression during pretraining improves generalisation.

---


### 325. [Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction](https://arxiv.org/abs/2605.20107)

**<font color=#1a73e8>作者：</font>** Robert Jenkinson Alvarez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> JEPAs often regularize one-view embeddings toward an isotropic Gaussian, implicitly baking Euclidean symmetry into the representation. We show that this is not merely a benign default. For a known structured downstream geometry $H\succ0$, the minimax and maximum-entropy covariance under a Hamiltonian energy budget is $(c/d)H^{-1}$, and Euclidean isotropy incurs a closed-form price of isotropy. More importantly, when the downstream geometry is unknown, no geometry-independent fixed marginal target is canonical: every fixed covariance shape can be maximally misaligned for some structured geometry. We further show that even oracle one-view marginals do not identify the JEPA view-to-view predictive coupling. These results suggest that the structural bias in JEPAs should enter the cross-view coupling rather than a fixed encoder marginal. We instantiate this principle with \textbf{HamJEPA}, which encodes each view as a phase-space state $(q,p)$ and predicts view-to-view transitions with a learned Hamiltonian leapfrog map, while non-isotropic scale and spectral floors prevent collapse. In a deliberately headless token protocol, HamJEPA improves over SIGReg on CIFAR-100 by $+4.89$ kNN@20 and $+3.52$ linear-probe points at 30 epochs, and by $+6.45$ kNN@20 and $+10.64$ linear-probe points at 80 epochs, while a matched MLP predictor ablation shows that the symplectic coupling is the ingredient driving the neighborhood-geometry gain. On ImageNet-100, HamJEPA-$q$ improves by $+4.82$ kNN@20 and $+7.52$ linear-probe points at 45 epochs.

---


### 326. [SetCon: Towards Open-Ended Referring Segmentation via Set-Level Concept Prediction](https://arxiv.org/abs/2605.20110)

**<font color=#1a73e8>作者：</font>** Zhixiong Zhang, Yizhuo Li, Shuangrui Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring segmentation grounds natural-language queries to pixel-level masks, but extending it to complex scenarios with multiple instances, cross-category groups, or open-ended target sets remains challenging. Previous Large Vision Language Model (LVLM)-based methods represent referred targets with one or more special tokens sequentially, treating multiple targets as separate outputs rather than a coherent set and offering little incentive to capture set-level properties such as completeness and mutual exclusivity. We reformulate open-ended referring segmentation as explicit set-level concept prediction and propose Set-Concept Segmentation (SetCon), which uses LVLM-generated natural-language concepts, instead of segmentation-specific tokens, as semantic conditions for joint mask-set decoding. A hierarchical semantic decomposition first predicts a shared set-level concept defining the target scope and then refines it into fine-grained concept groups aligned with target subsets. To support this, a two-stage annotation pipeline augments existing reasoning segmentation datasets with hierarchical semantic supervision (236k samples, 784k concept phrases). SetCon achieves state-of-the-art results on image benchmarks (+3.3 gIoU on gRefCOCO, +12.1 gIoU on MUSE), with margins that grow as the number of referred targets increases. The concept interface also transfers to video under a detect-and-track setting, yielding new state-of-the-art results on seven referring video benchmarks, including +10.9 J&F on MeViS and +12.4 J&F on Ref-SeCVOS.

---


### 327. [Toto 2.0: Time Series Forecasting Enters the Scaling Era](https://arxiv.org/abs/2605.20119)

**<font color=#1a73e8>作者：</font>** Emaad Khwaja, Chris Lettieri, Gerald Woo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that time series foundation models scale: a single training recipe produces reliable forecast-quality improvements from 4M to 2.5B parameters. We release Toto 2.0, a family of five open-weights forecasting models trained under this recipe. The Toto 2.0 family sets a new state of the art on three forecasting benchmarks: BOOM, our observability benchmark; GIFT-Eval, the standard general-purpose benchmark; and the recent contamination-resistant TIME benchmark. This report describes our experimental results and details the design decisions behind Toto 2.0: its architecture and training recipe, training data, and the u-muP hyperparameter transfer pipeline. All five base checkpoints are released under Apache 2.0.

---


### 328. [Using Aristotle API for AI-Assisted Theorem Proving in Lean 4: A Formalisation Case Study of the Grasshopper Problem](https://arxiv.org/abs/2605.20120)

**<font color=#1a73e8>作者：</font>** Gabriel Rongyang Lau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted theorem proving can now generate substantial Lean developments for olympiad-level mathematics, but the evidential status of such developments depends on which declarations are actually verified. This paper reports a Lean 4 formalization case study of an Aristotle API proof attempt for the Grasshopper problem, originally posed as IMO 2009 Problem 6. The generated artifact states a generalized Lean version of the theorem, contains four verified helper lemmas for local components of a maximality and adjacent-swap exchange strategy, and leaves the main theorem grasshopper closed directly by one unresolved sorry. The verified components establish that the final partial sum equals the total sum, that an adjacent transposition can affect only the relevant intermediate partial sum, that the changed partial sum has the expected form, and that maximality at a position admitting an adjacent successor swap forces a corresponding forbidden-set membership fact. The Aristotle output summary identifies the intended remaining mathematical step as the global counting step needed to show that these membership facts produce at least n distinct forbidden values, contradicting the cardinality assumption |M| < n; the Lean source itself does not reduce the main theorem to a separately encoded counting lemma. This case study gives an inspectable example of a central limitation in AI-assisted formalization, namely that local proof search can succeed while the global combinatorial bookkeeping required for a theorem remains unresolved. The paper contributes a reproducible Lean artifact and a precise analysis of its verified and unverified proof content.

---


### 329. [TrajTok: Adaptive Spatial Tokenization for Trajectory Representation Learning](https://arxiv.org/abs/2605.20134)

**<font color=#1a73e8>作者：</font>** Zhen Xiong, Shang-Ling Hsu, Cyrus Shahabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning generalizable trajectory representations from raw GPS traces remains difficult because the data is continuous, noisy, and irregularly sampled. Spatial tokenization is also challenging: fine grids yield sparse cells with weak embeddings, while coarse grids merge heterogeneous movement patterns into the same token. We present TrajTok, a trajectory encoder with a simple pretraining recipe for transferable trajectory embeddings. TrajTok first learns a multi-resolution hexagonal cell partition from the spatial distribution of GPS points, converting noisy GPS sequences into discrete cell tokens. To capture both geometry and kinematics, it uses a factorized transformer encoder with early per-modality self-attention blocks, cross-attention fusion layers, and spatiotemporal rotary position embeddings, ST-RoPE, to encode where and when each token occurs. TrajTok is pretrained with masked-token modeling that recovers both geometric structure and kinematic patterns from partial trajectory observations. On the Porto dataset, a frozen TrajTok encoder with lightweight task adapters achieves strong performance across trajectory similarity search, classification, estimated time of arrival, and full travel-time regression, outperforming multiple task-specific methods. The same frozen encoder supports both geometry-dominated and kinematics-dominated tasks, suggesting that TrajTok learns transferable trajectory structure rather than task-specific shortcuts. These results indicate that learned multi-resolution spatial tokenization combined with masked-token pretraining is a promising direction for general-purpose trajectory foundation models.

---


### 330. [TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization](https://arxiv.org/abs/2605.20150)

**<font color=#1a73e8>作者：</font>** Chonghao Zhong, Linfeng Shi, Hua Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training 3D Gaussian Splatting (3DGS) at billion-primitive scale is fundamentally memory-bound: each Gaussian primitive carries a large attribute vector, and the aggregate parameter table quickly exceeds GPU capacity, limiting prior systems to tens of millions of Gaussians on commodity single-GPU hardware. We observe that 3DGS training is inherently sparse and trajectory-conditioned: each iteration activates only the Gaussians visible from the current camera batch, so GPU memory can serve as a working-set cache rather than a persistent parameter store. Building on this insight, we introduce TideGS, an out-of-core training framework that manages parameters across an SSD-CPU-GPU hierarchy via three synergistic techniques: block-virtualized geometry for SSD-aligned spatial locality, a hierarchical asynchronous pipeline to overlap I/O with computation, and trajectory-adaptive differential streaming that transfers only incremental working-set deltas between iterations. Experiments show that TideGS enables training with over one billion Gaussians on a single 24 GB GPU while achieving the best reconstruction quality among evaluated single-GPU baselines on large-scale scenes, scaling beyond prior out-of-core baselines (e.g., approximately 100M Gaussians) and standard in-memory training (e.g., approximately 11M Gaussians).

---


### 331. [When Does Model Collapse Occur in Structured Interactive Learning?](https://arxiv.org/abs/2605.20151)

**<font color=#1a73e8>作者：</font>** Yuchen Wu, Kangjie Zhou, Weijie Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The proliferation of generative artificial intelligence has given rise to an interactive learning environment, where model parameters are continuously updated using not only data generated by natural processes, but also synthetic outputs produced by other models. This paradigm introduces two major challenges: (1) training data are no longer drawn exclusively from the target population, undermining a core assumption of classical statistical learning, and (2) model training processes become inherently correlated, as models interact with one another through repeated exposure to each other's synthetic outputs in a potentially complex manner. Establishing reliable statistical inference in such structured interactive learning environments therefore remains an important open problem. In particular, there is growing concern about model collapse, a phenomenon in which the performance of generative models progressively degrades as they are trained on synthetic data produced by earlier model generations.
Prior work on model collapse primarily focuses on a single model trained on its own output, failing to capture model performance in multi-model interactive settings. In this work, we fill this gap by investigating the performance of generative models in an interactive learning environment with general interaction patterns. In particular, we formalize model interactions using directed graphs and show that the occurrence of model collapse depends critically on the topology of the interaction graph. We further derive an explicit necessary and sufficient condition characterizing when model collapse occurs, and establish finite-sample results for linear regression and asymptotic guarantees for general M-estimators. We support our theoretical findings through extensive numerical experiments.

---


### 332. [SAGE: Scalable Automatic Gating Ensemble for Confident Negative Harvesting in Fraud Detection](https://arxiv.org/abs/2605.20157)

**<font color=#1a73e8>作者：</font>** Sudheer Tubati, Amit Goyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Music streaming fraud, where bad actors artificially inflate stream counts to manipulate chart rankings and royalty payments, poses a significant threat to streaming services and legitimate content creators. Traditional fraud detection approaches struggle with a critical challenge: many legitimate edge cases, including super-fans and sleep-music sessions, exhibit activity patterns that closely mimic those of coordinated fraud. We present SAGE, a novel counterfactual-aware negative harvesting approach that combines SimHash-based stratified sampling with a modular gating ensemble for confident negative identification from unlabeled data. Our ensemble architecture employs pluggable statistical gates (currently instantiated with Mahalanobis distance and k-NN density) with configurable voting thresholds enabling adaptive precision-recall trade-offs. This addresses the representation bias problem in Positive-Unlabeled learning by ensuring comprehensive coverage of rare behavioral cohorts through floor-constrained sampling. Evaluation demonstrates strong precision and recall on held-out data. The approach generalizes across fraud detection domains, achieving strong performance on both customer-level and artist-level fraud without modification to the core methodology.

---


### 333. [Interpretable Computer Vision for Defect Detection in X-ray Tomography of Aerospace SiC/SiC Composites](https://arxiv.org/abs/2605.20159)

**<font color=#1a73e8>作者：</font>** Antonio Peña Corredor, Julien Lesseur, Romain Nunez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-destructive testing of aerospace SiC/SiC composites via X-ray computed tomography (XCT) relies on expert visual assessment, with current workflows offering limited traceability for accept/reject decisions. Deep convolutional networks can automate defect detection, yet their black-box nature conflicts with the transparency that industrial inspection practice demands. To close this gap, we introduce p-ResNet-50, a convolutional framework extended with a prototype layer that couples high detection accuracy with case-based explanations. Six learned prototypes are explicitly aligned with expert-defined semantic categories-healthy matrix, matrix--air interfaces, pores, line-like defects, and mixed morphologies-so that every classification is traceable to a physically meaningful reference. Two novel regularisation terms, anchor-based and medoid-based, tether prototypes to expert-selected patches and prevent prototype collapse, addressing a known limitation of prototype networks. Latent-space analysis via UMAP delineates semantically coherent sub-domains and maps zones of uncertainty where misclassifications concentrate, giving inspectors an explicit picture of where the model is-and is not-reliable. The framework is validated on an XCT patch dataset of approximately 12,000 patches extracted from four defect-rich SiC/SiC laboratory specimens. Taking a black-box ResNet-50 as a baseline (ROC-AUC = 0.991), the prototype extension achieves comparable performance (accuracy 0.957 vs. 0.959; ROC-AUC 0.994 vs. 0.993) while trading a slight reduction in sensitivity for higher precision and specificity. Each decision is backed by representative evidence patches, and the model explicitly flags its uncertainty regions. Beyond defect mapping, the framework establishes a reusable methodology for embedding domain-expert knowledge into prototype networks, applicable to other XCT inspection scenarios requiring traceable, auditable decisions.

---


### 334. [Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR](https://arxiv.org/abs/2605.20164)

**<font color=#1a73e8>作者：</font>** Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has made post-training highly effective when correctness can be checked automatically. However, many important model behaviors require satisfying several qualitative criteria at once. Rubric-based rewards address this setting by grading prompt-specific criteria and aggregating them into a scalar reward. Yet standard static aggregations conflate a criterion's human-assigned importance with its current usefulness as an optimization signal. We show that this assumption breaks down in rubric RL: many important criteria are already saturated or currently unreachable, while criteria that distinguish rollouts are not necessarily those with the largest human weights. We introduce POW3R, a policy-aware rubric reward framework that preserves human weights and category balance as the rubric objective while adapting criterion-level reward weights during training. POW3R uses rollout-level contrast to emphasize criteria that currently separate the policy's outputs, making the GRPO reward more informative without changing the underlying evaluation target. Across three base policies on two datasets spanning multimodal and text-only settings, POW3R wins $24$ of $30$ base-policy/metric comparisons, improving both mean rubric reward and strict completion (the fraction of prompts whose response satisfies every required rubric criterion) over vanilla GRPO with rubric rewards, and reaches the same plateau in $2.5$--$4\times$ fewer training steps. Rubric rewards should therefore distinguish what should matter in the final answer from what can teach the current policy.

---


### 335. [HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands](https://arxiv.org/abs/2605.20167)

**<font color=#1a73e8>作者：</font>** Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely, Md. Samiul Alim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flash floods in Bangladesh's haor wetlands show up with almost no warning. They wreck the annual boro rice harvest. Current setups, built for riverine floods, miss backwater dynamics entirely. These basins are flat. Water does not behave like it does on the Brahmaputra.
We built HaorFloodAlert, a deseasonalized machine learning ensemble that forecasts 72-hour flood probability for the Sunamganj Haor (approximately 8,000 km2). Temperature was acting as a seasonal cheat code - it inflated accuracy by 6.9 pp just because floods happen in warm months. We caught that. We also built an upstream Barak River Sentinel-1 SAR proxy from Silchar, Assam, giving about 36 hours of lead time. Otsu-thresholded SAR change detection validates at 84-91 percent spatial match.
The operational ensemble (RF 0.5625 + XGBoost 0.4375) hits 89.6 percent LOOCV accuracy, 87.5 percent recall, and 0.943 AUC-ROC on 77 real Sentinel-1 events. A three-tier alert pipeline and a BRRI-calibrated boro rice damage estimator are included.

---


### 336. [Multi-axis Analysis of Image Manipulation Localization](https://arxiv.org/abs/2605.20174)

**<font color=#1a73e8>作者：</font>** Keanu Nichols, Divya Appapogu, Giscard Biamby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advanced image editing software enables easy creation of highly convincing image manipulations, which has been made even more accessible in recent years due to advances in generative AI. Manipulated images, while often harmless, could spread misinformation, create false narratives, and influence people's opinions on important issues. Despite this growing threat, there is limited research on detecting advanced manipulations across different visual domains. Thus, we introduce Analysis Under Domain-shifts, qualIty, Type, and Size (AUDITS), a comprehensive benchmark designed for studying axes of analysis in image manipulation detection. AUDITS comprises over 530K images from two distinct sources (user and news photos). We curate our dataset to support analysis across multiple axes using recent diffusion-based inpaintings, spanning a diverse range of manipulation types and sizes. We conduct experiments under different types of domain shift to evaluate robustness of existing image manipulation detection methods. Our goal is to drive further research in this area by offering new insights that would help develop more reliable and generalizable image manipulation detection methods.

---


### 337. [Atoms of Thought: Universal EEG Representation Learning with Microstates](https://arxiv.org/abs/2605.20182)

**<font color=#1a73e8>作者：</font>** Xinyang Tian, Ruitao Liu, Ziyi Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning universal representations from electroencephalogram (EEG) signals is a cutting-edge approach in the field of neuroinformatics and brain-computer interfaces (BCIs). Conventionally, EEG is treated as a multivariate temporal signal, where time- or frequency-domain features are extracted for representation learning. This paper investigates a simple yet effective EEG representation, i.e., microstates. Microstates represent the building blocks of brain activity patterns at a microscopic time scale. We build a universal microstate tokenizer from a large medical EEG dataset by clustering continuous EEG signals into sequences of discrete microstates. The microstate tokenizer is then adopted universally across a series of downstream tasks, including sleep staging, emotion recognition, and motor imagery classification. Experimental results show that EEG representation learning with microstates outperforms traditional time-domain and frequency-domain features under different models and across different tasks. Further analysis shows that microstates offer greater interpretability and scalability, thereby opening up applications in both cognitive neuroscience and clinical research.

---


### 338. [MSAVBench: Towards Comprehensive and Reliable Evaluation of Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2605.20183)

**<font color=#1a73e8>作者：</font>** Yujie Wei, Yujin Han, Zhekai Chen 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation is rapidly evolving from single-shot synthesis to complex multi-shot audio-video (MSAV) narratives to meet real-world demands. However, evaluating such frontier models remains a fundamental challenge. Existing benchmarks are limited in scope and data diversity, and rely on rigid evaluation pipelines, preventing systematic and reliable assessment of modern MSAV models. To bridge these gaps, we introduce MSAVBench, the first comprehensive benchmark and adaptive hybrid evaluation framework for multi-shot audio-video generation. Our benchmark spans four key dimensions, video, audio, shot, and reference, covering diverse task settings, varying shot counts of up to 15, and challenging non-realistic scenarios. Our evaluation framework improves robustness through an adaptive self-correction mechanism for shot segmentation, instance-wise rubrics for subjective metrics, and tool-grounded evidence extraction for complex judgments. Furthermore, MSAVBench achieves high alignment with human judgments, reaching a Spearman rank correlation of 91.5%. Our systematic evaluation of 19 state-of-the-art closed- and open-source models shows that current systems still struggle with director-level control and fine-grained audio-visual synchronization, while modular or agentic generation pipelines offer a promising path toward narrowing the gap between open- and closed-source models. We will release the benchmark data and evaluation code to facilitate future research.

---


> [!TIP]
> 当前位于：**301-338**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-338**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
