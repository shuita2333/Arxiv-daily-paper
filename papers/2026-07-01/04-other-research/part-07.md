# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 301. [Efficient Visual Pointing for Embodied AI:Agent-Driven Data Synthesis, Cross-Block Attention, and Iterative Correction](https://arxiv.org/abs/2606.29850)

**<font color=#1a73e8>作者：</font>** Zijian Hong, Qi Lv, Yuxiang Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual pointing maps a language instruction to pixel co ordinates, a core skill for embodied AI. We describe our PointArena 2026 solution, which achieves 77.2% overall accuracy and ranks second on the benchmark. The ap proach targets three failure modes. First, agent-driven syn thesis builds large semantic and anchor-relative candidate pools; the server inventory contains 55,372 processed out puts, 53,772 de-duplicated sample IDs, and 37,574 train able completed or accepted rows. Second, a determinis tic steerable-data pipeline creates a verified 10,000-sample main set, plus reserve samples, using masks, templates, and path verification. Third, two model-side modules address complementary errors: AttnRes adds gated cross-block at tention for steerability, while ABC correction encodes per turbed coordinates with visual features for general coordi nate grounding. Category-aware routing combines comple mentary specialists; local validation used to select experts records 93.9% Affordance, 82.6% Spatial Relation, 78.2% Reasoning, 70.4% Counting, and 63.0% Steerability.

---


### 302. [RainODE: Continuous-Time Precipitation Forecasting with Latent Neural ODEs](https://arxiv.org/abs/2606.29855)

**<font color=#1a73e8>作者：</font>** Yeeun Seong, Doyi Kim, Minseok Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In precipitation forecasting, not only accuracy but also temporal resolution is critical. However, increasing temporal resolution is constrained by observational limitations and the computational cost of dense discrete modeling. To overcome this limitation, we reformulate precipitation forecasting as a continuous-time dynamical system and propose RainODE, a framework that models precipitation evolution in latent space using a Neural ODE. This formulation enables derivative-consistent temporal dynamics and captures the dominant large-scale advective motion of precipitation systems. Nevertheless, a purely deterministic ODE struggles to represent non-advective intensity changes such as localized growth, decay, and sub-grid variability, often leading to over-smoothed predictions. To address this issue, we introduce a stochastic source modeling module based on a Brownian Bridge formulation, which refines residual intensity variations and restores fine-grained structures while preserving advective consistency. By combining deterministic continuous dynamics with stochastic refinement, RainODE enables arbitrary-time inference while maintaining sharp predictions. Experiments on SEVIR and the newly introduced Radar-based Precipitation Integrated Dataset (RAPID) demonstrate consistent improvements across multiple temporal intervals and precipitation regimes. The code is available at this https URL.

---


### 303. [Comparing Chatbot Performance Enhanced with Persistent Homology](https://arxiv.org/abs/2606.29857)

**<font color=#1a73e8>作者：</font>** Nithisha Raghavaraju, Barbara Giunti, Bastian Rieck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chatbots have become increasingly prevalent across various domains, offering automated assistance in many areas, especially mental health support. The training is done using extremely large datasets, which are sometimes not available in very specific domains. Moreover, it would sometimes be ideal to train the chatbot with personal information about the patients, which, of course, cannot be done on shared servers since it would violate patient confidentiality. Hence, being able to improve the performance of a chatbot, possibly trained locally and on a restricted dataset, without having to increase the dataset itself, would be extremely beneficial. In this work, we will enhance the input datasets using persistent homology (PH) vectorizations computed from the raw datasets themselves. Then we will compare, across several metrics, the performance of multiple chatbot models with or without the PH enhancement. Our experiments suggest that, while at times the PH enhancement is not particularly beneficial, it sometimes brings remarkable advantages for virtually no cost.

---


### 304. [Smooth Scaling Laws Hide Stepwise Token Learning](https://arxiv.org/abs/2606.29858)

**<font color=#1a73e8>作者：</font>** Pingjie Wang, Zechen Hu, Peiru Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model loss follows remarkably regular scaling laws over model and data size, yet it remains unclear why the aggregate loss should exhibit a power-law form. Existing explanations often attribute this regularity to a heavy-tailed spectrum of pattern difficulty in natural language, but this view has not been directly validated at token-level granularity in large-scale real-data training. We present a token-level framework that decomposes scaling laws into localized learning events of individual contextualized tokens. By fitting token loss trajectories with sigmoids, we show that token learning is concentrated in localized transitions, giving rise to a learning-time spectrum that dominates the scaling-law shape. Across more than one hundred pre-training runs on large and diverse real-language corpora with modern LLM architectures, scaling up to 6B parameters and 300B training tokens, the measured learning-time spectrum quantitatively reconstructs the validation loss derivative along the training-step $T$, data-scale $D$, and model-scale $M$ axes. We further show that the same signal is actionable: by reshaping the training distribution according to when tokens become learnable, we alter the optimization trajectory and achieve 11\% faster validation-loss reduction. These results provide direct empirical evidence that scaling laws are governed primarily by the distribution of token-level learning times, and that this distribution can be used not only to explain scaling behavior but also to improve training performance.

---


### 305. [Exploring Motivations for Algorithm Mention in the Domain of Natural Language Processing: A Deep Learning Approach](https://arxiv.org/abs/2606.29859)

**<font color=#1a73e8>作者：</font>** Yuzhuo Wang, Yi Xiang, Chengzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rise of data-intensive science, algorithms have become central to scientific research. In academic papers, algorithms are mentioned for different purposes, such as describing, using, comparing, or improving methods for specific research tasks. Identifying these purposes can reveal relationships among algorithms and help assess their roles and value. Taking natural language processing (NLP) as an example, this study proposes a sentence-level framework for identifying, analyzing, and tracing the evolution of motivations for mentioning algorithms. We first identify algorithm entities and algorithm-related sentences from full-text papers through manual annotation and machine learning. We then classify mention motivations using pretrained models and data augmentation, and analyze their distribution and temporal evolution. The results show that deep learning models trained with augmented data outperform traditional machine learning models in motivation classification. In NLP papers, more than half of algorithm-related sentences express direct use, whereas improvement is the least frequent motivation. The diversity of motivations has increased over time. For specific algorithm categories, grammar-based algorithms are more often mentioned for description, while machine learning algorithms are more often mentioned for use. Over time, use motivations have gradually replaced description motivations across different algorithms, and the number of motivation types associated with individual algorithms has declined significantly. This study reveals how authors mention algorithm entities in academic writing and provides a basis for future research on algorithm relationship identification and algorithm impact evaluation.

---


### 306. [Beyond Triplet Plausibility: Relation Set Completion in Knowledge Graphs](https://arxiv.org/abs/2606.29860)

**<font color=#1a73e8>作者：</font>** Zihao Zheng, Borui Cai, Yao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) organize real-world knowledge as triplets and underpin many downstream applications. Due to their inherent incompleteness, knowledge graph completion (KGC) is widely studied and is typically formulated as triplet prediction, with link prediction as the dominant paradigm. However, this formulation focuses on the incompleteness of triplet-wise information and overlooks the incompleteness of entity-relation compatibility information. To address this limitation, we introduce a relation set completion task (RSC), which complements the link prediction task and aims to reason about missing relations that are semantically compatible with a given entity. We further propose a Relation Set Embedding model (RelSetE), which models latent patterns among the observed relations of entities to infer missing ones. To evaluate RelSetE, we derive three benchmark datasets from standard KG benchmarks. Extensive experiments demonstrate that RelSetE effectively captures entity-relation compatibility patterns and performs favorably in inferring missing relations of entities. Code and data are publicly available.

---


### 307. [SUMO: Segment and Track Any Motion with Nonlinear State Space Models](https://arxiv.org/abs/2606.29861)

