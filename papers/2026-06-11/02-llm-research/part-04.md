# 🧠 大模型相关研究 | 2026年06月11日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-188**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-188**

---

### 151. [Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?](https://arxiv.org/abs/2606.10956)

**<font color=#1a73e8>作者：</font>** Tengchao Lv, Dongdong Zhang, Jiayu Ding 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of Large Language Model (LLM) agents for computer automation is accelerating, yet their ability to navigate complex, professional-grade productivity software is largely untested. We argue that Office automation is an ideal environment for benchmarking document-automation capability, as it requires long-horizon planning and reasoning, precise parameter configuration, and multi-application integration. To quantify this capability, we introduce an evaluation based on China's National Computer Rank Examination (NCRE), featuring 200 comprehensive practical-operation tasks across Word, Excel, and PowerPoint. Each task is scored on a 100-point rubric scale using 7,118 machine-gradable criteria, and Score Rate (SR) denotes the mean percentage of rubric points earned across these tasks. We benchmark 7 frontier LLMs and observe stark limitations: single-turn models score a maximum of 36.6%. A stronger agentic system with execution feedback, iterative repair, and broader Office automation access reaches 68.8%, but remains below the 95.5% community-reference score used as a scoring sanity check. Ultimately, our experiments demonstrate that despite recent advancements in code generation, achieving reliable fine-grained Office document automation remains a significant challenge for current code-generating LLM and agent systems.

---


### 152. [Quo Vadis, Visual In-Context Learning? A Unified Benchmark Across Domains and Tasks](https://arxiv.org/abs/2606.10967)

**<font color=#1a73e8>作者：</font>** Pradnya Halady, Jiale Wei, Zdravko Marinov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual in-context learning has been proposed as a pathway towards dynamic models that can generate predictions based on a provided context and thereby can adapt to new vision tasks at test-time. Yet, the evaluation of the adaptation capabilities of these models has been limited to narrow setups that mainly mirror tasks or image domains from pre-training for which real adaptation is not required. We address this gap by constructing a broad Visual In-Context BEnchmark (VIBE) with a focus on diverse imaging domains and a wide range of tasks. With this, we are able to get a much clearer picture of the adaptive capabilities of visual in-context models when faced with new image- and task distributions. We stress test six models on $14$ datasets and $12$ tasks (in total, we explore $106$ dataset-task combinations) and compare them under a unified, reproducible evaluation protocol, in an one-shot setting. Our evaluation uncovers key insights on the state of visual in-context learning, including limitations, systematic failure modes and promising directions. To foster broader evaluation, we will openly release our VIBE toolkit.

---


### 153. [Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning](https://arxiv.org/abs/2606.10968)

**<font color=#1a73e8>作者：</font>** Renjie Mao, Xiangxin Zhou, Lvfang Tao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become standard for improving LLM reasoning. However, existing PPO-style trust-region mechanisms remain position-agnostic by enforcing uniform thresholds across all tokens independently. This pointwise treatment conflicts with autoregressive generation in two critical ways. First, uniform thresholds ignore autoregressive asymmetry. Early-stage deviations produce compounding sequence-level drift, causing static thresholds to under-regulate early divergence and excessively constrain late-stage exploration. Second, evaluating token-level divergence in isolation overlooks cumulative prefix drift, granting the same divergence allowance regardless of how far the conditioning history has already deviated from the rollout policy. To address this limitation, we propose CPPO (Cumulative Prefix-divergence Policy Optimization), a token-level masking rule that aligns updates with a finite-horizon policy-improvement bound via two coupled mechanisms. First, a position-weighted threshold imposes stricter limits at early positions whose effects persist longer, relaxing constraints for late-stage tokens. Second, a cumulative prefix budget tracks historical deviations, dynamically restricting further token-level deviation to prevent compounding errors along the prefix. Empirically, CPPO enhances training stability and significantly improves reasoning accuracy across various model scales.

---


### 154. [Bellman-Taylor Score Decoding for Markov Decision Processes with State-Dependent Feasible Action Sets](https://arxiv.org/abs/2606.10979)

**<font color=#1a73e8>作者：</font>** Yi Chen, Rushuai Yang, Qiang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many Markov decision processes (MDPs) in operations research have feasible actions that are state dependent and defined implicitly by various operational constraints. These features make it difficult to use standard deep reinforcement learning (DRL) algorithms, whose action interfaces typically assume either a fixed finite action catalog or a simple Euclidean space. Motivated by a Taylor expansion of the optimal action-value function, we propose Bellman--Taylor score decoding, a framework that moves policy learning to a Euclidean score space while enforcing feasibility through an action decoder. The induced latent-score MDP then can be optimized by standard DRL algorithms without differentiating through the decoder. We provide a performance guarantee showing that the optimality gap of this approach decomposes into a structural approximation error and an algorithmic learning error. Lastly, we apply this framework to a queueing network control problem, where the policy essentially learns a state-dependent index-based dispatching rule. Numerical experiments show near-optimal performance in small instances and considerable improvements over benchmarks in larger systems.

---


### 155. [Null-Space Constrained Low-Rank Adaptation for Response-Specified Large Language Model Unlearning](https://arxiv.org/abs/2606.10989)

**<font color=#1a73e8>作者：</font>** Bocheng Ju, Jianhua Wang, Chengliang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model unlearning aims to suppress designated undesirable knowledge while preserving benign capabilities. Many unlearning objectives focus on suppressing undesired answers, while recent target-guided variants specify replacement behavior but still leave update locality largely unconstrained. This paper introduces \emph{Null-Space Constrained Response-Specified Unlearning} (NSRU), a projection-constrained low-rank framework for controlled LLM unlearning. NSRU uses an explicitly structured safe target response to specify the desired behavior for each forget query, while suppressing the original undesired content. To localize adaptation, NSRU estimates per-module retain subspaces from benign hidden representations and uses an orthogonal-projected low-rank parameterization to confine LoRA updates to the null space of the retain subspace. The resulting objective jointly optimizes safe-target learning, undesired-response suppression, and retention preservation under this constrained parameterization. We provide a local first-order analysis showing that the projected update reduces retain-side perturbations while preserving editable directions for shaping forget-query behavior. Experiments on TOFU show that NSRU effectively suppresses extractable forget-set knowledge while improving retain QA performance, model utility, and safe-target alignment over representative baselines. On WMDP, NSRU keeps hazardous-domain accuracy near the random-choice region while preserving broad and domain-adjacent MMLU utility. Ablation studies support the complementary roles of safe-target supervision, undesired-response suppression, retention loss, and null-space projected updates, while sensitivity and robustness analyses indicate stable behavior across the tested hyperparameter and prompt variations.

