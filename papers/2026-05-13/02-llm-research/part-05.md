# 🧠 大模型相关研究 | 2026年05月13日

> 本类共 **223** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-223**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-223**

---

### 201. [Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training](https://arxiv.org/abs/2605.12380)

**<font color=#1a73e8>作者：</font>** Rasool Fakoor, Murdock Aubry, Nicholas Stranges 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is structurally harder than supervised learning because the policy changes the data distribution it learns from. The resulting fragility is especially visible in large-model training, where the training and rollout systems differ in numerical precision, sampling, and other implementation details. Existing methods manage this fragility by adding hyper-parameters to the training objective, which makes the algorithm more sensitive to its configuration and requires retuning whenever the task, model scale, or distribution mismatch changes. This fragility traces to two concerns that current objectives entangle through hyper-parameters set before training begins: a trust-region concern, that updates should not move the policy too far from its current value, and an off-policy concern, that data from older or different behavior policies should influence the update only to the extent that it remains reliable. Neither concern is a constant to set in advance, and their severity is reflected in the policy-ratio distribution of the current batch. We present a simple yet effective batch-adaptive objective that replaces fixed clipping with the normalized effective sample size of the policy ratios. The same statistic caps the score-function weight and sets the strength of an off-policy regularizer, so the update stays close to the usual on-policy score-function update when ratios are nearly uniform, and tightens automatically when stale or mismatched data cause ratio concentration, while retaining a nonzero learning signal on high-ratio tokens. Experiments across a wide range of settings show that our method matches or exceeds tuned baselines, introducing no new objective hyper-parameters and removing several existing ones. The code is available at this https URL.

---


### 202. [Pretraining Exposure Explains Popularity Judgments in Large Language Models](https://arxiv.org/abs/2605.12382)

**<font color=#1a73e8>作者：</font>** Jamshid Mozafari, Bhawna Piryani, Adam Jatowt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit systematic preferences for well-known entities, a phenomenon often attributed to popularity bias. However, the extent to which these preferences reflect real-world popularity versus statistical exposure during pretraining remains unclear, largely due to the inaccessibility of most training corpora. We provide the first direct, large-scale analysis of popularity bias grounded in fully observable pretraining data. Leveraging the open OLMo models and their complete pretraining corpus, Dolma, we compute precise entity-level exposure statistics across 7.4 trillion tokens. We analyze 2,000 entities spanning five types (Person, Location, Organization, Art, Product) and compare pretraining exposure against Wikipedia pageviews and two elicited LLM popularity signals: direct scalar estimation and pairwise comparison. Our results show that pretraining exposure strongly correlates with Wikipedia popularity, validating exposure as a meaningful proxy for real-world salience during the training period. More importantly, we find that LLM popularity judgments align more closely with exposure than with Wikipedia, especially when elicited via pairwise comparisons. This alignment is strongest for larger models and persists in the long tail, where Wikipedia popularity becomes unreliable. Overall, our findings demonstrate that popularity priors in LLMs are primarily shaped by pretraining statistics rather than external popularity signals, offering concrete evidence that data exposure plays a central role in driving popularity bias.

---


### 203. [Scalable Token-Level Hallucination Detection in Large Language Models](https://arxiv.org/abs/2605.12384)

**<font color=#1a73e8>作者：</font>** Rui Min, Tianyu Pang, Chao Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities, but they still frequently produce hallucinations. These hallucinations are difficult to detect in reasoning-intensive tasks, where the content appears coherent but contains errors like logical flaws and unreliable intermediate results. While step-level analysis is commonly used to detect internal hallucinations, it suffers from limited granularity and poor scalability due to its reliance on step segmentation. To address these limitations, we propose TokenHD, a holistic pipeline for training token-level hallucination detectors. Specifically, TokenHD consists of a scalable data engine for synthesizing large-scale hallucination annotations along with a training recipe featuring an importance-weighted strategy for robust model training. To systematically assess the detection performance, we also provide a rigorous evaluation protocol. Through training within TokenHD, our detector operates directly on free-form text to identify hallucinations, eliminating the need for predefined step segmentation or additional text reformatting. Our experiments show that even a small detector (0.6B) achieves substantial performance gains after training, surpassing much larger reasoning models (e.g., QwQ-32B), and detection performance scales consistently with model size from 0.6B to 8B. Finally, we show that our detector can generalize well across diverse practical scenarios and explore strategies to further enhance its cross-domain generalization capability.

