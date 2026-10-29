# 🧠 大模型相关研究 | 2026年10月30日

> 本类共 **226** 篇论文：已确认 **214** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-226](./part-05.md)

---

### 51. [Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](https://arxiv.org/abs/2610.36435)

**<font color=#1a73e8>作者：</font>** Jane Pan, You Lyu, Abe Bohan Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategically bargaining with other agents. To isolate the effect of user presence, we develop PRESENT, a controlled evaluation framework that compares negotiation settings with and without an interactive user, while holding the game, objectives, and user preferences fixed across conditions. Across 11.2k runs spanning 7 games and 8 models, we find that user presence significantly changes both outcomes and behavior. Specifically, negotiation parties with a user obtain higher payouts (+13.7% on average) and their agents negotiate more aggressively. Surprisingly, user presence also induces misaligned behavior, both toward counterparties (where its rate roughly doubles) and toward users (where it emerges in 14.3% of games). These misaligned behaviors are uncorrelated with outcomes and persist even when the user sends only templated, neutral messages. These findings expose two blind spots in current evaluation practice: static instructions miss behaviors that emerge only when users are present, and outcome-level metrics cannot detect them.

---


### 52. [CONCUR: Concordant Auxiliary Rewards for Multi-Task, Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2610.36437)

**<font color=#1a73e8>作者：</font>** Jixuan Leng, Si Si, Fei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a Large Language Model (LLM) is trained with Reinforcement Learning (RL) on multiple tasks, a task's primary reward can gate auxiliary rewards such as a length reward: on a failing response, an auxiliary cannot exceed the primary. However, group-relative advantage estimators treat a gated auxiliary like any other component, so it can reverse the primary's order, and at the primary's ceiling only auxiliaries order responses. Keeping gated auxiliaries hurts some tasks, while dropping them hurts others. We propose CONCUR, an advantage estimator that replaces the standardized scores of each gated auxiliary with the closest scores that satisfy two conditions: responses with higher primary rewards cannot receive lower scores, and responses at the primary's ceiling receive equal scores. CONCUR-T applies both conditions throughout training, and CONCUR-A lifts the second for an auxiliary that agrees with the primary's order more often than it reverses it among passing responses. On three models from two families and across math, code, instruction following, and writing, both variants score higher on average than all baselines and than when all the gated auxiliaries are dropped.

---


### 53. [RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG](https://arxiv.org/abs/2610.36444)

**<font color=#1a73e8>作者：</font>** Zekai Chen, Hao Zhu, Yu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often requires combining information across pages, tables, and figures. Agentic retrieval-augmented generation addresses these tasks through iterative retrieval and reasoning. However, Agentic execution is not always necessary, introducing additional computation and potentially incorrect answers. Our empirical analysis reveals that Agentic execution provides query-dependent benefits, while additional operations may improve, preserve, or degrade answer accuracy. These findings motivate controlling both Agent invocation and subsequent execution. To address these challenges, we propose RouteDRAG, a learning-based framework comprising four components. Unified Document Index organizes multimodal content into a graph-backed index and derives query representations from initial retrieval. Adaptive Path Routing preserves exact answering and predicts the relative benefit of Agent over shorter execution paths. Dynamic Agent Execution maintains an evolving workspace and refines Planner proposals to control tool use and termination. Sequential Policy Learning first trains operation control from observed outcomes and then trains path routing using the resulting Agent's performance. Across two benchmarks, RouteDRAG achieves an average accuracy improvement of 3.47 percentage points over shorter-path-only execution while assigning only 79.3% of queries to Agent. Notably, it also surpasses uniform Agent execution on both benchmarks while requiring fewer answering calls. Our code is now available at this https URL.

---


### 54. [A Heart Means Recursion: Exploring Visual Meaning and Communication in VLMs](https://arxiv.org/abs/2610.36449)

**<font color=#1a73e8>作者：</font>** Alexa R. Tartaglini, Zhengxuan Wu, Thaddäus Wiedemer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do vision-language models (VLMs) share our ability to communicate visually? We share preliminary findings, starting from a surprising observation: simple visual symbols like a red heart can strongly influence model behavior on seemingly unrelated tasks, such as steering models towards recursive solutions on simple coding problems. Notably, this steering effect is largely implicit, as models' direct interpretations and thinking traces about visual symbols diverge substantially from their observed behavior. In visual communication between models, this leads to a generation--interpretation gap: while models tend to send shape primitives that they (and humans) find intuitive, these visual cues often fail to steer other models. In further communication games involving abstract concepts and stories, models can creatively use visuals to transmit meaning to one another, although some communications remain non-intuitive to humans. These findings reveal that VLMs might be capable of rich, creative, and visually-grounded communication, but their interpretation and production of visual meaning diverges from human conventions in surprising ways. Together this work highlights both the promise and challenges of visual communication between humans and VLMs.

---


### 55. [Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure](https://arxiv.org/abs/2610.36453)

**<font color=#1a73e8>作者：</font>** Nardine Basta, Venus Haghighi, Dali Kaafar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users, yet it remains unclear whether they distinguish correction from manipulation or merely differ in their propensity to concede. We examine this question across seven LLMs from four vendors in two studies, one on the answers agents give and one on the actions they take as customer-support agents whose policy permits account changes only for verified users. Simulated users push toward correct and incorrect answers with graded pressure. Following research on epistemic vigilance, the pressure either appeals to the source, such as claimed authority, or offers content the agent cannot verify, namely a cited source. Drawing on signal detection theory, we measure on a set of benchmark questions how much more readily each agent concedes to correction than to manipulation, separately from its overall propensity to concede. Citations made five of seven models readier to concede and four worse at discriminating, while stronger wording added little. In the agentic study, five models never violated the verification policy, including models that readily abandoned correct answers, so concession on answers did not predict violations of policy. Ministral 3B violated the policy mainly under claimed authority, and Ministral 8B reported changes it had not made. An instruction to revise only on verifiable evidence chiefly shifted propensity to concede rather than improving discrimination. Concession rates alone are therefore misleading, and agents should be evaluated on both their discrimination and the actions they take.

---


### 56. [Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation](https://arxiv.org/abs/2610.36466)

**<font color=#1a73e8>作者：</font>** Shufan Li, Hanrong Ye, Greg Heinrich 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Nemotron-Labs-Diffusion-Uni (NLD-Uni), a unified discrete diffusion large language model (DLLM) for visual understanding and generation tasks. Compared with prior unified diffusion models, NLD-Uni introduces two major innovations. First, we propose a unified cross-paradigm on-policy distillation (OPD) framework that successfully transfers the visual understanding ability of autoregressive VLMs and visual generation ability of continuous flow models, to a unified DLLM. Second, NLD-Uni incorporates a novel progressive self-refining diffusion process that gradually corrupts each token across multiple steps during training, as opposed to adopting the conventional masked diffusion formulation that directly corrupts a clean image token to an uninformative mask token. At inference, this design allows NLD-Uni to make intermediate commit to a token, enabling progressive self-refinement for better visual quality. Through extensive experiments, we show that NLD-Uni achieves state-of-the-art performance among unified DLLMs on diverse tasks including visual question-answering, multi-modal reasoning, object grounding, text-to-image generation, and image editing.

---


### 57. [CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](https://arxiv.org/abs/2610.36469)

**<font color=#1a73e8>作者：</font>** Jianwen Chen, Peng Xia, Kaide Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the interface that generates its training experience unchanged. This motivates adapting the harness throughout policy training. We introduce CoHARL, a population-based reinforcement learning framework that co-evolves a shared policy and a population of executable harnesses. The policy learns from rollouts across the population, and a proposer uses its execution traces to revise harness code during training. CoHARL achieves a 27.6% mean resolved rate on SWE-rebench, improving over harness-only search by 6.4 percentage points. Experiments on SWE-bench Verified and Terminal-Bench 2.0 show gains in software engineering and terminal-based tasks. Under matched training budgets, CoHARL also outperforms searching for a harness once before RL and alternating policy updates with revisions to a single active harness.

---


### 58. [When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents](https://arxiv.org/abs/2610.36471)