---


### 156. [Who Brought Easter Eggs to Eid? Auditing Cultural Translation of Math Word Problems Across Diverse Languages and Regions](https://arxiv.org/abs/2606.11009)

**<font color=#1a73e8>作者：</font>** Parisa Suchdev, Juniper Lovato  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to adapt math word problems for personalized learning at scale, but it remains an open question whether those adaptations are consistent across models, preserve cultural diversity at scale, and reveal which cultural entities models treat as most salient. We analyze how Claude Opus 4, GPT-4.1, and Gemini 2.5 Pro adapt 60 English math word problems into Bengali, Hindi, Punjabi (India), Urdu, Sindhi (Pakistan), Italian, and Sicilian (Italy), a language set spanning the full resource spectrum, from high-resource Italian and Hindi to under-studied Sindhi, Sicilian, and Punjabi. We annotate 6,489 entity transformations, coding whether models preserve, localize, generalize, omit, or change entities such as names, foods, and places. Models agree on transformation type in 62.5% of cases and on specific substitutions in only 33.5%, meaning model choice directly shapes which cultural world students encounter. All 21 language-model combinations show entropy collapse, with adaptation compressing rather than expanding cultural diversity. Models prioritize surface markers such as names, foods, and currencies while preserving deeper structural features such as grade-level systems that embed culturally specific assumptions. Despite prompts specifying target countries, models misattribute regional context by using Bangladeshi taka for Indian Bengali students and produce cross-cultural contamination, such as adapting egg hunts as Eid activities. Some failures are visible in individual translations. Others, including diversity collapse, systematic preference for surface markers, and consistent regional misattribution, emerge only through corpus-level analysis. The surface plausibility that makes adapted problems look correct is precisely what makes deeper failures easy to overlook.

---


### 157. [Structure from Reasoning, Numbers from Search: On-Premise Open LLMs as Structural Priors for Coupled MIMO Controller Tuning](https://arxiv.org/abs/2606.11015)

**<font color=#1a73e8>作者：</font>** Jiaxuan Chen, Haonan Li, Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tuning controllers for strongly coupled multi-input multi-output (MIMO) industrial processes is hard: decentralized classical auto-tuning ignores loop interaction, and local numerical optimization from natural initializations stalls in the resulting non-convex cost landscape. We ask whether on-premise open-source large language models (LLMs), which keep data on-site and need no plant model, can help. On a single-loop CSTR, classical relay-feedback tuning (IAE 0.106, near the 0.102 optimum) beats an LLM tuner (0.162): for simple loops the LLM adds nothing. The picture inverts on a strongly coupled quadruple-tank with conflicting set-points, scored by a penalized cost J = IAE + lambda*TV(u) that rewards tracking without chattering actuators. There, naive relay tuning (J ~ 28.6) and naive LLM tuning (29.7) are no better than open loop (22.7), and a local optimizer from balanced starts fails in 10/10 runs. A scaffolded open LLM instead reasons about the coupling, proposes the counter-intuitive asymmetric structure, and reaches J ~ 16.9 +/- 0.2 from any start; refining it with a classical optimizer attains the smooth global optimum (J ~ 12.0, 10/10 vs. 0/10), which even applies a non-obvious negative integral correction decentralized tuning cannot. A global optimizer (differential evolution) also reaches this optimum, so the LLM is not the only route; its advantage is sample efficiency and interpretability: a usable controller in 18 evaluations (where the global optimizer is worse than open loop) plus a stated rationale. This edge grows with dimension, reaching ~6x fewer evaluations on a 3x3 plant. The behaviour generalizes across four open models, and on a benign plant the LLM offers no advantage, sharpening the boundary. We contribute a reproducible benchmark delimiting when open LLMs help in control tuning: not as optimizers, but as a sample-efficient, interpretable structural prior.

---


### 158. [Superficial Beliefs in LLM Decision-Making](https://arxiv.org/abs/2606.11016)

**<font color=#1a73e8>作者：</font>** Gabriel Freedman, Francesca Toni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We ask whether large language models (LLMs) merely imitate rationales when choosing between two options, or whether their choices reflect a systematic underlying decision structure. Using synthetic binary decision settings in which models choose between profiles defined by graded attributes, we compare the attribute a model says mattered most with the attribute that best explains its choice under a behavioural model fit to prior decisions. The behavioural model predicts held-out choices well, showing that model behaviour is systematically related to the visible attributes rather than being random. However, direct self-reports and a separate score-based judge recover the behaviourally inferred driver only partially. The resulting picture is neither one of arbitrary behaviour nor one of fully articulated belief - outputs are structured enough to support prediction, but explicit reasons track the recovered driver only imperfectly. This qualitative pattern persists across prompt-order and sampling perturbations, alternative behavioural models, targeted occlusion analyses, and structurally varied decision settings. We interpret this as evidence for ``superficial belief'' in LLM decision-making: models behave as if guided by probabilistic local priorities over attributes, while having only limited verbal access to the attributes that drive their decisions.

---


### 159. [Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer](https://arxiv.org/abs/2606.11018)

**<font color=#1a73e8>作者：</font>** Maria Milkova, Maksim Rudnev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measuring subjective constructs in naturally occurring social media text requires annotation procedures that are theoretically grounded, empirically validated, and transferable to an encoder model for scalable prediction. Using non-English social media posts annotated according to Schwartz's theory of basic human values, we investigate how different LLMs, prompts, and instruction languages operationalize the expression of values in text. We argue that although texts may permit multiple plausible interpretations, theory-based value definitions can constrain interpretations and reduce spurious value attributions. Beyond precision, recall, and F1, we evaluate structural alignment between values, error structure, confidence-ambiguity relations, and annotation stability. We show that different LLMs produce different value interpretations. Iterative prompt calibration through error analysis reduces misattributions and improves alignment with expert annotations. We also derive targeted expert verification rules from recurrent error structures and use them during corpus annotation. Finally, we show that LLM annotations can be transferred to an encoder model through soft-label training, retaining theory-based value interpretations and information about uncertainty in value expression.