---


### 204. [Question Difficulty Estimation for Large Language Models via Answer Plausibility Scoring](https://arxiv.org/abs/2605.12398)

**<font color=#1a73e8>作者：</font>** Jamshid Mozafari, Bhawna Piryani, Adam Jatowt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Estimating question difficulty is a critical component in evaluating and improving large language models (LLMs) for question answering (QA). Existing approaches often rely on readability formulas, retrieval-based signals, or popularity statistics, which may not fully capture the reasoning challenges posed to modern LLMs. In this paper, we introduce Q-DAPS (Question Difficulty based on Answer Plausibility Scores) method, a novel approach that estimates question difficulty by computing the entropy of plausibility scores over candidate answers. We systematically evaluate Q-DAPS across four prominent QA datasets-TriviaQA, NQ, MuSiQue, and QASC-demonstrating that it consistently outperforms baselines. Moreover, Q-DAPS shows strong robustness across hyperparameter variations and question types. Extensive ablation studies further show that Q-DAPS remains robust across different plausibility estimation paradigms, model sizes, and realistic settings. Human evaluations further confirm strong alignment between Q-DAPS's difficulty estimates and human judgments of question difficulty. Overall, Q-DAPS provides an interpretable, scalable, and bias-resilient approach to question difficulty estimation in modern QA systems.

---


### 205. [OGLS-SD: On-Policy Self-Distillation with Outcome-Guided Logit Steering for LLM Reasoning](https://arxiv.org/abs/2605.12400)

**<font color=#1a73e8>作者：</font>** Yuxiao Yang, Xiaoyun Wang, Weitong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study {on-policy self-distillation} (OPSD), where a language model improves its reasoning ability by distilling privileged teacher distributions along its own on-policy trajectories. Despite the performance gains of OPSD, we identify a common but often overlooked mismatch between teacher and student responses: self-reflected teacher responses can be shifted by reflection-induced bias and response templates, leading to miscalibrated token-level supervision. To mitigate this issue, we propose \methodname, an outcome-guided logit-steering framework that leverages verifiable outcome rewards to contrast successful and failed on-policy trajectories and calibrate teacher logits. By combining outcome-level correctness with dense token-level guidance through logit steering, \methodname stabilizes self-distillation and improves reasoning performance over standard OPSD and other variants across diverse benchmarks.

---


### 206. [Stories in Space: In-Context Learning Trajectories in Conceptual Belief Space](https://arxiv.org/abs/2605.12412)

**<font color=#1a73e8>作者：</font>** Eric Bigelow, Raphaël Sarfati, Daniel Wurgaft 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) update their behavior in context, which can be viewed as a form of Bayesian inference. However, the structure of the latent hypothesis space over which this inference operates remains unclear. In this work, we propose that LLMs assign beliefs over a low-dimensional geometric space - a conceptual belief space - and that in-context learning corresponds to a trajectory through this space as beliefs are updated over time. Using story understanding as a natural setting for dynamic belief updating, we combine behavioral and representational analyses to study these trajectories. We find that (1) belief updates are well-described as trajectories on low-dimensional, structured manifolds; (2) this structure is reflected consistently in both model behavior and internal representations and can be decoded with simple linear probes to predict behavior; and (3) interventions on these representations causally steer belief trajectories, with effects that can be predicted from the geometry of the conceptual space. Together, our results provide a geometric account of belief dynamics in LLMs, grounding Bayesian interpretations of in-context learning in structured conceptual representations.

---


### 207. [Beyond Localization: A Comprehensive Diagnosis of Perspective-Conditioned Spatial Reasoning in MLLMs from Omnidirectional Images](https://arxiv.org/abs/2605.12413)

