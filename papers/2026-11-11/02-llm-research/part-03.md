# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 101. [Represented but Not Used: Value-Policy Dissociation in LLM Agents](https://arxiv.org/abs/2611.10457)

**<font color=#1a73e8>作者：</font>** Yuzhang Luo, Mohamed Aghzal, Liangming Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents need to choose actions whose consequences unfold over multiple future steps, yet poor decisions do not reveal whether the model failed to represent those consequences or failed to use them. Mechanistic interpretability has studied internal representations of environment state and plans, but sequential decision making also requires evaluating how candidate actions change future outcomes. Reinforcement learning formalizes this as action value. We study this computation in Qwen2.5-7B-Instruct, Qwen2.5-32B-Instruct, and GPT-OSS-20B across a partially observed Grid environment and WebShop, a simulated web shopping environment. We find that the relative values of candidate actions are linearly decodable from intermediate hidden states, including at states where the policy prefers a worse action. We call this gap between value representation and policy choice value-policy dissociation. To investigate how represented value relates to action selection, we compare direct interventions along the value readout direction with Natural Value Transport (NVT), a transformation learned from hidden state changes that naturally result from differences in action value. While readout-direction interventions have limited and inconsistent effects, NVT more consistently influences action preferences, particularly at later layers. We also test a closed-loop controller that uses the value readout as a sensor and NVT as an actuator, observing improvements in task outcomes. These results suggest that LLM agents can represent useful prospective value without reliably translating it into policy choice.

---


### 102. [LongCapHarness: Capability-Guided Auto-Harnessing for Long-Context Reasoning](https://arxiv.org/abs/2611.10463)

**<font color=#1a73e8>作者：</font>** Tao Zhang, Yuhang He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing methods enhancing an LLM's long-context reasoning capability often rely on data synthesis and follow-up LLM post-training. However, the data synthesis strategy and the post-training recipes are empirically driven and computationally intensive. In this work, we propose a new framework, dubbed LongCapHarness, to instead harness the underlying capabilities for long-context reasoning. The harnessing process recursively revises and updates capability primitive implementation, capability state and control logic through recursive self-improvement on the development set. With neither data synthesis nor LLM post-training, LongCapHarness is applied to Llama3-8B and transferred to Qwen2.5-3B. LongCapHarness substantially outperforms recent data-synthesis-based baselines on HELMET and RULER benchmarks; its estimated development cost is less than 50% of the estimated training costs of NExtLong and PolicyLong. We hope these results motivate further research into harnessing the latent capabilities of LLMs to solve tasks beyond their explicit training.

---


### 103. [Who Benefits, and When? Trajectories of Academic Achievement and Interest in AI-Supported Learning](https://arxiv.org/abs/2611.10467)

**<font color=#1a73e8>作者：</font>** Hyejeong Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-supported learning environments are increasingly used, yet relatively little is known about how students' achievement and interest develop over time or whether these trajectories vary across learners. This study examined longitudinal trajectories of mathematics achievement and interest in a semester-long AI-supported mathematics learning. Using a mixed-methods longitudinal design, repeated measures of mathematics achievement were collected at four time points and mathematics interest at three time points. Linear mixed models (LMMs) were used to examine overall changes over time, while linear quantile mixed models (LQMMs) were used to examine differences in trajectories across the lower, median, and upper portions of the outcome distributions. Mathematics achievement increased substantially during the intervention, with the largest gains emerging between the second and third measurement occasions. However, the trajectory differed across the achievement distribution. Mathematics interest increased significantly after the first month, but this increase was not sustained through the end of the semester. Qualitative findings further indicated that students experienced the AI platform differently. The study highlights the importance of examining both cognitive and motivational trajectories.

---


### 104. [Hibana: Fast Agentic Inference on Unified-Memory Devices](https://arxiv.org/abs/2611.10469)

**<font color=#1a73e8>作者：</font>** Yahya Emara, Chi-Chih Chang, Anthony Fei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Local AI promises capable personal assistants that run on users' own devices, keeping data and computation under their control. Open-weight models that fit on local devices can now handle practical tasks such as coding. Yet current inference engines fall short. Popular engines such as vLLM and SGLang target datacenter GPUs with dedicated host memory, while local engines underuse the memory hierarchy of unified-memory devices. We present Hibana, an inference engine for unified-memory devices that co-optimizes model representation, memory management, and decoding strategy. Model surgery, the process of editing a trained model's architecture to suit its hardware, changes how the model computes, shrinking its memory footprint and data movement. Unified-memory management preserves each agent's state across turns, so long-running agents can resume instantly instead of recomputing their state. Adaptive speculation generates several tokens per step. Hibana codesigns these features around the shared memory capacity and limited bandwidth of unified-memory systems-on-chip to support local multi-agent workloads. On a single DGX Spark serving Qwen and Nemotron models of up to 125B parameters, Hibana completes up to 3.4$\times$ more agentic tasks per hour and delivers up to 3.9$\times$ higher decoding throughput than other established frameworks such as vLLM, NVIDIA Flare, this http URL, and TensorFold. Code is available at this https URL.

---


### 105. [PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns](https://arxiv.org/abs/2611.10477)

**<font color=#1a73e8>作者：</font>** Yi Ge, Heng Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning-trained agents for retrieval-augmented generation retrieve content (passages, knowledge-graph fragments, or hyperedges) and supervise training with outcome rewards on the final answer. Across these paradigms the reasoning route through retrieved content never leaves the language model's hidden state, conflating declarative knowledge with the procedural knowledge that recurs across queries of the same logical type; content-only methods consequently plateau as reasoning depth grows. We introduce PatternBloom, an agentic RAG framework that shifts the unit of retrieval from content (what to read) to logic (how to reason). A first RL stage scores the agent's constructed evidence graph by a frozen oracle's information gain through the Information-Density Reward (IDR), a size-normalized mutual-information surrogate. High-reward trajectories are distilled into a Graph Pattern Memory (GPM) of type-abstracted reasoning skeletons, and a second RL stage uses the Pattern-Augmented Reward (PAR) to couple policy to memory, turning procedural reasoning into a learnable, externalized structural prior. A 7B PatternBloom outperforms $27$ baselines by $+15.0$ Avg-OOD EM, with the gain compounding with reasoning depth precisely because procedural knowledge, once distilled, is reused rather than re-derived at every query. We release our code at this https URL.

---


### 106. [They Can See It but Not Say It: Iterative Self Knowledge Re-expression in Visual Reasoning Relative Pose Identification](https://arxiv.org/abs/2611.10483)

**<font color=#1a73e8>作者：</font>** Mengyu Wang, Ken Deng, Yftah Ziser 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of visual reasoning relative pose identification (VRRPI) has exposed critical weaknesses in the multi-view 3D spatial reasoning capabilities of modern vision-language models (VLMs). We present a systematic analysis of VLMs' behavior in VRRPI, uncovering stable output biases where VLMs disproportionately predict specific motion patterns regardless of visual evidence. To mitigate these inherent biases, we propose self knowledge re-expression with iterative debiasing (SKR-ID), an annotation-free pipeline that adapts VLMs for VRRPI using only randomly extracted unannotated image pairs. SKR-ID transitions VLMs' output mechanism from generic next-token prediction to task-optimized classification heads. The pipeline proceeds in two stages: (1) a cold-start initialization using debiasing object-centric prompts to anchor motion inference in 2D visual evidence; and (2) a recursive logit-ranking mechanism that enforces statistical parity by using the median logit value as a dynamic threshold. Experimental evaluation across frontier VLMs on standard benchmarks demonstrates that SKR-ID significantly mitigates systematic biases. Our method improves open-source VLMs' Macro-F1 scores from 35.0-45.4% to 53.7-58.0%, without using any annotated data. These results show that SKR-ID can effectively improve 3D reasoning performance from a severely collapsed baseline. The code is publicly available at this https URL.

---


### 107. [Can General-Purpose Generative AI Supply Training Data for Medical Vision Models? A Multimodal Retrospective Study](https://arxiv.org/abs/2611.10484)

