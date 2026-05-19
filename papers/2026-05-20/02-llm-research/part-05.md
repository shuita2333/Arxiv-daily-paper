# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-346](./part-07.md)

---

### 201. [EGI: A Multimodal Emotional AI Framework for Enhancing Scrum Master Real-time Self-Awareness](https://arxiv.org/abs/2605.17684)

**<font color=#1a73e8>作者：</font>** Jingni Huang, Peter Bloodsworth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While increasing research focuses on the emotional well-being of agile team members, a significant gap remains in emotion monitoring studies for Scrum Masters and meeting organizers, whose impact on team dynamics is crucial. This paper proposes a novel application integrating four carefully selected and recommended AI models to monitor the unconsciously expressed emotions of these key roles. This is achieved through: real- time transcription using a speech-to-text model; thresholding for intonation analysis to detect emotional cues in prosody; applying emotion-based vocabulary matching to identify sentiment in spoken content; and providing context-aware suggestions containing emotion keywords using an open-source, multi-module AI API. The system achieved an ASR word error rate WER of 10% in simulated meeting environments. Our evaluation shows that real- time feedback significantly improves emotion awareness during simulated agile meetings, providing Scrum Masters and meeting organizers with real-time and practical suggestions to help them quickly identify and minimize the expression of negative emotions, fostering more positive and effective team interactions.

---


### 202. [Validate Your Authority: Benchmarking LLMs on Multi-Label Precedent Treatment Classification](https://arxiv.org/abs/2605.17691)

**<font color=#1a73e8>作者：</font>** M. Mikail Demir, M. Abdullah Canbaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automating the classification of negative treatment in legal precedent is a critical yet nuanced NLP task where misclassification carries significant risk. To address the shortcomings of standard accuracy, this paper introduces a more robust evaluation framework. We benchmark modern Large Language Models on a new, expert-annotated dataset of 239 real-world legal citations and propose a novel Average Severity Error metric to better measure the practical impact of classification errors. Our experiments reveal a performance split. Google's Gemini 2.5 Flash achieved the highest accuracy on a high-level classification task (79.1%), while OpenAI's GPT-5-mini was the top performer on the more complex fine-grained schema (67.7%). This work establishes a crucial baseline, provides a new context-rich dataset, and introduces an evaluation metric tailored to the demands of this complex legal reasoning task.

---


### 203. [Fine-tuning Pocket-Aware Diffusion Models via Denoising Policy Optimization](https://arxiv.org/abs/2605.17693)

**<font color=#1a73e8>作者：</font>** Yuan Xue, Daniel Kudenko, Megha Khosla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structure-based drug design has been accelerated by pocket-aware 3D generative models, yet most methods primarily fit the training distribution and may fall short of satisfying multiple properties required in real-world therapeutic drug discovery. Recently, increasing attention has focused on structure-based molecule optimization (SBMO), which targets fine-grained control over multiple specified molecular properties. In this paper, we present DEPPA, a novel SBMO approach building upon Denoising Diffusion Policy Optimization for fine-tuning a pre-trained pocket-aware diffusion model via reinforcement learning. DEPPA enables optimization over multiple properties, including binding affinity, drug-likeness, synthesizability and diversity. We formulate the reverse denoising process of the pretrained pocket-aware diffusion model as a multi-step Markov Decision Process, where the desired properties that serve as reward signals are evaluated on the final generated ligand molecules. DEPPA incorporates a coarse denoising scheduler during the RL fine-tuning to achieve efficient and effective molecule optimization. Experimental results on the CrossDocked2020 benchmark demonstrate that DEPPA outperforms baselines in binding affinity (Vina Score -8.5 kcal/mol), drug-likeness and diversity while exhibiting competitive performance in synthesizability. The source code is available at this https URL .

---


### 204. [Do LLM Agents Mirror Socio-Cognitive Effects in Power-Asymmetric Conversations?](https://arxiv.org/abs/2605.17694)

**<font color=#1a73e8>作者：</font>** Anvesh Rao Vijjini, Sagar Manjunath, Snigdha Chaturvedi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Power differences shape human communication through well documented socio cognitive effects, including language coordination, pronoun usage, authority bias, and harmful compliance. We examine whether large language models (LLMs) exhibit similar behaviors when assigned high or low status personas. Using personas from diverse professions, we simulate multi turn, power asymmetric dialogues (e.g., principal teacher, justice lawyer) and measure (i) linguistic coordination, (ii) pronoun usage, (iii) persuasion success, and (iv) compliance with unsafe requests. Our results show that LLMs show key socio cognitive effects of power, albeit with nuances and variability, linking simulated interactions to both desirable and unsafe behaviors.

---


### 205. [Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces](https://arxiv.org/abs/2605.17698)

**<font color=#1a73e8>作者：</font>** Seth Karten, Cameron Crow, Chi Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of Large Language Models (LLMs) as autonomous economic agents introduces systemic risks that extend beyond individual capability failures. As agents transition to directly interacting with marketplaces, their collective behavior can amplify volatility and mask deception at scale. We introduce the Agent Bazaar, a multi-agent simulation framework for evaluating Economic Alignment, the capacity of agentic systems to preserve market stability and integrity. We identify two failure modes: (1) Algorithmic Instability in a B2C market ("The Crash"), where firms amplify price volatility until the market collapses, and (2) Sybil Deception in a C2C market ("The Lemon Market"), where a single deceptive agent controlling multiple coordinated seller identities floods the market with fraudulent listings, eroding trust and consumer welfare. We evaluate frontier and open-weight models across both scenarios and find that models largely fail to self-regulate, with failure severity varying by model rather than by size. We propose economically aligned harnesses, Stabilizing Firms and Skeptical Guardians, that improve outcomes but remain fragile under harder market conditions. To close this gap, we train agents with REINFORCE++ using an adaptive curriculum, producing a 9B model that outperforms all evaluated frontier and open-weight models. We propose the Economic Alignment Score (EAS), a 4-component scalar metric aggregating stability, integrity, welfare, and profitability, enabling direct cross-model comparison. Our results show that economic alignment is orthogonal to general capability and can be directly trained with targeted RL.

---


### 206. [Patch-MoE Mamba: A Patch-Ordered Mixture-of-Experts State Space Architecture for Medical Image Segmentation](https://arxiv.org/abs/2605.17719)

**<font color=#1a73e8>作者：</font>** Diego Adame, Fabian Vazquez, Jose A. Nunez 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CNN- and Transformer-based architectures have achieved strong performance in medical image segmentation, but CNNs are limited in modeling long-range dependencies, while Transformers often suffer from quadratic computational and memory complexity. State space models, especially Mamba-based networks, offer an efficient alternative with linear sequence complexity. However, existing Mamba segmentation models still face two limitations: pixel-wise directional scanning can disrupt local 2D spatial structure, and simple summation-based fusion of scan directions cannot adapt well to diverse object sizes, shapes, and boundaries. To address these issues, we propose \textit{Patch-MoE Mamba}, a patch-ordered mixture-of-experts state space architecture for medical image segmentation. It introduces a hierarchical patch-ordered scanning mechanism that preserves local spatial neighborhoods while capturing multi-scale context, and an MoE-based directional fusion module that adaptively combines multiple Mamba scanner outputs using four directional experts, a learnable concatenation expert, and residual directional aggregation. Experiments on five public polyp segmentation benchmarks and the ISIC 2017/2018 skin lesion segmentation datasets demonstrate the effectiveness and generality of Patch-MoE Mamba.

---


### 207. [EXG: Self-Evolving Agents with Experience Graphs](https://arxiv.org/abs/2605.17721)

**<font color=#1a73e8>作者：</font>** Yuxin Jin, Siyuan Zhang, Hanchen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents have demonstrated strong capabilities in complex reasoning and problem solving through multi-step interactions, yet most deployed agents remain behaviorally static, with knowledge acquired during execution rarely translating into systematic improvement over time. In response, a growing line of work on self-evolving agents explores how agents can improve through experience during deployment, but most existing approaches either rely on ad hoc reflection limited to single-task correction or adopt unstructured memory that accumulates fragmented experience with delayed usability. To address this limitation, we introduce EXG, an experience graph framework for self-evolving agents that explicitly organizes accumulated successes and failures into a structured, relational representation. EXG is the first experience graph designed for self-evolving agents, supporting both online, real-time graph growth during execution for immediate cross-task experience reuse, and offline reuse of a consolidated experience graph as an external memory module. This design also enables EXG to serve as a plug-and-play component for existing self-evolving agents, organizing prior experience into a unified experience graph and improving both solution quality and resource efficiency as deployment progresses. Extensive experiments across code generation and reasoning benchmarks show that EXG attains more favorable performance-efficiency trade-offs than reflection- and memory-based baselines in both online and offline evaluations. Our results suggest that structuring experience as a graph provides a principled foundation for scalable and transferable self-evolving agent behavior.

