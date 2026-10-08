# 🧠 大模型相关研究 | 2026年10月09日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 101. [The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs](https://arxiv.org/abs/2610.09384)

**<font color=#1a73e8>作者：</font>** Jiachen Zhao, Zhengxuan Wu, David Bau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are routinely fine-tuned under a fixed context, such as a generic system prompt, persona or domain-specific instruction, yet the learned behavior sometimes stays confined to that context and sometimes broadly generalizes to unseen contexts. We propose the Persona Hierarchy Model to explain this: a shared default persona influences behavior across contexts. Under this model, fine-tuning that modifies the shared persona promotes broader transfer, whereas changes to local personas remain more context-specific. Across 120 fine-tuned models spanning four behaviors and 15 training contexts, generalization narrowness positively correlates with the similarity between the training context's persona and the default persona (Pearson's r = 0.72 for Qwen3-4B). Prior fine-tuning under the default context can broaden generalization in subsequent training under other contexts. Aligning contextual responses with default-persona responses produces stronger effects. Finally, we propose persona-preserving regularization (PPR) to confine undesired contextual generalization. In RL, PPR cuts reward hacking from 42-55% to at most 0.2% under every evaluated prompt while retaining accuracy gains. These results support the Persona Hierarchy Model as an explanation for contextual generalization and can motivate future controls on unintended generalization for better alignment of LLMs.

---


### 102. [Quantifying Volumetric Risk: Class-Aware Asymmetric Weighted Conformal Prediction for 3D Medical Image Segmentation](https://arxiv.org/abs/2610.09392)

**<font color=#1a73e8>作者：</font>** Shadi Alijani, Fereshteh Aghaee Meibodi, Homayoun Najjaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable volumetric segmentation is critical for clinical diagnostics, yet foundation models such as MedSAM remain deterministic and lack calibrated uncertainty under distribution shift. Existing conformal prediction methods offer statistical guarantees but are frequently applied in 2D and assume symmetric error distributions, so they do not capture the class-specific biases that arise in 3D multi-class segmentation. We propose Class-Aware Asymmetric Weighted Conformal Prediction (CA-WCP), which combines latent-space density-ratio weighting for covariate shift with directional quantiles for the lower and upper volume bounds, and scales each bound by a class-specific asymmetry factor derived from validation-set false-positive and false-negative rates. We prove that CA-WCP retains the weighted-exchangeability marginal coverage guarantee for every class, and we evaluate it on 3D brain tumor segmentation (BraTS 2020) and on a synthetic multi-organ CT benchmark constructed under covariate shift. On both benchmarks the 95\% Clopper--Pearson interval for the observed coverage of CA-WCP contains the nominal 90\% level for every semantic class, while interval width is reduced by 8--14\% relative to symmetric weighted conformal prediction. We further encode the calibrated intervals into structured prompts for a multimodal large language model to produce uncertainty-conditioned radiology reports, linking distribution-shift-aware uncertainty quantification to interpretable clinical communication.

---


### 103. [ARCS: Towards Precise Text-to-SQL via Structured Disambiguation](https://arxiv.org/abs/2610.09396)

**<font color=#1a73e8>作者：</font>** Yihao Hu, Yanlin Feng, Naoki Otani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As text-to-SQL systems move beyond demonstrations toward real-world deployment, ambiguity in user questions becomes a primary source of errors. Such ambiguities are often subtle, domain- or data-specific, and can silently cause system outputs to deviate from the user's true intent. Ambiguity is traditionally addressed through conversational clarification, which is often inefficient, cognitively demanding, and poorly aligned with real-world user workflows. We propose structured disambiguation, a new paradigm in which ambiguity is resolved through explicit, constrained interactions rather than free-form dialogue. We construct ARCS (Ambiguity Resolution Corpus for SQL), the first text-to-SQL benchmark featuring naturally occurring, unconstrained ambiguities over real-world databases, with complete annotations of all valid ambiguity points, interpretations, and SQL queries. Experimental results show that text-to-SQL remains challenging in the presence of ambiguity: gpt-6-sol achieves only 51% end-to-end execution accuracy, and no open-source model exceeds 27%.

---


### 104. [TutorLoop: Regulating Student Learning Behaviors via Sensor-in-the-Loop Generative Feedback](https://arxiv.org/abs/2610.09400)

**<font color=#1a73e8>作者：</font>** Songlin Xu, Xinyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present TutorLoop, a sensor-in-the-loop system that regulates student learning behaviors by delivering adaptive feedback based on real-time cognitive states. Unlike prior large language model (LLM) tutors that directly depend on scenario-specific content, TutorLoop operates on sensor-derived signals captured via webcams. Moreover, unlike direct cognitive-to-feedback mappings that are short-sighted, the system employs a deep reinforcement learning (DRL) agent to optimize the feedback type across the entire learning process. Finally, another LLM tutor refines feedback into human-like, context-aware messages. We evaluate TutorLoop in a large-scale user study (N=187), where a model trained offline is directly applied to a new learning task without retraining. Results show that TutorLoop provides less frequent yet more effective interventions, improving attention, reducing workload, increasing engagement, and ultimately enhancing learning outcomes. These findings highlight the potential of closed-loop, sensor-driven feedback for scalable human-AI integrated systems to support learning.

---


### 105. [Let the Library Speak: Self-Advertised Method Selection for Formal Proving](https://arxiv.org/abs/2610.09401)

**<font color=#1a73e8>作者：</font>** Xiaopeng Yuan, Suijin Wang, Yanli Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based formal provers can retrieve relevant lemmas and prior proofs, but relevance alone does not say whether a mathematical method can be used on the current theorem. A method has prerequisites, a target, an intended action, and obligations that its use leaves to prove. Methods that look equally related to a theorem may therefore differ substantially in whether they offer a plausible next step. We formulate this as an applicability-aware method-selection problem and introduce self-advertisement: before candidates are ranked, a model generates a problem-specific proposal for each one, stating what part of the goal it targets, what action it would take, and what conditions that action requires. We organize 82 reusable methods from Putnam 2000-2014 as Method Contracts, which pair applicability descriptions with Mathlib anchors, a checked example or scaffold, and expected proof obligations. A single batched call elicits proposals across the library; vague or unsupported proposals are demoted, yielding a ranked shortlist accompanied by inspectable claims about each candidate's use. We analyze when similarity-based representations cannot distinguish methods with different applicability, how errors in applicability estimates affect shortlist quality, and what a checked scaffold guarantees under its stated assumptions. Against lexical, embedding, and embedding-plus-LLM reranking baselines, self-advertisement achieves 95.0% hit@5 on Putnam 2015-2025, compared with 84.2% for the strongest reranker. On IMO ProofBench, it achieves 91.7% compared with 88.3%. These results indicate improved coverage of annotated methods in the retrieved shortlists, particularly on Putnam.

---


### 106. [TiTok: Audio-Visual LLM for Multi-Segment Temporal Grounding](https://arxiv.org/abs/2610.09408)

**<font color=#1a73e8>作者：</font>** Eunji Shin, Dahyun Choi, Seungyeon Jo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual multi-segment grounding (AV-MSG) in untrimmed videos, reasoning over audio-visual evidence and predicting multiple segments for a query, is a fundamental problem but remains challenging. Visual-only models overlook complementary acoustic cues, while audio-visual models often fail to calibrate the number of events - a phenomenon we refer to as count miscalibration. We present TiTok, an audio-visual large language model (AV-LLM) that localizes an arbitrary number of temporal event segments for each query. For precise boundary prediction, we introduce the Time Token Interleaving (TTI) method, which explicitly injects special time tokens into the audio-visual stream to align input-side temporal perception with output-side temporal prediction. We further propose decoupled, multi-segment-oriented rewards for reinforcement learning, consisting of global, local, count, precision, and format rewards, optimized with Group reward-Decoupled Normalization Policy Optimization (GDPO). To assess the performance on AV-MSG, we establish a new UnAV-100-based evaluation protocol, and propose the CountF1 metric for quantifying count miscalibration that overlap metrics fail to capture. TiTok reaches 65.7 mIoU and 0.58 CountF1, achieving state-of-the-art performance. Our code is available at this link.

---


### 107. [Stability and Diversity of Networked Self-Consuming Generative Ecosystems](https://arxiv.org/abs/2610.09409)