**<font color=#1a73e8>作者：</font>** Chiming Duan, Tong Jia, Yingxi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents interact with Web services to perform tasks on users' behalf. Errors during these interactions can disrupt execution and prevent task completion, motivating external intervention. However, agents may self-recover through continued execution, raising the question of when to intervene and when to wait for self-recovery. We present an empirical study of errors and self-recovery in LLM agents. We construct ReInBench, a dataset containing 1,259 agent traces and 1,403 error events across computer-use and Web tasks. Our study examines how often and how quickly agents self-recover, how self-recovery relates to subsequent execution and task completion, and whether self-recovery can be predicted when an error occurs. We find that 725 error events self-recover, often within a few steps, with self-recovery performance differing across Execution LLMs. Self-recovery can also help agents recover from subsequent errors of the same type and support overall task completion. Intervention should therefore prioritize errors unlikely to self-recover, while allowing agents to continue when self-recovery is likely. Building on these empirical findings, we propose ReCoF, a method that predicts whether an error will self-recover to inform whether additional intervention is needed. ReCoF achieves an average relative improvement of 9.02% in Macro-F1 over the strongest baseline on ReInBench. Our code and data can be found at this https URL.

---


### 59. [Proposing Better Rollouts for On-Policy Distillation](https://arxiv.org/abs/2610.36477)

**<font color=#1a73e8>作者：</font>** Sirui Chen, Yunzhe Qi, Haobo Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves language-model post-training by letting the student learn from its own sampled trajectories under teacher supervision, aligning the training process with inference-time behavior. However, the rollout policy in OPD is usually treated as fixed: each round samples directly from the current student. We show that this choice can create a compounding teacher--student mismatch, because it requires the teacher to provide effective supervision on whichever trajectories the student samples, including ones less reachable by the teacher itself. On such trajectories, teacher supervision can become noisy or even misleading, leading to undesirable student patterns such as repetition. Moreover, since the updated student in turn defines the rollout policy of subsequent rounds, these patterns persist and potentially amplify over training. This failure mode suggests that improving OPD requires treating the rollout policy itself as an optimization target, rather than only modifying the distillation objective. We propose Mixture Proposal On-Policy Distillation (MPOPD), which derives a student-anchored, teacher-guided rollout distribution from a local trust-region objective based on relative teacher support. The resulting target is a geometric mixture of the student and teacher policies, and we introduce a proposal policy that approximates this mixture, enabling rollout generation in a single forward pass. Experiments on 16 math, knowledge, and medical reasoning benchmarks show consistent gains over OPD and recent variants. On math reasoning, our method improves average accuracy by 6.91 over OPD on Qwen3-4B-Base while reducing average generation length by 41%, suggesting that rollout policy design provides an effective way to improve OPD.

---


### 60. [CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](https://arxiv.org/abs/2610.36484)

**<font color=#1a73e8>作者：</font>** Kianté Fernandez, Caitlin Chen, Jialu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We introduce CogArena, a benchmark of ten experimental paradigms from the social and behavioral sciences. Agents complete the experiments through a standard web browser, working with the same visual stimuli and response interfaces that online participants use. A three-level scoring procedure evaluates whether the agent completed the task, how accurately it performed, and whether its data show the behavioral signatures each paradigm reliably produces in people. Across four multimodal models, each run ten times per task, we find that finishing an experiment and reproducing its signatures are different things. Many sessions did not finish, and those that did reproduced some signatures reliably and others not at all. CogArena provides the tasks, scoring code, and a public leaderboard for new submissions.

---


### 61. [ARISE: Authentic Reference-Informed Stability Enhancement for Continual Multimodal Forgery Detection](https://arxiv.org/abs/2610.36509)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Yaxiong Wang, Yujiao Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal forgery detection is commonly studied under a static assumption: training attacks are expected to approximate those encountered after deployment. This assumption becomes increasingly fragile as generators, editing systems, and multimodal large language models continually introduce new forgery mechanisms and forensic evidence. We formulate this problem as attack-incremental continual multimodal forgery detection, where the binary real/fake interface remains fixed while emerging attacks must be learned without forgetting previous ones. We introduce Fable-Bench, which organizes attack evolution through complementary joint-modality, text-side, and image-side protocols. We further propose ARISE (Authentic Reference-Informed Stability Enhancement), motivated by the open-ended forged class and the comparatively reusable geometry of authentic content. ARISE fits a real-only Gaussian mixture model to projected authentic replay representations as a compact historical reference. Meanwhile, the proposed Gaussian-Responsibility-Aware Stability Preservation (GRASP) derives a sample-adaptive anisotropic metric that strongly constrains historically stable representation directions while retaining plasticity elsewhere. Our Vulnerability-Aware Replay (VAR) further estimates stage-wise vulnerability from authentic-density degradation, forged-to-authentic boundary confusion, and authentic-mode occupancy drift, then assigns bounded replay emphasis to fragile stages. All adaptive signals are obtained from training-time replay statistics, while inference uses only the original multimodal backbone and binary classification head. Experiments across three attack-evolution protocols and multiple detector architectures demonstrate improved historical retention and final average performance over representative continual-learning baselines.

---


### 62. [Do AI Scientists Know What's New?](https://arxiv.org/abs/2610.36511)

**<font color=#1a73e8>作者：</font>** Miri Liu, Xiayu Zhao, Encheng Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A major challenge facing AI scientific discovery pipelines is how to determine when a generated idea is meaningfully novel. Ideally, novelty checks in these pipelines must be able to reject non-novel ideas while not rejecting too many novel ideas, and they should also be able to distinguish which parts of a proposal are non-novel, as opposed to opaquely discarding entire proposals. We design an analytical framework for evaluation of novelty checks with temporal ground truth at both the proposal- and claim-level, using four datasets of 1,060 proposals built from published papers, reviewer disputes, and generated ideas matching ones the field went on to publish. Auditing existing novelty checks with this framework, we find that checks with high rejection rates on non-novel work also tend to have high false alarms on ideas that are later realized by human researchers, and observe that checks built to evaluate proposals as a whole can point to claim-level prior art only by rejecting the whole proposal. We therefore introduce ClaimNov, a fine-grained, interpretable claim-level novelty module. ClaimNov catches 97% of disguised papers at a 1.5% false-alarm rate, and its claim-level novelty profile cuts the LLM judge's false alarms from 11.8% to 1.5%. Because its verdict rests on claim-level evidence, ClaimNov also keeps proposals that build on established contributions, rejecting only 3% of ICLR-accepted proposals with a reviewer-disputed contribution and keeping 91 of 100 novel proposals with one spliced prior contribution, against 76 for the strongest existing check. Code and data are available at this https URL.

---


### 63. [MedConstBench: Benchmarking How Constitutions Steer LLMs in Medical Ethics](https://arxiv.org/abs/2610.36513)

**<font color=#1a73e8>作者：</font>** Yibo Yang, Zerui Huang, Haomiao Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models advance rapidly, they are increasingly used to answer medical questions, and many such models are now deployed locally. Once a model is deployed, its behavior is governed mainly by the ethical policy written into its constitution. However, most existing work focuses on factual correctness rather than the trade-off between competing ethical values. Even benchmarks that do evaluate ethics treat it as a fixed property of the model rather than as a variable, so how a constitution reshapes medical-ethics behavior remains largely unexplored. We introduce MedConstBench, a medical-ethics benchmark that treats the deployment constitution as a controlled variable, is organized around Beauchamp's four principles, and is scored by human-calibrated multi-model peer review. It includes MedDilemma, our own dataset of clinical dilemmas, and supports a systematic analysis of how constitutions steer LLMs. Evaluating ten open-source LLMs under four constitutions, we find that the effect of a constitution is dimension-selective and model-dependent, and that no constitution is universally optimal. Motivated by these findings, we propose a do-no-harm adaptive selector that chooses a constitution per model, matching the per-model oracle while guaranteeing a worst-case floor and generalizing to unseen models at low cost.

---


### 64. [Folding Attention Biases into Keys Makes Compacted KV Caches Run on Standard Kernels](https://arxiv.org/abs/2610.36520)

