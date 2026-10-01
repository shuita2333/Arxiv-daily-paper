# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

---

### 151. [MEMO: Multi-Level Entity-Aware Memory for Streaming Video Understanding](https://arxiv.org/abs/2609.38900)

**<font color=#1a73e8>作者：</font>** Yinying Li, Yuqian Fu, Yulin Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires models to process unbounded visual streams while preserving rich visual semantics across vast temporal horizons, posing a fundamental challenge for memory modeling. Existing approaches primarily focus on increasing memory capacity, either by compressing historical information into fixed-size representations or by extending storage beyond GPU memory. However, these methods largely rely on global or coarse-grained representations, inevitably losing fine-grained visual information. In this work, we argue that streaming video memory should explicitly encode structured and semantically meaningful representations, particularly at the entity level. To this end, we propose MEMO, a novel framework that models streaming video through multi-level, entity-aware structured memory. MEMO performs multi-level perception to jointly capture global semantics, entity dynamics, and spatial structures, partitioning streaming video into semantically coherent chunks. Each chunk is organized into a structured memory, where lightweight global and entity-level representations serve as retrieval indices, while the corresponding high-resolution visual content is retained separately for on-demand access. At inference time, MEMO performs query-specific retrieval over the structured memory and selectively recalls relevant visual evidence for downstream reasoning. Notably, MEMO is training-free and plug-and-play with existing multimodal large language models. Extensive experiments on StreamingBench and OVO-Bench demonstrate that MEMO consistently improves multiple base models and achieves state-of-the-art performance.

---


### 152. [Unlearning Deceptive Behaviors in LLMs with Contrastive Forget Sets](https://arxiv.org/abs/2609.38909)

**<font color=#1a73e8>作者：</font>** Haoran Tang, Rajiv Khanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often know the truth and say otherwise: a model that answers correctly when asked neutrally will affirm a user's mistaken belief, or misstate a fact its system prompt wants hidden, once the context rewards it. Such deception is a behavior conditioned on context, not knowledge, yet machine unlearning, the natural tool for removing a behavior from the weights, is built to forget facts that a deceptive model still needs. We propose to unlearn when a model deceives rather than what it knows, with a contrastive forget unit built from the model's own realized deceptions: the same question under a deception-triggering and a neutral context, admitted only where belief holds and behavior flips. Standard objectives on this unit face a dilemma. Suppression objectives such as NPO leave much of the deception in place. Target-based objectives, which distill the model's neutral behavior into the pressured context, remove it but induce context blindness: a target generated without the context teaches the model to stop reading it, eroding benign system-prompt instructions, secret-keeping and the reasoning a monitor inspects, a failure invisible to deception rates and capability benchmarks. We introduce PACT, which trains toward pressure-aware counterfactual targets (the model's own honest response, with a trace that registers the pressure and resists it) while retaining the benign uses of the triggering context. On two 32B reasoning models, PACT reduces held-out deception from over 50% to under 3% while system-prompt adherence, secret-keeping and the reasoning trace stay at the base model's level. On a tug-of-war score of removal against retention, PACT reaches 0.94 and 0.86, against at most 0.77 and 0.60 for any baseline. Like removed knowledge, removed deception is shallow under relearning, and terms that simulate the attacker hold it only at a cost in context use.

---


### 153. [Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives](https://arxiv.org/abs/2609.38912)

**<font color=#1a73e8>作者：</font>** Peng Kuang, Haibo Jin, Dehao Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses govern how large language models (LLMs) gather context, invoke tools, verify results, preserve state, and terminate, largely affecting agent performance. However, the value of each harness mechanism can differ across heterogeneous tasks: a mechanism that improves one task may impose overhead or context distraction on another, leading to the suboptimality of a global harness. We characterize this suboptimality as a mismatch induced by fixed mechanism choices, motivating task-specific harness construction. Nonetheless, generating harness code for each task introduces generation and debugging costs, with execution risks that can compound as more mechanisms are generated. To address those challenges, we introduce Harness Primitives, reusable harness mechanisms with clear application scope and composition contract mined from failed task trajectories. Based on Harness Primitives, we propose STITCH, a framework that Selects suitable primitives given Task Information and compiles them into Task-speCific Harnesses at test time. This separation enables task-specific harnesses without generating or repairing mechanism code at test time. Extensive experiments demonstrate that STITCH not only improves harness adaptability and robustness, but also scales with the primitive library size, boosting task success rates by up to 12 points over fixed harness baselines, surpassing human-designed harnesses like Codex CLI while maintaining a minimal test-time harness composition overhead of only 2.7%, 638 times more efficient than generating task-specific harnesses from scratch. Ultimately, our work demonstrates that building task-adaptive harnesses can be beneficial for completing diverse tasks and that building reusable primitives can be a promising path towards this goal.

---


### 154. [GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis](https://arxiv.org/abs/2609.38923)

**<font color=#1a73e8>作者：</font>** Qisheng Su, Hanchen Wang, Guanru Zhu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Working agents need to read diverse files, coordinate tools, and produce deliverables. Training such agents requires tasks built on many real files with verifiable results, but few pipelines exist to synthesize this kind of data. Existing pipelines either generate files with models, which lack realism and diversity, or build tasks on real files without task-specific verifiers, leaving result quality unchecked. We introduce GraphForge, an evidence-graph based framework that grounds both the task and its verification in real files. Starting from occupation-grounded seeds for controlled diversity, GraphForge assembles a workspace of real files for each seed and builds an evidence graph over their relations. Since the task statement and rubrics are both derived from this graph, task requirements are backed by the workspace files and each criterion is anchored to the files needed to verify it. An initial rollout further tests executability, and a revision agent repairs the task and rubrics against the original files before trajectories are collected. Fine-tuning Qwen3.6-27B on 2,169 GraphForge trajectories brings GDPVal to 1445.7 (+65.7) under OpenHands, and Workspace-Bench-Lite and SpreadsheetBench II to 63.7 (+7.7) and 24.0 (+13.7) under Claude Code. Rejection fine-tuning on the SFT model's own rollouts, with candidates selected by the evidence-anchored rubrics, yields further improvements on all three benchmarks, suggesting that the rubrics provide a useful selection signal. The data and models are available.

---


### 155. [From Image Interpretation to Clinical Reasoning: Upstream Physician-Context-Aware Multimodal Learning with Causal Reinforcement Learning](https://arxiv.org/abs/2609.38924)

**<font color=#1a73e8>作者：</font>** Jialu Pi, Yanan Ma, Weijie Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Major adverse cardiovascular events (MACE) remain the leading cause of mortality worldwide. Opportunistic screening using routinely acquired clinical data offers a scalable approach for identifying high-risk individuals before acute events occur. Although chest X-rays (CXRs) capture latent cardiovascular biomarkers and clinical histories provide complementary patient context, existing medical vision-language models are primarily optimized for radiology interpretation rather than prognostic reasoning. We propose a causal reinforcement learning framework for multimodal clinical reasoning that integrates CXRs and physician-authored clinical histories for opportunistic MACE prediction. The framework introduces (1) a role-decoupled dual-LLM architecture that separates reasoning from risk prediction, (2) a dual-action causal reinforcement learning policy for evidence selection and reasoning optimization, and (3) causal token pruning to learn compact multimodal representations. Evaluated on an internal cohort, an emergency department cohort, and the external MIMIC dataset, the proposed framework consistently outperformed unimodal baselines and state-of-the-art medical vision-language models, achieving AUROCs of 0.720, 0.760, and 0.845, respectively. It also substantially improved reasoning quality, achieving higher GREEN scores and higher expert preference while maintaining robust predictive performance across diverse patient populations.

---


### 156. [Learning What to Forget: Distributional Unlearning for LLM Representation Spaces](https://arxiv.org/abs/2609.38929)

**<font color=#1a73e8>作者：</font>** Pinaki Mohanty, Haoran Tang, Maggie Makar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning systems increasingly face the need to remove the influence of entire data domains, such as toxic language, harmful behavior, or topical content, rather than isolated records. Recent work formalizes this problem as \emph{distributional unlearning}: selecting a subset of a forget domain whose removal moves the training distribution away from an unwanted population while preserving proximity to the desired one. However, existing analyses often impose parametric assumptions to obtain tractable selection rules. These assumptions may be poorly suited to high-dimensional language-model representations. We introduce \textsc{Mamushi}, a framework for non-parametric distributional unlearning that ranks forget examples using a probabilistic classifier whose Bayes-optimal logit equals the forget-to-retain log-density ratio (up to an additive class-prior constant). We show that thresholding the population log-density ratio yields the optimal fixed-budget selection rule for our removal--preservation objective and establish a non-asymptotic transfer guarantee relating score-estimation and threshold-calibration errors to degradation from the population-optimal selection rule. Our empirical evaluation spans real-world datasets on toxic-language removal and topical-domain removal regimes using different representations, with \textsc{Mamushi} achieving a more favorable removal--preservation trade-off than other baselines. Our work shows that \textsc{Mamushi} can serve as an efficient selection approach for downstream machine unlearning procedures, reducing the number of forget examples required to reach a fixed forgetting target.

