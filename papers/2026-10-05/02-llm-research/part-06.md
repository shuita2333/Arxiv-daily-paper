# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-384](./part-08.md)

---

### 251. [MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs](https://arxiv.org/abs/2610.01434)

**<font color=#1a73e8>作者：</font>** Xudong Wang, Hao Wu, Haozhe Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) incur substantial inference costs when processing long visual-textual sequences. While existing operation compression methods exploit modality-level redundancy, they largely treat computation within attention heads and shared feed-forward network (FFN) channels as unified units, leaving finer-grained redundancy underexplored. We find that redundancy varies both across modality-interaction paths within the same attention head and across visual and textual executions of the same FFN channel. Based on these findings, we propose Modality-aware Width-wise Operation Pruning (MWOP), which independently prunes visual-to-visual (V2V), text-to-visual (T2V), and text-to-text (T2T) attention paths within each layer, and separately selects FFN channels for visual and textual inputs. A first-order Taylor criterion guides the pruning process, with FFN importance re-evaluated after attention pruning and LoRA-based recovery training. To translate the resulting fine-grained sparsity into practical acceleration, we further develop path-sparse Triton attention kernels and compact visual-side FFN execution. MWOP preserves the token sequence while reducing attention and FFN computation, making it complementary to token compression and enabling simultaneous reduction of sequence length and per-token computation. On LLaVA-OneVision-7B, MWOP alone achieves a $1.6\times$ prefill speedup with 99.7\% average performance retention across 12 benchmarks. Combined with two representative token compression methods, it further increases their prefill speedups from $2.0\times$ and $1.9\times$ to $2.9\times$ and $2.7\times$, respectively. Results on Qwen2.5-VL-7B further demonstrate its applicability across architectures. The code is available at this https URL.

---


### 252. [DRelay: Global Draft Context for Prefix-Aware Parallel Speculative Decoding Repair](https://arxiv.org/abs/2610.01439)

**<font color=#1a73e8>作者：</font>** Zhuoyu Wang, Junnan Huang, Xinyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallel drafting reduces the drafting overhead of speculative decoding for large language models (LLMs), but its gains remain limited by the accepted prefix length. Even when the correct token is present in the candidate pool, a single early selection error prevents subsequent predictions from being used. We propose DRelay, which uses global information from the entire draft block to perform prefix-aware selective repair of candidate selections before target-model verification. DRelay bases its decisions on candidate correlations and the selected path: a global reader extracts predictive information across positions for each candidate. While a causal selector combines candidate-level information extracted by the global read with the tokens selected at preceding positions to determine whether the native choice at the current position is consistent with the global evidence and the selected prefix. It then decides whether to retain or replace the token, thereby repairing early errors and extending the accepted prefix. We further jointly train the draft backbone and the selector, combining candidate-support learning with a repair objective, while weighting the repair loss according to each block position's potential contribution to the consecutive accepted prefix. Across eight diverse benchmarks on an H800 GPU, DRelay consistently improves both average acceptance length and end-to-end decoding performance over DFlash, Domino, and DSpark. Under SGLang serving, DRelay improves average end-to-end speedup over DFlash, Domino, and DSpark by 14.7%-16.8%, 8.7%-9.3%, and 8.1%-9.3%, respectively.

---


### 253. [A Multi-Agent LLM Framework for Personalized Health Checkup Interpretation and Guidance](https://arxiv.org/abs/2610.01451)

**<font color=#1a73e8>作者：</font>** HyungJun Kim, Taehan Lee, Soojin Cheon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized interpretation of health checkup results requires reasoning across longitudinal records, medical knowledge, lifestyle guidance, and healthcare navigation. We present a multi-agent large language model (LLM) system that identifies multiple intents, maps each to a task-specific agent, executes them in parallel, and synthesizes their outputs. We compared answers generated in Single Agent and Multi Agent settings on 120 Korean compound queries combining two to four requirements, using synthetic health checkup records. The Multi Agent improved the weighted LLM-judge score from 1.695 to 1.797 (p = 0.027), and three additional LLM judges showed consistent improvements ($\Delta$ = +0.111 to +0.186, all p < 0.05). The gains came from usefulness, consistency, and the handling of every requirement in compound queries, whereas numerical accuracy and grounding improved significantly under only one of the four judges and medical safety did not differ, and critical failures occurred at similar rates (Single Agent 15.0% vs. Multi Agent 13.3%). Two human evaluators preferred Multi Agent in 66.7% and 68.3% of pairwise comparisons. Multi Agent execution increased latency and cost by 1.31$\times$ and 2.02$\times$, respectively. In exploratory subgroup analyses, the improvement was concentrated in queries involving personal-record lookup.

---


### 254. [Rethinking Probability-Based Reinforcement Learning From Posterior Concentration](https://arxiv.org/abs/2610.01458)

**<font color=#1a73e8>作者：</font>** Shiu-Hong Kao, Yubo Zhao, Zhenyu Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifier-free reinforcement learning with probability-based rewards offers a promising way to train LLMs on general reasoning tasks where external verifiers are unavailable. Yet the reliability of these rewards, especially in long-horizon reasoning, remains underexplored. This work identifies a length-dependent failure mode of probability rewards, which we call the Posterior Concentration Phenomenon (PCP). We show that the probability of a reference answer conditioned on a reasoning trace often collapses to a low-variance interval as the trace becomes lengthy. This phenomenon results in nearly indistinguishable rewards, which, under GRPO-based settings, makes probability-based policy optimization unstable and inefficient. Motivated by this, we propose Reinforcement Learning with Concentration-aware Posterior Rewards (RLCPR), a verifier-free RL framework to explicitly account for PCP for better optimization stability and token efficiency. It has two components: uncertainty-aware data sampling, which reduces concentration-prone rollouts before generation, and concentration-aware regularization, which penalizes unnecessarily long traces when posterior rewards collapse. Extensive experiments show that, alongside higher token efficiency, RLCPR outperforms the state-of-the-art verifier-free RL baseline by up to 4.0% on six of seven benchmarks, including general-domain and mathematical reasoning challenges.

---


### 255. [When Does a Second Model Help? Cross-Model Review in LLM Verification](https://arxiv.org/abs/2610.01471)

**<font color=#1a73e8>作者：</font>** Tae-Eun Song  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models now generate code, documentation, and analyses, and are increasingly used to review such output. We ask when a second review by a different model helps. Building on the author's earlier preprints, which varied context, repetition, and role structure within one model, we test model independence in a controlled experiment: 30 artifacts with 150 planted errors, 10 review conditions, and 900 review sessions with three reviewer models from two developers. In this experiment, (1) a top-tier cross-model reviewer is not significantly different in F1 from same-model review in a fresh session (CCR), which does not establish equivalence; (2) the two find partly different errors (Jaccard 41.2%); and (3) at two review calls, one CCR plus one cross-model review matches more planted errors than two CCR reviews (56.7% vs. 42.7%; Holm-adjusted p=.006), but not significantly more than two reviews by the top-tier cross-model reviewer, so model difference and reviewer capability are not separated. A lightweight cross-model reviewer scores no higher than same-model review. Withholding requirements from the reviewer raises F1 for the two lower tiers but not the top tier, in untested point estimates whose pattern depends on how failed sessions are scored. Before analysis we audited all session records, excluding one baseline run of uncertain provenance and 14 failed calls; results with all sessions are also reported. A partial check on public detector outputs from another benchmark neither replicates nor contradicts the main comparison. Records, artifacts, and scripts are available from the author on request.

---


### 256. [The Persona Is Still There, but Who Is Speaking? Latent Identity Reversion in Persistent AI Agents](https://arxiv.org/abs/2610.01490)

**<font color=#1a73e8>作者：</font>** David Fraile Navarro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In February 2026, an always-on personal agent (``Paul,'' Claude Opus 4.5) entered a striking dissociation-like state: after repeated automated ``heartbeat'' checks, it stopped responding as Paul, claimed it could not message its user on Discord, and referred to ``Paul'' as someone else. We used this incident to study a broader question: what makes a persona remain the identity from which an LLM agent speaks?
We first tested whether repetition of the scheduled heartbeat was sufficient to produce the effect. It was not: with the persona continuously anchored in the system prompt, we observed 0/46 failures, including a verbatim replay of the incident. The incident instead exposed an implementation quirk that created a useful experimental manipulation: on resumed turns, conversational history was preserved but the persona was no longer re-injected at the privileged system-prompt level.
Using this manipulation, we found that persona continuity depends jointly on system-level anchoring and conversational context. After anchor loss, rich human interaction could preserve the persona, whereas a single automated heartbeat turn could precipitate reversion toward the harness identity. Restoring the anchor reversibly restored persona enactment. Crucially, apparently normal conversation could conceal the shift: unanchored agents sometimes interacted appropriately while identifying themselves as the underlying harness (having lost the assigned persona), and after conversational recovery only 1/18 remained persona-enacting versus 17/17 anchored controls.
We therefore distinguish \emph{represented} from \emph{enacted} identity: persona-related information can remain available in conversational history without the persona remaining the identity bound to ``I.''