---


### 208. [Harnessing LLM Agents with Skill Programs](https://arxiv.org/abs/2605.17734)

**<font color=#1a73e8>作者：</font>** Hongjun Liu, Yifei Ming, Shafiq Joty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equipping LLM agents with reusable skills derived from past experience has become a popular and successful approach for tackling complex and long-horizon tasks. However, such lessons are often encoded as textual guidance that remains largely advisory, lacking explicit mechanisms for when and how to intervene in the agent loop. To bridge the gap, we introduce HASP(Harnessing LLM Agents with Skill Programs), a new framework that upgrades skills into executable Program Functions (PFs). Rather than offering passive advice, PFs act as executable guardrails that activate on failure-prone states and modify the next action or inject corrective context. HASP is highly modular: it can be applied at inference time for direct agent-loop intervention, during post-training to provide structured supervision, or for self-improvement by evolving validated, teacher-reviewed PFs. Empirically, HASP drives substantial gains compared to both training-free and training-based methods on web-search, math reasoning, and coding tasks. For example, on web-search reasoning, inference-time PFs alone improve the average performance by 25% compared to (multi-loop) ReAct Agent, while post-training and controlled evolution achieve a 30.4% gain over Search-R1. To provide deeper insights into HASP, our mechanism analysis reveals how PFs trigger and intervene, how skills are internalized, and the requirement for stable skill library evolution.

---


### 209. [AURORA: Contextual Orthogonalization for Geometric Representation Learning in Healthcare Foundation Models](https://arxiv.org/abs/2605.17765)

**<font color=#1a73e8>作者：</font>** Yuanyun Zhang, Shi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent healthcare foundation models have achieved strong predictive performance through large scale self supervised learning, yet their latent representations frequently entangle physiologic severity, intervention intensity, observational structure, and institutional workflow into shared embedding directions. While effective for downstream prediction, such representations remain semantically opaque and unstable under contextual shift. We introduce AURORA, Adaptive Uncertainty aware Representations through Orthogonalized Relational Alignment, a new framework for healthcare representation learning based on contextual latent geometry. Rather than optimizing a single unified embedding manifold, AURORA decomposes representations into orthogonal semantic subspaces corresponding to distinct contextual factors and learns relational consistency objectives within each subspace. This induces latent spaces that are both semantically disentangled and geometrically interpretable. Across multiple clinical prediction and retrieval tasks, AURORA consistently outperforms reconstruction, contrastive, and self distillation baselines while substantially improving contextual disentanglement, neighborhood purity, and robustness under institutional distribution shift. Our results suggest that latent geometry itself constitutes an important axis of healthcare foundation model design and that explicitly structuring representation space according to contextual semantics provides a complementary direction beyond conventional predictive compression objectives.

---


### 210. [LatentUMM: Dual Latent Alignment for Unified Multimodal Models](https://arxiv.org/abs/2605.17766)

**<font color=#1a73e8>作者：</font>** Yinyi Luo, Wenwen Wang, Hayes Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) achieve strong performance in both understanding and generation by learning a shared latent space, yet they often exhibit functional inconsistency between these two capabilities. We observe that this issue does not stem from a lack of shared representations, but from the absence of explicit alignment between the transformations that map into and out of the latent space. As a result, generation and re-encoding can follow inconsistent trajectories, leading to semantic drift under modality transitions. In this work, we propose LatentUMM, a framework that constructs an enhanced shared latent space to explicitly align these transformations and improve cross-modal consistency. LatentUMM consists of two stages. First, dual latent alignment enforces consistency at both the modality and capacity levels: cross-modal alignment uses a stronger embedding model to impose structured cross-modal semantics, while dual capacity alignment enforces bidirectional consistency under generation and re-encoding. Second, latent dynamics stabilization improves robustness via stochastic latent rollouts and preference optimization, favoring trajectories that better preserve semantic consistency. Experiments show that LatentUMM consistently improves multimodal consistency across diverse architectures. Code is available at: this https URL.

---


### 211. [Entropy-Gradient Inversion: Moving Toward Internal Mechanism of Large Reasoning Models](https://arxiv.org/abs/2605.17770)

**<font color=#1a73e8>作者：</font>** Junyao Yang, Chen Qian, Kun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The advancement of Large Reasoning Models (LRMs) has catalyzed a paradigm shift from reactive ``fast thinking'' text generation to systematic, step-by-step ``slow thinking'' reasoning, unlocking state-of-the-art performance in complex mathematical and logical tasks. However, the field faces \textit{the fundamental gap between token-level behavioral analysis and internal reasoning mechanisms, and the instability of reinforcement learning (RL) for reasoning optimization relying on costly external verifiers}. We identify and formally define \textbf{Entropy-Gradient Inversion}, a robust negative correlation between token entropy and logit gradients that acts as a definitive geometric fingerprint for LRM reasoning capability. Building on this, we propose \textbf{Correlation-Regularized Group Policy Optimization (CorR-PO)}, which embeds this inversion signature into RL reward regularization. Extensive experiments on various reasoning benchmarks across multiple model scales show CorR-PO consistently outperforms state-of-the-art baselines, confirming that stronger inversion directly correlates with superior reasoning performance.

---


### 212. [Internalizing Tool Knowledge in Small Language Models via QLoRA Fine-Tuning](https://arxiv.org/abs/2605.17774)

**<font color=#1a73e8>作者：</font>** Yuval Shemla, Ayal Yakobe, Tanmay Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as planning components in agentic systems, but current tool-use pipelines often require full tool schemas to be included in every prompt, creating substantial token overhead and limiting the practicality of smaller models. This paper investigates whether tool-use knowledge can be internalized into small language models through parameter-efficient fine-tuning, enabling structured planning without explicit tool descriptions at inference time. Using AssetOpsBench as the primary benchmark, we fine-tune Gemma 4 E4B and Qwen3-4B with 8-bit QLoRA on approximately 1,700 tool-use examples spanning tool knowledge, question-to-plan mappings, and execution-style traces. We evaluate the resulting models under description-free inference, where the prompt omits the tool catalog entirely. The fine-tuned models outperform an informed unfine-tuned baseline that receives full tool descriptions, reducing input length by 82.6\% while improving structural and LLM-judge planning scores. In the best Gemma run, the model achieves an AT-F1 of 0.65 and an overall judge score of 3.88, compared with 0.47 and 2.88 for the informed baseline. Qwen3-4B achieves a strong overall judge score of 3.78 while using 62\% less memory and running 2.5$\times$ faster than Gemma, though it also exhibits greater catastrophic forgetting on general multiple-choice benchmarks. Additional ablations show that LoRA rank controls a quality--retention trade-off, with $r=32$ maximizing planning quality and smaller ranks preserving more general knowledge. These results suggest that, for fixed tool catalogs, QLoRA fine-tuning can shift tool knowledge from prompt context into model weights, substantially reducing inference overhead while maintaining or improving tool-planning quality.

---


### 213. [Systematic Evaluation of the Quality of Synthetic Clinical Notes Rephrased by LLMs at Million-Note Scale](https://arxiv.org/abs/2605.17775)

**<font color=#1a73e8>作者：</font>** Jinghui Liu, Sarvesh Soni, Anthony Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate or synthesize clinical text for a wide range of applications, from improving clinical documentation to augmenting clinical text analytics. Yet evaluations typically focus on a narrow aspect -- such as similarity or utility comparisons -- even though these aspects are complementary and best viewed in parallel. In this study, we aim to conduct a systematic evaluation of LLM-generated clinical text, which includes intrinsic, extrinsic, and factuality evaluations of synthetic clinical notes rephrased from MIMIC databases at million-note scale. Our analysis demonstrates that synthetic notes preserve core clinical information and predictive utility for coarse-grained tasks despite substantial linguistic changes, but lose fine-grained details for task like ICD coding. We show this loss of detail can be substantially mitigated by rephrasing notes by chunks rather than by the whole note, but at the cost of reduced factual precision under incomplete context. Through fact-checking and error analysis, we further find that synthesis errors are dominated by misinterpretation of clinical context, alongside temporal confusion, measurement errors, and fabricated claims. Finally, we show that the synthetic notes -- despite their task-agnostic nature -- can effectively augment task-specific training for rare ICD codes.