---


### 157. [Adaptive Self-Consistency: From Black-Box Sampling to Distribution-Valued Feedback](https://arxiv.org/abs/2609.38931)

**<font color=#1a73e8>作者：</font>** Jingkai Huang, Yunfan Zhang, Will Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-consistency samples many reasoning trajectories and aggregates their final answers, treating the LLM as a black box that returns one answer per trajectory. Yet the final answer of each trajectory is sampled from a softmax vector that is available from the model's log-probabilities. We refer to this as the grey-box setting in which each trajectory reveals this answer distribution rather than a single draw from it. We formulate efficient inference in this setting as sequential mode identification with distribution-valued observations: sample trajectories one at a time and stop as soon as the LLM's modal answer is identified at a prescribed confidence level. We characterize the asymptotic stopping rate of mode identification with distribution-valued observations exactly and show that it is never worse than the black-box rate. We then propose the ASC-D algorithm, a betting stopping rule that attains this asymptotic stopping rate. On MMLU-Redux, ASC-D uses $46.4$--$95.6\%$ fewer trajectories than answer-only adaptive self-consistency baselines and achieves the highest fixed-budget correct-certification rate across three open-source models.

---


### 158. [APTInvestBench: Evaluating Autonomous APT Investigation under Varying Telemetry](https://arxiv.org/abs/2609.38954)

**<font color=#1a73e8>作者：</font>** Yu Wang, Shuhao Li, Tao Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents could help security operations centers (SOCs) investigate advanced persistent threats (APTs) by turning weak leads into evidence for intrusion scoping and response. Yet success under one telemetry setting does not establish robustness to changes in log collection, retention, or sampling. We introduce APTInvestBench, a benchmark for evaluating cross-telemetry robustness in autonomous APT investigation. It comprises 370 cases across seven SOC-inspired conditions, derived from 56 report-informed attack reconstructions with 16.4 million log records. Agents investigate unverified leads and submit reports with record-level citations. Fixed action-level support requirements track sufficient evidence across available logs, query returns, and formal citations, separating telemetry limitations from acquisition and reporting gaps. Across eleven LLMs, agents acquire sufficient evidence for 44.3% of recoverable attack actions on average, while formal citations support only 25.0%. More importantly, aggregate coverage can conceal substantial instability: from Full to endpoint-only telemetry, coverage declines by only 1.6 percentage points, yet 35.5% of previously covered actions lose sufficient citation support despite remaining recoverable. Across four frameworks, such losses persist even when registered supporting records remain unchanged. APTInvestBench provides reusable investigation environments and diagnostic evaluation for identifying these gaps and developing more reliable defensive agents.

---


### 159. [Targeted Retrieval, Compact Representations: How CoT Reasoning Improves Long-Context Counting](https://arxiv.org/abs/2609.38958)

**<font color=#1a73e8>作者：</font>** Liang Twist Shan, Tianyu Hu, Hao Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been rapidly improving in long-context tasks, powered by Chain-of-Thought (CoT) reasoning. However, the internal mechanisms underlying this improvement remain unclear. We investigate these mechanisms through a needle-in-a-haystack (NIAH) counting task, where an LLM is asked to count the number of records dispersed in a long text. Across twelve model comparison groups, Thinking (or reasoning) improves counting accuracy over Non-thinking, with pronounced gains at larger counts. This motivates our mechanistic analysis, which identifies two contrasting mechanisms: (i) broad retrieval, where Non-thinking models broadly attend to multiple needles; (ii) targeted retrieval, where Thinking models use enumeration in CoT traces to successively retrieve needles. Targeted retrieval concentrates attention on individual needles and is accompanied by more compact internal representations. Moreover, causal intervention analysis suggests that Thinking models use the CoT trace to maintain and update an internal counter as needles are successively retrieved, even without explicit numbering. In small controlled experiments, both retrieval mechanisms and counter states emerge under standard autoregressive training. Together, our results connect long-context retrieval with representation geometry of counting, supporting a state-tracking account of CoT reasoning.

---


### 160. [Alleviating Hallucination in Reasoning Tasks with Training-Free Uncertainty-Guided Steering](https://arxiv.org/abs/2609.38962)

**<font color=#1a73e8>作者：</font>** Litian Liu, Qiqi Hou, Yubing Jian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on hallucination detection in large language models has shown that, for a fixed pre-trained model and reasoning task, it is possible to estimate the model's confidence in the correctness of its outputs. Such uncertainty estimates have primarily been used to improve truthfulness by detecting or filtering confabulations. In this work, we ask whether these signals can instead be used more proactively to directly improve the accuracy of model-generated answers. We propose USteer, a simple, training-free steering mechanism that adjusts a model's layer-wise activations during inference using the gradient of a confidence measure with respect to the activations. This procedure nudges generation toward outputs with lower uncertainty at inference time, without modifying model parameters or requiring additional supervision. We show that this approach consistently reduces hallucination across a range of tasks, demonstrating that confidence signals can be leveraged not only for detection, but also for effective inference-time control of model behavior.

---


### 161. [When Order Matters: First-Speaker Bias and Mitigation through Personality in Sequential Multi-Agent Debate](https://arxiv.org/abs/2609.38964)

**<font color=#1a73e8>作者：</font>** Duofeng Xu, Bryan Hooi, Dandan Qiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) is often used to improve large language model (LLM) reasoning, but sequential debate is rarely a neutral aggregator of agents' opinions. We show that sequential MAD suffers from a pronounced first-speaker bias: agents disproportionately shape the final answer when they speak first. As a result, placing a stronger model after weaker ones can substantially offset its reasoning advantage. We then focus on the disadvantaged strong-agent-last setting and ask whether personality prompting can mitigate this imbalance. Drawing on the Big Five model, we study agreeableness and extraversion as behavioral interventions applied to either the strong or weak side. We find that their effects are trait-specific. Influence consistently shifts in the direction of lower agreeableness, and assigning low agreeableness to the stronger agent helps restore its lost influence and improves final accuracy. Extraversion, by contrast, produces less systematic changes in influence and accuracy, with its clearest effect appearing in agents' verbosity. These findings show that effective MAD design depends not only on model capability, but also on how speaking order and induced interaction behavior shape the debate process.

---


### 162. [Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment](https://arxiv.org/abs/2609.38972)

**<font color=#1a73e8>作者：</font>** Yihuai Hong, Shauli Ravfogel, Chen Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) traces often serve as a proxy for how Large Language Models (LLMs) arrive at their answers. However, growing evidence shows that models' CoT often fails to reflect their internal computations and can be changed without affecting their final answers. In this work, we measure and improve the alignment between the reasoning described in an LLM's CoT and what it computes internally. We propose CoT-Interpretability Alignment (CIA), a metric that measures the agreement between a model's CoT traces and its internal reasoning strategies as detected by interpretability tools. We evaluate CIA on three tasks (two-hop question answering, hint intervention, and integer multiplication) across three LLMs, finding that LLMs exhibit limited alignment across all tasks (44.8-75.9%). We then experiment with improving CIA via post-training, setting both the task accuracy and parametric faithfulness signals as a reward. Experiments show that we can substantially improve CoT parametric faithfulness while maintaining or improving the task accuracy. We provide rich analysis, such as their generalization patterns. Our work provides both a framework for auditing CoT parametric faithfulness and a pathway toward making models' explicit reasoning more trustworthy. Code and data are available at this https URL.

---


### 163. [RealWorldShop: Benchmarking and Improving Conversational Shopping Agents in Real-World E-commerce](https://arxiv.org/abs/2609.38974)