**<font color=#1a73e8>作者：</font>** Xiukun Wei, Yang Zhang, Xueru Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widespread deployment of generative AI has made it increasingly difficult to distinguish synthetic content from real data. Consequently, synthetic data is inevitably incorporated into the training pipelines of future model generations, forming a self-consuming training loop. Prior work has studied the effects of such recursive self-consuming training, but analyses have largely been limited to isolated models, where a model consumes only its own synthetic data, or to simplified interactions between two models. This paper takes a first step toward understanding networked self-consuming generative models, in which multiple models consume synthetic data generated by one another through complex interaction pathways. We introduce a theoretical framework representing models as nodes in a directed, weighted graph, with edge weights governing the flow of synthetic data among models. Using this framework, we analyze the long-term behavior of networked models under retraining dynamics, establishing conditions for convergence and characterizing the resulting fixed points. We further investigate how the system's long-term stability and diversity are shaped by each model's access to real data, cross-model data consumption, and the structure of the interaction graph.

---


### 108. [Efficient Reasoning with Flow Language Models](https://arxiv.org/abs/2610.09416)

**<font color=#1a73e8>作者：</font>** Hanru Bai, Faissal Izermine, Oscar Davis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow Language Models (FLMs) have emerged as a continuous-state alternative to discrete diffusion language models, yet the role of their continuous representations in reasoning remains unclear. We investigate this question by comparing the reasoning efficiency of FLMs and discrete diffusion models, measured by solution accuracy under matched denoising steps. Unlike discrete diffusion, which passes categorical states between denoising steps, FLMs evolve a continuous sequence representation throughout denoising and decodes it into discrete tokens only at the end. Our theoretical analysis shows, from a superposition perspective, how information retained in these continuous states can benefit reasoning. Intermediate-state interventions provide further empirical support for this theoretical account, showing that removing information about alternative candidates reduces subsequent solution recovery. Together, these findings show that FLMs allow evidence for multiple candidates to persist and inform subsequent reasoning before a discrete answer is produced. Furthermore, our experiments on maze planning and Sudoku tasks show that FLMs achieve greater reasoning efficiency in the few-step regime: FLMs achieves higher sequence accuracy than discrete diffusion baselines at matched model sizes and small denoising steps. On maze planning tasks, FLMs can also achieve comparable accuracy with smaller models. For example, on Maze15, FLM reaches the 95\% accuracy target at 64 denoising steps with 36.5\% fewer parameters than MDLM. These findings point to continuous state spaces as a promising foundation for reasoning models that require fewer refinement steps.

---


### 109. [Spatial Latent Reasoning for Embodied Reference Understanding](https://arxiv.org/abs/2610.09418)

**<font color=#1a73e8>作者：</font>** Ling Li, Jianhui Zhong, Wei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pointing-gesture visual grounding requires connecting hand geometry with the visual identity and extent of a referred object. A central challenge for continuous latent reasoning is how to organize these complementary cues into useful intermediate supervision. We propose Spatial Latent Reasoning (SLR), a framework that structures this supervision around an ordered sequence of geometric and visual states. A spatial ray state is supervised by fingertip position and pointing direction, followed by four states aligned with target-region features. To construct the visual targets, we introduce parity pooling, which applies polyphase grouping to average region tokens on four interleaved spatial supports. All states are generated recurrently during training and inference; auxiliary annotations are required only during training. On EgoPoint-Ground, the framework improves mIoU over same-backbone supervised fine-tuning by 2.8, 17.5, and 21.1 percentage points on Qwen3.5-4B, Qwen2.5-VL-7B, and Qwen3-VL-8B, respectively, with improvements on both hard subsets. On YouRefIt, it achieves 77.6% precision at IoU 0.5, a numerical margin of 5.2 percentage points over the reported state of the art under differing evaluation protocols. Ablations support joint geometric and visual supervision on the standard and similar-object sets, and favor parity over three alternative pooling operators on the standard set. These results support task-structured supervision for continuous pointing grounding. We will release the code and supporting materials.

---


### 110. [SkillCycle: Co-Evolving Agent Policies and Skill Banks](https://arxiv.org/abs/2610.09430)

**<font color=#1a73e8>作者：</font>** Ling Li, Qiuyu Shen, Zheng Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Internalizing external skills changes a language agent's capabilities and, with them, the value of its remaining guidance: rules can become redundant, misleading, or insufficient for newly encountered decisions. This creates a coupled problem of learning from skills and adapting the skills that supervise further learning. We introduce SkillCycle, a framework for co-evolving agent policies and skill banks through a feedback loop between skill internalization and rule revision. Our central contribution is to give distillation feedback a second role: token-level contextual differences help locate rules for inspection, while interaction outcomes guide edits to their content and applicability. SkillCycle alternates between two phases: policy learning with a fixed skill bank and router, and rule revision with a frozen policy. Candidate edits undergo rule-level and whole-bank environment comparisons before they guide the next learning cycle. On WebShop, SkillCycle with a 3B model achieves a success rate of 74.74% and a score of 88.37 without inference-time skill inputs, representing relative improvements of 0.73% and 3.96% over the state-of-the-art (SOTA) model, respectively. In Cycle 3 ablations on ALFWorld and WebShop, SkillCycle's no-skill success rates improve by 10.18% and 18.11% relative to a static skill bank, and by 2.41% and 2.50% relative to a single bank update, respectively. These results show that continually revising skill guidance as the agent's capabilities change helps transform external skills into policy capabilities that require no skill inputs at inference. We will release code, configurations, skill banks, and evaluation protocols.

---


### 111. [Mixture of Layers: Dynamic Layer Routing for Visual Reasoning](https://arxiv.org/abs/2610.09440)

**<font color=#1a73e8>作者：</font>** Jeonghwan Kim, Sofia Stoica, Jiwan Chung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision encoders contain layer-wise visual representations that differ in spatial granularity, semantic abstraction, and sensitivity to local details. However, most Multimodal Large Language Models (MLLMs) rely on only the final or penultimate vision encoder representations or fixed aggregation rules, making visual abstraction largely query-agnostic and limiting access to fine-grained cues such as small objects, spatial details, text, and subtle visual attributes. In this work, we propose Mixture of Layers (MoL), an instruction-conditioned layer routing approach at the visual patch level that dynamically aggregates query-relevant latent representations from intermediate vision encoder layers. Given a text query, MoL predicts routing probabilities over vision encoder layers and performs a top-k sparse aggregation over selected hidden states at either the image level, patch level, or through a hybrid routing mechanism. In doing so, MoL enables query-adaptive access to layer-specific visual features for fine-grained visual reasoning. Our experiments across 7 fine-grained visual reasoning tasks demonstrate substantial performance improvements, especially across fine-grained visual grounding and understanding tasks such as +18.9% improvement on V* in overall accuracy, +4.5% on HRBench4K, and +16.3% on CharXiv compared to the baseline MLLMs, without resorting to multi-resolution inputs, simple interleaving of multiple vision encoders, or increasing the number of patch tokens. We study vision encoders' receptive field scales across different layers and their sampling behaviors to provide an in-depth analysis of why layer-wise sampling is helpful, demonstrating that conditional visual representations are a key step towards better visual perception and reasoning in MLLMs. Our project page is available at this https URL.

---


### 112. [Arctic Questions, Missing Answers: A Dataset and Benchmark for LLM Abstention in Arctic Science](https://arxiv.org/abs/2610.09446)

**<font color=#1a73e8>作者：</font>** Benjamin Wilcox, Dawei Gao, Pradeeban Kathiravelu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) should abstain from scientific multiple-choice questions when no option is valid, but frequent abstention alone does not demonstrate sensitivity to answer availability. We introduce ArcticQA, a dataset of 194 questions derived from primary Arctic research, with automated checks of answer support and distractor contradiction against source evidence. We further develop ArcticAbstain, a paired benchmark comparing answer-present and answer-absent conditions, with the correct answer replaced by a distractor in the latter and an explicit abstention option in both. We evaluate eight models from the Gemini, Claude, and ChatGPT families at high reasoning effort, with three trials per condition, yielding 9,312 recorded responses. Answer-present abstention rates range from 0.0% to 63.0%, whereas replacing the correct answer increases abstention by 5.05 percentage points on average. These findings highlight substantial baseline differences and the need to evaluate abstention frequency and responsiveness jointly. The dataset and benchmark are available at this https URL.

---


### 113. [Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning](https://arxiv.org/abs/2610.09450)

