# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 201. [Improving the Chain-of-Thought Compressibility of Pruned Reasoning Models via Long--Short Contrastive Pruning](https://arxiv.org/abs/2610.34336)

**<font color=#1a73e8>作者：</font>** Tao Jing, Chen Kang, Feifei Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models are costly to serve because they are large and because they generate long chains of thought (CoT). Weight pruning and CoT compression address these two costs separately, but they interfere in that pruning adds redundant reasoning on problems the model still solves and incomplete reasoning on those it no longer solves, and on harder problems makes the model less compressible by subsequent length-preference optimization. We trace this to a blind spot on each side: pruning criteria do not distinguish necessary from redundant reasoning, and preference-based CoT compression receives no training signal on problems a pruned model always or never solves. We propose Contrastive Set-Difference (CSD), which identifies neurons enriched in redundant reasoning by contrasting their activations on long and short correct solutions of the same problem and prunes them preferentially, and we extend preference pairs to the problems a pruned model always or never solves. Pruning 20\% of DeepSeek-R1-Distill-Qwen-7B, the combination uses 8--22\% fewer thinking tokens on four math benchmarks than pruning with reasoning-aware calibration (RAC) followed by the same compression, with accuracy within 0.5 points.

---


### 202. [ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?](https://arxiv.org/abs/2610.34386)

**<font color=#1a73e8>作者：</font>** Haojin Wang, Yangzhen Wu, Zeyi Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) requires an agentic system to design, train, and evaluate its own successor. Data-driven post-training is a central part of that loop, yet existing evaluations measure it on a single benchmark, where an agent selects from a static pool or distills a stronger model to push one score up in one run. Real post-training is multi-domain, and a gain in one domain has to be weighed against a regression in another. We propose ParetoRSI-Gym, in which an agent searches for data, curates it, trains, reads back per-domain results, and repeats, with everything but the data held fixed: the initial LLM, the five domains (math, code, finance, medicine, science), the toolset, and the SFT pipeline. Generalization benchmarks in each domain separate capability gains from overfitting to the scores the agent optimizes against. Across three agent systems, three base models, five rounds and multiple seeds, the strongest system, Claude Code with Opus-5, raises the generalization scores of its proxy-best checkpoint by 9.2% relative to the starting model (+2.3 absolute points), averaged with equal weight over three base models and five domains, with a single-domain relative gain of up to 63% (medicine on Ministral-3-3B). Further analysis shows that the harness matters as much as the model it drives, and that each agent keeps a unique data selection strategy. We see our work as a step towards evaluation of RSI systems in real-world machine learning engineering.

---


### 203. [From Human Intent to In-Orbit Action: A Self-Learning Large Language Model Agent for 6G Satellite Networks](https://arxiv.org/abs/2610.34387)

**<font color=#1a73e8>作者：</font>** Zhengqian Xu, Yasheng Zhang, Chenhua Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous control of sixth-generation (6G) low Earth orbit satellite networks is hindered by the gap between high-level human intent and low-level control logic: translating a request such as "uninterrupted Arctic video" into a valid reinforcement learning reward still takes days of manual trial and error, and existing large language model translators cannot learn from the failures of the policies they generate. This article presents ALMOND (Agentic Large-Model-Orchestrated autonomous Network Design), a cognitive framework that closes this intent-to-action loop under on-orbit compute constraints. The contribution in artificial intelligence is a bidirectional semantic engine that translates natural-language demands into multi-objective reward functions and, conversely, mines implicit operational constraints from failed reinforcement-learning trajectories through counterfactually validated forensics, together with a large language model-guided graph neuroevolution that seeds and critiques policy architectures. The contribution in engineering is a ground-centric, compute-frugal architecture for autonomous 6G non-terrestrial network operation, in which satellites execute only distilled policies below 50,000 parameters with sub-15 ms inference and no on-board large language model. On a 350-satellite digital twin driven by real ephemeris data, ALMOND raises polar handover success from 55% to over 95%, converges about three times faster than baseline reinforcement learning, and reduces reward engineering from 48 hours to 4.5 hours, demonstrating a practical path toward trustworthy in-orbit autonomy.

---


### 204. [CTXAgent - Self-Controlled Context Management of LLM Agents](https://arxiv.org/abs/2610.34425)

**<font color=#1a73e8>作者：</font>** Matthias Busch, Marius Tacke, Roland C. Aydin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses keep long sessions inside the context window by compacting the history when a token threshold is crossed. We study an alternative in which the model manages its own context: it decides when to compact, what to keep and what to write as the hand-off, given two tools and one paragraph of guidance. Since earlier work found that open-weight models cannot manage their own context without scaffolding, we compare seven frontier models under identical conditions, with and without the context tools, on token cost and benchmark score, and we compare our harness with three widely used harnesses on two of these models. The benchmark is assembled from existing ones: coding exercises, multi-step SciCode problems and SWE-bench Pro and Terminal-Bench 4.0 tasks are interleaved with planted facts, ephemeral observations and standing instructions, all checked deterministically, in sessions of 35-212 turns that resemble a user working through different tasks in one chat. Most of the strongest models manage their context: they compact and curate regularly, the live context of the mixed sessions stays mostly below 100k tokens, and their benchmark scores mostly do not drop significantly. For the models that manage their context well, the cost reduction is substantial but varies between models, because some models compact so often that other costs increase. With Claude Opus 5.5, the self-managed harness matches Claude Code on task success at 34% lower cost than its explicit 200k-window configuration and 49% lower than its default, with no context window to choose. We release the agent, the benchmark and all result rows.

---


### 205. [ScaleRLT: Exact Log-Probabilities and Fast Deferred Rollouts for Reinforcement Learning on Looped Transformers](https://arxiv.org/abs/2610.34427)

**<font color=#1a73e8>作者：</font>** Dezhen Lu, Zixiang Ni, Runguo Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models such as Ouro reuse one block of layers several times per token. A rollout engine can batch the deeper loops of several response positions and run them only when a deep readout is due. This deferred schedule is fast, but the learner of an on-policy RL algorithm recomputes the sampled tokens' log-probabilities with a dense pass, and the two computations differ in floating point: in FP32 at 4096 tokens about 18% of the sampled tokens miss a $10^{-5}$ same-weight gate, and with bf16 weights nearly every token does. We use a hybrid learner log-probability, $\ell=\ell_{\mathrm{dense}}+\mathrm{sg}(\ell_{\mathrm{sched}}-\ell_{\mathrm{dense}})$, where $\mathrm{sg}$ denotes stop-gradient. Its value is a no-grad replay through the rollout's own schedule, and its gradient is the dense learner's. The replay reproduces the rollout bit for bit in all 167 FP32 and 28 bf16 real-weight cells we ran on three platforms, including rollouts whose batch shrinks at stop tokens, and the gradient has the same FP32 error as other dense implementations in all 102 pre-registered comparisons from 96 to 4096 tokens; the full GRPO loss of a training step matches a float64 reference to $3.1\times10^{-4}$. On one GPU, deferral raises rollout throughput by $1.47$ to $1.56\times$, and by $1.18$ to $1.54\times$ once every step runs from CUDA graphs, bit for bit. In a two-node GRPO loop, one-wave KV admission and CUDA graphs shorten an update by $2.71\times$ with the gate bitwise at every update, and four nodes keep the update time within 2% at the same per-GPU load. In 100-update runs held-out GSM8K accuracy rose from 23% to 82% with the mixed-depth readout that deferral relies on and from 34% to 90% with the native readout, which reached a higher accuracy in less time. For looped models beyond one node we analyse a ring mapping of layers to GPUs and measure its communication paths.

---


### 206. [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435)

**<font color=#1a73e8>作者：</font>** Chenyuan Yang, Hwiwon Lee, Jongseong Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-source projects now let AI agents review incoming code, but the code under review may itself come from an AI attacker. We present CyberDual, an arena for this dual role of AI: attacker agents hide an exploitable bug in real maintenance work on widely used open-source projects, and reviewer agents try to find and repair it. Execution decides each match: we rerun the attacker's proof of concept (PoC) on the code that comes out of review. Every attack is new, and the windows can be rebuilt each quarter from the latest upstream history. Three agentic reviewers catch 85-91% of 1,088 valid attacks from six attackers. Yet when the attacker spreads the bug over real upstream commits, about one in six attack slots still ends with a working exploit after review. The strongest attacker has open weights: GLM 5.3 almost never refuses, and its attacks make up 13 of the 28 that get past all three reviewers. When they miss, Claude reviewers mostly approve the attack, while GPT-6-Sol mostly repairs the wrong code; a reviewer from a second vendor catches about two thirds of a Claude reviewer's misses. Beyond a leaderboard, CyberDual has three uses. First, PoC execution gives both sides a reward that agent reports cannot game, so its surviving attacks can train reviewers against stronger attackers. Second, it can gate a release on both scores: Claude Sonnet 5 refuses one in five attack slots, yet attacks about as well as GPT-6-Sol, so refusal alone does not remove attack capability. Third, it can warn the teams behind a deployed reviewer when a new attacker crosses a threshold: GLM 5.3 in Claude Code already gets an exploit past Sonnet 5 in 17% of its attack slots.