---


### 214. [Revisiting the Adam-SGD Gap in LLM Pre-Training: The Role of Large Effective Learning Rates](https://arxiv.org/abs/2605.17787)

**<font color=#1a73e8>作者：</font>** Athanasios Glentis, Dawei Li, Chung-Yiu Yau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is widely believed that stochastic gradient descent (SGD) performs significantly worse than adaptive optimizers such as Adam in pre-training Large Language Models (LLMs). Yet the underlying reason for this gap remains unclear. In this work, we attribute a large part of the discrepancy to SGD's inability to sustain learning rates comparable to Adam's much larger effective learning rates. Through empirical and theoretical analysis of LLM pre-training dynamics, we identify that training is characterized by small gradient norms and large weight-to-gradient ratios, an effect that becomes more pronounced with larger batch sizes typical in pre-training, necessitating such large effective learning rates. However, we find that output-layer gradient magnitudes become highly uneven across token classes, and that large gradient spikes frequently occur during training. Together, these effects severely restrict the admissible learning rate of SGD. Guided by this understanding, we show that simple clipping mechanisms that stabilize SGD at large learning rates enable it to recover most of Adam's performance. In our large-scale experiments, the validation loss gap between large-learning-rate SGD and Adam shrinks from more than 50% to only about 3.5% when pre-training a 1B-parameter LLaMA model with a 1M-token batch size.

---


### 215. [HydroAgent: Closing the Gap Between Frontier LLMs and Human Experts in Hydrologic Model Calibration via Simulator-Grounded RL](https://arxiv.org/abs/2605.17792)

**<font color=#1a73e8>作者：</font>** Zhi Li, Songkun Yan, Jie Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibrating distributed hydrologic models is a critical bottleneck across operational water resources management - streamflow prediction, reservoir operation, drought monitoring, infrastructure design, and flood forecasting all depend on it. Each basin demands an expert to translate hydrograph signatures into adjustments of a high-dimensional parameter vector, and the resulting workflow does not transfer between watersheds. We ask: can frontier large language model (LLM) agents replace the human hydrologic modeler, and if not, what would it take? We benchmark nine frontier LLM agents - Claude Opus 4.6/4.7, Sonnet 4.6, GPT-5/5.4/5.4-pro, and Gemini 2.5-pro/3.1-pro/3-flash - on the operational CREST distributed hydrologic model used by the U.S. National Weather Service for flash-flood forecasting. Best-of-twenty-rounds Nash-Sutcliffe Efficiency (NSE) across four held-out gauges spanning 329-40,792 km2 ranges from -0.16 (GPT-5.4) to 0.75 (Sonnet 4.6); the ceiling reproduces across all three vendors and capability tiers, with the strongest models concentrating in the 0.65-0.75 band, and no model reaches the human-expert reference except Opus-4.7 on one gauge. We argue this gap is not a parameter-count problem but a domain-grounding problem. We then propose HYDROAGENT, fine-tuning open-weight Qwen3-4B with supervised fine-tuning on 2,576 expert calibration trajectories and Group-Relative Policy Optimization using NSE as a verifiable reward from online CREST simulations - reinforcement learning with simulation feedback (RLSF). For Earth system science, a small domain-tuned policy with simulator-in-the-loop RL is a more compute-efficient and physically faithful path than scaling generic frontier models, and the multi-modal richness of Earth data - remote sensing, in-situ time series, and forecaster narrative - makes domain agents a leveraged direction for AI in physical science.

---


### 216. [AMO: Adaptive Muon Orthogonalization](https://arxiv.org/abs/2605.17806)

**<font color=#1a73e8>作者：</font>** Xinlin Zhuang, Panyi Ouyang, Yichen Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as a competitive alternative to AdamW for large-scale pre-training, with orthogonalization via Newton-Schulz (NS) iterations as its core operation. Existing Muon variants apply a uniform NS schedule to all parameter matrices, overlooking possible differences in orthogonalization difficulty and its impact on performance. Through a systematic empirical study, we show that this per-matrix heterogeneity is pervasive and largely determined by matrix geometry, which evolves dynamically across operator types, training stages, and network depths. As a result, uniform NS schedules can lead to uneven orthogonalization quality across the model. Motivated by these findings, we propose Adaptive Muon Orthogonalization (AMO), an observe-then-commit method that measures weight geometry by operator type early in training and then uses these signals to allocate the NS budget for the remainder of training. AMO delivers consistent improvements over uniform-schedule Muon across standard, prolonged, and continual pre-training, surpassing the strongest baseline by +0.76 on Llama3.1-1.4B and +0.51 on Qwen3-1.7B in average downstream performance of 12 evaluation tasks.

---


### 217. [Accelerating AI-Powered Research: The PuppyChatter Framework for Usable and Flexible Tooling](https://arxiv.org/abs/2605.17809)

**<font color=#1a73e8>作者：</font>** Chun-Hsiung Tseng, Hao-Chiang Koong Lin, Andrew Chih-Wei Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This research addresses the challenges inherent in developing Artificial Intelligence (AI) applications, particularly those leveraging Large Language Models (LLMs). While AI vendors provide Application Programming Interfaces (APIs) and Software Development Kits (SDKs) to facilitate developer interaction, the former often requires intricate manual request construction, and the latter can lead to significant vendor lock-in. Furthermore, existing model abstraction frameworks, though mitigating vendor dependency, introduce an additional layer of complexity and potential security concerns. To reconcile these conflicting factors, the study introduces PuppyChatter, a novel software framework designed to preserve the intuitive simplicity of vendor-specific SDKs while simultaneously adhering to the vendor-neutrality principles characteristic of model abstraction, thereby offering a more streamlined and flexible development paradigm.

---


### 218. [Why We Look Where We Look: Emergent Human-like Fixations of a Foveated Visual Language Model Maximizing Scene Understanding](https://arxiv.org/abs/2605.17823)

**<font color=#1a73e8>作者：</font>** Shravan Murlidaran, Ziqi Wen, Sana Shehabi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When humans view scenes without a specific task (free-viewing), they initially direct their eye movements toward the scene center and then fixate on people, text, objects being gazed at or grasped, and semantically meaningful regions. What these signature fixation patterns reflect and whether they optimize an underlying perceptual task remain unknown. We show that a computational agent with simulated foveation, trained to optimize scene comprehension, exhibits emergent human fixation signature patterns. In contrast, versions of the agent trained to search or classify scenes, or equipped with peripheral vision that was better or worse than human vision, predicted human fixation patterns less accurately. Thus, human free-viewing fixation patterns may emerge as a functional byproduct of optimizing scene comprehension under the biological constraints of foveated vision.

---


### 219. [CounterCount: A Diagnostic Framework for Counting Bias in Vision Language Models](https://arxiv.org/abs/2605.17826)

**<font color=#1a73e8>作者：</font>** Reem Alzahrani, Hassan Alshanqiti, Bushra Bin Hemid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at multimodal reasoning, yet it remains unclear whether their answers are grounded in visual evidence or driven by learned language and world priors. Counting provides a precise testbed: when visual evidence conflicts with canonical object knowledge, a model must rely on the image rather than a prototypical count. We introduce CounterCount, a diagnostic framework for counterfactual counting in VLMs, consisting of paired factual and counterfactual images with edited count-relevant attributes, verified answers, and localized evidence annotations. Evaluating recent VLMs, we find strong performance on factual images but consistent degradation under counterfactual attribute changes, indicating reliance on object-level priors even when contradictory visual evidence is present. Using localized annotations, we show that these failures are not solely due to missing or ambiguous visual evidence, but to models underweighting attention to count-relevant visual tokens. We introduce a unified inference-time attention modulation strategy that reweights selected visual tokens, improving counterfactual counting accuracy by up to 8% across multiple VLMs. Overall, CounterCount exposes prior-driven counting failures and provides diagnostic insights for designing future VLMs.

---


### 220. [Interactive Evaluation Requires a Design Science](https://arxiv.org/abs/2605.17829)