**<font color=#1a73e8>作者：</font>** Hanqiu Li Cai, Chema Garabito  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a $256\to512\to1024$ curriculum, after first ablating the prediction target and representation alignment at $256^2$ to decide what to scale. We also convert a pretrained latent model, FLUX.2 Klein base 4B, to pixel space. We fine-tune both families for monocular depth estimation and for image restoration/super-resolution. We find no significant improvement from using a pixel-space generative prior. Fine-tuned for depth with one matched direct-regression recipe, Iris-3B is level with the latent FLUX.2 Klein and the converted pixel FLUX.2 Klein falls behind it, and on $4\times$ DIV2K restoration neither pixel model beats a latent FLUX.2 Klein fine-tune, the converted one trailing it slightly. We document the recipes, the failure modes and the remaining confounds behind this negative result. Nevertheless, Iris-3B shows that pixel-space pretraining with the pixel-transformer (PiT) head of PixelDiT scales to 3B parameters and to text-to-image quality competitive with latent models, matching Qwen-Image on OneIG under the official evaluators at $1024^2$. We release its weights and training code in the hope that they help pave the way for further work on pixel-space generation.

---


### 114. [GeoPrior-Mamba: Structured Process Priors with Mamba for Fine-Resolution XCO2 Reconstruction](https://arxiv.org/abs/2610.09456)

**<font color=#1a73e8>作者：</font>** Zhao Meng, Yinan Cai, Siru Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing fine-resolution column-averaged dry-air CO2 (XCO2) fields from sparse satellite observations requires models to infer spatial structure that is only weakly constrained by direct measurements. Existing learning-based methods typically treat environmental covariates as ordinary numerical inputs and must therefore learn heterogeneous source-sink relationships largely from sparse supervision. We introduce GeoPrior-Mamba, a multi-directional Mamba framework augmented with offline language-model-induced structured process priors. Rather than using a language model to predict XCO2, we use it before training to organize relative process knowledge for biospheric uptake, ecosystem respiration, and anthropogenic emissions into deterministic prior tables. These priors are spatially instantiated using geographic, ecological, emission-related, and seasonal information and are adaptively injected into the reconstruction backbone through a lightweight knowledge adapter. Using OCO-2 observations from 2018-2020, GeoPrior-Mamba achieves an RMSE of 0.81 ppm and an R2 of 0.93 on held-out observations, reducing RMSE by 48.2% relative to CAMS background interpolation and by 3.1% relative to Trans-XCO2 under the same evaluation protocol. Ablation experiments show a measurable contribution from the knowledge-prior branch and substantially faster convergence than the knowledge-free Mamba backbone. Independent TCCON evaluation further supports the consistency of the reconstructed fields with ground-based column CO2 measurements. These results suggest that language models can provide a practical mechanism for constructing structured process priors when globally consistent process-response representations are difficult to obtain directly, while remaining outside the numerical prediction loop.

---


### 115. [Right Number, Wrong State? Measuring Cross-Jurisdiction Substitution in LLM Recall of State Policy](https://arxiv.org/abs/2610.09458)

**<font color=#1a73e8>作者：</font>** Jiayu Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When an LLM answers a state-specific policy question wrongly, it may be hallucinating, or it may be returning a real value that holds in another state. We test this with a minimal-set design: the question wording is fixed and only the jurisdiction varies, across the 50 U.S. states and the District of Columbia (51 jurisdictions) and three exactly defined Medicaid income-eligibility quantities. Gold values come from an official data book and agree with an independent source in 101 of 102 checked cells. Under a pre-registered protocol, Claude Sonnet 5.5 and GPT-5.6 Sol reproducibly give another state's current value, identical across two independent repeats, for 10 and 25 of 153 items. Attribution is fragile, however. Crediting any wrong answer that equals another state's value yields 3-5x more reproducible substitutions than checking every number in the asked state's own records, because many apparent cross-state answers are the asked state's own values under another convention or from an earlier year. Claims about cross-jurisdiction error need a complete same-state reference set. We will release the protocol, gold table, and all model outputs.

---


### 116. [LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy](https://arxiv.org/abs/2610.09466)

**<font color=#1a73e8>作者：</font>** Xiao Han, Aoyang Quan, Xiangyu Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) dispatch is beginning to move beyond isolated path planning and optimization-driven resource allocation toward system-level coordination supported by semantic reasoning and LLM-based interfaces. This survey provides a unified characterization of LLM-enabled UAV dispatch systems that bridges semantic intent, symbolic decision-making, and physical UAV execution. Rather than treating LLMs as standalone add-ons, we conceptualize them as a cross-layer semantic orchestration layer connecting human instructions, external solvers, and distributed control modules. We organize the literature into four representative dispatch paradigms: pipeline dispatch, global assignment dispatch, decentralized agentic dispatch, and divide-and-conquer dispatch. For each paradigm, we analyze its decision logic, system structure, control flow, representative methods, and potential LLM roles. We further examine how LLMs support semantic parsing, retrieval-grounded planning, solver orchestration, local agent reasoning, multi-agent coordination, safety assessment, and human-facing explanation. We discuss the implications of these paradigms for scalability, robustness, coordination burden, and verification requirements, and identify open challenges including latency-aware reasoning, grounding reliability, physical feasibility guarantees, edge deployment, privacy protection, and distributed consistency. This survey provides a system-level taxonomy and design perspective for integrating LLMs into safety-critical UAV dispatch systems.

---


### 117. [Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents](https://arxiv.org/abs/2610.09469)

**<font color=#1a73e8>作者：</font>** Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) perform tasks across applications (such as desktops, mobile apps, and web browsers) by observing graphical interfaces and issuing commands such as clicks and keystrokes. These interfaces combine trusted controls and content with untrusted content needed for legitimate tasks. An adversary controlling this untrusted content can embed instructions or misleading visual cues to change the agent's intended action or redirect its commands to the wrong interface target. We formalize security requirements for both the agent's decisions and their execution through GUI commands. In an ideal execution model, we show that enforcing both requirements at each step protects execution traces.
We instantiate this model in Secure-CUA, our system for secure CUA execution. Its key idea is to commit to an explicit per-action program, called an $\textit{action transaction}$, before accessing untrusted content. Each transaction fixes its queries to untrusted content and the permitted uses of their responses. The system masks untrusted regions and evaluates each transaction to produce the next action, using an isolated query model to answer its queries. It then locates the intended interface target using the masked interface. Under the model's assumptions, Secure-CUA is secure by design, while generating a new transaction at each step helps maintain high task utility by adapting to changing interfaces.
We evaluate Secure-CUA under benign conditions on 400 WebArena tasks using three frontier models across $5$ seeds, yielding $6,000$ execution traces. Secure-CUA achieves an average task success rate of $53.55\%$, compared with $55.12\%$ for Vanilla-CUA and $13.17\%$ for CaMeL-CUA.

---


### 118. [Before Bringing It Up: When and How AI Companions Should Use Memor](https://arxiv.org/abs/2610.09470)

**<font color=#1a73e8>作者：</font>** Zihan Guo, Roxy He, Junwei Quan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Memory can sustain AI companionship, yet even accurate recollection can be inappropriate to use. Two rounds of formative interviews with 14 users (n = 6 exploratory, n = 8 memory-focused) motivate asking what a companion should consider before using past information. Eight themes inform Reconsider, a single-call procedure with five checks and four handling modes, evaluated on 80 scenarios across five models over 400 blinded within-model pairs. Two LLM judges favored Reconsider by net margins of +15 and +23 percentage points, with bootstrap intervals excluding zero for three of five models but not for GPT or Claude. Evaluator analysis linked judge scoring differences to model family, and a preliminary matched-guidance control isolating memory-specific content gave positive margins. We contribute an interview-grounded design framework for memory use and an evaluation that scrutinizes its own evaluators.

---


### 119. [When Should an In-Context Learner Expand Its Hypothesis Space?](https://arxiv.org/abs/2610.09471)

**<font color=#1a73e8>作者：</font>** Weihan Li, Xinlei Chen, Junhao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning systems adapt quickly inside a familiar family of models. The harder step comes earlier: deciding, from observations that could be noise, an exception, a change within the family or structure outside it, whether opening a richer family is worth its cost. We treat this as a costly sequential decision: prediction failure must be turned into structural evidence, evidence into a value of expansion, and value into action. The Structural Revision Environment produces matched failures from each source, varies the price of expansion and the remaining horizon independently of the evidence, and admits exact Bayesian calculations and an exact normative solution of the one-shot decision. Its solution shows that revision is a value boundary and not an evidence threshold: one history has different optimal actions under different prices, horizons and announced queries, the boundary between local repair and expansion is set by the inputs a rule predicts and a repair cannot cover, and belief in the richer family crosses long before the decision does. Transformers trained in the environment reproduce this boundary from utility alone. Language models of three post-training lineages carry a failure-sensitive signal in their predictions that is not reflected in their revision decisions, and given the gain of expanding they read it without weighing it against price and horizon. Three models allowed to reason weigh the stated gain in the reference's proportions and still do not turn the history into an estimate of what expansion would buy. Controlled post-training of the meta-trained learners moves the prior and the sharpness of predictions, and neither moves the criterion.