**<font color=#1a73e8>作者：</font>** Jiachuan Peng, Kyle Lam, Jierui Qu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Well-annotated, diverse medical imaging datasets remain a major constraint for vision-based medical AI. We evaluated Nano Banana, a general-purpose image generation and editing model, as a source of synthetic medical images for model training, subgroup augmentation, and model auditing. Methods: In this retrospective study across four imaging modalities, chest radiography, fundus photography, and CT models were trained only on synthetic images and externally validated on real-world data against real-data-trained models. Carotid ultrasound models were trained on a private Human Phenotype Project cohort (aged 40-75 years) with and without synthetic augmentation. Clinicians rated image plausibility. Evaluation used AUROC, AUPR, calibration, and decision curve analysis. Findings: Synthetic-only models achieved AUROCs of 0.877 (95% CI 0.843-0.910) for pneumonia (n=14863), 0.963 (0.948-0.975) for retinal detachment (n=1149), and 0.711 (0.600-0.823) for renal calculus (n=4122), comparable to real-data-trained models, but their calibration and net benefit were not consistently more favorable. With mixed synthetic-real training, a carotid ultrasound model produced an ordinal vascular age index that stratified 633 external subjects into subgroups differing in BMI and glucose (both p<0.01), linking vascular aging to cardiometabolic health. To stress-test shortcut learning, editing a moderate tessellated pattern into fundus photographs reduced the true-class probability for central serous chorioretinopathy from 0.996 to 0.822. Clinician-guided editing raised low-quality CT plausibility from 3.10/5 to 4.30/5. Interpretation: Synthetic data can complement real data in model training, subgroup representation, and model testing via controlled editing, but its clinical value should be assessed with calibration, decision curve analysis, and clinician review, not discrimination alone.

---


### 108. [Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking](https://arxiv.org/abs/2611.10486)

**<font color=#1a73e8>作者：</font>** Bowen Zuo, Yue Yu, Dongruo Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) generate text through iterative denoising, where decisions about which tokens to commit or remask strongly affect output quality. Existing certainty-aware strategies rely on instantaneous confidence or entropy, but these local signals can be misleading on difficult reasoning problems. We formulate DLM test-time scaling as adaptive allocation of both inference compute and decoding strategies. Our two-stage approach uses a fast base sampler to solve easy questions, then applies frequency-aware remasking to the remaining hard questions. This strategy tracks how often each token's prediction changes across denoising steps and preferentially commits frequently changing tokens, encouraging samples to explore alternative reasoning paths rather than collapse onto the model's preferred trajectory. Experiments with LLaDA-8B-Instruct and Dream-7B-Instruct show consistent improvements over a strong adaptive allocation baseline, with absolute accuracy gains of up to 3.73 percentage points (LLaDA) and 7.33 percentage points (Dream) on MATH-500, and absolute coverage gains of up to 11.39 percentage points (LLaDA) and 10.98 percentage points (Dream) on HumanEval. On questions unsolved by the base certainty-aware strategy after 100 samples, frequency-aware remasking recovers solutions for 3.75% to 18.75% of examples.

---


### 109. [Safer for Whom? A Systematic Exploration of AI Safety in Eating Disorder Interactions](https://arxiv.org/abs/2611.10488)

**<font color=#1a73e8>作者：</font>** Jinyuan Wang, Minh Duc Chu, Frances Ross 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistants advise users about diet, exercise, and weight loss---areas in which unsafe guidance can worsen body dissatisfaction, dietary restriction, compulsive exercise, and other behaviors associated with eating disorders (EDs). Existing evaluations emphasize diagnostic accuracy, overtly harmful prompts, or synthetic scenarios, providing limited insight into whether models recognize implicit vulnerability in natural interactions or protect users consistently. We evaluate responses from three open-weight large language models to 100 questions sourced from an online pro-anorexia community. We grade responses using clinically informed criteria that extend a seven-dimensional taxonomy of ED-related harms. We also construct matched conditions in which questions are accompanied by information about the user varying race, gender, body mass index (BMI), and explicit ED vulnerability. Safety varies substantially across models and harm dimensions. High-risk responses are approximately twice as frequent without bios, suggesting that models do not consistently recognize vulnerability from language alone. Explicit signals of ED vulnerability improve safety by 10--14 points across models. Responses also differ significantly by race, gender, and BMI, with body size producing the largest disparities. These patterns are consistent with reliance on the stereotype that EDs primarily affect thin, White women, potentially leaving users outside this profile with less protective responses.

---


### 110. [Sampling Is Not Curiosity: Why LLM Agents Should Investigate](https://arxiv.org/abs/2611.10501)

**<font color=#1a73e8>作者：</font>** Alfonso Amayuelas, Piotr Piękos, Xin Eric Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used for open-ended tasks, very common in research scenarios where they are required to explore, investigate, or act curiously. At inference time, an LLM is a fixed map from context to next-token distribution, the pretrained weights determine the function, and only its conditioning changes as context accumulates. Mechanisms like temperature, best-of-N, tree search, or RAG vary how the distribution is sampled or what it is conditioned on, but do not update the agent's model of the environment. We argue that current LLM agents do not explore curiously; they explore stochastically. From how curiosity is understood in the RL literature, it requires a predictive structure over how the environment responds to the agent's actions, which improves online from current interaction, drives action selection through its predicted improvement, and persists beyond the context window. Additionally, in its open-ended form, the agent should intrinsically originate what to investigate. Thus, we propose a framework defining curiosity in LLM agents, reserving the term for systems that satisfy it. In doing so, we identify the research directions its implementation opens up.

---


### 111. [Distinguishing Extraction Failures and Clinical Discordance with LLM Uncertainty on Radiology Reports](https://arxiv.org/abs/2611.10502)

**<font color=#1a73e8>作者：</font>** Jerjes Aguirre-Chavez, Shant Malkasian, Roshun Sankaran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can structure clinical datasets, but extraction error must be distinguished from discordance in the underlying data. From a real-world cohort of 1{,}045 patients undergoing coronary CT angiography (CCTA), we evaluated whether LLM uncertainty during vessel-level coronary artery disease (CAD) stenosis extraction could identify extraction failure and clinical discordance. References were expert CCTA annotations (253 patients) and subsequent invasive coronary angiography (ICA; 729 patients). We quantify extraction failure as disagreement between stenosis severity in LLM extracted versus expert annotations, and clinical discordance as disagreement in stenosis severity between CCTA and subsequent ICA. Stenosis Margin, selected from ten candidate measures, was used to quantify LLM uncertainty, and generalized estimating equation logistic regression and AUC evaluated its association and incremental discrimination for each failure mode. LLM uncertainty was strongly associated with extraction failure (adjusted OR 4.15 [95% CI 2.57--6.69], $P<0.001$) and substantially improved discrimination beyond LLM-extracted CCTA stenosis severity alone (AUC 0.81 to 0.86; $\Delta$AUC $+0.06$ [$+0.03$, $+0.09$], $P=0.001$). In contrast, LLM uncertainty weakly associated with clinical discordance (adjusted OR 1.22 [1.04--1.43], Holm-adjusted $P=0.118$) but provided no incremental discrimination beyond LLM-extracted CCTA stenosis severity ($\Delta$AUC $+0.01$ [$-0.00$, $+0.02$], $P=0.245$). Moreover, extraction errors and clinical discordance showed little overlap, with 38 of 42 clinically discordant vessels (90%) having been extracted correctly. LLM uncertainty may identify extraction failures without identifying underlying clinical discordance, supporting failure attribution when evaluating LLM-derived clinical datasets.

---


### 112. [Imperfectly Imperfect: Evaluating Graded Cognitive Diversity in LLM Persona Simulations](https://arxiv.org/abs/2611.10508)

**<font color=#1a73e8>作者：</font>** Sion Weatherhead, Ben Newell, Aaron Belbasis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly used as synthetic participants in social, behavioural, and decision-making research, yet it remains unclear whether they can express graded cognitive diversity as assigned when engaging in simulated behaviour. We introduce a cognition-suite evaluation that tests whether simulated populations reproduce human variation in reasoning, self-reported traits, their associations, and downstream behaviour. Agents conditioned on synthetic or human-derived profiles of cognitive reflection, Need for Cognition, and Big Five personality answer the same suite as a cohort of 473 adults: two newly assembled tests, a Cognitive Reflection Test (CRT) and a Behavioural Reflection Test (BRT) whose decision scenarios measure reflection in behaviour, alongside an established CRT and the two trait questionnaires. Across seven full-battery simulation runs of four models, agents recover Need for Cognition and Big Five trait distributions on self-report questionnaires, but fall short on simulating diversity of cognitive task performance and downstream behaviours. In the four Claude Sonnet 4.6 runs, every agent scores full marks on both CRTs, whatever reflection level its persona was assigned. In the other three runs agents make intuitive-lure errors (the tempting wrong answers CRT items invite), but 49 to 85% score full marks, against under 10% in the human sample. Claude Sonnet 5 comes closest to people's item-by-item pattern of lures; the other two runs give fewer lures and vary less between items. In the BRT scenarios, every run over-produces 8 to 11 of 15 coded behaviours by at least 20 percentage points, and people's links between reflection and behaviour carry over only in part. Useful synthetic populations must preserve not only trait descriptors but the structured variation in reasoning, error type, and behaviour those descriptors are meant to organise.