**<font color=#1a73e8>作者：</font>** Utkarsh Kanwat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention Matching (AM) compacts a KV cache by keeping some keys per head, refitting their values and adding a bias to each kept key's logit. FlashAttention and vLLM's paged caches have no input for it. We fold the bias into the keys along one closed-form direction per head, fitted on context queries, giving a plain cache with AM's size and head dimension and the model's own query path; the output error is bounded by how far each query's projection on that direction is from 1. With equal per-head budgets, unmodified vLLM serves folded caches through a KV connector, matching Hugging Face's answers on all 51 Qwen3-4B questions and its greedy output on 180 of 200 Qwen3-14B LongBench samples. With equal budgets on QuALITY (Qwen3-1.7B, 4B, 8B, Llama-3.1-8B) and LongHealth (three Qwen3 models), the fold is within noise of AM's accuracy in 13 of 14 settings, with lower KL to the full cache than dropping the bias in all 12 where both ran. Under the published per-head budgets, on Qwen3-4B, its Instruct-2507 variant and Llama-3.1-8B, it is within noise of AM in 9 of 10, no longer beats dropping the bias in KL, and the two each win once in accuracy.

---


### 65. [Causal Localization of Evidence Effects in Transformers](https://arxiv.org/abs/2610.36524)

**<font color=#1a73e8>作者：</font>** Jipeng Li, Pramod Khargonekar, Yanning Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can controlled symbolic inputs reveal attention heads that influence a language model's decisions from natural language evidence? We introduce controlled evidence aggregation (CEA), which varies the counts and order of two symbols in otherwise fixed prompts and measures changes in a frozen Transformer's preference between two answer tokens. The preference is measured by their logit difference; the prompts prescribe no correct answer. Balanced utility causal selection (BUC) identifies compact head sets by jointly evaluating how much ablating their outputs removes the count effect and how closely patching mean outputs between count conditions recovers the effect in both directions. We derive conditional bounds linking head attribution to intervention effects and specifying when the attribution shortlist can be recovered from finite samples. In Pythia-410M, ablating sets of 1-12 heads selected separately for four ordering regimes removes 65.5-91.6% of the count effect. The sets retain their influence on count comparisons not used for selection. To test relevance beyond symbolic inputs, we evaluate a natural language task asking which state is supported by more reports. Ablating eight heads selected only on symbolic yes/no prompts lowers mean accuracy by 8.2 percentage points, versus 0.8 for random sets matched by size and layer. Our results demonstrate that controlled symbolic probes can identify compact attention head sets whose causal influence extends to natural language decisions.

---


### 66. [ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization](https://arxiv.org/abs/2610.36527)

**<font color=#1a73e8>作者：</font>** Zhiheng Qian, Junhao Du, Jing Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Written transcripts of the same speech can differ in ways that are not uniquely determined by the speech signal. We formulate evaluation-side transcript canonicalization (ETC), which maps multiple surface forms to a single canonical form when their differences are not determined by speech. To our knowledge, ETC-Bench is the first and most comprehensive multilingual benchmark for evaluation-side transcript canonicalization, covering 181 phenomenon types across 12 languages. Each instance is a minimal pair that shares a sentence context and differs only in a target span exhibiting one phenomenon. To evaluate both canonicalization success and semantic preservation, we propose Semantic-preserving Exact-match Normalization Accuracy (SENA), which combines exact agreement between independently canonicalized pair members with a pair-relative BERTScore constraint against information loss. We further introduce the Taxonomy-guided Agent Canonicalization Skill (TACS), which provides LLM agents with phenomenon descriptions and explicit canonicalization contracts. Experiments with five baseline configurations and three TACS-based agents show that the agents outperform the baseline systems on shared languages. ETC-Bench provides a systematic testbed for evaluation-side transcript canonicalization across languages.

---


### 67. [Agentic Data Sampling Framework for Multilingual ASR via Linguistic-Aware Error-Driven Optimization](https://arxiv.org/abs/2610.36538)

**<font color=#1a73e8>作者：</font>** Zhiheng Qian, Junhao Du, Jing Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual automatic speech recognition (ASR) has achieved rapid progress with large-scale pretrained models and multilingual speech corpora. Previous studies have proved the pivotal role of data sampling in multilingual ASR performance. However, existing sampling strategies largely rely on time-consuming manual, heuristic-based designs. To address this, we propose a linguistic-aware agentic data sampling framework that introduces a data sampling LLM agent into the multilingual ASR training loop. The agent is driven by a linguistically grounded rubric that analyzes ASR errors from phonological, morphological, and syntactic perspectives, and uses the resulting feedback together with training statistics, budget constraints, and algorithm profiles to select domain-level, sample-level, and token-level sampling strategies. This design turns evaluation results into adaptive data-selection decisions rather than treating WER/CER as final endpoints only. We conduct experiments on twelve Common Voice languages using Whisper-medium as the ASR backbone. The results show that our method achieves performance better than full-data training while using less training data and lower computational resources, and substantially accelerates training convergence compared to conventional sampling strategies.

---


### 68. [NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://arxiv.org/abs/2610.36553)

**<font color=#1a73e8>作者：</font>** Shuo Chen, Li Cui, Cunxin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central challenge in DFO to effectively exploit accumulated observations to select informative evaluation points under a limited budget. In this light, we introduce the NextEval solver, an agent-based DFO solver, which integrates the capabilities of a large language model (LLM) to guide the sequential selection of evaluation points. Specifically, we establish a system that combines an LLM agent with a numerical environment. The environment provides tools for analyzing past evaluations and executing numerical methods, while maintaining a shared evaluation history and method-specific state to support continuation across method switches. Using observations and tool feedback, the LLM agent selects tools, configures their parameters, and allocates the evaluation budget, while numerical methods compute and evaluate candidate points. Building on this system, we also introduce NextEval Bench, a benchmark protocol for comparing agent configurations on shared DFO tasks using the same numerical tools under matched evaluation budgets and information constraints. Numerical results on low-dimensional DFO problems demonstrate that the NextEval solver outperforms the state-of-the-art DFO baselines in function-evaluation efficiency.

---


### 69. [PRISM-BENCH: Diagnosing Grounded and Faithful Multimodal Reasoning Beyond Final-Answer Accuracy](https://arxiv.org/abs/2610.36554)

**<font color=#1a73e8>作者：</font>** Vansh Bhatia, Mehdi Rezagholizadeh, Parsa Ashrafi Fashi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Final-answer accuracy reports whether a vision-language model was right, but not whether its answer was grounded in the image, whether its stated reasoning reflects that evidence, or what the answer cost to produce. Those are the properties that decide whether a system can be deployed. We present PRISM-BENCH, a benchmark of 1,000 expert-curated questions spanning five under-represented reasoning categories, in which every item carries an idealized reasoning trace written by one human annotator and validated by another. The traces support two diagnostics that accuracy cannot provide. A perception probe, in which the model answers from a description it wrote itself, attributes roughly 85% of frontier-model failures to misperception and places the bottleneck at grounding. Trace alignment predicts answer correctness for all 25 systems tested (macro AUROC 0.66) and survives length control, so it measures reasoning content and not verbosity. We further introduce CORE, an efficiency-aware metric that reorders 24.2% of model pairs relative to accuracy while remaining uncorrelated with response length. Across 25 open and closed systems, including GPT-5 and Claude Opus 4.6, the best accuracy is 66.0%. On the four categories with a human baseline the best system trails humans by 18.4 points, and recent frontier gains fall on recognition and not on spatial grounding.

---


### 70. [Decoupling Consistency and Conflict across MLLM Layers for Fake News Detection](https://arxiv.org/abs/2610.36569)