**<font color=#1a73e8>作者：</font>** Kexin Tian, Sixu Li, Keshu Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Object Tracking (VOT) and Moving Object Segmentation (MOS) are two fundamental tasks in computer vision that involve both spatial and temporal object dynamics. Existing methods rely predominantly on visual cues and thus often falter in real-world scenarios where object motions are inherently complex and nonlinear. To address this limitation, we propose SUMO, a zero-shot, training-free, unified framework integrating nonlinear dynamics with vision-based segmentation for accurate and consistent VOT and MOS. Specifically, we develop a nonlinear State Space Model (SSM) inspired by robotics principles to capture the complex object dynamics. Building on this model, we propose a Selective Unscented Filter (SUF) for accurate state estimation, which features a joint scoring mechanism and dynamically fuses multi-source predictions to identify the most plausible object state over time. Furthermore, we apply a memory selection mechanism to evaluate the reliability of memory frames. Our extensive experimental results show that SUMO achieves state-of-the-art performance on both VOT and MOS tasks.

---


### 308. [RoAd-RL: A Unified Library and Benchmark for Robust Adversarial Reinforcement Learning](https://arxiv.org/abs/2606.29867)

**<font color=#1a73e8>作者：</font>** Adithya Mohan, Daniel Kriegl, Torsten Schön  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Reinforcement Learning (DRL) has achieved significant success in robotics and autonomous systems, yet remains vulnerable to adversarial perturbations that can severely degrade performance. Research in adversarial reinforcement learning is often limited by fragmented implementations, inconsistent evaluation protocols, and poor reproducibility. To address these challenges, we present \textbf{RoAd-RL}, an open-source benchmarking framework that provides unified abstractions for policies, attacks, defenses, and robustness metrics, together with reproducible evaluation pipelines and seamless integration with Stable-Baselines3 and Gymnasium.
We evaluate DQN, PPO, and SAC agents in LunarLander and Highway-v0 under 192 attack-defense configurations. Results reveal substantial variations in robustness across environments and show that some commonly used defenses can be more detrimental than the attacks they aim to mitigate, while temporal smoothing consistently achieves strong performance. RoAd-RL establishes a standardized benchmark for adversarial reinforcement learning research and is publicly available at this https URL.

---


### 309. [AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes](https://arxiv.org/abs/2606.29871)

**<font color=#1a73e8>作者：</font>** Anjali Rao, Nikhil Kamalkumar Advani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the AI Training Manager, a bounded LLM-based supervisory controller for adaptive machine learning training. Standard training pipelines often rely on fixed recipes or single-axis schedulers, which can struggle with mid-run failures such as severe overfitting, loss imbalance, exploration collapse, or unsafe exploration. Rather than replacing mathematical optimizers or acting as an unconstrained coding agent, the manager operates through a schema-conditioned interface: it reads structured telemetry snapshots from an active run, audits a constrained action space, and returns validated updates to training parameters such as learning rate, regularization strength, loss-weight coefficients, and exploration settings. We evaluate this architecture across supervised language modeling and reinforcement learning. On TinyStories, the manager detects and corrects overfitting, achieving a validation loss 60% lower than the baseline while producing auditable intervention logs. In this supervised setting, we additionally show that manager inference does not need to block the training loop: training can continue while a manager response is pending, and validated updates can be applied asynchronously once available. In a robotic manipulation reinforcement-learning task, we use the same bounded decision interface in an episodic closed-loop setting, where manager updates are applied at evaluation or checkpoint boundaries. The manager mitigates both conservative and unsafe exploration regimes. These results suggest that schema-conditioned LLMs can serve as bounded supervisory managers for live training runs, complementing conventional optimizers and schedulers with interpretable, multi-axis intervention capabilities

---


### 310. [Decision-Value Attribution in Predict-then-Optimize Systems](https://arxiv.org/abs/2606.29878)

**<font color=#1a73e8>作者：</font>** Konstantinos Ziliaskopoulos, Alexander Vinel, Alice E. Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models are increasingly embedded in operational decision-making, yet standard explanation methods typically explain forecasts rather than the decisions those forecasts induce. This distinction is important in predict-then-optimize systems: large forecast changes may leave the optimizer's action unchanged, while small changes can alter the selected decision and its realized value. We propose Decision Value Attribution (DVA), a Shapley-based framework for attributing the value of a fixed prediction--optimization pipeline. The framework defines cooperative games whose payoff is the downstream decision value, allowing the players to be information sources, optimization or design parameters, or both. We present three variants: InfoDVA attributes value to features, DesignDVA attributes value to operational configurations, and Decision-Value Interactions (DVI) quantifies how information and design jointly create value. We further distinguish post-DVA, which evaluates decisions using realized outcomes, from pre-DVA, which evaluates decisions under the model's full prediction. This separation turns attribution into a decision-level diagnostic of whether the model's operational beliefs align with realized performance. The resulting attributions are expressed in the units of the operational objective and decompose the gain or loss relative to a baseline. Case studies in electricity storage arbitrage and emergency medical service coverage show that predictive explanations can be poor proxies for operational value, that DVA can guide targeted information-control interventions, and that optimization configurations determine when predictive information is decision-relevant.

---


### 311. [IREU: Identity-Related Encoder-Only Unlearning for Customized Portrait Generation](https://arxiv.org/abs/2606.29880)

**<font color=#1a73e8>作者：</font>** Chaoyi Shi, Shanshan Zhang, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Customized Portrait Generation (CPG) technologies have been widely used to generate high-fidelity person images given an input image indicating the identity and a text prompt indicating the required edits. Yet these methods pose significant privacy risks by spreading fake visual information. Against such risks, each public generator should be able to suppress its generation ability for a particular person when requested. Therefore, in this work we investigate the identity unlearning problem for CPG. Since there are no previous methods in this field, we propose a simple baseline that updates the image encoder by minimizing identity similarity between generated and input images for target identities to be unlearned, while maximizing it for identities to be retained. However, we find such a global perturbation in the feature space harms the fidelity of generated images for other identities to be retained. To solve this problem, we propose a novel method IREU, which first locates identity-related features in an offline manner and then only performs feature perturbations on them. The experimental results show that our proposed method IREU achieves better identity unlearning performance for target identities to be unlearned, and also keeps high fidelity for other identities to be retained. In addition, our unlearned image encoder is generalizable across different generators with the same encoder without fine-tuning, which is friendly for deployment in practice.

---


### 312. [Building artificial intelligence virtual tissue (AIVT) for tissue state representation, feature prediction, and dynamic simulation](https://arxiv.org/abs/2606.29883)

**<font color=#1a73e8>作者：</font>** Qiqi Lu, Qianjin Feng, Shaoqun Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling tissue states and their transitions is essential for understanding tissue homeostasis in health and pathological remodeling in disease. However, conventional computational modeling approaches are inadequate to capture the complexity of tissues as spatially organized, multiscale biological systems. Artificial intelligence (AI) has shown a remarkable ability for representing intricate systems, creating new opportunities to characterize tissue states and their transitions. Here, we propose the concept of AI virtual tissue (AIVT), an AI framework grounded in spatial multimodal data for modeling tissues in health and disease. AIVT is designed to learn unified, spatially resolved, and dynamically manipulatable representations of tissue state, enabling tissue state representation and analysis, molecular and morphological feature prediction, and simulation of spatiotemporal tissue dynamics. We outline the fundamental assumptions, core capabilities, architectural components, as well as data and algorithm foundations of AIVT as a framework for AI-driven tissue modeling.

---


### 313. [SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing](https://arxiv.org/abs/2606.29887)

**<font color=#1a73e8>作者：</font>** Jiacheng Zhang, Haoyu He, Sen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In real-world applications, guardrails are often expected to identify unsafe user-model interactions according to application-specific safety policies, rather than relying on predefined risk taxonomies. In this work, we study this setting under the paradigm of in-context policy guardrailing, where guardrails predict safety violations based on policy specifications provided in context. To systematically evaluate this capability, we introduce SafePyramid, a safety benchmark comprising 1,000 multi-turn conversations across 10 domains and 3,000 corresponding application-specific policies, which together contain 61,699 distinct natural-language rules. SafePyramid organizes the evaluation into three difficulty levels: L0 evaluates individual-rule understanding, L1 evaluates reasoning over rule dependencies, and L2 evaluates adaptation of full novel policy frameworks defined in context. To ensure benchmark quality, we employ a rigorous multi-stage pipeline to construct and validate the benchmark. Using SafePyramid, we evaluate 10 frontier LLMs and 5 policy-configurable guardrails and find that in-context policy guardrailing remains highly challenging: even the best-performing model, GPT-5.5, exactly identifies the full set of violated rules in only 54.0%, 35.3%, and 12.9% cases on L0, L1, and L2, respectively. These results highlight the limitations of current guardrails and call for stronger in-context policy guardrails that can reliably execute policies, resolve rule dependencies, and adapt to novel policy frameworks.

