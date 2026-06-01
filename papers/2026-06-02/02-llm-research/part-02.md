# 🧠 大模型相关研究 | 2026年06月02日

> 本类共 **168** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-168](./part-04.md)

---

### 51. [Neuron-Level Interventions for Gendered and Gender-Neutral Generation in Language Models](https://arxiv.org/abs/2605.30717)

**<font color=#1a73e8>作者：</font>** Zhiwen You, Nafiseh Nikeghbal, Jana Diesner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) can produce gendered language and stereotypes even when given neutral prompts. Most prior work on gender bias in LMs primarily examines gender through a binary lens (feminine vs. masculine), with limited attention to gender-neutral forms, such as they/them pronouns or neutrally phrased job titles. How gender-related signals are encoded in the internal representations of LMs remains an open question. In this work, we study gender-specific neurons in LMs across three categories: feminine, masculine, and gender-neutral. We propose a neuron-level intervention method to identify neurons that are strongly tied to each gender category. We then test these neurons through controlled generation, showing that activating or masking gender-related neurons can steer a sentence toward a target gender form while preserving its original meaning. To evaluate the effectiveness of our gender-intervention approach, we curate two datasets with controlled sentences labeled across all three gender categories and validate the data quality through human evaluation. Experiments on two open-source LMs show that gender-specific neurons are not evenly distributed across model layers; instead, they concentrate heavily in the earliest layers with smaller contributions from later layers. Compared to existing methods, our method achieves more precise gender control, with less leakage into non-target gender categories and stable output quality through two evaluation criteria. Overall, our work examines how gender is encoded in LMs and provides a simple yet effective approach toward controlled gender intervention for both neuron intervention evaluation and gender bias mitigation. Code and datasets are available at: this https URL

---


### 52. [When are LLMs Sufficient Policy Optimizers for Sequential RL Tasks?](https://arxiv.org/abs/2605.30719)

**<font color=#1a73e8>作者：</font>** Stephane Hatgis-Kessell, Emma Brunskill  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study when large language models (LLMs) can serve as effective black-box policy optimizers for reinforcement learning (RL) tasks, i.e., when can we replace classical RL algorithms with an LLM? We explore this question by introducing Prompted Policy Optimization (PromptPO), an iterative method that prompts an LLM with Python descriptions of the state space, action space, and reward function, then has it generate and refine executable policies based on rollout feedback. Across hard exploration environments, Meta-World robotics tasks, and several real-world control problems, PromptPO often matches or exceeds the performance of standard RL baselines while using substantially fewer environment interactions. To maximize expected return, and without further explicit prompting, the policies PromptPO outputs range from tuned proportional controllers or rule-based plans to policies that run planning algorithms like value iteration. Our results demonstrate that LLM-based policy optimization is sufficient when the LLM can leverage prior knowledge about the environment or optimization strategy. PromptPO underperforms standard RL baselines in MuJoCo domains. This demonstrates possible limitations of LLM-based policy optimization to settings that requiring fine-grained continuous control.

---


### 53. [Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents](https://arxiv.org/abs/2605.30723)

**<font color=#1a73e8>作者：</font>** Jianxiang Yu, Jiapeng Zhu, Bochen Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly retrieve externally curated skills-procedural instructions retrieved at decision time-to improve performance on long-horizon interactive tasks. Existing skill libraries are typically treated as model-agnostic, reusing the same skill formulations across backbones with substantially different capacities and behaviors. However, our controlled experiments across multiple model scales show that skill effectiveness is strongly model-dependent: a skill that benefits one backbone can harm another. Motivated by this observation, we propose MASA Model-Aware Skill Alignment, a framework that adapts skills to each target backbone without modifying agent weights. MASA operates in two stages: (1) a hierarchical skill evolution pipeline that iteratively rewrites general and task-specific skills using hill climbing and UCB-driven tree search, guided by environment feedback and model capability profiles; and (2) a lightweight model-conditioned skill rewriter trained on evolution trajectories to reproduce the adaptation in a single forward pass. Experiments across three interactive environments and four backbones show that MASA consistently achieves the best overall performance, with gains of up to 25.8 points over the strongest baseline. The learned rewriter further generalizes to unseen tasks and environments without additional search, consistently outperforming a much larger teacher LLM at a fraction of the inference cost.

---


### 54. [OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning](https://arxiv.org/abs/2605.30736)

**<font color=#1a73e8>作者：</font>** Zhenghua Bao, Fengya Tian, Chris Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models, each with distinct capabilities and inference costs, raises a practical deployment question: given an incoming request, which model should handle it? We present OrcaRouter, a production-oriented LLM router that combines a LinUCB-based contextual bandit over lexical and sentence-embedding features with a hybrid offline-online learning protocol. Offline, OrcaRouter obtains full-information feedback by evaluating each candidate model on a curated set of routing prompts, yielding a reward matrix used to fit one ridge regressor per arm. At deployment time, it initializes from these parameters and can optionally continue learning from bandit feedback, updating only the selected model's arm after observing its reward. At the time of our RouterArena submission (May 20, 2026), OrcaRouter-Adaptive ranked second on the public RouterArena leaderboard with an arena score of 72.08, achieving 75.54% accuracy at a cost of USD 1.00 per 1,000 queries.

---


### 55. [MAVEN: Improving Generalization in Agentic Tool Calling](https://arxiv.org/abs/2605.30738)

**<font color=#1a73e8>作者：</font>** Omkar Ghugarkar, Vishvesh Bhat, Muhammad Ahmed Mohsin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generalization across agentic tool-calling environments remains a central challenge for reliable agentic reasoning systems. Although large language models achieve strong results on individual benchmarks, their ability to compose reasoning strategies, preserve intermediate states, and coordinate tools across domains remains underexplored. We present MAVEN (Modular Agentic Verification and Execution Network), a lightweight symbolic reasoning scaffold for structured decomposition, adaptive tool orchestration, and intermediate verification. We evaluate MAVEN across established tool-calling benchmarks, including BFCL v3, TauBench, Tau2Bench, AceBench, and introduce MAVEN-Bench, a stress-test benchmark for multi-step mathematical and physical reasoning with explicit verification and adversarial task composition. MAVEN-Bench exposes a substantial gap between partial reasoning quality and end-to-end task success; in direct MAVEN-Bench runs, MAVEN improves its GPT-OSS-120b base model from 48% to 71% accuracy without additional training. It also remains competitive with frontier proprietary baselines while using an open-weight backbone with an estimated cost ratio of roughly 1/10, suggesting that lightweight verification-centered scaffolds can strengthen compositional reasoning and motivate more process-aware evaluation of agents in the wild.

---


### 56. [Immuno-VLM: Immunizing Large Vision-Language Models via Generative Semantic Antibodies for Open-World Trustworthiness](https://arxiv.org/abs/2605.30745)

**<font color=#1a73e8>作者：</font>** Xiang Fang, Wanlong Fang, Wei Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models have achieved unprecedented success in zero-shot recognition by aligning visual features with broad semantic concepts. However, this semantic abstraction creates a critical vulnerability in open-world deployment: the ``Hubris of Semantics'', where models force-fit unknown anomalies into known categories with high confidence due to the lack of explicit negative knowledge. To address this \textit{Open-World Trustworthiness Paradox}, we propose \textbf{Immuno-VLM}, a bio-inspired framework that adapts the biological principle of \textbf{Immunological Negative Selection} to high-dimensional latent spaces. Departing from traditional Open-Set Recognition methods that rely on passive density estimation or inefficient pixel-space outlier generation, Immuno-VLM leverages the generative reasoning of Large Language Models to actively hallucinate ``Semantic Antibodies'', textual descriptions of near-distribution outliers (e.g., look-alikes, contextual anomalies) that effectively bound the decision space of known this http URL experiments on ImageNet-1K and four challenging OOD benchmarks reveal that Immuno-VLM establishes a new state-of-the-art.

---


### 57. [SLAP: The Semantic Least Action Principle for Variational Video-Language Modeling](https://arxiv.org/abs/2605.30750)