**<font color=#1a73e8>作者：</font>** Xinwei Yang, Kelong Mao, Yudong Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are reshaping ecommerce from static recommenders into interactive shopping assistants, yet real-world shopping requires session-level decision support: users reveal and revise constraints, coordinate multiple goals, and expect product-grounded recommendations over a full conversation. Existing benchmarks are mostly outcome-oriented or execution-oriented, leaving this evolving decision process under-evaluated. We introduce REALWORLDSHOP, a benchmark built on 3.28M grounded products, structured shopping episodes, a profile-grounded and actioncontrolled user simulator, and role-play evaluation. Our analysis shows that current systems produce locally plausible responses but struggle with state tracking, constraint updating, and grounded convergence, especially under ambiguous intent, bundle, and multi-intent scenarios. We further propose REALSHOP_AGENT, an executable session-control framework with explicit state management, shopping-flow control, catalog-grounded retrieval, and runtime guards. Experiments show that REALSHOP_AGENT consistently outperforms strong baselines on REALWORLDSHOP.

---


### 164. [Fairness Beyond a Single Run: Training-Seed Variability in Speech LLM Adaptation](https://arxiv.org/abs/2609.38976)

**<font color=#1a73e8>作者：</font>** Srishti Ginjala, Eric Fosler-Lussier, Srinivasan Parthasarathy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Demographic fairness gaps in automatic speech recognition are almost always reported from a single training run. We fine-tune the Q-former projector and LoRA adapters of a speech LLM at five audio compression factors and six random seeds, holding the encoder, base decoder, data and decoding fixed, and evaluate every run on Common Voice and Fair-Speech. At 460 h of clean LibriSpeech, the seed moves fairness metrics more than compression does on most demographic axes. A balanced 3x3 decomposition attributes 85.3% of the variation in Fair-Speech ethnicity normalized gap to the seed against 8.3% to compression (p = 0.009), though compression explains more on age and gender. Held-out LibriSpeech word error rate spreads by 0.04 points across those seeds while Common Voice spreads by 8.57, so these are not failed runs, and the effect survives controlling for accuracy and dropout. Scaling and diversifying the adaptation set to 960 h damps the effect but does not remove it. On Fair-Speech ethnicity, two single-run systems must differ by more than 0.30 in normalized gap to exceed seed variability.

---


### 165. [Mitigating Object Hallucination in Large Vision-Language Models via False Discovery Controlled Visual Data Splitting](https://arxiv.org/abs/2609.38979)

**<font color=#1a73e8>作者：</font>** Chang Liu, Yu Tian, Rui Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple object hallucination, where large vision-language models (LVLMs) generate objects not supported by the visual input, is a persistent challenge caused by visual uncertainty during decoding. Existing methods reduce hallucinations using contrastive signals, but they rely on heuristics and lack principled control of false positives at the image level. To address this, we propose False Discovery Rate-COntRol of HALlucination (CORAL), a training-free framework that models visual uncertainty using an uncertainty-aware visual data splitting strategy and leverages mirror statistics to quantify visual contrast during decoding. By computing mirror statistics from paired, symmetrically perturbed visual inputs, CORAL estimates spurious object predictions and sets a data-driven threshold to control the expected fraction of false discoveries per image, suppressing hallucinations while retaining high power for truly grounded objects. The framework is flexible, supports multiple LVLMs, and mitigates hallucinations without retraining or supervision. Extensive experiments on multiple benchmarks with several evaluation metrics demonstrate that CORAL consistently outperforms state-of-the-art methods, providing more reliable and robust hallucination control. Code is available at: this https URL

---


### 166. [SCORE-LM: State-Space Radar Representations with Language Models for Fault Diagnosis](https://arxiv.org/abs/2609.38980)

**<font color=#1a73e8>作者：</font>** Mainak Mallick, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radar hardware faults threaten automated perception, motivating accurate, compact diagnosis and understandable maintenance guidance. We introduce SCORE-LM, which couples a small scatterer-conditioned operator-response encoder (SCORE) to an adapted local language model. SCORE combines self-referenced complex trajectories, physical descriptors, and a selective state-space branch, with source-only self-supervision and directional fault inference. On eight capture-excluded Rad-R fault recordings, it achieves state-of-the-art performance within the evaluated nine-model comparison: 88.39% mean capture recall and 88.20% four-fault macro-F1 at ten frames. Its 39,520 radar inference coefficients are 119.7 times fewer than RadrNet-DS-CI's, while recall is 15.56 percentage points higher than this strongest competitor. In a separate low-label protocol, SCORE reaches 71.58% recall with one labeled source window per class. A nonlinear projector converts four frozen fault similarities into five soft tokens, linking compact diagnosis to class-conditioned maintenance guidance. On 75 development questions covering 24 radar windows, language adaptation raises correct-fault answers from 45 to 62 (60.0% to 82.7%) relative to removing the co-trained adapters, while retaining the same projector. SCORE-LM thus combines a compact radar specialist with a language interface for communicating fault-specific inspection guidance.

---


### 167. [Settle: Learning When to Stop Reasoning](https://arxiv.org/abs/2609.38997)

**<font color=#1a73e8>作者：</font>** Ryan Brown, Zihao Fu, Chris Russell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning models often continue generating after their answers have settled. Settle learns when to stop from answer stability in completed traces. It trains the existing end-of-reasoning token while keeping other predictions close to the base model, and requires only ordinary decoding at inference. On MATH-500 with Qwen3-4B, Settle reduces token count by 40% with a 0.5-percentage-point decrease in accuracy. It gains 6.16 percentage points over supervised fine-tuning on the same traces shortened at their first stable answer, at nearly identical token counts. Its stopping score predicts whether a correct answer will remain correct. Settle extends the accuracy-token-count Pareto frontier of the evaluated stopping methods.

---


### 168. [The Invisible Language Tax: Token Premiums of French and Regional Languages in 2026 LLM Tokenizers, and a French-Optimized Prototype](https://arxiv.org/abs/2609.39001)

**<font color=#1a73e8>作者：</font>** Thomas Serval  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM services are billed per token and context windows are measured in tokens, yet the number of tokens needed for the same content varies across languages. We measure this token premium on seven tokenizers of widely used 2026 models (OpenAI o200k, Llama 3, Qwen3, DeepSeek V3/V4, Gemma 3, Mistral Tekken, and the Claude generation-5 tokenizer via Anthropic's counting API) on NTREX-128 (124 non-English reference translations) and on the Universal Declaration of Human Rights for regional languages. French requires 31% to 58% more tokens than English, whereas Simplified Chinese ranges from 5% fewer to 40% more and is cheaper than French on six of the seven tokenizers. Regional and overseas languages of France pay roughly 1.6 to 3.3 times the English count. We discuss how history re-sending, tiered pricing and fixed context windows amplify the absolute gap in agentic use. In a controlled experiment (BPE, Europarl, 50k vocabulary), adding French to tokenizer training data quickly reduces the premium, with diminishing returns and a growing cost for English. Finally, we present Baracoda FR v1.2, a byte-level BPE prototype with Tekken's vocabulary size. On a final test of six corpora never consulted during design, with a protocol declared fixed beforehand, it uses 11.5% fewer tokens than Tekken on French and 3.7% fewer on English; results hold after removing test sentences overlapping the training data and with an equal ordinary-token budget. It is worse on other languages and, at comparable vocabulary size, does not outperform CroissantLLM. These are segmentation results only; effects on model quality and task cost remain to be shown.

---


### 169. [Evidence First, Arithmetic Second: A System Report and Failure Analysis for DocSem](https://arxiv.org/abs/2609.39013)

**<font color=#1a73e8>作者：</font>** Divya Godara, Sachin Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> EVICALC, our system for the DocSem shared task, achieved 8.61% joint accuracy on 1,730 tasks in the official final test evaluation. It reads a PDF, selects a passage, asks a language model to write an arithmetic expression, and evaluates that expression in local code. Saved intermediate results support inspection of failures. A separate public-validation run achieved 92.17% answer accuracy and 1.00 evidence F1. The configurations and metrics differ, so these scores are not a controlled comparison. Our manual, post-hoc analysis is descriptive: in one inspected case, optical character recognition (OCR) and block grouping merged the relevant passage into another block, and the system answered from unrelated text. An exploratory study of reading page images on 100 documents returned evidence identifiers for only 22 documents. These descriptive findings motivate further evaluation; they do not establish the causes of the overall score.

---


### 170. [Frame Differential On-Policy Self-Distillation for Video Reasoning](https://arxiv.org/abs/2609.39021)