**<font color=#1a73e8>作者：</font>** Yuangong Chen, Wai Keung Wong, Jiaxing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) show strong visual perception, yet remain limited in reasoning about space under changing viewpoints. We study this challenge as Perspective-Conditioned Spatial Reasoning (PCSR) in 360-degree omnidirectional images, where broad scene coverage reduces ambiguity from partial observations without eliminating the need for viewpoint-dependent inference. To assess this capability, we introduce PCSR-Bench, a diagnostic benchmark of 84,373 question-answer pairs from 2,600 omnidirectional images across 26 indoor environments. PCSR-Bench contains eight tasks spanning foundational perception (e.g., object counting, relative distance, and relative direction) and advanced PCSR, including compositional chains, egocentric rotation, perspective re-anchoring, ego-distortion, and limited-FOV visibility. We evaluate 14 representative MLLMs and observe a substantial perception-reasoning gap: accuracy reaches 57.59% on foundational relative direction, but drops to 13.49% on egocentric rotation, 7.13% on egocentric distortion, and 0.64% on open-ended compositional reasoning. To probe the plasticity of this gap, we conduct an RL-based diagnostic study on a 7B-scale model. Reward shaping improves a matched 7B baseline from 31.10% to 60.06% under a controlled setting, suggesting that PCSR is partial plasticity rather than being fully immutable. Still, the gains are task-selective, sensitive to reward design including both weight allocation and reward formulation, and partially dependent on the evaluation protocol. These results position PCSR as a key bottleneck in current MLLMs and highlight limited but meaningful room for recovery under targeted optimization.

---


### 208. [ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging](https://arxiv.org/abs/2605.12419)

**<font color=#1a73e8>作者：</font>** Neha Verma, Nikhil Mehta, Shao-Chuan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancements in large language model (LLM) development, fine-tuning them for specific tasks often results in the catastrophic forgetting of their general, language-based reasoning abilities. This work investigates and addresses this challenge in the context of the Generative Retrieval (GenRetrieval) task. During GenRetrieval fine-tuning, we find this forgetting occurs rapidly and correlates with the distance between the fine-tuned and original model parameters. Given these observations, we propose ORBIT, a novel approach that actively tracks the distance between fine-tuned and initial model weights, and uses a weight averaging strategy to constrain model drift during GenRetrieval fine-tuning when this inter-model distance exceeds a maximum threshold. Our results show that ORBIT retains substantial text and retrieval performance by outperforming both common continual learning baselines and related regularization methods that also employ weight averaging.

---


### 209. [Formalize, Don't Optimize: The Heuristic Trap in LLM-Generated Combinatorial Solvers](https://arxiv.org/abs/2605.12421)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Yuliang Song, Tao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) struggle to solve complex combinatorial problems through direct reasoning, so recent neuro-symbolic systems increasingly use them to synthesize executable solvers. A central design question is how the LLM should represent the solver, and whether it should also attempt to optimize search. We introduce CP-SynC-XL, a benchmark of 100 combinatorial problems (4,577 instances), and evaluate three solver-construction paradigms: native algorithmic search (Python), constraint modeling through a Python solver API (Python + OR-Tools), and declarative constraint modeling (MiniZinc + OR-Tools). We find a consistent representational divergence: Python + OR-Tools attains the highest correctness across LLMs, while MiniZinc + OR-Tools has lower absolute coverage despite using the same OR-Tools back-end. Native Python is the most likely to return a schema-valid solution that fails verification, whereas solver-backed paths preserve higher conditional fidelity. On the heuristic axis, prompting for search optimization yields only small median speed-ups (1.03-1.12x) and a strongly bimodal effect: many instances slow down, and correctness drops sharply on a long tail of problems. A paired code-level audit traces these regressions to a recurring heuristic trap. Under an efficiency-oriented prompt, the LLM may replace complete search with local approximations (Python), inject unverified bounds (Python + OR-Tools), or add redundant declarative machinery that overwhelms or over-constrains the model (MiniZinc + OR-Tools). These findings support a conservative design principle for LLM-generated combinatorial solvers: use the LLM primarily to formalize variables, constraints, and objectives for verified solvers, and separately check any LLM-authored search optimization before use.