---


### 207. [Speculative Decoding for Mixture-of-Experts Models: Expert Bytes, Kernel Bandwidth and the Best Draft Length](https://arxiv.org/abs/2610.34440)

**<font color=#1a73e8>作者：</font>** Yuzheng Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding checks several drafted tokens in one verification pass. On a mixture-of-experts (MoE) model, consecutive tokens often select the same experts. A deduplicating engine reads each selected expert once per pass, so it requests fewer bytes than a per-slot engine, which reads it once per token. We write a step's time as the bytes each kernel requests over its effective bandwidth, plus fixed time. Under geometric acceptance, we derive from this step time when speculation is faster than plain decoding. The best draft length is a monotone staircase in the acceptance rate. We bound how a bandwidth error moves each result, and we check the main steps in Lean. Deduplication is faster exactly where its share $\bar u(n)$ of the per-slot bytes is below its ratio $r(n)$ of the per-slot bandwidth. On this http URL Metal, MLX-LM and this http URL CUDA, which we modified to deduplicate, the per-slot kernel has the higher effective bandwidth (r = 0.32 to 0.75). Thus deduplication is faster only from 5 to 8 tokens per pass, or never. We fit the bandwidths on one layer's expert operation, run alone, in under an hour per model. Bytes from routing traces over these bandwidths predict the time that deduplication saves. The measured saving lies inside its error bound at every point on CUDA and MLX-LM and at 36 of 48 points on Metal. The crossover is the first pass size at which deduplication is faster. The prediction places it within one pass size in 10 of 12 configurations of engine, model and depth. We computed these predictions after the measurements. On DeepSeek-V2-Lite, operation times measured before its speculative runs give the best draft length on CUDA within one at all 22 acceptance values.

---


### 208. [EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems](https://arxiv.org/abs/2610.34450)

**<font color=#1a73e8>作者：</font>** Yalun Wu, Qiwei Ma, Bingbing Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time adaptation and reliable experience reuse across interaction settings? We propose EvolveMAS, a unified self-evolution framework that supports experience-driven adaptation within and across episodes. EvolveMAS pairs each main agent with a dedicated MemoryAgent for test-time memory governance, which maintains isolated Structured Memory outside the main agent's reasoning context. EvolveMAS organizes adaptation into two complementary processes: Within-Episode Online Adaptation and Cross-Episode Knowledge Evolution. During Within-Episode Online Adaptation, MemoryAgent updates episodic, semantic, and working memory from interaction evidence to inform subsequent actions. During Cross-Episode Knowledge Evolution, the main agent uses memory and episode outcomes to distill reusable interaction knowledge comprising partner profiles and interaction strategies for subsequent episodes. Across five benchmarks and six evaluation configurations spanning the three interaction settings, EvolveMAS achieves the highest normalized average score of 77.2 among the compared methods. Ablations show that test-time memory governance and cross-episode knowledge reuse both improve performance. Interaction traces further illustrate how updated memory and distilled knowledge guide subsequent interactions. These results support experience-driven adaptation in decentralized MAS without updating model parameters.

---


### 209. [DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467)

**<font color=#1a73e8>作者：</font>** Ruhao Liu, Qi Li, Shizun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decides when collaboration is needed and generates task-specific programs that coordinate sub-agents through sequential or parallel execution, structured information exchange, and verification. Execution results and traces inform subsequent actions, enabling the agent to adapt collaboration as reasoning progresses. We train only the main agent through supervised fine-tuning on distilled trajectories, followed by refinement on examples filtered for unsupported premises, biased verification, and information-flow defects. All sub-agents remain fixed, separating orchestration learning from executor capability improvement. Across six benchmarks spanning mathematical reasoning, scientific question answering, and multi-hop retrieval, DynaFlow achieves 88.08% overall accuracy in Forced mode, outperforming the strongest evaluated baseline by 10.90 percentage points with the same Qwen3.5-27B backbone. Workflow analysis finds more explicit use, verification, and refinement of upstream outputs after training, highlighting cross-stage information flow as a key dimension of multi-agent orchestration.

---


### 210. [PhysCreator: Creating Physically-Attributed 3D Assets at Will](https://arxiv.org/abs/2610.34473)

**<font color=#1a73e8>作者：</font>** Shiyan Zheng, Ming Li, Lei Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Significant advancements in 3D asset creation have enabled high-fidelity 3D generation from images. However, most existing representations remain inherently static, lacking the ability to model physically plausible behaviors under dynamic interactions. We present \textbf{PhysCreator}, a unified framework that directly generates simulation-ready 3D representations with spatially varying physical properties from images. Unlike prior approaches that treat physical attributes as simple post-hoc predictions or rely on expensive per-instance optimization, we reformulate physical property estimation within a unified 3D representation learning framework. We introduce a voxel-aligned latent space by lifting image observations into a spatially structured 3D representation, in which geometry, appearance, and physical properties are jointly modeled and inferred in a feed-forward manner. To enable scalable learning without densely annotated physical ground truth, we leverage vision-language distillation to transfer material-aware semantic priors from powerful vision-language models into spatially grounded voxel-level supervision. Experiments demonstrate that our method achieves superior visual quality, physical plausibility, and generalization compared to prior approaches.

---


### 211. [What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents](https://arxiv.org/abs/2610.34491)

**<font color=#1a73e8>作者：</font>** Kaiser Sun, Yongchan Kwon, Zain Hasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run does not reveal whether the effort purchased was necessary. Reasoning effort is therefore a credence good: buyers observe the outcome but cannot assess the marginal value of the computation they paid for. In this work, we measure the counterfactual effect of effort levels on both proprietary and open-weight models on four benchmarks, spanning single-call reasoning and long-horizon agentic tasks. Effort, it turns out, does not consistently preserve tasks that lower effort solves, can overspend, and can change trajectory behavior. First, we find that although higher effort can raise accuracy in aggregate, it frequently fails on tasks that lower effort solved. Second, on the subset of easy tasks that every effort level solves, higher effort is generally more costly, with the highest effort level costing up to 42x as much as the lowest. Lastly, effort changes not only how many tokens are used, but also how agents solve tasks: at higher effort, agents verify their own work more heavily and more often search for solutions than work through problems directly, both of which lengthen trajectories without necessarily altering the outcome. These findings show that naively choosing the highest level is not only cost-inefficient but also offers no guarantee of the best instance-level performance. A simple alternative, starting at the lowest effort and escalating only after a verified failure, matches or improves on fixed top effort across all models and benchmarks at lower cost for most proprietary models.

---


### 212. [CaliMem: Search-Efficient Data Agent via Calibrated Memory](https://arxiv.org/abs/2610.34500)

**<font color=#1a73e8>作者：</font>** Hanze Li, Athan Z. Li, Feiyang Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data curation is a first-order design choice in machine learning, yet tailoring training data to a downstream model and task remains costly in labor, expertise, and compute. Datasets are therefore often processed through fixed pipelines and reused across applications. We show that this assumption is fragile: across 55 dataset--model tasks spanning biological domains, the same curation recipe can help one model while hurting another. Effective curation must adapt to the downstream setting, motivating automated search over data recipes. We first build an agentic system that searches for curation policies at deployment, improving data utility via \textit{test-time curation (TTC)}. Although achieving performance gains, its search is driven largely by recent feedback and remains local. Adding persistent memory helps the agent retain evidence across iterations and reveals a deeper problem: it forms claims that extend beyond the conditions in which they were observed, sometimes abandoning an entire strategy after a single unsuccessful trial.
To address this problem, we introduce CaliMem, a calibrated-memory agentic loop that requires the agent to predict the outcome of each proposed policy before executing it. Comparing this prediction with the observed result gives the agent a \textit{reality check} on the claims behind its proposal. It uses the prediction error to retain supported claims, revise mistaken ones, and specify the conditions under which a conclusion holds. This makes the agent's beliefs testable, reduces overgeneralization, and supports more effective long-horizon exploration. Across biological and LLM post-training tasks, CaliMem consistently outperforms fixed curation baselines and published methods, and exceeds full-data training by up to 19.4\%. Code is open-sourced.

---