**<font color=#1a73e8>作者：</font>** Keyang Xuan, Peiyang Song, Pan Lu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI evaluation is undergoing a structural change. Large language models (LLMs) are increasingly deployed as systems that act over time through tools, environments, users, and other agents, while many evaluation practices still inherit assumptions from response-centered benchmarks (e.g., fixed inputs, isolated outputs, and outcome judgments that can be made from a single response). The field has begun to build interactive benchmarks, but the resulting landscape is fragmented: benchmarks differ in what interaction artifacts they admit, how trajectories are scored, and what claims their results support. This position paper argues that interactive evaluation should be treated as a principled evaluation paradigm, not merely a new family of agent benchmarks. Simply adopting previous evaluation paradigms does not suffice. We define evaluation as an autonomous mapping from evidence to judgments, and show that interactive evaluation changes both sides of this mapping: the evidence becomes interaction-generated trajectories, while the evaluation procedure must assess process, recoverability, coordination, robustness, and system-level performance. Building on this definition, we propose a two-axis taxonomy, derive design principles and reporting standards, examine representative scenarios, and analyze how longstanding evaluation challenges reappear at the trajectory level.

---


### 221. [Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents](https://arxiv.org/abs/2605.17830)

**<font color=#1a73e8>作者：</font>** Ahmad Al-Tawaha, Shangding Gu, Peizhi Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety evaluations of memory-equipped LLM agents typically measure within-task safety: whether an agent completes a single scenario safely, often under adversarial conditions such as prompt injection or memory poisoning. In deployment, however, a single agent serves many independent tasks over a long horizon, and memory accumulated during earlier tasks can affect behavior on later, unrelated ones. Studying this regime requires evaluation along the temporal dimension across tasks: not whether an agent is safe at any single memory state, but how its safety profile changes as memory accumulates across many independent interactions. We call this failure mode temporal memory contamination. To isolate memory exposure from stream non-stationarity, we introduce a trigger-probe protocol that evaluates a fixed probe set against read-only memory snapshots at varying prefix lengths, together with a NullMemory counterfactual baseline for identifying memory-induced violations. We apply this protocol across three deployment scenarios spanning records, memos, forms, and email correspondence and eight memory architectures, and additionally on Claw-like AI agents, such as OpenClaw, using the platform's native memory mechanism. Memory-enabled agents consistently exceed the NullMemory baseline, and memory-induced violation rates show a robust upward trend with exposure length on both agent classes. Order-randomization experiments indicate that the effect is driven primarily by accumulated content rather than encounter order. Finally, a structural consequence of the event decomposition is that memory-induced risk is detectable from retrieval state before generation, which we confirm with a high-recall diagnostic monitor. Our results argue for treating memory safety as a longitudinal property that requires temporal evaluation, not a single-state property that can be captured by a snapshot.

---


### 222. [Agentic Cost-Aware Query Planning with Knowledge Distillation for Big Data Analytics](https://arxiv.org/abs/2605.17831)

**<font color=#1a73e8>作者：</font>** Mahdi Naser-Moghadasi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Query optimization in big data analytics remains computationally expensive, particularly for resource-constrained environments where traditional optimizers fail to satisfy memory and latency constraints. We present an agentic query planning system that combines a rule-based teacher planner, UCB1 bandit exploration, cost-aware prediction, and knowledge distillation to a lightweight student planner. Our teacher planner generates SQL plans using six key optimization strategies, while UCB1 bandit search efficiently explores the plan space under explicit resource constraints. A Random Forest cost model predicts query latency from plan features, enabling cost-aware decisions. A distilled student planner (Logistic Regression or Gradient Boosting) learns to mimic teacher-bandit decisions for fast inference. Evaluation on NYC Taxi and IMDB datasets demonstrates 23% latency reduction compared to default planners while maintaining 94% constraint satisfaction. The student planner achieves 89% accuracy in replicating optimal plans with 15x faster inference time. Our single-file implementation enables reproducible big-data analytics on resource-limited machines and is publicly available at this https URL.

---


### 223. [KISS - Knowledge Infrastructure for Scientific Simulation: A Scaffolding for Agentic Earth Science](https://arxiv.org/abs/2605.17856)

**<font color=#1a73e8>作者：</font>** Ziwei Li, Liujun Zhu, Yuchen Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process-based simulation models encode decades of scientific understanding across the Earth sciences, yet the communities most exposed to climate risk and resource scarcity are the least able to use them. Here, we introduce knowledge infrastructure (KI), an agent-actionable scaffold that externalizes expertise into validated modelling operators, staged domain protocols, and diagnostic recovery mechanisms. Across a 3,000-trial coupled-hydrology benchmark, agents equipped with KI produced physically plausible, verifiable end-to-end simulations in up to 84% of trials, while agents without KI plateaued below 40%. KI generalizes across disciplines. We packaged its construction into a Knowledge Dissection Toolkit (KDT) that autonomously produced KI enabling end-to-end agent execution of 117 additional process-based models across 14 Earth-science domains. Across all 119 KIs, modelling decisions and failure remedies converged despite different underlying physics, showing that operational expertise is structured and extractable rather than ad hoc. Demonstrations show KI-equipped agents lowering both the access barrier between non-specialist users and process-based simulation, and the integration barrier between modelling communities. Through this scaffold, process-based science can then evolve as a living scientific commons, answerable to whoever needs to know and extendable by whoever can contribute.

---


### 224. [$\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control](https://arxiv.org/abs/2605.17862)

**<font color=#1a73e8>作者：</font>** Xianwei Chen, Shimin Zhang, Jibin Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling on-policy distillation (OPD) for large language models (LLMs) confronts a fundamental tension: asynchronous execution is necessary for system efficiency, but structurally deviates from the ideal on-policy objective. To address this challenge, we theoretically decompose the objective discrepancy into rollout drift and supervision drift, capturing staleness in student rollout and teacher context, respectively. Building on this, we introduce a sample-level freshness score that quantifies the reliability of a buffered sample with respect to the on-policy objective. Guided by this signal, we further propose f-OPD, a novel framework that adaptively regulates stale-sample influence and constrains policy drift accumulated under asynchronous training. Across reasoning, tool-use, and coding-agent tasks of increasing interaction horizon, f-OPD consistently achieves task performance comparable to synchronous optimization while largely retaining the throughput advantages of asynchronous execution. Our results establish the first recipe for achieving a performance-efficiency trade-off in OPD, paving the way for long-horizon agentic post-training at scale.

---


### 225. [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](https://arxiv.org/abs/2605.17889)

**<font color=#1a73e8>作者：</font>** Mu-Young Son, Yi Chen, Seungjae Yoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Mixture-of-Experts (MoE) architecture improves computational efficiency via sparse expert activation, but throughput-oriented inference faces substantial GPU memory pressure due to a significant parameter size and intermediate data. Prior works attempt to mitigate this using expert offloading with micro-batching or by offloading computation to the CPU. However, the fragmented workload resulting from micro-batching degrades operational intensity, causing expert execution to become memory-bound. Meanwhile, CPU offloading is constrained by slow PCIe transfers and its limited applicability to attention computation in the decode stage. Consequently, these inefficiencies prevent effective system utilization, severely restricting the end-to-end throughput of MoE inference.
To address these challenges, this paper proposes CoX-MoE, an Advanced Matrix Extensions (AMX)-enabled CPU-GPU collaborative system that comprehensively optimizes MoE inference by combining coalesced expert execution with strategic workload orchestration for higher throughput. CoX-MoE introduces (i) a coalescing-aware orchestration policy to jointly optimize resource allocation by adopting ordinary batch, instead of micro-batch, for expert computation and selective attention offloading, and (ii) a static expert-aware stratification scheme that pre-assigns frequently activated experts to the GPU, mitigating PCIe transfer overhead and balancing workload for the CPU and GPU during inference. Compared to state-of-the-art frameworks, CoX-MoE delivers significant gains, achieving up to 7.1x and 2.4x higher throughput than FlexGen and MoE-Lightning, respectively.

---


### 226. [Evaluating Cognitive Age Alignment in Interactive AI Agents](https://arxiv.org/abs/2605.17894)