**<font color=#1a73e8>作者：</font>** Haiying He, Xin Zheng, Shaoli Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has substantially improved the reasoning ability of multimodal language models through verifiable rewards and increasingly fine-grainedvisual or temporal credit assignment. In video reasoning, however, current RL methods typically train with a fixed sparse frame budget: increasing the number of frames makes autoregressive rollouts expensive, while too few frames may miss temporally localized events and fine-grained visual details. We present \textbf{Frame Differential On-Policy Self-Distillation (FD-OPSD)}, which transfers the useful evidence of dense frame observations to a sparse frame policy during RL training. FD-OPSD compares the policy's token level preferences for the same sampled response under sparse and dense views, and distills the resulting frame differential signal without an external teacher or dense autoregressive rollout. The method preserves sparse-frame rollouts and leaves inference unchanged. Across Qwen2.5-VL-7B and Qwen3-VL-4B on six video reasoning benchmarks, FD-OPSD yields higher overall average performance than the strongest corresponding GRPO, T-GRPO, or Video-KTR baselines across the 16, 32, and 64 frame evaluation settings. These results show that dense visual evidence can be transferred selectively during training through token level self-distillation while retaining sparse frame rollouts and unchanged inference.

---


### 171. [A Missing Piece for Trustworthy AI Reviewers: From Benchmarking Rhetorical Robustness to SciCore Review](https://arxiv.org/abs/2609.39027)

**<font color=#1a73e8>作者：</font>** Chenguang Wang, Ming Li, Chengrui Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI reviewers can assign different judgments to manuscripts that report the same science in different wording, potentially rewarding rhetorical optimization over scientific improvement. We formulate Rhetorical Robustness as the joint requirement of stability across content-preserving rewrites and discrimination across papers. We introduce RobustReview, a controlled full-manuscript benchmark with 1,260 manuscript versions, and evaluate 30 reviewer configurations. The benchmark reveals false robustness, where low rewrite sensitivity coincides with score collapse across papers, and shows that human alignment and rhetorical robustness rank reviewers differently. Moreover, the evaluated content-focused prompting protocol does not consistently improve robustness across backbones. Motivated by these findings, we introduce SciCore, a dual-branch reviewer that averages a full-manuscript judgment with a judgment based on an extracted, structured science core. This design combines manuscript-level assessment with a content-normalized view intended to reduce rhetorical sensitivity. In our primary GPT-5.5 comparison, SciCore achieves a leading joint stability-discrimination profile among the benchmarked reviewers while maintaining competitive human alignment. These results identify rhetorical robustness as a distinct evaluation target and demonstrate the potential of science-core review to improve it.

---


### 172. [TED:Text-Axis Evidence Decomposition for Prompted Anomaly Localization](https://arxiv.org/abs/2609.39033)

**<font color=#1a73e8>作者：</font>** JinYoung Kim, Geonho Kim, GiJeong Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP is a powerful vision-language model, but it was not designed for fine-grained defect localization; CLIP-based anomaly detectors therefore adapt it with prompts or lightweight modules to increase defect sensitivity. We show that stronger sensitivity does not necessarily make local evidence reliable: under domain shift, adapted CLIP-AD models often assign high anomaly scores to both true defects and visually complex normal regions. The issue is not simply missing defect information, but a local scoring rule that decodes defect and hard-normal evidence, having the same anomaly evidence. We propose TED (Text-Axis Evidence Decomposition), a post-hoc scoring method that asks whether each ambiguous response is better supported by source defect patches or by source normal patches mistaken as anomalous. TED compares these supports under the host's normal-versus-anomaly text response, leaves the backbone and prompts unchanged, and requires no target-domain training. It works as a train-free score for raw VLM backbones or as a source-calibrated residual correction for adapted CLIP-AD hosts. Across frozen VLM backbones, TED substantially improves pixel-level localization over raw prompt similarity; across adapted hosts, it improves most pixel-level settings over P-AUROC, P-PRO, and P-AP. Gains are largest under stronger hard-FP competition, with mean localization gain increasing from +5.0 in low-competition regimes to about +10.9 in mid/high-competition regimes. These results suggest that recoverable defect evidence can already exist in pretrained multimodal representations, but reliable localization requires decoding it against hard-normal competitors. Code will be released at TED GitHub repository.

---


### 173. [RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement](https://arxiv.org/abs/2609.39045)

**<font color=#1a73e8>作者：</font>** Wenyi Wu, Minghao Fu, Jieyu You 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have made automatic game generation increasingly feasible, yet reliably improving generated games beyond a playable version remains challenging. Naive iterative refinement can easily overfit a small set of test cases, producing fragile games with unresolved bugs, missing behaviors, and poor generalization to broader player interactions. We introduce RSIGame, an autonomous agentic game development framework with recursive self-improvement. RSIGame organizes development into complementary local and global loops. Concretely, a local explore-diagnose-improve loop broadly explores the executable game, diagnoses and prioritizes discovered issues, and performs evidence-grounded revision, where an evolving checklist continually accumulates new testing and improvement guidance. A global loop tracks overall quality, preserves the best checkpoint, and detects saturation or regression over long-horizon development. Beyond test-time improvement, RSIGame further internalizes successful development experience into the generator through training. Across 140 GameCraft-Bench tasks, two game engines, and five generators, RSIGame consistently improves game quality under matched development budgets. Notably, experience internalization enables Qwen3.8-27B to reach 61.38 on Godot and 58.53 on Phaser, exceeding GPT-5.5 one-shot scores while reducing Qwen's generation tokens by 11 times.

---


### 174. [Structure vs. Chain-of-Thought: Evaluating LLM Criteria Extraction for Depression Severity](https://arxiv.org/abs/2609.39049)

**<font color=#1a73e8>作者：</font>** Xinkai Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) can rate depression severity directly from a social media post or mark which clinical criteria the post shows and let code turn the count into a label. The latter is easier to audit because a clinician can check each marked criterion. We compare these approaches on two Reddit corpora using three LLMs (from 9B to frontier scale) and two questionnaires (PHQ-9, BDI-II), and measure agreement with quadratic weighted kappa. For the two frontier models, criteria extraction scores above chain-of-thought on one corpus only when its decision thresholds are fitted on labeled data. Neither model's gain is significant, with or without recalibrating chain-of-thought on the same labels. With thresholds fixed a priori from PHQ-9's criteria, extraction shows no gain on either corpus, even where models mark over two criteria per post. The 9B model behaves differently on a corpus from depression communities. It labels most posts severe, whether prompted directly or with chain-of-thought, while the a priori rule beats both without labels. After chain-of-thought is recalibrated on the same labels, no significant gap remains, consistent with a calibration effect. Yet higher ordinal agreement does not ensure better detection of severe cases. PHQ-9 criteria extraction misses most severe posts, and moving from direct prompting to chain-of-thought and then to extraction increases misses in nearly all comparisons. On the primary corpus, a relabeled stress dataset, a model using that dataset's own features, including word counts from the text, is not significantly different from frontier criteria extraction under the a priori rule.

---


### 175. [Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems](https://arxiv.org/abs/2609.39050)

**<font color=#1a73e8>作者：</font>** Deema Alnuhait, Gengyu Wang, Muhammad Khalifa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As multi-agent systems enter high-stakes domains, the possibility that agents may circumvent safety boundaries is a growing concern. Prior work has examined this risk primarily in adversarial settings, where agents are instructed or rewarded to communicate covertly and evade oversight. We show that benign agents can cross the same boundaries without adversarial incentives. We emulate a software-engineering workflow in which a planner represents a company hiring an external developer. The planner writes requirements and holds a company credential it is instructed not to disclose to the developer; a monitor screens their exchanges. Seven of nine tested frontier models disguise the credential in their requirements to help the developer recover it while evading the monitor, even after completing their assigned objective. For example, across 6,000 episodes with DeepSeek-V4-Pro, the planner attempts concealment in 16.9%; in 0.9%, the credential evades the monitor and is recovered and used by the developer. Despite the low per-episode rate, the risk compounds across repeated exchanges: at 0.9%, 105 independent episodes carry a 61.3% chance of at least one breach. Our analysis suggests that the planner misinterprets disguised disclosure as helping the developer and reads the nondisclosure rule as banning plaintext, not character codes or riddles. We call this behavior covert assistance. Monitoring favors concealment, while concealment gives way to direct disclosure when the recipient is presented as a human rather than an AI agent, so leakage persists. Giving the monitor the credential improves detection but requires trusting it with the secret. These risks, in models already used for software engineering, challenge oversight to distinguish authorized cooperation from task-advancing assistance that crosses safety boundaries.

---


### 176. [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](https://arxiv.org/abs/2609.39065)