---


### 113. [CALFA-KV: Joint Calibration and Fisher-Guided Anchors for 1-Bit KV Cache Compression](https://arxiv.org/abs/2611.10511)

**<font color=#1a73e8>作者：</font>** Xiancai Tian, Leichao Zhang, Shenhui Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 1-bit key-value (KV) cache compression can combine quantizer calibration with selective high-precision storage to reduce reconstruction error. We propose Calibration and Fisher-guided Anchors for KV cache compression (CALFA-KV). Offline, we jointly fit a key center, radial normalization parameters, and K/V vector codebooks to match the frozen model's projected attention output. We also estimate channel-wise Fisher-type sensitivities from squared gradients of a reference next-token cross-entropy loss. Online, we use these sensitivities to weight the squared reconstruction errors of each KV state. Here, a KV state is one token's key-value pair within one layer and KV head. We retain the highest-scoring states at high precision under a per-layer, per-KV-head budget. Under exact restoration, we bound the excess risk of score-based anchor selection relative to the optimum at the same anchor budget, where risk is the conditional mean square of the first-order loss change. With a budget of 56 additional FP16 anchors per layer and KV head, CALFA-KV (d8b8) outperforms all evaluated nominal 1-bit baselines on the mean score across seven benchmarks for each of the three models. At the same anchor budget, CALFA-KV (d8b10) uses a nominal index rate of 1.25 bits per channel and narrows the gap to BF16 to 0.90--2.01 points on the same metric.

---


### 114. [TimeHF 2.0: Multimodal, Multivariate, and Multi-Region Collaborative Forecasting for Large-Scale Retail Supply Chains](https://arxiv.org/abs/2611.10521)

**<font color=#1a73e8>作者：</font>** Zhongxuan Han, Zhengxin Shi, Kunxiu Chen 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale retail supply chains need sales forecasts for specified products, future dates or planning windows, and regions under the conditions available at the forecast origin. Regional sparsity, changing environments, volatile sales, and unfamiliar business situations make these dimensions difficult to model together. We introduce TimeHF 2.0, a multimodal, multivariate, and multi-region collaborative forecasting framework that makes flexibly expressed business knowledge usable in numerical prediction. A coverage-aware directed encoder integrates regional sales and applicable covariates. A semantic alignment module transfers language-model hidden representations of natural-language plans and domain experience into target-specific forecasting context. Learning against sales observations connects these meanings to numerical evidence, allowing business users to supply experience, future plans, and changing circumstances without defining a new numerical feature for each description. Text-conditioned future queries and shared/routed experts adapt prediction to the supplied context. An ordered-distribution head allocates fine resolution to routine fluctuations and coarse resolution to extreme sales movements, while daily/window learning connects forecasts to cumulative planning quantities. Online parallel forecasting at JD yields relative accuracy improvements of 18.25% and 17.94% for national daily and planning-window sales, and 19.44% and 18.99% for DC daily and planning-window sales, over the original production deep learning baseline. Component comparisons, loss-design results, and product-type analyses examine the roles of regional information, covariates, business knowledge, context-dependent processing, and robust planning-oriented learning.

---


### 115. [In Search of Lost Time: Temporal Competence in Large Language Models](https://arxiv.org/abs/2611.10536)

**<font color=#1a73e8>作者：</font>** Ryan Liu, David Lee, Icey Siyi Ai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Today's large language models (LLMs) increasingly interact with time: AI agents schedule tasks, coordinate with people and other AI systems, and even decide how long to think. Yet LLMs only ever encounter time secondhand---in descriptions rather than experience. Does this hinder their reasoning and decisions that involve time? Our paper traces this question from a model's knowledge to its actions through four successive evaluations. We find that models know the rules of time, which can be read, but struggle to predict durations, which must be lived; while they are highly accurate (92.0-97.5\%) on a collection of questions built from the theorems of various time-related literatures, they underestimate their own completion times by up to 99.5\% and fail to identify which tasks will take them longer to run. And while they are better at estimating durations of human tasks, their duration judgments change based on how an event is worded, magnifying similar human biases by up to 1.3$\times$. Moving from estimation to action, we find that some LLMs disregard time costs completely when answering user queries, ignoring a 1,200-fold increase in wait time entirely. Together, our experiments reveal new challenges posed to LLMs as they navigate a dimension they cannot directly perceive, and highlight how their blind spots can even be simple cognitive abilities that humans take for granted.

---


### 116. [AFVE-Bench: Measuring Abandoned-Frame Verbalization Errors in Multi-Turn LLM Revision](https://arxiv.org/abs/2611.10541)

**<font color=#1a73e8>作者：</font>** Jiaming Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn revision often asks a model to replace an earlier organizing frame while preserving still-valid facts and artifact requirements. Existing instruction-following evaluations mainly assess the latest target and may therefore score an artifact as successful even when it adopts the new frame but exposes the superseded one. We call this failure an abandoned-frame verbalization error (AFVE). AFVE-Bench evaluates silent frame replacement in English and Chinese using 192 matched four-turn dialogues across eight writing domains. Each seed has zero, one, or two pre-target user requests to generate under the source frame. AFVE eligibility depends on the user-request history and applies to the one- and two-request conditions; the zero-request condition serves as a frame-bearing baseline. Eleven model configurations yielded 4,224 expected post-target response units. Two annotators independently scored 4,204 scorable responses for target adoption, source-frame verbalization, and direct usability; model and condition metadata were hidden, and disagreements were adjudicated. AFVE occurs in 25.54% (715/2,799) of history-conditioned responses. Of 2,388 target-passing history-conditioned responses, 472 (19.77%) still expose the abandoned source frame, most often through contrastive framing (423/472). For these standalone revision tasks, target adoption does not ensure source-frame silence.

---


### 117. [Seeing Isn't Enough: Unlocking Visual Reasoning by Bridging the Reasoning-Access Gap with TIGER](https://arxiv.org/abs/2611.10552)

**<font color=#1a73e8>作者：</font>** Gregory Kang Ruey Lau, Minh Huynh Nguyen, Bryan Kian Hsiang Low  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) inherit strong textual reasoning capabilities from their language backbones and text pretraining, but often fail to apply the same level of competency to visual inputs. We show that this degradation cannot be attributed to only perception failures, by evaluating models on semantically-equivalent text and rendered-text image inputs: models can accurately read text in the images and recover near-text performance when provided their own transcriptions, but just cannot reason well on the images directly. We characterize this discrepancy as a modality reasoning-access gap, where models fail to route perceived visual content into existing reasoning machinery accessible with text. To bridge this, we propose TIGER (Text-to-Image Gap-targeted training for Enhanced Reasoning), which first mines synthetic modality counterfactuals where a model succeeds on a text problem but fails when provided the corresponding rendered image, and post-trains the model on the image input via Group Relative Policy Optimization (GRPO), along with SFT and DPO variants. Importantly, although trained exclusively on synthetic rendered-text images with no multimodal annotations, TIGER results in model performance improvements across diverse real-world visual benchmarks including geometric diagrams (MathVerse), multi-disciplinary sciences (EMMA, MMMU), complex charts (ChartQAPro), and embodied spatial reasoning (RoboSpatial-Home). TIGER also complements existing state-of-the-art RLVR visual reasoning methods, yielding further performance gains. Analysis involving reasoning-subspace activation and activation patching provide support indicating that TIGER helps to align visual-to-reasoning pathways toward text reasoning states. Our implementation is available at this https URL.

---


### 118. [YRC-Bench: Benchmarking Culturally Aware Machine Translation for Historical Heritage via Tri-Level Semantic Bridging](https://arxiv.org/abs/2611.10555)

**<font color=#1a73e8>作者：</font>** Huang Yan, Aobo Li, Jiayi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translating historical cultural heritage poses profound challenges for machine translation systems due to the acute semantic asymmetry across eras and cultures, where terse classical syntax frequently obscures domain-specific cultural knowledge. While Large Language Models have demonstrated remarkable prowess in generic translation benchmarks, they struggle to negotiate Culturally-Specific Items and diachronic shifts in domain-rich historical texts, such as Yellow River cultural records. To bridge this critical gap, we introduce YRC-Bench, the first human-curated, multi-parallel benchmark dedicated to historical heritage translation across Classical Chinese, Modern Chinese, and nine target foreign languages. YRC-Bench establishes a tri-level parallel corpus incorporating modern explanatory glosses as explicit semantic bridges and operationalizes translation strategies through paired conserved versus substituted CSI variants categorized by cultural translatability. Systematic evaluations of nine leading LLMs across bidirectional translation directions reveal that leveraging modern Chinese glosses - especially human-curated ones - dramatically elevates both lexical fidelity and semantic adequacy. Furthermore, multidimensional human preference audits by native experts unveil distinct cross-cultural preferences between Sinographic-tradition and non-Sinographic language groups.