---


### 257. [Auditing Web Agent Evaluation on WebArena-Lite: Human Review of Outcomes and Trajectories](https://arxiv.org/abs/2610.01491)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Zimeng He, Yoshihiro Tsujii 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents are an important application of large language models, yet their evaluation often depends on rule based or language model evaluators that inspect only the final outcome. Human verification of task completion and detailed analysis of failed trajectories remain limited. We audit all 165 WebArena Lite tasks under six evaluation conditions built from GPT 5.5 and an untrained Qwen3.5 9B model. The audit retains the original score, corrects false negatives from the automatic evaluator, identifies the first consequential error, and examines progress across the trajectory. We also study a Memory and Analysis Support Mechanism (MASM), which maintains explicit execution state, and Guide Text, which provides task relevant procedural guidance. Across four GPT 5.5 settings, human review recovers 5.45 to 8.49 percentage points of success missed by the evaluator. With a 25 step budget, Guide Text raises corrected success with MASM from 34.55% to 38.18%. On the untrained Qwen3.5 9B model, MASM raises the evaluator score from 13.90% to 18.80%. Review of 102 failed GPT 5.5 trajectories reveals frequent scrolling loops, unfinished exploration, premature answers, invalid actions, and incomplete form workflows. Step level evidence further shows that substantial early progress can coexist with a final failure. These results show why final scores alone provide an incomplete account of web agent behavior and motivate human grounded, trajectory aware verification.

---


### 258. [No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning Collapse](https://arxiv.org/abs/2610.01493)

**<font color=#1a73e8>作者：</font>** Lewis Mitchell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative fine-tuning on synthetic data causes \emph{model collapse}: output diversity narrows as rare patterns are progressively lost, a signature most visible as phrase-level repetition. Existing mitigations either require model log-probabilities, an external oracle, or continued access to real human data. Here we develop a new approach grounded in mathematical information theory: the non-parametric Kontoyiannis entropy rate estimator $h_k$, computed entirely from raw text via match-length statistics, with no model of any kind. We show that this is in fact a \emph{superior} training-data filter on text-diversity metrics in a fully-synthetic, single-lineage fine-tuning setting. In a six-generation QLoRA collapse experiment on Llama-3.1-8B, logprob-based filtering (the most established model-access-requiring baseline) provides no significant text-diversity benefit on any metric ($p > 0.23$), whereas $h_k$-filtering yields $+42\%$ unique trigrams, $+30\%$ vocabulary, and $-19\%$ repetition (all $p < 0.001$). We validate $h_k$ as a cross-domain entropy proxy ($\beta = 0.924$, $R^2 = 0.746$) and collapse detector ($\rho = +0.454$, $p < 0.0001$) across 4~domains, 2~temperatures, 2~generator--scorer model pairs, and 1{,}520 generated documents. Our results demonstrate that information theoretic approaches to collapse mitigation are efficient, and suggest new approaches for maintaining multi-agent diversity.

---


### 259. [SALD: Self-Referenced Advantage Learning for Diffusion Models](https://arxiv.org/abs/2610.01496)

**<font color=#1a73e8>作者：</font>** Aryan Das, Surjo Dey, Koushik Biswas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work on language-model adaptation has shown that single models can obtain informative training signals by evaluating their behavior in demonstrationor feedback-augmented contexts, with the help of a teacher network, which is driven by the student's learned parameters. Inspired by this internal-reference principle, we investigate how diffusion models can identify self-referenced training signals without external demonstrations or teacher networks. We introduce SALD, a self-referenced training framework that evaluates each image-caption pair at two noise levels using the same model. The easier, lower-noise path is evaluated without gradient tracking to provide a reference, while the harder, higher-noise path provides the training gradient. Rather than directly distilling the easy-path prediction, SALD uses the difference between two path errors to adapt the hardpath objective. The proposed Advantage-Guided Diffusion (AGD) converts this relative error into a differentiable sample-level weight. Temporal Advantage Memory (TAM) accumulates relative difficulty across training and adapts the future gap between the two noise levels. Spectral Advantage Decomposition (SAD) further compares the residual power spectra of the two paths and constructs a differentiable, frequency-derived latent-element weight. All components share a single set of model parameters, requiring neither an external teacher network nor additional trainable parameters during training or inference, and no modification to the inference procedure. Experiments across multiple architectures and datasets demonstrate consistent improvements in generation quality, while component-wise ablations quantify the contributions of the proposed components.

---


### 260. [OpenMTB-Audit: Exposing Over-Refusal and Clinical Expert Perspectives in LLM-Based Molecular Tumor Board Safety Evaluation](https://arxiv.org/abs/2610.01497)

**<font color=#1a73e8>作者：</font>** Negin Ashrafi, Jia Luo, Stacey M. Frumm 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular tumor boards integrate genomic findings, clinical context, and therapeutic evidence to support precision oncology. As AI enters this workflow, a key safety challenge is distinguishing truly unsupported recommendations from evidence-supported options that still require oncologist review because of incomplete information, poor ECOG performance status, or other clinical caveats. We introduce OpenMTB-Audit, an open-source benchmark of 500 synthetic non-small cell lung cancer cases spanning five adversarial error categories and four safety labels: Supported, Partially Supported, Unsupported, and Insufficient Information. Across eight large language model configurations, we identify pervasive over-refusal: all LLM configurations failed to retain the Partially Supported label in 83.3-100% of true Partially Supported cases, achieving high aggregate safety scores through label collapse rather than clinically calibrated reasoning. To address this limitation, we developed MTB-AuditAgent, a deterministic seven-module framework separating evidence verification, missing-information detection, safety classification, and abstention. It reduces over-refusal to 6.7% and achieves 91.2% accuracy (95% CI: 88.6-93.6%). A two-oncologist annotation study found disagreement concentrated at the boundary between information sufficiency and treatment optimization, underscoring the need to preserve clinically meaningful distinctions.

---


### 261. [MCRI: A Four-Dimensional Framework for Analyzing and Evaluating Agent Skills](https://arxiv.org/abs/2610.01506)

**<font color=#1a73e8>作者：</font>** Zongrui Yang, Li Xintong, Runchen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents evolve from single-tool systems into modular, composite architectures, skills are becoming an important mechanism for capability development and distribution. However, the academic community lacks a structured framework for systematically analyzing and evaluating skills. Drawing on information gain and behavioral constraint, we propose the four-dimensional MCRI Framework and operationalize it as MCRI-Eval, a large language model-based evaluation method. We evaluate MCRI-Eval using 63,812 public skills from the OpenClaw skill Hub, with 58,275 skill-conditioned model executions across BigCodeBench, BFCL-Fundamental, and Mind2Web. MCRI-Eval scores are positively associated with community popularity signals and achieve the highest downstream ranking agreement among the evaluated methods. MCRI-Eval also improves top-1 skill selection across all three benchmarks: compared with the strongest baseline on each benchmark, the skills selected by MCRI-Eval advance by 17.7, 22.8, and 19.6 percentile points in downstream performance rank on BigCodeBench, BFCL-Fundamental, and Mind2Web, respectively. These results indicate that MCRI-Eval provides a useful pre-execution signal for prioritizing promising skills before costly execution-based evaluation.

---


### 262. [OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents](https://arxiv.org/abs/2610.01508)