---


### 120. [MIMESIS: Learning User Simulators as Training Environments for Interactive Agents](https://arxiv.org/abs/2610.09484)

**<font color=#1a73e8>作者：</font>** Hoang Phan, Dat Huynh, Andrey Zhmoginov 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training and evaluating interactive language agents typically requires rich user interactions, yet collecting human feedback is expensive and difficult to scale. Simulated users offer a scalable alternative, but they must both resemble real user behavior and provide useful learning experiences for agents. In contrast, most agent-training frameworks rely on off-the-shelf assistant LLMs, whose helpfulness can make them overly cooperative, explicit, and behaviorally homogeneous compared with real users. We introduce MIMESIS, a purpose-built user simulator trained on human conversations with explicit reasoning supervision and 13 realistic behavioral patterns derived from real user interactions. Empirically, our 9B model achieves a SOUL-Index of 65.7, surpassing the strongest frontier model. Compared with Claude-Opus-5, the strongest baseline on RealUserSim and SimulatorArena, MIMESIS improves behavioral fidelity by 13.4 points and reduces Turing distance by 3.6 points, respectively. We then freeze the simulator and train an agent by interacting with the frozen simulator using multi-turn reinforcement learning. Across eight environments, training with MIMESIS yields better agent performance than training with GPT-5.5 under all nine unseen user simulators, demonstrating stronger generalization to new user simulators. Moreover, we propose Coached On-Policy Self-Distillation (CSD), which leverages simulator-generated private reasoning traces and subsequent utterances as feedback on how well the agent addresses user needs. A coach converts this information into concise coaching notes that describe how the agent can better anticipate user needs and adapt its behavior over the course of an interaction. CSD turns this feedback into dense, token-level supervision beyond sparse task rewards, yielding further gains across all nine evaluation user models.

---


### 121. [Goldsmith: Gold-Loss-Guided Definition Optimization with an Agentic Annotation Harness](https://arxiv.org/abs/2610.09489)

**<font color=#1a73e8>作者：</font>** Yihan Li, Hanyi Zhang, Xiaoxi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many annotation projects begin before experts have a stable guideline or enough labels to train a task-specific model. We present Goldsmith, an agentic pipeline that turns a small gold set---expert-annotated calibration examples representing the intended task boundaries---into a reusable structured annotation definition. Goldsmith treats this definition as a trainable textual object. Candidate definitions are run on the same gold examples and scored with an executable structured loss, while the output schema, formatting, retrieval, repair, judging, and human review remain in an external harness. A large language model (LLM) editor converts the highest-loss failures into textual-gradient revisions, which are accepted only when the measured loss decreases. In prompt-optimization comparisons, Goldsmith improves over direct rewriting, OPRO, APE, and PromptBreeder under matched evaluation protocols. The resulting definition also improves downstream annotation when combined with retrieval, score-based routing, and human review across typed span, pair-level relation, and fixed-trigger event-argument tasks. These results show that scarce expert supervision can support both task-definition learning and scalable annotation.

---


### 122. [The Attribution Blind Spot: Layerwise Trajectory Diagnostics for Source Reliance in Retrieval-Augmented Language Models](https://arxiv.org/abs/2610.09493)

**<font color=#1a73e8>作者：</font>** Zhe Yu, Wenpeng Xing, Yunzhao Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A retrieval-augmented model can match a document without relying on it. Controlled knowledge conflicts make source choice observable and let us ask a second question that prediction alone cannot answer: which internal-state properties define useful intervention directions? We study paired hidden-state changes with Latent Trajectory Shift (LTS), a signed projection onto a training-fitted first principal component (PC1), and keep verified training exposure separate from behavioral source choice. Across the evaluated conflicts, state-change magnitude is often the stronger predictor, whereas signed PC1 is the stronger selective controller: equal-norm interventions change source preference while better preserving non-target behavior, and the frozen direction transfers across the tested datasets and aligned model pairs. A same-system OLMo study further combines positive choice and control results with inconclusive exposure detection at the achieved power. The central result is a separation: representations that diagnose what a model will choose need not be the representations that best control that choice.

---


### 123. [RT-DETR-World: Transferring Rich LLM Semantics to Real-Time Open-Vocabulary Detection](https://arxiv.org/abs/2610.09502)

**<font color=#1a73e8>作者：</font>** Yupeng Zhang, Ziyi Zhao, Juntao Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary detection (OVD) recognizes categories unseen during training through textual category queries, yet achieving strong generalization with real-time efficiency remains challenging. Beyond vocabulary scaling, zero-shot generalization may benefit from reusable visual--semantic cues learned from seen data, including attributes, actions, states, and contextual relations. Existing real-time OVD methods primarily emphasize vocabulary coverage and efficient region/query--text matching; under strict efficiency constraints, compact detectors may struggle to absorb rich instance semantics and scene context. We propose RT-DETR-World, a compact DETR-style detector that transfers the rich semantics conveyed by descriptions during training while retaining lightweight query--text matching at inference. We construct GroundingCapv2 with three levels of supervision: category names for standard OVD, object descriptions conveying instance-level semantics, and image descriptions conveying object relations and scene context. These descriptions serve only as training-time semantic supervision. To help the compact detector absorb these semantics, we propose Dual-Path Description Alignment (DDA), combining a deployment-consistent MiniLM pathway with a training-only LLM teacher. MiniLM provides query--category supervision and object-description alignment, while offline teacher features supervise matched queries and global visual representations at the object and image levels, respectively. All teacher features are precomputed, and the teacher-side modules are removed after training. We further propose Relation-Aware Negative Relaxation (RNR), which uses teacher-derived semantic similarities to relax related negatives while preserving exact positives. Experiments demonstrate competitive zero-shot accuracy and a favorable accuracy--efficiency trade-off. The code will be released.

---


### 124. [It Is Not Seeing the Hazard: A Frozen Vision-Language Safety Score Measures Its Caption Bank](https://arxiv.org/abs/2610.09517)

**<font color=#1a73e8>作者：</font>** Samuel Tetteh, Cody Fleming  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen vision-language models increasingly provide safety signals for reinforcement learning. Their use assumes that similarity to language describing danger indicates the hazard itself. Yet policy return and collision rate cannot reveal whether a score detects hazards or responds to correlated features of the scene. VLM-based methods have reported gains in driving and safe-RL benchmarks by converting image-text similarity into rewards, costs, or confidence weights. Such signals promise to reduce reliance on manually designed feedback. They may also reflect prompt structure, embedding geometry, or camera viewpoint, leaving their safety meaning unverified. To address this gap, we present a controlled evaluation of a frozen CLIP prompt-margin safety score. We apply the score to trajectories generated by policies that never receive it, match pre-contact observations to contact-free observations with comparable hazard geometry, and vary the captions, encoder, and camera view. Across three policies, 180 episodes, and 130 isolated contact onsets, the score decreases for about twenty steps before contact. Mechanism controls indicate that the score mainly tracks resemblance to the scene shared by its captions and changes with caption separation and camera view. A constant-confidence control retains the lower catastrophe-rate point estimate, so policy gains do not establish hazard perception.

---


### 125. [Visual Evidence Under Cross-Examination: Evaluating and Controlling Decision-Level Evidence Use in Vision-Language Models](https://arxiv.org/abs/2610.09550)

**<font color=#1a73e8>作者：</font>** Huiyao Zhang, Jin Bai, Zilong Su 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models increasingly reason through crops, regions, and tool-produced observations. Yet an observation can influence the answer without benefiting the candidate it supports. We study candidate-bound visual contribution: valid evidence should help, invalidating its supporting relation should remove its additional effect, and valid rebinding should redirect that effect to the newly supported candidate. We introduce CROSS-Bench, a benchmark of 28,000 decision problems, with matched invalidation and rebinding tests on a dedicated evaluation subset. Our RIVET interface preserves evidence identity and uncertainty, composes a candidate-conditioned response, and separately controls its strength. Shared-evidence experiments show that task accuracy and evidence ownership can diverge. Under matched capacity and training, RIVET increases normalized effect transfer from 0.512 to 0.651 where clean evidence has a positive effect. The advantage persists on common evaluation examples and across repeated decision-layer fits. With evidence predicted from raw inputs, RIVET improves CROSS-Bench accuracy by an average of 5.70 pp across four frozen backbones, relative to the same models without auxiliary evidence. These results separate the utility of visual evidence from the candidate-specific destination of its effect.