**<font color=#1a73e8>作者：</font>** Xiang Fang, Wanlong Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of Large Video-Language Models (LVLMs), the computational necessity of sparse frame sampling creates a fundamental ``temporal gap'', rendering models blind to critical causal transitions. Existing solutions relying on generative hallucination (e.g., latent diffusion) or autoregressive extrapolation often fail to maintain semantic consistency over long horizons, suffering from object vanishing and energetic instability. We propose a paradigm shift from probabilistic generation to variational mechanics with the \textbf{Semantic Least Action Principle (SLAP)}. Drawing a rigorous isomorphism between classical mechanics and semantic dynamics, we model the latent video trajectory as a path on a Riemannian manifold governed by a Semantic Lagrangian. By formulating the interpolation task as a Boundary Value Problem (BVP) solved via the discrete Euler-Lagrange equations, SLAP naturally enforces object persistence without pixel-level rendering. Extensive experiments show the effectiveness of our proposed SLAP.

---


### 58. [Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation](https://arxiv.org/abs/2605.30753)

**<font color=#1a73e8>作者：</font>** Zekai Li, Ji Liu, Yiqing Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion-based large language models (dLLMs) support parallel text generation via iterative denoising, yet inference remains latency-heavy because many steps are spent on redundant refinement and repeated remasking of tokens whose final values are already determined. Prior acceleration methods mainly depend on step-local confidence heuristics or fixed schedules, which are sensitive to prompt and task variation and ignore strong positional effects within a sequence. We cast diffusion decoding as a dynamic control problem and show that token-wise denoising trajectories provide the key signal for reliable control. We propose a trace-aware decoding framework with two components. First, Temporal-Spatial Parallel Decoding (TSPD) uses a lightweight temporalspatial controller that consumes per-token trajectory features, including confidence, entropy, and momentum, together with token position, to decide when a token has converged and can be safely fixed. Second, we introduce Confidence Extrapolation (CE), a training-free state-space module that forecasts future logit trends with uncertainty to support proactive decisions, including safe look-ahead and targeted stabilization when trajectories are oscillatory or underconfident. Together, TSPD and CE reduce unnecessary denoising iterations while preserving output quality, and they compose cleanly with system optimizations such as KV caching.

---


### 59. [MechVQA: Benchmarking and Enhancing Multimodal LLMs on Comprehensive Mechanical Drawing Understanding](https://arxiv.org/abs/2605.30794)

**<font color=#1a73e8>作者：</font>** Qian Kou, Xiaofeng Shi, Yulin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated significant achievements in general visual question answering (VQA) tasks. However, they remain brittle on mechanical engineering drawings, where high annotation density and weak domain knowledge, compounded by unreliable spatial relation reasoning under strict projection rules and geometric constraints, make decisive cues easy to miss and frequently lead to wrong answers. To bridge this gap, we introduce the first comprehensive mechanical drawing understanding dataset, MechVQA, created through a semi-automated construction and quality-control pipeline. MechVQA contains 3.3k high-density pictures with 21K question-answer pairs, spanning 10 different fine-grained tasks across three capability levels: Recognition, Reasoning, and Judging, providing a testbed to evaluate and improve MLLM understanding on real-world mechanical drawings. On top of MechVQA, we then develop the MechVL model through a multi-stage training paradigm, building a strong domain-specialized baseline. Extensive experimental results demonstrate that MechVL outperforms the strongest closed-source baseline by 7.57 percentage points on the MechVQA total score, significantly enhancing mechanical drawing understanding ability and providing a reusable foundation for deploying MLLMs in mechanical design and inspection scenarios.

---


### 60. [Design and Evaluation of Multi-Agent AI Oracle Systems for Prediction Market Resolution](https://arxiv.org/abs/2605.30802)

**<font color=#1a73e8>作者：</font>** Tarun Kota  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Prediction markets aggregate collective intelligence to forecast uncertain events, but their utility depends on reliable outcome resolution. Existing oracle systems tradeoff fast but brittle automation against accurate but costly human arbitration. Single-LLM oracles achieve meaningful accuracy but inherit all failure modes of their underlying model with no self-correction mechanism. We evaluate whether multi-agent LLM architectures can improve oracle resolution accuracy over single-model baselines. We compare independent aggregation and deliberative consensus against single-LLM baselines (GPT-5 Nano, DeepSeek V3, and Llama-3.3-70B) on 1,189 resolved prediction market questions from KalshiBench. All agents share a common evidence layer through Exa, with retrieval filtered by publication date to isolate reasoning from retrieval quality. Independent aggregation with confidence-weighted voting achieves the highest accuracy at 83.43 percent, outperforming the best individual model by 1.01 percentage points. Deliberative consensus degrades accuracy to approximately 76 percent, below every single-model baseline, attributed to error propagation during debate where confidently wrong models flip correct ones. Error correlations across models (0.529-0.689) explain why aggregation gains fall short of the theoretical Condorcet ceiling, placing a fundamental limit on ensemble approaches. Many questions resist correction by any multi-agent architecture, motivating escalation to human arbitration. We propose routing criteria for hybrid AI-human oracle systems: auto-resolving only unanimous, high-confidence questions yields 97.87 percent accuracy on 47 percent of the dataset, with inter-agent disagreement flagging the remainder for human review.

---


### 61. [PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges](https://arxiv.org/abs/2605.30803)

**<font color=#1a73e8>作者：</font>** Swastik Roy, Rajkumar Pujari, Tharindu Kumarage 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are increasingly used to evaluate open-ended responses, but their scores depend strongly on the rubrics that condition them. A vague rubric asking for a response to be ``helpful and factual'' can reward polished answers that invent facts or violate user intent. We treat reusable rubrics as measurement specifications: changing the rubric changes the response quality measurement induced by a fixed judge. We introduce PReMISE, a framework that, given pairwise human-preference data, (i) discovers a policy-level rubric set, and (ii) audits any rubric set under LLM-judge use along four axes: structural adequacy, reliability, preference fit, and adversarial robustness. Across rubric sources no raw source is simultaneously reliable, preference-predictive, and adversarially robust; and high inter-rater agreement does not imply low exploitability. PReMISE is the only rubric source to score non-trivially on applicability, specificity, and effective dimensionality simultaneously. We contribute two audit-targeted repair operations: preference-rank selection raises judge accuracy on paired responses from $65.0\%$ to $68.6\%$, competitive with the strongest rubric-discovery baselines and leading on two of three judges in our cross-judge sweep; reliability-constrained refinement reduces the rate at which exploit responses receive high scores from $46.4\%$ to $36.0\%$ with little change in inter-judge agreement ($\alpha{=}.531\to.519$).

---


### 62. [Anchoring LLM Gender Bias to Human Baselines: A Cross-Lingual Audit](https://arxiv.org/abs/2605.30804)

**<font color=#1a73e8>作者：</font>** Jiwoo Choi, Seonwoo Ahn, Tongxin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We audit six large language models (LLMs) for gender stereotyping across English, Korean, Chinese, and Japanese. Three were developed primarily for English-language use (Claude, GPT, Gemini) and three for East Asian use (DeepSeek, Syn-Pro, HyperCLOVA X). We adopt the HEXACO-100 personality inventory and anchor each model against a cross-cultural human dataset spanning 48 countries to ask not whether LLMs are biased, but how far their gender attributions drift from the populations they are deployed among. Our findings show that their stereotyping spans a range roughly 2.5 times wider than the entire cross-country range found in humans, and the effect can compound across languages. One English-centric model, prompted in Korean, reached 5 times the local baseline, even when the prompt stated the candidate had already been hired, which often dampens human stereotyping. To characterize such behaviors without ranking them, we introduce a four-pattern framework -- concordance, suppression, reorganization, and amplification -- across 24 (model x language) cells. Item-level analysis reveals that translation does not just rescale stereotypes, but changes the attributes tied to it, hiding significant rearrangement under the surface while appearing well-calibrated. Our results ultimately suggest that no single debiasing pipeline is likely to address bias evenly across linguistic boundaries.

---