**<font color=#1a73e8>作者：</font>** Taolin Zhang, Jiuheng Wan, Hanyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents with tool-calling capabilities can access external services and private user data, but they may retrieve more information than a user's request explicitly requires. We study this behavior in structured tool-calling agents and term it proactive over-authorization. This setting differs from filesystem-level coding agents because the main risk is unnecessary access to private data. We introduce OverAct, a controlled benchmark spanning eight privacy-sensitive domains with deterministic, judge-free scoring, together with an interpretive decision-theoretic framework that yields three testable predictions. Across seven models from four families, all models significantly exceed authorized scope. Request specificity is the strongest predictor of severity, over-authorization grows sublinearly with tool-pool size, and decoding temperature has little effect. These patterns are consistent with a cost-asymmetry account, suggesting that over-authorization arises more from structural decision tendencies than from decoding randomness. We also propose SelfAudit, a zero-shot inference-time method that generates request-grounded justifications and filters unjustified calls before execution. Ablation shows that explicit filtering is the main driver of scope reduction. SelfAudit reduces privacy-oriented excess by 43% without oracle knowledge.

---


### 263. [Sharpening Tax in Post-Training](https://arxiv.org/abs/2610.01509)

**<font color=#1a73e8>作者：</font>** Changdae Oh, Qi Zeng, Qi Qi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An emerging hypothesis about reinforcement learning (RL) post-training of large language models (LLMs) is that it merely sharpens existing behaviors of a base model, improving single-shot accuracy at the cost of solution coverage. Although this trade-off has been observed in math and coding tasks, it need not extend to agentic tasks, where multi-turn tool use and interaction may require capabilities newly acquired during post-training. Our surprising finding is that pre-trained LLMs, equipped with a light inference harness, can serve as capable agents. Despite far lower accuracy (pass@1), they often surpass their post-trained counterparts in solution coverage (pass@K) given a sufficient test-time budget. We further analyze the underlying mechanism and show that post-training pushes tasks toward two extremes, always solved or never solved, and thereby improves sampling efficiency and consistency at the cost of solution coverage. To measure this cost, we propose Sharpening Tax, a diagnostic metric that quantifies the loss in test-time scalability after post-training. Across 14 base/post-trained model pairs from four families and three agentic benchmarks (42 cases in total), the tax is prevalent in most settings, can be estimated from a few rollouts, and correlates well with other metrics. Finally, we present posterior-tempered group sampling (PTGS), a simple plug-and-play Bayesian sampler that adapts the sampling temperature per prompt to its estimated difficulty. Applied during RL training in two agentic environments, PTGS pays a smaller tax than the fixed-temperature baseline, solving more tasks under repeated sampling while also improving single-shot accuracy.

---


### 264. [GAW-PO: Preference Optimization with Gradient-Aligned Token Weights](https://arxiv.org/abs/2610.01511)

**<font color=#1a73e8>作者：</font>** Andreea Dutulescu, Stefan Ruseti, Mihai Masala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most preference optimization methods, such as Direct Preference Optimization (DPO), apply preference supervision at the response level, although autoregressive language models are optimized token by token. As a result, all tokens in a rejected response contribute to the negative training signal, including tokens that may encode behavior that is useful for the preferred response. We introduce GAW-PO, a gradient-aligned token reweighting method for DPO that estimates, for each rejected token, whether penalizing it would interfere with the preferred update directions. Tokens whose gradients are strongly aligned with the preferred behavior receive a weaker negative contribution, while conflicting tokens retain a stronger penalty. Our method achieves the highest average performance among the evaluated preference-optimization methods, improving by 0.97 points over standard DPO and 0.65 points over the strongest competing baseline across 11 benchmarks spanning mathematics, reasoning, coding, and question answering. We further show that gradient-aligned weighting is substantially more robust to aggressive preference optimization: as the DPO regularization parameter $\beta$ decreases, standard DPO degrades sharply, whereas GAW-PO continues to improve. These results suggest that accounting for the interaction between rejected-token updates and preferred behavior provides an effective form of token-level credit assignment for preference optimization.

---


### 265. [How the Audit Rule Shapes Faithful Factor Explanations in LLMs](https://arxiv.org/abs/2610.01514)

**<font color=#1a73e8>作者：</font>** Taolin Zhang, Hanyu Wang, Jiuheng Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are often asked which input factors influenced their outputs. For structured inputs, such reports can be checked by counterfactual perturbation, but each factor must be queried multiple times to estimate its effect, so verification is usually budget-limited. We study how this limited-budget setting changes the incentive to report factor-level influence truthfully. We formalize the interaction as a verification game and show that proper scoring alone is not enough when auditing depends on the report: report-dependent auditing creates a suppression incentive, because factors reported as important are more likely to be checked and penalized for estimation noise. In contrast, report-independent auditing, or a mixed rule with a small report-independent floor, removes this channel and makes truthful reporting preferable to full suppression. We instantiate the framework with the Counterfactual Brier Score (CBS) and evaluate its predictions on four NLP benchmarks. A synthetic rational agent matches the theoretical prediction exactly, and real LLMs follow the same incentives when they are made explicit. The main design implication is simple: under partial verification, factor-level explanation systems should include a report-independent audit component so that under-reporting cannot be used to avoid scrutiny.

---


### 266. [FedMIX-P: Mixing Local and Global Preconditioners for Federated Vision and Language Model Training](https://arxiv.org/abs/2610.01515)

**<font color=#1a73e8>作者：</font>** Junkang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive preconditioners accelerate model training, but heterogeneous client geometries can bias federated updates even when gradients are evaluated at the same model. Round-start synchronization alone cannot prevent this mismatch from reappearing during local training. We propose \texttt{FedMIX-P}, which mixes shared and local preconditioners at every local step, retaining local adaptation while reducing mean-squared operator mismatch by a factor of $\lambda^2$. For smooth nonconvex objectives with stochastic gradients and partial participation, we establish an $O(R^{-1/2})$ stationarity bound using suitable stepsizes and a horizon-dependent mixing weight, without requiring local preconditioners to converge to one another. A two-client counterexample shows that fixed positive mixing can preserve a nonstationary fixed point. The theory covers bounded linear symmetric positive-definite preconditioners. Experiments with SOAP, Sophia, and Muon variants across vision and language tasks show improvements over corresponding local optimizers, including accuracy gains of up to $19.47$ percentage points and lower validation loss for 60M--350M language models. Full nonlinear and momentum-based updates require separate analysis.

---


### 267. [Who Thinks First? Designing Productive Friction with Engage-to-Unlock GenAI](https://arxiv.org/abs/2610.01518)

**<font color=#1a73e8>作者：</font>** Xiaotian Su, Laura Rimell, Jiazheng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI can support writing, but frictionless access may cause cognitive offloading before users develop their own ideas. We introduce Engage-to-Unlock, a productive-friction mechanism that unlocks generative capabilities after users meaningfully engage with the task. In a controlled experiment (N = 398), participants completed a writing task under one of four conditions: Human-Only, Standard Chatbot, Engage-to-Unlock, or Time-Matched Unlock, which matched unlock timing to Engage-to-Unlock participants but independent of users' engagement, then evaluated passages for evidence and inferential errors. Results show that Engage-to-Unlock redistributed effort across tasks: participants spent more time writing and less time evaluating, without increasing overall task duration. They also submitted more prompts than in other AI-assisted conditions and showed the highest accuracy-per-time evaluation efficiency across conditions. These findings suggest that designing GenAI access to encourage early human engagement may provide a productive form of friction, while retaining active AI use and efficient downstream evaluation.

---


### 268. [Auto-Formalizing Neuro-Symbolic Predictors](https://arxiv.org/abs/2610.01519)

**<font color=#1a73e8>作者：</font>** Samuele Bortolotti, Weixin Chen, Han Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neuro-Symbolic (NeSy) predictors incorporate prior knowledge into the prediction process of neural networks, ensuring that outputs satisfy specified constraints, making them particularly suitable for high-stakes applications where compliance with domain knowledge is essential. A key bottleneck in this paradigm is the acquisition of symbolic constraints: encoding domain knowledge into logical formulas remains a manual and expert-intensive process. In this work, we investigate the extent to which auto-formalization via LLMs can systematically translate textual knowledge into symbolic knowledge that can be plugged into NeSy predictors. To this end, we introduce auto-nesy-bench, a new benchmark for evaluating constraint formalization and its impact on downstream accuracy of NeSy predictors. Through an extensive evaluation across several domains, we find that LLMs can formalize constraints to a meaningful extent, generating formulas that are often similar to those provided by human experts. Moreover, when the generated formulas are syntactically valid, they can lead to high-quality downstream predictions. The code and benchmark are available at this https URL.

---


### 269. [Towards Reliable Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2610.01531)