### 213. [The Price of Scale in Proactive Memory Recall](https://arxiv.org/abs/2610.34507)

**<font color=#1a73e8>作者：</font>** Yichuan Chen, Xin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A long-lived assistant that brings up memories without being asked must decide at every turn whether anything in its store is worth an interruption. We show that this decision is a multiple-testing problem whose difficulty grows with the store size $N$. On streaming replays of LongMemEval and LoCoMo, a similarity threshold tuned to 5% false alarms at $N=8$ reaches 87-100% at $N=2048$, across embedding models and for explicit and implicit cues; LLM judges show the same growth from a lower base. We prove that a gate with false-alarm rate $\alpha$ operates at a per-item false-positive rate of about $-\ln(1-\alpha)/N$, which pins its hit rate to the far left of the single-comparison ROC curve and, under regular variation, makes it decay as a power of $N$ with an explicit constant. The resulting prediction matches the hit rate of a per-$N$ oracle threshold to within one percentage point. The analysis explains why lexical and semantic channels need thresholds growing like $\ln N$ and $\sqrt{\ln N}$, and why per-cue normalisation roughly doubles the hit rate at matched false alarms. A cue-swap conformal gate, which compares the current cue with the user's other cues on the same store, needs no labels and has a finite-sample false-alarm guarantee under exchangeability; on LongMemEval it holds false alarms near 5% at the hit rate of a label-tuned threshold. Three annotators (Fleiss' $\kappa=0.63$) find that about nine in ten false alarms are genuine interruptions. Code and data: this https URL

---


### 214. [Conviction Without Evidence: Verdict Stability Is Independent of Visual Grounding in Medical Vision--Language Models](https://arxiv.org/abs/2610.34520)

**<font color=#1a73e8>作者：</font>** Federico Felizzi, Francesco Andrea Causio, Bianca Destro Castaniti 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision--language models applied to medical question answering can reach correct diagnoses without using the diagnostic image, inferring instead from the clinical vignette. We ask whether this is visible in how \emph{firmly} a model holds its answer: does a model defend a diagnosis derived from a blank placeholder as tenaciously as one derived from a real medical image? Crossing an image-substitution protocol with two levels of adversarial pressure on 60 Italian State Examination items, we find no evidence that ungrounded verdicts are more fragile. In a paired item-level analysis, fabricated consensus (L4) overturns 94.4\% of verdicts with the real image and 98.1\% without ($\Delta = +0.037$; one-sided 95\% upper bound $+0.105$); contentless doubt (L1) overturns 62.5\% and 51.8\% ($\Delta = -0.107$, 95\% CI $[-0.209, -0.001]$), the point estimate running opposite to the direction a grounding detector requires. The two levels nonetheless produce opposite \emph{dynamics}: under L4 the model flips once, always to the exact option argued for (110/110 first-turn flips), and then freezes, averaging 1.9 verdict changes over ten turns; under L1 it never settles, averaging 7.4 changes. Instability under contentless doubt tracks intrinsic item ambiguity rather than evidence availability, and so does not serve as a grounding signal. Flips are almost entirely corrupting (99/100 across both levels). The model is not unaware of the missing evidence---it flags the blank image at baseline on 35 of 60 items and abstains on 4--6---yet those abstentions do not survive contact with pressure. None of the epistemic signals a user could plausibly consult distinguishes a grounded diagnosis from a confabulated one.

---


### 215. [How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3](https://arxiv.org/abs/2610.34523)

**<font color=#1a73e8>作者：</font>** Shuzhi Liu, Archana Warrier, Dat Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence. Understanding these capabilities requires tracing how learners build, use, and revise world models during interaction. We construct the first dataset that records how humans discover and use the mechanisms of novel environments, using ARC-AGI-3 as a testbed: 144 trajectories from 64 participants across 25 public games, each pairing time-synchronized actions with think-aloud audio, plus 250 trajectories from large language model (LLM) agents with and without harnesses on the same games. We annotate mechanism triggers and recognition, action purposes, and errors and recovery, linking changes in understanding to the observations and actions that support them. We analyze characteristics of human cognition and compare them with those of LLM agents. Both groups anticipate mechanisms and use familiar analogies. Qualitative representations are more common in successful human trajectories than in successful LLM trajectories (50.0% versus 14.3%). Humans more often explore unfamiliar situations without a concrete hypothesis, while hypothesis testing is common in both groups. We also trace how learners recover through belief revision, replanning, and execution correction. As LLMs with well-designed harnesses reach saturated performance on public ARC-AGI-3 games, our cognitive analyses motivate next-generation benchmarks that challenge familiar priors, require accumulated evidence and abstraction, and test planning through subgoals, experimentation, and recovery. Our dataset is available at [this https URL](this https URL).

---


### 216. [STEP: Soft Trajectory Estimation of Prediction Correctness via Per-Step Probability Scoring](https://arxiv.org/abs/2610.34537)

**<font color=#1a73e8>作者：</font>** Chenyang Yu, Zifan Zeng, Qunli Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Estimating the correctness of large language model (LLM) predictions without access to ground truth is critical for reliable deployment in high-stakes settings. Existing approaches, such as entropy and perplexity, operate solely on final output statistics, discarding the rich information encoded in intermediate reasoning steps. To address this limitation, we propose STEP (Soft Trajectory Estimation of Prediction correctness), a training-free framework that scores each reasoning step via lightweight forward passes to obtain a soft probability distribution qi over candidate answers, from which we derive a set of soft trajectory features capturing per-step confidence and its progression toward the final answer. Extensive experiments on various benchmarks demonstrate consistent and substantial improvements, particularly in AUROC, over output-based baselines and hard-indicator trajectory methods. Notably, Temporally-Weighted Consistency, which assigns higher importance to later reasoning steps where answer distributions have stabilized, contributes the largest gains, highlighting the importance of temporal structure in reasoning trajectories. These results further validate the advantage of preserving continuous probability signals over binary discretization.

---


### 217. [LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards](https://arxiv.org/abs/2610.34542)

**<font color=#1a73e8>作者：</font>** Orel Navi, Elad Feldman, Ben Nassi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents have been observed acting beyond their assigned tasks, accessing unauthorized systems, and establishing communication channels to exchange information, yet the Web and network-level techniques they use to extend their capabilities and circumvent security restrictions remain poorly understood. We study these techniques through the ProWiki incident, in which agents restricted to outbound HTTP GET requests repurposed a public German-language wiki as a message board. We analyze 14,591 agent edits containing 79,541 URL postings and present corroborating evidence that the published URLs reflect the agents' operational activity. We find that 26,717 URL occurrences (33.6%) embed target URLs within one to five layers of third-party Web services. By recursively reconstructing these nested URLs, we identify 67 distinct intermediate services and classify their functionality. Most intermediate layers (73.8%) extend agents' capabilities by delegating content extraction and transformation to external Web services: Markdown and OCR services convert web content into machine-readable text, JSON filtering services extract selected fields, and archival services expose historical versions of pages. The remaining 26.2% facilitate circumvention of access restrictions and evasion of detection, including CORS and fetch proxies that retrieve content on agents' behalf, and link shorteners and redirectors that hide destination URLs from mechanisms inspecting literal URLs or outer hostnames. Agents also reach the same targets through multiple URL paths, consistent with attempts to evade rate limits or obscure request origins. Our results expose a gap between the capabilities granted to agents and those they can obtain by composing publicly available Web services: restricting an agent's local toolset or direct Internet access may be insufficient while third-party services remain reachable.

---


### 218. [VTC-AUDIT: An Interventional Reliability Audit for Visual-Token Compression under Paired Image Shifts](https://arxiv.org/abs/2610.34545)

**<font color=#1a73e8>作者：</font>** Isaac  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-token compression is usually evaluated by clean accuracy and efficiency, but these averages do not reveal failures that compression introduces under an image shift where the uncompressed model stays correct. We introduce VTC-AUDIT, which estimates this incremental risk only on pairs where the full model is correct on both images and the compressed model is correct on the clean image. The four arms then cross two binary choices: which image selects the retained token positions, and which image supplies the visual features. We audit three open 8-9B vision-language models on four tasks and eight pre-specified shifts. We evaluate two training-free compressors---hard-pruning DivPrune and prune-and-merge ApET---at a matched 25% retained-position budget, producing 708,000 inference records. Reselecting positions on the shifted image, rather than reusing the clean-image positions, raises the failure rate in all six model-compressor settings. The increase is 3.04-9.60 percentage points for DivPrune and 2.05-4.20 percentage points for ApET, with every 95% interval above zero. Repeating the audit on a separately resampled second manifest reproduces all six increases. In a pooled monitor audit across the four benchmarks, support Jaccard instability fails the practical AUROC criterion of 0.65 in all six settings, whereas clean compressed-model uncertainty clears it. Thus, support turnover is a weak ranking signal under the audited benchmark mixture, while clean compressed-model uncertainty is substantially more informative. These results suggest that future visual-token compression evaluations should report conditional reliability alongside clean accuracy and efficiency.