---


### 126. [MARS: Malware Analysis with Rule-Based Scoring of LLM Claims](https://arxiv.org/abs/2610.09553)

**<font color=#1a73e8>作者：</font>** Hyeongjun Choi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models can triage malware through direct verdicts or behavioral claims scored by an external policy. We present MARS, a malware triage framework, and compare direct classification with single-pass claim scoring using the same evidence collector and identical static evidence bundles for each model. The evaluation covers 1,195 PE and ELF binaries grouped into 1,001 near-duplicate clusters and six language models, with deterministic rules providing a baseline. Direct classification is more accurate for all six models. On samples with usable outputs from both paths, its accuracy advantage ranges from 3.7 to 20.9 percentage points, with all 95% cluster-bootstrap confidence intervals for the differences above zero. It also achieves higher malicious alert recall in ten of twelve platform and model combinations. Claim mediation provides no consistent reduction in performance variation across models. Separate subset studies find more consistent alert decisions for direct classification and a larger recall loss for the claim path when predefined indicator fields are removed. In a family identification probe, claims yield higher accuracy than verdict labels but lower accuracy than evidence text. Retained claims expose the inputs to verdict computation and permit policy revision without another model call. We reproduce archived verdicts exactly and apply a revised policy to the same records, including outputs from two additional models withdrawn by their provider. Under the evaluated claim taxonomy and additive policy, these results favor direct classification when only a verdict is required, while demonstrating that retained claims support explicit policy inspection and revision.

---


### 127. [Reliability of LLM Judges for Evaluating Entity Alignment](https://arxiv.org/abs/2610.09554)

**<font color=#1a73e8>作者：</font>** Vaibhava Lakshmi Ravideshik, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Entity Alignment (EA) identifies equivalent entities across knowledge graphs and is critical for knowledge base integration and ontology merging. Evaluating EA systems at scale requires expensive expert annotation, making systematic assessment across diverse domains practically infeasible. LLM-as-judge evaluation offers a potentially scalable alternative, yet its reliability for structured prediction tasks like EA remains unstudied. We present the first systematic benchmarking study across three frontier models, three datasets, and four EA systems, using perturbation bias diagnostics, meta-evaluation across all dataset-judge-prompt combinations, and counterfactual label-flip tests. We identify anchor bias, a failure mode in which judges invert discrimination when the system's decision label is visible. Label exposure causally collapses judge discrimination (J-ROC-AUC 0.12-0.87), while a label-free protocol recovers near-ceiling capability on distinctive-name datasets (0.93-1.00) and significant recovery on biomedical pairs (0.93-0.95). Counterfactual experiments confirm causality (FSR 53-99%) and reveal a frontier model paradox: stronger judges exhibit greater label sensitivity, not less. A blinded two-annotator human evaluation (102 pairs, Cohen's kappa=0.902) confirms this mechanism directly. We release the first biomedical EA benchmark (MeSH-SNOMED CT, 15K pairs) and a reproducible auditing framework for LLM judge reliability in EA. Code and data are available at this https URL.

---


### 128. [DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists](https://arxiv.org/abs/2610.09558)

**<font color=#1a73e8>作者：</font>** Samuel Margolis, Paul Schmiedmayer, Alan Huang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drug target discovery requires distinguishing molecules that causally drive disease from those that are merely associated with it. Training and evaluating AI agents to perform this workflow end-to-end is difficult because real world biobanks lack known causal ground truth and participant-level data is access controlled. We introduce DrugTargetWorld, a framework that procedurally generates simulated biobanks, or "worlds," with known but concealed causal structure. Each world contains genotypes, proteins, health records, outcomes, and synthetic magnetic resonance imaging (MRI) for 54,000 participants. Agents must construct a disease phenotype, identify causal driver proteins, infer the beneficial direction of modulation, and optionally conduct virtual 'wet lab' experiments. We evaluated nine agents in 540 episodes across 20 cardiovascular worlds and three experimental budgets. Opus 5 and GPT-5.6 Sol achieved the highest mean composite scores, 39.98 and 35.38 of 100, respectively, and both recovered 64% of causal drivers on average. However, no agent reliably distinguished misleading non-causal proteins, and performance remained limited by the integrative judgments required to connect phenotype construction, causal evidence, and intervention decisions. By making each world's causal structure known to the evaluator but hidden from the agent, DrugTargetWorld turns end-to-end drug target discovery into a scalable training and evaluation problem with verifiable reward.

---


### 129. [World Potential Model: Pretrained World Knowledge as Progress Potentials](https://arxiv.org/abs/2610.09560)

**<font color=#1a73e8>作者：</font>** Jun Zhao, Jixin Tang, Yang Shu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents often receive supervision only from terminal task outcomes, leaving little signal for distinguishing productive intermediate behavior from stagnation or even regression. Rather than learning a separate value function or process reward model for every task, we ask whether pretrained models can recognize task progress from their existing world knowledge. We formalize this capability with a World Potential Model (WPM), a goal-conditioned evaluator of task-relative realized progress in agent contexts. In ALFWorld and ScienceWorld, off-the-shelf pretrained models substantially outperform chance at recovering realized-progress structure without task-specific evaluator fine-tuning. We further anchor these progress judgments to task-specific milestones to obtain scalar world potentials, whose temporal differences provide process-sensitive step-level credit for policy optimization. Under matched comparisons, WPM-guided optimization improves success over outcome-only GRPO across all evaluated configurations. Together, these results provide initial evidence that pretrained world knowledge can support reusable realized-progress evaluation and provide useful supervision for long-horizon agents.

---


### 130. [EvoSignal: LLM-Guided Evolutionary Design of Modular Traffic Signal Control Programs](https://arxiv.org/abs/2610.09563)

**<font color=#1a73e8>作者：</font>** Leizhen Wang, Peibo Duan, Zhenlin Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective traffic signal control (TSC) requires policies that respond to changing traffic demand and network conditions while meeting different control objectives. However, adapting existing strategies often involves repeated manual design and adjustment, making it difficult to systematically explore better control rules for a target network. Large language models (LLMs) can automate this process, but directly using them to select signal phases leaves decision rules embedded in black-box models and incurs recurring inference costs and latency. This paper formulates TSC as a modular program design problem and proposes EvoSignal, an LLM-guided evolutionary framework using traffic knowledge and performance feedback. The modular representation separates traffic feature extraction, local phase prioritization, and optional network-based priority adjustment. Starting from several established strategies, EvoSignal improves programs through feedback on congestion and signal operation, retaining strategies with different performance trade-offs. The resulting programs operate without online LLM inference. Simulation experiments across five scenarios on two real-world road networks show that the selected default EvoSignal program reduces waiting time by 16.8--49.2\% relative to the lowest waiting time achieved by the 20 conventional, reinforcement learning-based, and LLM-based baselines in each scenario. A program prioritizing travel time and queue length outperforms all 20 baselines on all three metrics in the search scenario and remains among the top three on each metric when transferred unchanged to the other four scenarios. These findings support automated design of inspectable control programs that transfer across the evaluated road networks and traffic this http URL is available at this https URL.

---


### 131. [RELATE: An Evaluation Framework for measuring Relational Orientation of Large Language Models](https://arxiv.org/abs/2610.09569)

**<font color=#1a73e8>作者：</font>** Shivam Shukla, Jihye Kim, Shubham Gaur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for emotional support, raising concern that sustained use may draw users away from their real-world relationships. Yet existing evaluations primarily focus on the safety, empathy, or helpfulness of responses, leaving under-examined a relational question: where does the model orient the user for continued support? To address this question, we introduce relational orientation, a property operationalized through two non-exclusive dimensions: inward-facing (IF) language, which positions the AI as the user's ongoing source of support, and outward-scaffolding (OS) language, which encourages real-world human connection. Grounded in psychological and sociological literature, we formalize a taxonomy of relational orientation and present RELATE, a persona-conditioned framework for measuring inward-facing and outward-scaffolding language at the sentence level in multi-turn dialogues. RELATE pairs 76 help-seeking situations adapted from naturally occurring questions with three simulated user styles, providing 228 evaluation stimuli. In our experiments, we evaluate seven LLMs using dialogues with six assistant turns each, yielding 1,596 dialogues and 69,194 assistant sentences. We assess these sentences using a primary rubric-based LLM judge and apply a secondary judge to a subset. Under automated evaluation, we find that the proportion of sentences labeled as IF is higher at the sixth assistant turn than at the first, while the proportion labeled as OS is substantially lower for hesitant, indirect simulated users than for explicit, reassurance-seeking users. RELATE provides a reproducible framework and a sentence-level signal for auditing and steering the relational orientation of supportive LLMs.