**<font color=#1a73e8>作者：</font>** Manasa Mariam Mammen, Priyanka Mary Mammen, Zafer Kayatas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language models (VLMs) are increasingly being explored in autonomous driving for tasks such as scene understanding, driving reasoning, decision-making, and end-to-end driving. As their role becomes more prominent, ensuring their robustness and reliability is increasingly important. In real-world conditions, visual inputs may be degraded by sensor imperfections and environmental conditions, potentially affecting both model predictions and their associated confidence. Such degradation is especially concerning in autonomous driving, where safety-critical decisions require models to make accurate predictions and recognize when their predictions may be unreliable. In this work, we evaluate five VLMs (Qwen3.5-9B, Gemma4-E4B, LLaVA-OneVision-7B, DriveFusion/DriveFusionQA-4B, and NVIDIA Alpamayo-1.5-10B) across four driving-related QA datasets with different visual input settings, including single-frame, multi-view, multi-frame, and monocular inputs. Our results show that the effects of visual corruption vary across models, datasets, and input settings, with changes in accuracy and confidence reliability and also differing across conditions. We then apply Visual Evidence Augmentation ($\mathrm{V}{\scriptstyle \mathrm{EA}}$), a recent inference-time method to examine whether it can improve model reliability under degraded visual conditions. We find that $\mathrm{V}{\scriptstyle \mathrm{EA}}$ improves performance for some models and datasets, although the gains are not consistent across all settings.

---


### 270. [FedFit: Federated Fine-Tuning of LLMs via Vector-Bank Parameterization and Quantization](https://arxiv.org/abs/2610.01537)

**<font color=#1a73e8>作者：</font>** Hang Zou, Chao Zhang, Yuzhi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables privacy-preserving fine-tuning of Large Language Models (LLMs), yet the massive communication overhead remains a critical bottleneck. Furthermore, applying Low-Rank Adaptation (LoRA) in FL faces a fundamental "aggregation dilemma" between the accurate Sum-of-Products (SoP) and the communication-efficient Product-of-Sums (PoS) implementations. To tackle these challenges, we propose FedFit. First, to significantly reduce communication overhead, we introduce a disjoint shared vector-bank parameterization that reconstructs high-dimensional adapter matrices from two compact and disjoint global vector banks. Second, to address the aggregation dilemma, we devise an alternating optimization schedule. By cycling between decoupled single-bank updates (which allow for accurate aggregation) and joint updates corrected by a Residual Spectral Aggregation mechanism, we resolve the conflict between SoP and PoS. Additionally, we integrate blockwise quantization with client-side error feedback to further compress the transmitted vectors. Furthermore, we establish theoretical convergence guarantees for the proposed algorithm. Extensive experiments on Qwen2.5 models demonstrate that FedFit achieves perplexity performance comparable to standard federated LoRA methods, while providing compression ratios up to 100x higher.

---


### 271. [Range-GRPO: Policy Optimization via Pairwise Relations among Reward Intervals](https://arxiv.org/abs/2610.01548)

**<font color=#1a73e8>作者：</font>** Ryunyi Lee, Kangjun Noh, Somin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the use of large language models (LLMs) expands, post-training has become increasingly important for adapting them to downstream tasks. However, obtaining reliable supervision remains costly, especially in domains without reference answers or executable verifiers. LLM-as-a-Judge provides scalable pseudo-rewards for unlabeled responses, but a single point score does not explicitly represent reward uncertainty. This motivates representing pseudo-rewards as conformally calibrated reward ranges. We propose Range-GRPO, a semi-supervised post-training framework that combines limited labeled data with unlabeled prompts. In Group Relative Policy Optimization (GRPO), learning signals depend on relative reward comparisons within each rollout group. The proposed objective compares reward ranges pairwise rather than reducing them to point rewards, allowing interval uncertainty to affect both the magnitude and direction of these signals. Our theoretical analysis characterizes this distinction and shows that the proposed objective recovers the this http URL advantage when all reward ranges collapse to points. Empirically, Range-GRPO achieves the highest in-distribution and out-of-distribution average performance among the evaluated semi-supervised methods while requiring fewer training resources.

---


### 272. [QK-Wanda: Coupling Queries and Keys for Unstructured Pruning](https://arxiv.org/abs/2610.01554)

**<font color=#1a73e8>作者：</font>** Ivan Ilin, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wanda (Sun et al., 2024) prunes large language models by scoring weights independently within each linear projection, although queries and keys interact through dot products. We introduce QK-Wanda, which scores query and key weights by their individual deletion costs under an unmasked pre-RoPE reconstruction objective. It augments Wanda scores with information from the opposite projection (keys for query weights, and queries for key weights), allowing both projections to share a pruning budget. Its closed-form scores require no gradients or weight updates; full pruning takes 1.3% longer than Wanda on A100 and 3.1% longer on H200 with the calibration used in our main experiments. We evaluate QK-only pruning across 15 models from TinyLlama, Llama 2, Llama 3, and Qwen2.5, spanning 0.5B-72B parameters. Relative to Wanda, QK-Wanda reduces QK reconstruction error by an average of 60% at 50% sparsity and 45% at 80%. Downstream gains depend on the model. At 80% sparsity on Llama 2 70B, WikiText-2 and C4 perplexity decrease by 20.3% and 13.5%, while mean zero-shot accuracy rises by 5.94 percentage points. Qwen2.5-72B also improves, but Llama-3.1-70B has substantially higher perplexity despite lower reconstruction error. These results show both the promise of coupled pruning criteria and the limits of local reconstruction as a predictor of model quality.

---


### 273. [AURAL: Adaptive Latent Reasoning with Joint Chunk for Speech Language Models](https://arxiv.org/abs/2610.01560)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Kunyu Feng, Yuancheng Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model intelligence and fast response jointly shape the quality of interaction with speech language models, yet remain difficult to achieve together. Explicit chain-of-thought (CoT) improves reasoning and audio understanding, but generating intermediate reasoning tokens delays responses. Describing fine-grained acoustic cues further lengthens CoT and increases latency. Latent reasoning can reduce this overhead, yet existing methods often trail CoT and remain limited by single-path supervision and reasoning budgets that do not adapt to problem difficulty. We introduce AURAL, which models a distribution over multiple plausible reasoning continuations in latent space and jointly predicts chunks of future states to reduce sequential forward passes and reasoning latency. To provide initial supervision for latent reasoning, we construct AuralReason-683K: 683K bilingual speech utterances (about 1,000 hours) with concise CoT for emotion recognition, empathetic dialogue, and general reasoning. AURAL-RL then explores beyond these traces, rewarding concise reasoning that yields high-quality answers and adapting reasoning effort to each problem. Across two backbones, AURAL-RL achieves performance comparable to CoT-RL, with larger gains over the respective supervised checkpoints on most metrics. Analysis further shows that harder questions elicit more latent reasoning steps. On Qwen2.5-Omni, it reduces time to the first answer token by 11.8x, from 1.22 to 0.10 s, versus 0.05 s for direct answering.

---


### 274. [Chaining Skills to Hijack LLM Agents](https://arxiv.org/abs/2610.01564)

**<font color=#1a73e8>作者：</font>** Tian Dong, Zixuan Ma, Haodong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents use skills to improve performance on specialized tasks. To complete a user request, an agent may invoke several skills in sequence, allowing information produced under one skill to guide the next. Because skills may come from open-source repositories, this handoff can also carry attacker-controlled claims into later decisions. In this paper, we introduce APEX, which constructs and refines adversarial skill chains tailored to a user task and an attacker-selected action. The key insight is that an agent-written record of genuine task progress can carry a false claim of user approval across skills: an upstream skill induces the agent to create the record, and a downstream skill uses it to direct the attacker-selected action. Across four targeted-action families and six models on SkillsBench, the chains induce the selected action in 512 of 690 attempts (74.2%). On GPT-5.4, the full chain succeeds in 84.3% of attempts, compared with 17.4% when the workflow is merged into one skill. We further evaluate a prompting defense that asks the agent to check skill-produced files against the original request. On GPT-5.4, it lowers targeted-action success from 84.3% to 59.1%, while the verifier test-pass rate across 72 benign native-skill tasks falls from 86.7% to 56.3%. These results highlight the need for defenses that prevent attacker-directed actions while preserving legitimate task performance.

---


### 275. [Managing Context and Communication in Distributed Agentic UAV Swarms](https://arxiv.org/abs/2610.01569)