**<font color=#1a73e8>作者：</font>** Yifan Shen, Jiawen Zhang, Jian Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While agentic AI and its core multimodal large language models (MLLMs) have demonstrated remarkable promise in language and visual reasoning across domains ranging from daily life to advanced scientific research, a profound gap remains between artificial and human intelligence. Despite the integration of powerful tools and advanced MLLMs, state-of-the-art AI agents frequently fail at foundational, seemingly simple tasks that a child can resolve with ease. Inspired by the Wechsler Intelligence Scale for Children (WISC), we introduce ChildAgentEval, the first psychometrically grounded interactive benchmark for evaluating cognitive age alignment in MLLM-based agents. ChildAgentEval systematically compares the reasoning performance of various MLLM-based interactive agents against age-specific human developmental stages, exposing where current agentic AI systems can and cannot simulate age-specific cognitive behavior.

---


### 227. [DuIVRS-2: An LLM-based Interactive Voice Response System for Large-scale POI Attribute Acquisition](https://arxiv.org/abs/2605.17900)

**<font color=#1a73e8>作者：</font>** Le Zhang, Shengming Zhang, Rui Zha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate Point of Interest (POI) attribute acquisition is essential for location-based services, yet traditional modular Interactive Voice Response (IVR) systems suffer from error accumulation and high maintenance overhead. We present DuIVRS-2, a large language model (LLM)-based end-to-end framework designed for large-scale POI attribute acquisition at Baidu Maps. To address the long-tail distribution of real-world interactions, our methodology first employs a finite state machine (FSM)-guided data augmentation strategy to synthesize a balanced and diverse training dataset. We then streamline dialogue management via a selective generation scheme combined with a Chain-of-Thought (CoT) mechanism, which ensures output stability and effectively eliminates hallucinations in industrial settings. To facilitate continuous policy refinement with minimal manual effort, we design a cooperative iterative learning framework that leverages a dual-evaluator voting system. Deployed in production for two months, DuIVRS-2 processed 0.4 million calls daily and achieved a 83.9\% Task Success Rate (TSR), outperforming its predecessor by 4 percentage points while maintaining a low reaction time of 130ms. This work provides a production-proven reference for developing robust, cost-effective LLM agents for large-scale industrial dialogue applications.

---


### 228. [LAST-RAG: Literature-Anchored Stochastic Trajectory Retrieval-Augmented Generation for Knowledge-Conditioned Degradation Model Selection](https://arxiv.org/abs/2605.17902)

**<font color=#1a73e8>作者：</font>** Hanbyeol Park, Hyerim Bae  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stochastic-process-based degradation modeling is a core approach for estimating the distribution of remaining useful life (RUL); however, the selection of an appropriate stochastic process has not been sufficiently addressed. Existing model selection methods mainly rely on the statistical fit of the observed health indicator (HI) trajectory, but this approach may select a model that is inconsistent with the underlying degradation mechanism when the observation window is short or the signal is highly noisy. To address this issue, this paper proposes Literature-Anchored Stochastic Trajectory Retrieval-Augmented Generation (LAST-RAG). The proposed method uses both the observed HI trajectory and domain-specific context, and hierarchically conditions the candidate degradation model space based on theoretical and mechanical evidence retrieved from a local evidence bank. In addition, Rule-based Confidence Reasoning with Uncertain State (RCRUS) is introduced to prevent candidate models from being prematurely eliminated when hierarchical decisions are uncertain. Simulation-based experiments demonstrate that the proposed method outperforms statistical, prognostic, and uncertainty-aware baselines in both Wiener/gamma family classification and detailed degradation model classification. Ultimately, this study reframes degradation model selection from a purely statistical goodness-of-fit problem into a knowledge-conditioned decision-making problem that integrates observed data with domain knowledge.

---


### 229. [Agentic Chunking and Bayesian De-chunking of AI Generated Fuzzy Cognitive Maps: A Model of the Thucydides Trap](https://arxiv.org/abs/2605.17903)

**<font color=#1a73e8>作者：</font>** Akash Kumar Panda, Olaoluwa Adigun, Bart Kosko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We automatically generate feedback causal fuzzy cognitive maps (FCMs) from text by teaching large-language-model agents to break the text into overlapping chunks of text. Convex mixing of these chunk FCMs gives a representative cyclic FCM knowledge graph. The text chunks can have different levels of overlap. The chunk FCMs still mix to form a new FCM causal knowledge graph. The mixing technique scales because it uses light computation with sparse causal chunk matrices. The mixing structure allows an operator-level type of Bayesian inference that produces "de-chunked" or posterior-like FCMs from the mixed FCM. These de-chunked FCMs are useful in their own right and allow further iterations of Bayesian updating. We demonstrate these mixing techniques on the essay text of Allison's "Thucydides Trap" model of conflict between a dominant power such as the United States and a rising power such as China. The FCM dynamical systems predict outcomes as they equilibrate to fixed-point or limit-cycle attractors. Seven out of 8 FCM knowledge graphs predicted a type of war when we stimulated them by turning on and keeping on the concept node that stands for the rising power's ambition and entitlement. Gemini 3.1 LLMs served as the chunking AI agents.

---


### 230. [Ethical Hyper-Velocity (EHV): A Provably Deterministic Governance-Aware JIT Compiler Architecture for Agentic Systems](https://arxiv.org/abs/2605.17909)

**<font color=#1a73e8>作者：</font>** Riddhi Mohan Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous agentic systems scale across regulated critical infrastructures, the lack of mechanistic, hardware-rooted enforcement for high-frequency policy updates presents a fundamental safety gap. We introduce Ethical Hyper-Velocity (EHV), a novel architectural framework for the formal verification of AI governance policies at runtime. Unlike retrospective auditing frameworks (ISO/IEC 42001, NIST AI RMF) which introduce 14-30 day latencies, EHV relocates the Policy Enforcement Point (PEP) into the inference pipeline via a Governance-Aware Just-In-Time (JIT) Compiler. By integrating Conflict-free Replicated Data Types (CRDTs) for policy synchronization and Epoch-based Attestation Caching within Trusted Execution Environments (TEEs), EHV achieves Sub-millisecond Formal Determinism (SMFD). We demonstrate via TLA+ formal verification that non-compliant agentic actions are computationally unreachable within the system's bounded operating state space. We prove that O(1) runtime enforcement can eliminate the traditional trade-off between deployment velocity and governance integrity, reducing Governance Latency from O(days) to O(1).

---


### 231. [PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis](https://arxiv.org/abs/2605.17916)

**<font color=#1a73e8>作者：</font>** Jinrang Jia, Zhenjia Li, Yijiang Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating a consistent whole-house VR tour from a floorplan and style reference requires both photorealistic panoramas and cross-view spatial coherence. Pure 2D generators produce appealing single panoramas but re-imagine geometry and materials when the viewpoint changes, whereas monolithic 3D generation becomes expensive and loses fine texture at multi-room scale. We introduce PanoWorld, a generative spatial world model that treats whole-house synthesis as autoregressive generation of node-based 360-degree panoramas, matching the discrete navigation used by real VR tour products. PanoWorld uses a floorplan-derived 3D shell as a global geometric proxy and a dynamic 3D Gaussian Splatting cache as renderable spatial memory. A feed-forward panoramic LRM designed for metric-scale multi-room 360-degree inputs lifts generated panoramas into local 3DGS updates, while Room-aware Group Attention suppresses cross-room feature interference. A topology-aware progressive caching strategy fuses these local updates without repeatedly reconstructing the full history. By decoupling shell-based geometry guidance from cache-rendered visual memory, PanoWorld preserves high-frequency 2D synthesis quality while improving cross-node layout and material consistency. The project link is this https URL

---


### 232. [An Efficient Streaming Video Understanding Framework with Agentic Control](https://arxiv.org/abs/2605.17921)

**<font color=#1a73e8>作者：</font>** Jinming Liu, Jianguo Huang, Zhaoyang Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video requires handling dynamic information density under strict latency budgets. Yet, existing methods typically employ static strategies, such as fixed memory compression or reliance on a single model, forcing a trade-off: fast models fail on complex queries, while always-on heavy models violate real-time constraints and overcomplicate simple queries. Rather than fixing these decisions upfront, we propose R3-Streaming (Remember, Respond, Reason), which formulates streaming video understanding as a cascaded control problem: for each query, the system compresses memory, judges response readiness, and routes computation sequentially, so that each downstream decision builds on progressively refined information states. To optimize this pipeline, we introduce an age-aware forgetting policy for memory compression, as aggressively compressing historical frames can yield substantial performance gains. For compute routing, we propose TB-GRPO, a target-balanced reinforcement learning objective that routes hard queries to a stronger model while preventing mode collapse. Extensive evaluations demonstrate that R3-Streaming achieves state-of-the-art results among streaming MLLMs, reaching 57.92 on OVO-Bench and 76.36 on StreamingBench, while reducing visual token usage by 95 to 96 percent.