### 63. [Cross-Layer Subspace Coupling for LLM Compression: A Unifying Framework and Its Empirical Limits](https://arxiv.org/abs/2605.30836)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent SVD based compression methods for large language models like SVD LLM and Basis Sharing can be unified under one optimization problem. While mathematical proofs and tests on Pythia models show this unified approach improves weight reconstruction error by up to 46% percent it fails in practical tasks. Downstream metrics like perplexity and accuracy severely degrade compared to standard per layer SVD LLM. The authors explain this failure mechanistically. Although the bundle method mathematically couples adjacent layers the transformer residual stream actually decouples them during forward passes. Thus per layer optimality matters more than joint cross layer optimization. The paper concludes that weight space reconstruction is a flawed objective for cross layer compression and future methods must focus on per layer activation reconstruction instead.

---


### 64. [COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents](https://arxiv.org/abs/2605.30838)

**<font color=#1a73e8>作者：</font>** Wenkai Shen, Pengyang Zhou, Jiahe Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered search agents enable multi-step reasoning and tool use. However, these capabilities introduce retrieval-induced safety degradation, as harmful intents may decompose into seemingly innocuous sub-queries that lead to unsafe outcomes. Existing alignment methods struggle to capture sparse safety signals and fail to supervise diverse violations across multi-step interactions. We propose COMPASS, a Cognitive MCTS-Guided Process Alignment framework designed to achieve robust safety alignment throughout the agent workflow while preserving general utility. COMPASS integrates cognitive tree exploration (CTE) to efficiently synthesize stealthy attack trajectories, and introspective step-wise alignment (ISA) to isolate risky intermediate actions for fine-grained process supervision. Empirical results show that COMPASS achieves a favorable safety-utility trade-off while requiring substantially less training data.

---


### 65. [Fine-Tuning Improves Information Conveyance in Language Models](https://arxiv.org/abs/2605.30844)

**<font color=#1a73e8>作者：</font>** Yuwei Cheng, Weiyi Tian, Haifeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning is often believed to reduce uncertainty and diversity in large language models, but existing analyses overlook output length, a key confounder, and therefore fail to capture how uncertainty is distributed across an entire generation rollout. To address this, we propose Canopy Entropy ($\mathrm{CE}^\star$), a measure that views language generation from a tree perspective, where ``canopy'' represents the space of all possible rollouts, making $\mathrm{CE}^\star$ naturally quantify the effective size of the generation space. $\mathrm{CE}^\star$ jointly captures uncertainty in both the output length $N$ and the generated sequence $Y_{1:N}$ -- indeed, we show that it equals to total Shannon entropy $H(N, Y_{1:N}\mid X)$, where $X$ denotes the prompt. This formulation yields interpretable metrics, including a length-entropy correlation term $\rho(N, r_N)$, where $r_N$ is the entropy rate, quantifying information conveyance efficiency by indicating whether longer outputs are more or less informative per token. Empirically, across tasks and model families, we find that fine-tuned models consistently exhibit stronger positive correlation $\rho(N, r_N)$, even when total entropy decreases. Furthermore, after controlling for model family, task, prompt, and output-length effects, we find that fine-tuning nearly triples the correlation strength between entropy rate and semantic diversity, suggesting that aligned models convert token uncertainty into semantic diversity more efficiently. Overall, these results demonstrate that fine-tuning does not simply reduce uncertainty, but fundamentally reorganizes it into more informative and semantically meaningful generations. Our code is available at this https URL.

---


### 66. [Safe Equilibrium Policy Optimization for Strategic Agent Policies](https://arxiv.org/abs/2605.30854)

**<font color=#1a73e8>作者：</font>** Karthika Arumugam, Kiran Kumar Manku, Amit Dhanda  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Language models fine-tuned with reinforcement learning typically optimize for task reward, ignoring multi-agent strategic structure. Because these agents condition on natural language game-state descriptions and emit actions through free-form generation, strategic failure modes -- exploiting weaker opponents, coordinating on harmful equilibria, and externalizing costs are inseparable from the language interface itself. We propose Safe Equilibrium Policy Optimization (\sepo{}), a training objective that augments expected payoff with explicit penalties for exploitability, collusion risk, and externality cost. We implement \sepo{} as a reward signal for Group Relative Policy Optimization (GRPO), applied to Gemma~4 E4B-it and Qwen~3.5-4B after supervised fine-tuning (SFT). Evaluated across five strategic domains: Iterated Prisoner's Dilemma, repeated auctions, two negotiation variants, and Kuhn Poker. \sepo{} achieves zero exploit-pool advantage in Kuhn Poker for both models, outperforms the base model on safety in four domains, and corrects the over-cooperative behavior introduced by SFT. In negotiation, \sepo{} achieves a positive-safety outcome and only the positive normalized relative advantage of any negotiation configuration. Ablation experiments confirm that per-rollout exploit computation is necessary: a shared constant penalty cancels in GRPO advantage normalization (constant control-variate property), producing zero gradient. To support further research in strategic safety for agents, we release our \href{this https URL}{code} and SFT datasets.

---


### 67. [MADS: Model-Aware Diverse Core Set Selection for Instruction Tuning](https://arxiv.org/abs/2605.30857)

**<font color=#1a73e8>作者：</font>** Yi Bai, Wenhao Zhang, Yao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction fine-tuning is employed to enhance the instruction-following ability of large language models (LLMs). As the amount of instruction fine-tuning data increases, selecting the optimal core set becomes particularly important. However, ensuring the diversity of the core set remains a significant challenge. Existing methods predominantly distinguish different training data based on the text features themselves, decoupled from LLMs' own understanding and representation of the data. To address this issue, we propose a Model-Aware Diverse Core Set Selection method, which distinguishes data features based on the neural activation states during LLM inference. This approach serves as an efficient instantiation of coverage-based selection using model-intrinsic activation features to ensure the diversity in the core set. We extensively evaluate our method on six benchmarks that cover five distinct tasks. In our method, the core set selected by the 3B-parameter LLM performs effectively when utilized to fine-tune larger models with 7B, 8B, and 13B parameters. Experimental results on the Alpaca-GPT4 dataset, which comprises 52K instruction-response pairs, show that the core set, sized at 15\% of the original dataset and selected by Llama-3.2-3B-Instruct, achieves an average improvement of 2.5\% when fine-tuning four larger base models compared with training on the full dataset. The experimental results demonstrate that our method enhances model performance on multiple downstream tasks while reducing data requirements.

---


### 68. [ForecastCompass: Guiding Agentic Forecasting with Adaptive Factor Memory](https://arxiv.org/abs/2605.30858)

**<font color=#1a73e8>作者：</font>** Yurui Chang, Yongkang Du, Yuanpu Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic forecasting is important for decision-making in dynamic environments, but it remains challenging because agents must reason from incomplete, time-limited evidence and produce calibrated probabilities before outcomes are resolved. Memory provides a natural mechanism for transferring experience from resolved forecasts to future prediction tasks. However, existing agent-memory methods are not tailored to forecasting, as they typically store past interactions, reflections, or factual associations without explicitly representing reusable predictive factors or calibration knowledge. We propose ForecastCompass (FoCo), an adaptive factor-based memory framework for agentic forecasting. FoCo organizes forecasting experience with a hierarchical forecasting-task taxonomy, enabling retrieval task-relevant forecasting knowledge. It maintains two complementary memory components: factor memory, which captures reusable predictive dimensions, and reasoning memory, which encodes probability updating, uncertainty handling, and calibration principles. Using retrospective analyses as learning signals, FoCo iteratively revises memory through a verbalized memory-revision procedure, enabling the agent to accumulate transferable forecasting knowledge over time. Experiments on Prophet Arena and FutureX with GPT-5-mini and Gemini-2.5-Flash show that FoCo improves both probabilistic accuracy and calibration.

---


### 69. [DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning](https://arxiv.org/abs/2605.30859)

**<font color=#1a73e8>作者：</font>** Yujie Wang, Siwei Chen, Longzan Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has become pivotal for improving model capabilities yet suffers from rollout efficiency bottlenecks due to the long-tail response length distribution. While existing works mitigate the impact of long tails via prompt-level tail scheduling, we focus on the root source of inefficiency: the distribution itself. Specifically, we characterize the long-tail distribution at a finer granularity, identifying intra-prompt long tails, and revealing that they frequently consist of ineffective verbosity. To address this, we propose a novel paradigm of active distribution shaping to shape the rollout distribution towards conciseness and certainty, thereby fundamentally resolving tail-induced overheads. We achieve this through a distribution-aware trajectory sampling mechanism, which selects trajectories from a redundant exploration space for each prompt, and an adaptive redundancy allocation scheme to maximize both shaping effectiveness and system efficiency. Experiments demonstrate significant acceleration over state-of-the-art systems by up to 1.77x without compromising model performance.