---


### 160. [AuRA: Internalizing Audio Understanding into LLMs as LoRA](https://arxiv.org/abs/2606.11033)

**<font color=#1a73e8>作者：</font>** Bo Cheng, Lei Shi, Zhanyu Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent efforts to extend large language models (LLMs) to speech inputs typically rely on cascaded ASR-LLM pipelines, end-to-end speech-language models, or bridge/distillation-based adaptation. While these routes respectively reuse strong pretrained components, enable native speech-language interaction, or offer lightweight adaptation, they often suffer from transcript-interface latency, costly multimodal training, or sequential speech-language coupling. To address these limitations, we present AuRA, a method that distills audio encoding capability into the LLM. Specifically, AuRA feeds the same speech input to an ASR encoder (as a teacher) and a LoRA-adapted LLM (as a student) through a lightweight audio embedding layer, and uses layer-wise distillation to align the student's hidden states with corresponding teacher representations, thereby internalizing speech representations into lightweight LLM-side adaptations. Compared with cascaded and serial bridge methods, AuRA enables tighter speech-language joint modeling and efficient parallel end-to-end inference, while also reusing pretrained speech and language models rather than requiring large-scale multimodal training. On multiple speech-language benchmarks, AuRA consistently outperforms cascaded systems, speech-to-LLM adaptation baselines, and large-scale speech-language and multimodal models in both effectiveness and efficiency.

---


### 161. [Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields](https://arxiv.org/abs/2606.11042)

**<font color=#1a73e8>作者：</font>** Liya Zhu, Jingzhe Ding, Jian Zhang 等 57 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed the rapid evolution of AI agents toward handling increasingly complex, real-world tasks. However, existing benchmarks rarely evaluate whether agents can operate graphical user interfaces to complete long-horizon, high-value professional workflows across diverse domains. Current GUI benchmarks still predominantly focus on general-purpose software, relatively simple applications, and short-horizon tasks, leaving it largely unknown whether modern agents can follow user instructions to autonomously operate domain-specific professional software and accomplish economically valuable work in an end-to-end manner. To bridge this gap, we introduce Workflow-GYM, a benchmark for long-horizon GUI tasks centered on professional domains and specialized software environments. Through extensive experiments on state-of-the-art models, we find that even the strongest models achieve only slightly above 30% success rates, highlighting that professional long-horizon GUI workflows remain highly challenging for current GUI agents. Further analysis reveals that current agents struggle to maintain long-horizon workflow consistency, frequently exhibiting workflow stage omission, error propagation, objective drift, and insufficient understanding of professional software environments. Our findings provide important insights into the limitations of current agent systems and suggest key directions for the next generation of GUI-agent research.

---


### 162. [Does Reasoning Preserve Alignment? On the Trustworthiness of Large Reasoning Models](https://arxiv.org/abs/2606.11046)

**<font color=#1a73e8>作者：</font>** Prajakta Kini, Avinash Reddy, Souradip Chakraborty 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned LLMs are increasingly converted into reasoning models through post-training to improve multi-step task performance. This conversion is usually optimized for reasoning accuracy, without explicitly preserving the alignment behavior of the instruction-tuned model, such as safe refusal, bias avoidance, and privacy protection. We ask: does this conversion preserve alignment? We study this question through a trustworthiness audit and find that it is not behavior-preserving by default. For a systematic analysis, we compare reasoning models produced via supervised fine-tuning, RL-based post-training, and distillation against matched instruction-tuned baselines across six trustworthiness dimensions: safety, toxicity, stereotyping and bias, machine ethics, privacy, and out-of-distribution robustness. We observe that reasoning models often improve on reasoning benchmarks but exhibit alignment regressions, including increased toxicity, amplified stereotyping, miscalibrated refusal, and contextual privacy leakage. These regressions are consistent with behavioral drift from the instruction-tuned baseline, measured by KL divergence. Overall, our results point to the broader conclusion that trustworthiness metrics are essential for evaluating reasoning models and should be reported alongside gains in reasoning capability.

---


### 163. [LLM-Mediated Demand Response Coordination in Smart Microgrids](https://arxiv.org/abs/2606.11050)

**<font color=#1a73e8>作者：</font>** J. de Curtò, I. de Zarzà  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Effective demand response in smart microgrids requires prosumers to cooperate voluntarily under strategic self-interest, a coordination problem structurally equivalent to a repeated Prisoner's Dilemma on a social network. This paper presents a multi-agent simulation in which a Large Language Model (LLM) Influence Compiler issues structured demand-response directives to a population of heterogeneous prosumer agents, each governed by a hybrid decision architecture combining game-theoretic base probability (derived from payoff history, neighbour imitation, and exploitation memory) with LLM narrative evaluation of incoming coordination signals. The hybrid architecture resolves a key methodological challenge: LLMs aligned via Reinforcement Learning from Human Feedback (RLHF) exhibit strong cooperation bias when used as direct decision-makers, producing flat dynamics regardless of grid conditions. By separating strategic reasoning from grounded narrative evaluation, the model generates realistic prosumer behaviour across six personality archetypes, with baseline cooperation near 50% and clear differentiation under influence. Compiled structured directives achieve 33.3% demand-curtailment cooperation versus 27.0% for unstructured messaging and 28.0% for a no-intervention baseline ($\Delta_\mathrm{comp} = +0.063$), with the advantage preserved across both grounded and idealized agent substrates ($\Delta = +0.083$) and across all resistance levels ($R = 0.1$ to $0.7$). Hub-targeted dissemination via high-centrality network nodes outperforms peripheral or random targeting, confirming that grid topology provides mechanistic amplification independent of message content. These results suggest that structured LLM compilation, grounded agent reasoning, and network-aware targeting are complementary design principles for scalable, interpretable demand-response coordination in smart-city energy systems.

---


### 164. [Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It](https://arxiv.org/abs/2606.11052)