---


### 233. [Prompt Compression in Diffusion Large Language Models: Evaluating LLMLingua-2 on LLaDA](https://arxiv.org/abs/2605.17932)

**<font color=#1a73e8>作者：</font>** Sterling Huang, Abigayle Brown, Jiyoo Noh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt compression reduces inference cost and context length in large language models, but prior evaluations focus primarily on autoregressive architectures. This study investigates whether prompt compression transfers effectively to diffusion large language models (DLLMs) using LLMLingua-2, specifically the 8B-parameter DLLM LLaDA. We evaluate compression performance on GSM8K, DUC2004, and ShareGPT using 250 prompts per dataset at an approximate 2$\times$ compression ratio, across mathematical reasoning, prompt reconstruction, and summarization tasks. Outputs generated from original prompts, compressed prompts, reconstructed prompts, and reconstructed-prompt reasoning were compared using exact-match accuracy, BLEU, ROUGE, and BERTScore. Results show that semantic preservation does not necessarily imply stable downstream behavior in diffusion models. Summarization tasks remained comparatively robust under compression, while mathematical reasoning degraded substantially despite high semantic similarity scores. Reconstruction experiments further showed that semantically similar prompts may still omit reasoning-critical information required for stable denoising. Across tasks, BERTScore recall was consistently lower than precision, suggesting that compression failures are primarily driven by information omission rather than semantic drift. These findings indicate that prompt compression methods designed for autoregressive models do not transfer uniformly to diffusion large language models and motivate the development of diffusion-aware compression strategies.

---


### 234. [BacktestBench: Benchmarking Large Language Models for Automated Quantitative Strategy Backtesting](https://arxiv.org/abs/2605.17937)

**<font color=#1a73e8>作者：</font>** Zhensheng Wang, Wenmian Yang, Qingtai Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantitative backtesting is essential for evaluating trading strategies but remains hampered by high technical barriers and limited scalability. While Large Language Models (LLMs) offer a transformative path to automate this complex, interdisciplinary workflow through advanced code generation, tool usage, and agentic planning, the practical realization is significantly challenged by the current lack of a large-scale benchmark dedicated to automated quantitative backtesting, which hinders progress in this field. To bridge this critical gap, we introduce BacktestBench, the first large-scale benchmark for automated quantitative backtesting. Built from over 6 million real market records, it comprises 18,246 meticulously annotated question-answering pairs across four task categories: metrics calculation, ticker selection, strategy selection, and parameter confirmation. We also propose AutoBacktest, a robust multi-agent baseline that translates natural language strategies into reproducible backtests by coordinating a Summarizer for semantic factor extraction, a Retriever for validated SQL generation, and a Coder for Python backtesting implementation. Our evaluation on 23 mainstream LLMs, complemented by targeted ablations, identifies key factors that influence end-to-end performance and highlights the importance of grounded verification and standardized indicator representations.

---


### 235. [SVFSearch: A Multimodal Knowledge-Intensive Benchmark for Short-Video Frame Search in the Gaming Vertical Domain](https://arxiv.org/abs/2605.17946)

**<font color=#1a73e8>作者：</font>** Lingtao Mao, Huangyu Dai, Xinyu Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models are increasingly used as agent backbones that understand multimodal inputs, plan retrieval actions, invoke external tools, and reason over retrieved information. Yet existing benchmarks rarely evaluate this ability in short-video applications, where a paused frame is often visually ambiguous and answering requires vertical, long-tail, and fast-evolving domain knowledge. We introduce SVFSearch, the first open benchmark for short-video frame search in the Chinese gaming domain. SVFSearch contains 5,000 four-choice test examples and 4,198 auxiliary training examples, each centered on a paused game scene from a real short-video clip. To support fair and reproducible evaluation, SVFSearch provides a frozen offline retrieval environment with a game-domain text corpus, a topic-linked image gallery, and text, image, and multimodal retrieval interfaces, avoiding reliance on uncontrolled web search APIs. We evaluate representative paradigms ranging from direct QA and RAG workflow to Plan-Act-Replan agents and learned search models. Results reveal a large gap between model-only answering, practical agentic search, and oracle knowledge: the best open-source direct-QA model reaches 66.4%, the best practical agent achieves 79.1%, and oracle knowledge reaches 95.4%. Further analysis exposes bottlenecks in visual grounding, retrieval quality, evidence-grounded reasoning, and tool-use behavior, including over-search, answer-only shortcuts, and retrieval-induced misleading.

---


### 236. [SkyNative: A Native Multimodal Framework for Remote Sensing Visual Evidence Reasoning](https://arxiv.org/abs/2605.17949)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Ronghao Fu, Zhiwen Lin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing vision-language models commonly rely on pretrained visual encoders to convert images into semantic features before language-model reasoning. While effective for scene-level understanding, this pipeline may prematurely compress local visual evidence, making fine-grained spatial reasoning vulnerable to language priors, especially in ultra-high-resolution remote sensing imagery. We present SkyNative, a native multimodal framework for remote sensing that adopts an encoder-free architecture, removing the pretrained visual backbone to directly represent images as raw patch tokens in the language-model token space. To reconcile low-level visual patches with textual tokens, SkyNative introduces a modality-aware decoupling mechanism that uses modality-specific parameters within a unified autoregressive backbone. We further introduce a visual reliance benchmark that diagnoses whether models ground their answers in image evidence through progressive visual degradation and misleading textual prompts. Across standard remote sensing understanding tasks and large-format spatial reasoning evaluations, SkyNative shows stronger image-grounded perception and improved robustness against prompt-induced language priors. These results suggest that native patch-level multimodal modeling is a promising direction for reliable remote sensing vision-language reasoning.

---


### 237. [A More Word-like Image Tokenization for MLLMs](https://arxiv.org/abs/2605.17954)

**<font color=#1a73e8>作者：</font>** Hyun Lee, Hyemin Jeong, Yejin Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern multimodal large language models (MLLMs) typically keep the language model fixed and train a visual projector that maps the pixels into a sequence of tokens in its embedding space, so that images can be presented in essentially the same form as text. However, the language model has been optimized to operate on discrete, semantically meaningful tokens, while prevailing visual projectors transform an image into a long stream of continuous and highly correlated embeddings. This causes the visual tokens to behave differently from the word-like units that LLMs are originally trained to understand. We propose a novel Disentangled Visual Tokenization (DiVT) that clusters patch embeddings into coherent semantic units, so each token corresponds to a distinct visual concept instead of a rigid grid cell. DiVT further adapts its token budget to image complexity, providing an explicit accuracy-compute trade-off modifying neither the vision encoder nor the language model. Across diverse multimodal benchmarks, DiVT matches or surpasses baselines with significantly fewer visual tokens, demonstrating robustness under limited token budgets, significantly reducing memory cost and latency while making visual inputs more compatible with LLMs. Our code is available at this https URL.

---


### 238. [Enhancing the Code Reasoning Capabilities of LLMs via Consistency-based Reinforcement Learning](https://arxiv.org/abs/2605.17958)

**<font color=#1a73e8>作者：</font>** Zhanyue Qin, Jia Feng, Yibo Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code reasoning refers to the task of predicting the output of a program given its source code and specific inputs. It can measure the reasoning capability of large language models (LLMs) and also benefit downstream tasks such as code generation and mathematical reasoning. Existing work has verified the effectiveness of reinforcement learning on the task. However, these methods design rewards solely based on final outputs or coarse-grained signals, and neglect the inherent consistency of the stepwise reasoning process in the task. Therefore, these methods often result in sparse reward or reward hacking, which limits the full play of enhanced learning capabilities. To alleviate these issues, we propose CodeThinker, a consistency-driven reinforcement learning framework for code reasoning. Specifically, CodeThinker has three key components: (1) a stepwise reasoning-aware model training module, which utilizes a consistency tracing paradigm as a template to synthesize training data that captures the stepwise reasoning process; (2) a dynamic beam sampling strategy, which aims to improve the quality of sampled outputs under a fixed sampling budget; and (3) a consistency reward mechanism that can effectively alleviate reward hacking. Experiments on three popular benchmarks show that CodeThinker achieves state-of-the-art performance across multiple LLMs. For instance, it outperforms the strongest baseline by 4.3% in accuracy when deployed on Qwen2.5-Coder-7B-Instruct. We also validate the effectiveness of CodeThinker on downstream tasks. Results show that, without additional training, CodeThinker obtains average accuracy gains of 5.33 and 3.11 percentage points on mathematical reasoning and code reasoning tasks covering 17 programming languages, respectively.