---


### 70. [Distilling LLM Feedback for Lean Theorem Proving](https://arxiv.org/abs/2605.30861)

**<font color=#1a73e8>作者：</font>** Gaetan Narozniak, Gérard Biau, Rémi Munos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training for reasoning models typically combines supervised fine-tuning with reinforcement learning from verifiable rewards, most commonly with GRPO. However, this algorithm suffers from sparse rewards, limited exploration, and mode collapse. Building upon recent works on self-distillation, we propose Feedback Distillation, a training method where the model is trained to match, at the token level, its own distribution conditioned on privileged feedback produced by a language model. Feedback Distillation offers token-level supervision and can inject external knowledge. Evaluating our method for Lean4 theorem-proving, we find that Feedback Distillation maintains greater diversity in generated trajectories than GRPO, yielding higher policy entropy and better pass@k scaling. The two methods are complementary: initializing GRPO from a Feedback Distillation checkpoint outperforms either method alone. All in all, our results suggest a promising avenue to improve post-training for complex reasoning.

---


### 71. [GlucoFM: A Dual-Stream Foundation Model for Continuous Glucose Monitoring](https://arxiv.org/abs/2605.30865)

**<font color=#1a73e8>作者：</font>** Zechen Li, Keerthana Natarajan, Weizhi Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitoring (CGM) provides a dense view of daily metabolic physiology, yet existing generic time-series and CGM-specific foundation models often encode glucose traces as entangled single-stream sequences, leaving the distinct temporal structure of glycemic dynamics only implicitly modeled. We present GlucoFM, a lightweight CGM foundation model that aligns irregular recordings to a 24-hour chronological grid, preserves observation masks, and decomposes glucose dynamics into slow physiological state and transient event streams, capturing low-frequency glycemic baselines and short-term deviations that may reflect acute physiological responses or sensor artifacts. GlucoFM is pretrained on 109,066 hours of unlabeled CGM recordings from 477 subjects with two complementary objectives: masked contextual latent prediction over fused daily representations and temporal dynamics prediction over state and event streams. Across four diverse cohorts and seven clinical prediction tasks, GlucoFM achieves the strongest subject-disjoint linear-probing performance among evaluated baselines, improving average PR-AUC by 4.1 points over the best CGM-specific foundation model. Its gains are most pronounced on core metabolic outcomes, leading PR-AUC on all diabetes-risk and $\beta$-cell dysfunction tasks and on 3 of 4 insulin-resistance tasks. GlucoFM also achieves the best overall cross-dataset transfer performance and strong few-shot adaptation among evaluated methods, and consistent gains when aggregating multiple days for subject-level prediction, highlighting physiology-aware decomposition as an effective inductive bias for transferable CGM representation learning.

---


### 72. [Federated Variational Preference Alignment with Gumbel-Softmax Prior for Personalized User Preferences](https://arxiv.org/abs/2605.30873)

**<font color=#1a73e8>作者：</font>** Jabin Koo, Hoyoung Kim, Minwoo Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) offers a privacy-preserving pathway for aligning Large Language Models (LLMs); however, existing frameworks typically enforce a monolithic reward model, inevitably averaging out inherently conflicting user preferences (e.g., helpfulness vs. harmlessness). While Variational Preference Learning (VPL) offers a pathway to personalization, adapting it to decentralized settings presents a fundamental challenge: posterior collapse driven by severe local data scarcity and heterogeneity. In this paper, we propose Federated Variational Preference Alignment with Gumbel-Softmax Prior (FedVPA-GP), a framework designed to disentangle diverse preferences without compromising privacy. To stabilize variational inference, we introduce a Federated Mixture Prior that enables clients to leverage the aggregate population distribution as a dynamic prior. Furthermore, we incorporate an Orthogonal Loss that explicitly enforces the separation of preference prototypes in the latent space. Experiments on the HH-RLHF dataset demonstrate that FedVPA-GP significantly outperforms monolithic baselines, successfully disentangling conflicting user intents and enabling dynamic preference switching.

---


### 73. [dMoE: dLLMs with Learnable Block Experts](https://arxiv.org/abs/2605.30876)

**<font color=#1a73e8>作者：</font>** Sicheng Feng, Zigeng Chen, Gongfan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive models, offering competitive performance while naturally supporting parallel decoding. However, as dLLMs are increasingly integrated with Mixture-of-Experts (MoE) architectures to scale model capacity, a fundamental mismatch arises between block parallel decoding and token-level expert selection. Specifically, each dLLM forward pass processes multiple tokens with bidirectional dependencies, whereas conventional MoE layers route each token independently. This mismatch substantially increases the number of uniquely activated experts, making inference increasingly memory-bound. To address this, we propose dMoE, a simple yet effective block-level MoE framework. The central idea of dMoE is to aggregate token-level expert distributions within each block into a unified block-level expert distribution, which is then used to guide expert routing in a more coherent manner. In this way, dMoE substantially reduces the number of uniquely activated experts during inference without sacrificing performance, thereby mitigating the memory-bound bottleneck. Extensive experiments across a variety of benchmarks demonstrate the effectiveness of dMoE. On average, dMoE reduces the number of uniquely activated experts from 69.5 to 14.6 while retaining 99.11% of the original performance. Meanwhile, it reduces memory usage by 76.64% to 79.84% and achieves 1.14$\times$ to 1.66$\times$ end-to-end latency speedup. Code is available at: this https URL

---


### 74. [PatchWorld: Gradient-Free Optimization of Executable World Models](https://arxiv.org/abs/2605.30880)

**<font color=#1a73e8>作者：</font>** Jiaxin Bai, Yue Guo, Yifei Dong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-agent environments are typically modeled as partially observable Markov decision processes (POMDPs), assuming that the simulator's latent state and transition dynamics are hidden from the agent. Yet little work has examined whether executable code can be induced to serve as a world model for prediction and planning under partial observability. We introduce PatchWorld, a gradient-free framework that turns offline trajectories into executable Python world models through counterexample-guided code repair. Instead of predicting the next observation with a black-box model, PatchWorld induces symbolic belief-state programs whose action updates can be inspected, replayed, and locally patched. Across seven AgentGym environments, PatchWorld-Simple achieves the highest code-based planning score among evaluated methods, reaching 76.4\% macro success in live one-step lookahead while invoking no LLM calls inside the world-model prediction module itself. We further find that a human-specified residual-memory bias improves surface observation fidelity but weakens decision utility. This exposes a tradeoff in executable world models, since improving observation fidelity can come at the expense of action-discriminative dynamics, and vice versa. Code is available at this https URL.

---


### 75. [The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement](https://arxiv.org/abs/2605.30888)

**<font color=#1a73e8>作者：</font>** Xiaobo Wang, Tong Wu, Min Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building strong reward models (RMs) for language model alignment is bottlenecked by the cost and difficulty of acquiring diverse and reliable preference data from human annotation or judge models. It is dramatically worse as the policy evolves beyond the static RM training. Therefore, we propose SAVE (Self-supervised reward model improvement via Value-Anchored On-policy feedback), a framework that grades on-policy responses as feedback by using the value function for on-policy RM training. SAVE naturally converts the reward-graded on-policy responses into supervision with a prompt-specific value head as an adaptive anchor. It computes RM advantages and filters ambiguous samples to update the RM via a contrastive objective. The effectiveness of SAVE for enhancing RM training is strongly validated through rigorous empirical evaluation across six diverse benchmarks. It achieves outperforming results across all datasets while maintaining consistent improvements across three RL algorithms (GRPO, RLOO, GSPO) and different policy backbones.

---


### 76. [BilliardPhys-Bench: Benchmarking Physical Reasoning and Visual Dynamics of Multimodal LLMs](https://arxiv.org/abs/2605.30900)