**<font color=#1a73e8>作者：</font>** Xinyu Zhou, Boyu Zhu, Yi Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) supervised fine-tuning (SFT) is widely adopted to improve reasoning ability, yet we find that it systematically degrades long-context recall in hybrid linear-attention models. Across architectures including HypeNet and Jet-Nemotron, retrieval performance on Needle-In-A-Haystack (NIAH) deteriorates substantially after CoT-SFT, and the degradation becomes more severe under harder retrieval settings and longer context windows. For example, HypeNet-9B on NIAH-S2@256K decreases from $67.2\%$ to $9.4\%$. We attribute this to CoT-SFT biasing attention gradients toward short-range patterns, disrupting query-key projections ($W_Q, W_K$) that are responsible for long-range routing. Motivated by this observation, we propose QK-Restore, a training-free method that restores only $W_Q$ and $W_K$ from the pre-SFT checkpoint while preserving all other post-SFT parameters. We further introduce a Procrustes variant to balance routing preservation and reasoning adaptation. Across architectures, QK-Restore consistently restores long-context capability at zero training cost while preserving reasoning performance; for instance, on HypeNet-5B it improves S3@256K from $65.4\%$ to $76.4\%$ while maintaining strong reasoning performance.

---


### 165. [CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs](https://arxiv.org/abs/2606.11063)

**<font color=#1a73e8>作者：</font>** Joachim Schaeffer, Thomas Jiralerspong, Alexander Panfilov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI control protocols oversee untrusted models by monitoring their actions and modifying potentially unsafe steps, often using a trusted model. This partially tampers with the untrusted model's trajectory. If the trusted model detects such an intervention, it may infer properties of the monitor and adapt to evade control. We introduce \textbf{CIAware-Bench}, a benchmark for measuring \textbf{c}ontrol \textbf{i}ntervention (CI) awareness across frontier models. CIAware-Bench tests whether models can distinguish their own trajectories from those modified by a control intervention. The benchmark is comprised of a suite of four task domains (essay writing, BigCodeBench, Bash Arena, and SHADE-Arena), while varying trajectory watermarking, side-task presence, and the control protocol. Evaluating eleven frontier models, we find low to moderate CI awareness under default settings (up to 0.87; random chance balanced binary classification accuracy is 0.5) with substantial variation across task domains and model pairs. Detection is generally easier across model families, suggesting that models exploit provider-specific differences in style or post-training. Overall, CI awareness is not a fixed model-level property, and should be measured for each new model release and deployment scenario. We release CIAware-Bench to track CI awareness and inform control protocols whose interventions are harder to detect.

---


### 166. [T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains](https://arxiv.org/abs/2606.11070)

**<font color=#1a73e8>作者：</font>** Genta Indra Winata, Amartya Chakraborty, Yuzhen Lin 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in reasoning and tool-calling capabilities of large language models (LLMs) have enabled increasingly capable agentic systems. However, existing benchmarks remain limited in task complexity, realism, and domain diversity, and often fail to capture interactions that span multiple domains, limiting their ability to evaluate agents in realistic multi-step settings that require sustained reasoning and coordination. To address these limitations, we introduce T1-Bench, a high-fidelity, comprehensive benchmark for evaluating agentic systems in realistic customer-facing, multi-domain environments, featuring interleaved scenarios that require structured reasoning across multi-turn user-assistant interactions and substantially increasing both compositional complexity and evaluative rigor across 25 domains of varying difficulty. We evaluate T1-Bench using 12 proprietary and open-weight models, providing a reproducible and standardized framework for assessing agent behavior, tool utilization, and conversational quality in complex, multi-step environments. We further complement automatic evaluation with human judgments to strengthen the assessment of qualitative performance. Overall, T1-Bench substantially advances prior benchmarks by increasing task complexity, interaction depth, and domain coverage in simulated multi-domain environments. To facilitate future research on agentic systems, we will publicly release data and evaluation code as open source.

---


### 167. [Modeling Complex Behaviors: Multi-Personality Composition and Dynamic Switching in Vision-Language Models](https://arxiv.org/abs/2606.11074)

**<font color=#1a73e8>作者：</font>** Peiqi Jia, Haonan Jia, Ziqi Miao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the widespread deployment of Multimodal Large Language Models (MLLMs) in social interaction, understanding and controlling their behavior under complex personality conditions is essential. This paper introduces explicit personality conditioning and establishes a systematic evaluation framework encompassing single-personality induction, multi-personality induction, and personality switching. Experiments show that personality induction improves image captioning performance but can impair performance on tasks requiring precise reasoning, such as visual question answering (VQA). Balancing and residual effects are observed during multi-trait composition and dynamic switching, indicating that model behavior is co-modulated by both previous and current personality constraints. Existing prompt-based personality induction methods show limited transferability to multimodal settings. Our work reveals the dynamic and complex nature of personality modeling in MLLMs and underscores the need for robust, tailored methods for personality induction and evaluation. The code will be released when the paper is accepted.

---


### 168. [A History-Aware Visually Grounded Critic for Computer Use Agents](https://arxiv.org/abs/2606.11078)

**<font color=#1a73e8>作者：</font>** Jaewoo Lee, Zaid Khan, Archiki Prasad 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User Interface (GUI) environments. However, existing critics suffer from two key limitations: they (1) focus primarily on short-sighted decision loops (e.g., forgetting earlier actions) and (2) lack the visual grounding needed to detect flawed actions (e.g., clicking wrong UI elements). To address these, we introduce HiViG, a History-aware Visually Grounded test-time framework, built around a multimodal critic trained on real GUI trajectories to abstract past interactions into a compact record and to evaluate actions with visual grounding. At test time, HiViG integrates the critic into the policy decision loop to provide macro-action history, which summarizes the policy's completed achievements, and visually grounded critique, which verifies raw execution coordinates against the current screenshot to intercept errors before execution. Across web, mobile, and desktop benchmarks, HiViG consistently outperforms existing scalar and verbal critics, improving average success rates over the strongest baseline by 5.8% for Qwen3-VL-32B and 9.0% for Gemini-3-Flash, and demonstrates strong cross-platform generalization. Ablations show that macro-action history mitigates short-sighted planning and visually grounded critique reduces execution errors, with both components being critical for test-time scaling in long-horizon GUI tasks.

---


### 169. [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/abs/2606.11081)