---


### 210. [Predicting Disagreement with Human Raters in LLM-as-a-Judge Difficulty Assessment without Using Generation-Time Probability Signals](https://arxiv.org/abs/2605.12422)

**<font color=#1a73e8>作者：</font>** Yo Ehara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic generation of educational materials using large language models (LLMs) is becoming increasingly common, but assigning difficulty levels to such materials still requires substantial human effort. LLM-as-a-Judge has therefore attracted attention, yet disagreement with human raters remains a major challenge. We propose a method for predicting which LLM-generated difficulty ratings are likely to disagree with human raters, so that such cases can be sent for re-rating. Unlike prior approaches, our method does not rely on generation-time probability signals, which must be collected during rating generation and are often difficult to compare across LLMs. Instead, exploiting the fact that difficulty is an ordinal scale, we use a separate embedding space, such as ModernBERT, and identify disagreement candidates based on the geometric consistency of the rating set. Experiments on English CEFR-based sentence difficulty assessment with GPT-OSS-120B and Qwen3-235B-A22B showed that the proposed method achieved higher AUC for predicting disagreement with human raters than probability-based baselines.

---


### 211. [A Causal Language Modeling Detour Improves Encoder Continued Pretraining](https://arxiv.org/abs/2605.12438)

**<font color=#1a73e8>作者：</font>** Rian Touchent, Eric de la Clergerie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When adapting an encoder to a new domain, the standard approach is to continue training with Masked Language Modeling (MLM). We show that temporarily switching to Causal Language Modeling (CLM) followed by a short MLM decay improves downstream performance. On biomedical texts with ModernBERT, this CLM detour outperforms MLM baselines trained on identical data and compute across 8 French and 11 English biomedical tasks, by +1.2-2.8pp and +0.3-0.8pp respectively, depending on model size. We investigate the reasons for these gains. We find that CLM's dense supervision impacts low transformer layers (0-7) far more than MLM does. Freezing low layers during CLM eliminates the downstream benefit; freezing mid layers preserves it. The representational changes persist through the MLM decay phase, even when it matches the CLM phase in length, and they scale with model capacity. We release ModernCamemBERT-bio and ModernBERT-bio as state-of-the-art biomedical encoders in Base and Large sizes.

---


### 212. [ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models](https://arxiv.org/abs/2605.12446)

**<font color=#1a73e8>作者：</font>** Chen Li, Xiaoling Hu, Songzhu Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often produce answers with high certainty even when they are incorrect, making reliable confidence estimation essential for deployment in real-world scenarios. Verbalized confidence, where models explicitly state their confidence in natural language, provides a flexible and user-facing uncertainty signal that can be applied even when token logits are unavailable. However, existing verbalized-confidence methods often optimize answer generation and confidence generation jointly, which can cause confidence-alignment objectives to interfere with answer accuracy. In this work, we propose a decoupled and order-aware framework for verbalized confidence calibration. Our method first generates an answer and then estimates confidence conditioned on the fixed question--answer pair, allowing confidence optimization without directly perturbing the answer-generation process. To align confidence with correctness likelihood, we construct a sampling-based surrogate from multiple model completions and optimize rank-based reinforcement learning objectives that encourage responses with higher estimated correctness likelihood to receive higher verbalized confidence. Experiments on reasoning and knowledge-intensive benchmarks show that our method improves calibration and failure prediction performance while largely preserving answer accuracy. These results demonstrate that verbalized confidence can be more reliably aligned by decoupling confidence estimation from answer generation and optimizing the relative ordering of confidence across responses.

---


### 213. [The Algorithmic Caricature: Auditing LLM-Generated Political Discourse Across Crisis Events](https://arxiv.org/abs/2605.12452)