**<font color=#1a73e8>作者：</font>** Ben Wang, Xiaogang Li, Ruochen Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current multimodal models handle static image recognition well, but intuitive physical reasoning remains a weakness. Predicting how objects will move and interact from a single image is still difficult for these systems. We present BilliardPhys-Bench, a benchmark for physical reasoning in synthetic billiards environments. Its procedural engine generates randomized scenarios with friction and elastic collisions. The benchmark tests three abilities: (1) predicting ball-to-ball collisions, (2) reasoning about wall bounces, and (3) estimating final ball positions after motion stops. We evaluate recent MLLMs from the GPT, Claude, Gemini, and Qwen families. Performance drops as simulation time increases and scene geometry grows more complex. We also observe a consistent failure mode we call "stasis bias": when the correct physical outcome is harder to infer, models tend to predict no interaction. These findings show where current MLLMs break down on visual dynamics and point toward the need for better physical inductive biases in multimodal architectures.

---


### 77. [Inverse Reinforcement Learning without an Optimal Demonstrator: A Feasible Reward Set Approach](https://arxiv.org/abs/2605.30903)

**<font color=#1a73e8>作者：</font>** Kihyun Kim, Shripad Deshmukh, Nikos Vlassis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse reinforcement learning (IRL) typically assumes demonstrations from a single optimal demonstrator, but in many applications data come from multiple imperfect demonstrators with heterogeneous suboptimality levels. We study reward learning in this setting through a feasible-reward-set framework: for each demonstrator, we encode its declared suboptimality level as a linear constraint and intersect the resulting feasible sets across demonstrators. Our theoretical analysis shows that the joint feasible set shrinks monotonically as data are added, and we give an exact characterization of when a new demonstrator strictly tightens it. We further establish two recovery guarantees for the feasible reward set of the ground-truth optimal demonstrator: one bound depends on closeness to the optimal occupancy, while the other requires only sufficient coverage and no near-optimal demonstrator. On the practical side, we introduce strategies to address the inherent reward ambiguity in the obtained reward set and provide an offline algorithm with function approximation for high-dimensional environments. Experiments in tabular grid-world and large language model (LLM) fine-tuning settings are consistent with the theoretical predictions and demonstrate the effectiveness of the proposed framework over baselines.

---


### 78. [What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness](https://arxiv.org/abs/2605.30911)

**<font color=#1a73e8>作者：</font>** Yusheng He, Jizhe Zhou, Xia Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hallucination remains one of the key challenges undermining the reliability of Large Vision-Language Models (LVLMs). But what makes an LVLM hallucinate less? Many existing efforts focus on improving internal components of the model. We argue that hallucination fundamentally stems from how the model architecture is designed. To investigate this, we factor the architecture design into three dimensions: Linguistic Foundation (LF), Visual Representation (VR), and Semantic Alignment (SA), and categorize hallucinations into Co-occurrence, Similarity, and previously overlooked Uncertainty types. Building on this formulation, we propose CoSimUE, a benchmark that creates fine-grained hallucination scenarios through controlled textual perturbations and random perturbations, enabling mapping between design choices and hallucination behaviors. Experiments across 7 design aspects show that: 1) the widely emphasized scaling of model parameters has only limited impact on reducing all three types of hallucinations; 2) larger and better-trained language foundations can reduce co-occurrence hallucinations; 3) stronger visual encoders and higher resolutions mitigate similarity errors; 4) effective alignment strategies alleviate uncertainty hallucinations. 5) Furthermore, cross-dimensional analysis reveals that jointly enhancing visual fidelity and alignment quality yields the most comprehensive improvements. This study provides the first systematic exploration linking architecture-level design to hallucination robustness, offering practical guidance for developing reliable and efficient LVLMs.

---


### 79. [Attend to Evidence: Evidence-Anchored Spatial Attention Supervision for Multimodal RLVR](https://arxiv.org/abs/2605.30912)

**<font color=#1a73e8>作者：</font>** Ruina Hu, Chen Wang, Lai Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves vision-language models (VLMs) by optimizing outcome rewards derived from final answers. However, such outcome-only rewards do not tell the model which image regions justify an answer. For questions that require visual grounding, these rewards cannot distinguish responses supported by relevant visual evidence from those produced by language-prior shortcuts or lucky guesses. We introduce EASE (Evidence-Anchored Spatial Attention), which augments multimodal RLVR with visual-evidence process supervision. EASE converts annotated evidence regions into a smoothed visual-token target and uses it to guide response-to-image attention during RL training, but only on high-reward trajectories. The annotations are used solely as privileged training labels, while inference requires only the original image and question. Across Qwen2.5-VL-7B, Qwen3-VL-4B, and Qwen3-VL-8B, EASE raises average scores over DAPO by 2.5 to 3.1 points on perception, hallucination, visual math, and multimodal reasoning benchmarks. Diagnostics and ablations show that EASE better aligns visual attention with annotated evidence regions.

---


### 80. [Toxic HallucinAItions: Perturbing Prompts and Tracing LLM Circuits](https://arxiv.org/abs/2605.30913)

**<font color=#1a73e8>作者：</font>** Soorya Ram Shimgekar, Agam Goyal, Amruta Parulekar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in conversational settings where user tone ranges from polite to adversarial or toxic, yet less is known about whether toxic language in otherwise semantically equivalent prompts can degrade factual reliability. We study how lexical and tone-based prompt perturbations affect the factual reliability of LLMs. Using controlled prompt variations across polite, random, and three toxicity levels, we evaluate five LLMs on ARC-Easy, GSM8K, and MMLU. We find that toxic lexical perturbations consistently reduce factual accuracy and increase uncertainty, while polite phrasing yields limited and inconsistent changes. To examine whether these answer inconsistencies correspond to internal changes, we conduct attribution-graph analyses of model activations and influences. We find that increasing toxicity selectively amplifies perturbation-sensitive variant nodes while relatively stable core reasoning nodes remain more invariant. These findings position prompt tone as a critical dimension of LLM reliability and provide behavioral and mechanistic evidence that surface-level lexical variation can alter factual outputs and internal computation.

---


### 81. [DiTTo: Scalable Order-aware All-in-One Image Restoration Agent](https://arxiv.org/abs/2605.30915)

**<font color=#1a73e8>作者：</font>** Seungho Choi, Jihyong Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world images rarely suffer from a single degradation, and the order in which degradations are removed substantially affects the final restoration quality, motivating agent-based image restoration (IR), where a vision-language model schedules a pool of pre-built restoration-experts. However, existing training-based agents require $\mathcal{O}((N^{\mathbf{D}})^{2})$ restoration-expert calls per image to construct the Optimal Restoration-action Trajectory Dataset (ORTD), where $N^{\mathbf{D}}$ denotes the number of degradation types in the universe $\mathbf{D}$, and couple agent training to a fixed restoration-expert pool, preventing extension to newly introduced restoration-experts without full retraining. To overcome these efficiency and extensibility bottlenecks, we propose \textbf{DiTTo}, a novel order-aware image restoration agent framework consisting of the DiTTo Simulator and the DiTTo Agent. The DiTTo Simulator combines $\cup$S-IR for single-step restoration-action simulation and AiO-IQA for per-action quality prediction, reducing ORTD construction to $\mathcal{O}(N^{\mathbf{D}})$ simulator calls per image; the DiTTo Agent is trained by SFT on the simulator-generated ORTD, followed by \textbf{Order-aware Restoration Alignment (ORA)} that aligns degradation identification, restoration-action-ordering, and output format along independent axes. This enables \textbf{plug-and-play scalable extensibility}: adding a new restoration-expert requires updating only the lightweight ORA stage. On the MiO-100 evaluation set with up to five concurrent degradations, our DiTTo Agent achieves state-of-the-art multi-degradation restoration quality among previous agent-based IR methods.

---


### 82. [De-attribute to Forget for LLM Unlearning](https://arxiv.org/abs/2605.30919)