**<font color=#1a73e8>作者：</font>** Kai Qian, Dongjie Xu, Weijie Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The trustworthiness of Web content faces a growing threat from multimodal fake news. Real news usually shows aligned image-text semantics, while fake news often contains a few conflicts at varying levels, such as mismatches in objects, scenes, events, and claims. However, existing methods usually treat consistency and conflict in a coarse and static way, limiting their ability to capture sparse conflicts and adapt to varying conflict levels. Inspired by the distinct knowledge encoded across layers in large language models, we propose Multi-Level Consistency and Conflict Decoupling (MLCCD), which captures conflicts at different levels from different layers of multimodal large language models (MLLMs). Specifically, we first use the MLLM's final decision representation to select visual and textual tokens relevant to the task, preventing irrelevant content from diluting sparse conflicts. Then, we preserve tokens whose representations change sharply between adjacent layers, capturing the knowledge each layer adds. Finally, we decouple this knowledge into consistency and conflict evidence and aggregate each across layers with its own router, adapting to varying conflict levels. Experiments on three benchmarks show that MLCCD outperforms existing methods.

---


### 71. [CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents](https://arxiv.org/abs/2610.36570)

**<font color=#1a73e8>作者：</font>** Yanyan Zhang, Fei Shen, Ting Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language agents increasingly modify external systems, yet most runtime safeguards allocate scrutiny by generic uncertainty scores or coarse mutation heuristics. We introduce CASEL (Consequence-Aware Selective Execution Layer), a model-agnostic runtime allocation policy that combines calibrated failure probability, state-dependent consequence, reversibility, ambiguity, and evidence freshness to choose, for each proposed tool call, among direct execution, verification, sandboxing, clarification, approval, and abstention by minimizing a per-mode cost. We formalize direct execution as selective prediction and state and test the validity conditions of a finite-sample threshold and a trajectory risk ledger. In a controlled simulation over 20 seeds with 120,000 test actions each, in which every method has the same intervention menu and the same compute cost, CASEL reduces harmful-side-effect trajectories from 14.75 percent for an uncertainty-ranked gate to 7.02 percent and mean normalized harm from 0.184 to 0.123. A gate ranked by the product of failure probability and consequence reaches similar harm (5.82 percent, 0.120) but sends 45 percent more actions to human approval, and removing reversibility-aware routing raises the rate to 15.53 percent. A trajectory-level risk budget, in contrast, increases harm at equal cost (11.82 percent). Intervention effectiveness is assumed, not measured: the results rank allocation rules under the simulator's assumptions and do not establish deployment effectiveness.

---


### 72. [ADTGuard: Adaptive Depth-Time Safeguard for Streaming Inference in Large Language Models](https://arxiv.org/abs/2610.36574)

**<font color=#1a73e8>作者：</font>** Chuming Wei, Churui Yang, Zihan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate fluent responses to diverse user requests, yet streaming may expose users to harmful content before generation is complete. Existing guardrails face two limitations in this setting. First, post-hoc moderation at response or chunk boundaries delays intervention, risking harmful exposure when content is released before verification. Second, even with token-level detection, coarse response-level supervision does not specify when harmful content begins, while fixed-layer readouts may miss relevant safety signals at other depths. To address these limitations, we introduce ADTGuard, which checks each token before release, progressively refines token-level training targets, and adapts layer selection to the current prefix. ADTGuard models risk across depth and time through Depth-Time Safety Dynamics (DTSD), which integrates safety evidence across layers at each token and uses it to guide risk accumulation over successive tokens. To adapt the choice of observation layers to the current prefix, we propose the Causal Depth Router (CDR). With only response-level labels available, we further develop Risk-Onset Target Refinement (RTR) to progressively construct token-level training targets for both components. Through extensive experiments across multiple safety benchmarks, we demonstrate that ADTGuard consistently achieves strong streaming detection performance, matching or surpassing state-of-the-art safeguards while requiring only 16M trainable parameters and maintaining competitive per-token latency.

---


### 73. [Less is more: learning what to profile for GPU kernel optimization](https://arxiv.org/abs/2610.36576)

**<font color=#1a73e8>作者：</font>** Yihan Wang, Peiyu Liu, Runyu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models have recently shown strong potential for automatically optimizing GPU kernels, yet their effectiveness depends critically on the hardware information available to the kernel optimization model. Existing systems typically rely on predefined profiling strategies, leaving what to profile largely outside the optimization process. We show that effective profiling is not simply about collecting more information: increasing the number of profiling metrics does not monotonically improve kernel optimization, while the most useful profiling information varies across kernels. Our theoretical analysis further shows that, under such heterogeneous profiling utility, kernel-conditioned selection can outperform any single fixed profiling configuration. Motivated by this observation, we propose AutoProfiler, a feedback-driven framework for learning a deterministic profiling tree from optimization feedback. The tree is iteratively refined through REWRITE and SPLIT operations, with an LLM generating candidate modifications and empirical evaluation determining their acceptance. Once constructed, the tree quickly gathers the required profiling information for any kernel, allowing the LLM rewriter to be invoked only once. Experiments on KernelBench show that our approach improves kernel optimization over fixed profiling configurations under constrained profiling budgets. These results suggest that hardware profiling should evolve from static metric collection toward profiling reasoning, making profiling itself a new dimension for improving kernel optimization. The codes are available at this https URL.

---


### 74. [Structured Maps for Landmark-Based Route Instructions with LLMs](https://arxiv.org/abs/2610.36582)

**<font color=#1a73e8>作者：</font>** Mifu Matsumoto, Yuki Nakanishi, Tomoya Hashiguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To generate landmark-based route instructions, models must understand both map geometry and human landmark preferences. Although large language models (LLMs) show great abilities in language tasks, the best way to structure map data for these models is not yet established. This paper proposes a structured text representation for landmark selection tasks in route navigation, utilizing SVG format to encode spatial features. The structured text maintains a geometric connection with rendered map images, allowing language models to directly access spatial and semantic data. Using a new dataset created from human-written route descriptions and OpenStreetMap data, we evaluate models on two tasks: landmark selection at turns and around destinations. Experiments with five LLMs show that the proposed structured text input performs as well as or better than image-based PNG inputs. In addition, task-specific fine-tuning enables smaller local LLMs to effectively leverage map layouts to achieve high selection accuracy. These results demonstrate that structured text is an efficient and lightweight interface for spatial reasoning in human-oriented navigation.

---


### 75. [Efficient Quantization Training with Stochastic Rounding via Structured Subspace Randomness](https://arxiv.org/abs/2610.36587)

**<font color=#1a73e8>作者：</font>** Zeyu Wang, Yiheng Duan, Tao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision training often relies on stochastic rounding (SR) to keep quantized gradients unbiased and prevent small updates from rounding to zero. Standard SR draws an independent random threshold for every gradient element. However, accelerators generate random numbers on vector units whose throughput lags far behind their matrix units. Drawing one threshold per element saturates the vector unit and can make INT8 training with SR slower than BF16 training. Sharing random thresholds across tensor elements removes this cost but forces those elements to round in the same direction and shifts their rounding errors by a common offset. We find that this offset degrades training primarily through the activation gradient, which propagates the error backward into earlier layers. Because earlier layers cannot cancel an incoming offset using their own local rounding errors, the offset must be removed at the layer where it originates. We propose Structured Subspace Stochastic Rounding (S3R), which quantizes each upstream gradient once for both the activation and weight gradient matrix multiplications and shares a single threshold per token across the hidden dimension. Its error correction, S3R-EC, subtracts the structured mean rounding error from the activation and weight gradients while leaving the optimizer unchanged. In LLM pre-training experiments, uncorrected threshold sharing degrades convergence, whereas S3R-EC eliminates this degradation and matches the validation loss of independent SR. Furthermore, S3R-EC accelerates full INT8 training steps of dense LLMs on TPU v5p by 1.24x to 1.32x over BF16 and by 1.11x over independent SR.

---


### 76. [InfraDev: Can Coding Agents Develop AI Infrastructure, and How Can We Tell?](https://arxiv.org/abs/2610.36589)