**<font color=#1a73e8>作者：</font>** Gunjan, Sidahmed Benabderrahmane, Talal Rahwan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate fluent political text at scale, raising concerns about synthetic discourse during crises and social conflict. Existing AI-text detection often focuses on sentence-level cues such as perplexity, burstiness, or token irregularities, but these signals may weaken as generative systems improve. We instead adopt a Computational Social Science perspective and ask whether synthetic political discourse behaves like an observed online population. We construct a paired corpus of 1,789,406 posts across nine crisis events: COVID-19, the Jan. 6 Capitol attack, the 2020 and 2024 U.S. elections, Dobbs/Roe v. Wade, the 2020 BLM protests, U.S. midterms, the Utah shooting, and the U.S.-Iran war. For each event, we compare observed discourse from social platforms with synthetic discourse generated for the same context. We evaluate four dimensions: emotional intensity, structural regularity, lexical-ideological framing, and cross-event dependency, using mean gaps and dispersion evidence. Across events, synthetic discourse is fluent but population-level unrealistic. It is generally more negative and less dispersed in sentiment, structurally more regular, and lexically more abstract than observed discourse. Observed discourse instead shows broader emotional variation, longer-tailed structural distributions, and more context-specific, colloquial lexical markers. These differences are event-dependent: larger for fast-moving, decentralized crises and smaller for formal or institutionally mediated events. We summarize them with a simple event-level measure, the Caricature Gap. Our findings suggest that the main limitation of synthetic political discourse is not grammar or fluency, but reduced population realism. Population-level auditing complements traditional text-detection and provides a CSS framework for evaluating the social realism of generated discourse.

---


### 214. [Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs](https://arxiv.org/abs/2605.12460)

**<font color=#1a73e8>作者：</font>** Guinan Su, Yanwu Yang, Xueyan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The continued improvements in language model capability have unlocked their widespread use as drivers of autonomous agents, for example in coding or computer use applications. However, the core of these systems has not changed much since early instruction-tuned models like ChatGPT. Even advanced AI agents function on message exchange formats, successively exchanging messages with users, systems, with itself (i.e. chain-of-thought) and tools in a single stream of computation. This bottleneck to a single stream in chat models leads to a number of limitations: the agent cannot act (generate output) while reading, and in reverse, cannot react to new information while writing. Similarly, the agent cannot act while thinking and cannot think while reading or acting on information.
In this work, we show that models can be unblocked by switching from instruction-tuning for sequential message formats to instruction-tuning for multiple, parallel streams of computation, splitting each role into a separate stream. Every forward pass of the language model then simultaneously reads from multiple input streams and generates tokens in multiple output streams, all of which causally depend on earlier timesteps. We argue that this data-driven change remedies a number of usability limitations as outlined above, improves model efficiency through parallelization, improves model security through better separation of concerns and can further improve model monitorability.

---


### 215. [Search Your Block Floating Point Scales!](https://arxiv.org/abs/2605.12464)

**<font color=#1a73e8>作者：</font>** Tanmaey Gupta, Hayden Prairie, Xiaoxia Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization has emerged as a standard technique for accelerating inference for generative models by enabling faster low-precision computations and reduced memory transfers. Recently, GPU accelerators have added first-class support for microscaling Block Floating Point (BFP) formats. Standard BFP algorithms use a fixed scale based on the maximum magnitude of the block. We observe that this scale choice can be suboptimal with respect to quantization errors. In this work, we propose ScaleSearch, an alternative strategy for selecting these scale factors: using a fine-grained search leveraging the mantissa bits in microscaling formats to minimize the quantization error for the given distribution. ScaleSearch can be integrated with existing quantization methods such as Post Training Quantization and low-precision attention, and is shown to improve their performance. Additionally, we introduce ScaleSearchAttention, an accelerated NVFP4-based attention algorithm, which uses ScaleSearch and adapted prior techniques to ensure near-0 performance loss for causal language modeling. Experiments show that ScaleSearch reduces quantization error by 27% for NVFP4 and improves language model PTQ by up to 15 points for MATH500 (Qwen3-8B), while ScaleSearchAttention improves Wikitext-2 PPL by upto 0.77 points for Llama 3.1 70B. The proposed methods closely match baseline performance while providing quantization accuracy improvements.