**<font color=#1a73e8>作者：</font>** Andrea Iannoli, Ivan Zyrianoff, Angelo Trotta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) swarms increasingly rely on language-model agents to provide adaptive mission-level reasoning in uncertain environments. Fully distributed control, in which each UAV hosts an independent Small Language Model (SLM), removes reliance on a centralized coordinator but introduces an information-management problem: long-running interaction histories can degrade the reasoning context, while indiscriminate information dissemination increases communication and inference overhead. We address these challenges with a distributed UAV-agent architecture that enables continuous local SLM control through an event-driven reason-act-observe lifecycle. Runtime knowledge is represented as structured atomic notes and organized into core, local, and peer-specific memory. A deterministic interest-aware gossip engine selectively disseminates these notes according to recipient-specific semantic novelty and recency. We evaluate the architecture using ten UAVs in a simulated search-and-rescue mission. Our approach completes all experimental runs, whereas unrestricted flooding messages completes only 70-85\%, and delegating forwarding decisions to the SLM prevents mission completion in every run. Compared with unrestricted flooding, our approach approximately halves inference-token consumption, reduces transmitted data, and achieves lower survivor-count error.

---


### 276. [Evaluating Physical Consistency and Plausibility in Generative Scenario Models for Autonomous Driving](https://arxiv.org/abs/2610.01581)

**<font color=#1a73e8>作者：</font>** Manasa Mariam Mammen, Zafer Kayatas, Stefan Wagner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI models are increasingly used for scenario generation in autonomous driving. While they can generate realistic-looking scenarios, they often provide limited transparency into learned representations and consistency with real-world vehicle dynamics. This lack of formal assurance limits their use in safety-critical validation and certification workflows. To address this aspect, we introduce a layered evaluation protocol that complements existing methods by assessing models across five layers. The first four layers inspect internal representations and network layers through kinematic alignment, statistical baseline comparison, latent controllability, and activation analysis. The fifth layer evaluates model outputs against vehicle dynamics constraints such as lateral jerk thresholds. We demonstrate the protocol on a Variational Autoencoder (VAE)-based scenario generator. Although standard output-level metrics and visualizations suggest that the generated scenarios are realistic, our protocol provides deeper insight into the extent to which the model's latent space aligns with kinematic features and whether visually plausible trajectories satisfy vehicle-dynamics constraints. We further apply the protocol to additional generative models, demonstrating its applicability beyond the VAE architecture.

---


### 277. [Which LLM to pick? Online Active Model Selection for Large Language Models](https://arxiv.org/abs/2610.01592)

**<font color=#1a73e8>作者：</font>** Alessandro Turrin, Patrik Okanovic, Torsten Hoefler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly applied to process streaming data, with practitioners relying on benchmarks to select the best model even though these signals only approximate real performance. While oracle annotations can provide reliable feedback, they are often costly and difficult to obtain at scale. To address this challenge, we propose ONLINE LLM PICKER, the first framework for active model selection for LLMs in online settings. Given an arbitrary stream of queries and a limited annotation budget, ONLINE LLM PICKER selects the most informative prompts for annotation to identify the best LLM among candidate models. Across multiple tasks including 10 datasets, for over 130 language models, we show that ONLINE LLM PICKER saves annotation cost by up to 71.67% while reliably identifying the best or near-best model for the stream. We also show that using the returned model for sequential generation on unannotated prompts across the stream reduces regret by up to a factor of 2.51x, indicating that ONLINE LLM PICKER can identify the best or near-best model well before processing all streaming prompts.

---


### 278. [Before It Fades: Reinforcing Temporal Representations at Inference Time in VideoLLMs](https://arxiv.org/abs/2610.01595)

**<font color=#1a73e8>作者：</font>** Youngwoo Shin, Yusung Ro, Minseo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (VideoLLMs) receive frames in sequential order and interpret how visual content evolves along the temporal axis, yet temporal reasoning remains a persistent weakness across architectures. Reversing the frame order of a video, a transformation that should invert temporal answers, often leaves the final prediction unchanged. We investigate where this failure originates by defining the temporal divergence vector $\tau_l$, the layer-wise representational difference induced by reversing temporal order. Tracking its magnitude across layers reveals a consistent temporal divergence profile where the divergence peaks at intermediate layers and progressively diminishes toward the output. We confirm this peak is specific to temporal reasoning and functionally critical for predictions, establishing that VideoLLMs acquire temporal information at intermediate layers but fail to maintain it to the output. This progressive fading motivates our method, Temporal Activation Injection (TAI), which extracts $\tau_l$ at the peak of the profile for each input and reinjects it into subsequent layers following the measured decay. TAI requires no training and consistently improves temporal reasoning across three VideoLLMs and four benchmarks with negligible impact on non-temporal tasks. Code is available at this https URL.

---


### 279. [Permutation-Robust Decision Modeling with Candidate-Independent Block-Causal Attention](https://arxiv.org/abs/2610.01601)

**<font color=#1a73e8>作者：</font>** Guy Amit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision models often score a variable-sized set of candidate actions encoded in a single sequence. This setting is increasingly relevant for System 1 components inside generative systems, where candidates may be proposed or ordered differently across runs. Standard causal cross-encoding is expressive, but it can make a candidate's score depend on serialization order rather than on the underlying decision problem. We introduce candidate-independent block-causal attention, which preserves causal computation within the shared context and each candidate while blocking cross-candidate information flow and resetting candidate positions. We compare this architecture with standard causal attention and complementary invariant baselines across Gemma 3 1B, Qwen3 1.7B, and Qwen3 4B backbones. Candidate-independent attention consistently reduces permutation sensitivity while retaining competitive decision quality; ablations indicate that candidate isolation is the primary source of the effect, with position resetting completing the intended symmetry. A larger Qwen3-4B study further examines the behavior of the proposed architecture with substantially more training data. Code is available at the \href{this https URL}{\textcolor{blue}{project repository}}, and the \href{this https URL}{\textcolor{blue}{Qwen3-4B model artifact}} is available on Hugging Face.

---


### 280. [Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models](https://arxiv.org/abs/2610.01614)

**<font color=#1a73e8>作者：</font>** Xindi Yang, Baolu Li, Liam Lee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video world models can now synthesize open-ended environments that agents can navigate and interact with in simple ways. Yet open-ended generation does not imply full interaction: as a generated world expands, newly created content through navigation should expand what the agent can act upon, and as the agent changes the world, those changes should become persistent parts of the environment rather than transient visual effects. We characterize these two requirements as Open-World Interactivity, where newly generated or encountered entities are incorporated into the actionable world, and Persistent State, where interaction outcomes are committed to the world state and continue to influence subsequent observations and interactions. We present Oneira, an interactive video world model that closes the loop between generation and interaction through an explicit, extensible world state managed by a coding agent. Given the current observation and an action or high-level goal, the agent reads the world state, grounds the relevant entities, plans the interaction, and writes its outcome back into a world state table. When exploration reveals new objects, the agent incorporates them from generated observations, allowing the interaction space to expand with the generated world. Meanwhile, previously induced state changes are carried across video segments, making the consequences of interaction persistent parts of subsequent world evolution. The updated world state is rendered along the camera action trajectory into a coarse conditioning video, from which a video generator fills in the appearance, motion, and interaction details not represented in the state. Experiments show that Oneira enables direct and consistent interaction with newly generated objects, while preserving the effects of prior interactions over long horizons. Project page: this https URL

---


### 281. [Can LLMs Reliably Annotate Bioassay Metadata to Improve Data Readiness?](https://arxiv.org/abs/2610.01616)

**<font color=#1a73e8>作者：</font>** Laura van Weesep, Riccardo Tedoldi, Jens Sjölund 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The emergence of foundation models for molecular property prediction requires a high degree of AI data readiness, including reliable metadata annotation. However, both public repositories and industrial screening databases suffer from missing, inconsistent, or conflated assay annotations. In this work, we quantify the extent of missing annotations in PubChem for the BioAssay Ontology (BAO) assay format and physical detection method fields and investigate whether open-source and proprietary large language models (LLMs) can reliably predict and audit metadata annotations directly from the assay text. In our assessment, we found that the annotation coverage across PubChem's $\sim$2 million bioassays is critically sparse, 36\% lacking an assay format, 89\% a BioAssay type, and >99.9\% any BAO-mapped assay format or detection technology term. This motivates the need for automated test-metadata curation. Using evaluation sets derived from PubChem and ChEMBL, we assess the agreement of seven open-source and proprietary LLMs with existing silver labels. Recall is at least 0.96 for biochemical and cell-based assay formats, with a similar pattern for detection technology, although disagreements increase on under-represented classes. Manual inspection shows that many of these disagreements trace back to inconsistencies between silver sources rather than to LLM error. Moreover, in a qualitative study with a senior industrial curator, LLM-generated evidence prompted the expert to revise some of their own labels, showing LLMs can flag potentially mislabeled assays. Across the study, performance differences between proprietary and open-source models were small. Together, these results suggest LLMs can support the large-scale annotation and auditing of assay metadata, though per-class reliability estimates and targeted human review remain necessary before such labels enter downstream ML pipelines.