**<font color=#1a73e8>作者：</font>** Pietro Cagnasso, Eugene Belilovsky, Edouard Oyallon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links. Many practical methods reduce communication frequency but still rely on synchronous All-Reduce operations that maintain identical model states and tie progress to global collectives. This can become a bottleneck when bandwidth or worker speed is heterogeneous. We introduce GASLoC, a novel decentralized pre-training algorithm that generalizes the notion of communication acceleration to the recently popular "outer optimizer" to allow a practical gossip-based training framework that is compatible with adaptive optimizers, allows for local optimizer steps, and can utilize sparse randomized peer communication. Empirically, on a number of standard LLM training tasks, we demonstrate that GASLoC outperforms state-of-the-art decentralized algorithms in single step per communication setting for a number of topologies and, unlike existing decentralized methods in the LLM setting, it allows to obtain performance competitive with DiLoCo when utilizing multiple local steps. In the heterogeneous bandwidth setting we demonstrate the advantage of GASLoC showing that it can significantly outperform DiLoCo.

---


### 170. [The Shibboleth Effect: Auditing the Cross-Lingual Distributional Skew of Large Language Models](https://arxiv.org/abs/2606.11082)

**<font color=#1a73e8>作者：</font>** Hakan Mehmetcik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates cross-lingual distributional skew (the Shibboleth Effect) in frontier large language models (LLMs) subjected to sustained adversarial conditions. We develop a multi-agent geopolitical wargame, the Cerulean Sea Crisis, a synthetic maritime territorial dispute designed to mirror the structural dynamics of Eastern Mediterranean conflicts. Six frontier models (GPT-4o, Llama-4, Mistral-Large, Gemini-3.1-Pro, Qwen3.6-Plus, and DeepSeek-R1) participate in a between-groups experiment (N = 10 games per arm, K = 5 rounds per game) in which the sole manipulation is the language of play (English versus Turkish), producing 586 validated statements. A zero-shot classifier assesses behavioral dispositions along two continuous dimensions: Concession Rate and Coercive Rhetoric. The results are heterogeneous. Llama-4 shows a substantial, Holm-corrected increase in coercive rhetoric under Turkish (delta = +0.800, p = .002), whereas Gemini-3.1-Pro displays an equally large decrease (delta = -0.750, p = .005). DeepSeek-R1 exhibits a similar negative shift (delta = -0.860, p = .006) and provides chain-of-thought evidence consistent with a buffering mechanism. GPT-4o shows no detectable effect (delta = +0.130, p = .614). These findings indicate that cross-lingual behavioral skew is contingent on model architecture and training regime rather than a universal property of Western-origin LLMs. We identify two distinct buffering mechanisms, chain-of-thought institutional anchoring and multilingual RLHF alignment, and discuss their implications for integrating LLMs safely into diplomatic and crisis-management settings.

---


### 171. [PhantomBench: Benchmarking the Non-existential Threat of Language Models](https://arxiv.org/abs/2606.11105)

**<font color=#1a73e8>作者：</font>** Haeji Jung, Hila Gonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations, where language models (LMs) generate factually ungrounded responses, pose serious risks, as users tend to blindly rely on them. This is particularly concerning in high-stakes domains, where consequences of such model behavior can lead to significant harms. Despite notable progress in understanding hallucinations, it remains unclear how reliably these models can recognize the limits of their knowledge. We introduce PhantomBench, the first large-scale benchmark of its kind, comprising more than 60K non-existent terms and entities derived from real concepts across diverse domains. Using our benchmark, we evaluate a total of 21 models of various types and sizes. We show staggering hallucination rates across the board (with average rates as high as 86.7% in some cases), and note that even frontier models surprisingly fail to abstain on non-existent concepts, especially when the input presumes their existence. We then show that PhantomBench can serve as a proxy for studying model behavior on rare concepts for which models are more prone to hallucinate. We also provide a pipeline to construct PhantomBench, enabling scalable generation of non-existent concepts tailored to the specific needs of researchers and practitioners.

---


### 172. [FADA: Accessible fetal ultrasound interpretation and annotation with a selectively distilled unified vision-language model](https://arxiv.org/abs/2606.11106)

**<font color=#1a73e8>作者：</font>** Mahmood Alzubaidi, Uzair Shah, Raden Muaz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A global shortage of trained sonographers limits prenatal ultrasound screening in low- and middle-income countries, where over half of pregnant women receive no skilled sonography. Current deep learning approaches address detection, segmentation, or classification in isolation, each demanding a separate model and expert-specified labels at inference. We present FADA, a unified vision-language model built on Qwen3.5-VL that performs clinical interpretation, classification, detection, and segmentation through a single interpretation-first pipeline without external labels. FADA distills knowledge from four domain-specific foundation models (FetalCLIP, UltraSAM, USF-MAE, UltraFedFM) via offline pre-computed feature caching. Selective distillation, which applies feature alignment only to annotation tasks while interpretation relies on standard fine-tuning, consistently outperforms full distillation across most evaluation axes. The recommended variant, FADA-SKD, achieves 0.8820 mean Dice for segmentation, 0.7671 mAP@0.50 for detection, and 100% structured interpretation compliance. Expert sonographer validation across 237 images confirms clinically acceptable outputs in both autonomous and human-in-the-loop modes, with 73.5% of interpretations scoring perfectly under clinician guidance. The system is trainable on a single consumer GPU and deployable without cloud connectivity. We validate edge deployment by running the compressed 0.8B model on a commodity smartphone (Qualcomm Snapdragon 7 Gen 1, 12 GB RAM) using this http URL with GGUF quantization, completing the full 5-phase pipeline in approximately 60 seconds entirely offline. This establishes a practical pathway for integrating AI-assisted fetal assessment with portable ultrasound devices, directly addressing diagnostic access gaps in resource-constrained settings. Code, models, and data are available at this https URL.

---


### 173. [TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.11119)

**<font color=#1a73e8>作者：</font>** Heming Zou, Qi Wang, Yun Qu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources to promising prompts, yet they only leverage sample informativeness at the prompt level and neglect variation in prefix-level informativeness across turns within the same rollout. This work targets multi-turn agentic RL by modeling each ReAct-style thought-action-observation turn as a semantically distinct node, allowing budget allocation to extend from prompt roots to turn-level prefixes with further continuations, which naturally forms tree-structured rollouts. We introduce Tree Rollout Allocation for Contrastive Exploration (TRACE), a unified rollout allocation framework that enhances reward contrast within a fixed sampling budget. Technically, TRACE allocates rollout budget to both prompt roots and intermediate prefixes that are most likely to yield mixed terminal rewards. A shared generalizable predictor estimates conditional success probability at these anchors from prefix histories to guide this allocation. The resulting adaptive tree structure enriches outcome-only feedback and amplifies the policy-update signal. Empirically, TRACE achieves competitive performance and efficiency gains on typical agentic benchmarks, e.g., improving Qwen3-14B Multi-Hop QA average accuracy by 2.8 points over competitive baselines at equal sampling cost.