**<font color=#1a73e8>作者：</font>** Xinyang Lu, Jiabao Pan, Rachael Hwee Ling Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models (LLMs) has raised concerns on the use of inappropriate data for training, which has led to a growing interest in LLM unlearning. Many existing LLM unlearning approaches rely on optimizing prediction loss(es), such as maximizing the loss on the forget set, but often face critical issues like over-forgetting and poor model utility. To address them, this paper novelly frames the optimization objective for LLM unlearning as one of zeroing out data attribution instead. In particular, we propose the first LLM unlearning framework based on data attribution rewards called DareU that performs reinforcement learning to update the LLM by reducing the attribution score of its generated responses (i.e., de-attributing) to the forget data owners. Empirical evaluation using an LLM classifier as an efficient approximation of attribution shows that DareU outperforms existing baselines by achieving effective unlearning while balancing forget quality and model utility well.

---


### 83. [EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents](https://arxiv.org/abs/2605.30924)

**<font color=#1a73e8>作者：</font>** Dongwook Choi, Taeyoon Kwon, Bogyung Jeong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> MLLM-powered embodied agents deployed in real-world environments encounter physical hazards. However, existing approaches lack explicit mechanisms for identifying hazards and reasoning about action-conditioned risks, leading agents to either miss risky interactions or over-identify risks. To address this, we propose EMBGuard, the first MLLM-based safety guardrail for embodied agents designed to decouple physical risk reasoning from agent policy. By evaluating a (visual observation, action) pair, EMBGuard identifies hazardous configurations and provides natural language explanations of potential risks. Alongside EMBGuard, we contribute EMBHazard, a training dataset of 15.1K action-conditioned pairs, and EMBGuardTest, a benchmark of 329 manually curated real-world scenarios spanning seven physical risk categories. Through compositional variation of hazards and actions, we generate diverse risky and benign scenarios that agents may encounter during planning. Despite its compact size (2B, 4B), EMBGuard achieves performance competitive with proprietary MLLMs (e.g., GPT-5.1, Gemini-2.5-Pro) while significantly reducing the false-positive rates that hinder real-time deployment. We make the code, data, and models publicly available at this https URL

---


### 84. [TUX: Measuring Human--AI Tacit Understanding](https://arxiv.org/abs/2605.30930)

**<font color=#1a73e8>作者：</font>** Yueshen Li, Hanyi Min, Vedant Das Swain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) increasingly act as collaborative partners, human--AI alignment is often evaluated through explicit task success, accuracy, or reward optimization. Yet many collaborative settings depend on tacit understanding: whether an agent can align with a human's evaluative stance or representational priors without clear objectives, communication, or feedback. To study this capacity, we develop a spectrum-placement task inspired by the social party game Wavelength, in which humans and agents independently place concepts along subjective spectra. We operationalize the Tacit Understanding Index (TUX) as a pairwise measure of similarity between human and agent judgments, and evaluate it with 241 human participants and 200 profile-conditioned LLM agents across four models. We find that nearest human--agent pairs in trait space achieve significantly higher TUX, suggesting that tacit alignment is structured by person-level characteristics rather than random similarity. Regression analyses show that TUX becomes more explainable as predictor sets become richer, with individual traits, decision-making styles, and confidence improving over aggregate trait-distance baselines. These findings suggest that tacit understanding between humans and LLMs is measurable, while revealing the limits of profile-based conditioning for capturing deeper representational alignment.

---


### 85. [MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft](https://arxiv.org/abs/2605.30931)

**<font color=#1a73e8>作者：</font>** Tianjie Ju, Yueqing Sun, Zheng Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong capabilities in perception, reasoning, and action generation. However, their ability to sustain exploration in dynamic open worlds remains unclear. Existing embodied and game-based benchmarks often compress interaction into short-horizon tasks or entangle success with domain-specific game mechanics. In this paper, we introduce MineExplorer benchmark for evaluating open-world exploration capabilities of MLLM agents in Minecraft. We first filter atomic tasks whose solutions rely heavily on Minecraft-specific knowledge to better reflect general open-world reasoning. Then we organize the benchmark around a ReAct-style capability formulation and compose atomic tasks into implicit multi-hop tasks. To further construct reliable instances, MineExplorer uses a multi-agent synthesis workflow that jointly designs task graphs, sandbox scenes, and rule-based milestone evaluators. Human evaluation shows that the multi-agent synthesis workflow produces significantly more reliable instances than a single-agent baseline. Experiments with advanced MLLM agents show that open-world exploration remains challenging, as strong models can handle many single-hop tasks but degrade sharply when hidden prerequisites must be coordinated over longer trajectories. Further analysis finds that task difficulty tracks agent completion, and larger models or thinking modes do not consistently translate into better performance. Code and dataset are available at this https URL.

---


### 86. [Do Large Language Models Encode Institutional Experience? Evidence from Cross-Linguistic Moral Reasoning Under Ambiguity](https://arxiv.org/abs/2605.30934)

**<font color=#1a73e8>作者：</font>** Nattavudh Powdthavee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit systematic differences in moral reasoning across languages, yet the source of this variation remains unclear. We test the hypothesis that languages encode aspects of the institutional environments in which they are spoken, allowing LLMs to inherit institution-specific moral priors through training. Across nine languages spanning a broad gradient of institutional quality, six frontier LLMs, and two preregistered studies, we examine moral dilemmas whose acceptability depends on institutional functioning. In Study 1, explicit institutional framing produced uniformly null results: cross-linguistic moral divergence did not increase in institutionally contingent scenarios, nor did it track institutional differences between language communities. In Study 2, we introduced institutionally ambiguous scenarios in which institutional stakes were present but not explicitly stated. Under these conditions, cross-linguistic moral divergence increased relative to institutionally inert controls and, with one theoretically informative exception, was associated with real-world institutional differences between language communities. Explicit framing again attenuated these effects. These findings suggest that institutional experience may leave detectable traces in language that shape LLM moral reasoning, while also indicating that explicit institutional cues can suppress the expression of those differences.

---


### 87. [EvoGens: A Population-Based Heuristic Search Framework for Scientific Idea Generation](https://arxiv.org/abs/2605.30961)

**<font color=#1a73e8>作者：</font>** Xu Li, Hanzhe Tu, Xinyi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating novel research ideas is fundamental to scientific progress. While Large Language Models (LLMs) show promise in assisting this process, existing approaches often exhibit semantic convergence, resulting in limited diversity and novelty. To address this, we introduce EvoGens, an evolution-inspired framework that recasts scientific idea generation as an evolutionary search over a population of ideas. EvoGens iteratively applies rank-based mutation with differentiated retrieval planning to incorporate external knowledge, and semantic-aware crossover to fuse complementary concepts for conceptual reorganization. A lightweight evaluation signal guides the selection process, encouraging sustained exploration while mitigating premature convergence. Extensive experiments demonstrate that EvoGens substantially enhances exploration capabilities compared to state-of-the-art baselines. Specifically, it improves the Novelty from 0.1 to 0.4 and the Diversity from 0.24 to 0.55, while maintaining comparable idea quality under the current automatic evaluation protocol. These findings suggest that evolutionary mechanisms can serve as a useful framework for exploration-oriented research ideation, especially for broadening the novelty and diversity of candidate ideas under a shared automatic evaluation setting.

---


### 88. [Parallel Tempering Initial Sampling in Inference-Time Reward Alignment](https://arxiv.org/abs/2605.30991)

**<font color=#1a73e8>作者：</font>** Myeongjun Oh, Gwangho Kim, Sungyoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time reward alignment steers pretrained diffusion and flow-based generative models to satisfy user-specified rewards without retraining. Recently, Sequential Monte Carlo (SMC) has emerged as a powerful framework for this task by iteratively filtering and propagating multiple particles. However, we show that standard SMC-based methods often suffer from poor performance because they initialize particles from a standard prior, whereas high-reward regions in complex reward landscapes are extremely rare. Further, we show that even recent reward-aware initial sampling approaches remain vulnerable to getting trapped in local modes, as complex reward landscapes are often multi-modal. To overcome these limitations, we propose PATHS (PArallel Tempering for High-complexity reward Sampling), a novel initialization method that couples multiple sampling chains through parallel tempering. PATHS maintains a ladder of reward-tempered chains and periodically performs Metropolis swaps, enabling efficient exploration across flattened reward landscapes, thereby mitigating the mode-trapping issues. Our analysis reveals that this mechanism substantially enhances the finite-budget exploration of rare, high-reward regions that are typically challenging to sample. Experiments on layout-to-image and quantity-aware generation show that PATHS achieves consistent gains in alignment quality, particularly on complex prompts.