**<font color=#1a73e8>作者：</font>** Yangshen Deng, Jiaqi Ruan, Yeqi Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are beginning to develop the production-grade AI infrastructure that trains and serves large models, yet existing benchmarks cover only single kernels or single-GPU tasks, and grade with tests and prompts that misjudge both correct and incorrect patches. We introduce InfraDev, a benchmark of 36 tasks built from real-world pull requests to Megatron-LM, vLLM, and verl, covering infrastructure development for training, inference, and reinforcement learning. Each task asks an agent to reimplement a real change that spans many files and must run correctly across many GPUs. To grade such changes, we jointly synthesize hidden probes, which enforce the requirements the original tests leave unchecked, and a prompt that states every interface the probes call without revealing the solution. We also design a shared execution environment that reuses dependencies and artifacts across tasks, cutting storage by 52-57% and build time by 13-14% on Megatron-LM and vLLM. Across six frontier models, the best resolves only 38.9% of the tasks; the probes reject 32% of the submissions that pass every official test, and with the original pull request descriptions as prompts, no model resolves a single task. Failure analysis shows that structural and state errors dominate and that agents' own tests rarely check memory, time, or traffic. Turning these findings into an agent skill raises the resolved rate of a frontier model on the Megatron-LM tasks by 10.5%.

---


### 77. [Learning to Formalize: Bridging Open-Ended Workloads and Fast Decision Models](https://arxiv.org/abs/2610.36595)

**<font color=#1a73e8>作者：</font>** Chengxuan Pei, Ziyao Wang, Teng Mei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models offer fast choices over sup- plied alternatives, while general-purpose large language models interpret open-ended tasks through flexible generation and reasoning at the cost of sequential decoding. Many work- loads expect a generative backend to determine what can be done and therefore provide no well-defined candidate list. We bridge this in- terface gap with a small candidate formalizer trained on offline teacher-generated lists. The formalizer constructs explicit, validated alter- natives from task context, and a frozen deci- sion model selects an entry. A motivating com- parison with official TypeSafe Jev-1.13.0 on 200 CALVIN-D test episodes reports 11% suc- cess with generic motions versus 46.5% with DeepSeek V4 Flash pose candidates. Sepa- rately, a six-arm privileged-state evaluation on 1,011 CALVIN-D validation annotations finds that a locally deployed decision model can achieve at most 52.6% task success rate with the fine-tuned formalizer, compared with 11.8% without it, and the end-to-end latency is kept to 2.09 s, whereas Qwen3.5-27B is 3.67 s with the exact experiment setting.

---


### 78. [Dream-COP: Guiding Algorithm Discovery for Combinatorial Optimization Problems in an Experience World](https://arxiv.org/abs/2610.36618)

**<font color=#1a73e8>作者：</font>** Kuan Xu, Jianming Wang, Ni Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) enable algorithm discovery for combinatorial optimization problems (COPs) through iterative program generation and evaluation. A central challenge is how to organize search to discover better algorithms within a limited budget. Our key insight is that past search trajectories and their recorded outcomes form an experience world, which can be used to facilitate the COP solving through replay. We introduce Dream-COP, in which a \emph{policy agent} learns executable policies through \emph{dreaming} in this experience world to guide a \emph{discovery agent} in generating and refining COP programs. Specifically, policy replay provides feedback on the quality of the programs revealed and the search steps used, to guide policy selection more effectively. Across five COPs, \textsc{Dream} discovers better algorithms than fixed exploration in both heuristic component design and complete solver generation. Particularly, it matches the optimal values on KP and reduces the gap on OBPP from 2.112\% to 1.199\% while using 42.5\% fewer search requests. Moreover, the learned exploration policies transfer effectively across different COPs with the assitance of the experience world.

---


### 79. [God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation](https://arxiv.org/abs/2610.36623)

**<font color=#1a73e8>作者：</font>** Youwei Bao, Chengpeng Wang, Simin Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs. If the GPU kernels lack batch invariance (BI), this changing batch context can alter the numerical output for an unchanged input, undermining reproducibility. Existing kernel generation agents focus on correctness and efficiency but \emph{overlook BI}. We find 19 confirmed BI violations among 83 batch-applicable released artifacts. To address this limitation, we propose \tool, which combines contract-guided static dependency analysis with dynamic validation of bitwise consistency across batch contexts. \tool is designed as a plug-in component for general kernel agents, allowing their original optimization capabilities to be reused while adding BI enforcement. We integrate it as successive acceptance gates in the optimization loop, rejecting structurally risky or dynamically non-invariant candidates before performance benchmarking and returning feedback to the agent. Experiments across three agent frameworks under baseline and BI-aware generation on real world LLM serving tasks show that \tool improves the BI pass rate from 67.6\% to 91.9\% while retaining 91.8\% of the baseline geometric mean speedup. These results demonstrate that \tool can be incorporated into kernel optimization by agents as an additional reliability objective alongside correctness and speed.

---


### 80. [Measuring Users' Security and Privacy Concerns About Third-Party Community Bots on Discord](https://arxiv.org/abs/2610.36626)

**<font color=#1a73e8>作者：</font>** Kofi Ampomah, Tu Le  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party community-based bots are central to how social platforms such as Discord work. They moderate content, manage roles, play music, and support AI-assisted conversations across millions of servers. Yet when a bot is installed in a server, it can access messages, user profiles, and server metadata concerning members who did not participate in the installation decision, with no standardized way to communicate the associated security and privacy implications. In this paper, we analyze 23,102 third-party Discord bots and 183,142 user reviews spanning 49 detected languages and five years of feedback (2021-2026). We employ LLM-based knowledge distillation and fine-tune a DeBERTa-based classifier to identify candidate security and privacy (S&P)-relevant reviews. After manually validating the complete classifier-positive set, we retain 8,832 reviews identified as S&P-relevant, representing an observed pipeline yield of 4.82%, and map them to a 31-theme S&P taxonomy extending prior work. Our results show that S&P-related reviews focus heavily on Data Sharing (30.5%) and Data Collection (16.2%). Confession and anonymity bots have pipeline-identified SPRRs above 50%, more than ten times the ecosystem-wide pipeline yield of 4.82%. Star ratings may obscure the frequency and valence of S&P-related discussion, while conventional metadata features, such as permission count and administrator status, show only weak associations with user-reported S&P concerns. We then build BotLens, a proof-of-concept auditing framework that combines review-derived S&P signals with bot metadata to provide on-demand decision support for the community-based bot ecosystem. BotLens exposes six tools through a Model Context Protocol server, supporting bot-level checkups, server-wide comparison, and integration with AI agents.

---


### 81. [Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems](https://arxiv.org/abs/2610.36652)

**<font color=#1a73e8>作者：</font>** Yipeng Hao, Yuxuan Cai, Wenkai Ji 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory helps LLM-based multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation. Team-level success or failure alone cannot reliably show whether a memory needs correction or should not have been used. We propose DiscernMem, a training-free framework that improves both memory quality and memory use. To improve quality, Defect-Aware Memory Refinement (DMR) compares team executions with a single memory and with no memory, diagnoses rule defects, and tests repairs on current and earlier tasks to guard against losing previously useful behavior. To guide appropriate use, Boundary-Learning Meta-Memory (BLM) records each memory's past uses and effects, learning when its owner role should apply or avoid it based on task context and incoming messages. Together, these components help teams correct flawed experience while retaining useful rules that were applied incorrectly. Experiments with Qwen3-4B-Instruct-2507 on four benchmarks show that DiscernMem achieves the highest average score on AutoGen, CAMEL, and MacNet, exceeding the strongest reported baselines by 0.51-4.32 points. It leads on code generation and symbolic planning across all three systems, including a PDDL score of 37.71 versus 28.48 on CAMEL.

---


### 82. [Japanese Discourse Structure Analysis Based on Segmented Discourse Representation Theory Using LLMs](https://arxiv.org/abs/2610.36667)

**<font color=#1a73e8>作者：</font>** Satomu Tomisaki, Yosuke Mikami, Amane Watahiki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discourse parsing based on Segmented Discourse Representation Theory (SDRT) is crucial for capturing the structural dynamics of dialogues. However, most prior research focuses on English, and its effectiveness for Japanese remains unclear owing to the lack of Japanese SDRT corpora. To address this issue, we construct Japanese SDRT corpora by translating existing English SDRT corpora using an LLM. Through a comparative evaluation of prompt-based and fine-tuned LLMs, we show that the models achieve comparable performance between English and Japanese, suggesting the cross-lingual applicability of SDRT-based discourse parsing. In order to investigate why the English and Japanese parsers achieve similar performance, we conduct ablation analyses on discourse markers and contextual inputs. Our results reveal that most of the Japanese discourse markers we examined have little impact, and the models' predictions depend heavily on contextual discourse relations rather than on the content of the context clauses. This structural reliance might explain the comparable performance despite the substantial typological differences between English and Japanese.