---


### 132. [How Do LLMs Change Predictions Under Negation?](https://arxiv.org/abs/2610.09571)

**<font color=#1a73e8>作者：</font>** Jongwook Yoon, Jongwon Lim, Sungjib Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negation is an essential feature of human language, yet large language models (LLMs) remain unreliable in processing it. We evaluate recent open-source and closed-source LLMs on our negation benchmark and find that, in 37-71% of cases, they repeat the same answer under negation (e.g., "Madrid" for "What is not the capital of Spain?"). To understand and address this brittleness, we mechanistically examine how models operate under negation. Our main finding is that specialized attention heads and MLP neurons jointly implement negation by (1) suppressing retrieval of the original answer (e.g., "Madrid") while (2) promoting a favored candidate within the answer category (e.g., "Paris"). This contrasts with accounts of human negation processing, in which information about the original answer helps to determine what should be excluded. Furthermore, we find that this difference from human processing is a key source of negation failures: the model's mechanism relies on suppressing the original answer rather than using it to determine what to exclude, so the model can repeat the original answer when suppression is too weak or when a bias toward particular answers prevents it from selecting an alternative. To address this weakness in the model's negation mechanism, we propose a training objective that requires larger shifts in answer preference for more confident original predictions, and show that it reduces negation failures with less degradation of general capabilities than standard fine-tuning baselines. Together, our results demonstrate how mechanistic analysis can reveal why a linguistic capability fails and guide training that targets the underlying limitation.

---


### 133. [Correct Answers, Unsupported Findings: Evidence Binding in Forensic Reconstruction of LLM Agent Logs](https://arxiv.org/abs/2610.09581)

**<font color=#1a73e8>作者：</font>** Taehyeon Yun, Dongho Kim, Geonwoo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Forensic reconstruction of LLM-agent actions requires not only recovering the correct value, but establishing which preserved record supports that finding. Tool logs, generated explanations, and local citation identifiers capture different parts of this evidence, yet a citation identifier does not establish a source unless its binding to a record is preserved. We audit this distinction using 64 mechanically checkable cases from saved AgentDojo Banking executions. Two LLM readers reconstruct source relationships under controlled variations in visible evidence and identifier-to-record bindings. We separately evaluate complete-record agreement, evidence-grounded findings, justified abstention, and unsupported assertions. With original identifiers and no binding table, Sonnet recovered every literal source location but made unsupported citation-source assertions in 26 of 28 cases requiring the missing relation; 22 nevertheless matched the complete reference. Adding explicit bindings improved grounded reconstruction for both readers, whereas identifier renaming alone provided no consistent remedy. A deterministic same-packet comparator correctly resolved the bounded task or abstained throughout. These results show that factual agreement alone is insufficient for evaluating forensic reconstruction of agent logs and motivate preserving explicit record bindings to distinguish supported findings from correct guesses.

---


### 134. [Collaborative Reasoning Distillation via Cross-Feedback and Coherent Curation](https://arxiv.org/abs/2610.09587)

**<font color=#1a73e8>作者：</font>** Taehoon Kim, Seunggeun Cho, Dongsu Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning capabilities are critical for advancing Large Language Models, yet current approaches either require massive computational budgets or struggle to effectively distill reasoning to smaller models. Standard distillation methods rely on outcome-based rewards, failing to distinguish between sound reasoning and lucky guesses. We propose Collaborative Reasoning Distillation (CRD), a framework that enhances reasoning in compact models through three innovations: (1) interactive cross-feedback where teachers iteratively critique each other's reasoning, (2) fine-grained step-wise quality assessment capturing logical validity independent of final answers, and (3) coherence-aware step stitching that synthesizes complementary strengths. Students are trained via Reasoning Quality Optimization (RQO) with budget constraints. Our model, CRD-4B, achieves 97.3% on MATH-500 and 70.3% on AIME'25, surpassing baselines while using only 50K training examples, up to 12 times smaller than the datasets of comparable models.

---


### 135. [Dual- versus Single-Suggestion AI Support for Radiographic Interpretation in Residents: Randomized Multireader Study](https://arxiv.org/abs/2610.09589)

**<font color=#1a73e8>作者：</font>** Lin Wu, Zhe Xu, Hongyi Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose: To compare dual- and single-suggestion AI support for radiographic interpretation by residents, particularly when the shared AI suggestion was incorrect.
Materials and Methods: This prospective, multicenter, randomized three-arm reader study was conducted at three hospitals in China from July to September 2026 (ChiCTR2600129243). After specialty stratification, 132 residents with fewer than 3 years of clinical experience were randomized 1:1:1 to GPT-5.4 alone (group A), GPT-5.4 plus Kimi-K2.6 (group B), or GPT-5.4 plus Gemini-3.6 Flash (group C); 123 were analyzed. Participants interpreted 60 radiographs before and after AI support. The primary outcome was accuracy change. Welch ANOVA and Holm-adjusted t tests compared support conditions; HC3 linear models assessed specialty interaction.
Results: Among 123 residents (mean age, 24.1 years +/- 1.4; 65 women), radiology residents showed greater accuracy improvement with dual- than single-suggestion support (B-A, 6.69 percentage points [95% CI, 0.97-12.40]; C-A, 7.87 percentage points [95% CI, 1.64-14.11]; Holm-adjusted P = .030 for both), whereas accuracy change did not differ in non-radiology residents (P = .20). When GPT-5.4 was incorrect, AI-assisted accuracy was higher with dual- than single-suggestion support in radiology residents (40.1% and 40.4% vs 20.0%) and non-radiology residents (31.3% and 31.0% vs 12.1%) (all Holm-adjusted P < .001). The dual-suggestion effect differed by specialty (interaction difference, 10.44 percentage points; 95% CI, 4.36-16.52; P < .001).
Conclusion: Dual-suggestion support may mitigate the influence of erroneous AI suggestions, with greater accuracy improvement observed in radiology but not non-radiology residents.

---


### 136. [Learning Situation-Conditioned Thinking Policies for Long-Term LLM Agents](https://arxiv.org/abs/2610.09590)

**<font color=#1a73e8>作者：</font>** Hong Su  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running autonomous agents must reuse accumulated reasoning experience without allowing explicit historical memory and LLM context to grow indefinitely. However, existing memory mechanisms mainly retrieve, summarize, or compress past content and do not directly learn when particular kinds of thinking should be activated or discover new thinking knowledge from temporally dispersed experiences. This paper proposes a situation-conditioned thinking memory framework that transforms historical reasoning experience into a lightweight policy for predicting what should be thought about in the current situation, while leaving detailed reasoning to a large language model. Situations may represent temporal or spatiotemporal evolution rather than only current states. Temporary experiences are also periodically analyzed across multiple independent episodes to identify repeated long-range regularities, which are consolidated into new thinking knowledge and further internalized by the lightweight policy. Experiments show that the learned policy achieves 1.000 F1 on temporal-rule generalization, improves DeepSeek reasoning F1 from 0.789 to 0.868, reduces online processing time from 0.3636 ms to 0.0382 ms per query at 30,000 historical situations, and reaches 1.000 relation-discovery F1 and future-thinking accuracy after sufficient repeated cross-experience evidence.

---


### 137. [Structured pre-generation elicitation versus single-shot prompting in AI-assisted enterprise decision-making: a randomised online experiment](https://arxiv.org/abs/2610.09593)