---


### 89. [Eigenvectors of Experts are Training-free Non-collapsing Routers](https://arxiv.org/abs/2605.30992)

**<font color=#1a73e8>作者：</font>** Giang Do, Hung Le, Truyen Tran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture of Experts (SMoE) architectures improve the training efficiency of Large Language Models (LLMs) by routing input tokens to a selected subset of specialized experts. Despite their remarkable success, both training and inference in SMoE models suffer from the expert collapse issue (Chi et al., 2022), which degrades model performance. Prior studies primarily focus on improving the router; however, such methods rely on training from scratch or fine-tuning, which requires high computational and data-processing costs. Furthermore, we demonstrate that, despite these efforts, the issue persists when advancing well-pretrained SMoE models, as evidenced by both theoretical and empirical results. To fill that gap, we analyze the advanced SMoE models and observe that the eigenvectors of expert weight matrices encode rich semantic information, pointing to an effective alternative to conventional routing strategies. Building on this insight, we propose Singular Value Decomposition SMoE (SSMoE), a novel and training-free framework that leverages spectral properties of the expert weights to address the collapse issue and enhance model performance. Extensive experiments across diverse language and vision tasks, under both clean and corrupt data settings, demonstrate the strong generalization and robustness of SSMoE. Our findings highlight how a deeper understanding of model internals can guide the development of more effective SMoE architectures. Our implementation is publicly available at this https URL.

---


### 90. [MoG: Mixture of Experts for Graph-based Retrieval-Augmented Generation](https://arxiv.org/abs/2605.31010)

**<font color=#1a73e8>作者：</font>** Zheng Yuan, Chuang Zhou, Linhao Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation is intensively studied to ground large language models on external evidence. However, retrieving from a unified knowledge base could inevitably introduce irrelevant information that may mislead generation for complex reasoning. Inspired by the conditional computation of mixture of experts (MoE), where a router sparsely selects specialized experts alongside shared ones for each input, we propose \textbf{M}ixture \textbf{o}f experts for \textbf{G}raph-based Retrieval-Augmented Generation, i.e., \textbf{MoG}. It organizes knowledge into two core components: (i) diverse, always-accessible hub graphs that encode semantically and structurally central knowledge and provide contextual clues for expert activation, and (ii) sparsely activated expert graphs that contain domain-specific evidence. MoG first accesses hub graphs to identify general evidence and derive contextual clues. Then, a topology-aware router dynamically activates a limited set of expert graphs conditioned on the query, thereby confining retrieval to a focused evidence subspace. Extensive experiments on challenging benchmarks show that MoG consistently outperforms strong baselines, with over 20\% relative improvement on MuSiQue. Our code is available in this https URL.

---


### 91. [A Persona-Based Evaluation Framework for Pluralistic Alignment in Generative AI](https://arxiv.org/abs/2605.31021)

**<font color=#1a73e8>作者：</font>** Atahan Karagoz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current alignment paradigms for generative artificial intelligence rely predominantly on monolithic benchmarking frameworks that reduce the plurality of human judgment to aggregated statistical baselines, thereby obscuring cultural, demographic, and contextual variability in evaluation. We introduce a state-space constrained emulation framework for AI evaluation that replaces singular assessment functions with a structured manifold of synthetic cognitive profiles representing diverse human perspectives. We show that modern generative architectures can instantiate and maintain these evaluative personas with high consistency, enabling a form of pluralistic, perspective-dependent benchmarking that more closely reflects real-world consensus variability. However, we further analyze the stability of these simulated evaluators under sequential inference and stochastic prompt perturbations, revealing systematic degradation in persona coherence that manifests as state-space drift and semantic inconsistency. These findings suggest that static alignment constraints are insufficient for sustaining robust evaluative behavior over time. Instead, we argue for the necessity of embedding dynamic, viability-driven regulatory mechanisms within generative systems to preserve coherent cognitive emulation. By framing persona-based evaluation as a structured dynamical system over latent representation manifolds, this study provides a foundation for more adaptive, human-aligned, and context-sensitive approaches to AI evaluation.

---


### 92. [TRACE: Discovering Task-Specific Parameter via Adaptation-Aware Probing for Continual Fine-Tuning](https://arxiv.org/abs/2605.31025)

**<font color=#1a73e8>作者：</font>** Xiaosong Han, Ke Chen, Xindi Dai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In real-world deployment, LLMs are often adapted continually across tasks to keep LLMs up-to-date in production, where new fine-tuning should preserve previously learned skills. However, indiscriminately mixing tasks can dilute task specialization, while sequential fine-tuning (full-parameter or low rank adaptation) often causes catastrophic forgetting due to destructive overwriting. Replay-based continual tuning and maintaining separate task-specific adapters can mitigate forgetting, but introduce additional compute, storage, and management overhead. Recognizing the redundancy of LLM parameters for any single task, we reframe continual task adaptation as task-specific parameter discovery via adaptation-aware probing: a short warm-start probe exposes a task's adaptation trace, enabling us to identify and isolate the small subset of parameters essential for each task to mitigate catastrophic forgetting. Building on this view, we introduce TRACE, a novel approach for discovering Task-specific paRameters via Adaptation-aware probing for Continual finE-tuning. We perform a short warm-start fine-tune to derive task-specific core parameters by comparing the warm-started and pre-trained models. Core parameters are identified via two strategies: importance scoring (L$_2$ norm and Fisher Information) and specificity analysis (cosine similarity of parameter updates). In continual fine-tuning settings, only the active task's core parameters are updated while others remain frozen, preserving prior knowledge. We conduct extensive experiments across multiple standard benchmarks to demonstrate the superior performance of our proposed method. Additionally, we validate the generalization of our method through a cross-model and scale transferability study, demonstrating a "small-to-large" paradigm that guides the fine-tuning of large-scale models under resource constraints.

---


### 93. [Best-Arm Identification-Based Trust Region Selection for Bayesian Optimization on Multimodal Functions](https://arxiv.org/abs/2605.31050)

**<font color=#1a73e8>作者：</font>** Nobuo Namura, Sho Takemori  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process-based Bayesian optimization (BO) is a popular approach for expensive black-box optimization, but its performance often degrades on complex multimodal or high-dimensional problems. Trust region-based BO mitigates this issue by focusing on local regions, and recent studies suggest that selecting an effective region can be formulated as a multi-armed bandit problem. We propose a trajectory-aware framework that integrates best-arm identification (BAI) with trust region-based BO to efficiently solve multimodal optimization problems. Our method extrapolates the optimization trajectories of multiple locally initialized optimizers to predict their final performance and progressively eliminates suboptimal candidates via BAI. We theoretically show that the proposed BAI-guided BO converges faster to the global optimum than conventional BO under mild assumptions, and demonstrate its effectiveness through extensive experiments on synthetic and real-world benchmarks.

---


### 94. [How Much Do LLMs Know About Chinese Zero Pronouns?](https://arxiv.org/abs/2605.31056)

**<font color=#1a73e8>作者：</font>** Yifei Li, Guanyi Chen, Tingting He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Zero Pronouns (ZPs) are a pervasive linguistic phenomenon in pro-drop languages such as Chinese and have long posed a challenge for natural language processing systems. Although Large Language Models (LLMs) perform well on many Chinese language tasks, their ability to process ZPs remains poorly understood. We conduct a systematic investigation of LLMs' handling of Chinese ZPs through a sequence of linguistically motivated tasks, including identification, referentiality classification, referential type classification, resolution, and translation. A diverse set of LLMs is evaluated across all tasks. Our results show that Chinese ZPs remain highly challenging for current LLMs, particularly for upstream tasks such as identification and referentiality classification. Performance on downstream tasks, such as ZP translation, is also consistently low: even state-of-the-art reasoning-oriented LLMs correctly translate fewer than half of Chinese ZPs into English.

---