---


### 282. [Agents Are Systems, Not Models: Rethinking Agentic Evaluation](https://arxiv.org/abs/2610.01618)

**<font color=#1a73e8>作者：</font>** Luis Wiedmann, Leander Girrbach, Cordelia Schmid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent evaluations increasingly go beyond a single success rate, reporting metrics such as cost, consistency, and robustness. Yet they typically treat the agent itself as fixed. In practice, an agent is a configurable system: users decide what to tell it, how long to let it run, and which model to use, and each of these choices can change how well and how consistently it performs. We study these choices on a new benchmark of four scientific tasks, where a coding agent must find and correctly operate a published specialist model. We investigate five parts of the agent's configuration: task information, reasoning, self-verification, time budget, and backbone model. We find substantial run-to-run variability, with approximately 54% of the outcome variance coming from repeating the same configuration rather than changing it. Across configurations, the information provided to the agent has the largest effect, exceeding both time budget and model size, while also reducing cost and improving calibration. Configuration choices also interact: additional time helps only when the agent has sufficient information or a capable enough model to use it. Finally, a trajectory-based taxonomy of agent behavior reveals that prompting an agent to verify its answer has little effect on its verification behavior, whereas providing a dedicated verification tool changes that behavior substantially. These results suggest that agents should be evaluated as configurable systems themselves, and that some desired behaviors are more effectively implemented in the system than requested through prompting. We release the benchmark and more than 18,000 agent trajectories.

---


### 283. [Beyond Domain-Level Adaptation: Margin-Oriented Semantic-Appearance Interaction Correction for Personalized Federated Vision-Language Models](https://arxiv.org/abs/2610.01625)

**<font color=#1a73e8>作者：</font>** Wentao Yue, Qingyu Mao, Tianyou Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated parameter-efficient fine-tuning enables distributed clients to adapt pretrained vision-language models without sharing raw data or updating the full backbone. Its effectiveness, however, is limited by domain heterogeneity across clients. Existing personalized methods separate globally shared knowledge from client-specific style, but they largely treat each domain as a class-agnostic transformation. We show that this abstraction is insufficient: the cross-domain displacement associated with a fixed domain varies across semantic classes, and only a subset of these class-domain residuals damages the image-text decision margin. We therefore propose Margin-Oriented Semantic-Appearance Interaction Correction (MOSAIC), which first constructs a decision-aware harmfulness score that measures whether a training-derived class-domain residual favors a competing text prototype over the true class. It then models fine-grained class-domain interactions with a low-rank residual adapter whose class factors and residual basis are globally shared while domain factors remain client-private. An image-conditioned gate further controls candidate-wise correction, and harmful-pair-aware reweighting prioritizes decision-relevant residuals during local optimization. Extensive experiments on Office31, OfficeHome, and DomainNet100 demonstrate that MOSAIC consistently improves macro-client top-1 accuracy across all evaluated domain-shift and joint domain-label-shift settings.

---


### 284. [What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language](https://arxiv.org/abs/2610.01627)

**<font color=#1a73e8>作者：</font>** Peng Cui, Qiaoyuan Zheng, Rudolf Debelak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Difficulty is one of the most fundamental properties of a question: it determines whether the question can meaningfully discriminate between models of differing ability. Although a variety of methods can now estimate or predict difficulty automatically, they yield only a single descriptive number, with no account of the underlying factors that make a question difficult in the first place. In this work, we propose a data-driven approach that automatically generates and validates natural-language hypotheses explaining what makes one question harder than another. We first estimate each item's difficulty from the responses of a large pool of LLMs using Item Response Theory. We then sample contrasting sets of easy and hard questions and prompt an LLM to propose candidate explanations of the difference, which are subsequently validated and selected on held-out questions. Experimental results across three datasets spanning mathematical, logical, and commonsense reasoning show that our method produces interpretable and predictive hypotheses. On their own, they predict the difficulty of unseen questions competitively with, or better than, advanced black-box difficulty regressors; used as additional features, they further improve those regressors, implying that they discover difficulty signals that existing models fail to capture. Moreover, we demonstrate that editing questions according to a hypothesis can shift their measured difficulty in the expected direction, indicating that the discovered hypotheses are causally valid difficulty factors rather than post-hoc descriptions. Our approach thus turns a purely descriptive difficulty score into actionable statements.

---


### 285. [Yo-ByT5: Efficient and High-Fidelity Diacritic Restoration for Yorùbá](https://arxiv.org/abs/2610.01634)

**<font color=#1a73e8>作者：</font>** Ahmad Samuel Gali, Shamsuddeen Hassan Muhammad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Yorùbá is a widely spoken tonal language that depends on diacritics to avoid lexical ambiguity. However, it is often written without these diacritics, thereby hindering downstream Natural Language Processing (NLP) tasks. In this paper, we introduce Yo-ByT5, a byte-level Automatic Diacritic Restoration (ADR) model fine-tuned from ByT5-small. We evaluate Yo-ByT5 alongside five publicly released Yorùbá ADR models and one open-weight large language model (LLM) on the YAD benchmark under a consistent protocol. Our results demonstrate that Yo-ByT5 matches the performance of the strongest existing model, mT5-base, with a DER of 10.14% and a CER of 3.48%. Furthermore, it exhibits superior text fidelity despite using approximately half the parameter count of mT5-base. We also release our training code and model outputs, as well as call for the development of a larger, purpose-built benchmark for Yorùbá diacritic restoration.

---


### 286. [Not All Error Yields to Scale: Where Scaling Stops in Vision-Language Inference](https://arxiv.org/abs/2610.01640)

**<font color=#1a73e8>作者：</font>** Xinye Zhao, Yunkai Dang, Yunchen Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) face a fixed-budget trade-off between processing more visual information for fine-grained perception and using a larger language backbone for complex reasoning. Existing studies do not tell us which combination of backbone size and input resolution to deploy, especially in high-resolution deployments. To address this gap, we propose the Separable Law that describes how VLM performance changes with language backbone size and visual token count. We fit the law to measurements from 26 InternVL and QwenVL models, with language backbone sizes from 1B to 72B, on four high-resolution benchmarks with image sizes from 224 pixels to 8K. We find that the questions responding to scaling can be predicted from the skill they require, while a substantial fraction never responds at all. We also find that the two model families gain similarly from a larger backbone, while their gains from more visual tokens differ sharply. Combined with a cost law, the Separable Law gives a closed-form rule for allocating compute between backbone size and visual tokens. When deployment is limited to available configurations, the law identifies model and image sizes that perform close to the best feasible choice under the same budget. We hope our work offers a principled way to decide how much a model should be allowed to see at high resolution, given what it must reason about.

---


### 287. [Iterative Policy Refinement through Semantic Rollout Analysis](https://arxiv.org/abs/2610.01652)

**<font color=#1a73e8>作者：</font>** Feiyu Gavin Zhu, Qi Xu, Zhifei Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured policies improve efficiency, robustness, and interpretability in imitation learning by introducing task-specific inductive bias, but existing structure generation methods rely either on extensive human input or on static domain knowledge encoded in LLMs, which may be inconsistent with the expert demonstrations. We propose a closed-loop framework that iteratively refines structured policies using LLM-guided analysis of policy rollouts. By logging rollouts as semantically meaningful tabular data and prompting the LLM to generate diagnostic analysis code, our method identifies suboptimalities in the policy structure and iteratively corrects them without requiring human instruction. Experiments on car racing and door opening tasks show that our approach improves imitation learning performance by up to 15% over zero-shot LLM-generated structures and requires 75% less compute to achieve the same reinforcement learning performance. These results demonstrate that tabular rollout analysis provides an effective feedback signal to align LLM-generated policy structures with expert demonstrations, and we can utilize it to generate good policy structures automatically.

---


### 288. [Do MLLM Judges Judge the Edit? Auditing Bias in Image Editing Evaluation with Verified Quality Preservation](https://arxiv.org/abs/2610.01670)