**<font color=#1a73e8>作者：</font>** William Scott-Jackson  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI speeds, and mostly improves, professional work, but there is concern that users who delegate both the production and the evaluation of an answer may accept weak output and engage less with the underlying reasoning (cognitive surrender). Interventions proposed so far, such as unassisted practice or slowing adoption, sit outside the working task. We tested a different approach: an interactive metacognitive scaffolding layer (Cognistance, a prototype developed at the Oxford Centre for Impact Research (OCIR) that asks users to clarify context, choose a strategic direction and explain their reasoning before the AI generates a deliverable). Mean composite quality was 32% higher with the scaffold, with the same direction for every rater. Gains were largest for trade-off articulation and strategic coherence and absent for technical specificity. A large part of the aggregate effect reflected rescue of weak prompts: floor-scored (off-task) deliverables fell from 34% to 5%. Among participants whose own prompt already stated the data-localisation problem, the advantage was 21%. Treatment participants reported greater involvement and took about 2.4 minutes longer on average (10.46 minutes). Immediate recall scores were higher, which tentatively suggests better retention, but in this limited experiment, was not robust to sensitivity analyses. Self-ratings of quality did not track rated quality in either condition. Structured elicitation before generation improved the rated quality and task relevance of AI-assisted strategy documents at modest cost in time. Delayed retention, error detection and effects in live organisations are the priorities for the next stage of research.

---


### 138. [COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning](https://arxiv.org/abs/2610.09597)

**<font color=#1a73e8>作者：</font>** Zicheng Hu, Zhijian Zhou, Xuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous RL accelerates large language model post-training by decoupling rollout generation from optimization, but trains on stale trajectories. Existing methods primarily correct token-level policy mismatch through importance-ratio control in the actor objective. We show that this \emph{policy-side correction} alone is insufficient: advantage estimates also inherit mismatch from behavior-policy continuations, which we term \emph{advantage staleness}. We derive exact bias and variance decompositions for a general two-channel actor update, revealing nonseparable coupling between policy-weight and advantage-estimation errors: their interaction induces multiplicative bias terms, while squared policy weights amplify advantage uncertainty in gradient variance. This motivates the hypothesis that policy- and advantage-side correction should be coordinated. We introduce Coupled Off-Policy Correction (COPC), an actor--critic method combining token-level ratio masking with two-sided clipped-ratio weighting of TD residuals for return and advantage estimation. Joint parameter sweeps across staleness levels support this hypothesis: the effect of one correction parameter depends on, and can reverse with, the other. COPC achieves the highest reported performance on tool-integrated mathematical reasoning and search, outperforming the strongest reported asynchronous baseline in each setting. It also offers a broad high-performing parameter region and improved training stability. In search, COPC remains stable throughout training, while most evaluated asynchronous baselines collapse late in training. These gains persist at 64-step policy staleness. COPC adds minimal step-time overhead over asynchronous PPO and retains a $1.7\times$ step-time speedup over synchronous PPO.

---


### 139. [Lightweight and Versatile Learned Optimization by Recombination of Gradient History](https://arxiv.org/abs/2610.09604)

**<font color=#1a73e8>作者：</font>** Minyoung Choi, Dalta Imam Maulana, Wanyeong Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a lightweight and versatile learned optimizer that dynamically recombines gradient history, represented as averages over disjoint time spans. The optimizer reduces the prediction space to one scalar coefficient per gradient average, shared by multiple parameters. Progressively averaging older gradients minimizes memory cost of long history, while keeping their contributions independently accessible. A 37k-parameter network trained in 0.87 GPU-hours generalizes zero-shot to unseen tasks, lowering validation loss by 9.1% and 0.4% on BERT-Tiny and GPT-Tiny, and improving test accuracy over Adam by 3.5 %p on a Vision Transformer and by 2.7 %p on average across nine graph models, with FLOPs overhead as low as 0.3%.

---


### 140. [Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning](https://arxiv.org/abs/2610.09607)

**<font color=#1a73e8>作者：</font>** HyeonSeok Lim, SeungWoo Song, Inho Won 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skeleton-based reasoning prompting is a promising training-free approach for structuring LLM reasoning, but prior work largely assumes an English-centric setting. We propose the Language-Aware Skeleton Exploration Framework (LASEF) to study skeleton-language choice in multilingual mathematical reasoning. Across math benchmarks, model scales, and languages, we show that English skeletons yield a small positive tendency on average, most visible for smaller models and low-resource languages. However, few language-level gains remain significant after correction, and English is not universally optimal. Combining greedy decoding, multi-rollout evaluation, translation ablation, and cross-benchmark validation, we further find three patterns of skeleton-language effects: directionally consistent, evaluation- and benchmark-dependent, and asymmetric negative. These effects cannot be fully explained by generation quality alone. Overall, skeleton language is a context-dependent design variable that requires multi-level exploration. All resources are released at this https URL.

---


### 141. [When My Skill Becomes Agent Skill: How Knowledge Workers Share Their Expertise with AI Systems](https://arxiv.org/abs/2610.09608)

**<font color=#1a73e8>作者：</font>** Tianqi Song, Zicheng Zhu, Hancheng Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Organizations have long sought to make workers' expertise reusable by others. Agentic AI changes the nature of such reuse by enabling AI systems to act on workers' knowledge with limited human involvement. This raises the question of how this shift shapes workers' willingness to share their expertise. We conducted an experiment with knowledge workers who created materials incorporating domain knowledge and decided whether to authorize human or AI reuse. We find that AI and human reuse differ primarily in whether workers choose to share their knowledge, rather than in what they choose to share. Participants' reasoning shifts from prosocial considerations when sharing with humans toward concerns about loss of control, replacement, and downstream governance when sharing with AI. These findings suggest that AI reuse may intensify tensions between organizational knowledge reuse and contributors' interests. We discuss implications for workplace AI and knowledge management policies that preserve workers' rights and agency.

---


### 142. [How Do Agentic LLMs Decide to Call Tools? A Tool-Call Vector Shaped by Suppression](https://arxiv.org/abs/2610.09624)

**<font color=#1a73e8>作者：</font>** Xijie Gong, Tingxu Han, Jiahao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool calling, invoking external tools on demand, is central to agentic LLMs, yet the mechanism that decides whether a model calls a tool or responds directly remains poorly understood. Agentic prompts are long and heavily scaffolded, combining role instructions, tool schemas, format templates, and the user's request across hundreds of tokens, creating a noisy, highly entangled context in which no single controllable variable for mechanistic analysis is obvious. To obtain such a variable, we propose a method that converts complex agentic prompts into minimal contrastive pairs in which a single request verb determines the tool-call decision: replacing an execution-verb (e.g., \textit{write}) with an analysis-verb (e.g., \textit{discuss}) reliably flips the decision, suggesting it is mediated by a compact internal state. We construct 500 such paired prompts across Python, Java, and C++ (300 for mechanistic analysis, 200 held out for evaluation). We trace the decision to a vector, $\mu_\Delta$, that is both causally necessary and sufficient and generalizes beyond the discovery prompts to native multi-turn $\tau^2$-Bench trajectories and verb-free requests. Behavioral ablations show that the scaffold establishes a tool-call prior; Transcoder decomposition then reveals that analysis verbs suppress this prior through features signaling that tool use is unnecessary, whereas execution verbs largely leave it intact. Downstream scaffold-reading attention heads and MLP features read out the resulting state, and the same mechanism recurs across seven models from the Qwen, Mistral, and Granite families. Our code is available at this https URL.

---


### 143. [Coding-Agent Benchmarks Should Match Their Users' Task Flows](https://arxiv.org/abs/2610.09633)

**<font color=#1a73e8>作者：</font>** Igor Slinko, Yaroslav Golubev, Sergey Titov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evaluation of coding agents generally strives to be as realistic as possible. In our study, we collect 4,782 agent sessions of real software engineers in JetBrains IDEs, which we call Production Sessions. Since our subject is interactive agents, we study the sessions with at least three user messages (33% of the sample). These long sessions differ from issue-derived benchmark tasks in two ways: (i) user requests span a far wider mix of task types - questions about the project's code, planning, review, refactoring, execution - and (ii) users switch between types throughout a session. Long-session samples from three public interaction corpora exhibit markedly different Task Flows (the distributions of session lengths, task types, and type-to-type transitions), so no single interaction distribution is universally realistic: benchmarks should name a target use case and calibrate to measurements from it. We present SWE-TaskFlow, an approach for transforming any issue-derived benchmark: it preserves the verified tasks and tests while steering the interaction toward a target Task Flow through prompt splitting and verifiable repository QA, with a TaskFlow Alignment Score (TFAS) for selecting among generated trajectories. In a pilot on 700 SWE-Bench Pro tasks, solving the task sequentially in several steps approximately doubles agent cost without a stable change in resolve rate: the interaction protocol itself is an important dimension of evaluation.

---