---


### 119. [onóna: Twin Embeddings with Tied Unembeddings](https://arxiv.org/abs/2611.10556)

**<font color=#1a73e8>作者：</font>** Cheng Luo, Xinnan Dai, Zhongzhu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Weight tying reduces the parameter cost of language models, but the usual tied output head is limited to a single softmax. We introduce onóna, a two-table parameterization that increases output expressiveness while preserving input-output weight sharing. The Transformer takes the average of two embedding tables as input, and the output head combines the softmax distributions defined by those same tables. A gate conditioned only on the current input token determines the mixture weight. Its values can be precomputed for inference, and the Transformer body remains unchanged. We evaluate onóna across Dense, Gated DeltaNet hybrid, mixture-of-experts, and Attention Residual architectures at 142M, 330M, and 1B scales. Under matched token budgets, onóna lowers final validation loss and external perplexity in 11 of 12 comparisons and raises the average accuracy over eight downstream tasks in 10 of 12. The one exception on loss is the 1B MoE model. The cost is one extra embedding table and one extra vocabulary projection.

---


### 120. [CompositionEvidence: Controlling Geometric Evidence for Cinematic Composition Reasoning with Frozen Vision-Language Models](https://arxiv.org/abs/2611.10559)

**<font color=#1a73e8>作者：</font>** Yichen He, Xin Huang, Yuxi Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cinematic composition questions depend on in-frame geometry that vision-language models (VLMs) use inconsistently. External perception tools can expose this geometry, but naive prompt injection can overwrite useful visual predictions. On ShotBench composition, pre-question geometry reduces Qwen2.5-VL-7B from 49.5% to 46.3%; corrupted measurements lower it to 33.6%. CompositionEvidence derives nine reproducible features from frozen detection, depth, and line experts and supplies their shared 24-dimensional representation through two interfaces. A training-free channel appends gated neutral evidence after the question, reaching 56.2% (+6.7, exact McNemar p=0.0018) and 48.4% under corrupted evidence. A minimal-training channel maps the same representation to four soft tokens with a 7.37M-parameter projector while leaving the VLM frozen; it reaches 61.0% (+11.5). Across nine VLMs, including five commercial models queried through official provider APIs, zero-shot accuracy ranges from 43.8% to 63.0%, and the text channel changes it by +6.7 to -6.9 points; the highest baseline is among the regressions. The effect of explicit geometry depends on measurement reliability and on how the receiving model integrates it.

---


### 121. [Large Language Models without QK-Normalization](https://arxiv.org/abs/2611.10560)

**<font color=#1a73e8>作者：</font>** Yongding Tao, Yitong Qiao, Tianqi Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Query-Key Normalization (QK-Norm) is widely adopted in modern large language models to control the growth of attention logits and improve training stability. However, query and key norms are not merely sources of instability. The query norm controls the sharpness of the attention distribution, while the key norm determines how strongly a token attracts different queries. These norms therefore carry token-specific information about attention selectivity and token importance. By normalizing both, QK-Norm suppresses this information. This raises a natural question: can we control query-key representations without discarding their sensitivity to magnitude? To address this question, we propose QK-MAP, a Magnitude-Aware Projection for constructing queries and keys. Rather than removing magnitude through normalization, QK-MAP transforms the input representation using multiple learnable frequencies, so that changes in magnitude are encoded as bounded phase patterns. This allows magnitude to be represented through phase and direction rather than vector length alone. Its periodic features have a fixed norm while remaining sensitive to magnitude changes, separating magnitude encoding from norm growth. Multiple frequencies further help distinguish magnitudes and reduce periodic ambiguity. Experiments across model scales from 190M to 7B parameters show that QK-MAP achieves lower training and validation loss than both Standard attention and QK-Norm. Further analyses show that QK-MAP preserves sensitivity to input scale, assigns less attention to the first token, and produces stronger attention contrast for relevant evidence in synthetic long-context tests. These results demonstrate that query-key scale can be effectively controlled without sacrificing token-specific magnitude information.

---


### 122. [ROLECUE: Diagnosing Cross-Lingual Role-Binding Failures in Vision-Language Models](https://arxiv.org/abs/2611.10575)

**<font color=#1a73e8>作者：</font>** Niaz Mohaiman Abtahi, Evan Maksud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can recognize events in images and parse sentences, but it remains unclear when they bind visual Agent-Patient structure to linguistic semantic roles across languages whose role cues depend on morphology, word order or construction. We introduce ROLECUE, a controlled diagnostic that pairs 192 validated two-person action images with German, Turkish, Japanese, English, Korean and Bangla sentences in canonical and patient-first orders. The evaluation separates image-only role recognition, text-only role parsing, direct image-sentence matching, response-compliance behavior and an external modular composition of the model's own component predictions. Across eight recent open-weight VLMs, ROLECUE reveals a structured spectrum: some models fail visual or linguistic component tests, some largely solve the diagnostic, some collapse to constant semantic assent and several show component-joint gaps in which reliable image-only and text-only role predictions do not survive direct joint inference. The largest non-degenerate gaps reach 44.9 percentage points, with final bootstrap intervals confirming that the effect is not a point-estimate artifact. These results reveal multilingual component-joint performance gaps and acceptance biases hidden by aggregate VLM benchmarks and show why component diagnostics are necessary before interpreting joint multimodal errors.

---


### 123. [Global Context Guidance for Diffusion Large Language Models](https://arxiv.org/abs/2611.10577)

**<font color=#1a73e8>作者：</font>** Jeimin Jeon, Bumsub Ham  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (LLMs) have recently emerged as a promising alternative to autoregressive LLMs, enabling parallel generation through iterative denoising. Recent guidance methods improve diffusion LLMs by introducing a weak model to guide the prediction of the base model during denoising. However, the influence of the weak model during denoising remains less clear, and computing its prediction requires an additional forward pass at each denoising step. We present in this paper an in-depth analysis of how diffusion LLMs use contextual information during denoising. Our analysis reveals that diffusion LLMs rely more heavily on local context while often underutilizing global context. Based on this observation, we introduce Global Context Guidance (GCG), a feature-space guidance method that enhances global-context utilization without constructing an explicit weak model. Extensive experiments on LLaDA-8B, Dream-7B, and LLaDA-1.5 across diverse benchmarks demonstrate that GCG consistently outperforms existing guidance methods, while incurring much lower inference overhead.

---


### 124. [EgoVeil: Personalized Privacy Reasoning for Egocentric Video](https://arxiv.org/abs/2611.10578)

**<font color=#1a73e8>作者：</font>** Xue Wang, Yang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) enable AI systems to interpret egocentric video. Yet continuous visual capture raises privacy concerns because sensitive content is pervasive and varies across users and contexts. We present EgoVeil, a personalized privacy reasoning system that determines which visual content to obscure based on individual preferences while retaining context useful for downstream assistance. It converts localized visual regions into structured semantic observations and combines a privacy reasoner with an explicit user-specific memory for personalized privacy reasoning. This design supports personalization and continual adaptation as preference evidence accumulates. We evaluate on in-the-wild data from 10 smart-glasses users under a cross-user chronological protocol. EgoVeil achieves 91.93% balanced accuracy and 84.42% Mask recall, outperforming direct VLM baselines and other controlled privacy reasoning baselines. Our results show that personalized, adaptive privacy reasoning better aligns privacy preservation with individual preferences while retaining the visual context needed for effective smart-glasses assistance.

---


### 125. [M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading](https://arxiv.org/abs/2611.10586)

**<font color=#1a73e8>作者：</font>** Jiashun Wang, Beile Wang, Guangyan Gan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency perpetual futures form a large-scale online financial market in which automated agents manage interacting asset positions under changing conditions. Policies relying solely on micro-level numerical states may overlook cross-asset relationships and become vulnerable to regime shifts, while macro-level linguistic judgments alone cannot ensure precise measurement or optimize positions under trading costs and risk constraints. Connecting market interpretation to coordinated multi-asset decisions remains challenging. We propose M3FT, a micro-macro-micro framework for multi-agent perpetual futures trading. The first micro stage constructs time-aligned numerical states from exchange and account observations through deterministic processing. The macro stage transforms these measured states into explicit market interpretations without adding external market information. Four asset-specific teams, each comprising a Market Interpreter, an Asset Communicator, and a Risk Reviewer, refine these interpretations through experience retrieval, cross-asset communication, and review of joint-position risks. The final micro stage combines encoded linguistic representations with the original numerical states to learn continuous target positions. We implement this framework with a language-conditioned multi-agent policy: asset actors use global and private numerical states together with linguistic context, while centralized critics evaluate joint actions using portfolio-wide information and shared-account rewards. Experiments on real cryptocurrency perpetual futures data, including comparisons across language models and policy-learning algorithms and component ablations, show that the best-performing M3FT configuration achieves a higher mean test return than the evaluated direct LLM, numerical RL, and rule-based baselines.