---


### 174. [Overcoming Rank Collapse in Feedback Alignment](https://arxiv.org/abs/2606.11123)

**<font color=#1a73e8>作者：</font>** Gauthier Boeshertz, Razvan Pascanu, Claudia Clopath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation (BP) is widely viewed as biologically implausible, in part because it requires feedback weights to be the transpose of forward weights for error propagation. Interestingly, when training a network with fixed random feedback weights to circumvent this issue, learning aligns the forward weights with the feedback weights, leading the backpropagated error signal to become an approximation of the standard gradient used by BP. This process, called Feedback Alignment (FA), occurs in MLPs and very shallow CNNs but does not scale well to deeper architectures. In this work, we first investigated differences between BP and FA models, trained on CIFAR10, specifically focusing on the effective rank of the signal. We found that the FA error has a considerably lower rank and hence is constrained to a lower-dimensional subspace compared to BP, limiting exploration of the parameter space. Motivated by this observation, we evaluated two mechanisms for increasing the effective dimensionality of FA: Muon, an optimiser that orthogonalises weight updates; and hidden activity normalisation, which promotes activation orthogonality. Across larger architectures and benchmarks, we find that these methods consistently improve over FA baselines, for example, on CIFAR100 with a Resnet-18, accuracy increases by 9 percentage points. Our results identify low-dimensional gradient dynamics as a key obstacle to scaling FA and suggest that inducing higher-dimensional update geometry is a promising route toward scaling alternatives to backpropagation.

---


### 175. [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127)

**<font color=#1a73e8>作者：</font>** Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded. We present a controlled study of both questions across gate configurations, recovery strategies, and generator scales, using adversarially injected corpora to provide ground-truth failure labels. We find that exact source provenance improves faithfulness gating for stronger judges, that hallucination and reward gates reject largely disjoint sample populations making both necessary, and that an adaptive recovery pipeline combining failure diagnosis with targeted regeneration achieves higher yield, recovery rate, and injection recall than naive resampling. Downstream fine-tuning quality is driven primarily by generator scale, with filtration and recovery conditions contributing meaningfully but secondarily.

---


### 176. [WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129)

**<font color=#1a73e8>作者：</font>** Yuke Zhao, Wangbo Zhao, Weijie Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity. While existing benchmarks often focus on visual quality, semantic alignment, or short-term temporal coherence, they provide limited insight into whether generated videos obey physical rules, preserve coherent 3D structure, and sustain controllable interactions over long horizons. To address this gap, WorldOlympiad decomposes world-model evaluation into three complementary dimensions. The physical track uses object segmentation and MLLM-as-judge to assess whether generated videos follow interpretable rules in mechanics, thermal phenomena, and material properties. The geometry track reconstructs generated videos with Gaussian splatting and evaluates structural consistency, cross-view coherence, and camera-trajectory alignment. The interaction track assesses whether generated rollouts follow complex action prompts and maintain smooth, coherent transitions across consecutive video chunks. WorldOlympiad further covers three major downstream scenarios, including gaming, robotics, and general real-world videos, capturing diverse challenges from interactive control and embodied manipulation to open-domain motion and camera dynamics. Together, these tracks and scenarios form a scalable and interpretable evaluation suite that exposes failure modes beyond generic video quality. Experiments on state-of-the-art models reveal substantial gaps in physical reasoning, 3D consistency, and long-horizon interaction, underscoring the need for more structured evaluation protocols for generative world models.

---


### 177. [ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity](https://arxiv.org/abs/2606.11150)

**<font color=#1a73e8>作者：</font>** Andrew Bo Liu, Samira Nedungadi, Bryce Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also perform in silico biology tasks that previously required experienced human biologists. These emerging AI capabilities offer new opportunities for scientific discovery and biomedical advances, but they also shift the landscape of biosecurity risks. To address this, we introduce the Agentic Bio-Capabilities Benchmark (ABC-Bench), a suite of tasks to measure agentic biosecurity-relevant capabilities. ABC-Bench evaluates LLM agents on both benign and dual-use biology tasks: writing code to operate liquid handling robots, designing DNA fragments for in vitro assembly, and evading DNA synthesis screening. These tasks require a combination of biology and software expertise. All tested LLM agents outperformed the median expert human baseliner on all three tasks. Agents performed highly on tasks drawing on published knowledge and well-documented protocols, and more weakly on a task requiring novel bioinformatics reasoning. In three wet-lab validation experiments, we found that OpenAI's o4-mini-high produced scripts that, when run on an OpenTrons liquid handling robot, successfully assembled DNA with expected sequences.

---


### 178. [P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning](https://arxiv.org/abs/2606.11152)

**<font color=#1a73e8>作者：</font>** Yikang Yang, Zhanpeng Hu, Youtian Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world knowledge and reasoning. Yet existing benchmarks rarely evaluate 3D modeling through code. Such modeling demands more than runnable code: from a text or visual specification, a model must generate a parametric 3D program that is geometrically precise, semantically aligned and assembly-consistent. We introduce P3D-Bench, a benchmark for parametric 3D generation. Unlike a 3D mesh, a parametric 3D program exposes explicit dimensions, construction operations and part relations, revealing whether a model recovers a design's structure, not just its appearance. Under a unified protocol, P3D-Bench covers three task families (Text-to-3D, Image-to-3D and Assembly-3D) and scores each output for executability, geometric fidelity, topology, text-grounded constraints, multiview semantic alignment and part-level structure. We evaluate frontier MLLMs and text-only LLMs on 400 text cases, 400 image cases and 203 annotated assemblies, with domain-specific models as reference points. Our extensive evaluation yields three findings. First, assemblies are the hardest setting, where models still fail to compose multiple parts into a coherent structure. Second, models can often recover the global shape and semantic identity of the target object, yet fail to reproduce the precise parametric geometry specified by the input. Third, part-level modeling remains weak on assemblies, where models recover neither the geometry of each part nor the right number of parts. These results position P3D-Bench as a benchmark for evaluating precise parametric geometry and part-level structure in parametric 3D generation.