---


### 216. [ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents](https://arxiv.org/abs/2605.12481)

**<font color=#1a73e8>作者：</font>** Xuhao Hu, Xi Zhang, Haiyang Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer Use Agents (CUAs) can act through both atomic GUI actions, such as click and type, and high-level tool calls, such as API-based file operations, but this hybrid action space often leaves them uncertain about when to continue with GUI actions or switch to tools, leading to suboptimal execution paths. This difficulty stems from the scarcity of high-quality interleaved GUI-Tool trajectories, the cost and brittleness of collecting real tool trajectories, and the lack of trajectory-level supervision for GUI-Tool path selection. In this paper, we propose ToolCUA, an end-to-end agent designed to learn optimal GUI-Tool path selection through a staged training paradigm. We first introduce an Interleaved GUI-Tool Trajectory Scaling Pipeline that repurposes abundant static GUI trajectories and synthesizes a grounded tool library, enabling diverse GUI-Tool trajectories without manual engineering or real tool-trajectory collection. We then perform Tool-Bootstrapped GUI RFT, combining warmup SFT with single-turn RL to improve decisions at critical GUI-Tool switching points. Finally, we optimize ToolCUA with Online Agentic RL in a high-fidelity GUI-Tool environment, guided by a Tool-Efficient Path Reward that encourages appropriate tool use and shorter execution paths. Experiments on OSWorld-MCP show that ToolCUA achieves 46.85% accuracy, a relative improvement of approximately 66% over the baseline, establishing a new state of the art among models of comparable scale. It also improves by 3.9% over GUI-only settings, demonstrating effective GUI-Tool orchestration. The results further suggest that training in a hybrid action space is a promising paradigm for real-world digital agents. Open-sourced here: this https URL

---


### 217. [Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training](https://arxiv.org/abs/2605.12483)

**<font color=#1a73e8>作者：</font>** Yuanda Xu, Hejian Sang, Zhengze Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In settings where labeled verifiable training data is the binding constraint, each checked example should be allocated carefully. The standard practice is to use this data directly on the model that will be deployed, for example by running GRPO on the deployment student. We argue that this is often an inefficient allocation because it overlooks a reward-density principle: sparse sequence-level reward should train models where exploration is productive, while dense token-level teacher reward should be used where the aim is to compress behavior into a smaller model. In this view, GRPO-style sparse RL and OPD-style dense teacher supervision are not separate recipes; they are different reward-density regimes. The allocation rule is simple: use scarce labeled training data upstream on the strongest model that can turn it into reward-shaped behavior, then transfer that behavior downstream as dense supervision. We evaluate this rule on verifiable math with Qwen3 and Llama models. At fixed Qwen3-1.7B deployment-student size, an RL-improved 8B teacher distilled through the dense bridge outperforms direct GRPO on the same student, while transfer from the same teacher before RL underperforms. The bridge is important: a forward-KL warmup on teacher rollouts followed by OPD on student rollouts is consistently strongest on MATH before any post-bridge student-side sparse RL, and also gives the best pre-Stage~3 AIME endpoints for the canonical 8B/14B teachers. The bridge also makes later student-side sparse RL effective: GRPO that is weak on a cold student lifts MATH from $75.4\%$ to $78.5\%$ after the bridge and outperforms a matched replay control by $2.8$ points. The operational principal is to avoid using scarce labeled data on the least prepared policy: use sparse reward for teacher-side discovery, dense transfer for student compression, and student-side sparse reward only after the bridge.

---


### 218. [Learning, Fast and Slow: Towards LLMs That Adapt Continually](https://arxiv.org/abs/2605.12484)