### 95. [AdaptR1: Reinforcement Learning Based Adaptive Interleaved Thinking in Multi-hop Question Answering](https://arxiv.org/abs/2605.31062)

**<font color=#1a73e8>作者：</font>** Yuxin Wang, Jiahao Lu, Qifeng Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable performance in complex reasoning tasks through Chain-of-Thought (CoT) prompting. However, this approach often leads to ``over-thinking,'' where models generate unnecessarily long reasoning traces for simple queries and incur avoidable inference cost. While recent work has explored adaptive reasoning, existing methods typically make a single query-level decision about whether to reason. This overlooks the dynamic nature of multi-step tasks, where the need for explicit reasoning varies across intermediate stages. To address this limitation, we introduce AdaptR1, a Reinforcement Learning (RL) based framework for adaptive interleaved thinking in multi-hop Question Answering (QA). Unlike previous approaches that require Supervised Fine-Tuning (SFT) for cold-start initialization, AdaptR1 uses a fully RL-based strategy with a quality-gated efficiency reward to dynamically allocate reasoning budgets at each step. Under the Graph-R1 setting, AdaptR1 reduces average think tokens by 69.71\%, with a 90.35\% reduction on HotpotQA, while maintaining performance comparable to or better than standard baselines. Furthermore, our analysis reveals that overthinking in multi-hop reasoning is not uniformly distributed but occurs predominantly during the initial planning stages, highlighting the effectiveness of step-wise adaptive budget allocation.

---


### 96. [Towards Effective Long-Video Event Prediction via Multi-Level Event Semantics Mining](https://arxiv.org/abs/2605.31069)

**<font color=#1a73e8>作者：</font>** Bo Peng, YuanJie Lyu, PengGang Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately predicting future events is fundamental to content understanding and decision-making across various domains. While prior research has primarily focused on text or short-video scenarios, long-video event prediction, characterized by vast multimodal context and more complex narratives, remains underexplored. Meanwhile, although recent Long-Video Language Models (LVLMs), built on Large Language Models (LLMs) and Vision-Language Models (VLMs), have shown promise in long-video question answering and summarization, they struggle to generalize to event prediction, as they can neither precisely extract event-related details nor perform fine-grained analysis of event development. To address this gap, we propose VISTA, a multi-level event semantics mining framework for long-video event prediction. Initially, VISTA applies a character-centric visual prompt to precisely extract event-related visual details, enhancing detail-level semantics; subsequently, it employs a knowledge-enhanced iterative retrieval strategy, guiding the LLM to progressively construct logically coherent event chains, thereby improving event-level narratives; ultimately, VISTA adopts a human-like propose-then-retrieve strategy to generate diverse future-oriented proposals and integrate multi-level clues, producing robust and accurate predictions. Extensive experiments on real-world datasets validate the effectiveness of VISTA for long-video event prediction.

---


### 97. [ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails](https://arxiv.org/abs/2605.31073)

**<font color=#1a73e8>作者：</font>** Yan Wang, Zhixuan Chu, Zihao Xue 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning-based LLM guardrails improve safety moderation by generating explicit rationales before issuing final decisions. However, their rationales do not always lead to faithful enforcement: a model may recognize a harmful intent in its reasoning but still predict a safe label, or issue an unsafe decision without policy-grounded justification. We identify this safety-critical failure mode as the deliberation-to-enforcement gap. Unlike general chain-of-thought faithfulness, guardrail reliability requires policy execution consistency: the generated reasoning should be grounded in the safety policy, and the final decision should be entailed by that reasoning. We propose ConsisGuard, a consistency-aware framework for reasoning-based LLM guardrails. ConsisGuard performs Policy-to-Decision Trajectory Distillation and Functional Coupling Alignment, aligning the internal coupling between safety deliberation and decision enforcement. Experiments on prompt and response harmfulness detection benchmarks show that ConsisGuard improves detection performance while reducing policy execution failures. These results suggest that reliable reasoning-based guardrails require accurate faithful execution of safety policies.

---


### 98. [Task-Focused Memorization for Multimodal Agents](https://arxiv.org/abs/2605.31075)

**<font color=#1a73e8>作者：</font>** Tao Zou, Yichen He, Tian Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for multimodal agents to build coherent experience, accumulate world knowledge, and achieve continual learning. However, constructing effective memory goes beyond memory module design and basic requirements such as accuracy and fidelity; the key challenge lies in determining what to memorize. Multimodal agents, such as embodied agents, continuously perceive, reason, and act in real or virtual environments, receiving an unbounded stream of multimodal observations. From this combinatorial explosion of information, an agent must selectively retain content that is relevant to its role in the environment and valuable for future tasks. To bridge this gap, we frame memory generation as a learnable memorization policy and introduce TaskMem (Task-focused Memorization Policy Learning), a reinforcement-learning-based framework that enables the policy to dynamically adjust its focus to the demands of real tasks encountered in the environment. TaskMem adopts a two-phase training paradigm: Phase One learns how to memorize by optimizing memory quality under fundamental fidelity requirements; Phase Two occurs after deployment, where the agent learns what to memorize by tuning an adapter on its base MLLM, using recent environment tasks to define a reward model that guides the memorization policy toward task-relevant content. To evaluate our approach, we reformulate VideoMME, EgoLife, and EgoTempo into streaming benchmarks that simulate a realistic setting in which an agent processes streaming observations and handles tasks arriving online. To isolate memory assessment, the questions must be answered using only the agent's memory, without access to raw video. Built on Qwen3-VL-30B-A3B, TaskMem improves VQA accuracy by 6.3%, 7.0%, and 5.3% on these benchmarks, respectively.

---


### 99. [Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory](https://arxiv.org/abs/2605.31086)

**<font color=#1a73e8>作者：</font>** Han Zhang, Zihao Tang, Xin Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In existing memory benchmarks for Large Language Models (LLMs), the evaluated dialogue sessions often lack long-term semantic consistency, and the underlying personas tend to be flat and static. Furthermore, in real-world scenarios, interactions between users and assistants involve more diverse, heterogeneous data streams, such as documents and emails. These shortcomings significantly limit the realism and effectiveness of current evaluations. To address these limitations, we introduce RHELM (Realistic, Heterogeneous, and Evolving Long-term Memory). Driven by meticulously crafted user profiles and a novel LOOP (pLan-rOllout-evOlve-Prune) module, we construct realistic dialogues across diverse interaction scenarios that exhibit dynamic temporal evolution and long-term coherence. Crucially, these dialogues are deeply integrated with heterogeneous external sources synchronized with the user's temporal event trajectory. The resulting benchmark encompasses challenging question-answer pairs spanning seven inquiry types, with each question mapping to at least one of 27 critical memory characteristics that we identify as essential yet underexplored in current research. Comprehensive experiments across full-context models, retrieval-augmented generation (RAG) methods, and representative memory frameworks reveal that contemporary approaches still expose critical weaknesses in complex, real-world settings, particularly in resolving multi-source aggregation and real-world contextual reasoning.

---


### 100. [iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning](https://arxiv.org/abs/2605.31096)

**<font color=#1a73e8>作者：</font>** Chang-Bin Zhang, Yujie Zhong, Qiang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While visually grounded Chain-of-Thought (CoT) has emerged as a promising paradigm to enhance fine-grained perception in multimodal large language models (MLLMs), its efficacy during the inference phase remains underexplored. In this work, we empirically find that mandating explicit object boxes in visually grounded CoT during inference often degrades performance compared to standard textual CoT, which reasons without explicit visual grounding. We hypothesize that the visual localization capability can be internalized into the textual CoT and that the mandatory explicit grounding introduces unnecessary interference with the model's primary objective of answer prediction. To address this problem, we propose Internalizing Visually Grounded Reasoning (\textbf{iVGR}), a novel reinforcement learning framework that transfers localization capabilities into the textual reasoning process. We employ a dual-stream training strategy, where a textual stream is aligned with a high-quality visually grounded stream via a proposed consistency reward, enabling the model to localize accurately without explicit grounding during inference. Extensive experiments demonstrate that our method significantly outperforms existing baselines on fine-grained benchmarks, while maintaining the flexibility to support tool-assisted inference workflows.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-168](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