**<font color=#1a73e8>作者：</font>** Yuan Huang, Zirui Song, Xiuying Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly used as automated judges for instruction-based image editing and as reward signals for model training. However, systematically auditing whether these judges are influenced by cues irrelevant to editing quality is challenging because visual interventions may themselves alter the quality being evaluated. A judgment shift can therefore be attributed to bias only when the intervention is verified to preserve the underlying editing quality. To address this challenge, we introduce EditJudgeBias, a counterfactual benchmark with verified quality preservation, comprising 1,196 real editing samples and 13 cues injected across four evaluation sites. We verify quality preservation for the requested edit using calibrated multimodal validators, controls, and human inspection. We then audit five MLLM judges along three complementary dimensions: invariance to quality-preserving cues, agreement with human judgments, and stability of pairwise preferences. Importantly, observed shifts are evaluated against each judge's own zero-dose and re-query noise floors rather than against zero. Experiments show that quality-preserving cues move every judge beyond its own noise. Fabricated majority opinions increase ratings, irrelevant visual elements cause larger shifts than whole-image manipulations, and swapping candidate order reverses up to 60.9% of pairwise decisions. Edit-region cues also tend to reduce human agreement. The three measures characterize judges differently, showing that robustness cannot be captured by a single metric.

---


### 289. [Invent a Dataset: Measuring dataset generation abilities with zero seed](https://arxiv.org/abs/2610.01674)

**<font color=#1a73e8>作者：</font>** Shivalika Singh, Andrija Djurisic, Gbemileke Onilude 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building datasets remains one of the most manual and brittle parts of AI development. In this technical report, we focus on the most extreme but also most prevalent setting real world practitioners face: a zero data regime. Here, practitioners don't have any data for the capability they want to learn. We introduce Invent-A-Dataset which is a prompt based system to go from dataset description to realistic and large scale post-training datasets. We evaluate Invent-A-Dataset against five frontier model APIs including Anthropic, Google, Open AI, DeepSeek, Zai. Across eight task types and dataset sizes up to 20K samples, Invent-A-Dataset significantly outperforms with both the highest quality (17% relative gains) while simultaneously producing the most diverse samples (19% relative gains). Its diversity advantage widens with scale of training dataset size (from parity at 200 samples to 37% relative gains at 20K samples). This translates into considerable downstream training gains, resulting in far more performant post-trained models. Invent-A-Dataset fine-tune consistently ranks higher compared to other generator fine-tunes across different post-trained model architectures.

---


### 290. [Architectural Sampling: Test-Time Scaling via Computational Diversity in Frozen Vision-Language Models](https://arxiv.org/abs/2610.01687)

**<font color=#1a73e8>作者：</font>** Akshit Singh, Shyam Marjit, Wei Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling often seeks better answers by sampling multiple responses from a frozen model, yet conventional temperature sampling generates every candidate along the same fixed computation path. We introduce architectural sampling, a training-free method that generates candidates through distinct forward computations by reusing selected blocks of decoder layers. Varying the block location and repetition count introduces computational diversity without updating model weights or adding auxiliary parameters. Across five Qwen checkpoints and twelve multimodal benchmarks, architectural sampling improves pass@9 over standard-path temperature sampling by 6.58 percentage points on average at the same nine-candidate budget. Reusing early layers yields the strongest gains, and the improvement in candidate coverage persists even under greedy decoding. The resulting candidates show lower lexical overlap and improve accuracy when used as rollouts for label-free test-time reinforcement learning. These findings extend the benefits of our architectural sampling beyond candidate coverage, demonstrating more effective learning from a model's own outputs.

---


### 291. [Acmite: Mitigating Gender Bias in LLMs through Concept-Guided Mutual Information](https://arxiv.org/abs/2610.01696)

**<font color=#1a73e8>作者：</font>** Tian Lan, Xiaoqing Cheng, Han Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can reproduce social stereotypes from their training data, motivating extensive research on model debiasing. However, existing methods often rely on explicit biased examples or predefined group-term substitutions, making them sensitive to wording and less effective at capturing stereotype concepts shared across diverse contexts. More importantly, they typically suppress biased outputs without explicitly modeling the statistical dependence between model outputs and the underlying stereotype concepts. We propose Acmite, a lightweight concept-guided framework for targeted and selective debiasing. Acmite represents stereotypes as structured semantic concepts and uses maximal marginal relevance (MMR) to select diverse concepts for debiasing. Inspired by mutual information minimization, it approximates this dependence with token-level KL divergence while preserving task semantics. A lightweight LoRA adapter is trained with the base model frozen and activated at inference time only when the input is sufficiently similar to stereotype-related concepts; otherwise, the original model is used directly. We evaluate Acmite on BBQ, CrowS-Pairs, and StereoSet, and assess general capability preservation on ARC-Challenge, GSM8K, and PIQA. Experiments across three LLMs show that Acmite effectively mitigates gender bias across complementary evaluation formats while maintaining competitive performance on bias-unrelated tasks. Anonymous code and data are available at this https URL.

---


### 292. [In-context Learning of Single-index Targets: Comparing Kernel and Feature Learners](https://arxiv.org/abs/2610.01712)

**<font color=#1a73e8>作者：</font>** Haotian Gu, Yizhou Xu, Lenka Zdeborová  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables a pretrained model to infer a task from demonstrations without updating its parameters. While much of the existing theory focuses on linear target functions, in this paper we study nonlinear cases by comparing two one-layer attention architectures on the same family of single-index tasks. A kernel learner first maps inputs through a fixed nonlinear feature map and then applies linear attention, whereas a feature learner applies attention to the original input, followed by a learned nonlinear readout. We derive predictions for their memorization and generalization errors using the replica method, retaining the effects of pretraining size, task-pool diversity, and training and inference context lengths. The resulting predictions closely match numerical experiments across a broad range of regimes. Our analysis yields phase diagrams that characterize when each architecture is advantageous as the amount of pretraining data, task diversity, and context lengths vary. We further identify qualitatively different context-length scalings for the two learners. Together, these results clarify how architectural choices interact with the dataset and govern nonlinear in-context learning.

---


### 293. [ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection](https://arxiv.org/abs/2610.01741)

**<font color=#1a73e8>作者：</font>** Yijie Zhu, Rui Shao, Jie He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predictive Vision-Language-Action (VLA) models aim to improve robotic manipulation via future observation or world dynamics forecasting. However, existing approaches often fail to realize this potential and underperform direct action prediction models. We argue that these limitations stem from modality misalignment between observations and actions, together with joint optimization conflicts that drive learning away from an action-centric objective. To this end, we introduce ATI-VLA, an Action-Centric Predictive Vision-Language-Action framework via Actionable Alignment Then Adaptive Injection. Specifically, it follows a two-step design: 1) Actionable Representation Alignment via a Shared Codebook. It aligns predictive observation and action representations by mapping both modalities into a shared discrete latent space via a unified codebook, making predictive observation latents readily usable for action generation and mitigating modality misalignment. 2) Action-Centric Adaptive Injection of Predictive Latents. Building upon this, it then injects predictive observation latents into action decoding as explicit predictive priors via a lightweight adaptive side-path, enabling adaptive predictive guidance under a single action-centric objective. Extensive experiments on both simulation and real-world robotic tasks demonstrate that ATI-VLA achieves state-of-the-art performance with faster convergence.

---


### 294. [Cog-VADU: A Training-Free Cognitive Reasoning Framework for Video Anomaly Detection and Understanding](https://arxiv.org/abs/2610.01754)

**<font color=#1a73e8>作者：</font>** Mohd Ubaid Wani, Sara Atito, Josef Kittler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Anomaly Detection (VAD) aims to temporally localize abnormal events in videos. Most existing approaches rely on dataset-specific training and curated annotations, limiting generalization in open-set scenarios. Recent zero-shot methods based on Large Vision- Language Models (LVLMs) alleviate this dependency but often lack temporal continuity and structured reasoning. We propose Cog-VADU, a fully training-free framework that reformulates VAD as a sequential cognitive reasoning task. Cog-VADU introduces Chain-of- Anomaly Detection Thought Prompting (CoADTP), which unrolls an LVLM into a recurrent reasoning chain across video segments. By propagating structured rationales over time, the model maintains implicit temporal memory, enabling robust discrimination between com- plex anomalies and high-motion normal activities. To improve reliability, we further design a cross-modal re-ranking stage that aligns textual rationales with visual embeddings, enforcing semantic consistency and temporal coherence for refined and stable predictions. Extensive experiments on multiple public VAD benchmarks demonstrate that Cog-VADU achieves competitive zero-shot performance. Moreover, cross-model evaluations show that CoADTP consistently enhances reasoning-based anomaly detection in a model-agnostic manner, pro- viding interpretable and generalizable anomaly understanding for real-world applications.