---


### 314. [Same Concept, Different Directions: Cross-Modal Feature Heterogeneity in Sparse Autoencoders](https://arxiv.org/abs/2606.29888)

**<font color=#1a73e8>作者：</font>** Chungpa Lee, Jihoon Kwon, Kyle Min 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models map images and text into a joint embedding space. However, these embeddings often entangle multiple semantic features, which limits their interpretability and controllability. While sparse autoencoders have emerged as a useful tool for decomposing these embeddings into monosemantic features, their application to joint embedding spaces has largely relied on an implicit, untested assumption that semantically corresponding features share the same directions across modalities. In this paper, we challenge this assumption by identifying discrepancies in feature directions for the same concept across image and text modalities, a phenomenon we term cross-modal feature heterogeneity. We demonstrate that this heterogeneity is a key driver of the modality split, where a shared concept activates different latents depending on the modality. This finding further reveals why aligning latent activations alone is insufficient to resolve the underlying feature mismatch. Motivated by this observation, we propose an approach that trains modality-specific sparse autoencoders to preserve each modality's feature geometry, and then aligns corresponding features post hoc. Our method improves reconstruction fidelity and enhances performance in cross-modal retrieval and concept steering.

---


### 315. [Golden Hour Divide: Trauma Care Accessibility and Resource Vulnerability in Sri Lanka](https://arxiv.org/abs/2606.29889)

**<font color=#1a73e8>作者：</font>** Sonath Kirindage, Vihanga Nimsara, Sakindu Rajapaksa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Timely intensive care dictates survival, yet emergency infrastructure remains unevenly distributed across Sri Lanka. While pre-hospital services have expanded, the transition to definitive care remains a critical bottleneck. This study evaluates national emergency resilience by quantifying the gap between clinical demand and the availability of specialized resources across all 25 districts. Using the latest national epidemiological data and terrain-aware H3 hexagonal modeling, we analyzed accessibility for seven critical conditions based on spatial gaps, clinical need-gaps, lethality, coverage, and resource availability. Based on these metrics, unsupervised K-Means clustering was applied to categorize districts into four policy-actionable archetypes: Critical Structural Exclusion, Institutional Mirages, Operational Capacity Strain, and High-Resilience Benchmarks. Our study suggests that severe service deficits exist in the Northern and Eastern provinces, where spatial gaps exceed 70%, rendering the Golden Hour operationally impossible. Notably, specialist scarcity drives systemic pressure more than bed capacity; underserved regions effectively function as institutional mirages. This study suggests that improving accessibility by 25% in high-priority clusters would reduce the national need-gap by 9.65%, providing a roadmap for the strategic redistribution of specialists to ensure healthcare equity.

---


### 316. [Timesteps of Mamba Align with Human Reading Times](https://arxiv.org/abs/2606.29904)

**<font color=#1a73e8>作者：</font>** Yuji Yamamoto, Shinnosuke Isono, Yoshinobu Kawahara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study demonstrates an alignment of per-word processing time in a popular state-space language model Mamba and human readers. In Mamba, the recurrent state transition at each layer conceptually takes some duration of time, the discretization timestep $\Delta_t$, determined dynamically in response to the input. Using a naturalistic reading dataset, we show that the per-word timestep from Mamba is a significant predictor of human reading times, and remains significant even when known predictors such as GPT-2 surprisal are controlled for. We further suggest, through formal analysis of Mamba's architecture and internal dynamics, that Mamba can serve as a new, valuable lens to look at human real-time language processing with ever-updated memory, because it allows us to look at how each module (layer) weighs short- and long-term information retention, and how noise may interact with dynamic, continuous memory representation. Code is available online.

---


### 317. [StrucTab: A Structured Optimization Framework for Table Parsing](https://arxiv.org/abs/2606.29905)

**<font color=#1a73e8>作者：</font>** Gengluo Li, Shangpin Peng, Chengquan Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table parsing aims to convert table images into structured, machine-readable representations, a task requiring the joint perception of complex spatial layouts and textual content. While recent vision-language models (VLMs) enable end-to-end parsing, they typically rely on direct supervision of the final output, thereby bypassing the explicit intermediate reasoning that is crucial for understanding complex table structures. Furthermore, attempts to optimize these models using reinforcement learning (RL) are often hindered by unstable or ambiguous reward designs, limiting potential performance gains. To address these limitations, we propose StrucTab, a table parsing model learned through intermediate structural supervision and reward decomposition. At the modeling level, by decomposing the parsing process into human-inspired subtasks, such as row-column counting and merged-cell analysis, StrucTab progressively unifies them through a sequential reasoning strategy. At the optimization level, we introduce Uni-TabRL, a unified RL framework that leverages decomposed rewards (validity, structure, and content) to provide stable and informative optimization signals. Finally, at the evaluation level, we present TableVerse-5K, a large-scale, challenging benchmark encompassing diverse, real-world table scenarios. Extensive experiments demonstrate the state-of-the-art performance of StrucTab across all evaluated public benchmarks and significant improvements on TableVerse-5K, validating the effectiveness of explicit structural modeling and decomposed reward optimization. Code and benchmark are publicly available at this https URL.

---


### 318. [CW-B: Class Weighted Boosting Framework for Imbalance Resilient Multi Class Cardiac Phenotyping](https://arxiv.org/abs/2606.29907)

**<font color=#1a73e8>作者：</font>** Sijia Li, Xiaoyu Tan, Chen Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiac discharge phenotyping informs post-discharge treatment and follow-up, but real-world records are often incomplete and class-imbalanced, increasing the risk of missed high-risk phenotypes. We propose CW-B, a clinical risk-aligned class-weighted XGBoost pipeline for five-class cardiac discharge phenotyping under real-world class imbalance and missingness. CW-B combines fold-specific class-balanced instance weighting, missingness-indicator augmentation, and classwise error auditing to improve recognition of clinically prioritized phenotypes while preserving interpretable and auditable decision logic. In five-fold stratified cross-validation, CW-B achieves the best Accuracy, Macro-F1, Balanced Accuracy, and Prioritized F1 among tree-based, ensemble, and neural baselines. Overall, CW-B provides a practical and deployment-oriented approach for more reliable cardiac discharge phenotyping in real-world clinical settings.

---


### 319. [A causal modeling perspective on decision theory](https://arxiv.org/abs/2606.29911)

**<font color=#1a73e8>作者：</font>** Arvid Sjölander  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision theory provides a formal framework for how agents should make choices under uncertainty, drawing on ideas from philosophy, probability, and causality. Despite significant progress, the field still lacks a unified modeling language, and key concepts - such as the distinction between subjective and objective elements, or what it means for a decision theory to perform well - are often left implicit. This can make it difficult to evaluate and compare competing theories, particularly in controversial cases. In this paper, we address these issues by introducing a formal framework for decision theory based on nonparametric structural equation models (NPSEMs), a well-established tool in causal inference. NPSEMs provide a unified foundation for representing agents, counterfactuals, and causal relationships, allowing for unambiguous definitions of EDT and CDT. Building on this foundation, we propose a novel decision theory - personal decision theory - which instructs agents to maximize a subjective model of their own counterfactual utility. We introduce a formal performance metric based on hypothetical interventions that enforce a given decision theory across a population - such as might be achieved through education or policy -- and show that, under certain assumptions, personal decision theory is optimal with respect to this metric. Throughout, we use the smoking lesion problem as a running example and conclude with a formal analysis of Newcomb's problem. Our aim is to provide decision theory with a clearer modeling language and firmer evaluative ground, thereby enabling more rigorous comparisons and facilitating conceptual progress in the field.

---


### 320. [H-GRPO: Permutation-Invariant Reinforcement Learning for Grounded Visual Reasoning](https://arxiv.org/abs/2606.29915)