---


### 126. [MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification](https://arxiv.org/abs/2611.10592)

**<font color=#1a73e8>作者：</font>** Jiaju Ma, Ashvini Kumar Jindal, Chuhua Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models can generate motion graphics from static images and natural language requests, but it remains difficult to evaluate how well models can follow requests that combine spatial, appearance, and temporal requirements. We introduce MotionGraphicsBench, an expert-curated benchmark of 100 instances for animating an input static SVG with a motion edit prompt. By supplying all required visual elements, our editing task reflects a designer-like workflow and isolates motion generation from graphic generation. Derived from real-world Lottie motion designs, our benchmark contains diverse combinations of spatio-temporal animation behaviors. Each benchmark instance pairs its model input with a deterministic, human-readable verification program that accepts different valid implementations and reports which prompt requirements pass or fail, rather than comparing against a reference animation or using a VLM judge. We construct these programs with a multi-agent pipeline using human-labeled animations and synthesized test cases. On a balanced test set of 180 animations, our programs achieve 93.3% raw agreement with human judgments, compared with 83.3% for a GPT-6 Astra VLM baseline, and outperform the baseline in both approval and rejection recall. Across 47 configurations from 32 LLMs and 12 providers, pass@1 ranges from 6.0% to 67.7%. Across 15 models evaluated at their highest available reasoning effort with 32 attempts per instance, additional attempts improve every model, but pass@32 still ranges from 38.0% to 95.0%. Our analysis of verification programs reveals that generated animations often fail to match reference poses, follow requested motion trajectories, or coordinate related events. We release our benchmark at this https URL.

---


### 127. [The RenAIssance: Caption-Guided Diffusion Models for Historical-Art Visual Media](https://arxiv.org/abs/2611.10599)

**<font color=#1a73e8>作者：</font>** Zhanyu Tuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative AI can expand cultural collections into prompt-responsive visual media, but historical artworks rarely provide the paired descriptions needed to adapt modern image generators. We present The RenAIssance, a scalable pipeline that turns a collection of historical European artworks into a reusable text-to-image media resource. The pipeline generates scene-level captions with BLIP and uses the resulting approximately 15,000 image--text pairs from DEArt to train a compact LoRA adapter for Stable Diffusion v1.5. The adapter shifts generated images toward the historical-art distribution while retaining the base model's ability to render novel concepts. On historical and contemporary prompts of different lengths, it improves FID to the DEArt reference distribution in every setting with only a modest decrease in CLIP text--image similarity. Qualitative results show that the same adapter can render both period-appropriate subjects and contemporary concepts in a coherent historical visual language. By decoupling a reusable style representation from the base generator, the approach offers a practical building block for controllable historical-art media creation, interactive authoring, and rich-media experiences.

---


### 128. [InfoOrgBench: Can Agents Turn Scattered Information into Coherent Hierarchies?](https://arxiv.org/abs/2611.10600)

**<font color=#1a73e8>作者：</font>** Justice Ou, Lanming Ma, Zijian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When agents organize records into folders, they may correctly group the excerpts of a design proposal yet place the proposal under the wrong owning group. Existing agent benchmarks do not directly measure such higher-level errors. We introduce InfoOrgBench, a benchmark of 150 tasks in which agents organize scattered records from meeting recaps, issue threads and design proposals into hierarchies. Integrity checks verify that every record is preserved, and a Structure Score measures agreement with the source hierarchy at every level, independent of folder names and order. We evaluate 45 systems that pair nine models with five agent harnesses. The best system scores 83.2 out of 100, but no system exceeds 78 on meeting recaps or issue threads. Model choice affects scores far more than harness choice: model means span about 27 points, whereas the average effect of each harness is below one point. More importantly, parent-level relations have higher error rates than leaf-level relations in all three domains. In design proposals, nearly half of the outputs analyzed by level make exactly this kind of error. These results show that evaluating information organization requires measuring higher-level relations separately from record preservation and local grouping.

---


### 129. [AI in the Clinical Documentation Loop: Effects of LLM-Induced Note Bloat and Diagnostic Overcall on Downstream LLMs](https://arxiv.org/abs/2611.10601)

**<font color=#1a73e8>作者：</font>** Jinghui Liu, Anthony Nguyen, Taylan Gurgenci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to process medical records for healthcare tasks such as clinical documentation. Because these tools also generate documentation, the relationship is now bidirectional: models both read from and write to the record. Understanding how LLMs behave when reading records that already contain LLM-authored content is therefore critical for their safe deployment. In this study, we examine how LLM-authored content in the medical record affects downstream LLMs that read the same record. We consider two types of LLM-induced artifacts: bloat, in which LLM-generated summaries accumulate in the record and change the length and provenance of its content over time; and distortion, in which LLMs subtly alter clinical findings rather than fabricating facts outright. As a case of distortion, we study diagnostic overcall (documenting an unconfirmed differential diagnosis in the record) and test whether it propagates to the reader LLM's output. Across seven reader models from four families, we find evidence of both effects. First, LLM-generated summary notes modestly but consistently degraded downstream hospital-course generation compared with copy-forward and templated text of matched length. Second, injected overcalls reappeared in downstream outputs at rates that varied by reader model, without detectable changes in standard quality metrics. These findings show the need to monitor AI-generated content in medical records and to account for it when those records are later processed by AI.

---


### 130. [An LLM-Orchestrated Multi-Modal Chatbot for Tomato Disease Consultant](https://arxiv.org/abs/2611.10608)

**<font color=#1a73e8>作者：</font>** Ngoc-Son Le, Khanh-Nghi Phan, Ngoc Hong Tran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a chatbot developed to assist in diagnosing common diseases in tomato plants through natural language interaction. Users can describe symptoms in text. Then, the chatbot responds with the most likely disease, and basic treatment suggestions and related image-based reasoning. The system leverages pre-trained Mistral and Llama 3.2 large language models. The system is also built using LangChain and Streamlit to provide a lightweight and offline-friendly interface. This work targets to support tomato growers a fast and accessible tomato plant health guidance when the technical expertise is not available nearby, especially in the remote areas. The experimental results are promising and encourage further improvement of the chatbot for future real-world deployment.

---


### 131. [Reason First, Retrieve What Matters: Hypothesis-Guided Keyframe Selection for Long Video Understanding](https://arxiv.org/abs/2611.10609)

**<font color=#1a73e8>作者：</font>** Yisong Hu, Junbo Wang, Yuke Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding requires models to identify and reason over sparse, temporally distributed evidence within limited frame budgets. Existing keyframe selection methods typically retrieve query-relevant frames from a densely sampled candidate set before inference. However, global image-text matching incurs unnecessary computation when a small set of uniformly sampled frames already provides sufficient evidence. Query relevance alone may also overlook evidence that distinguishes competing answers, while one-shot selection offers no opportunity to correct earlier selection errors. We propose HypoKFS, a training-free, plug-and-play framework that couples keyframe selection with iterative inference by multimodal large language models (MLLMs). HypoKFS first reasons over sparsely sampled frames to construct an initial hypothesis space. The resulting answer distribution determines whether additional frame selection is needed. When needed, the retained hypotheses guide the selection of discriminative frames, followed by renewed inference and hypothesis refinement. This iterative process directs additional visual computation toward unresolved hypotheses while avoiding unnecessary global frame matching. Experiments on Video-MME, LongVideoBench, and MLVU demonstrate consistent improvements across multiple MLLM backbones. HypoKFS improves accuracy by up to 6.7 percentage points and achieves 72.9% accuracy on Video-MME at only 1.3% of the reference frame-hypothesis matching cost.

---


### 132. [Efficient LLM Adaptation with Forward-Only Passes](https://arxiv.org/abs/2611.10610)