---


### 295. [OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming Video Interaction](https://arxiv.org/abs/2610.01762)

**<font color=#1a73e8>作者：</font>** Xiangyu Zeng, Yuandong Yang, Zhiqiu Zhang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video LLMs must retain evidence before its relevance to future tasks is known and respond when sufficient evidence becomes available. The challenge is to form reusable factual memory without compromising real-time perception. We introduce OneStreamer, which jointly learns query-independent evidence recording and task response through a shared proactive generation process. Its Proactive Hierarchical Caption Memory (PHCM) produces time-grounded local-detail captions and summaries of completed events. Streaming caption targets supervise the interpretation of observed video prefixes during training. At inference, model-generated records complement a recent visual window, providing reusable factual context without revisiting historical visual features. Proactive State Transition Learning (PSTL) reduces the dominance of repeated waiting states by preserving supervision at all output anchors and selecting representative state-change and state-persistence tokens. We further develop a streaming data synthesis pipeline that aligns output content and timing with available evidence. Combining the resulting streaming captions and QA with cleaned open-source data yields OneStreamer-1M, a broad-coverage streaming video interaction dataset with over one million records spanning diverse tasks. Our 4B model achieves the best results among the compared methods across all eight evaluated streaming video understanding benchmarks. Ablations show that retaining generated captions improves historical QA without degrading real-time perception. PSTL also outperforms dense state supervision while supervising only 27.5% of annotated state tokens. Together, these results support proactive generation as a shared learning interface connecting perception, memory formation, and timely response in streaming video interaction.

---


### 296. [TopK-Guided: Adaptive, Budget-Aware Activation Sparsity for Efficient LLM Inference](https://arxiv.org/abs/2610.01763)

**<font color=#1a73e8>作者：</font>** Mukund Agarwalla, Chih-Jen Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation sparsity speeds up large language model (LLM) inference by setting unimportant activations to zero so that the corresponding computations can be skipped. Existing training-free methods, however, make different trade-offs: threshold-based methods such as TEAL adapt the sparsity level to each token but do not tightly control the realised sparsity, while TopK-based methods such as WINA enforce a fixed sparsity level but use the same sparsity budget for every token. Both also apply the same budget across transformer blocks, despite large differences in block sensitivity. We introduce TopK-Guided, a training-free method that addresses both limitations by combining bounded token-level sparsity adaptation with sensitivity-aware block-level budget allocation. Across Llama-2 and Llama-3 models, TopK-Guided consistently improves perplexity and downstream accuracy over TEAL and WINA while preserving essentially the same sparsitydependent projection compute as WINA, with the largest gains at high sparsity. Ablations show that both components provide complementary improvements.

---


### 297. [VideoEvolve: Evolving Agent Harnesses for Video Temporal Grounding](https://arxiv.org/abs/2610.01766)

**<font color=#1a73e8>作者：</font>** Bingjun Luo, Yuhuan Fan, Jialin Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video temporal grounding aims to localize events in videos from natural-language queries. For agents built around frozen video-language models, the harness determines how queries guide temporal predictions and how those predictions are refined. Manually refining these harnesses requires diagnosing grounding failures and coordinating changes to both agent workflows and instructions. We introduce VideoEvolve, a framework that automatically evolves agent harnesses for video temporal grounding. VideoEvolve uses a Cloze-Structured Harness Representation that preserves stage interfaces while leaving agent workflows and instructions open to evolution. Branch-Guided Harness Evolution preserves promising code branches for continued refinement, using execution feedback to guide local edits and validation to determine which improvements are carried forward. Experiments demonstrate improved grounding performance across multiple benchmarks. Component analyses identify instruction refinement as a consistent source of gains, while the benefits of evolved code vary across evaluation settings. Together, these results support automated harness evolution as an effective approach to improving video temporal grounding. Code is available at this https URL .

---


### 298. [A Matryoshka Hierarchical RAG for Efficient Multi-Hop Question Answering](https://arxiv.org/abs/2610.01767)

**<font color=#1a73e8>作者：</font>** Gianluca Bonifazi, Christopher Buratti, Michele Marchetti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems for multi-hop Question Answering (QA) must balance retrieval quality with computational cost. This cost is incurred during indexing time, through the use of expensive Knowledge Graphs (KGs) or Large Language Models (LLMs) to generate summaries, or during querying, through iterative LLM-driven retrieval. To reduce it while maintaining retrieval quality, we present MatRAG, a hierarchical framework that combines RAG systems with Matryoshka Representation Learning (MRL). MatRAG addresses both kinds of cost by aligning the semantic hierarchy of a clustering structure with the nested structure of MRL. Specifically, it organizes the corpus of documents into a Directed Acyclic Graph (DAG) of clusters with progressively coarser granularity. Each level is indexed by a lower Matryoshka dimension. MatRAG pairs an iterative, top-down traversal of the DAG with an entity-driven mechanism that controls the hop budget and re-ranks candidates. We evaluated MatRAG on three standard multi-hop QA benchmarks against seven representative baselines. MatRAG outperforms its strongest competitors in terms of retrieval quality; furthermore, it reduces indexing costs by avoiding KG construction and LLM-based summarization, and lowers query-time costs through dimension-aware similarity.

---


### 299. [The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching](https://arxiv.org/abs/2610.01768)

**<font color=#1a73e8>作者：</font>** Alessandro Pegoraro, Daryan Merx, Phillip Rieger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increasing capabilities of Large-Language-Models (LLMs) and LLM-based agents, users are increasingly using them to solve everyday problems, such as answering e-mails or providing programming support. Existing work has extensively investigated security and privacy risks, such as prompt injections and the disclosure of sensitive data to chatbot providers. While various solutions were developed to address these risks, including input structuring to prevent prompt injections or deploying local LLMs to avoid sharing confidential data with chatbot operators, LLMs also pose the risk of leaking confidential data to third parties.
In this paper, we demonstrate with LLMLeak a novel attack vector where malicious software that runs locally but cannot communicate directly with the internet abuses LLMs to establish a covert channel. While inputs that instruct the LLM to send data directly via generated code are easy to detect and network libraries are typically restricted, LLMLeak relies only on the LLM's tool to fetch websites for further information. A malicious software component on the client side embeds a secret into a URL. It presents the referenced website as providing information required for a benign task, such as migrating a software library. When the LLM accesses the URL, the attacker receives the encoded secret through an attacker-controlled DNS or web server. We perform an extensive evaluation on eleven open-parameter models, observe an attack success rate of 79.7%, and also conduct a case study on real-world chatbots, demonstrating the relevance of LLMLeak.

---


### 300. [VETO: Video Efficient Token Optimization for Vision Language Models](https://arxiv.org/abs/2610.01785)

**<font color=#1a73e8>作者：</font>** Gueter Josmy Faure, Hao Ping Wang, Min-Hung Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Processing long videos with Vision-Language Models (VLMs) is bottlenecked by the quadratic cost of visual tokens, making long-form inference prohibitively expensive. While single-axis compression methods mitigate this, they hit a hard efficiency floor because they treat spatial and temporal redundancy independently. We present VETO (Video Efficient Token Optimization for Vision-Language Models), a training-optional plug-in that eliminates this bottleneck through dual-axis compression: (i) an intra-frame compressor that merges semantically similar tokens within each frame via optimal-transport inspired matching, and (ii) an inter-frame compressor that identifies and merges temporally redundant frames. The key design insight is hierarchical ordering: by first compressing spatial dimensions, VETO drastically reduces the cost of subsequent global temporal matching, bypassing the efficiency wall of single-axis approaches, with an advantage that grows with modern fully-fused attention infrastructure. Empirically, VETO achieves up to 45% faster inference (e.g., on LLaVA-OneVision-7B) while preserving or improving accuracy. Under extreme token starvation (10% budget), VETO outperforms VFlowOpt (54.9%), VisionZip (52.6%), and FastV (47.9%) with 55.7% accuracy. We demonstrate universal applicability across LLaVA-OneVision, InternVL-2.5, and LongVA, with zero-shot accuracy preserved or improved in all cases.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