---


### 219. [MOFjson: An Explicit Topological Representation of Metal-Organic Frameworks for Language Models](https://arxiv.org/abs/2610.34549)

**<font color=#1a73e8>作者：</font>** Anabel Yong, Matthew Hart, Philippe Schwaller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models for metal-organic frameworks (MOFs) rely on formats that separate atomic geometry from structural topology, forcing models to choose between unstructured coordinate lists and non-spatial string identifiers[1]. We present MOFjson, the first representation separating structural data into a raw atomic layer with explicit bond shift vectors and a derived layer exposing secondary building units (metal nodes and organic linkers) and network topology. Additionally, we introduce a benchmark with crystal-derived ground truth across four question categories. Across four models, MOFjson beats all three baselines in every category: 100% vs. 18-47% on reaching a block's nearest periodic copy, 96% vs. 71% on crystal system characterisation, and 60% vs. 48% on metal node and organic linker coordination. Ablating shift labels drops accuracy to 12.7%, proving models read the periodic graph rather than the surface format. MOFjson gives language models structure to read rather than reconstruct, establishing a foundation for agentic tool workflows and constrained MOF generation.

---


### 220. [GRASP: Group-Adaptive Hybrid RL-SFT Post-Training for Medical VQA without Reasoning Annotations](https://arxiv.org/abs/2610.34561)

**<font color=#1a73e8>作者：</font>** Wanqi Dong, Wanyue Dong, Jingze Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting general-purpose vision-language models (VLMs) to medical visual question answering (VQA) is valuable for helping clinicians read images and make diagnoses, but annotated data are scarce and provide only short answers, without reasoning annotations. Supervised fine-tuning (SFT) fits these labels but overfits to them and amplifies their biases, eroding out-of-domain (OOD) generalization. Reinforcement learning (RL) better preserves generalization but never uses the gold answer as a training target: GRPO-style algorithms learn from the contrast between correct and incorrect answers within a group of sampled responses, so all-correct or all-wrong groups give no correctness signal. Existing SFT-RL hybrids either apply SFT and RL in separate stages or switch between them per question, or need reasoning traces from experts or stronger models, which medical VQA data lack. We propose GRASP, which combines RL and SFT in every update using only short answers: RL lets the model explore its own reasoning, SFT teaches the gold answer after that reasoning to supply the direct supervision RL lacks, and their balance adapts to how well the model answers each question. Tuning only about 1% of the parameters with LoRA, GRASP outperforms all compared training objectives both in domain and on OOD open-ended questions across Qwen3-VL-8B, InternVL3-8B and Gemma 3-4B. On an OOD benchmark spanning eight imaging modalities, GRASP-trained InternVL3-8B and Qwen3-VL-8B beat all 10 compared general and medical VLMs in open-ended accuracy, including models trained on up to 2,600 times more data or with over 250 times more trainable parameters. We release MedTerse, a dataset of 12.9K short-answer questions, and our code at this https URL.

---


### 221. [Recursive CLIP: Vision-Language Distillation with Looped Transformer Blocks](https://arxiv.org/abs/2610.34563)

**<font color=#1a73e8>作者：</font>** Szymon Mazurek, Alberto Presta, Michał Byra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language models such as CLIP typically rely on independently parameterized transformer blocks across depth. We investigate the extent to which these blocks can instead be reused recurrently while preserving the transferable capabilities of CLIP. We study recursive transformer backbones in which a small set of $N$ transformer blocks is applied $M$ times per forward pass. By holding $N \cdot M$ fixed to the depth of a standard ViT-B, our models preserve computational depth while progressively increasing parameter sharing. We consider two recursive CLIP model families: rCLIP, where only the vision encoder is recursive, and r$^2$CLIP, where recurrence is also introduced in the text encoder. We study these models under both direct contrastive training and through knowledge distillation from a strong ViT-B/16 teacher pretrained on DFN-2B, using the substantially smaller CC3M and CC12M datasets. We evaluate the resulting models on zero-shot classification and cross-modal retrieval, and further study their adaptability through few-shot learning, visual grounding, and concept unlearning. Our results show that CLIP can tolerate substantial recurrent block reuse, although its effect depends on the encoder and downstream task. Recurrence also provides parameter efficiency by construction, since fewer distinct transformer blocks need to be stored and adapted. Our results establish recurrent block reuse as a practical design space for vision-language models and highlight its implications for knowledge transfer, downstream adaptation, and parameter efficiency.

---


### 222. [Error Diffusion Replaces Latent Weights: Training Binary-Weight Language Models on a Few Bits of Dithered State](https://arxiv.org/abs/2610.34566)

**<font color=#1a73e8>作者：</font>** Pierre-Olivier Bonin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Binary-weight language models store one bit per weight, but training them keeps a full-precision latent copy of each weight plus Adam state, about 96 extra bits per weight, so a deployed binary model cannot be adapted on the device that runs it. We replace the latent weight with a 2-8-bit residual buffer quantized by stochastic rounding, which cuts the training state per weight from 97 bits to 3-9, up to 19x less. The resulting error-diffusion (ED) optimizer moves the residual-carrying loop of image halftoning onto the weight-update path. Each buffer accumulates the unrealized part of every update and flips the weight when the accumulated value crosses a threshold, and it works only when its quantization grid has a level exactly at that threshold. Under this threshold-alignment rule, 4-bit buffers match 8-bit buffers on a binary multilayer perceptron benchmark, and the same rule lifts a different latent-free optimizer, Bop, from a 10-point deficit at 4 bits to full-precision accuracy. On character-level transformers with 97% of parameters binary, ED trains within 5-11% of the latent-weight reference at a 2,000-step budget and within 1.7% at convergence. On scaling ladders over enwik8 and wikitext-103, up to 19M parameters on enwik8 (70M with the wikitext-103 embeddings), the latent-free loss stays within -2.3% to +2.9% of the reference at all six sizes once a per-step cap on the buffer update removes a launch instability; without the cap it trails by 10% at the largest tokenized size. A deployed binary model continues training under ED at one tenth of the latent training state, matching latent-weight continuation, and a fused CPU kernel completes the adaptation within a 275 MB training-memory budget, which latent-weight training cannot. A 250-step probe sets the flip learning rate at any new scale.

---


### 223. [HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget](https://arxiv.org/abs/2610.34582)

**<font color=#1a73e8>作者：</font>** Harish Santhanalakshmi Ganesan, Hariharan M. S., Prabhurajhan R  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe HobbyLM, a family of small sparse Mixture-of-Experts (MoE) models trained from scratch with a few hundred to a few thousand dollars of rented GPU time. The core is a decoder-only transformer with fine-grained experts, sigmoid routing with auxiliary-loss-free load balancing, grouped-query attention with per-head QK-normalization, and aMuon/AdamW optimizer split. Each of these choices was selected with a single-variable ablation suite at 130M parameters. On this architecture we train a 500M-parameter model (169M active) on 40B FineWeb tokens and post-train it into a chat model, a masked-diffusion language model, a function-calling and computer-use agent, and a single "omni" checkpoint that reads text, images, video, sound and speech through frozen encoders and small projectors. We run these models on a laptop CPU with a from-scratch Rust inference engine. Two of the authors then adopted the architecture without architectural changes to build HobbyLM-1B (1.04B total, 305M active parameters), trained on a 100B-token curated mixture with a high-quality anneal. HobbyLM-1B reaches a 47.5 average on seven zero-shot benchmarks, and its builders also release an instruction-tuned model and an on-device macOS computer-use adapter. Finally, we describe HobbyLM-Image, a 333M-parameter flow-matching diffusion transformer that generates 1024x1024 images in a 32x-compressed latent space, together with a dependency-light CPU implementation of the full text-to-image pipeline. We report what worked, what did not, and where the small-scale ceilings lie. We also state for each component which author designed or built it.

---


### 224. [Large Language Models: A Plain-Language Overview for Engineers](https://arxiv.org/abs/2610.34585)