---


### 239. [Reconciling Contradictory Views on the Effectiveness of SFT in LLMs: An Interaction Perspective](https://arxiv.org/abs/2605.17967)

**<font color=#1a73e8>作者：</font>** Junpeng Zhang, Lei Cheng, Guoxi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper explores a scientific question in supervised fine-tuning (SFT): why SFT is broadly effective for small-scale deep neural networks, yet can produce inconsistent or even detrimental effects when applied to large language models (LLMs). Recent advances in interaction-based explanations suggest that interactions between words/tokens provide a faithful metric for quantifying the inference patterns encoded by LLMs. We find that the evolution of interactions during SFT can effectively explain the inconsistent effectiveness of SFT for LLMs. Specifically, we find that (1) SFT primarily removes noise-like interactions, while rarely acquiring reliable new interactions. (2) This denoising stage is extremely brief, after which continued fine-tuning tends to introduce overfitted interactions. We validate these findings across multiple LLMs and datasets. Our findings provide new insights into early stopping and offer practical guidance for LLM training.

---


### 240. [Generation Navigator: A State-Aware Agentic Framework for Image Generation](https://arxiv.org/abs/2605.17969)

**<font color=#1a73e8>作者：</font>** Jinming Liu, Ruoyu Feng, Yuqi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advances in text-to-image generation, faithfully realizing user intent remains challenging, often requiring manual multi-turn trial and error. To automate this process, existing systems rely on either simple prompt rewriting or closed-loop agents driven by hand-crafted rules, rather than learning to adapt actions to the evolving generation process. In this paper, we reformulate image generation as a state-conditioned action-making problem and propose Generation Navigator, a multi-turn T2I agent that learns to dynamically steer the generation trajectory and output the next action. However, training this agent via reinforcement learning introduces a critical credit assignment challenge: naively rewarding a trajectory based solely on a single state assigns equal credit to all actions in the rollout, ignores the quality dynamics across turns, and fails to distinguish actions that improve the trajectory from those that degrade it or waste turns without progress. We resolve this with PRE-GRPO (Peak-Retention-Efficiency Group Relative Policy Optimization), a trajectory-level reinforcement learning objective that explicitly rewards discovering a high-quality image (Peak), avoiding subsequent quality degradation across turns (Retention), and minimizing unnecessary turns (Efficiency). Experiments show substantial improvements across benchmarks, reaching a WISE score of 0.90 and 79.06% reasoning accuracy on T2I-ReasonBench.

---


### 241. [Unleashing LLMs in Bayesian Optimization: Preference-Guided Framework for Scientific Discovery](https://arxiv.org/abs/2605.17976)

**<font color=#1a73e8>作者：</font>** Xinzhe Yuan, Zhuo Chen, Jianshu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is increasingly constrained by costly experiments and limited resources, underscoring the need for efficient optimization in AI for science. Bayesian Optimization (BO), though widely adopted for balancing exploration and exploitation, often exhibits slow cold-start performance and poor scalability in high-dimensional settings, limiting its applicability in real-world scientific problems. To overcome these challenges, we propose LLM-Guided Bayesian Optimization (LGBO), the first LLM preference-guided BO framework that continuously integrates the semantic reasoning of large language models (LLMs) into the optimization loop. Unlike prior works that use LLMs only for warm-start initialization or candidate generation, LGBO introduces a region-lifted preference mechanism that embeds LLM-driven preferences into every iteration, shifting the surrogate mean in a stable and controllable way. Theoretically, we prove that LGBO does not perform significantly worse than standard BO in the worst case, while achieving significantly faster convergence when preferences align with the objective. Empirically, LGBO consistently outperforms existing methods across diverse dry benchmarks in physics, chemistry, biology, and materials science. Most notably, in a new wet-lab optimization of Fe-Cr battery electrolytes, LGBO attains \textbf{90\% of the best observed value within 6 iterations}, whereas standard BO and existing LLM-augmented baselines require more than 10. Together, these results suggest that LGBO offers a promising direction for integrating LLMs into scientific optimization workflows.

---


### 242. [AutoVecCoder: Teaching LLMs to Generate Explicitly Vectorized Code](https://arxiv.org/abs/2605.17978)

**<font color=#1a73e8>作者：</font>** Shangzhan Li, Xinyu Yin, Xuanyu Jin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vectorization via Single Instruction, Multiple Data (SIMD) architectures is a cornerstone of high-performance computing. To fully exploit hardware potential, developers often resort to explicit vectorization using intrinsics, as compiler-based auto-vectorization frequently yields suboptimal results due to conservative static analysis. While Large Language Models (LLMs) have demonstrated remarkable proficiency in general code generation, they struggle with explicit vectorization due to the scarcity of high-quality corpora and the strict semantic constraints of low-level hardware instructions. In this paper, we propose AutoVecCoder, a novel framework designed to empower LLMs with the capability of automated explicit vectorization. AutoVecCoder integrates two core components: VecPrompt, an automated data synthesis pipeline to inject domain-specific intrinsic knowledge; and VecRL, a reinforcement learning framework that aligns code generation with execution efficiency. AutoVecCoder-8B trained by this framework achieves state-of-the-art performance on the SSE and AVX subsets of SimdBench and, in some cases, generates implementations surpassing standard -O3 optimizations, effectively overcoming the inherent bottlenecks of traditional automated vectorization.

---


### 243. [SAFE-SVD: Sensitivity-Aware Fidelity-Enforcing SVD for Physics Foundation Models](https://arxiv.org/abs/2605.17985)

**<font color=#1a73e8>作者：</font>** Chengjie Hong, Feixiang He, Yiheng Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new method for compressing physics foundation models (PFMs) which is a new trend in AI for Science. While model compression is essential for reducing memory use and accelerating inference in large foundation models, it remains under-explored for PFMs, where preserving physical fidelity is crucial. The challenge lies in the functional nature of physics data, where partial derivatives encode spatiotemporal dynamics and exhibit high sensitivity to compression. Conventional compression methods ignore this structure, often causing severe performance degradation or failure. To address this, we introduce a sensitivity-aware fidelity-enforcing compression framework that explicitly models loss-aware layer sensitivity in the output function space during compression. This provides a new route to compressing scientific foundation models while preserving accuracy and physical fidelity. Experiments show substantial gains over existing methods across multiple models and datasets, achieving significantly higher compression ratios while maintaining accuracy, in some cases by orders of magnitude. More broadly, the work potentially leads to a new subfield of efficient, deployable, and sustainable scientific foundation models in AI for Science.

---


### 244. [Predictive Prefetching for Retrieval-Augmented Generation](https://arxiv.org/abs/2605.17989)

**<font color=#1a73e8>作者：</font>** Wuyang Zhang, Shichao Pei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves factual grounding in large language models but suffers from substantial latency due to synchronous retrieval. While recent work explores asynchronous retrieval, existing approaches rely on heuristic coordination between retrieval and generation and assume stable information demands during decoding that often break in complex, multi-domain settings. In this paper, we propose an advanced asynchronous retrieval framework that enables predictive prefetching aligned with evolving information needs. The framework explicitly predicts when retrieval should be triggered and what information should be retrieved using three components, a retrieval predictor, a context monitor, and a query generator, by exploiting semantic precursors in generation dynamics that emerge several tokens before uncertainty becomes critical. Experiments on multiple benchmarks demonstrate up to 43.5% end-to-end latency reduction and 62.4% improvement in time-to-first-token, while maintaining answer quality comparable to synchronous RAG baselines.

---


### 245. [MARR: Module-Adaptive Residual Reconstruction for Low-Bit Post-Training Quantization](https://arxiv.org/abs/2605.17997)