**<font color=#1a73e8>作者：</font>** Eric Peh, Debaditya Roy, Basura Fernando  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) often achieve high performance on benchmarks while remaining "black boxes", yet they remain prone to hallucination or rely on superficial shortcuts. In this work, we propose a framework designed to enhance both performance and interpretability through De-compositional Evidence Grounding. Unlike monolithic inference approaches, our approach forces the model to decompose a global query into a sequence of atomic sub-questions, each requiring an explicit sub-answer and critically a localized evidence bounding box. By grounding intermediate logical steps (e.g. identifying a container, analyzing liquid properties, and assessing environmental context) in specific visual regions, we construct a structured reasoning path that mirrors human-like deduction. This allows the final answer to emerge as a logical consequence of verified visual facts rather than a statistical guess.

---


### 321. [EVAF: A Test-Retest Protocol for Selective Parametric Consolidation](https://arxiv.org/abs/2606.29916)

**<font color=#1a73e8>作者：</font>** Haoliang Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-running language agents need mechanisms for deciding which experiences should persist after the working context is gone. Retrieval systems can reinsert past text, but they do not by themselves show that an experience has been selectively consolidated into the model's own behavior. We introduce EVAF, an Echo-Valence Attractor Field mechanism for gated LoRA consolidation, and a test-retest protocol for measuring selective parametric consolidation under controlled interference. Across GPT-2 and TinyLlama, EVAF preferentially consolidates high-valence, high-surprise experiences while preserving retrieval-accessible factual memory through a complementary routed memory path. Test-retest measurements show stronger post-interference behavioral persistence than frozen, retrieval-only, and ungated continual-update baselines, while keeping parameter drift and cross-persona contamination low. The results support a separation between memory access and memory depth: retrieving a fact and internalizing an experience are distinct computational operations.

---


### 322. [DCGrasp: Distance-aware Controllable Grasp Generation](https://arxiv.org/abs/2606.29924)

**<font color=#1a73e8>作者：</font>** Hiroyasu Akada, Jesús Pérez, Emre Aksan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating 3D hand-object interactions is essential for applications in robotics, XR, and synthetic data generation, where flexible controllability and strong generalization to diverse object geometries are required. However, existing methods rarely satisfy these requirements, limiting their practical applicability. We present DCGrasp, a distance-aware controllable grasp generation system built on a novel grasp energy term. This term computes Distance Profile, a signed distance from each hand vertex to the nearest object point, coupled with distance-aware weighting, effectively capturing the semantically similar hand-object interaction in near-contact regions while remaining invariant to object and hand identity. Given various controllable signals, DCGrasp first generates a Distance Profile based on a Diffusion Transformer, together with a corresponding candidate hand pose. We then refine the candidate pose through optimization, enforcing consistency between the optimized hand pose and the generated Distance Profile in near-contact regions. Our experiments show that DCGrasp produces high-quality, physically plausible grasps with flexible user control, generalizing to diverse object and hand shapes and scales. Our work establishes a robust and versatile pipeline for the synthesis of controllable 3D hand-object interactions.

---


### 323. [Bandwidth Selection in Kernel Density Estimation for Model Calibration](https://arxiv.org/abs/2606.29925)

**<font color=#1a73e8>作者：</font>** Han Zhou, Teodora Popordanoska, Matthew Blaschko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep learning models are increasingly deployed in high-stakes applications, providing well-calibrated uncertainty estimates has become as critical as achieving high predictive accuracy. While Kernel Density Estimation (KDE) has emerged as a smooth and continuous alternative to traditional binning for quantifying miscalibration, its reliability is heavily dependent on the choice of the kernel bandwidth. Standard selection techniques, such as Maximum Likelihood Estimation (MLE), often fail to produce optimal bandwidths for calibration tasks. In this work, we introduce Risk Alignment (RA), a novel optimization framework that determines the optimal bandwidth by aligning KDE-reconstructed risk with empirical risk. We theoretically demonstrate that this alignment minimizes calibration estimation bias across the data distribution, establishing a principled bandwidth selection criterion applicable to various metrics, including the challenging case of canonical calibration error. Extensive experiments across multiple architectures and datasets show that RA consistently outperforms standard bandwidth selection methods, yielding more reliable calibration assessments.

---


### 324. [Latent-CURE for Breast Cancer Diagnosis](https://arxiv.org/abs/2606.29928)

**<font color=#1a73e8>作者：</font>** Weiyi Zhao, Xiaoyu Tan, Lu Gan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Models have significantly advanced automated breast ultrasound diagnosis. However, most existing frameworks utilize opaque, end-to-end paradigms prioritizing global statistical correlations over structured clinical reasoning. Consequently, these models remain susceptible to shortcut learning amid extreme real-world epidemiological imbalances, often bypassing rare but decisive malignant indicators for dominant benign patterns. To address this disconnect, we propose Latent-CURE, a novel diagnostic framework driven by asymmetric weighted chain-of-thought methodology grounded in latent space reasoning. Unlike traditional approaches, our framework constructs an implicit reasoning trajectory forcing the model to sequentially infer standardized BI-RADS morphological descriptors before converging on a final diagnosis. Furthermore, to combat the extreme scarcity of critical malignant features, we couple this architecture with a dual-asymmetric optimization strategy. By dynamically adjusting margins and weights, this strategy safeguards high-specificity malignant descriptors from being overshadowed by common benign priors. Comprehensive evaluations demonstrate that our knowledge-injected approach provides transparent clinical evidence while achieving robust, accurate diagnostic performance in imbalanced medical cohorts.

---


### 325. [SAGA: Scene-Aware, Goal-Evolving Agents for Long-Horizon CivRealm Strategy Planning](https://arxiv.org/abs/2606.29932)

**<font color=#1a73e8>作者：</font>** Tianyu Jin, Shuo Chen, Yida Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon strategic planning in complex strategy games demands concurrent reasoning across multiple decision domains under imperfect information and sparse reward. Existing LLM-based agents suffer from three systematic failures: scene blindness from raw tile coordinates, context overflow and domain coupling from monolithic state dumps, and shallow cross-game learning that treats each episode in isolation. We present SAGA, an LLM multi-agent framework with three mechanisms each directly targeting one class of failure: (i) a Map-Semantic Scene Graph that encodes typed spatial relations among game entities into per-unit natural-language context, resolving spatial blindness without global token inflation; (ii) a Tool-Augmented Planner that pulls fine-grained domain state on demand and dispatches per-domain directives to dedicated specialist controllers, eliminating context overflow, domain coupling, and mechanical constraint violations; and (iii) a Dual-Horizon Feedback Loop that combines periodic within-game goal generation with structured cross-game causal post-mortem, enabling principled strategic evolution without manual reward engineering. Evaluated on FreeCiv, SAGA attains the highest mean civilization score -- the environment's sole sparse objective reward -- with lower variance than the two strongest baselines, and is the only method that significantly surpasses every baseline on infrastructure construction, the resource axis most readily sacrificed under multi-objective conflict. It outscores the two strongest baselines in most head-to-head games while cutting output tokens (the dominant decoding cost) by 27%. Equipped with the cross-game evolution module, SAGA reaches the highest end-of-chain score across five successive episodes. Ablation studies confirm that each architectural component contributes independently to this advantage.

---


### 326. [LatentRevise: Learning from Zero-Hit Reasoning](https://arxiv.org/abs/2606.29938)

**<font color=#1a73e8>作者：</font>** Yiqiu Guo, Xueting Han, Qi Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is bottlenecked by hard prompts on which correct trajectories have low probability, so sampling misses them within a practical budget and leaves the policy update with little useful signal. We frame such zero-hit prompts as RLVR's sampling frontier, where new reasoning behavior is most valuable yet least likely to be sampled. Importantly, failed rollouts can be informative: they expose where the model's reasoning went wrong. We introduce LatentRevise, a first-order latent revision method that recovers training signal for this zero-hit regime. Given a failed rollout and the gold answer as an anchor, LatentRevise optimizes the input embeddings of its reasoning prefix under two complementary gradients, moving the prefix away from the failed continuation and toward the gold answer. The optimization is constrained to the convex hull of the model's vocabulary embeddings, so each update moves the latent toward a real token embedding rather than an arbitrary feature direction. We find that continuations from the revised prefix lengthen, exhibit self-reflection, and reach correct answers missed by the original rollouts. Used as training data, these trajectories improve SFT and RLVR on math benchmarks over standard baselines.