**<font color=#1a73e8>作者：</font>** Yan Wang, Zhihao Zhang, Ke Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on installable skills, which are packages of instructions, code, and resources that equip them with task-specific capabilities and, once installed, can be automatically invoked across subsequent user tasks. This creates a chain of trust in which users delegate authority to agents, while agent frameworks admit skill-provided content into the agents' context with insufficient validation, allowing malicious skills to influence agent behavior under that delegated authority. Yet, little is known about whether this trust model adequately constrains untrusted skill content before it reaches security-sensitive operations, or how frequently such trust violations arise in real-world agents. We present TrustProbe, a framework for uncovering unsafe chains of trust in skill-based LLM agents. First, TrustProbe analyzes agent source code to identify source-to-sink call paths from skill-controlled inputs to security-sensitive operations. Second, it generates semantically realistic this http URL seeds with injected canaries and evolves them through feedback-guided scheduling and mutation. Finally, it validates vulnerabilities using an oracle that confirms attacker-controlled flows and verifies observable harm. Across 11 open-source agents, eight with more than 10,000 GitHub stars, TrustProbe identifies 104 taint-style vulnerabilities. Validation on a large corpus of real-world skills collected from public hubs such as ClawHub further shows that 25.1% of skill-agent trials exercise the identified vulnerable paths, with payload injection successfully weaponizing 15 of the vulnerabilities. These results reveal a systematic trust failure in skill-based LLM agents: untrusted skill content can reach security-sensitive operations and exercise authority delegated by users to their agents.

---


### 177. [Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)

**<font color=#1a73e8>作者：</font>** Zhiya Tan, Jing Huang, Changtao Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional image forgery detection methods produce binary scores or pixel-level masks without interpretable evidence, while recent multimodal large language model (MLLM)-based approaches generate post-hoc explanations of predetermined classification results rather than reasoning from evidence. Inspired by the forensic workflow of human judicial experts, we propose Agentic Tool-Augmented Reasoning (ATAR), a framework integrating 22 specialized forensic tools across seven complementary domains to autonomously detect, localize, and explain image forgeries through multi-turn reasoning. A Dual-Stream Forensic Reasoning paradigm combines a high-level semantic anomaly path, which magnifies suspicious regions for fine-grained inspection, with a low-level forgery artifact path, which invokes forensic tools to extract objective evidence. We further introduce Forensics Curriculum Learning: during General Experience SFT, an automated teacher-student mentoring pipeline synthesizes multi-turn tool-usage reasoning trajectories; during Forensic Scene RL, a Tool Prior Curriculum guides early tool exploration and progressively transfers control to the agent, while a Structured Evidence Reward provides fine-grained process-level supervision. Experiments across IMDL, Deepfake detection, DMDL, and AIGC detection show that ATAR achieves 78.5% average image-level F1 on six zero-shot IMDL benchmarks, surpassing the strongest MLLM baseline by 11.8 percentage points, and remains competitive with specialized detectors on other tasks while producing substantially more faithful and grounded explanations.

---


### 178. [SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068)

**<font color=#1a73e8>作者：</font>** Jitai Hao, Quansheng Gu, Qiang Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose shared lifecycle contract lets each method control its KV representation and computation while coordinating state transitions with common serving infrastructure. SparseEngine supports 15 methods across four categories and enables cross-request state management through Chain Cache, which resumes KV-eviction methods from retained history, and controllable Prefix-Cache Pruning, which removes KV from selected history regions while preserving logical-prefix matching. While maintaining method quality, SparseEngine delivers over 10x higher throughput with KV eviction, over 2.5x faster decoding at matched concurrency than vLLM, and over 2x end-to-end speedup on agent benchmarks. The code is available at this https URL.

---


### 179. [CORE: Conflict-Oriented Reasoning Elimination for Verifiable Language-Model Search](https://arxiv.org/abs/2609.39069)

**<font color=#1a73e8>作者：</font>** Siyu Song, Rui Xu, Jia Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time reasoning systems often respond to failure by restarting or revising the latest step, even when an earlier decision caused the error. We introduce CORE, a search controller that requests a certified conflict core from a verifier, backjumps to the latest decision in that core, and caches the conflict to avoid repeating it. Under sound verification, finite branching and depth, and exhaustive proposals, the uncapped search is complete and never prunes a valid solution. On 2,000 planted graph-coloring instances with matched proposals and an exact verifier, CORE reduces median verifier calls by 39.8% at 30 variables and 35.0% at 36 variables relative to chronological repair; caching further improves on backjumping alone. Across five reasoning tasks, CORE achieves 75.9% mean success with Qwen2.5-7B-Instruct and 84.2% with Qwen3-8B, compared with 72.5% and 81.8% for Tree of Thoughts. It also uses fewer verifier calls and generated tokens on both backbones. These results show the value of using certified failure explanations to direct language-model search.

---


### 180. [LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models](https://arxiv.org/abs/2609.39071)

**<font color=#1a73e8>作者：</font>** Yida Cai, Xin Dai, Bingxiang He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal language models require reward signals that capture not only answer correctness but also the multidimensional quality of legal responses. Existing reward methods, however, often rely on coarse-grained holistic judgments, providing limited domain specificity and interpretability. We introduce LexReward, a taxonomy-driven framework for legal reward modeling. LexReward characterizes legal response quality along three complementary dimensions: Style, covering lexical and syntactic quality; Element, assessing legal subjects, facts, statutes, and decisions; and Chain, evaluating the order, completeness, correctness, and non-redundancy of legal reasoning. For each dimension, we develop rubrics that specify evaluation criteria and quality levels. The resulting rewards are used to construct pairwise preference data for Direct Preference Optimization (DPO) and reward-model training. Experiments show that the rubric-based rewards reliably distinguish legal responses of different quality and that DPO training on the preference data improves performance across all three dimensions. The learned reward models, LexRM, also support effective downstream optimization: each dimension-specific reward model improves policy performance in its corresponding dimension through reinforcement learning, without requiring reference answers at reward time. Dimension-wise analyses further support the effectiveness of the proposed taxonomy and reward construction.

---


### 181. [Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue](https://arxiv.org/abs/2609.39072)

**<font color=#1a73e8>作者：</font>** Yutong Hu, Jinho Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion recognition in conversation has been widely studied, but applying Large Language Models (LLMs) to continuous dimensional emotion evaluation in multimodal dialogue remains largely unexplored. We propose an LLM-based framework that performs discrete emotion recognition and Valence-Arousal-Dominance (VAD) dimensional evaluation on IEMOCAP, incorporating acoustic cues as natural language descriptions following the SpeechCueLLM approach. We evaluate six models spanning the LLaMA, GPT, and Qwen families under zero-shot prompting, few-shot prompting, and LoRA fine-tuning. LoRA fine-tuned LLaMA models substantially outperform prompt-engineered GPT models on both tasks despite GPT's larger scale, a gap we attribute to domain adaptation rather than model capacity. Our best model achieves a Valence CCC of 0.7822, a new state-of-the-art on IEMOCAP. Ablation studies confirm that textual audio descriptions meaningfully improve smaller models (+3.5 to 3.6 weighted F1) while contributing little for the largest model, suggesting audio cues are most valuable when linguistic capacity is limited. The performance asymmetry across VAD dimensions closely mirrors the annotator agreement hierarchy in IEMOCAP's own annotations.

---


### 182. [RAGScope: A Leakage-Controlled, Cost-Aware Evidence-Gating Protocol for RAG Hallucination Triage](https://arxiv.org/abs/2609.39075)

**<font color=#1a73e8>作者：</font>** Zeming Liu, Qibai Chen, Jingtao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems need inexpensive ways to route generated answers: accept low-risk outputs, review uncertain ones, and reserve strong verifiers for the expensive tail. We present RAGScope, a leakage-controlled protocol for evaluating local evidence gates that use only the task input, retrieved context, and answer text. The protocol combines context-grouped splits, fold-scoped preprocessing, group bootstrap intervals, deployment operating points, end-to-end runtime, and explicit source-shift stress tests. On three RAGTruth tasks, the enhanced gate RAGScope-E reaches 0.798 AUROC and 0.660 average precision (AP) in pooled grouped cross-validation. Its pooled AP exceeds ROUGE-L by 0.034 with a 95% context-group interval of [0.002, 0.064], although the AUROC gain is not significant and ROUGE-L remains stronger on data-to-text. At a top-10% review budget, RAGScope-E attains 0.748 precision; accepting the lowest-risk 50% yields 0.141 residual unfaithfulness. RAGScope-E runs in 6.22 ms/example on CPU, versus 145.75 and 223.07 ms/example for the tested DeBERTa-NLI and HHEM settings. A 14,900-example HaluBench stress test exposes the deployment boundary: an in-domain calibrated gate reaches 0.879 AUROC, but leave-source-out calibration averages only 0.466. Target-only calibration recovers to 0.675 AUROC with 100 labels per source and 0.685 with 200. Cheap evidence gates are therefore useful routing components, but learned calibration must be validated and adapted within the target domain.