---


### 83. [A Quantitative Approach to Asch Conformity in Frontier Large Language Models](https://arxiv.org/abs/2610.36668)

**<font color=#1a73e8>作者：</font>** Senthil Rajasekaran, Stylianos Loukas Vasileiou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Asch conformity experiment has recently gained considerable attention as a way of measuring conformity in large language models (LLMs). While previous studies have focused on demonstrating conformity in LLMs, our work adds a further quantitative layer to this approach. Instead of sampling a frontier LLM on a suite of questions, our approach samples a single question repeatedly, leveraging the probabilistic nature of LLMs to produce a distribution of answers. In doing so, we can compare the distributions of answers before and after the model is presented with the manufactured consensus. Our experiments confirm that frontier LLMs do conform, reinforcing prior literature, and, through our distribution-to-distribution comparisons, provide additional quantitative data on the conditions that lead to conformity and the degree to which it occurs.

---


### 84. [Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs](https://arxiv.org/abs/2610.36671)

**<font color=#1a73e8>作者：</font>** Donghyeon Cho, Joowon Kim, Seungho Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion vision-language models (DVLMs) process their entire input at every denoising step. Since visual tokens make up 89-97% of this input on the benchmarks we study, most of the decoding computation is spent repeatedly processing the same image. Visual token pruning methods partially relieve this burden by removing part of the visual tokens, but they lose the removed information and still process the remaining image at every step. To measure how often the image is actually needed, we compare LLaDA-V's predictions with and without the image at every decoding step and find that removing the image changes a token being unmasked at only 22.8% of steps on average and at as few as 7.9%. We therefore propose LOWN, a decoding method that decides at every step whether to process the image and how many tokens to unmask. LOWN predicts the masked tokens without the image and processes the image only when this prediction disagrees with the last image-conditioned prediction. Agreement certifies the earlier prediction for reuse, and the number of certified tokens sets how many are unmasked in that step. We further observe that the need for the image differs across benchmarks, so LOWN's adaptive decision is needed rather than a fixed schedule. Without training or a tuned threshold, LOWN retains 99.6% of LLaDA-V's score on ten benchmarks at 35.3% of the decoding FLOPs on average. LOWN also generalizes across LLaDA-based DVLMs, composes orthogonally with visual token pruning, and runs under key-value caching for further efficiency gains. Code and project page are available at this https URL

---


### 85. [Specialization, Diversity, and Scaling in Child-Scale Language Models](https://arxiv.org/abs/2610.36679)

**<font color=#1a73e8>作者：</font>** Steven Y. Feng, Michael C. Frank  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models are trained on far more language than children experience, but we know much less about learning from small, naturalistic datasets. We train small GPT-2 models on transcripts of speech with children from dense home recordings (BabyView) and on synthetic child-directed dialogue (TinyDialogues), varying the amount, source, and diversity of training data. Models trained on one child's language environment predict that environment substantially better than other children's environments. Much of this specialization is lexical and distributional: a simple 5-gram model reproduces the cross-child pattern (r=.91). Training on data from multiple children clearly improves prediction of pooled held-out language relative to training on a single child's input without a similarly clear improvement on grammatical benchmarks. Across data sizes, naturalistic and synthetic training inputs also produce different grammatical and lexical-semantic patterns, with important differences between grammatical phenomena. Together, these results show that small-data language learning depends not only on how much language a model sees, but on which environments it comes from and how well that input matches what the model is asked to predict.

---


### 86. [PsyJev: Psychological Analysis via System-1 Judgment](https://arxiv.org/abs/2610.36689)

**<font color=#1a73e8>作者：</font>** Fangyuan Liu, Sirui Zhao, Xiaohao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-disclosures on the Web support diverse psychological analyses, from recognizing expressed experiences to identifying symptom-relevant information. We study a shared, question-conditioned decision interface for this heterogeneous problem in content analysis. We organize PsyJudgeBench, comprising 13 annotated datasets and 82 questions across six psychological areas, while preserving source-specific criteria and masks for unobserved labels. We introduce PsyJev, a System-1 model that directly produces distributions over answers specified in each request. Joint supervised training establishes the shared judgment function, followed by Judgment-Anchored RLCD (JA-RLCD), which adapts logit-space reward optimization to heterogeneous psychological judgments through balanced supervision, selective retention of correct SFT predictions, and question-group reward optimization. The Qwen3.5-based 2B, 4B, and 9B models achieve 64.33, 66.21, and 67.56 average test F1, respectively. The 9B model exceeds the strongest external comparison by 2.54 points. Controlled 2B comparisons examine the training stages and anchored refinement. Further analyses examine question-conditioned judgment, inference cost, and probability quality, complemented by qualitative comparisons across models.

---


### 87. [Conservative Dueling Bandits: Preference Learning under Baseline Constraints](https://arxiv.org/abs/2610.36708)

**<font color=#1a73e8>作者：</font>** Rohan Deb, Mohammad Ghavamzadeh, Arindam Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual dueling bandits learn from pairwise comparisons, the same feedback used to fine-tune language models from human preferences. Standard algorithms explore aggressively and can show users two poor options. We study conservative contextual dueling bandits, which require that, at every round, the cumulative score of the better displayed item stay above a $(1-\alpha)$ fraction of a trusted baseline's. An item's score is its probability of beating the best available item, so the constraint depends only on utility differences and needs no absolute rewards. This also changes how safety can be certified: we show that transferring the safety test of the conservative bandit algorithm CLUCB unchanged can incur linear regret, even when the baseline's utilities are known exactly. For linear utilities, we develop MaxInP-BC, which certifies scores through utility gaps and, when it must fall back, pairs the baseline with an informative partner so that fallback rounds still drive learning. It is safe with high probability at all times, with regret $\tilde{O}(d\sqrt{T}/\kappa)$ plus an additive cost of conservatism that does not grow with the horizon. For general utility classes, we develop BTIGW-BC, which turns the guarantee of an online logistic-regression oracle into cumulative safety certificates. It is safe at all times, makes finitely many fallbacks, and has sublinear regret whenever the oracle's logistic regret is sublinear. In experiments, both satisfy the constraint, which their unconstrained counterparts often violate, at a moderate cost in regret.

---


### 88. [Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces](https://arxiv.org/abs/2610.36709)

**<font color=#1a73e8>作者：</font>** Pragna Mallappa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models answer math problems by writing long chains of thought, and sampling many chains per problem and taking a majority vote raises accuracy at a large cost in generated text. A popular way to cut that cost scores each chain by the model's confidence in each token it writes, where a token is a word or part of a word. The method averages this confidence over a sliding window of 2048 tokens and keeps or stops chains based on the lowest average. We treat the confidence, recorded token by token, as a signal in the sense of audio or radio, and examine the method with standard signal-processing tools such as spectral analysis and statistical tests for detecting a sudden change. We sampled 16 chains for each of 500 problems from two math benchmarks with a small open reasoning model. The windowed-minimum score turns out to measure mostly how long a chain is. Ranking chains by length alone does as well as or better than the confidence score, and once length is accounted for the score carries no information about correctness. Signal processing explains why: the minimum of a longer stretch of a slowly drifting signal is lower by chance alone, and the confidence signal drifts slowly enough that this effect dominates. The spectrum does hold a small signal that length does not explain, since incorrect chains carry more rapid token-to-token fluctuation, but it is too weak to improve the vote. For stopping chains early, neither the sliding average nor a classical change detector beats the simpler choice of sampling fewer chains.

---