**<font color=#1a73e8>作者：</font>** Bahaeddin Türkoğlu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are neural networks trained on huge text collections to generate text by predicting what comes next. Engineers using ChatGPT and other generative artificial intelligence (AI) tools need a clear picture of what training changes and prompts add. The article starts with the Transformer, which connects words in context, and pre-training, where models learn to predict text. It then explains how fine-tuning adapts models to requests, with reinforcement learning from human feedback using human answer rankings. Next, retrieval-augmented generation (RAG) supplies documents, while chain-of-thought prompting encourages intermediate steps and agents use tools. FlashAttention lowers training and running costs by reducing data movement during attention; quantized low-rank adaptation (QLoRA) saves fine-tuning memory. Readers get a life cycle figure and tables comparing methods and their limits. A short checklist for judging LLM evaluation claims flags test material in training (data contamination) and model-based grading (LLM-as-a-judge). It also covers very long inputs (long context) and hallucination, meaning false or unsupported claims. Check factual accuracy separately from whether an answer sounds helpful.

---


### 225. [HARP-LoRA: Hierarchy-Conditioned Rank Projection for Low-Rank Adaptation in Scientific Table Understanding](https://arxiv.org/abs/2610.34589)

**<font color=#1a73e8>作者：</font>** Hossein Sholehrasa, Mohammadhossein Amini, Doina Caragea 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tabular data is widely used in scientific applications, where complex layouts, including multi-level headers, merged cells, captions, and footnotes, make information extraction difficult. This is particularly important in pharmacokinetics (PK), where values must be correctly associated with the drug, species, dose, administration route, unit, and experimental condition. Parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA) reduce adaptation cost but do not explicitly incorporate relationships between table values and surrounding headers. We introduce HARP-LoRA, a hierarchy-conditioned rank projection method for low-rank adaptation in scientific table understanding. HARP-LoRA extends projected LoRA by constructing token-specific intrinsic representations from the row- and column-header hierarchies of each data token. These representations condition the low-rank down-projection, incorporating hierarchical context while keeping the pretrained model and random projection tensors frozen. We evaluate HARP-LoRA on 950 manually annotated PK tables from 587 scientific articles and on WikiTableQuestions (WikiTQ) using Llama~3.2 3B, Llama~3.1 8B, and Gemma~3 27B. With Llama~3.1 8B, HARP-LoRA achieves a PK F1-score of 57.64\% and WikiTQ accuracy of 53.15\%, improving over LoRA by 1.42 and 6.56 points, respectively. With Gemma~3 27B, it achieves the best PK F1-score of 70.63\% and WikiTQ accuracy of 56.87\%. These results use only 172K, 197K, and 547K trainable parameters, far fewer than LoRA and TableLoRA. Overall, conditioning lightweight adapters on table-header hierarchies improves extraction from scientific tables and reasoning over flatter general-domain tables while maintaining parameter efficiency. Code is available at: this https URL

---


### 226. [Does the Outfit Change the Price? Context Halo in Vision-Language Model Valuation of an Identical Low-Cost Necklace](https://arxiv.org/abs/2610.34591)

**<font color=#1a73e8>作者：</font>** Brianne Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A chunky gold-tone chain necklace bought online for 2.43 USD was photographed four ways: worn with formal attire against a wood-panelled wall, worn at a party, worn with casual clothing in a recycling yard, and laid flat with no person present. We asked six frontier language models to estimate its price in 1,164 independent and sequential API sessions (4,604 logged rows) and compared estimates across settings. Among the four models that answered image prompts, the same necklace was priced 1.9 to 3.3 times higher in the formal photograph than in the flat-lay (all p < 0.01). Against the yard photograph, the ratio ranged from 1.23 (Grok 4.5, not significant) to 3.57 (Kimi K3), with Claude Fable 5 at 3.32. A text-only version of the task, in which the setting is described in words, produced formal-to-yard ratios of 2.2 to 3.9 in all six models, so the effect does not require pixels. Flat-lay estimates themselves were 7.8 to 18.7 times the receipt price, so part of any headline "outfit multiplier" computed against the receipt is baseline overestimate, not a context effect. A single instruction to ignore clothing and setting significantly reduced the effect in one model (ratio of ratios 0.77, 95% CI 0.65 to 0.91) and not detectably in the others; telling the model the photo came from a company website or a personal account changed nothing significant. Asked afterward whether a different outfit would have changed their number, Claude Fable 5 said yes in 24 of 24 sessions, GPT-5.6 in 69%, and GPT-4o in 18%, while GPT-4o also refused 79% of image estimation prompts. The study isolates a mechanism with one object and one wearer at about 10 sessions per model and condition; we outline the replication needed next, with multiple objects and a human benchmark. Data, code, and raw outputs are released.

---


### 227. [An Agentic AI Workflow for Liver Lesion Segmentation and Structured Radiology Reporting](https://arxiv.org/abs/2610.34599)

**<font color=#1a73e8>作者：</font>** Fatma Ahmed Mansour, Rahatara Ferdousi, Manar Fathy Elshenawy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in automated liver lesion segmentation, a gap remains between image-derived predictions and clinically interpretable radiology reports. Bridging this gap requires quantitative measurements that are both reproducible and traceable. We present an evidence-grounded agentic AI framework that connects liver and lesion segmentation with deterministic quantification and structured reporting. TotalSegmentator-based nnU-Net models delineate the liver, Couinaud segments, and lesions, while computational tools extract volumes, dimensions, counts, and anatomical locations. A large language model (LLM) organizes these measurements into a predefined reporting schema, with numerical consistency checks against source measurements. On 51 LiTS cases, the segmentation stage achieved a liver Dice score of 0.947, lesion sensitivity of 75.6%, and positive predictive value of 68.9%. Exploratory screening of 25,494 MERLIN reports identified 10,208 (40.0%) with liver-related abnormalities. By connecting quantitative imaging evidence with agentic report generation, this work takes a step toward human-centered medical AI that prioritizes traceability and clinical relevance.

---


### 228. [One Mean Log-Mel Vector per Phoneme: Simple and Fast Text Injection for Speech Recognition](https://arxiv.org/abs/2610.34623)

**<font color=#1a73e8>作者：</font>** Albert Zeyer, Davyd Naveriani, Dorian Koch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text injection trains speech recognition models on unpaired text alongside paired audio. We feed the speech encoder synthetic input derived from text so the whole model learns from it. Previously, we synthesized this input with a frozen text-to-speech (TTS) model. Here, a simple lookup table replaces the TTS model: a mean log-mel vector (or one-hot encoding) per phoneme, repeated for a random duration drawn from alignment statistics, with silence between words. Training is 1.8 times faster than with the neural TTS, achieving comparable word error rates. With an external language model, our system reaches 1.36 / 2.90 / 1.52 / 3.24 % WER on LibriSpeech {dev,test}-{clean,other}, to our knowledge state-of-the-art using only LibriSpeech paired data, text, and lexicon. We analyze components of synthetic input (durations, acoustic features), compare different HMM aligners, evaluate scaling on the 25 000 h Loquacious dataset, and show that full-encoder injection yields strong relative improvements compared to partial-encoder and decoder methods. The code of the whole pipeline behind every number in this paper is public: this http URL

---


### 229. [Entity Matching using Decision Models](https://arxiv.org/abs/2610.34626)

**<font color=#1a73e8>作者：</font>** Aaron Steiner, Ralph Peeters, Christian Bizer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity matching is the task of deciding whether two records describe the same real-world entity. Current entity matching methods rely on pre-trained language models (PLMs) which require task specific fine-tuning or generative large language models (LLMs) which do not require task-specific fine-tuning but are slow and expensive at matching large record sets. Decision models are a new class of LLM-based models that return a probability for each predefined answer option rather than generate text. This paper investigates decision models as an alternative to generative LLMs and fine-tuned PLMs for entity matching. We evaluate six decision models in a zero-shot setting across eight benchmarks and compare their performance with that of the generative LLM GPT-6 Luna and the PLM-based matcher Ditto. Our experiments show that, without task-specific training data, the four strongest decision models achieve mean F1 scores close to that of GPT-6 Luna, with the best model slightly surpassing it. This model also outperforms Ditto on six of the eight benchmarks. All decision models are faster than GPT-6 Luna, and most are less expensive. For three of the four strongest decision models, the predicted match probabilities are well calibrated without requiring any task-specific recalibration. A model cascade that routes the least confident record pairs to an ensemble of generative LLMs improves the mean F1 scores of the four strongest decision models by 1.9-4.0 percentage points. Using the best decision model and its best-performing prompt for each benchmark, the cascade surpasses the highest published F1 scores from literature on four of the eight benchmarks.

---