### 144. [On-Policy Distillation Teaches New Skills but Not New Knowledge](https://arxiv.org/abs/2610.09639)

**<font color=#1a73e8>作者：</font>** Yixuan Tang, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) strengthens language-model reasoning, yet whether students acquire new factual knowledge or compositional skill for multi-step reasoning remains unknown. We separate these capabilities using a controlled synthetic framework that measures the student's initial capabilities and independently controls the teacher's additional facts, compositional skill, or both. Across four models from three families, reverse-KL OPD reliably transfers compositional skill across unseen reasoning structures, but transfers minimal factual knowledge. Decoupling the distillation recipe reveals the source of this asymmetry: replacing reverse KL with forward KL restores factual transfer, whereas student rollouts specifically improve the execution of multi-step reasoning. Experiments on recent factual QA and competition mathematics show a similar asymmetry under reverse-KL OPD, yielding notable reasoning gains without factual memory expansion. Together, these results demonstrate that on-policy distillation does not expand a model's parametric knowledge, but instead teaches it to organize and compose the knowledge it already possesses.

---


### 145. [Automatically Building and Updating a Knowledge Graph of MLIP Models](https://arxiv.org/abs/2610.09644)

**<font color=#1a73e8>作者：</font>** Alexis Beer, Liudmyla Klochko, Mathieu d'Aquin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complementing the many efforts in providing semantic representations of concepts, notions, and entities in materials science, we report and illustrate a process by which we can automatically build a knowledge graph of the fast evolving field of machine learning applied to the prediction of material properties, focusing on MLIP (Machine Learning Interatomic Potential). This LLM-based process relies on multiple steps, from information extraction in documents and articles to a validation loop using SHACL constraints to detect and correct errors. It is carried out on a model-by-model basis, focusing on the consistency of representation, therefore enabling an iterative construction where the addition of new models is facilitated. We illustrate the process by showing a few interesting aspects that can be queried from a knowledge graph built from the models listed in the Matbench Discovery leaderboard.

---


### 146. [When Rank Rises as LLMs Degrade](https://arxiv.org/abs/2610.09647)

**<font color=#1a73e8>作者：</font>** Zhaohui Geoffrey Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training adapts language models in non-stationary environments. Practitioners monitor representation health with RankMe and related spectral statistics, often assuming that rank falls when representations degrade. We show that this assumption is unsafe for LLM post-training. In a controlled study of Qwen3-0.6B with four degradation modes and three seeds, data duplication worsens held-out loss by 75% relative to healthy while increasing both original and centred RankMe; the latter changes by 13.5 pooled standard deviations. Covariance effective rank rises to nearly twice its healthy value. This failure is spectral dispersion rather than collapse, so a one-sided monitor rates the worst checkpoint as the healthiest. By contrast, a learning-rate misconfiguration lowers centred RankMe and k95, while uncentred RankMe is inconsistent across seeds. Direction is therefore a property of the regime-statistic pair and cannot be fixed by recalibration alone. We also distinguish two often-conflated statistics: RankMe normalises singular values, whereas covariance effective rank normalises eigenvalues. On raw intermediate-layer states in the pretrained model, massive activations pin the latter near 1 out of dimension d while RankMe retains usable range. We then test a two-sided, multichannel sequential monitor with separate calibration and test data. In a pre-registered shared-prefix, leave-one-seed-out evaluation, it detects all three damage regimes in every fold 10 to 60 steps after the fork and separates dispersion from downward-rank damage by firing direction. However, it never precedes held-out probe loss, and calibration with two seeds produces false alarms on the held-out healthy seed. Spectral monitoring can diagnose failure regimes, but it does not warn earlier than held-out loss, and validity claims require held-out healthy data.

---


### 147. [Rubric Spans are Label Representations: Joint LLM Encoding for Short Answer Scoring](https://arxiv.org/abs/2610.09660)

**<font color=#1a73e8>作者：</font>** Zhifan Sun, Sebastian Gombert, Fabian Zehner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Short Answer Scoring (ASAS) requires models that can score student responses against question-specific criteria while remaining efficient and transferable across rubric sets. We propose RUSPAN, a rubric-conditioned ASAS framework that treats rubric descriptions as semantic label representations. RUSPAN serialises the question context, student answer, and all candidate rubric levels into a single sequence, then scores the levels listwise from the rubric-span and whole-sequence representations produced in a single LM pass. We further introduce RUSPAN-RIM, in which a Rubric-Independent Mask prevents rubric spans from attending to one another, making rubric representations depend only on the answer and question context and preventing overfitting to rubric patterns during training for zero-shot transfer. On six ASAS benchmarks spanning English, German, and Portuguese, RUSPAN improves mono-benchmark scoring over discriminative and generative baselines, while RIM with position reindexing delivers consistent and substantial gains on PT-ASAG, the held-out benchmark with the strongest combined language and rubric-structure shift.

---


### 148. [Alice: A Large-Scale German Benchmark for Rubric-Based Multi-Dimensional Automatic Short Answer Scoring](https://arxiv.org/abs/2610.09661)

**<font color=#1a73e8>作者：</font>** Zhifan Sun, Sebastian Gombert, Jannik Lossjew 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Short Answer Scoring (ASAS) is central to NLP for Education. However, openly available benchmarks remain scarce, and existing datasets largely address how well students answer a question directly rather than how well they master underlying concepts (knowledge elements) such as thermal energy or epistemic activities (skills) such as reasoning or claim.
To address this gap, we introduce Alice, a large-scale, rubric-based German ASAS dataset that is pedagogically aligned and comprises three subtasks: (i) learning performance (Alice-LP), (ii) knowledge elements (Alice-KE), and (iii) skills (Alice-SK).
We further formulate rubric-based ASAS as a rubric-retrieval task and benchmark the dataset with a range of language models, from encoder-only models to lightweight LLMs. We also benchmark the dataset with zero-shot prompting via LLMs and a standard classification baseline. The experiments show that LLMs, in particular, struggle to score knowledge elements and skills in the zero-shot setting. They also indicate that rubric text is often useful, especially for Alice-KE and Alice-SK, while on Alice-LP gains over sample-solution-focused inputs are more modest and vary by model and input format.

---


### 149. [SAPD: Step-Aligned Privileged Distillation](https://arxiv.org/abs/2610.09665)

**<font color=#1a73e8>作者：</font>** Tianle Wang, Jiayu Liu, Ruizhi Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy post-training can improve large language models by learning from their own trajectories, but requires costly rollout generation. We ask whether fixed demonstrations can support competitive off-policy learning through better supervision. Our premise is that their usefulness depends not only on the training trajectories, but also on whether supervision provides informative preferences among continuations and connects this guidance to the reasoning decision being learned. We introduce Step-Aligned Privileged Distillation (SAPD), a rollout-free self-distillation method that turns demonstrations into step-aligned distributional supervision. Its key insight is to use the known progression of a reference solution to associate each reasoning transition with targeted privileged guidance, rather than treating the solution as undifferentiated context. On mathematical reasoning benchmarks, SAPD outperforms supervised fine-tuning and label smoothing on average while remaining competitive with on-policy reinforcement learning and self-distillation. Analyses support both the value of context-dependent distributional guidance and the benefit of aligning privileged information with the current step. SAPD also largely preserves out-of-domain coding performance and achieves approximately 2x training-loop speedups over the on-policy baselines. These findings suggest that carefully constructed supervision can make fully off-policy post-training a competitive and computationally efficient alternative. Our code is available at this https URL.

---


### 150. [Shared and structured inputs undermine collective random choice by reasoning AI agents](https://arxiv.org/abs/2610.09667)

**<font color=#1a73e8>作者：</font>** Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Random selection is widely used in resource allocation and auditing, making reliable implementation essential for AI-agent systems. Behavioural tests across six reasoning models uncovered threshold and divisibility rules used in identifier-based choices. For threshold-following GPT-6 Sol and Gemini 3.8 Flash, single-agent measurements prospectively predicted correlated participation under shared identifiers and biased participation under distinct identifiers with common timestamp bits. Changing dates, formats and identifier labels revealed when these predictions held. Explicit instructions to randomize independently reduced but did not eliminate shared-input correlation. To test implications for oversight, we asked four models to select customer requests randomly for human review. GPT-6 Sol approached the target rate while selecting predictably from identifiers; the others rarely selected requests. All four closely followed supplied random draws. These findings expose collective and audit vulnerabilities that selection rates alone miss, making input-dependent bias, correlation and predictability central targets for agent evaluation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