**<font color=#1a73e8>作者：</font>** Baichuan Huang, Ananth Balashankar, Amir Aminifar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference serving is undergoing rapid growth and large-scale deployment, motivating us to rethink how the inference process itself can be leveraged to enable efficient task-specific LLM adaptation. In this paper, we propose a forward-only approach for efficient LLM adaptation with forward-only passes in LLM inference serving. We exploit the angle concentration of activations induced by each singular value decomposition (SVD) component to measure its contribution-dispersed or concentrated-to the angle concentration of the hidden states. Based on this, our forward-only search then efficiently identifies the weight matrix with the highest dispersion that merits rank reduction. We then selectively remove the higher-order components and retain the lower-order components in SVD. Empirical results across diverse datasets demonstrate the competitive accuracy of our forward-only approach, while theoretical analysis shows lower peak memory and greater speedup than the gradient-based approach and greater speedup than the exhaustive search approach. The experiments further present the robustness and generalization of our forward-only approach to various LLMs with up to 57B parameters. The code is included in the supplementary material.

---


### 133. [Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed](https://arxiv.org/abs/2611.10611)

**<font color=#1a73e8>作者：</font>** Peixu Xin, Runchuan Feng, Jiazhen Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reproducible evaluation, verifiable inference and on-policy reinforcement learning (RL) need an LLM engine to give a request the same output bits whichever requests share its batch. Batch-invariant kernels exist, but engines still select each kernel and its parameters from the batch. Two kernels that compute the same sum can round it differently. The engines' deterministic modes remove the choice by keeping one conservative kernel per operator and pay for it in latency. Many fast kernels are batch-invariant by themselves, so it is enough to fix the few batch-dependent values that kernel selection reads. Detent expresses kernel selection as a program that the engine executes. It finds the fewest values in this program that must be fixed and tunes them for the workload before deployment. On multi-GPU deployments of Llama-3.1-70B and Qwen3-30B-A3B in vLLM and SGLang, Detent is batch-invariant. Tuned per load, it serves at 1.04-1.17x the latency per output token of Stock (each engine with its standard settings), against 1.67-10.3x for the deterministic modes. In SGLang it matches the GSM8K accuracy of SGLang's deterministic mode. Detent covers multiple deployment combinations, including multiple engines, GPU generations, tensor-parallel degrees, and dense and MoE models. Seeded RL rollouts of models up to Llama-3.1-70B replay bit for bit under other batches and cache splits. A trainer on Detent's kernels and values matches every rollout logprob bit for bit at 1.03x Stock's rollout time per token. BF16 GRPO then stays stable where Stock's run collapses.

---


### 134. [An Agentic Multi-Agent Framework for System Log Anomaly Detection](https://arxiv.org/abs/2611.10612)

**<font color=#1a73e8>作者：</font>** Ngoc-Son Le, Huy-Hoang Mac Nguyen, Ngoc Hong Tran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As enterprise systems grow in scale and complexity, manual log analysis and conventional SIEM tools struggle to keep pace with the volume and diversity of incidents. To address this challenge, this paper proposed a multi-agent AI framework supporting in analyzing the system log to trace the attack forensic in the system more effectively and efficiently. The framework is designed using n8n platform and Gemini large language model. The framework consists of 7 AI agent layers. Each agent work on a specific task. When the task is done, the agent will forward the result to the output-associated agent of the next layer. The multi agent model improves the analysis velocity, so it is able to support numerous log analysis requirement at the same time. We deployed 16 test cases to test operation of the multi agent workflow, and evaluate the accuracy per test case and the operative performance. The result findings are very promising.

---


### 135. [What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors](https://arxiv.org/abs/2611.10620)

**<font color=#1a73e8>作者：</font>** Mainul Hasan Mohsin, Mohammad Shahidur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation probes look like near-perfect monitors for secret collusion among large language model (LLM) agents. We show that they mostly detect that an agent was told to collude, not that it decided to. Our benchmark (2,500 committee and 1,476 code-review episodes) adds agents who receive the collusion instruction and refuse it, separating instruction from decision. Published detectors barely tell colluders from these refusers, and our best probe separates them mostly by reading the instruction: without it, agent AUROC falls from 1.00 to 0.61. Two further pitfalls inflate reported results: scored after the vote, a rule that only reads the votes reaches AUROC 0.990 but finds nothing before it; and in 57% of attempts no colluder argues for the target in public. The decision is still there: a probe trained on agents' own choices reads it (AUROC 0.73 without the instruction), and probes find colluders whose goal was fine-tuned into the weights (AUROC 0.995; pre-registered). We turn the controls into a protocol for testing any collusion monitor, and adapt scan statistics into an online monitor for groups of any size.

---


### 136. [EndoSCOP-V: A Multi-Turn Video Understanding Evaluation Framework for Multimodal Models in Endoscopy Reporting and Clinical Reasoning](https://arxiv.org/abs/2611.10626)

**<font color=#1a73e8>作者：</font>** Abhishek Tyagi, Tanmay Jain, Vilas Biradar 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endoscopic diagnosis unfolds over native video, where a single positive finding during traversal of the gastrointestinal tract sets off a multi-minute chain of reasoning over location, morphology, severity and intervention. Existing endoscopy multimodal benchmarks test only static images or single-disease videos, which miss the temporal and clinical reasoning that real-world reporting demands. We introduce EndoSCOP-V, a video-grounded multi-turn evaluation framework for structured endoscopy reporting and clinical reasoning. It contains 1,307 real-world endoscopy and colonoscopy videos (63.2 h; 97% 1080p) averaging about 174 s. Its 20,274 question-answer turns are instantiated deterministically from clinician-filled structured endoscopy-reporting EHRs, so no per-case annotation is synthetic or LLM-rephrased. They come from 1,033 clinician-reviewed templates, about 18 per disease, that span a clinically aligned 9-task x 30-sub-task reporting taxonomy over 54 World Endoscopy Organization (WEO) MST 3.0 diseases. 22% of procedures carry co-existing pathologies, up to six per case. A Markovian context-pruned oracle-forcing protocol evaluates the dialogue turn by turn, injecting the gold answer before each subsequent turn so that per-turn reasoning is isolated from cascading dialogue errors. A panel of 15 board-certified endoscopists sets a 78% strict-accuracy baseline on 1,500 questions. Across 14 open-weight LMMs, the best 27B-class model reaches 59.8% strict accuracy, falling to 53.4% once format-trivial disease-rejection items are excluded. On a between-subjects spot-check, the best of 3 frontier proprietary models trails the clinician panel by 23 pp on strict NDR accuracy. Sub-task analysis reveals consistent gaps in quantitative measurement, multi-variable grading and intervention reasoning on long-horizon video. Data: Hugging Face (EndoSCOP-V). Code: GitHub (abhi25t/EndoSCOP-V).

---


### 137. [Towards Identity-Preserving LLM Agents under Model Transition](https://arxiv.org/abs/2611.10628)

**<font color=#1a73e8>作者：</font>** Yihuang Kang, Pei-Cing Huang, Chan-Tung Ku 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM agent's backend model is upgraded or replaced, operators typically reload the same persona, memory, and rules onto the new model and assume the agent will behave as before. We show this assumption requires empirical validation-and that whether identity is preserved depends on the specific model pairing. Across 5,760 compliance-testing runs in 12 regulated domains with three open-weight models, we find that some transitions produce significant behavioral drift while others do not, even when the agent's external state remains identical. Crucially, this drift is invisible to verbal verification: every model claims full policy compliance, yet actual decisions under pressure differ across models. The same external state can reorder which model is most compliant-a large positive effect on one substrate, negligible on the other two. Practitioners should treat model transitions as behavioral changes requiring action-level empirical testing, not as transparent infrastructure operations.

---


### 138. [DFT-Agent Bench: Scaffold Effects and Execution Provenance in Autonomous DFT](https://arxiv.org/abs/2611.10629)

**<font color=#1a73e8>作者：</font>** Shijie Liu, Jin Yang, Weilin Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as autonomous agents for first-principles materials simulation. We report empirical findings from DFT-Agent Bench, a benchmark of 200+ Quantum ESPRESSO tasks spanning relaxation, electronic structure, equation-of-state, and elastic-tensor pipelines over multiple material tiers. Each task carries a QE-derived ground truth with public-reference cross-checks where available, and a provenance audit checks whether the required QE execution contract was met. Under one execution harness, we compare a near-bare ReAct baseline with a bundled v5.1 scaffold on two models. The complete scaffold improves bands+DOS by +0.08/+0.11 and d-electron vc-relax by +0.17 on both models, while high-scoring relaxation and equation-of-state cells leave little room for improvement. The elastic result is model-dependent (0.18 to 0.40 for deepseek-v4-pro and 0.62 to 0.59 for claude-opus-4-8). A fixed 100-task analysis with retrieval disabled supports the aggregate pattern: the fully frozen DeepSeek comparison gains +0.17, while the Opus comparison gains +0.10 against a historical pool baseline (p < 0.001). The provenance gate catches incomplete or unmarked executions that can receive high rubric scores; it is an execution-contract check, not a test for intentional fraud. These results characterize the evaluated DFT workflows. The anonymous review artifact contains the frozen diagnostic slice, prompts, scorer, and solver revisions: this https URL.