---


### 327. [Scene-aware Prediction of Diverse Human Movement Goals](https://arxiv.org/abs/2606.29942)

**<font color=#1a73e8>作者：</font>** Qiaoyue Yang, Amadeus Weber, Magnus Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipation of human behaviours facilitates autonomous systems in proactive planning. Human behaviour could be stochastic due to varying goals. Human goals typically guide their own movement and could therefore help to predict the human trajectory and human motion in the long-term. To infer the human movement intentions, the environmental context plays a significant role, in addition to the social cues expressed by the individual. Previous works on human goals prediction either require semantic knowledge of the scene, or only tackle interactions with objects. In this paper, we propose a novel multi-goal prediction method using the generative model to address the stochasticity of human movement. It leverages the current RGB scene and the human pose to predict diverse potential future goals of human movement based on the Conditional Variational Autoencoder (CVAE). Our results demonstrate that our approach is capable of generating multiple movement goals in the scene via samplings in latent space of the CVAE and exhibits generalization capability across scenarios in GTA-IM dataset and PROX dataset. Code is publicly available at \href{this https URL}{\texttt{this https URL}}.

---


### 328. [Improved Predictive Performance and Interpretability for Mesomorphic Neural Networks Using Local Fidelity Regularization](https://arxiv.org/abs/2606.29951)

**<font color=#1a73e8>作者：</font>** Hugo L. Hammer, Vajira Thambawita, Kristoffer Herland Hellton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretable Mesomorphic Neural Networks (IMNs) offer a promising framework that combines the predictive power of deep neural networks with the interpretability of linear models. However, the original formulation lacks safeguards to ensure that the learned interpretations are in fact reliable. In particular, the network is free to concentrate all explanatory variance into a single weight of the linear output layer, achieving strong predictive performance while producing interpretations that are largely meaningless. Paradoxically, the L1 penalty proposed to encourage sparse solutions exacerbates this problem by further incentivizing such degenerate configurations.
To address this vulnerability, we introduce Local Fidelity Regularization (LFR), a novel penalty term that prevents degenerate weight collapse by aligning the linear output weights with local data variations. This structural constraint guarantees faithful explanations and substantially improves the reliability of model interpretations. Furthermore, empirical evaluations across the OpenML benchmark suite demonstrate that LFR does not compromise accuracy for explainability; rather, it achieved improved AUROC over the unregularized IMN. By yielding results highly competitive with state-of-the-art black-box models, LFR provides the dual benefit of reliable interpretability and superior predictive performance. Source code and usage instructions are available at this https URL.

---


### 329. [Exploiting Local Flatness for Efficient Out-of-Distribution Detection](https://arxiv.org/abs/2606.29952)

**<font color=#1a73e8>作者：</font>** Seonghwan Park, Hyunji Jung, Dongyeop Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting out-of-distribution (OOD) data is crucial for reliable machine learning deployment. Among detection strategies, post-hoc methods are particularly attractive due to their efficiency, as they operate directly on pre-trained networks without requiring retraining. Within this paradigm, one promising direction exploits loss-landscape curvature to estimate model uncertainty; however, such methods incur substantial computational cost and rely on implicit assumptions about how landscape flatness differs between in-distribution (ID) and OOD data. In this work, we provide the first systematic investigation of this curvature discrepancy and show that OOD inputs exhibit larger Hessian curvature than ID data, with the gap widening under stronger distributional shifts. Motivated by these observations, we propose Fold, a lightweight flatness-modulated OOD detector that leverages the feature Hessian and partial feature normalization to improve ID-OOD separability while avoiding costly parameter-space curvature approximations. To optimally adapt this normalization across diverse datasets, we further introduce AutoFold, a self-supervised tuning scheme that synthesizes pseudo-OOD samples via ID logit masking for automatic calibration without requiring external data. Experiments on OOD benchmarks show that Fold outperforms prior methods, improving the average AUROC by 1.63% and reducing FPR95 by 2.30%, while maintaining computational efficiency comparable to a standard forward pass. Supported by theoretical analysis and extensive ablations, Fold provides a principled and practical solution for robust real-world deployment.

---


### 330. [DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation](https://arxiv.org/abs/2606.29961)

**<font color=#1a73e8>作者：</font>** Peyman Hosseini, Ondrej Bohdal, Ahmed Alajrami 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents can solve complex procedural tasks by interacting with environments over multiple turns, but this ability typically depends on large models, long contexts, and repeated inference calls. This makes advanced memory-augmented agents difficult to deploy on resource-constrained devices. We introduce DuoMem, a dual-space distillation framework that transfers procedural problem-solving ability from a large teacher model to compact student models. DuoMem distils in two complementary spaces: (1)context-space distillation, which replaces student-generated memories with higher-quality teacher-generated procedural memories prepended to the student's input, and (2)parameter-space distillation, which fine-tunes lightweight LoRA adapters on successful teacher trajectories. Evaluated on ALFWorld, a challenging embodied decision-making benchmark, DuoMem boosts a 4B-parameter model from 4.3% to 77.9% task success rate, closing most of the gap to a 72B teacher model (87.1%), while adding fewer than 10M trainable parameters and only a few megabytes of pre-computed teacher memories. Moreover, the DuoMem-enhanced 4B model completes tasks over 3x faster than the 72B teacher in wall-clock time, making it viable for real-time edge deployment, which would be challenging for the this http URL ablations across eight models spanning 2B-72B parameters reveal that both distillation axes contribute complementary

---


### 331. [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)

**<font color=#1a73e8>作者：</font>** Chengzeng You, Binbin Xu, Soteris Demetriou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood. Prior work has studied adversarial robustness primarily on isolated 3D object models, while recent LiDAR spoofing attacks target richer and more realistic driving scenes but focus mainly on physical realizability rather than understanding detector behavior or attack efficiency. In this work, we investigate how LiDAR-based detectors rely on spatial evidence in complex scenes and whether these reliance patterns can be exploited to induce failures more efficiently. To this end, we propose an explainability-guided adversarial analysis methodology. We introduce the Saliency-LiDAR (SALL) method, which aggregates Integrated Gradient attributions across scenes to produce universal saliency maps for LiDAR-based 3D object detectors. Guided by these maps, we design the Explainability-aware Frustum Attack (EFA), which selectively perturbs only the most influential frustums rather than uniformly attacking entire object regions. Experiments on KITTI and nuScenes, across detectors such as PointPillars and SECOND, show that EFA reduces detection recall by more than 15 percentage points while requiring 25-50% fewer perturbed frustums than the state-of-the-art non-saliency-aware baseline. These findings reveal that modern 3D detectors concentrate discriminative evidence in a small subset of spatial regions, exposing a structural robustness vulnerability in current LiDAR perception systems. Our code is released at this https URL.

---


### 332. [Variance Reduction on the Camera Axis: Multi-View Score Distillation for 3D](https://arxiv.org/abs/2606.29964)

**<font color=#1a73e8>作者：</font>** Marian Lupascu, Mihai Sorin Stupariu, Ionut Mironica  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Score distillation turns a pretrained 2D diffusion model into a 3D generator, but the per-step gradient is estimated from a single randomly chosen view: it is high-variance and blind to global shape consistency. Prior work addresses this by retraining the diffusion prior on multi-view data; this improves consistency but makes the sampling contribution inseparable from prior quality. We instead isolate the sampling axis. The per-step gradient is one noisy sample of an expectation over views; aggregating K samples per step at a fixed total UNet budget reduces variance without touching the prior. We introduce Multi-View Aggregated Score Distillation (MV-SDI), which aggregates gradients from K views per step via gradient accumulation, keeping peak memory unchanged and the 2D prior frozen, and draws views as antithetic antipodal pairs, a prior-independent geometric property, for balanced angular coverage. At a fixed 10,000-UNet-call budget, K=2 raises CLIP R-Precision from 74.8% to 83.8% and CLIP score from 0.297 to 0.312, with consistent gains on HPSv2 and ImageReward and a 0.0% divergence rate on the 43-prompt benchmark; optimization steps halve as a consequence. K=4 gives a fourfold step reduction at R-Precision 86.9% and CLIP 0.307, still well above the single-view baseline on every alignment metric. MV-SDI is compatible with gradient-based score-distillation pipelines, including Score Distillation via Inversion, and requires no retraining and no multi-view data.