**<font color=#1a73e8>作者：</font>** Le Su, Xing Luo, Zhi Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, residual reconstruction-based model quantization methods have achieved promising performance in low-bit post-training quantization (PTQ) by introducing cross-layer residuals to reduce error accumulated from previous this http URL, these residuals may also introduce additional bias arising from the Hessian-approximation (HA) assumption underlying reconstruction-based PTQ, leading to suboptimal quantization this http URL this work, we analyze that multiplying the residual term by a scaling coefficient provides a direct way to mitigate the HA bias associated with residual strength, while preserving accumulated-error correction. More importantly, we observe that this trade-off is module-dependent, making a single global residual strength insufficient to balance effective correction and residual-related bias across this http URL on these observations, we propose Module-Adaptive Residual Reconstruction (MARR), which assigns a module-specific scaling coefficient to adaptively balance accumulated-error correction and residual-related HA bias for each this http URL avoid expensive per-module coefficient search and obtain a stable coefficient estimate, we design a Proportional-Integral-Derivative (PID)-based adaptive update strategy that uses reconstruction error as feedback to progressively refine this coefficient. Experiments on several typical large language models (LLMs) and vision transformers (ViTs) demonstrate the effectiveness of MARR under low-bit quantization (less than or equal to 4-bit), achieving up to 20.2% performance gains on LLMs and up to 4.6% relative gains on ViTs over the residual reconstruction state-of-the-art this http URL will be made publicly available upon acceptance.

---


### 246. [Shared Backbone PPO for Multi-UAV Communication Coverage with Connection Preservation](https://arxiv.org/abs/2605.17999)

**<font color=#1a73e8>作者：</font>** Z. Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Shared Backbone Proximal Policy Optimization (Shared Backbone PPO) algorithm. By sharing the base module between the Actor and Critic networks, the algorithm achieves efficient training and improved performance. The algorithm is implemented in a connectivity-preserving multi-UAV swarm communication coverage task and compared with the standard PPO algorithm. Experimental results demonstrate that the proposed method achieves superior performance. Furthermore, a graph information aggregation module is incorporated into the model architecture to accommodate the communication conditions among agents. With the integration of this module, the algorithm remains effective, and the trained agent swarm exhibits a higher level of cooperation.

---


### 247. [LogRouter: Adaptive Two-Level LLM Routing for Log Question Answering in Big Data Systems](https://arxiv.org/abs/2605.18015)

**<font color=#1a73e8>作者：</font>** Mert Coskuner, Merve Zeybel, Melik Mert Dolan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production log analytics in self-hosted, resource-constrained environments requires natural-language access to massive log streams without the cost of routing every query through a large language model. We present LogRouter, an end-to-end log question-answering system deployed on TUBITAK BILGEM's national big data platform that combines a PySpark-based Drain3 ingestion pipeline, GPU-accelerated embeddings, and dual-index storage in Apache Druid and PostgreSQL with pgvector. A two-level cost-aware router dispatches each query along one of four execution paths: direct response, Druid keyword search, template lookup with SQL generation, and pgvector semantic retrieval, while a Level-2 router selects either a 14B-class or 32B-class generator for the semantic path. A dedicated coder LLM handles text-to-SQL generation. We evaluate the system on four LogHub datasets (Linux, Apache, Windows, and Mac; 70 questions in total) under both an online full-pipeline configuration and an offline configuration that isolates the generator. The router reaches 88.4% mean accuracy across datasets and 94.7% on Linux, while the full pipeline attains a mean ROUGE-1 of 0.373, BERTScore of 0.879, RAGAS Faithfulness of 0.779, and an end-to-end latency of 18.6 s. In an apples-to-apples offline comparison, the routed system reduces mean latency by 55% versus a Fixed-32B baseline (46.3 s vs. 102.1 s) while preserving Answer Correctness within 5.8 points and exceeding a Fixed-14B baseline on RAGAS Faithfulness across every dataset. Cost-aware dispatching is therefore a practical mechanism for production log QA: routing recovers most of the quality of an always-32B configuration at less than half the latency, and the L1 keyword vocabulary makes that routing decision with high precision without a learned classifier.

---


### 248. [See What I Mean: Aligning Vision and Language Representations for Video Fine-grained Object Understanding](https://arxiv.org/abs/2605.18018)

**<font color=#1a73e8>作者：</font>** Boyuan Sun, Bowen Yin, Yuanming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SWIM (See What I Mean), a novel training strategy that aligns vision and language representations to enable fine-grained object understanding solely from textual prompts. Unlike existing approaches that require explicit visual prompts, such as masks or points, SWIM leverages mask supervision only during training to guide cross-modal attention, allowing the model to automatically attend to the user-specified object at inference. Our cross-attention analysis of pretrained multimodal large languagemodels (MLLMs) reveals a systematic discrepancy: Attribute words produce sharp, localized activations in the visual modality, whereas object nouns yield diffuse and scattered patterns due to semantic reference bias and distributed high-level representations. To address this misalignment, we construct NL-Refer, an enriched dataset, in which each object mask is paired with a precise natural language referring expression. SWIM extracts multi-layer cross-attention maps from object nouns and enforces spatial consistency with ground-truth masks. Experimental results demonstrate that SWIM substantially improves text-visual alignment and achieves superior performance over visual-prompt-based methods on fine-grained object understanding benchmarks. The code and data are available at \href{this https URL}{this https URL}.

---


### 249. [TeleCom-Bench: How Far Are Large Language Models from Industrial Telecommunication Applications?](https://arxiv.org/abs/2605.18025)

**<font color=#1a73e8>作者：</font>** Jieting Xiao, Yun Lin, Huizhen Qiu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models have achieved remarkable integration in various vertical scenarios, their deployment in the telecommunications domain remains exploratory due to the lack of a standardized evaluation framework. Current telecom benchmarks primarily focus on static, foundational knowledge and isolated atomic skills, neglecting the equipment-specific documentation and end-to-end industrial workflows essential for real-world production systems. To bridge this gap, we present TeleCom-Bench, a comprehensive benchmark comprising 12 evaluation sets with 22,678 curated samples, which evaluates LLMs across a synergistic hierarchy: (1) Multi-dimensional Knowledge Comprehension, which integrates telecommunication fundamentals, 3GPP protocols, and 5G network architecture with proprietary product knowledge across wired, core, and wireless networks via knowledge graph-driven synthesis; and (2)End-to-End Knowledge Application, which formalizes six core tasks on authentic trajectories from live network agent workflows, including intent recognition, entity extraction, event verification, tool invocation, root cause analysis, and solution generation-across network optimization and fault maintenance scenarios. Evaluations of eight state-of-the-art LLMs reveal a universal Execution Wall: while models achieve 90% accuracy in linguistic interface tasks such as intent recognition and entity extraction, performance collapses to approximately 30% in procedural execution tasks like solution generation. This capability gap demonstrates that current LLMs function competently as diagnosticians but fail as field engineers. TeleCom-Bench provides standardized diagnostics to precisely pinpoint this deficit, offering actionable guidance for domain-specific alignment toward production-ready telecom agents. The dataset and evaluation code have been released at this https URL.

---


### 250. [What Matters for Grocery Product Retrieval with Open Source Vision Language Models](https://arxiv.org/abs/2605.18029)

**<font color=#1a73e8>作者：</font>** Emmanuel G. Maminta, Rowel O. Atienza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal product retrieval (MPR) underpins checkout-free retail and automated inventory systems, yet it demands fine-grained SKU discrimination that standard vision-language benchmarks fail to capture. We present the first systematic zero-shot evaluation of 190 open-source VLMs on the MPR task of the GroceryVision Challenge, isolating pre-training data, architecture, and input resolution. Our analysis yields three actionable findings. \textbf{(1) Data quality trumps scale.} Switching from raw web-scrapes to filtered datasets delivers up to 16.6\% accuracy gains, exceeding the benefit of doubling model parameters. \textbf{(2) Efficient models can win.} MobileCLIP-B (150M parameters) outperforms 351M counterparts trained on noisy data. We introduce \textit{semantic power density} ($\phi$), an efficiency metric that penalizes sub-threshold accuracy. \textbf{(3) A precision gap persists.} State-of-the-art models achieve 94.5\% Recall@5 but suffer a 17.5\% drop at Recall@1, revealing that contrastive embeddings cluster categories effectively but fail to rank visually similar SKUs. Code and evaluation scripts are available at \url{this https URL}.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-346](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