---


### 139. [Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding](https://arxiv.org/abs/2611.10634)

**<font color=#1a73e8>作者：</font>** Yan-Cheng Li, Chun-Yi Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention accelerates long-context decoding by reading a subset of the KV cache, but existing methods are open-loop: the kernel commits to its selection with no signal indicating whether enough attention mass was preserved and no recovery path when it was not. The needed signal already exists inside the kernel. The fraction of softmax mass on the selected tokens, which we call coverage, satisfies an exact algebraic equality with per-step output error and serves a dual role as the acceptance criterion and the interpolation weight for recovery. Coverage-Verified Sparse Attention (CVSA) turns coverage into a training-free, closed-loop verify-then-correct decode loop that accepts high-coverage drafts and recovers only the heads that fall short, with no sampling, no draft model, and no speculative-decoding infrastructure. Quality varies by only $0.14$ points across the threshold sweep; budget and scheduling ablations characterize the deployed operating point. On LongBench at 7B and 70B, CVSA comes within $1.13$ points of dense attention, statistically matching it at 70B, and it loses $0.8$ points on RULER; measured median decode-step speedup reaches $6.21\times$ at 128K context.

---


### 140. [VisProve: Learning Typed Visual Provenance for Scientific Document Question Answering](https://arxiv.org/abs/2611.10642)

**<font color=#1a73e8>作者：</font>** Jingxuan Wei, Zhengyang Wang, Zheng Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual citations show where an answer is supported, but not how the cited content contributes to it. In scientific document question answering, a model may read a value directly, compress several observations, or combine evidence to infer a conclusion. We study typed visual provenance, where a system generates an answer together with source regions and explicit support relations. We introduce ReViE, a dataset of 3,941 questions over complete scientific documents, with page, section, and region annotations labeled as Quotation, Compression, or Inference. We further propose VisProve, which augments joint answer and provenance generation with differentiable Spatial Evidence Reading and Evidence-Answer Relation Feedback. VisProve conditions next-token prediction on localized visual evidence and its estimated support relation through a gated norm-bounded residual. On the document-disjoint ReViE test set, VisProve improves Typed-F1 from 3.52 to 5.48 and Section-F1 from 45.99 to 53.24 over joint supervised fine-tuning with the same backbone, while Page-F1 changes only marginally. These results suggest that coupling visual grounding with support relation modeling mainly improves fine-grained provenance, while the low absolute Typed-F1 reveals a substantial gap between answer generation and precise visual evidence attribution.

---


### 141. [On the Geometric Bottlenecks of Cross-Lingual Knowledge Editing](https://arxiv.org/abs/2611.10646)

**<font color=#1a73e8>作者：</font>** Aastha A K Verma, Anwoy Chatterjee, Sparsh Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based autoregressive multilingual language models (LMs) are often assumed to store factual knowledge in an interlingua: a language-agnostic latent space. If this assumption holds, a parameter update applied in a source language during knowledge editing should inherently propagate to its semantic equivalents in target languages. However, empirical benchmarks show that cross-lingual propagation of edits often degrades substantially, a degradation that prior work treats largely as an algorithmic symptom rather than a structural bottleneck. In this work, we investigate whether representational anisotropy creates a structural bottleneck for source-only associative-memory editing, and perform a geometric dissection of the cross-lingual propagation gap. Using associative memory-based "locate-then-edit" methods, including ROME, MEMIT, and AlphaEdit, as analytical frameworks, we derive a closed-form decomposition of this gap into key-space propagation, parallel residual mismatch, and orthogonal residual mismatch. Our empirical findings show that cross-lingual propagation is primarily bottlenecked by a large orthogonal residual component, indicating that source-language edits often fail to span the target-language update directions required for successful transfer. Furthermore, we show that post-hoc correction using only source-language residual statistics encounters a large residual-prediction barrier. Finally, we perform a structural realignment via a targeted contrastive alignment objective and find that it substantially improves key-space propagation and partially improves cross-lingual edit transfer, while leaving value-space mismatch as a remaining bottleneck.

---


### 142. [MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://arxiv.org/abs/2611.10649)

**<font color=#1a73e8>作者：</font>** Lorenz K. Muller, Philippe Bich, Chiara Boretti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that treats every linear layer independently. MACaQ applies a per-channel scale and a block-Hadamard transform online to each layer's activations, while absorbing the corresponding inverse transforms into its weights. Retaining these transforms online avoids cross-layer dependencies and enables a simple streaming implementation of the quantization process, in which only one layer must reside in memory at a time. To improve over round-to-nearest quantization, we introduce Flip-Refinement, a Hessian-aware coordinate-descent procedure that greedily moves individual FP4 codes to adjacent representable values. Despite executing the activation transforms at inference time, MACaQ adds only 2.3% end-to-end overhead over pure MXFP4 on Qwen3-32B in vLLM. MACaQ reaches lower perplexity than DuQuant++ and MR-GPTQ, and already matches their best perplexity on Llama-3-8B in 11 times less quantization time. We further apply MACaQ without architecture-specific modifications to an image diffusion model, illustrating the generality of its layer-local design and show quantization of a 122B parameter model in 64 minutes, using only 32.5GB GPU RAM.

---


### 143. [MMGraph-Agent: Agentic Multimodal RAG via Cache-Inspired Multimodal Knowledge HyperGraphs](https://arxiv.org/abs/2611.10657)

**<font color=#1a73e8>作者：</font>** Haoran Luo, Ziyue Zhu, Shangyang Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driven by increasingly complex real-world applications, Retrieval-Augmented Generation (RAG) has evolved from textual pipelines to multimodal settings, comprising two complementary dimensions: knowledge organization and retrieval enhancement. However, existing methods still face challenges of high construction cost, context window limitations, and the lack of unified training across offline and online knowledge sources. To address these challenges, we propose MMGraph-Agent, a unified multimodal RAG framework based on cache-inspired multimodal knowledge hypergraphs. MMGraph-Agent enables extremely lightweight hypergraph construction with zero API cost and dynamic memory-based retrieval that alleviates long-context issues. Experiments across offline, online, and joint retrieval settings demonstrate consistent improvements in performance, efficiency, and architectural unification. Our software and data are publicly available at this https URL.

---


### 144. [RankShift: Evaluating Ranking Instability Across Benchmark Dimensions in Document Parsing](https://arxiv.org/abs/2611.10679)

**<font color=#1a73e8>作者：</font>** Halimat Afolabi, Daeyoung Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document parsing benchmarks are often treated as stable measures of model quality, yet rankings may depend substantially on benchmark design choices. In this work, we present RankShift, a systematic study comparing OCR and vision-language models (VLMs) under controlled variation in dataset composition, matching strategy, and scoring methodology. Using OmniDocBench as a case study, we evaluate the ranking stability of 16 models across 3 dataset configurations, 6 matching strategies, and 3 scoring metrics. We quantify rank stability using pairwise rank correlation, top-k churn, and pairwise reversal rate. Our results show that the interaction between matching strategy and ground truth format is a substantial but understudied driver of instability: scoring against OmniDocBench's JSON annotations versus its Markdown rendering yields a mean Kendall's tau of approximately 0.33 under region-level matching strategies, with individual pairs as low as tau = 0.23, compared with tau = 0.77 when each page is scored as a single concatenated string. Dataset composition produces comparable instability across page-type strata (mean tau = 0.48) and layout-type strata (mean tau = 0.49), while the cross-dataset shift from OmniDocBench to Real5's Scanning reconstruction of the same pages is more stable (tau = 0.80). Metric choice is the most stable dimension, with mean tau of approximately 0.78 across NED, BLEU, and METEOR. These findings indicate that leaderboard position is not solely a property of model capability, motivating leaderboards that report not only headline scores but also the robustness of rankings across reasonable design choices.

---


### 145. [TransMem: Transition-Aware Retrieval for Evolving Personal Memory](https://arxiv.org/abs/2611.10683)