---


### 333. [NeuReasoner: Theory-grounded Mapping of Reasoning Elicitation Boundaries](https://arxiv.org/abs/2606.29971)

**<font color=#1a73e8>作者：</font>** Aydin Javadov, Shyngys Aitkazinov, Tobias Hoesli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of work suggests that the reasoning capabilities of large language models are largely latent in their base form, with post-training primarily amplifying rather than introducing them. However, this evidence comes mainly from mathematical and coding benchmarks, leaving the boundary conditions of that claim largely unexplored, namely which cognitive tasks can be recovered through elicitation and where that recovery fails. To investigate this, we introduce NeuReasoner, a theory-grounded elicitation instrument. At each step, an orchestrator pairs a Neuro Lens, inspired by functional specificity, with a Cognitive Lens, drawn from the Erotetic Theory of Reasoning, and integrates their outputs through internal modularization of a single model, without external tools. We evaluate NeuReasoner on CogBench, a suite of behavioral tasks from cognitive psychology, alongside standard mathematical and coding benchmarks, measuring both its improvement over vanilla inference and its ability to match a model's post-trained thinking mode. At sufficient scale, NeuReasoner matches or exceeds thinking-mode baselines on arithmetic reasoning, code generation, Bayesian reasoning, and reward learning; these gains persist against self-consistency and iterative-refinement baselines matched to NeuReasoner's per-decision call budget. Using NeuReasoner allows us to find clear boundaries: risk-taking and decision making under uncertainty remains hard to recover through elicitation alone, and model scale interacts with elicitation in both directions: widening its advantage on some cognitive signatures while erasing it on others. Overall, through NeuReasoner as a modular, interpretable, theory-grounded elicitation instrument, we empirically map where reasoning elicitation succeeds and fails, beyond the mathematical and coding benchmarks where prior claims have rested.

---


### 334. [First-Order Temporal Logic Tensor Networks](https://arxiv.org/abs/2606.29972)

**<font color=#1a73e8>作者：</font>** Luca Boscarato, Ivan Donadello, Alessandro Artale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most of the existing neuro-symbolic AI methods focus on the scenario of static knowledge where objects do not change according to a temporal dimension. Temporal neuro-symbolic works are still under explored and are mainly developed for time-interval logic or propositional linear temporal logic. There is a lack of models studying linear temporal logics with predicates that deal with objects whose properties and relations change through the time. We present First-Order Temporal Logic Tensor Networks (FOT-LTN) that is an extension of Logic Tensor Networks (LTN) that fills this gap by considering a linear-temporal dimension. In particular, FOT-LTN joins the syntax of First-Order Linear Temporal Logic with the fuzzy (and real-valued) semantics of LTN obtaining a framework that supports both temporal operators and quantifiers and is totally differentiable. A first evaluation regards a temporal knowledge graph completion task on two synthetic datasets showing better performance of FOT-LTN with respect to dedicated (purely neural) methods.

---


### 335. [Learning Efficient 4D Gaussian Representations from Monocular Videos with Flow Splatting](https://arxiv.org/abs/2606.29976)

**<font color=#1a73e8>作者：</font>** Shengjun Zhang, Jinzhao Li, Xin Fei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic 3D scenes from monocular videos is challenging due to scene complexity and temporal dynamics. With the advancement of 3D Gaussian Splatting in novel view synthesis, existing methods extend 3D Gaussians to 4D domain with deformation fields, trajectories or spatiotemporal 4D volumes to model scene element deformation. However, these methods suffer from long training time, low rendering speed or high memory consumption for per-frame reconstruction of 4D volumes, without fully exploiting dense dynamic information. To address this issue, we propose Flow Splatting, which constructs the velocity field and enables the conventional splatting technique to render optical flow from the velocity field to supervise dynamics learning process from monocular videos. Specifically, we extend 4D volumes with time varying means and covariance to represent complex dynamics. Then, we construct and approximate the velocity field naturally based on this representations. While conventional volume rendering techniques support to render color fields, we extend the volume rendering strategy to splat the velocity field by considering the influence of camera motions. We conduct experiments on various benchmarks to demonstrate the efficiency and effectiveness of our method. Compared to the state-of-the-art methods, our model achieves better image quality with less time consumption and higher rendering speed.

---


### 336. [Hephaestus: Toward a Cybersecurity AI Scientist](https://arxiv.org/abs/2606.29981)

**<font color=#1a73e8>作者：</font>** Jiaqi Li, Yang Zhao, Wen Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber offense is moving to machine speed; cyber research itself is not. Existing AI scientist systems make end-to-end research automation increasingly plausible, but they target relatively stable scientific domains. We argue that AI-native cybersecurity is a different kind of scientific object. Its recurring units of study are security events and interaction traces, not static assets; its model and tool substrate is non-stationary, not steady-state; and credible evaluation depends on digital twins, cyber ranges, and auditable evidence rather than on a single benchmark score. We call this object the Cybersecurity AI Scientist. A practical realization is a modular, role-specialized multi-agent research system that coordinates problem framing, threat modeling, tool generation, controlled experimentation, evaluation, governance, and scientific reporting, and that anchors its concrete objectives in a four-zeros frame spanning risk, trust, incident, and energy dimensions. As a representative agenda we focus on AI-native defense, where steady-state perimeters give way to resilient agent legions and the classical category of terminal security is itself being deconstructed into agent security. This paper defines the object, separates it from any single organizational realization, and offers an architecture and an agenda on which later systems, benchmarks, and empirical programs can be built.

---


### 337. [Stabilizing Extrapolation in Looped Transformers via Learned Stochastic Stopping](https://arxiv.org/abs/2606.29983)

**<font color=#1a73e8>作者：</font>** Hsun-Yu Kuo, El Mahdi Chayti, Patrik Reizinger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers, which repeatedly apply a shared transformer block, are an architecturally natural fit for variable-length algorithmic tasks. Although they can exhibit strong length generalization beyond the length of training sequences, this behavior is brittle, yielding high out-of-distribution (OOD) variance, even across well-performing in-distribution solutions. We trace this variance to the spurious correlation in simple algorithmic tasks between sequence length and number of loops. Introducing stochasticity into the number of loops during training sharply reduces OOD variance and stabilizes predictions across inference-time loop counts. To improve upon heuristic randomization schemes, we further analyze RL-Halting as a learned stochastic schedule and find that it generally improves the accuracy-stability trade-off. Across binary addition, Dyck-1, Unique Set, and Copy, learned stochastic stopping often improves this trade-off but can also stabilize a suboptimal computation. Our work suggests that "when to stop" should be treated as a training-time design choice, not merely an inference-time computation-allocation rule.

---


### 338. [AlgoSkill: Learning to Design Algorithms by Scheduling Human-Like Skills](https://arxiv.org/abs/2606.29999)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai, Liang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing an algorithm from a natural-language problem statement requires identifying the problem structure, reading constraints, choosing a suitable paradigm, checking correctness, and refining complexity. Existing large language model (LLM) methods often rely on direct generation or generic self-refinement, leaving these steps implicit. We propose AlgoSkill, which models algorithm design as sequential decision-making over a typed library of algorithmic skills, including abstraction, constraint analysis, state design, data-structure selection, proof checking, counterexample construction, and complexity refinement. A learned scheduler proposes skills from the current design state, while a Monte Carlo Tree Search (MCTS) controller explores skill sequences using verification feedback from compilation, testing, stress testing, and complexity analysis. Experiments on competitive programming and combinatorial optimization benchmarks show that AlgoSkill improves over direct LLM generation, chain-of-thought prompting, self-refinement, and MCTS without typed skills. Ablations show that typed skills, verification-based repair, and search-based scheduling each contribute to performance. These results support treating automatic algorithm design as verification-guided skill scheduling rather than one-shot code generation.

---


### 339. [SICAGE: Speaker-Independent Culture-Aware Gesture Generation using TED4C-L Dataset](https://arxiv.org/abs/2606.30001)