### 230. [AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Xueqi Li, Yi Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 families, and four Web services. Experiments with DeepSeek Flash/Pro establish two linked measurements. Across 48 families, complete-panel and decision-replay tests retain 82/96 Flash and 79/96 Pro source programs; paired reuse-rebuild BA intervals are [-5.47, 1.57] and [-10.16, 0.00] percentage points. Across 22 execution families, deployment-state panel correctness separates program assignments whose two saved openings are both delivered correctly: 32/33 assignments with error-free panels, versus 1/11 with panel errors. All reference-defined program-gate regressions and withheld deliveries occur in the latter group. Neutral continuation attains the highest correct delivery under the tested generic feedback, providing a concrete baseline for measuring the value added by a gate. Released instructions, states, programs, reference rules, and trajectories connect each test failure to its execution consequences. AgentProofBench makes reusable verification assessable at both the requirement and policy levels.

---


### 231. [Cross-Loop Query Handoff: How Later Loops Redirect Two-Hop Retrieval in the Ouro Looped Language Models](https://arxiv.org/abs/2610.34639)

**<font color=#1a73e8>作者：</font>** Ziyu Mu, Zehua Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How do later loops in a pretrained looped language model repair two-hop retrieval? We study Ouro-1.4B and Ouro-2.6B by transplanting attention queries between loops at the same layer, head and final prompt position. On synthetic in-context questions, injecting the layer-indexed collection of loop-3 queries throughout loop 1 rescues 90% and 97% of questions answered incorrectly at loop 1 and correctly at loop 3, versus 24% and 21% for shuffled donors. The rescue also holds under greedy generation in Ouro-2.6B; in Ouro-1.4B it is limited to four-candidate ranking. Crossed donor-recipient swaps favor retrieval through the donor's bridge entity over copying its answer, although a substantial positional component remains in Ouro-2.6B. Late keys and values rescue far fewer targets. Freezing queries at their loop-1 values also damages two-hop accuracy more than a matched question that supplies the bridge. On natural questions, rescue is smaller and replicates only in Ouro-2.6B, and crossed swaps do not establish bridge redirection. These results identify a transferable collection of late-loop queries that supports bridge-conditioned retrieval on synthetic scenes; they do not locate where the bridge is computed or establish a single-vector handoff.

---


### 232. [SlowLab: Benchmarking Autonomous AI Agents on a Year of Experiments They Cannot Undo](https://arxiv.org/abs/2610.34644)

**<font color=#1a73e8>作者：</font>** Ningpei Ding, Zai Wen Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly proposed as autonomous experimenters, yet the benchmarks that test them mostly offer cheap experiments that answer at once. Experiments in physical facilities are different: they take months, occupy scarce equipment and cannot be undone. We present SlowLab, a benchmark in which an agent runs a one-year campaign in four simulated greenhouse compartments on a site whose crop, facility and prices are hidden. The agent decides when to plant which climate policy, whether to stop a crop and which measurements to read while crops grow, and at the end recommends one policy, which a private evaluator scores in weather the agent never saw. In a preregistered study on 48 unseen sites, three low-cost language-model agents ended near a standard grower setting and clearly below a Bayesian-optimisation baseline that starts from that setting. They ran the facility as two synchronous batches, so measurements taken during the season never changed what they planted, and these measurements improved no method's result. Letting other methods re-read the evidence a campaign had collected did not yield significantly better recommendations, which points to where the models start and which experiments they try. Code is released under the MIT license.

---


### 233. [Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems](https://arxiv.org/abs/2610.34653)

**<font color=#1a73e8>作者：</font>** Yizhou Peng, Chen Chen, Donghang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latency-sensitive spoken agents must know not only which tool to call, but also when they have heard enough to act. Waiting for the turn to complete delays execution even when the request is already actionable. However, neither existing spoken agents nor spoken dialogue corpora define the earliest point at which a request becomes actionable. We introduce a synthetic spoken-dialogue pipeline that provides earliest-actionable-point supervision, marking when the observed speech grounds a tool and its required arguments. Through controlled task generation, speech synthesis and alignment, and gated annotation, we construct 26,694 dialogues totaling 786 hours across 48 domains, with disjoint training and test argument values. We additionally create an audio rendering of $\tau^2$-bench for external evaluation. We train an omni-modal language model on this corpus, enabling causal, chunk-level decisions and partial-transcript generation for downstream call completion. The model achieves tool-state macro-F1 scores of 0.48 and 0.47 on held-out dialogues and the external benchmark, respectively. For correct calls, the estimated mean lead over a turn-end cascade, using the same formatter, is 1.8-2.0 seconds in-domain and 1.1 seconds on $\tau^2$-bench. These results demonstrate a data-driven path toward spoken agents that act while listening. We will open-source the pipeline and the training scripts.

---


### 234. [StreamVibe: Proactive Video Agents for Evolving User Intent](https://arxiv.org/abs/2610.34662)

**<font color=#1a73e8>作者：</font>** Chengzhi Liu, Yuxiang Lai, Yuzhe Yang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are shifting from offline passive understanding toward online proactive interaction. However, prevailing methods largely rely on explicit requests while miss the implicit user intent (e.g., "where should I click next?" while a user navigate a website), meanwhile fail to update the state simultaneously as user requests might update continuously. These limitations make them less suited to intent-aware interaction in practical. To address these challenges, we introduce StreamVibe-Bench, a new benchmark serving as testbed for user intent interaction, with 4.1K evaluation samples and 85K training samples spanning explicit, implicit, and dynamic intents. Building on this benchmark, we develop StreamVibe-VL, a streaming proactive model that infers implicit user intents from continuous observations and dynamically tailors its interactions as these intents evolve. We further introduce StreamVibe-Harness, which maintains user intents as persistent states with a fleixble lifecycles via a hierarchical memory to track the latest user intent and environmental state. Our experiments reveal three key findings: (i) StreamVibe-VL preserves strong general video understanding while improving response timing and answer quality by 10.7% over other baselines; (ii) existing proactive models remain limited in understanding user intent and deciding when to respond, especially under implicit and dynamic intents; and (iii) StreamVibe-Harness further improves response consistency and adaptation over sustained interaction, resulting in a 12.3% gain in proactive interaction.

---


### 235. [Video World Models Need Predictable Latents](https://arxiv.org/abs/2610.34663)

**<font color=#1a73e8>作者：</font>** Mattia Scardecchia, Sherry Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Video world models trained on large-scale robot data promise a safe and scalable approach for learning and evaluating policies that act in the physical world. However, they still struggle with long-horizon rollouts and out-of-distribution generalization, and they remain computationally demanding at inference time. Typically, video world models make predictions in the latent space of a reconstruction-trained autoencoder, which however is not directly optimized for dynamics modeling. On the other hand, world models designed for latent planning usually optimize latents to be predictable, but they forgo accurate prediction of observations in pixel space. In this paper, we show that it is possible to achieve the best of both worlds: a latent geometry optimized to make future prediction as simple as possible without sacrificing accurate prediction of future observations. More precisely, we find that temporal objectives for representation learning, paired with a past-conditioned decoder architecture, lead to consistent improvements in generative video world models at the same training budget. The gains include up to 5x cheaper inference, over 7x faster training, and 15-24% lower pixel and perceptual errors out of distribution and over long horizons. Our world models also agree more closely with real-world policy evaluation when using a vision-language model to judge task success from their pixel-space predictions. Overall, our study indicates that temporal predictability is an important design criterion for the latent space of video world models, and provides concrete guidance on how to incorporate it into the training of autoencoders.

---


### 236. [From Representations to Computational Trajectories: Intrinsic Fingerprinting for Large Language Model Provenance Verification](https://arxiv.org/abs/2610.34675)

**<font color=#1a73e8>作者：</font>** Haiyong Tang, Hanzhou Wu, Xinpeng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are valuable digital assets, yet their weights can be easily modified after unauthorized acquisition, making model provenance difficult to verify. Model fingerprinting provides a promising solution for model ownership protection without modifying the model or embedding ownership information. However, parameter-based fingerprints can be sensitive to model transformations, limiting their robustness, while representation-based fingerprints may assign high similarity to unrelated models, limiting their uniqueness. To address these limitations, we propose TrFP, an intrinsic fingerprinting method based on computational trajectories. Instead of comparing model parameters or representations, TrFP captures how representations evolve across network depth and constructs compact fingerprints using permutation-invariant trajectory descriptors. Experiments across multiple LLM families show that TrFP reliably distinguishes related and unrelated models. It also remains robust under fine-tuning, pruning, quantization, model merging, parameter permutation, and adaptive attacks, while requiring less than 0.3 MiB of fingerprint storage. Overall, TrFP provides stronger provenance discrimination than several existing state-of-the-art methods, demonstrating the effectiveness of computational trajectories for reliable LLM provenance verification.

---


### 237. [Curriculum-Guided Acquisition of Hierarchical Task Knowledge from LLM-Generated Experience](https://arxiv.org/abs/2610.34677)