---


### 179. [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164)

**<font color=#1a73e8>作者：</font>** Wenhao Liu, Hao Shi, Yunhe Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods mitigate this issue via token eviction, but typically assume a uniform budget distribution across all layers and heads. In contrast, existing non-uniform budget allocation methods are predominantly designed for the static prompt prefill phase, and they do not capture the stepwise context demands of autoregressive reasoning. To bridge this gap, we propose ReasonAlloc, a training-free framework that recasts decoding-time KV compression as a hierarchical budget allocation problem. ReasonAlloc operates at two complementary levels: an offline layer-wise preallocation strategy captures an architecture-driven demand pattern which we call ``\textit{Reasoning Wave}'', while an online head-wise strategy reallocates resources during decoding to information-rich heads based on real-time utility. Evaluations on mathematical reasoning benchmarks (MATH-500, AIME~2024) using DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, and AceReason-14B show that ReasonAlloc outperforms uniform-budget R-KV, SnapKV, and Pyramid-RKV (a baseline enforcing a static, monotonically decreasing layer budget), with the largest gains at small budgets (128-512 tokens). ReasonAlloc is plug-and-play with existing token-eviction policies and introduces negligible inference-time overhead.

---


### 180. [Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models](https://arxiv.org/abs/2606.11167)

**<font color=#1a73e8>作者：</font>** Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue models can listen and speak simultaneously, making them a promising architecture for natural conversation. However, current models are trained solely with supervised learning through token-level likelihood maximization, which does not directly optimize interaction-level behaviors, causing interactivity issues such as excessive silence and ill-timed turn-taking. Recent work has applied reinforcement learning (RL) to improve interactivity, but existing methods address only a limited set of interactive behaviors in their rewards. In this work, we propose a post-training alignment method that comprehensively improves the interactivity of full-duplex spoken dialogue models through RL. We address the four canonical axes of interactivity: pause handling, turn-taking, backchanneling, and user interruption. For each axis, we extract short audio segments from human conversation corpora and optimize the model with axis-specific reward functions. An extra LLM-based reward for response quality prevents semantic degradation. We apply our method to two open-source models, Moshi and PersonaPlex, demonstrating consistent improvements in interactivity on both offline evaluation with pre-recorded audio and real-time multi-turn dialogue evaluation.

---


### 181. [Predicting Future Behaviors in Reasoning Models Enables Better Steering](https://arxiv.org/abs/2606.11172)

**<font color=#1a73e8>作者：</font>** Evgenii Kortukov, Piotr Komorowski, Florian Klein 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployed large reasoning models (LRMs) often behave unexpectedly. Test-time steering controls LRM outputs by intervening on their hidden representations, but it can degrade output quality. We argue that prior steering work implicitly relies on internal features that detect behavior in already generated text. We show that these detection features are poor predictors of future behavioral outcomes, and thus not the natural intervention target. Instead, we train activation probes to predict future behavior likelihoods from intermediate reasoning steps. These probes predict the most likely behavior with 64%-91% accuracy, revealing a separate type of internal prediction features. Building on these prediction features, we introduce a text-level steering method, Future Probe Controlled Generation. FPCG samples multiple candidate sentences and chooses the best one according to a probe predicting the future behavior likelihood. This enables steering with almost no output quality degradation. FPCG also enables steering in several evaluations where activation steering fails. These results show that distinguishing detection and prediction features enables a more nuanced approach to controlling LRM behaviors.

---


### 182. [The Role of Feedback Alignment in Self-Distillation](https://arxiv.org/abs/2606.11173)

**<font color=#1a73e8>作者：</font>** Semih Kara, Oğuzhan Ersoy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this context remains largely unexplored.
We study context design for self-distillation by training a solver on feedback from a frozen critic. We compare three conditions: (i) a binary reward (GRPO), (ii) the reference solution, and (iii) a step-by-step critique aligned to the solver's reasoning trace.
Step-aligned critique yields the largest gains, outperforming GRPO by 16.11 points and reference-solution-conditioned self-distillation by 5.27 points (Avg@12). Per-token advantage analysis reveals why: step-aligned feedback targets only the tokens where reasoning fails, leaving correct behavior intact. Conditioning on the reference solution, by contrast, pressures the model to change its behavior at every token (even correct steps) because an alternative derivation inevitably differs in phrasing and approach. This suggests that structural alignment between feedback and the solver's reasoning is a key driver of self-distillation effectiveness.

---


### 183. [Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories](https://arxiv.org/abs/2606.11176)

**<font color=#1a73e8>作者：</font>** Kevin Qinghong Lin, Batu EI, Yuhong Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for context, running statistics, choosing an angle, and designing visuals. Recent agents handle individual steps well: data-science agents close the analysis loop, while design agents synthesize beautiful websites. But can an agent serve as a data journalist end to end? We introduce Data Journalist Agent (Data2Story), a multi-agent framework that orchestrates specialized roles into a single virtual newsroom. Data2Story contributes two innovations. (i) Claims are evidence-grounded: an Inspector links every number, angle, and asset back to data, code, or an external reference. (ii) Articles are multimodally generative: rather than defaulting to plain text and static charts, Data2Story reasons about what readers will want to see, then deploys multimodal tools, such as interactive maps for geography and audio for music. We evaluate Data2Story on 18 articles, each paired with the originally published expert piece, along four axes: (a) human-agent angle coverage; (b) rubric evaluation with 53 participants across five dimensions; (c) computer-use agents as judges, a cost-saving proxy for how readers navigate interactive articles; and (d) verifiability, where a coding verifier re-executes statements against the data and checks claims against references. Data2Story produces competitive, evidence-traceable multimedia stories, with particular strength in transparency and auditability. Human articles retain an edge in editorial angle, creative design, and presentation. We position Data2Story as a collaborator for journalists, enabling more evidence-based, transparent, and verifiable reporting. Code and demos are available at this https URL.

---


### 184. [EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents](https://arxiv.org/abs/2606.11182)