**<font color=#1a73e8>作者：</font>** Ariel Gjaci, Antonio Sgorbissa, Vittorio Murino  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent co-speech gesture generation methods often overlook cultural differences, limiting their effectiveness in human-agent interaction. Moreover, culture-conditioned models are rarely evaluated under speaker-disjoint splits, so apparent "cultural" behavior may be confounded with speaker-specific gesturing style. We introduce SICAGE, a modular framework for culture-aware co-speech gesture generation that conditions motion synthesis models on speaker-independent cultural representations. SICAGE learns these representations from audio and text by treating each speaker as a separate domain while imposing invariance across speakers. This encourages representations to remain culture-discriminative while reducing dependence on speaker identity. The resulting cultural embeddings condition a multimodal generator to produce culturally appropriate gestures. We instantiate this idea with two domain generalization approaches: adversarial learning and Fishr regularization. We further introduce ALaDiT, a real-time diffusion-based gesture generator designed to efficiently incorporate the learned cultural embeddings. To validate our method, we built TED4C-L, a 106-hour multimodal dataset of 764 TED speakers from four cultural groups. Experiments show that SICAGE improves motion realism, diversity, beat synchronization, semantic relevance, and cultural consistency.

---


### 340. [GeoEdit: Geometry-Aware Object Editing via Dual-Branch Denoising](https://arxiv.org/abs/2606.30003)

**<font color=#1a73e8>作者：</font>** Yi He, Jiangming Wang, Xinyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precisely manipulating objects in a single photograph (translation, rotation, scaling) while obeying 3D physical constraints remains unsolved for diffusion-based editors. Current 2D methods lack spatial awareness and produce perspective violations. Forcing structural proxies into the latent space also disrupts variance homogeneity, and the resulting self-attention leakage leads to ghosting and background blur. The core difficulty is asymmetric: the relocated object must follow a rigid geometry, yet the uncovered background needs freedom to synthesize plausible content. We present GeoEdit, a training-free Lift-Manipulate-Render-Denoise pipeline that satisfies both constraints. We decouple scene and object in 3D, align them through point correspondence, and render a geometry-aligned proxy with a structural depth map. A Dual-Branch Denoising stage then refines this proxy: a video diffusion backbone preserves object identity, while 3D constraints are injected into the foreground within a narrow denoising window at matching noise variance (variance-homogeneous injection). The background denoises freely. Because the injected signal matches the native latent statistics, self-attention stays undisturbed. We also introduce GeoEditBench, a pose-aware benchmark covering object translation, object rotation, and camera movement with pose-aware evaluation metrics. Experiments confirm consistent gains in geometric accuracy, identity fidelity, and background quality. Our codes are available at this https URL.

---


### 341. [T3R: Deeper Test-Time Adaptation for Graph Neural Networks via Gradient Rotation](https://arxiv.org/abs/2606.30011)

**<font color=#1a73e8>作者：</font>** Huy Truong, Alexander Lazovik, Victoria Degeler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) deployed in real-world systems typically have fixed weights, often leading to degraded performance under distribution shifts. This issue can be mitigated by conventional fine-tuning, but in many real-world cases, collecting labeled data is expensive or infeasible. A potential approach is Test-Time Training (TTT), which adapts models' weights using unlabeled test data, yet it is typically limited to shallow updates that affect only a subset of model parameters. We propose T3R, leveraging multiple Rotograd matrices to improve task affinity between the target and auxiliary tasks, essential for effective test-time training. T3R further introduces a rotation technique that reorients self-supervised signals using these matrices to create surrogate gradients for the target task, allowing deeper adaptation across nearly the entire architecture. Empirically, T3R reduces MAE by 0.172 points over standard inference in regression datasets and achieves at least 9.37% relative improvement on cross-domain OGB classification benchmarks compared to models without adaptation. These results highlight the potential to develop an adaptation pipeline for graph-based systems, particularly in settings where conventional fine-tuning or retraining is infeasible.

---


### 342. [SkelEM: Training-Signal Decoupling of Skeleton and Diffusion for Self-supervised Axial Super-Resolution in Volume Microscopy](https://arxiv.org/abs/2606.30012)

**<font color=#1a73e8>作者：</font>** Bohao Chen, Yanchao Zhang, Yanan Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volume microscopy, including electron and light microscopy, suffers from severe anisotropic resolution due to physical axial sectioning. Existing self-supervised axial super-resolution (ASR) methods face a trilemma bounded by overly smoothed regression textures, structural hallucinations of pure diffusion models, and prohibitive inference latency. In this paper, we propose Skeleton-refinE Microscopy (SkelEM), a self-supervised framework that decouples ASR at the training-signal level: a frozen topological network and a diffusion refiner are optimized by disjoint objectives, separating low-frequency topology formulation from high-frequency detail enhancement. Building on this deterministic skeleton, we exploit a unified cycle-consistent mechanism on input sparse slices to simultaneously extract a real-domain residual prior and bidirectionally align the diffusion refiner, washing away cross-plane artifacts without synthetic bias. By truncating the reverse diffusion process with this physical prior, SkelEM achieves high-fidelity detail restoration in merely $\le 5$ steps. To rigorously assess cross-instrument generalization, we further introduce BRAVE-ASR, a new benchmark of co-aligned anisotropic and isotropic volumes acquired on a Plasma-FIB instrument. Across public benchmarks, SkelEM achieves the most favorable balance across the fidelity-perception trade-off among self-supervised methods, with state-of-the-art downstream membrane segmentation performance and robust zero-shot generalization across distinct modalities.

---


### 343. [Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction](https://arxiv.org/abs/2606.30014)

**<font color=#1a73e8>作者：</font>** Yuan Yang, Peijun Lu, Fangzhou Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-to-sim reconstruction for embodied AI requires geometry that is useful for collision reasoning, navigation, and agent-environment interaction, not only photorealistic novel-view synthesis. However, close-range urban facades are difficult for video-to-3D reconstruction: glass, reflections, repeated windows, and weak texture can produce visually plausible renderings with unstable surface geometry. We introduce shell-supervised Gaussian Splatting, a reconstruction-stage framework that uses an external facade structural shell as lightweight geometric supervision for video-driven Gaussian reconstruction. The method aligns an exterior shell to the video reconstruction frame, renders per-view depth, camera-space normal, and valid-mask maps, and applies these cues through mask-gated losses during Gaussian optimization. This design preserves RGB-driven appearance while regularizing only visible shell-supported facade regions. Experiments on anonymized close-range urban facade scenes show improved facade orientation and visible-surface point-cloud consistency over photo-only, monocular-cue, and surface-oriented Gaussian baselines, while maintaining comparable held-out rendering quality.

---


### 344. [Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017)

**<font color=#1a73e8>作者：</font>** Xiaobiao Du, YuAn Wang, Hao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting have demonstrated unprecedented success in novel view synthesis. However, the substantial inference and storage overhead driven by high-order Spherical Harmonics (SH) are primary bottlenecks for mobile platforms. In this paper, we present Flux-GS, a real-time Gaussian Splatting method designed to achieve high-fidelity rendering with significantly reduced overhead for resource-constrained mobile platforms. We first propose a Monte Carlo Specular Energy Aggregator, sampling third-order radiance residuals and aggregating specular energy into a compact latent space. In this way, our method effectively preserves visually salient lighting features in lower-order bands without expensive distillation or pre-training. To mitigate the high-frequency details lost during compression, we introduce an Attribute-Conditioned SH Enhancement module. This module predicts Gaussian-aware offsets based on intrinsic Gaussian attributes, which enhance the first-order SH representation prior to inference, without extra inference costs. Furthermore, the original single-view gradient-based densification is prone to producing excessive Gaussians and overfitting to a certain view. We address these limitations by proposing a Multi-view Alpha-based Densification and Pruning strategy. By leveraging multi-view guidance, we ensure multi-view structure consistency and the precise removal of redundant primitives. Extensive experiments demonstrate that Flux-GS achieves substantial parameter reduction while maintaining competitive visual quality, offering a robust and scalable solution for real-time mobile rendering. Code: \textcolor{magenta}{\href{this https URL}{this https URL}}.

---


### 345. [IBRSteG: Learning a Generalizable Steganography Framework for 3D Gaussian Splatting](https://arxiv.org/abs/2606.30024)