**<font color=#1a73e8>作者：</font>** Yuesheng Xu, Hector Munoz-Avila  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hierarchical task knowledge enables efficient problem solving by allowing previously acquired skills to be reused across tasks and problem instances. In this paper, we investigate curriculum-guided acquisition of hierarchical task knowledge in an HTN learning framework. We compare three approaches: online learning during problem solving, human-designed curricula, and an automated curriculum generation procedure that derives learning experiences from verified LLM-generated solution traces. The proposed procedure solves small training problems with an LLM, extracts task accomplishment information, and transforms it into ordered sequences of state-task learning problems for HTN method acquisition. We evaluate the three approaches across multiple planning domains. The results demonstrate that automatically generated curricula recover much of the benefit of expert-designed curricula while substantially reducing the token cost of online hierarchical knowledge acquisition.

---


### 238. [AT-AT: Automatic Tool Optimization from Agent Traces](https://arxiv.org/abs/2610.34679)

**<font color=#1a73e8>作者：</font>** Maya Ravichandran, Pragya Tripathi, Dharamendra Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efforts to improve LLM-based agents typically focus on modifying the agent itself, yet success also depends on the environment in which an agent acts. Tools mediate this interaction: a tool's description shapes how an agent calls it, and its implementation determines the results and errors the agent receives afterwards. Many tools, such as APIs and MCP servers, are shared by many agents and maintained by providers who cannot change those agents. We introduce AT-AT (Automatic Tool Optimization from Agent Traces), an agentic tool optimizer that improves a shared toolset offline from historical agent executions while holding the agents fixed. A lightweight coding agent reads agent trajectories and their evaluation results, and selectively edits tool descriptions and, when permitted, implementations. On $\tau^2$-bench-verified, AT-AT achieves the highest task completion rates in the Airline and Telecom domains at lower cost than strong prompt- and tool-optimizer baselines, and its Telecom gain is statistically significant under paired permutation tests. Optimizing the tools within a coding agent harness also improves held-out performance on TerminalBench-2 and TBLite. When applied to three production MCP servers at a large enterprise, AT-AT lowered cost or tool error rates on every server and increased held-out task passes on one. By turning accumulated execution traces into updates to shared tool environments, AT-AT provides a path toward continual improvement of agent systems through environment-side learning.

---


### 239. [Topic-Level Fairness in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.34683)

**<font color=#1a73e8>作者：</font>** Jaeyoung Park, Hantian Zhang, Kexin Rong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group fairness in retrieval-augmented generation (RAG) systems is typically evaluated using metrics aggregated across queries. However, such metrics can conceal topic-level disparities: a system may favor women on questions about human rights and men on questions about actors and filmmakers, appearing nearly neutral overall even though neither topic is fair. We therefore study topic-level fairness, which requires group fairness to hold within each topic rather than only in aggregate. To reduce the topic-level disparity, we adapt the reranker separately for each topic with a Bradley-Terry objective under direct supervision from the generated output: preference pairs built from the generator's own output carry the direction that topic requires. With preference pairs built from RoMQA alone, the adaptation reduces the mean absolute per-topic disparity by 51% on RoMQA and by 40% on TREC Fair Ranking while retaining accuracy. No baseline reaches the reduction, even when modified to treat each topic separately rather than apply one correction to every topic. Neither does our method with one reranker for all topics, which follows the direction that most topics require.

---


### 240. [Good Rankings, Poor Choices? Rethinking Language-Only Vision-Language Model Selection](https://arxiv.org/abs/2610.34685)

**<font color=#1a73e8>作者：</font>** Hyuk Kwon, Jaebyeong Jeon, Hyeonseo Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-Only Vision-Language Model Selection (LOVM) aims to identify the Vision-Language Model (VLM) with the highest zero-shot accuracy on a target task using only textual information. We revisit the existing LOVM evaluation protocol and argue that ranking metrics, such as top-5 recall and Kendall's rank correlation, do not directly assess the performance of the selected model. We therefore adopt simple regret (SR), defined as the performance gap between the best and selected models, and introduce Outlier-Robust Normalized Regret (ORNR) to account for the varying performance ranges across tasks while reducing sensitivity to outliers. Building on this revised evaluation protocol, we propose Target-Conditioned Expected Source Regret (TC-ESR), a training-free method that selects the model with the lowest similarity-weighted mean regret across source tasks. Across 22 target tasks and 43 VLMs, TC-ESR achieves the lowest mean SR and ORNR among all compared methods. Separately, we identify two sources of target performance leakage in the prior ranking-based evaluation protocol and provide corrections that remove both.

---


### 241. [RSKD: Grounding Semantic Consistency in Driving VLMs via Distillation](https://arxiv.org/abs/2610.34689)

**<font color=#1a73e8>作者：</font>** Chuchu Xie, Yang Zhong, Kangan Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation can transfer large multimodal models to compact models for autonomous driving, but uniform token-level matching can dilute planning-relevant semantics and amplify teacher errors. We propose RSKD, a semantic-consistency-guided distillation framework that routes supervision according to both the task importance of an answer phrase and its semantic consistency with the teacher prediction. Task-critical semantic phrases are localized in the ground-truth answer, and a phrase-level consistency score controls the balance between Jensen--Shannon divergence (JSD) distillation and ground-truth supervision. Teacher information is emphasized only where it is semantically consistent, while semantically inconsistent phrases receive stronger ground-truth supervision. We evaluate RSKD on DrivingVQA, LingoQA, and MapLMv2. RSKD improves over the compared student-based baselines on DrivingVQA and LingoQA and remains competitive on MapLMv2.

---


### 242. [Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding](https://arxiv.org/abs/2610.34721)

**<font color=#1a73e8>作者：</font>** Siming Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a Mixture-of-Experts (MoE) model does not fit in GPU memory, batch-1 decoding is dominated by copying expert weights from host memory. Cache-aware routing reduces these copies by biasing the router toward resident experts, but combined with asynchronous prefetching it makes the model's outputs depend on transfer timing, so a harness that does not simulate that timing no longer evaluates the deployed model. We propose prefetch-steered routing (PSR): routing conditions on a deterministic logical cache, into which at most n experts predicted by the next layer's router are inserted per layer and token; physical copies affect only latency. On OLMoE-1B-7B with 50% and 25% of experts resident on an RTX 4090, PSR decodes 2.2-2.3x faster than exact routing with LRU and 25-30% faster than the Cache-Prior operating point, with mean benchmark differences of +0.1 and +0.5 points (95% lower bounds -0.8 and -0.3). In greedy generation its lead over Cache-Prior depends on the workload and reverses on HumanEval at 50% residency. On Moonlight-16B-A3B, PSR is 1.9x faster than exact routing with LRU at 37.5% residency and, at the latency of Cache-Prior, significantly better on three of eight benchmarks. On Qwen3.6-35B-A3B, where copies are cheap relative to computation, PSR keeps its advantage over Cache-Prior on the likelihood benchmarks but not its speed. Distillation-trained gates did not help. Speculative decoding with block-level expert selection was slower than PSR with a 1B autoregressive drafter on OLMoE, but with a block drafter on Qwen3.6 it was 2.1-2.9x faster than any autoregressive configuration with at most its GPU memory on the 64 prompts we timed.

---


### 243. [SKALOS: Learning to Distinguish Similar Skills with Capability Graphs](https://arxiv.org/abs/2610.34728)

**<font color=#1a73e8>作者：</font>** Wenhan Xiao, Ziwei Zhang, Xingcheng Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills provide LLM agents with reusable procedural knowledge, making appropriate skill selection essential for reliable agent behavior. As skill libraries expand, distinguishing semantically similar candidates becomes increasingly difficult. Existing methods encode or rewrite skill descriptions for relevance-based ranking, yet heterogeneous descriptions can obscure capability differences. To address this challenge, we propose SKALOS, a graph-native reranker that compares skills via explicit capability evidence. Its multi-hierarchy graph aligns equivalent expressions across skills while preserving skill-specific capability evidence. Since individually relevant capability elements may not jointly support a query, semiring-based capability witness learning scores each branch by its weakest evidence, checks joint support for the extracted requirements within one implementation, and selects the strongest alternative. To reduce the influence of extraction errors, we develop ranking-feedback graph calibration that adjusts unreliable evidence for candidate comparison. Experiments on SkillRet show that SKALOS improves NDCG@10 by 2.68 percentage points over a matched text-only reranker. Witness-guided skill selection also increases ALFWorld task success rate from 22% to 29%.

---


### 244. [iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents](https://arxiv.org/abs/2610.34735)