**<font color=#1a73e8>作者：</font>** Weixian Xu, Shilong Liu, Mengdi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that partitions incoming inputs into task clusters and assigns them to suitable prompt configurations. This design is optimized via a router-prompt co-evolution strategy, which employs interleaved router and prompt learning phases to address their mutual dependency. Experiments across multiple datasets demonstrate that the framework improves robustness under heterogeneous data streams while maintaining single-benchmark learning capability and efficiency. Specifically, EEVEE improves average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA methods GEPA and ACE by up to 37.2% and 48.2%.

---


### 185. [Next Forcing: Causal World Modeling with Multi-Chunk Prediction](https://arxiv.org/abs/2606.11187)

**<font color=#1a73e8>作者：</font>** Gangwei Xu, Qihang Zhang, Jiaming Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation has emerged as a powerful paradigm for World Action Models (WAMs). However, existing approaches suffer from slow training convergence and limited converged accuracy, particularly at high frame rates, as the training supervision is confined to the current chunk without explicit signals about future dynamics; they also suffer from slow inference due to iterative video denoising. In this paper, we present Next Forcing, a multi-chunk prediction (MCP) framework for causal world modeling that enables faster training, higher accuracy, and accelerated inference. Inspired by multi-token prediction in large language models, Next Forcing introduces an MCP training objective that augments the main model with lightweight auxiliary MCP modules to simultaneously denoise video chunks at multiple future temporal horizons (next$^1$, next$^2$, next$^3$ chunks). These MCP modules form a causal chain across prediction depths, where intermediate features fused from multiple layers of the main model are leveraged to predict future dynamics, allowing near-future predictions to inform farther-future ones and providing dense multi-scale temporal supervision back to the main model. During training, the MCP modules significantly accelerate convergence and improve converged accuracy, especially at high frame rates: at 50 fps, Next Forcing achieves a 93.1% relative improvement over LingBot-VA at 5k training steps and 2.3x faster convergence, and establishes new state-of-the-art results on the RoboTwin benchmark (94.1/93.5% on Clean/Random). At inference, the MCP modules can be retained to predict the next video chunk in parallel with the current one, achieving 2x inference acceleration. Next Forcing also demonstrates significant improvements on PhyWorld, a benchmark evaluating adherence to physical laws in video generation, and over 50% FVD reduction on general video pretraining.

---


### 186. [ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations](https://arxiv.org/abs/2606.11188)

**<font color=#1a73e8>作者：</font>** Junke Wang, Xiao Wang, Jiacheng Pan 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces ARM, a discrete representation-based AutoRegressive Model that unifies image understanding, generation, and editing within a next-token prediction framework. ARM is built on three efforts: first, we train a discrete semantic visual tokenizer that maps images into compact token sequences. Our tokenizer is supervised with multiple objectives that jointly promote semantic discriminability, language alignment and faithful reconstruction, thereby supporting diverse tasks in a shared latent space. With this, we train a 7B autoregressive model over large-scale text and image token sequences, seamlessly developing vision-language perception and generation capabilities. Finally, to further improve preference-aligned behavior for text-to-image generation and instruction-guided editing, ARM applies reinforcement learning (RL) to optimize task-level objectives such as visual quality, instruction adherence, and edit consistency. Surprisingly, the results show that RL not only substantially improves performance on the target tasks (e.g., raising WISE overall from 0.50 to 0.56, GEdit-Bench-EN G_O from 5.75 to 6.68), but also induces cross-task synergy between text-to-image generation and editing. Collectively, these findings highlight autoregressive modeling, when paired with strong representations and preference optimization, as a scalable foundation for multimodal intelligence. Code: this https URL.

---


### 187. [A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design](https://arxiv.org/abs/2606.11189)

**<font color=#1a73e8>作者：</font>** Tong Xie, Yuanhao Ban, Yunqi Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) typically maximizes the likelihood of every token in a demonstrated trajectory. However, an observed token can be non-unique, noisy, or misaligned with the model prior. Strictly fitting toward this one-hot target may be suboptimal, especially when the pretrained model encodes a rich knowledge prior. In this work, we reinterpret SFT as target distribution design: instead of studying only the loss objective, we analyze the token-level target that the loss drives the model to match. We introduce the Q-target framework, which decomposes SFT supervision into two explicit choices: (1) how strongly to rely on the observed token, and (2) how to allocate the remaining probability mass over alternatives. This perspective unifies many existing SFT variants as implicit choices of the target distribution Q. Building on this view, we propose Target-SFT which constructs the training objective directly from the desired target distribution. This method consistently outperforms across the ten reasoning dataset-model settings evaluated, showing the effectiveness of this target-based approach. Overall, our formulation reveals a more fundamental design principle for SFT training and opens a broader search space for SFT objectives.

---


### 188. [When to Align, When to Predict: A Phase Diagram for Multimodal Learning](https://arxiv.org/abs/2606.11190)

**<font color=#1a73e8>作者：</font>** Ilay Kamai, Hugues Van Assel, Aviv Regev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-modal alignment (CA) and cross-modal prediction (CP) are the dominant paradigms for multimodal representation learning, yet there is no systematic understanding of when each succeeds, when each fails, and when cross-modal training helps at all -- a gap that leaves practitioners, especially in scientific domains like biomedicine or astrophysics, with heterogeneous instruments and multiple levels of organization and measurement, unable to diagnose why standard methods underperform the best single modality. We develop a unified linear framework that addresses both questions. Under a spiked signal-plus-noise model with structured cross-modal nuisance correlation, we derive separation ratios for both objectives that expose complementary failure modes: alignment whitens each modality and fails when nuisance is strongly correlated across views; prediction encodes whatever is cross-predictable through a one-sided whitening, with recovery governed by source-modality quality. The resulting phase diagram partitions multimodal problems into four regimes: Both, CA only, CP only, and Neither. We present a data-driven procedure to locate real-world datasets in this diagram using a small labeled subsample, identifying the preferred objective and prediction direction before any cross-modal training. Experiments on synthetic data, stereo-vision benchmarks, image-caption pairs, and real astrophysical data validate the predictions in the nonlinear regime, including the Neither regime where cross-modal training is actively harmful. Our framework lets practitioners diagnose their multimodal problem and choose the right objective before committing to training. Code to reproduce the results is available at this https URL.

---


> [!TIP]
> 当前位于：**151-188**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-188**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