**<font color=#1a73e8>作者：</font>** Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are trained for downstream tasks by updating their parameters (e.g., via RL). However, updating parameters forces them to absorb task-specific information, which can result in catastrophic forgetting and loss of plasticity. In contrast, in-context learning with fixed LLM parameters can cheaply and rapidly adapt to task-specific requirements (e.g., prompt optimization), but cannot by itself typically match the performance gains available through updating LLM parameters. There is no good reason for restricting learning to being in-context or in-weights. Moreover, humans also likely learn at different time scales (e.g., System 1 vs 2). To this end, we introduce a fast-slow learning framework for LLMs, with model parameters as "slow" weights and optimized context as "fast" weights. These fast "weights" can learn from textual feedback to absorb the task-specific information, while allowing slow weights to stay closer to the base model and persist general reasoning behaviors. Fast-Slow Training (FST) is up to 3x more sample-efficient than only slow learning (RL) across reasoning tasks, while consistently reaching a higher performance asymptote. Moreover, FST-trained models remain closer to the base LLM (up to 70% less KL divergence), resulting in less catastrophic forgetting than RL-training. This reduced drift also preserves plasticity: after training on one task, FST trained models adapt more effectively to a subsequent task than parameter-only trained models. In continual learning scenarios, where task domains change on the fly, FST continues to acquire each new task while parameter-only RL stalls.

---


### 219. [Task-Adaptive Embedding Refinement via Test-time LLM Guidance](https://arxiv.org/abs/2605.12487)

**<font color=#1a73e8>作者：</font>** Ariel Gera, Shir Ashury-Tahan, Gal Bloch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We explore the effectiveness of an LLM-guided query refinement paradigm for extending the usability of embedding models to challenging zero-shot search and classification tasks. Our approach refines the embedding representation of a user query using feedback from a generative LLM on a small set of documents, enabling embeddings to adapt in real time to the target task. We conduct extensive experiments with state-of-the-art text embedding models across a diverse set of challenging search and classification benchmarks. Empirical results indicate that LLM-guided query refinement yields consistent gains across all models and datasets, with relative improvements of up to +25% in literature search, intent detection, key-point matching, and nuanced query-instruction following. The refined queries improve ranking quality and induce clearer binary separation across the corpus, enabling the embedding space to better reflect the nuanced, task-specific constraints of each ad-hoc user query. Importantly, this expands the range of practical settings in which embedding models can be effectively deployed, making them a compelling alternative when costly LLM pipelines are not viable at corpus-scale. We release our experimental code for reproducibility, at this https URL.

---


### 220. [AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward](https://arxiv.org/abs/2605.12495)

**<font color=#1a73e8>作者：</font>** Runhui Huang, Jie Wu, Rui Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose AlphaGRPO, a novel framework that applies Group Relative Policy Optimization (GRPO) to AR-Diffusion Unified Multimodal Models (UMMs) to enhance multimodal generation capabilities without an additional cold-start stage. Our approach unlocks the model's intrinsic potential to perform advanced reasoning tasks: Reasoning Text-to-Image Generation, where the model actively infers implicit user intents, and Self-Reflective Refinement, where it autonomously diagnoses and corrects misalignments in generated outputs. To address the challenge of providing stable supervision for real-world multimodal generation, we introduce the Decompositional Verifiable Reward (DVReward). Unlike holistic scalar rewards, DVReward utilizes an LLM to decompose complex user requests into atomic, verifiable semantic and quality questions, which are then evaluated by a general MLLM to provide reliable and interpretable feedback. Extensive experiments demonstrate that AlphaGRPO yields robust improvements across multimodal generation benchmarks, including GenEval, TIIF-Bench, DPG-Bench and WISE, while also achieving significant gains in editing tasks on GEdit without training on editing tasks. These results validate that our self-reflective reinforcement approach effectively leverages inherent understanding to guide high-fidelity generation. Project page: this https URL

---


### 221. [From Web to Pixels: Bringing Agentic Search into Visual Perception](https://arxiv.org/abs/2605.12497)