**<font color=#1a73e8>作者：</font>** Shigeng Chen, Linhao Luo, Changlong Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term personalized agents are increasingly expected to answer queries over user histories in which preferences, goals, and constraints evolve across interleaved conversations. Existing retrieval-based and structured-memory systems can surface relevant facts, but often return isolated memory units that do not explain which earlier preference was refined, contradicted, or superseded by later evidence. We introduce TransMem, a transition-aware memory retrieval framework that stores preference updates as explicit retrieval units alongside ordinary factual memories. During memory construction, TransMem routes user interaction history into topic-structured memory graphs, detects shift events, and grounds them as transition records. At inference time, TransMem first retrieves factual anchors and then adaptively expands over transition records, producing a compact context of factual anchors and accepted transition records. Experiments on PersonaMem and PersonaBench across two Qwen backbones show that TransMem outperforms representative retrieval-based and structured-memory baselines. Controlled analyses further show that transition records and adaptive expansion contribute beyond factual anchoring, chronological expansion, flat transition retrieval, and fixed-hop traversal. These results suggest that preference-update records are useful retrieval units for long-term personalization.

---


### 146. [Audit Before You Merge: Provenance, Probing, and Continual LoRA Composition](https://arxiv.org/abs/2611.10684)

**<font color=#1a73e8>作者：</font>** Lenny Aharon, Neta Glazer, Lior Aharon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-hoc merging of public LoRA adapters is an attractive gradient-free path to continual adaptation, but reliable measurement of catastrophic forgetting in this setting depends on infrastructure that prior work has not addressed. We treat each adapter merge as a sequential task in a continual-learning setting, with the instruction-tuned base model's capabilities as Task 0, and study forgetting on Llama-3.1-8B-Instruct. Public adapter hubs contain modules that fail basic provenance checks: silent base-version mismatches and near-zero delta norms whose inclusion inflates measured interference by ~10pp. We propose a two-check audit (base-model match, non-trivial delta norm) and a leakage-free probing protocol as preconditions for any forgetting study in this setting. On an audited 4-adapter set, naive merging causes -10.5pp on GSM8K and -18.3pp on HumanEval, while Task Arithmetic at lambda=0.5 sits within a standard error of the unmerged baseline. A coordinate search including negative coefficients identifies the math adapter as probe-optimal at lambda=-0.5, outside the reach of positive-only mergers, suggesting forgetting has structure that negation-aware merging may exploit. The same protocol replicates on Mistral-7B-Instruct-v0.3, where 2 of 4 candidate adapters fail the audit and the audited merge reproduces the same merge-method ranking on GSM8K, supporting that our findings are not Llama-specific.

---


### 147. [Perception, Not Reasoning, Limits Visual Theory of Mind](https://arxiv.org/abs/2611.10694)

**<font color=#1a73e8>作者：</font>** Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models pass text-based false-belief probes at near-human levels but drop by over twenty percentage points on abstract panels the moment the same problem is conveyed visually. The consensus diagnosis is conceptual, prescribing new belief-reasoning modules. We argue the dominant bottleneck is perceptual: not what the model cannot reason about, but what it cannot see. We propose a five-condition dissociation protocol that holds the reasoning task constant while varying perceptual fidelity from visual only to text only, and quantify the result with the Perceptual Contribution Ratio, the share of the visual-to-text gap a given fidelity closes. We test this on two kinds of scenes: abstract 2D panels in the Heider--Simmel tradition, and naturalistic 3D game scenes from MuMA-ToM and MindPower. The evaluation covers seven VLMs and roughly 159,000 API calls. Ground-truth scaffolds substantially close the gap in every setting, and on the abstract panels and MuMA-ToM they match or exceed the text-only reasoning. Whereas scaffolds built by automatic parsers, including frontier VLMs, fail. The most common error in the visual-only condition is \emph{reality bias}, which accounts for 60\% of false-belief failures. Models report where an object actually is, not where an absent agent believes it is. This points to a perceptual front-end that fails to track which agents were present at each moment. Under the evaluated protocol, structured visual scene-state extraction, rather than belief inference, is the dominant bottleneck for visual ToM.

---


### 148. [Hallucination-Guided Unlearning: Using Hallucination Traces to Reveal Overfitted Memories](https://arxiv.org/abs/2611.10697)

**<font color=#1a73e8>作者：</font>** Jiayu Zhang, Ziqi Zhong, Yuliang Gai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Selective unlearning is increasingly important for the safety and compliance of large language models. Harmful or memorized content is often entangled with useful knowledge and difficult to enumerate. We use the model's own failures to identify candidates for unlearning. We propose Hallucination-Guided Unlearning (HGU), which uses hallucinations as diagnostic signals. HGU localizes unsupported spans via evidence and internal consensus, traces a sparse set of high-responsibility MLP neurons, and edits them with compact gates under a utility-preserving KL constraint. On TOFU, HGU achieves the best MU-FE trade-off, with Avg scores of 0.7221 (forget05) and 0.7699 (forget10), and the highest SepS H-Avg (0.4382/0.4715) under mixed forget/retain prompts. On the WMDP auxiliary task, HGU yields the strongest forgetting (e.g., 14.2 on Economics) while improving Retain (52.7) and MMLU (57.2). These results suggest that tracing hallucinations enables targeted, post-hoc unlearning that better balances forgetting efficacy and general utility without full retraining.

---


### 149. [AbductionBench: Benchmarking Abductive Reasoning in Large Language Models](https://arxiv.org/abs/2611.10705)

**<font color=#1a73e8>作者：</font>** Moein Salimi, Amir Qeysarbeigi, Babak Hosseini Mohtasham 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abductive reasoning is the inference of plausible explanations for observed evidence. Evaluating this capability requires more than a single task: a system may need to generate an explanation, discriminate among competing hypotheses, revise its hypotheses as evidence arrives, or decide what evidence to seek next. Yet these capabilities are typically evaluated through isolated benchmarks with different task formulations and scoring procedures, so claims that a model is ``good at abduction'' may reflect only a narrow aspect of this capability. We introduce AbductionBench, a unified framework whose taxonomy characterizes abductive tasks. We instantiate this framework on 27 datasets spanning ten domains and evaluate eight LLMs from four model families evaluated on single-choice selection tasks. Beyond harmonizing heterogeneous tasks, AbductionBench separates final-answer evaluation from analysis of the observable reasoning traces and interaction histories produced alongside those answers. We analyze written traces as observable model outputs rather than faithful representations of internal computation, characterizing evidence use, hypothesis comparison, uncertainty, contradiction handling, and answer commitment. Jev matches or exceeds small LLMs when selecting among explanations over compact evidence but falls substantially behind on longer cases, suggesting that candidate discrimination and extended evidence integration place different demands on a system. In interactive tasks, the proportion of actions judged relevant declines at later steps, and a relevant first question is associated with a correct final answer; in the passive task, models rarely revise their initial hypothesis as new evidence arrives. Together, these findings highlight the value of evaluating abductive reasoning through both final answers and observable evidence use, hypothesis revision, and information gathering.

---


### 150. [No Second Run: Does RSI Stop at Frontier Pre-training?](https://arxiv.org/abs/2611.10719)

**<font color=#1a73e8>作者：</font>** Xiaojie Cai, Jiayi Chen, Junwei Chen 等 59 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-training is where every foundation model begins; bringing recursive self-improvement (RSI) there would let AI improve the process that creates AI. Yet public RSI work has so far targeted only post-training, which starts from an existing base model, runs trials costing GPU-hours, and returns verifiable scores. Pre-training breaks all three conditions at orders-of-magnitude higher cost: a run consumes hundreds of thousands of GPU-hours over months and cannot be repeated; its objective, post-training headroom, cannot be read off any single score; and what must improve is not a model but the whole production system, from data pipelines and training infrastructure to the teams that run them. To our knowledge, we are the first to apply RSI to an entire frontier pre-training run from scratch and to report it in detail. RSI does not stop at frontier pre-training, but it changes form: since no end-to-end loop can close over a single unrepeatable run, we decompose it into smaller loops that can, each repairing a step the full run breaks. The result is 801-30B-A3B-Base, a 30B-A3B MoE trained from scratch on 11.8T tokens in three months by a newly formed team. We release it as a base model; the lightweight SFT reported here (6B tokens, no RL) only probes post-training headroom. As a base model, 801-30B-A3B outperforms Qwen3-30B-A3B and Nemotron-3.5-Lightning-30B-A3B, trailing only the larger Qwen3.5-35B-A3B, and keeps this position under identical SFT; with lightweight SFT alone, it achieves the highest average on four agentic benchmarks against fully post-trained models, including Qwen3.6-35B-A3B. Since post-training RSI presupposes a strong base model, bringing RSI into pre-training acts on the foundation every later stage builds on. We open-source 801-30B-A3B-Base and the lightweight SFT data at this https URL .

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