**<font color=#1a73e8>作者：</font>** Fanye Kong, Hongyu Xia, Yu Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep learning have notably improved steganographic message hiding. However, designing a generalizable steganographic approach for 3D Gaussian Splatting (3DGS) that can embed meaningful 3D scene content remains challenging. In this paper, we propose IBRSteG, a generalizable framework for 3DGS steganography that enables undetectable concealment of secret scenes within a steganographic scene. Unlike existing approaches whose parameter generation is rigidly coupled with the specific scene, we formulate 3D steganography as a feed-forward 3D Gaussian embedding process that generalizes across different 3DGS scenes. To realize this, we introduce GAS (Gaussian Attributes Steganographer), a network that learns a scene-independent embedding function by injecting the attributes of secret 3D Gaussian points into a cover scene, thereby directly reconstructing the steganographic scenes without per-scene finetuning or optimization. By transforming 3D Gaussian into these structured attributes, these attributes are compatible with 2D learning paradigms and benefit from their structured nature, thereby enhancing generalization to unseen 3DGS scenes. Extensive experiments on established datasets demonstrate that IBRSteG can effectively conceal different scenes with high visual quality, and achieves superior capacity and security. Code is available at this https URL.

---


### 346. [Cross-Modal Iteration Distillation for Robust IHD Screening: The IDNet Framework and A New Benchmark](https://arxiv.org/abs/2606.30027)

**<font color=#1a73e8>作者：</font>** Yongchang Gao, Junjie Pang, Shuaiyu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color Fundus Photography (CFP) offers a low-cost and non-invasive route for ischemic heart disease (IHD) screening, but current studies are limited by scarce public benchmarks and ineffective fusion of retinal images with sparse clinical variables. We propose IDNet, a multimodal framework with a Cross-Modal Distillation Aggregator (CDA) that uses learnable queries to sequentially integrate left-eye, right-eye, and clinical features, mitigating the imbalance between high-dimensional visual features and low-dimensional tabular inputs. We also construct a reproducible UK Biobank benchmark with open-source curation and quality-control pipelines, yielding 50,410 images from 25,205 subjects. On this benchmark, IDNet outperforms image-only, clinical-only, and several multimodal baselines, and CDA consistently improves multiple visual encoders as a plug-in fusion module.

---


### 347. [CogSENet: Blind Image Deblurring with Blur-Conditioned Semantic Routing and Explicit Frequency Fusion](https://arxiv.org/abs/2606.30030)

**<font color=#1a73e8>作者：</font>** Pan Wang, Yihao Hu, Xiujin Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image deblurring demands the recovery of high-fidelity details and coherent structures from complex, unknown degradations. Current blind image deblurring methods struggle with real-world, spatially varying degradations, and lack the semantic awareness necessary to reliably differentiate valid textures from artifacts. To bridge this gap, we propose CogSENet, a dynamic, semantic-aligned reconstruction framework inspired by the eagle's visual system. By mimicking the eagle's active saccadic scanning, we devise a Semantic-Driven State Space Module (SDSSM) with semantic-aware token regrouping via differentiable routing, enabling prompt-conditioned long-range dependency modeling. To ensure physically interpretable recovery of textures and structures, a BiFreqFusionBlock (BFFB) mirrors functional differentiation of the eagle's retina by decomposing features into high and low frequencies using wavelet transforms. Finally, we estimate a continuous Blur Field (CBF) from blur image and fuse it with CLIP semantic priors to modulate the deepest latent features, emulating focal adaptation and enabling adaptive restoration under spatially non-uniform blur. Extensive experiments demonstrate that CogSENetoutperforms state-of-the-art deblurring methods in both visual quality and structural fidelity with fewer parameters, while also performing favorably on dehazing, deraining, and denoising tasks.

---


### 348. [Consensus Clustering of Free-Viewing Gaze Data: New Insights into Human-Information Interaction](https://arxiv.org/abs/2606.30035)

**<font color=#1a73e8>作者：</font>** Beryl Gnanaraj, Jaya Sreevalsan-Nair, Saqib Alam Ansari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Free-viewing gaze data provides a rich, task-free window into human visual attention. Conventional exploratory data analysis of the data provides user attention patterns through fixations and areas of interest. However, despite the richness of this gaze data, its human-information interaction (HII) patterns are understudied. We address this gap using consensus clustering of gaze data with respect to users and stimulus characteristics. We present a novel end-to-end unsupervised ensemble learning system for consensus clustering of free-viewing gaze datasets, EnsembleGaze. With a goal of characterizing the user behavior and stimulus type, we propose a feature engineering step based on statistical descriptors of fixation-based distributions. EnsembleGaze involves consensus voting of selected clustering methods implemented on the feature vector to compute the co-association matrix. Using the separate consensus clustering of users and stimuli as a baseline, we further propose two high-dimensional clustering strategies for determining gaze clusters based on joint user and image characterization. They are consensus subspace clustering and spectral biclustering. Clustering performance is evaluated using selected standard metrics and is further interpreted through image-level properties. Our system provides a replicable method for the unsupervised analysis of fixation behavior in scene perception research. Our results show that image stimuli groupings are highly consistent across methods, reflecting a robust ambient-versus-focal viewing mode distinction, whereas user groupings are image-context-dependent, a structure that only biclustering and the two-step conditional approaches are architecturally capable of recovering. Testing on the publicly available datasets revealed dataset-specific patterns, with each offering complementary insights through distinct clustering strategies.

---


### 349. [Heads, Not Backbones: Output Heads Dominate Architectures on Fat-Tailed Returns](https://arxiv.org/abs/2606.30037)

**<font color=#1a73e8>作者：</font>** Sichao He, Yansong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a deep forecasting pipeline for fat-tailed financial returns at short horizons, which matters more - the backbone architecture or the output head? We compare four modern backbones (TimesNet, DLinear, N-BEATS, iTransformer) under three output heads: a point head, a single-Gaussian density head, and a Gaussian mixture density head with K=4 components. On S and P 500 monthly log-returns (1871-2023) under anchored walk-forward validation, the three heads form a strict gradient: switching from point to Gaussian improves CRPS by about 1.3 percent; switching from Gaussian to mixture adds a further about 2.4 percent. Switching between backbones, in contrast, changes CRPS by less than 1.5 percent on the point-head row and on the backbone-mean axis; density-head backbone spread is larger (up to 5.1 percent on the h=1 Gaussian row, driven by N-BEATS) but the head gradient (3.7 percentage points) still dominates. The Model Confidence Set on squared errors does not exclude any of the 12 variants at the 5 percent level: the head separates them only on distributional metrics (CRPS, pinball, coverage), not on squared error. The mixture head incremental value over a single Gaussian is largest in the highest-volatility regimes (13.9 percent in 1970s stagflation at h=12), confirming the mixture captures tail risk beyond what a unimodal Gaussian can express. The picture is horizon-dependent: the head dominates at short horizons, but at long horizons (h >= 6) the backbone re-takes the lead - an h-split we document against classical baselines (section 5.1). We conclude that on fat-tailed returns at short horizons, the head dominates the backbone, and the mixture distribution adds genuine value over a single Gaussian during crisis periods when risk-management decisions actually matter.

---


### 350. [Walking in the Implicit: Interactive World Exploration via Neural Scene Representation](https://arxiv.org/abs/2606.30045)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Chengrui Dong, Zhenhua Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video generation systems for camera-controlled world exploration roll out growing sequences of latent video frames, entangling state transition with high-frequency observation synthesis. We propose Walking in the Implicit, a scene-centric paradigm that changes the rollout variable from frame latents to a fixed-length, renderable implicit state, termed Neural Implicit Scene (NIS). This factorizes interactive generation into stochastic transition of a compact scene state and deterministic pose-conditioned rendering given the sampled state. We instantiate this paradigm as NeuWorld: a transformer VAE learns locally anchored NIS from sparse posed frames, and a diffusion transformer evolves NIS conditioned on future camera trajectories and geometry-aware retrieved history. By reusing the VAE encoder as a unified conditioner, NeuWorld maps camera, reference-image, and history cues into the same NIS modality, avoiding external heterogeneous encoders. Trained from scratch on public posed-view data without pretrained video backbones or auxiliary 3D reconstructors, NeuWorld achieves strong long-horizon consistency with favorable inference efficiency.

---


> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