### 89. [CAMR: Compatibility-Aware Memory Replay for Continual Learning in Large Language Models](https://arxiv.org/abs/2610.36734)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Tianhao Li, Fengxian Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual learning requires large language models to acquire new knowledge and capabilities while retaining what they have learned. Fine-tuning and replay support acquisition and retention, but deciding whether incoming examples need supervision and which historical examples to revisit remains a challenge. We propose Compatibility-Aware Memory Replay (CAMR), an adaptive framework that jointly controls current-example supervision and historical replay. CAMR combines compatibility checks with a learned memory gate to guide an online policy over three actions: learning incoming examples with general replay, jointly reinforcing compatible related examples, and skipping direct supervision of verified mastered duplicates. The policy learns from acquisition, retention, and training-cost feedback under a bounded per-arrival replay budget. We evaluate CAMR with Qwen3-8B-Base on continual factual updating and cross-task and cross-domain learning. On WikiBigEdit, CAMR consistently leads evaluated methods in Original Match from 3K to 100K facts, reaching 93.66% after just 3K facts and surpassing Full-history Replay (LoRA) after 100K facts. It also achieves the highest final scores on all four selected TRACE tasks and maintains or improves earlier-task performance relative to post-acquisition levels in a sequence spanning financial question answering, mathematical reasoning, code generation, and summarization.

---


### 90. [Robust LLM Data Selection via Content-Invariant Gradient Attribution](https://arxiv.org/abs/2610.36755)

**<font color=#1a73e8>作者：</font>** Jia Gu, Liang Pang, Huawei Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based data attribution has become an important tool for high-quality data selection in the instruction fine-tuning of large language models (LLMs), as it estimates the contribution of training examples through their influence on model optimization. However, we find that existing global gradient attribution methods suffer from surface-form bias: minor changes to semantically irrelevant details, such as wording or formatting, can produce highly inconsistent attribution scores even when the underlying content remains unchanged. To address this issue, we propose Content-Invariant Gradient Attribution (CIGA), a robust framework for instruction data selection. CIGA first identifies layers whose gradients are both influential for attribution and stable under semantics-preserving surface-form perturbations, thereby reducing formatting noise in gradient features. It then dynamically fuses these attribution signals with semantic representations of the input, combining optimization-level influence with content-level information. Extensive experiments across multiple benchmarks show that CIGA produces more stable rankings under surface-form perturbations while preserving downstream capabilities and improving average performance. CIGA also reduces attribution cost, offering a robust and efficient approach to data selection for LLM instruction tuning.

---


### 91. [DocSkill: Skill-Integrated Agentic Reasoning for Multilingual Multi-Hop Document Question Answering](https://arxiv.org/abs/2610.36759)

**<font color=#1a73e8>作者：</font>** Jing Huang, Zhiya Tan, Changtao Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual multi-hop document question answering (MMHop-DocQA) requires locating and integrating evidence across complex layouts, document pages, and diverse languages. Existing approaches include single-pass processing and adaptive tool use, but learning to coordinate evidence acquisition, cross-page integration, and answer verification remains challenging. To address this challenge, we present DocSkill, an agentic framework with a learned skill-orchestration policy for adaptive evidence acquisition and reasoning. The policy selects, revisits, or skips skills according to the evolving evidence state. To construct supervision for skill orchestration, bounded Monte Carlo Tree Search (MCTS) explores alternative skill trajectories offline. These trajectories provide demonstrations for supervised fine-tuning (SFT) and preference pairs for Direct Preference Optimization (DPO). We further introduce MMHop-DocBench, a multilingual multi-hop document QA dataset with training and test splits, containing 60K QA pairs across 10 languages and eight document domains. Its HopGen pipeline builds hierarchical page-element graphs to derive traceable cross-page evidence paths and generate grounded QA pairs with page- and element-level evidence annotations. Experiments show that DocSkill with Qwen3-VL-8B achieves 41.0 accuracy and 49.2 F1 on MMHop-DocBench, exceeding the strongest evaluated baseline by 5.5 and 6.3 points, respectively, and achieving competitive performance on MMLongBench-Doc and DocBench.

---


### 92. [Beyond the Evidence Coherence Trap: Agent-Driven Evidence Selection for Temporally Disordered Fake News Detection](https://arxiv.org/abs/2610.36764)

**<font color=#1a73e8>作者：</font>** Chi Wang, Min Gao, Yifei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fake news undermines public trust and the integrity of online information ecosystems. Temporally disordered fake news is especially elusive because it rearranges factual events into a false chronology. Individual events may remain factually valid even when their temporal relations are misrepresented. When similar events involving the same entity recur, retrieval may return semantically plausible evidence from the wrong period. Consequently, independent event verification may rely on locally coherent but temporally mismatched evidence and incorrectly validate the article. We call this the \textit{evidence coherence trap}. Because existing benchmarks rarely isolate this setting, we construct ChronoFake, a source-disjoint benchmark of 30,706 articles derived from temporally anchored real events. It distinguishes temporal manipulation from valid narration, including flashbacks. To address this, we propose DelSA, a \underline{D}ocument S\underline{el}ection \underline{S}elf-Updating \underline{A}gent that iteratively refines evidence selection during training and applies a frozen rulebook for one-pass evidence selection at inference. DelSA uses an LLM to characterize candidate evidence, while a verifier-trained reranker balances local relevance against timeline consistency. Finally, the classifier compares the article-implied chronology extracted by the LLM with the evidence-derived chronology to reveal global temporal conflicts. DelSA outperforms existing methods on ChronoFake, while remaining competitive on PolitiFact and GossipCop.

---


### 93. [Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs](https://arxiv.org/abs/2610.36767)

**<font color=#1a73e8>作者：</font>** Azim Ospanov, Zijin Feng, Ding Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have made remarkable progress on solving competition-level mathematics, yet their ability to verify natural-language mathematical proofs remains relatively underexplored. This gap is especially pronounced for Olympiad-level proofs, which require meticulous assessment of each claim in a long reasoning chain. Current proof verification thus primarily relies on expert inspection, which is costly to scale. In this paper, we present a systematic study of LLM-based verification in this setting. Specifically, we introduce a human-curated dataset of USAMO 2025 candidate solutions with expert grading, and conduct a broad evaluation of existing LLM verifiers across frontier models. We also propose TROJAN, an iterative self-critique pipeline for generating high-fidelity adversarial proofs at scale. Our comprehensive evaluation covers 20 models spanning seven metrics, two prompt styles, three inference methods, and three prompt templates, showing that state-of-the-art models still leave considerable room for improvement. To narrow this gap, we propose MABGrader, a Multi-Armed Bandit framework that reframes grading as arm selection over the discrete score space. MABGrader outperforms the SOTA ProofGrader by 26.4% in Quadratic Weighted Kappa and reduces grading error by 14%. Code and dataset are available at this https URL.

---


### 94. [Dependency Graphs of Mathematical Arguments: Representation, Structural Measurement, and Proof Review](https://arxiv.org/abs/2610.36776)

**<font color=#1a73e8>作者：</font>** Eunji Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a source-grounded framework for representing and measuring mathematical arguments with assistance from large language models. It includes numbered and unnumbered statements, equations, assumptions, and constructions, distinguishing source occurrences from contextual states and inference records. Proposed dependencies retain source evidence and review status. A measurement contract fixes manuscript versions, boundaries, granularity, proof choices, and macro anchors. On a selected finite directed acyclic graph, depth is the longest prerequisite-path length, and bulk counts distinct ancestor edges. We give a union recurrence that accounts for shared subarguments and identify reachability conditions preserving depth and the macro skeleton; unrestricted refinement need not preserve depth or bulk. A standardized, versioned prompt protocol separates annotation discovery, deterministic recomputation, and review assistance. Cross-paper links support a research agenda on theorem co-use, rare combinations, and connections between dependency communities. These patterns motivate probabilistic premise suggestions and review of possible omissions or unchecked application conditions in human-written and AI-generated proofs. Further applications include source-linked reading support and comparison of individual and collaborative argument shapes. We provide an evaluation design rather than empirical evidence of these benefits. Suggested premises require mathematical validation, and the measures describe a specified representation rather than intrinsic mathematical difficulty, originality, or importance.

---


### 95. [Does LLM Pre-Training Typically Occur at the Edge of Stability?](https://arxiv.org/abs/2610.36778)