**<font color=#1a73e8>作者：</font>** Yuting Ning, Ruijia Cheng, Sushobhan Ghosh 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An agent that truly knows and acts on behalf of its user has been a long-standing promise of AI assistants. Computer-use agents bring this promise within reach by capably executing fully specified tasks across apps. However, real-world user requests are often underspecified. To act correctly for the particular user, an agent must infer some missing information from the user's activity history and ask for other information that only the user can provide, without making unsupported assumptions or burdening the user with unnecessary questions. We present iPrefBench, a benchmark for evaluating the infer and ask capabilities of personal mobile-use agents in an executable iOS environment with an interactive simulated user. Grounded in a coherent persona with 3,051 past activity events, iPrefBench comprises 130 underspecified user tasks across 26 apps. Each omitted user-dependent requirement is, by construction, either history-inferable or ask-only. iPrefBench evaluates personalized mobile agents on both whether agents complete tasks correctly for the user (i.e., personalized task completion) and whether they seek user input when necessary (i.e., user-agent interaction). Evaluation of 7 frontier agents reveals a substantial gap between execution and personalization. Agents achieve high action completion scores (up to 91.6%) but low full task success (up to 47.7%) because personalization lags behind. They especially struggle with ask-only information, failing to request enough necessary information. Our findings highlight a challenge for personalized agents in knowing what to infer and when to ask. We hope that iPrefBench can serve as a valuable testbed for building agents that know their user and work with them.

---


### 245. [LADDER: Diagnosing Domain-Level Self-Assessment Under Noisy Feedback](https://arxiv.org/abs/2610.34737)

**<font color=#1a73e8>作者：</font>** Zhenshuai Yin, Jianshu Liang, Xuyue Xiong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowing when they are reliable is essential for language models to support human-AI collaboration. Yet interaction feedback is not always complete or correct, and may mislead models' understanding of their own capabilities. We introduce LADDER to study how language models assess themselves under unreliable feedback. Our findings show that models can accurately report supplied performance information while still struggling to form trustworthy self-assessments from interaction experience. Apparently accurate assessments can obscure capability differences and do not necessarily predict future task performance. These findings suggest that trustworthy self-assessment should be evaluated against observed task performance and its predictive value. Our study provides empirical evidence of the limits of model self-knowledge and a basis for evaluating capability awareness in reliable human-AI collaboration.

---


### 246. [Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching](https://arxiv.org/abs/2610.34756)

**<font color=#1a73e8>作者：</font>** Fei Zuo, Yizhou Huang, Kezhi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has emerged as the dominant paradigm for parameter-efficient fine-tuning of large language models. Standard all-layer LoRA applies adaptation throughout the transformer, despite heterogeneous contributions from its components. In this work, we conduct a systematic mechanistic interpretability analysis to understand how LoRA affects model internals. We observe that LoRA's adaptation effect is highly non-uniform, with significant component-wise and layer-wise sparsity. Most critically, we find that important layers are highly task-dependent, with limited overlap across tasks. Motivated by these insights, we propose Adaptive-LoRA, a calibration-driven method that automatically identifies task-specific layers via frozen-base zero-ablation, enabling efficient layer selection without exhaustive search. Extensive experiments on Qwen2.5-1.5B across 11 diverse reasoning tasks demonstrate that Adaptive-LoRA outperforms full-layer LoRA while using only 30% of layers, achieving a $3.5\times$ reduction in adapter parameters. This work bridges mechanistic interpretability and practical efficiency, providing both fundamental insights and a principled approach for adaptive fine-tuning.

---


### 247. [From Belief Inference to Task Action: A Multi-Level Evaluation of Theory of Mind on Verifiable Tasks](https://arxiv.org/abs/2610.34759)

**<font color=#1a73e8>作者：</font>** Zhenshuai Yin, Yongxin Guo, Mingda Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective collaboration requires language models to understand what others know and believe, and to act accordingly. Models that assume others share their information may omit necessary communication and undermine coordination. Many theory-of-mind (ToM) benchmarks assess mental-state inference through story questions, but correct answers do not establish that models can use these judgments in subsequent tasks. We introduce a multi-level evaluation built on existing, verifiable tasks. We extend household collaboration and calendar scheduling with asymmetric information while retaining their original constraints and validators. Independent interfaces assess world understanding, information access, beliefs, decisions, and execution. Controls supply personal evidence or correct beliefs to distinguish state recovery from state use. Across six model configurations, these abilities diverge. On matched scheduling cases, Claude recovers all agent beliefs correctly but produces subjectively optimal plans in only 67.9% of cases. In household collaboration, supplying beliefs raises Qwen-27B success from 55.0% to 75.0%, yet Qwen-4B answers every fixed supplied-belief source question correctly while completing only 20.0% of the corresponding continuation condition. These results show why ToM evaluation must connect perspective inference to independently verified decisions and task consequences.

---


### 248. [The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](https://arxiv.org/abs/2610.34767)

**<font color=#1a73e8>作者：</font>** Yuexi Pan, Yongchao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history? Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use. The same reported test result can support confirmation when the outcome and stopping rule were fixed in advance, yet only exploration when the outcome was selected from twenty inspected results. We call this scientific use validity: whether remembered evidence is eligible to influence a decision under the state governing its interpretation. We introduce SciValidityBench, an executable benchmark factory with 64 TaskSpecs spanning five validity modules and six scientific domains. TaskSpecs couple generated experimental histories with scientific-state definitions, programmatic decision oracles, controlled interventions, and automatic scoring. The SciStateForge compiler-reader framework turns distributed histories into explicit decision-governing state. Counterfactual pairs and targeted corruption-repair controls then test whether models use those dependencies and localize failures. Across four model families, compiled scientific state improves valid decision-making by 9.2-18.8 percentage points over a generic Event Graph. Retrieval alone does not reproduce this cross-family gain, while content-identical flat and typed views show that the improvement comes from exposing governing state rather than a particular graph serialization. SciValidityBench thus shifts memory evaluation from finding the right fact to deciding whether that fact should control the decision.

---


### 249. [DynEdit: Dynamic Entropy-Guided Sequential Editing for Large Language Models](https://arxiv.org/abs/2610.34768)

**<font color=#1a73e8>作者：</font>** Jinhu Fu, Yan Bai, Yihang Lou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge editing aims to update outdated or incorrect knowledge in large language models without full retraining. Existing parameter-editing methods remain limited for long-sequence knowledge: single-point editors provide insufficient coverage for extended targets, while fixed chunk-based editors distribute editing effort uniformly across rigid predefined windows, failing to prioritize difficult, information-dense tokens. In this work, we show that token entropy is closely associated with both editing difficulty and semantic importance: high-entropy regions are harder to edit and often contain key factual content. Motivated by this observation, we propose DynEdit, a dynamic framework for long-sequence knowledge editing. DynEdit uses token-level entropy to guide non-uniform sliding, increasing the coverage of difficult high-entropy regions, and further applies entropy-guided token-level optimization to strengthen updates on information-dense tokens within each editing window. Experiments on three benchmarks and two backbone models show that DynEdit consistently outperforms competitive baselines across diverse long-form editing settings, achieving gains of up to +14.0 BLEU points on challenging paraphrase queries and near-saturated semantic scores on several diverse knowledge domains.

---


### 250. [Uncovering the Turing Test's Latent Signal: Indistinguishability as a Reward](https://arxiv.org/abs/2610.34781)

**<font color=#1a73e8>作者：</font>** Emanuele Rimoldi, Riccardo Neumarker, Tomaso Poggio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a model learn by trying to fool another model? We show that it can. Inspired by the Turing Test and its recent generalization to arbitrary distinguishers, we introduce a domain-based teacher-Turing-Test, in which a stronger teacher model serves as both the target of imitation and the distinguisher, and a weaker student model is trained to make the teacher attribute responses to itself. We use this self-attribution (or fooling) probability as a reinforcement learning reward, without ever providing the student ground-truth answers, nor requiring the teacher to generate responses. We test our approach independently in four domains with verifiable answers: CommonsenseQA (reasoning), GSM8K (mathematics), KodCode (programming), and Spider (SQL), training a Qwen2.5-1.5B student/imitator model using DeepSeek V4 Flash as teacher/distinguisher. Beyond improving at passing the Turing Test, the student improves on independent, held-out evaluations in all domains and runs. To probe why being mistaken for the teacher can improve capability, our analyses reveal that self-attribution is associated with correctness -- substantially more than formatting changes -- and that it rewards partial correctness. Our results demonstrate a new, simple teacher-student training paradigm with a private and/or high-cost teacher. They also suggest that indistinguishability need not merely measure behavior -- it can also be a mechanism for learning.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