**<font color=#1a73e8>作者：</font>** Bokang Yang, Xinyi Sun, Kaituo Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception connects high-level semantic understanding to pixel-level perception, but most existing settings assume that the decisive evidence for identifying a target is already in the image or frozen model knowledge. We study a more practical yet harder open-world case where a visible object must first be resolved from external facts, recent events, long-tail entities, or multi-hop relations before it can be localized. We formalize this challenge as Perception Deep Research and introduce WebEye, an object-anchored benchmark with verifiable evidence, knowledge-intensive queries, precise box/mask annotations, and three task views: Search-based Grounding, Search-based Segmentation, and Search-based VQA. WebEyes contains 120 images, 473 annotated object instances, 645 unique QA pairs, and 1,927 task samples. We further propose Pixel-Searcher, an agentic search-to-pixel workflow that resolves hidden target identities and binds them to boxes, masks, or grounded answers. Experiments show that Pixel-Searcher achieves the strongest open-source performance across all three task views, while failures mainly arise from evidence acquisition, identity resolution, and visual instance binding.

---


### 222. [SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://arxiv.org/abs/2605.12500)

**<font color=#1a73e8>作者：</font>** Haiwen Diao, Penghao Wu, Hanming Deng 等 58 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large vision-language models (VLMs) remain fundamentally constrained by a persistent dichotomy: understanding and generation are treated as distinct problems, leading to fragmented architectures, cascaded pipelines, and misaligned representation spaces. We argue that this divide is not merely an engineering artifact, but a structural limitation that hinders the emergence of native multimodal intelligence. Hence, we introduce SenseNova-U1, a native unified multimodal paradigm built upon NEO-unify, in which understanding and generation evolve as synergistic views of a single underlying process. We launch two native unified variants, SenseNova-U1-8B-MoT and SenseNova-U1-A3B-MoT, built on dense (8B) and mixture-of-experts (30B-A3B) understanding baselines, respectively. Designed from first principles, they rival top-tier understanding-only VLMs across text understanding, vision-language perception, knowledge reasoning, agentic decision-making, and spatial intelligence. Meanwhile, they deliver strong semantic consistency and visual fidelity, excelling in conventional or knowledge-intensive any-to-image (X2I) synthesis, complex text-rich infographic generation, and interleaved vision-language generation, with or without think patterns. Beyond performance, we show detailed model design, data preprocessing, pre-/post-training, and inference strategies to support community research. Last but not least, preliminary evidence demonstrates that our models extend beyond perception and generation, performing strongly in vision-language-action (VLA) and world model (WM) scenarios. This points toward a broader roadmap where models do not translate between modalities, but think and act across them in a native manner. Multimodal AI is no longer about connecting separate systems, but about building a unified one and trusting the necessary capabilities to emerge from within.

---


### 223. [Covering Human Action Space for Computer Use: Data Synthesis and Benchmark](https://arxiv.org/abs/2605.12501)

**<font color=#1a73e8>作者：</font>** Miaosen Zhang, Xiaohan Zhao, Zhihong Tan 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) automate on-screen work, as illustrated by GPT-5.4 and Claude. Yet their reliability on complex, low-frequency interactions is still poor, limiting user trust. Our analysis of failure cases from advanced models suggests a long-tail pattern in GUI operations, where a relatively small fraction of complex and diverse interactions accounts for a disproportionate share of task failures. We hypothesize that this issue largely stems from the scarcity of data for complex interactions. To address this problem, we propose a new benchmark CUActSpot for evaluating models' capabilities on complex interactions across five modalities: GUI, text, table, canvas, and natural image, as well as a variety of actions (click, drag, draw, etc.), covering a broader range of interaction types than prior click-centric benchmarks that focus mainly on GUI widgets. We also design a renderer-based data-synthesis pipeline: scenes are automatically generated for each modality, screenshots and element coordinates are recorded, and an LLM produces matching instructions and action traces. After training on this corpus, our Phi-Ground-Any-4B outperforms open-source models with fewer than 32B parameters. We will release our benchmark, data, code, and models at this https URL

---


> [!TIP]
> 当前位于：**201-223**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-223**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