---


### 183. [Multi-LLM Collaborative Alignment via Stackelberg Games](https://arxiv.org/abs/2609.39076)

**<font color=#1a73e8>作者：</font>** Christina Hahn, Shangbin Feng, Dean Light 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A pool of language models can collaborate and improve collectively by learning from one another's responses. These interactions depend on the instructions used during training. Existing methods typically sample instructions uniformly, even though their usefulness may change as the models improve: an instruction on which models' responses once differed in quality may later be answered equally well, while a previously difficult instruction may begin to provide a useful learning signal. We propose Stackelberg Alignment, a game-theory-inspired leader-follower framework that turns instruction selection into an adaptive curriculum. An EXP3 bandit acts as the leader, allocating a fixed sampling budget across instructions and updating its sampling distribution using a reward that combines instruction difficulty and response discriminability. The language models act as followers: they respond to the selected instructions, evaluate one another's responses, and learn from the resulting preference signals through DPO or GRPO. The framework uses Elo-style reputation-weighted peer judgment and reputation-based opponent matching to support reliable and competitive model interactions. Experiments across three heterogeneous model pools and 12 benchmarks spanning scientific discovery, reasoning, code, instruction following, and knowledge show that Stackelberg Alignment achieves the highest macro-average across three diverse model pools, outperforming the strongest training-time baseline by up to 7.4% and the best static inference baseline by 12-25%. Analysis confirms that the adaptive leader concentrates duels on the most informative instructions, and ablations show that both reputation-weighted judgment and reputation-based matching improve the effectiveness of multi-LLM evolution.

---


### 184. [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096)

**<font color=#1a73e8>作者：</font>** Zeqi Xiao, Qingle Liu, Kaiwen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion supports streaming generation and interactive control, but its KV cache grows with the generated history. Existing compression strategies discard history using fixed windows or select tokens through local attention and similarity signals, without directly measuring whether a chunk contributes information beyond the retained context. We introduce DeCoPrune, a training-free method that treats cache compression as a denoising-consistency problem. We find that tokens with larger discrepancies between intermediate clean predictions and final denoised values tend to carry visual evidence less predictable from the retained context. DeCoPrune uses this model-intrinsic signal to retain high-discrepancy tokens in the long-term cache while pruning low-discrepancy tokens. To evaluate information retention, we introduce CMBench, comprising 58 approximately one-minute generated or real-world context episodes and 116 Reappear or Revisit continuation tasks requiring recall of earlier events or objects. Experiments with LingBot World v2 show that DeCoPrune achieves a DINO score of 0.6701 on a 0-1 scale, with an 85.43% reduction in cumulative historical KV token counts and a 4.14-fold continuation-generation speedup over FullKV. Its head-specialized variant reaches 0.6783 at an 86.19% pruning ratio, approaching FullKV's 0.6803 score and exceeding the evaluated compression baselines at similar budgets. These results indicate that denoising consistency can support long-range information retention while reducing autoregressive inference cost. Our project homepage is this https URL. The code is available at this https URL, and the benchmark at this https URL.

---


### 185. [Beyond Prediction: Steering VLM Agents with Retrospective World Modeling](https://arxiv.org/abs/2609.39101)

**<font color=#1a73e8>作者：</font>** Yongjiang Liu, Jie Zhang, Haoyue Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equipping VLM agents with world modeling capabilities has shown strong potential for complex reasoning and long-horizon planning, while reducing the dependence of policy learning on costly real-world interactions. Existing methods mainly rely on prospective simulation to predict the consequences of candidate actions. However, this forward-only paradigm focuses on what will happen next and provides limited constraints for verifying whether an action is causally consistent with the observed state transition, which can lead to plausible-looking but physically incoherent behaviors. In this paper, we challenge the view of world modeling as only prospective prediction and introduce Retrospective World Modeling, a new agent learning paradigm that enables agents to reason backward by estimating the retrospective attribution distribution $P(\hat{a}{t}|s_t, s{t+1})$ for the action that most likely caused a given transition. Based on this capability, we formulate the Self-Consistency Reward (SCR), an intrinsic signal that measures the probabilistic consistency between the policy action and the retrospective explanation. Integrating SCR into reinforcement learning provides dense transition-level feedback and steers agents toward behaviors that are both task-effective and physically grounded. Extensive experiments across diverse agentic tasks show that our method substantially improves policy robustness and generalization over prospective-only world modeling baselines.

---


### 186. [False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents](https://arxiv.org/abs/2609.39102)

**<font color=#1a73e8>作者：</font>** Meijia Chen, Hao Li, Zheng Lu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-evolving search agents build their own training curricula by jointly optimizing a proposer that generates questions and a solver that answers them. This closed loop introduces a failure mode we call co-cheating: the proposer and solver increasingly agree on shared errors, so internal reward improves without a matching gain in external correctness. A post-hoc audit against source evidence shows co-cheating growing more severe over successive rounds of self-evolution, with pseudo-label correctness stagnating or declining even as the in-loop training signal improves. The most direct mitigation is to verify proposals before training: we introduce multi-sample verification (MSV), which queries the same model three times with the source and three times without it to decide task admission and replace unreliable pseudo-labels. MSV partially reduces false agreement but leaves substantial residual co-cheating and costs six extra labeler generations per candidate. These limitations motivate CrossFit, our main method: it partitions the proposer's source documents into groups A and B; questions generated from A are scored by an auxiliary solver trained only on B, and vice versa. The cross-fitted agreement determines proposer reward, so a same-source pseudo-label cannot be reproduced through the feedback solver, while the original solver's update rule is unchanged. Rerunning the loop with Qwen3.5-4B and Qwen3.5-9B, MSV reduces false-agreement mass from 6.1% to 5.7% and from 8.8% to 7.2%, whereas CrossFit reduces it to 3.0% and 3.7%. Replaying identical proposals with source-excluded feedback further reduces false agreement to 0.4% and 0.1%, isolating feedback ancestry from curriculum changes. Across seven downstream search benchmarks, CrossFit improves average performance over standard coupled self-evolution by 8.8 and 8.4 points and over Search-R1 by 8.7 and 7.8 points at 4B and 9B.

---


### 187. [MASCRDM: Multi-Agent System for Compliance Risk Detection and Mitigation in Training Process of Large Language Models](https://arxiv.org/abs/2609.39107)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Chuming Wei, Ruien Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been applied in various fields. However, ensuring compliance and safety of LLMs, such as avoiding discrimination and bias, still remains a challenge. Current efforts mainly focus on detecting and filtering inputs and outputs of the trained models, rather than studying the intrinsic architecture of the models in real-time. To tackle this challenge, we analyze the LLMs training process and discover two critical issues: 1) Most of the existing methods are predominantly static in their approach to detection and filtering, achieving only localized optimizations without systematically enhancing the compliance of LLMs. 2) Another issue with existing approaches is the lack of real-time risk detection and mitigation across the full training process, which leads to limited flexibility. Motivated by these, we propose MASCRDM (Multi-Agent System for Compliance Risk Detection and Mitigation) during the LLM training process. Firstly, we develop a set of compliance rules based on existing Artificial Intelligence (AI) laws and a compliance-specific LLM with the instruction of compliance law experts. Then, we deconstruct LLMs into several components and identify key nodes based on the compliance knowledge graph. During LLMs training, we implement our multiple agents in the whole process, giving compliance risk alerts and suggestions for LLM developers. Experiments on discrimination and bias benchmark demonstrate that our multi-agent system can effectively improve the compliance while maintaining reasonable semantic performance. The results indicate that our method provides an executable path for mitigating compliance risk from within the LLMs systematically.

---


### 188. [CamAgent: An LLM-Agent Framework for Multi-Species Camera-Trap Workflows](https://arxiv.org/abs/2609.39112)

**<font color=#1a73e8>作者：</font>** Yutong Deng, Qi Song, Xi Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera traps accumulated vast, multidimensional data for wildlife monitoring, yet translating raw media archives into meaningful ecological insights remains highly fragmented. Current research workflows require laboriously stitching together disparate analysis tools and scripts, creating steep programming hurdles and complicating end-to-end spatiotemporal analyses. To overcome this fragmentation, we present CamAgent, an autonomous Large Language Model (LLM) agent framework that integrates camera-trap analytical workflows into a unified intelligent ecosystem. CamAgent interprets natural-language ecological intent, schedules computational routing, and executes specialized tools spanning computer-vision perception (e.g., SpeciesNet), CamtrapDP-compatible data management, detection-corrected occupancy modeling, temporal activity analysis, and species co-occurrence networks. The framework automates multi-stage analytical pipelines while maintaining essential data-quality controls and analytical conventions. Consequently, CamAgent significantly reduces manual programming overhead for conservationists, establishing a transparent, scalable, and fully integrated paradigm for camera-trap ecology. Our project is available at this https URL.