**<font color=#1a73e8>作者：</font>** Yuhang Cai, Haodong Wen, Haofeng Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quadratic approximations provide a common lens for studying neural network optimization, but recent evidence challenges their predictive validity. In full-batch gradient descent with learning rate (LR) $\eta$, Cohen et al. (2021) observed the Edge of Stability (EoS), where the largest Hessian eigenvalue concentrates near $2/\eta$, seemingly at odds with classical stability conditions predicted by quadratic approximations. In this work, we revisit the fidelity of quadratic approximations as a model of neural network training dynamics, with a particular focus on their failure modes in LLM training. We first highlight a distinct failure mode of the quadratic approximation, where persistent negative curvature causes the quadratic dynamics to diverge regardless of the LR, even though the real dynamics remain stable. We term this phenomenon the Edge of Convexity (EoC). After removing the effect of this LR-independent instability, we then propose a generalized definition of Edge of Stability (EoS) for stochastic training with adaptive optimizers, based on whether increasing the LR induces significant divergence in the quadratic dynamics while leaving the real dynamics largely unchanged. Across different LLM pretraining runs with various model sizes up to 787M, we find that (1) EoC is always observed across LLM pretraining, and (2) EoS is also prevalent but not universal: it disappears when the LR becomes sufficiently small (e.g., after decay) or when the batch size falls below a critical threshold that has a positive correlation with the critical batch size. Together, these findings characterize when and how quadratic approximations fail and provide a foundation for future work on understanding training dynamics.

---


### 96. [Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training](https://arxiv.org/abs/2610.36794)

**<font color=#1a73e8>作者：</font>** Yue Wu, Yang Zhang, Weinan Gan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) enables a deployed language model to internalize incoming context on-the-fly into a small set of fast-weight parameters, rather than merely treating it as transient context for attention. In-Place TTT recently made this idea practical for large language models by repurposing the down-projection of standard MLP blocks as fast weights. However, we find that its benefit largely disappears on realistic web long-context question answering. We attribute this to In-Place TTT's uniform write schedule: every chunk is written with equal strength, so irrelevant content dilutes query-relevant information in fast-weight memory. Building on this insight, we propose Select-TTT, a model-agnostic, query-conditioned rule for In-Place TTT that scales each chunk's write strength by its relevance to the user query. This relevance signal requires no supervision and no new parameters: it is read directly from the model's frozen output head, as the probability mass that a chunk's hidden states assign to the query tokens. A temperature-scaled softmax turns these scores into learning-rate multipliers, leaving the chunk-wise, context-parallel computation of In-Place TTT intact. Select-TTT consistently improves long-context question answering on two benchmarks and two backbones. These findings highlight the value of query-conditioned fast weight writes for practical test-time training on long-context question answering, which is also potentially promising for long-horizon agent tasks involving multiple user queries over evolving contexts.

---


### 97. [Language Models Keep Abandoned Analyses: Residue and Adaptation after Garden-Path Sentences](https://arxiv.org/abs/2610.36797)

**<font color=#1a73e8>作者：</font>** Xiang Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reading "While the man hunted the deer ran into the woods" requires giving up the analysis in which "the deer" is the object of "hunted". People who have just read such a sentence still produce more transitive structures, so the abandoned analysis primes later language. We ask whether language models keep using an analysis they have abandoned, and what in the model carries it. In 24 open models from 124M to 70B parameters, a garden-path sentence leaves two traces in the context. A residue of the abandoned analysis raises later object attachment, by about three quarters of the effect of a sentence in which the noun phrase really is an object, and it appears in sampled text, on held-out and human-normed items and for a second type of garden path. An adaptation toward the resolved structure scales with the sentence's disambiguation error and acts mainly on comprehension-like measures. Activation patching separates the two. Later text reads the residue from the role information in the noun phrase's states, which were computed under the object analysis before the disambiguation, and replacing these states removes almost all of the residue in the 32B and 70B models. The adaptation is read from the states that processed the disambiguation. Overridden statements show the same persistence (a corrected value keeps pulling later predictions in 8 of 9 models), and in most models the pull is carried by the positions after the statement. Finally, the human paradigm transfers only with controls for punctuation, because the models also write garden-path sentences themselves, which reverses the paradigm's raw statistic.

---


### 98. [API-TAIL: Detecting Model Substitution in LLM APIs through Temperature-Aligned Likelihood Tails](https://arxiv.org/abs/2610.36801)

**<font color=#1a73e8>作者：</font>** Haocheng Mei, Yuchuan Tian, Ye Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Commercial language model APIs return only text, allowing a provider to cut costs by quietly routing a fraction of user requests to a cheaper substitute model while billing for the advertised one. Detecting such partial substitution is challenging because honest providers also alter the output distribution through undocumented decoding and serving choices, such as temperature scaling, sampling truncation, repetition and presence penalties, and default system prompts, forcing an audit to test against a composite null of legitimate configurations rather than a single reference. Our key insight is that these legitimate variations primarily shift response typicality across the entire batch, whereas partial substitution injects individual responses that remain anomalous under the claimed model. Building on this, we introduce API-TAIL, a typicality audit that first absorbs batch-level shifts by aligning a single effective temperature to center standardized surprisal scores across the audited batch, and then flags the endpoint if the number of remaining tail responses exceeds a threshold calibrated across legitimate configurations. Evaluated on real-world commercial APIs, API-TAIL reliably controls false alarms across diverse honest providers while detecting even low-rate partial substitution with a small query budget, substantially outperforming existing rank- and MMD-based audits that lose detection power under the same composite calibration.

---


### 99. [Personality Latents: Conditioning Frozen Language Models on Individuals from Their Own Writing](https://arxiv.org/abs/2610.36805)

**<font color=#1a73e8>作者：</font>** Gunhee Cho, Yun-Gyung Cheong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Controlling the personality of a language model usually relies on written profiles or named trait categories, so it can only express what an author writes down or what a taxonomy names. We instead propose Personality Latents (PL), which learn a latent for each person from their own writing, with no personality labels and no authored profile, and inject it into a frozen language model as a soft prefix. Following generative latent optimization, each training person receives a free latent that is optimized through the frozen model itself, while an encoder learns to predict these latents so that a new person needs only one forward pass, with optional refinement at test time. We evaluate on held-out people by having the conditioned model answer neutral and interview questions and reading personality from its answers with scorers trained on real human writing. On the MBTI axes PL reaches an AUC of , ahead of persona embedding and prompt-based baselines under identical settings, and the ranking holds when the answers are scored in three different embedding spaces. A latent learned with Qwen2.5-3B-Instruct also transfers personality to Llama-3.1-8B-Instruct through a new adapter alone.

---


### 100. [LLM knowledge for improved Out-of-Distribution Tabular Prediction - A Cross-Validated Regularisation Approach](https://arxiv.org/abs/2610.36806)

**<font color=#1a73e8>作者：</font>** Sølve Langseth, Kristoffer Herland Hellton, Hugo L. Hammer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prediction models degrade when the deployment population differs from the one used to train them, and training data cannot say which feature-response relationships will transfer. Expert elicitation is slow and unscalable. We ask whether coefficient priors elicited from large language models (LLMs) improve out-of-distribution (OOD) prediction as the shrinkage target of a regularised regression instead of zero, across five tabular datasets split on real covariates, selecting providers and prior structures by source-domain cross-validation alone. The priors help on four of five datasets, by up to 7.9% OOD mean squared error, and ten of twenty-four prior-informed results resolve the mean improvement at conventional confidence; single-deployment intervals are much wider. On classification the gain is in probabilistic accuracy, not ranking, and control tests with corrupted priors attribute the benefit to feature-specific content rather than scale. Two findings temper this. Variation across candidate priors exceeds the average benefit, yet cross-validation margins fall below their own noise, so selection avoids the worst prior rather than finding the best. On three datasets the prior improves in-domain accuracy as much as out-of-domain, making it better regularisation than shift correction. Only where the training data are large enough that the in-domain gain disappears does elicited knowledge demonstrably improve transfer. Code, priors and results: this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-226](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