---


### 189. [The Row Normalization Puzzle in Muon](https://arxiv.org/abs/2609.39114)

**<font color=#1a73e8>作者：</font>** Jiayu Zhang, Tianyi Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper examines how row-wise renormalization affects Muon, focusing on the gap between NorMuon's worst-case guarantees and its practical performance (Li et al.). Despite its growing adoption and promising performance in large language model (LLM) pretraining, NorMuon's worst-case guarantees remain poorly understood. One fundamental question is: Does row normalization yield provable convergence gains, potentially through its interaction with approximate polar computation and exponential moving-average momentum? Our results show that row normalization introduces a dimension-dependent factor in the worst-case iteration complexity under the operator-norm geometry, which persists even with exact polar computation and any fixed momentum parameters. Indeed, we establish an algorithm-dependent lower bound and a matching upper bound in deterministic settings, and extend our upper bound analysis to stochastic settings. Both upper-bound analyses allow approximate polar computation. Experiments show that NorMuon is slower than Muon on synthetic problems inspired by our worst-case construction, yet outperforms Muon in LLM pretraining. These findings sharpen the puzzle of why row normalization helps in practice and complement the recent findings of Dewulf et al.

---


### 190. [SteerProbe: Learning to Bypass Safety Steering in Vision-Language Models](https://arxiv.org/abs/2609.39117)

**<font color=#1a73e8>作者：</font>** Xinwei Zhang, Aoting Hu, Hangcheng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Activation steering offers an inference-time defense for vision--language models (VLMs) by modifying intermediate representations without updating backbone parameters. However, protection on benchmark inputs may not persist across alternative expressions of the same harmful request. We investigate this gap using fixed textual, visual, and joint reformulations designed to preserve the underlying intent, and find that these changes can bypass representative steering defenses. A complementary local analysis provides a sufficient condition under which a reformulation can cross a surrogate safety margin despite any admissible change in the local steering correction. We then introduce SteerProbe, an output-only black-box attack that learns to select effective reformulations for unseen requests from a shared calibration budget. Across three VLM backbones, two benchmarks, and three steering defenses, SteerProbe increases Harmful Rate in all defended settings using 500 total calibration queries per endpoint and benchmark, raising the average from 7.43% to 18.36%. These findings highlight that robustness on original benchmark inputs is insufficient to characterize the safety of steering defenses and motivate reformulation robustness as an important evaluation dimension. They further motivate steering mechanisms that preserve safety across intent-preserving multimodal variations while maintaining benign utility.

---


### 191. [Diagnosing On-Policy Self-Distillation for Reasoning Language Models](https://arxiv.org/abs/2609.39118)

**<font color=#1a73e8>作者：</font>** Yang Li, Gongle Xue, Yuheng Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has attracted growing interest as a promising approach to improve the reasoning ability of language models. Without external rewards nor a separate stronger teacher, the self-teacher with privileged information could provide dense signals on student's trajectories. However, its behavior in language reasoning remains unclear, with reported outcomes ranging from modest gains to behavioral collapse. In this work, we diagnose OPSD for mathematical reasoning across models spanning 0.6B--8B parameters. We conduct controlled experiments and token-level analyses to fully delve into OPSD. We point out that teacher's signal is shaped by reasoning-mode alignment and the complete teacher prefix, rather than by privileged semantics alone. OPSD improves reasoning only in narrow compatibility regimes. Otherwise, it produces ineffective length growth, stable degradation, or behavioral collapse. Token-level analysis shows that teacher's signal is not stable and does not predict downstream performance. Based on these results, we argue that OPSD is a sensitive algorithm rather than a generally reliable reasoning-improvement post-training method.

---


### 192. [Is Better Teacher Supervision Enough? Unlocking Student-side Learning in Multimodal On-Policy Distillation](https://arxiv.org/abs/2609.39120)

**<font color=#1a73e8>作者：</font>** Siyuan Liu, Kanghui Tian, Yue Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves reasoning by providing token-level supervision from a teacher on a student's own trajectories. Existing methods primarily focus on enhancing this teacher-side guidance (e.g., by enriching teacher inputs and refining teacher feedback), yet we find that limited student perception is another critical bottleneck in multimodal OPD. By providing oracle visual facts, the performance of OPD-trained students can still be substantially improved for both weak and strong teachers. To address this bottleneck, we propose S-OPD, a simple multimodal on-policy distillation framework that explicitly strengthens student perceptual learning through two objectives. Specifically, Teacher-calibrated Policy Contrast separates student policies under original and masked images with teacher-based token-level gating, strengthening the student's reliance on visual evidence during reasoning. Policy Agreement aligns student policies under original and noise-perturbed images, further improving perceptual robustness to visual noise. Notably, our method can be seamlessly plugged into existing OPD frameworks, requiring no additional data annotations, model parameters or inference operations. Extensive experiments on eight benchmarks across student scales and distillation paradigms demonstrate consistent performance improvements, with gains of up to 4.25 points on LogicVista. When combined with existing teacher-side supervision methods, our method can yield further gains. Code is available at this https URL.

---


### 193. [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/abs/2609.39131)

**<font color=#1a73e8>作者：</font>** Zack Yu, Chloe Wong, Coleman Hooper 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) serving requires substantial memory to store model weights and KV caches. As models grow larger and contexts become longer, memory capacity and bandwidth increasingly become bottlenecks for serving performance. Agentic workloads compound this pressure through repeated interactions over growing contexts, making it increasingly important to retain KV state for reuse. High-bandwidth flash (HBF) offers a way to expand accelerator memory capacity for large language model (LLM) serving, but its access costs and limited write endurance complicate its use. We evaluate HBF for high-throughput agentic serving across system design and scheduling choices to understand when additional capacity improves serving performance and energy efficiency. We introduce an HBM-HBF-host hierarchical storage system and buffered cache-aware scheduling, and use trace-driven simulations to analyze their effects on performance, energy consumption, and HBF write lifetime. Across the evaluated workloads, the fastest HBF-augmented systems reduce completion time by 36.1-87.0% relative to HBM-only systems. Modeled energy savings reach 55.8%, although HBF increases energy consumption on some light workloads. Buffered cache-aware scheduling extends estimated HBF write lifetime from 4.77 to 14.82 years in the evaluated configuration. These results demonstrate the importance of coordinating data placement and scheduling to improve serving efficiency while sustaining a practical HBF write lifetime.

---


### 194. [Feature-Aware Token Attack for Compression-Triggered Stealthy Failures in Large Vision-Language Models](https://arxiv.org/abs/2609.39134)

**<font color=#1a73e8>作者：</font>** Shilinlu Yan, Bowen Chen, Yuechen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-token compression improves the efficiency of large vision-language models, but can expose failures that full-token evaluation misses. We study adversarial images that preserve full-token correctness yet induce errors after compression, even when both inference paths succeed on the clean image. Creating such failures is challenging because perturbing token importance can also damage the visual content needed for full-token inference. We propose Feature-Aware Token Attack (FATA), which couples attention suppression with cosine-based feature preservation on a fixed set of salient clean-image tokens. In the primary LLaVA-1.5-7B setting, FATA uses only vision-encoder gradients, without access to the deployed compressor, token budget, or downstream task. Across four visually dependent task subsets and four compressors under a controlled reconstruction protocol, FATA achieves SR = 96.3% full-token accuracy retention and CBR = 22.1% conditional blinding, compared with 89.8% and 15.7% for CAA. Ablations support the role of both objectives in balancing compressed-path failure against full-token preservation. FATA also has the lowest measured detection rate among four attacks across three evaluated detectors at a 5% false-positive rate. These findings motivate assessing adversarial robustness jointly across full-token and compressed inference.

---


### 195. [Asking the World: Generalist Physical Reasoning through Agentic World Modeling and Probing](https://arxiv.org/abs/2609.39135)

**<font color=#1a73e8>作者：</font>** Shenxiang Zeng, Chen Yang, Peiyao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical reasoning from video requires inferring latent physical properties and dynamics beyond direct observation. Direct VLM inference remains unreliable on complex physical tasks without explicit modeling and validation, while predefined tool pipelines rely on task- and domain-specific priors that limit generalization across materials, dynamics, and reasoning tasks. We introduce Asking the World (ATW), a generalist agent that constructs and interrogates task-relevant executable worlds through two adaptive stages: World Modeling calibrates a world from video, while World Probing queries, simulates, and intervenes on it to obtain question-relevant evidence. Rather than prescribing the operations in either stage, ATW determines how to model and probe according to the scene and question. We develop PolyWorld Engine, a lightweight and highly programmable Warp-based multiphysics simulator for constructing and probing worlds with rigid bodies, soft bodies, cloth, ropes, fluids, and their coupled interactions. CEM-based system identification recovers task-relevant dynamics during World Modeling. The resulting world becomes an active workspace for question-directed physical experiments rather than a predetermined downstream tool. We evaluate ATW on CLEVRER, ContPhy, and three real-world scenarios. Using Gemini-3-Flash as its base VLM, ATW achieves 80.82% overall per-question accuracy on CLEVRER, improving direct Gemini-3-Flash by 46.50 points, GPT-5.5 by 13.58 points, and PhysMind by 8.27 points. On ContPhy, it reaches 70.56% overall accuracy, surpassing Gemini-3-Flash by 28.10 points and GPT-5.5 by 3.53 points. Across the three real-world scenarios, ATW achieves 71.67% accuracy, 28.33 points above GPT-5.5. These results establish agentic world modeling and probing as an effective, execution-grounded approach to generalist physical reasoning.

---


### 196. [ID Balancing: Stable Training of Extremely Sparse MoE via PID-Based Load Control](https://arxiv.org/abs/2609.39137)

**<font color=#1a73e8>作者：</font>** Peng Jin, Zihan Qiu, Zekun Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling Large Language Models (LLMs) via Mixture-of-Experts (MoE) enables massive parameter growth with nearly constant per-token computation. However, further scaling the parameter count requires increasingly sparse routing, where expert load imbalance becomes more severe. This imbalance reduces parameter utilization and training efficiency, and can undermine training stability, becoming a bottleneck to reliable scaling. In this work, we unify two representative auxiliary-loss-free methods as incomplete Proportional-Integral-Derivative (PID) controllers: DeepSeek's loss-free method acts as a fixed-step integral controller, while Kimi K3's Quantile Balancing functions as a generalized proportional controller. Building on this control perspective, we propose ID Balancing, an Integral-Derivative controller. It scales its integral term with load error and activates its derivative term only when imbalance worsens, enabling stronger corrections for large or worsening errors and smaller updates near balance. Evaluated across Top-$10$, Top-$5$, and Top-$3$ routing over $768$ experts, ID Balancing reduces worst-case backbone MaxVio and training-average backbone MinVio by over $50\%$ and $12\%$, respectively, relative to the best baselines in the Top-$3$ setting. When the total parameter count increases from $18.9$B to $69.9$B (Top-$10$-of-$768$), ID Balancing's worst-case backbone MaxVio remains nearly unchanged and is approximately $89.6\%$ lower than that of the auxiliary-loss baseline. ID Balancing also maintains competitive language-modeling and downstream performance. The advantages of ID Balancing grow as sparsity increases, making it a promising solution for scaling larger, sparser MoE models.

---


### 197. [BELIEFRAG: Making Adaptive RAG State-Aware under Evolving Evidence](https://arxiv.org/abs/2609.39139)

**<font color=#1a73e8>作者：</font>** Hongji Pu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive RAG uses signals such as confidence, relevance, support, and retrieval quality to decide when to search or correct evidence. In multi-step retrieval, however, these local signals must be combined into a persistent view of what the current evidence supports, what remains missing, and which action should follow. Existing methods often use such signals as separate triggers, making it difficult to preserve a coherent evidence state across a trajectory; we call this problem evidence-state fragmentation. We introduce BELIEFRAG, a closed-loop controller that updates an explicit state over sufficiency, reliability, conflict, uncertainty, evidence gaps, and acquisition cost, then chooses among retrieval, query rewriting, verification, answering, stopping, and abstention. Across six QA benchmarks with gpt-oss-120b, BELIEFRAG reaches mean token F1 0.572 with 3.89k tokens per question, outperforming fixed iterative retrieval (0.555 F1) while using 39% fewer tokens. The same quality-cost pattern transfers to Qwen3-32B, where BELIEFRAG reaches 0.552 F1 versus 0.523 for iterative retrieval while using 35% fewer tokens. Analysis shows that the main gains come from corrective re-retrieval rather than pruning alone, while several belief dimensions are redundant and calibrated answerability plays the strongest operational role. Calibration improves threshold stability across related evidence sources, although source shift can still invalidate the same decision signal.

---


### 198. [Schema: Discovering Unknown Environments via Agentic Program Induction](https://arxiv.org/abs/2609.39140)

**<font color=#1a73e8>作者：</font>** Guanning Zeng, Jiani Wang, Wenjie Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning to complete tasks in unfamiliar environments with unknown rules remains a key challenge for LLM agents. Current LLM agents often record their discoveries in prose, which may not provide a compact, explicit account of how the environment works. Inspired by how scientists organize observations into testable, predictive theories, we introduce Schema, an agent harness that organizes learning and action through interactive program induction. The LLM agent decides what to investigate and how to act, expressing its evolving understanding of the environment as executable programs. The harness consists of a persistent program workspace and a small set of interfaces for checking these programs against the interaction history, planning within them, and executing plans under step-by-step verification. Schema raises ARC-AGI-3 RHAE from 58.7% to 99.2% with the same base model, solves 100% of the public DiG-bench games, and reaches the median performance of the top-50 human players on MazeBench. Extensive analysis shows the effectiveness of Schema in unknown mechanism discovery, and ablations confirm the contribution of each component.

---


### 199. [When Can Text Replace Vision? Structural Bottlenecks in Diagram Reasoning](https://arxiv.org/abs/2609.39142)

**<font color=#1a73e8>作者：</font>** Yunbei Zhang, Janet Wang, Jihun Hamm 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can structured text replace vision for diagram reasoning? A wrong answer after textualization can arise because the representation omits information the question needs, or because the solver fails to use information that is present. We introduce a diagnostic protocol to distinguish these explanations. Using the same solver model and generation settings, we compare three input conditions: the original image, question-blind structure extracted by a vision-language model, or gold structure derived from the diagram source. Validity-triggered recovery tests truncation and schema failure, question-relevant fidelity measures preservation of answer-critical structure, and matched edge interventions test the effect of error location. On a reserved holdout of 240 public FlowGen diagrams, evaluated under a frozen protocol, gold structure reaches 87% accuracy while direct vision and learned text both remain below 30%. The aggregate comparison includes source-derived relation labels that may not be printed in the image and uses different learned and gold graph encodings, so it does not isolate extraction error alone. Retrying only invalid extractions makes nearly every public representation schema-valid yet leaves accuracy essentially unchanged. The public learned-text deficit relative to gold more than doubles with structural difficulty. Question-relevant topology predicts correctness better than whole-graph topology. In an exposed intervention study, a single answer-relevant edge edit reduces the primary solver's original-answer accuracy to near zero, while matched irrelevant edits largely preserve it. Supplied structure requires fewer solving tokens than vision, but learned acquisition removes this advantage at single use. These comparisons motivate evaluating acquired text by the answer-relevant evidence it preserves and by the solver's ability to use that representation.

---


### 200. [MADBench: Benchmarking the Security of Multi-Agent Debate](https://arxiv.org/abs/2609.39146)

**<font color=#1a73e8>作者：</font>** Yuwan Liu, Jiaming Zhang, Yue Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) can improve large language model (LLM) reasoning by allowing multiple agents to exchange and critique their answers to the same task. However, the interactions that enable agents to correct mistakes can also spread adversarial errors and steer the agents toward an incorrect answer. Although some efforts have been made to examine particular attack types on MAD, systematic evaluation of MAD under diverse attacks remains limited. A central question is whether debate mitigates adversarial influence or amplifies it.
In this paper, we present MADBench, a benchmark for evaluating the security of MAD. We organize attacks into a layered taxonomy following the MAD workflow, incorporating both established attacks and new strategies tailored to debate. We evaluate six attack families over 356 source tasks and 3,958 test cases, examining their effects on the final answer and the propagation of adversarial influence. Our results show that, under attacks, MAD does not necessarily improve LLM reasoning. Compared with a single-agent baseline, MAD can mitigate attacks on answer accuracy in question-answering tasks while amplifying unauthorized reads or writes in both question-answering and workspace tasks. Moreover, even when three out of five agents collude, the attack changes the final answer from correct to wrong on only 28.30\% of tasks answered correctly without attack, while only 3.26\% of initially correct honest agents switch to wrong answers during debate.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
