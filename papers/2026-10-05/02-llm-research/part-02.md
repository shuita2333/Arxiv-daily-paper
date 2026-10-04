# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

---

### 51. [UnifiedAttack: Evaluating the Safety of Large Multimodal Models in Synergistic Harmful Image-Text Generation](https://arxiv.org/abs/2610.00341)

**<font color=#1a73e8>作者：</font>** Bingjun Luo, Jialin Guo, Tony Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Multimodal Models (LMMs) transition toward natively unified architectures, evaluating their safety in synergistic harmful image-text generation tasks becomes a critical challenge. Unlike unimodal threats, synergistic risks emerge when text and image modalities are coordinated to produce harm that significantly exceeds their individual components. We introduce UnifiedAttack, a novel benchmark designed to evaluate LMM safety in collaborative scenarios by focusing on the harmfulness gain achieved through cross-modal synergy. The benchmark incorporates samples filtered for their multimodal potential alongside a novel subset of synthesized disinformation queries. To verify identified vulnerabilities, we propose a synergistic hijacking framework featuring In-Context Reskinning (ICR) and Cognitive Planning Injection (CPI). ICR utilizes few-shot learning to wrap adversarial intent in benign virtual shells to desensitize safety filters, while CPI hijacks the reasoning path by enforcing a plan-then-execute paradigm. By compelling the system to commit to a neutral logical plan, we exploit its internal drive for consistency to induce the synchronized generation of harmful multimodal content. Extensive evaluations on state-of-the-art architectures demonstrate that UnifiedAttack consistently bypasses modern alignment. Our findings reveal that the structural helpfulness and logical coherence of unified models can be systematically weaponized, highlighting the urgent need for logic-aware defenses in synergistic generation tasks. Code is available at this https URL .

---


### 52. [Benchmarking System One decision models against trained classifiers and language models for automated decision gates](https://arxiv.org/abs/2610.00346)

**<font color=#1a73e8>作者：</font>** Amir Rafe, Subasish Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Software that hands branching decisions to a model needs a declared option and a probability it can threshold. Typed decision models, also called System One models, return such probabilities without generating text, while supervised classifiers and generative language models are the established alternatives. Under matched conditions, one harness sends eight decision-model checkpoints from six families, including the hosted model Jev, and two generative comparators the same semantic requests, and scores supervised and zero-shot classifiers on the same workflow, intent and social-science items. The ranking of the model classes depends on the conditions. With the task's own labels, small trained classifiers are the most accurate on intents and not significantly different from the best decision models on workflows. Without labels, every decision model except the encoder-based checkpoints exceeds a zero-shot entailment classifier on workflows and intents. Read through option-key likelihoods, a larger generative model is level with Jev on workflows and intents and accepts more workflow decisions at five percent risk, and fine-tuned decision checkpoints gain intent accuracy over their untuned backbones. Stored temperatures fitted on few options raise calibration error with many options, and a held-out threshold for five percent in-scope risk still lets Jev accept 0.310 of out-of-scope requests. Swapping yes and no flips 50.5 answers per hundred for Jev, while fine-tuned checkpoints cut their backbones' social-science flips. An intent-trained first stage escalating to Jev matches its accuracy at 0.43 of its cost at full graphics-processor utilization. The results yield condition-dependent design rules for automated decision gates.

---


### 53. [Proof-Gated Signing: Solver-Checked Transaction Guards that Hold Under State Drift for Onchain AI Agents](https://arxiv.org/abs/2610.00354)

**<font color=#1a73e8>作者：</font>** Bravish Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents that control wallets read attacker-reachable content, so they can be steered into proposing harmful transactions. The usual last line of defense is a pre-signing check: a static allowlist, an LLM reviewer, or a transaction simulation. All three share a gap: the check describes the chain state at check time, but the transaction executes in a later state that an adversary can shape through front-running, contract upgrades or token-parameter changes. We call this state drift. We present Proof-Gated Signing (PGS), which simulates a proposed transaction, extracts its effects, and uses an SMT solver to check a declarative value-and-permission policy for every price in an oracle-uncertainty band. It then compiles on-chain post-conditions (wallet balance bounds, payee receipts, allowance caps and ownership) and proves that every execution satisfying them also satisfies the policy. The agent's smart-contract wallet enforces them atomically, so the guarantee applies to the executed transaction under arbitrary drift. On an open testbed of 260 scenarios (14 attack families including five drift and two adaptive families, and 12 benign families), with harm measured from attacker balances rather than from any policy, PGS prevented 93.6% of the 140 harmful scenarios and passed 97.5% of the benign ones. Simulation-only checking prevented 57.9% and a static allowlist 71.4%. None of the 50 drift scenarios produced attacker gain under PGS. The only unprevented family, an in-policy drain, was bounded by the per-session budget. We also find that giving an LLM reviewer a clean pre-drift simulation made it more likely to approve a drift attack. Overhead is about 41k gas and 0.1-0.2 s per check.

---


### 54. [MoRA: MoE Pruning via Router Bias Learning and Expert Approximation](https://arxiv.org/abs/2610.00367)

**<font color=#1a73e8>作者：</font>** Yushuai Sun, Zikun Zhou, Lin Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models enable parameter scaling with limited per-token computation by activating only a small subset of experts for each token, but deploying them still requires loading the complete expert pool into memory. Structured expert pruning can effectively reduce the memory usage by removing experts. However, existing pruning methods either use expert ranking criteria that are not well aligned with model performance or rely on effective expert subset searching that is computationally expensive. Moreover, these methods typically overlook the routing-behavior redundancy among the retained experts. In this paper, we propose MoE Pruning via Router Bias Learning and Expert Approximation (MoRA), a framework for structured MoE expert pruning. We introduce a learnable router bias for each expert and optimize these biases by minimizing the language-modeling loss and a routing-diversity regularizer. The learned router biases sharpen the routing probability distributions to identify experts critical to model performance while encouraging the selection of experts with diverse routing preferences. In addition, we introduce an expert approximation mechanism as a post-pruning enhancement. It leverages the remaining experts to approximate the outputs of pruned experts by affine transformation, further improving the performance of the pruned model. We evaluate MoRA on Qwen3-30B-A3B, DeepSeek-V2-Lite, and Moonlight-16B-A3B, removing 25\% and 50\% of the routed experts in each MoE layer. Extensive experiments on nine zero-shot benchmarks show that MoRA outperforms state-of-the-art pruning algorithms. Our code will be released.

---


### 55. [When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents](https://arxiv.org/abs/2610.00372)

**<font color=#1a73e8>作者：</font>** Shuyao Xiao, Shengling Wang, Xuan Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents rely on external harnesses to pass information between the model and its environment and to recover from execution errors. Yet recovery is usually judged only by average task success. This hides an important tension. The same operation can rescue a failing trajectory or disrupt one that would otherwise succeed. We frame recovery as a causal decision problem. Starting from the same execution state, we compare what happens with and without recovery, separate rescue from harm, and study how the value of recovery changes over time. We then introduce the Causal Intervention Router (CIR), a lightweight policy that uses information available before recovery to decide when intervention is worthwhile. On long-horizon ALFWorld tasks with Qwen3-14B, CIR raises success from 70.33% to 73.33%, a gain of 3.00 percentage points. It leaves all evaluated trajectories with correct observations untouched. Additional controls show that the benefit of recovery cannot be explained solely by the new observation returned by the environment. These results provide a practical way to evaluate recovery and apply it selectively.

---


### 56. [When Do Attention-Head Ablations Support Causal Claims? Projection-Level Confounds, Floor Effects, and Matched Controls](https://arxiv.org/abs/2610.00373)

**<font color=#1a73e8>作者：</font>** Juli Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention-head ablation, zeroing a head and measuring the resulting change in task performance, is a common method for inferring which components of a language model are causally responsible for a behavior. We show using GPT-2 small that this inference can be fragile unless the intervention semantics, evaluation metric, and controls are carefully validated. A natural post-projection implementation of "zeroing a head" is nearly uncorrelated with a corrected pre-projection ablation (Pearson r = 0.057) and selects a completely disjoint top-5 set of important heads. We also show that binary accuracy can hide effects at behavioral floors and near ceilings, whereas gold-token log-probability remains graded. Using a discovery/held-out split and 1,000 matched random-head and layer-matched-head control draws, the corrected per-head effect ranking is highly stable across splits (Spearman rho = 0.974), and the top-5 selected heads significantly exceed both control distributions (Monte Carlo p = 0.001). However, evidence for task specificity is not robust on GPT-2. Replication on DistilGPT2 preserves the intervention-semantic and matched-control findings. These results show that single-head ablation does not by itself justify a causal claim; defensible interpretation requires correct intervention placement, a non-saturated continuous metric, and matched held-out controls.

---


### 57. [A First Glance at Jev for Network Traffic Classification: Accuracy, Processing Time, and Cost](https://arxiv.org/abs/2610.00376)

**<font color=#1a73e8>作者：</font>** Shenghe Xu, Lifan Mei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate Jev on ten dataset-defined application labels in CESNET-QUICEXT-25 using only the first ten packets' sizes, directions, and inter-packet times. To the best of our knowledge, this is the first empirical study of general-purpose decision models, represented here by Jev, for application classification of network flows. Across 52,000 records from 26 collection weeks following the training period, 40 fixed labeled examples raise Jev's accuracy from 9.80% to 28.42%. Random Forest and Extra Trees trained on 8,000 records achieve 69.95% and 66.80% and outperform Jev in every week. Increasing Jev's context to 150 examples yields 34.50% on the first test week. On a paired 100-record subset, Jev with 40 examples achieves 29% accuracy at a median request time of 0.750 s, versus 37% and 6.036 s for the generative language model OpenAI GPT-5.6 Sol with high reasoning effort through Azure; Jev also incurs lower API charges. The paired subset does not establish an accuracy advantage for either service, and the timing reflects different service configurations. Thus, labeled examples substantially improve Jev, but the tested Jev configurations remain less accurate than trained tree ensembles; unequal supervision budgets and fixed configurations prevent attributing the gap to a single cause.

---


### 58. [OmniMed-Jev: Calibrating LVLM Confidence for Trustworthy Medical Multimodal Decisions via System One](https://arxiv.org/abs/2610.00381)

**<font color=#1a73e8>作者：</font>** Luyao Tang, Cheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical models are judged not only on correctness, but on whether reported confidence matches actual accuracy. Generalist multimodal medical models have expanded what a single model can perceive, yet they still express bounded decisions such as diagnoses, findings or cell counts as generated text, so the reported probability reflects the next token rather than the decision itself. Motivated by decision-native interfaces such as Jev, we introduce OmniMed-Jev, which represents each medical decision as a Choice, Noul or Score decision over a runtime-supplied candidate set and returns a full distribution over that set: mutually exclusive classes, binary presence of a finding, or a bounded ordered value. The design is omni in three respects: it accepts diverse imaging modalities, covers different prediction tasks, and expresses them through one candidate-conditioned probability model, so heterogeneous outputs become comparable probabilities rather than task-specific strings. In an interface-controlled comparison against a generative baseline trained on the same backbone, data and schedule, OmniMed-Jev's reported probabilities track observed correctness far more closely, reducing calibration error by up to an order of magnitude and reliability error by up to two, while point-prediction performance remains comparable; counting is the one family where the generative baseline stays ahead. Making the decision distribution the model's output is not a format change but what turns reported numbers into probabilities that mean what they say. These results support explicit decision modeling as a way to make reported confidence meaningful within the evaluated tasks, and they are not evidence of clinical readiness: the comparison cannot separate the interface from associated training differences, which we state alongside the results. Code is available at this http URL.

---


### 59. [FAER: Auditable Utility-Aligned Trajectory Replay for Language Model Post-Training](https://arxiv.org/abs/2610.00385)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Replay selectors often rank cached trajectories by format feedback, confidence, freshness, or response length, although cache-level correctness and downstream learner utility are distinct objectives. We formalize this selection-to-learning gap and introduce FAER as an auditable full-trajectory replay framework. Its training-free fixed selector is a protocol baseline; FAER-UTILITY is the learner-aware selector fitted on disjoint calibration blocks. The normalized gradient alignment is reported as a baseline, while a disposable optimizer-aware virtual update supplies a magnitude-aware utility surface. The audit contract freezes observed fields and replay traces before evaluation labels are joined. On GSM8K with Qwen2.5-1.5B-Instruct, the matched learner study reports quality 0.6329 for the fixed selector, compared with 0.5482 for uniform and 0.6037 for format-feedback under 128 updates. Metadata-only cross-fitted calibration reaches $0.6476\!\pm\!0.0139$ over eight seeds (median 0.6481; paired 95% interval $[+0.079,+0.122]$) at 63,276 target-run tokens; its recorded full cost is 189,642 tokens and 3.48 GPU-hours including calibration. The completed FAER-UTILITY row reaches 0.6624 at 62,844 target-run tokens and 4.26 GPU-hours. Format-feedback selects records with correctness 0.6953, compared with 0.3594 for the fixed selector, despite the different downstream ranking. The completed comparison surfaces report the learner-aware ablation, same-seed gap, policy-optimization rows, and strict zero-shot transfer.

---


### 60. [T2SPO: Trajectory-to-Step Policy Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.00388)

**<font color=#1a73e8>作者：</font>** Bo-Wen Zhang, Junwei He, Maoqi Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning enables large language model (LLM) agents to learn multi-step behaviors through interaction with their environments. However, rewards in many interactive tasks reflect only the final outcome, providing limited guidance on which intermediate decisions advance the task. Successful training trajectories contain intermediate states that can provide supervision for subsequent interactions. We introduce Trajectory-to-Step Policy Optimization (T2SPO), a method that uses past interaction trajectories to provide step-level feedback for policy learning. T2SPO derives remaining-distance targets from successful trajectories and pairs them with representations of the states visited along the way. Conditioned on these examples, a pretrained TabPFN regressor estimates the remaining distance to success at each state of a new rollout. Changes in this distance estimate across consecutive states yield auxiliary credit for agent steps alongside task-level supervision. As training proceeds, newly completed trajectories refresh the estimator's context, incorporating new experience without updating its parameters. Experiments with 1.5B and 7B language models on ALFWorld and WebShop show that T2SPO consistently improves overall task success over GRPO.

---


### 61. [MatrixReward: Reward from Rubric Matrix for Open-Ended Generation](https://arxiv.org/abs/2610.00389)

**<font color=#1a73e8>作者：</font>** Zihan Shen, Qi Liu, Zixuan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-ended query generation lacks standard answers, thus necessitating an effective reward mechanism. Pointwise scoring rubrics provide limited information about the relative quality of sample answers under the same prompt; merging multiple rubric judgments into a single score may also mask the differences between these answers. We propose MatrixReward, which constructs rewards from a rollout-by-rubric win-rate matrix obtained by comparing every pair of sampled responses under each rubric. The spread of each matrix column captures how strongly that rubric distinguishes the current rollouts, while correlations between columns reveal rubric repetition; together, these statistics yield data-dependent rubric weights. We combine these weights with the prior weights of rubrics. After column normalization and weighting, the observed per-rubric maxima and minima define positive and negative ideal profiles. Each rollout's distances to these two ideals determine its relative-closeness quality reward. Evaluated using Qwen3-8B on four open-ended query-answering benchmarks, MatrixReward achieves an average score of 63.02, outperforming the strongest baseline by approximately 2.0%. These results support the idea that matrices derived from relative comparisons can be used to construct rewards more reasonably for open-ended generative reinforcement learning.

---


### 62. [Forking: Sudden Overfitting Under Replay](https://arxiv.org/abs/2610.00394)

**<font color=#1a73e8>作者：</font>** Shanbin Yu, Shaoyang Guo, Haoran Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies forking, a generalization failure discovered in NanoGPT autoresearch. Under data replay, models with an over-encoding n-gram memory branch show a sharp separation of training and validation loss at epoch boundaries, resembling the shape of forks. We study this phenomenon in a controlled vanilla NanoGPT setting and reproduce it in a DeepSeek-style model with Engram. Mechanistically, repeated updates sharpen the continuations observed in training while suppressing the probability of unseen continuations, whose loss grows with each pass. The n-gram module creates weakly interacting context-specific subspaces, amplifying this effect. Low-frequency contexts contribute most of the gap, whereas larger training budgets and heavily crowded tables suppress it. We also observe forking in short-budget, heavily repeated SFT and RL-like regimes. The contributions of this paper are twofold: (1) Forking reveals yet another curious phenomenon in deep learning, in addition to grokking and double descent. (2) Forking is an unexpected and unpleasant by-product of tricks proposed by autoresearch agents. While these agents produce an enormous number of results that seem useful, we should always be careful with their results.

---


### 63. [Metacognitive Reasoning in Energy Based Models using Instance Based Learning Theory](https://arxiv.org/abs/2610.00399)

**<font color=#1a73e8>作者：</font>** Tailia Malloy, Prateek Kumar Rajput, Serge Lionel Nikiema 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Metacognition involves reasoning about cognitive processes themselves. An example is in resource allocation where we choose how much time and effort to put into a reasoning task before we begin based on our confidence. Current Artificial Intelligence (AI) systems that rely on Large Language Models (LLMs) cannot estimate their uncertainty about an output without first responding, and cannot dynamically allocate resources to producing an output, making this type of metacognitive process difficult. A recently proposed alternative to classic transformer architectures that addresses these two concerns is the Energy Based Model (EBM) which allows for interpretable uncertainty modeling and dynamic allocation of compute resources. While EBMs can allow for control of these two processes, the actual metacognitive task of determining compute allocation based on uncertainty is not directly addressed. Instance-Based Learning Theory (IBLT) provides an approach to modeling human-like decisions from experience that has previously been applied to predicting human metacognitive reasoning. In this paper we introduce a framework for MEtacognitive Reasoning with Instance-based Learning Theory and Energy Dynamics (MERITED). Grounded in IBLT, this framework allows for control of the computational effort allocated in an EBM to allow for metacognitive control over reasoning effort based on uncertainty while remaining computationally efficient. This work has two main contributions, the training and open weight sharing of a 191M parameter reasoning EBM, and an implementation of the MERITED framework for dynamic compute allocation using an IBL model.

---


### 64. [Representation Transitions Reveal Emerging Safety Risks in Multi-Turn LLM Agents](https://arxiv.org/abs/2610.00400)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Wei Zhao, Yedi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn attacks on agentic systems can compose individually permissible actions into harmful outcomes, challenging defenses that assess actions or states in isolation. We show that such attacks leave a detectable signature in the agent's internal representations: harmful behavior emerges as an accumulated representation transition across context updates, whose triggering context can be identified from the same signal. We further find that naive aggregation is confounded by benign representation drift, as a contrastive safety direction need not assign zero to benign transitions. We address this by denoising the direction, anchoring benign traffic at zero and removing its leading variation directions, with no runtime cost.
These findings motivate DART, a runtime framework that detects and attributes representation shifts and intervenes with targeted reminders. Across six models and two multi-turn benchmarks, DART reduces attack success from 84% to 25% on MT-AgentRisk, catching every attack at a mean false-alarm rate of 12%, and from 97% to 52% on ASEval, at costs in benign non-refusal of 8% and 0%, respectively. On MT-AgentRisk, it outperforms ToolShield, the state-of-the-art multi-turn defense, on all six models: under the same protocol, ToolShield reaches only 55%. Denoising is critical: on ASEval, the undenoised monitor catches only 7%-40% of attacks, while the denoised monitor catches 60%-85%. The same monitor covers single-turn indirect injection without modification and adds only 0.14-0.56 s overhead per monitored step without requiring an auxiliary model, making it a lightweight complement to computation-heavy speculative defenses.

---


### 65. [LLM-as-a-Judge for Low-Resource Languages: Adapting Ragas and Comparative Ranking for Romanian](https://arxiv.org/abs/2610.00406)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Liviu P. Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating Retrieval-Augmented Generation (RAG) systems remains a challenge for Low-Resource Languages (LRLs), where standard reference-based metrics fall short. This paper investigates the viability of the "LLM-as-a-Judge" paradigm for Romanian by adapting the Ragas framework using next-generation models (Gemini 2.5 and Gemini 3). We introduce AdminRo-Eval, a curated dataset of Romanian administrative documents annotated by native speakers, to serve as a ground truth for benchmarking automated evaluators. We compare three evaluation methodologies - direct scoring, comparative ranking, and granular decomposition - across metrics for Faithfulness, Answer Relevance, and Context Relevance. Our findings reveal that evaluation strategies must be metric-specific: granular decomposition achieves the highest human alignment for Faithfulness (96% with Gemini 2.5 Pro), while comparative ranking outperforms in Answer Relevance (90%). Furthermore, we demonstrate that while lightweight models struggle with complex reasoning in LRLs, the Gemini 2.5 Pro architecture establishes a robust, transferable baseline for automated Romanian RAG evaluation.

---


### 66. [EchoPress: Query-Agnostic KV Cache Pruning via Virtual Context Reconstruction](https://arxiv.org/abs/2610.00412)

**<font color=#1a73e8>作者：</font>** Jiawei Lin, Saibo Geng, Thomas Bourgeat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache pruning reduces long-context inference memory usage by evicting less important key-value pairs. KVzip estimates importance through context reconstruction: prompting a model to repeat the context chunk by chunk. This achieves strong compression quality at the cost of additional forward passes. Learned approximations reduce this cost but require model-specific training. We analyze how KVzip identifies important cached information and show how to approximate its reconstruction scores using information already computed during prefill. These findings motivate EchoPress, a training-free method that approximates reconstruction attention using queries and keys from standard prefill. For each request, it reconstructs only the first chunk to calibrate importance scores for the remaining context. Experiments on LongBench and RULER with Qwen3-8B and Llama-3.1-8B-Instruct show that EchoPress matches KVzip in task accuracy across eviction ratios from 50% to 90%, while reducing compression overhead by a factor of 1.7-19.6 and total prefill time by a factor of up to 2.9. Code is available at this https URL.

---


### 67. [Benchmarking Prompt Optimization of Large Language Models With Chess](https://arxiv.org/abs/2610.00416)

**<font color=#1a73e8>作者：</font>** Timothée Lesort, Alejandra López de Aberasturi Gómez, Tristan Karch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models becomes increasingly challenging as their capabilities advance: benchmarks can saturate, public test sets risk contamination, and assessing harder tasks can require expensive grading or execution infrastructure. These challenges are amplified in automatic prompt optimization (APO), where evaluation is repeated throughout the search for better prompts. Studying APO therefore requires a benchmark that is cheap and deterministic to score, hard enough to leave room for improvement, and renewable as models evolve. We introduce a chess benchmark built from 1,118 Lichess puzzles to study APO for frozen LLMs: we optimize their prompts without updating their model weights. Chess combines inexpensive exact-match scoring, engine-based evaluation of alternative moves, and a renewable supply of problems with adjustable difficulty. Unlike evaluations that report only success on isolated test items, the benchmark also connects puzzle-solving gains to short game-play rollouts within the same domain. We use it to evaluate six APO algorithms on eight target models, measuring not only baseline strength but also how much each model responds to optimization and whether optimized prompts transfer across models and to game play. Chess is thus a well-suited benchmark for APO: it is (i) challenging, as even the strongest evaluated model, Gemini 3.5 Flash (used as the meta-model), solves only about 55\% of puzzles; (ii) discriminative, revealing gains, unchanged performance, and regressions across methods and models; (iii) renewable, with fresh puzzles to reduce contamination risk and adjustable difficulty to maintain headroom as models improve; and (iv) affordable, as the complete study runs for around \$800. We release the puzzles, optimization and evaluation code, and dataset-renewal scripts (this https URL).

---


### 68. [CommunityKV: Efficient Long-Context Decoding via Graph Partitioning](https://arxiv.org/abs/2610.00418)

**<font color=#1a73e8>作者：</font>** Joe McKenna, Anastasios Alexandridis, Nathan Susanj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling Transformers to long contexts is constrained by the quadratic cost of self-attention and the linear growth of key-value cache memory transfer. Sparse attention mitigates this by retrieving only relevant tokens, but current approaches either require large-scale training or, within the training-free regime, rely on semantically coarse heuristics or expensive clustering that is difficult to update efficiently during decoding. We introduce CommunityKV, a framework that formulates sparse attention as a community detection problem. CommunityKV constructs a token graph from the $QK^T$ scores already computed during standard prefill, and partitions the graph into communities to enable retrieval of semantically coherent token groups. A local update rule assigns newly generated tokens to communities in constant time, enabling sparse retrieval throughout streaming decoding without global re-partitioning. We evaluate CommunityKV on Qwen3 and Llama-3.1 models across three long-context benchmarks. With one graph per query head, CommunityKV delivers up to $1.25\times$ the end-to-end generation throughput of dense attention, while query-group graph aggregation yields up to $1.71\times$ with comparable accuracy.

---


### 69. [IrekoGPT: Turning Structured Pruning into Post-Hoc Slimmable LLMs](https://arxiv.org/abs/2610.00426)

**<font color=#1a73e8>作者：</font>** Pietro Moriello, Pietro Buzzega, Angelo Porrello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce IrekoGPT, a post-hoc method for converting pretrained LLMs into slimmable models whose width can be adjusted at inference time. Building on SliceGPT, we retain its projection matrices without pruning them, allowing a single model to expose nested subnetworks at different widths. We improve robustness by calibrating each layer across multiple compression ratios, and correct downstream linear layers through gradient-free ridge regression. Across Llama and Qwen models, preliminary results show improvements over naive PCA-based slimming, with the largest gains at high compression. Code is available at this https URL

---


### 70. [XOR-Trellis: Ultra-Low-Complexity Dequantization and Curvature-Aware Hadamard-Free LLM Quantization](https://arxiv.org/abs/2610.00432)

**<font color=#1a73e8>作者：</font>** Xiaofan Que, Nir Elkayam, Spandan Pyakurel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trellis-coded quantization enables high-dimensional compression of large language model (LLM) weights at ultra-low bit widths without the exponentially large codebooks required by conventional vector quantization. Practical deployment, however, presents two challenges: reconstructing compressed weights at sufficient parallel throughput to avoid making dequantization an inference bottleneck, and maintaining quantization accuracy without costly incoherence transformations. We address these challenges with two complementary techniques. First, we introduce an ultra-low-complexity trellis dequantizer that uses a structured, hardware-efficient state-to-value mapping while preserving diverse reconstruction choices for trellis search. Second, we reformulate discrete trellis path optimization with a curvature-aware objective that reflects model sensitivity directly in the original coordinate space. Together, these techniques enable high-quality ultra-low-bit trellis quantization with inexpensive, highly parallel runtime reconstruction and without relying on Hadamard-based incoherence processing.

---


### 71. [Every Batch Is Its Own Validation Set: Leave-One-Out Gradient Matching for Online Data Selection in LLM Fine-Tuning](https://arxiv.org/abs/2610.00436)

**<font color=#1a73e8>作者：</font>** Hongyu Chen, Xinyi Luo, Ming Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online batch selection fine-tunes a language model on the most useful part of each candidate batch. Selectors that match the gradient of the candidate batch are attractive because they need no held-out data, yet they rarely beat training on the whole batch. We show why. In-sample gradient matching uses every example as part of its own target, so its objective credits each example with its own gradient noise. This is the covariance penalty that makes training error optimistic, now sitting on the diagonal of the gradient Gram matrix: it steers selection toward the noisiest examples and makes the full batch the best solution the objective can reach. The fix costs nothing. For each example, the other candidates form an independent sample of the data distribution, so removing the diagonal turns the matching objective into an unbiased estimate of the update's error with respect to the population gradient. The minimizer of this leave-one-out objective weights examples by their gradient signal-to-noise ratio (SNR), and whenever per-example SNR is heterogeneous enough, half of a batch yields a lower-error update than the whole batch; we give the exact condition. We build \method{} on this principle. It computes the Gram matrix in the metric of the Adam preconditioner during the ordinary backward pass, selects a weighted subset greedily with a $(1-e^{-\gamma})$ guarantee, and uses no held-out data. Across four fine-tuning tasks and seven backbones from 1.5B to 8B parameters, LOOM improves on full-batch training by 2.3 and 2.4 points on Llama-3.1-8B and Qwen2.5-7B, exceeds every in-sample gradient matcher by 2.4 points and the validation-guided GREATS and OPUS by 1.6--2.0, and selects injected label noise at under a fifth of its base rate.

---


### 72. [JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces](https://arxiv.org/abs/2610.00437)

**<font color=#1a73e8>作者：</font>** Haoyang Su, Weiran Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents generate intermediate reasoning and actions token by token, making extended interactions slow and computationally expensive. Jev-style models offer fast probabilistic predictions over finite fields, but require those fields to be specified in advance. This requirement limits autonomous task solving, where the available actions must be derived from natural language instructions and adapted through interaction. We introduce JevSpawn, a compositional policy that connects natural language task specifications to finite probabilistic exploration. Parallel action spawning is coupled with feedback driven branch selection, representation revision, and recovery from retained alternatives. Shared action structure and model prefixes reduce repeated generation and context computation without additional training. Evaluations on eight benchmark tasks against seven agent baselines and a TypeSafe Jev variant establish JevSpawn as a promising approach to structured agentic inference, with improved task performance and faster navigation.

---


### 73. [ZoneClaw: Mitigating Persistent Memory Attacks by Establishing Memory-Zoning in OpenClaw-Style Computer-Use Agents](https://arxiv.org/abs/2610.00450)

**<font color=#1a73e8>作者：</font>** Haokai Ma, Chieh Lin, Yupeng Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents increasingly operate as long-running assistants through persistent workspace memory, which OpenClaw-style CUAs realize as automatically reloaded files that hold user instructions, system summaries, and external claims at the same privilege level. Here, remembering a claim confers authority over later behavior. This enables a persistent memory attack, in which an attacker who controls only benign-looking external content induces the CUA to record attacker-favored claims during a legitimate task, and those claims later govern benign tasks the attacker never touches. The attack chain extends "malicious context -> malicious response" into "malicious context -> memory injection -> malicious execution", making this a cross-environment threat. Existing defenses studied intervene either before content enters memory or at the action it later induces, not whether stored content may guide action. We propose ZoneClaw, which separates persistence from authority by replacing flat workspace memory with hierarchical trust zones carrying explicit authority levels. External claims persist in a low-trust zone and acquire action-guiding authority only by crossing an explicit authority boundary, at which promotion is cross-checked against zones the attacker cannot directly write. Role-specific processes of asymmetric privilege enforce this boundary, ensuring that no process both ingests external content and acts outward. Across four attack scenarios, two injection settings, and four backbones, ZoneClaw drives ASR from 372/480 to 6/480 while retaining utility in 458/480 trials, and remains effective against some defense-aware attackers. Attacker claims still persist in low-trust memory yet rarely cross the authority boundary, showing that ZoneClaw withholds authority rather than refusing to learn from the environment. Our code is available at: this https URL.

---


### 74. [Score the Update, Not the Token: Descent-Aligned Routing for Combinatorial LoRA Experts](https://arxiv.org/abs/2610.00493)

**<font color=#1a73e8>作者：</font>** Priya Nair, Lukas Brenner, Maya Lindqvist 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-LoRA-experts methods raise the capacity of low-rank adaptation by routing each token to a few low-rank experts. Nearly all of them tie one input-side factor to one output-side factor per expert, and nearly all of them route by scoring the token: the router picks experts without seeing what any of them would write. We argue that the router should score the update. To first order, adding an expert's update to a layer output lowers the loss by the inner product between that update and the negative loss gradient at the output. This usefulness is quadratic in the token, so a router that is linear in the token sees only the part of it that runs through the token mean, and routers that rank experts by the norm of their own activations never see the output factor. If each expert is split into a reader (down-projection) and a writer (up-projection), the usefulness of every reader--writer pair becomes an inner product in the shared rank-$r$ space, and all $N_AN_B$ pairs can be scored from $N_A+N_B$ vectors. We build VANE on this identity. A low-rank compass predicts the descent direction of each token. VANE scores every pair by the alignment between its update and the compass without forming any update, activates the top-$k$ pairs with additive gates, and gives every pair its exact first-order router gradient. On single-domain commonsense reasoning and a four-domain multi-task mixture with Llama-3.2-3B and Llama-3.1-8B, VANE attains the best average among twelve PEFT and MoE-LoRA baselines, by 0.9--1.1 and 1.3--1.5 points respectively, with less than half the trainable parameters of an 8-expert MoE-LoRA. Its router scores also track the measured usefulness of experts far more closely than token routers do.

---


### 75. [Gumbel Straight Flow: Distilling Autoregressive Models into One-step Flow Maps](https://arxiv.org/abs/2610.00497)

**<font color=#1a73e8>作者：</font>** Yeongmin Kim, Arnaud Doucet, Andrew Campbell 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Gumbel Straight Flow (GSF), a continuous flow map language model that leverages the noise-data coupling of a pretrained autoregressive language (AR) model. We theoretically demonstrate that the coupling between Gumbel noise and one-hot token sequences induced by an autoregressive model yields non-intersecting linear paths connecting the noise to the sequence representations. To further enhance high-quality few-step path sampling, we use a flow map semigroup objective where the tangent (velocity) condition is guided directly by the AR teacher. Across various benchmarks, including pretraining and downstream tasks, GSF can outperform current few-step language generation baselines.

---


### 76. [Denoising Surface: Modeling and Predicting Inference Cost for Diffusion LLM Serving](https://arxiv.org/abs/2610.00499)

**<font color=#1a73e8>作者：</font>** Haoyu Zheng, Fangcheng Fu, Binhang Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As diffusion large language models (dLLMs) become more capable, they are moving from research settings to real-world \textit{serving}, where request management (such as scheduling and resource allocation) relies on accurate estimation of per-request inference cost. However, common cost proxies fall short for dLLMs: output length ignores that one forward pass can unmask multiple tokens, and denoising-step count ignores the \textit{heterogeneous} per-step costs. We observe that the block-autoregressive generation mechanism induces a two-dimensional execution structure over output blocks and within-block denoising steps, whereas these proxies collapse it into a scalar, discarding information essential for characterizing the cost. Motivated by this insight, we propose the Denoising Workload Surface (DWS), which preserves this two-dimensional block-step structure as a probability surface to weight the heterogeneous per-step costs. We then design a coarse-to-fine training scheme that enables a lightweight prompt-only predictor to accurately predict the complex DWS. This predictor runs efficiently even on a single CPU core, avoiding GPU contention with the serving model. Since DWS decouples request-dependent execution behavior from deployment-specific cost factors, the predictor transfers across hardware configurations without retraining. In \textit{real-world} serving experiments, DWS reduces cost-prediction error by up to $2.50\times$ over scalar-based predictors, while the DWS-guided shortest-job-first scheduler reduces end-to-end latency by up to $1.92\times$ for online chatbots.

---


### 77. [Before Agents Decide: Epistemic Action in LLM-Based Systems](https://arxiv.org/abs/2610.00511)

**<font color=#1a73e8>作者：</font>** Yizhi Liu, Balaji Padmanabhan, Siva Viswanathan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before a difficult decision, people often act simply to understand the situation better. We turn an object to see another side, place alternatives next to each other, or change one condition and observe what happens. These actions may not complete the task, but they improve the evidence needed for the next choice. LLM-based agents can search and explore, yet agent design gives less attention to an earlier question: is the available evidence ready for the decision? Sometimes necessary evidence is missing. In other cases, the evidence is present but its form hides what matters, or the comparison needed to judge it does not yet exist. Cognitive science calls actions that improve the basis for a later choice epistemic actions. We bring this idea to LLM-based agents and distinguish three modes: acquiring missing evidence, transforming available evidence, and probing a system to create a revealing response. We use the term epistemic scaffolding for the interfaces, tools, and environments that make these actions possible and auditable. This paper argues that agent design must address how decision-ready evidence is produced.

---


### 78. [Rules Amortize, Pairings Don't: Linguistic Structure Determines What Latent Task Representations Can Replace In-Context Learning](https://arxiv.org/abs/2610.00526)

**<font color=#1a73e8>作者：</font>** Gunmay Jhingran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) can be amortized into latent objects (task vectors, function vectors, context vectors) that recover few-shot behavior at zero-shot inference cost, but recent theory shows a static vector acts as a single synthetic demonstration and must fail on high-rank mappings such as word-level bijections. We ask a linguistic version of this question: which linguistic operations can be amortized out of the prompt? We train a 2.6M-parameter network that reads the geometry of a few-shot support set (centroid, principal subspace, spectrum, computed once and cached) and produces an input-conditioned additive update to the query's residual stream at a mid-depth layer of a frozen GPT-2-large/XL. Across eight inflectional directions and one lexical relation, under a canonical split that bars inverted-pair leakage between directions, three regimes emerge. On forward inflection, where 10-shot ICL is strong (0.67-0.89) and extracted task vectors collapse (<=0.06), the transform matches ICL at strictly zero-shot per-query cost. On lemmatization directions, which frozen GPT-2 can execute but 10 demonstrations systematically fail to convey (ICL 0.13-0.48 at 1.5B), the transform is not capped by ICL at all: it reaches 0.78-0.92, up to +72 points over ICL (past to present: 0.85 vs. 0.13). On arbitrary pairings (antonymy) every amortizer plateaus near half of ICL at every scale, capacity, and seed tested. Controls show the support manifold acts as a causally necessary task fingerprint: wrong-task manifolds collapse accuracy to <=0.06, query-only variants cannot disambiguate tasks sharing an input space, and leave-one-task-out transfer is zero. Productive rules amortize into latent task representations, sometimes better than prompting can convey them; memorized pairings do not.

---


### 79. [Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers](https://arxiv.org/abs/2610.00531)

**<font color=#1a73e8>作者：</font>** Yerim Oh, Young-Jun Lee, Jaewoo Ahn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-generated content, often called AI slop, is increasingly common everywhere, particularly in academia. Slop in AI-generated scientific papers, however, has more complex patterns that cannot be easily detected by existing token-based AI detectors. Each part of such a paper looks plausible while the scientific reasoning that connects the parts breaks down, which can mislead how readers assess the work. We benchmark these failures as scientific slop through six measures across Structure, Argument, and Artifacts. We construct SciSlopBench with 390 AI-generated papers, mostly in computer science but spanning the life, social, and natural sciences, each paired with a human-written paper matched by research problem and contribution type. Our measures identify the AI paper in each pair with 85.9% accuracy, compared with 68.7% for Binoculars. Higher scientific slop accompanies lower ICLR ratings and distinguishes rejected from accepted papers above chance in every year from 2017 to 2025. Reducing these patterns, however, is not as simple as directly optimizing the measures. We therefore propose SciSlopHarness, a harness-level framework that guides a fixed LLM to revise slop only where the experiment records support the change. While standard revisions leave residual slop and direct slop-aware prompting triggers reward hacking, SciSlopHarness reduces the remaining AI-human gap by 63% over the strongest revision baseline without requiring human reference targets. Overall, we demonstrate that AI-generated scientific papers leave fundamental traces in their global reasoning, and that responsible mitigation demands strict evidentiary grounding rather than mere prose refinement.

---


### 80. [Assessing the Impact of Language Disparity on Multilingual Linguistic Ability in Large Language Models](https://arxiv.org/abs/2610.00540)

**<font color=#1a73e8>作者：</font>** Zhanyu Chen, Jaap Jumelet  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Claims about the grammatical competence of multilingual language models vary sharply with how competence is measured, yet the interaction between evaluation paradigm, post-training, and language resource availability has not been systematically examined. We evaluate base and post-trained models from six families on MultiBLiMP, a syntactic minimal-pair benchmark covering 101 languages, using four evaluation methods. We report three principal findings. First, post-training degrades grammatical competence, but the magnitude of this effect is reduced unevenly by model scale, while low-resource languages bear the highest cost. Second, post-trained models retain grammatical knowledge they cannot articulate through explicit prompting, yet this is measurable only in high-resource languages, because near-chance baselines in low-resource settings leave little knowledge to hide. Third, native-language prompting recovers otherwise hidden competence on low-resource languages, demonstrating that only high-resource languages can be probed directly from unprompted probabilities. We conclude that multilingual grammatical evaluation must adopt language-informed, multi-paradigm protocols to avoid systematically underestimating low-resource abilities.

---


### 81. [No One Architecture Fits All: A Cross-Environment Evaluation of Hierarchical Red Team Agents](https://arxiv.org/abs/2610.00557)

**<font color=#1a73e8>作者：</font>** Ayan Javeed Shaikh, Arunesh Sinha, Nathaniel D. Bastian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous red team agents increasingly stress-test AI-enabled cyber defenses by planning strategy and executing multistage attacks. Reinforcement learning (RL) and large language models (LLMs) offer complementary mechanisms for the planning and execution such agents require, and prior work has combined them in hybrid hierarchies. Yet a given architecture is typically developed and evaluated within a single environment, leaving open whether an observed advantage reflects a generally stronger decision mechanism or merely alignment with a particular setting. We address this gap with a controlled cross-environment comparison of two homogeneous hierarchical red team architectures: an RL planner with an RL executor (RL+RL) and an LLM planner with an LLM executor (LLM+LLM). We evaluate both against expert autonomous defenders in CybORG CAGE-4 and in Cyberwheel at two network scales, across 18 configurations under one unified disruption metric. We find a pronounced environment-dependent inversion. RL+RL wins the compact, densely rewarded CAGE-4 (78.5% disruption success versus 18.0% for the strongest LLM configuration) and the 100-host Cyberwheel network (81.0% versus 50.5%), while a pretrained cybersecurity LLM agent wins the larger, escalation-gated 1010-host Cyberwheel network (55.0% versus 0.0% for RL). A kill-chain analysis explains the inversion through architecture-specific bottlenecks that aggregate success rates this http URL the 1010-host Cyberwheel network, RL discovers and compromises hosts but stalls at privilege escalation, whereas in CAGE-4, LLM agents obtain privileged access but rarely convert it into operational impact. These results indicate that conclusions drawn in a single environment may not generalize, and that hybrid planner-executor designs should be motivated by specific failure modes rather than the assumption that one architecture is universally preferable.

---


### 82. [Redundancy Meets Synergy: Dependency-aware Expert Selection for MoE via Submodular Optimization](https://arxiv.org/abs/2610.00558)

**<font color=#1a73e8>作者：</font>** Zheng Lin, Shaoke Fang, Yuxin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Mixture-of-Experts (MoE) models effectively scale model capacity through sparse activation, their deployment is often bottlenecked by prohibitive memory requirements. Extracting a compact subset of experts presents a promising solution. However, existing expert selection heuristics predominantly rely on Top-k ranking, which isolates the evaluation of individual experts and ignores the intricate inter-expert dependencies introduced by the MoE gating network. In this paper, we propose DS-MoE, a theoretically grounded framework that redefines expert selection via difference-of-submodular (DS) optimization. By analyzing the second-order Taylor expansion of the loss degradation, we reveal functional duality within expert combinations: redundancy (where experts encode overlapping representations) and synergy (where experts provide complementary error cancellation). To navigate this duality, we mathematically decouple redundancy reduction from synergy maximization by formulating the selection objective as a DS function. Furthermore, we devise a tailored majorization-minimization (MM) algorithm with provable monotonicity guarantees to efficiently identify the optimal expert subset. Extensive experiments demonstrate that DS-MoE effectively preserves indispensable expert combinations, achieving superior performance compared to the state-of-the-art baselines.

---


### 83. [PhysVista: Benchmarking Physical Intelligence in VLMs via a Perception-Reasoning-Assessment Loop](https://arxiv.org/abs/2610.00559)

**<font color=#1a73e8>作者：</font>** Xinge Peng, Yiting Lu, Tianwu Zhi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown strong multimodal reasoning capabilities, yet whether they truly capture the physical consistency underlying real-world dynamics remains unclear. Existing benchmark paradigms often suffer from fragmented evaluation, focusing on isolated cognitive stages while overlooking the inherent synergy between perception, reasoning, and physical judgment. The lack of a holistic perspective limits the ability to diagnose whether VLMs can reliably evaluate the physical authenticity of emerging generative models. To address these issues, we introduce PhysVista, a benchmark designed to evaluate physical intelligence in VLMs through a closed cognitive loop framework inspired by the human seeing-reasoning-assessment process. PhysVista restores this loop by jointly evaluating physical state perception, physical dynamics reasoning, and physical plausibility assessment. It further distinguishes event-level reasoning and scale-level reasoning to enable fine-grained analysis of physical understanding. In addition, PhysVista incorporates both real-world and AI-generated videos, allowing evaluation across diverse domains and emerging generative scenarios. Extensive experiments across a diverse set of VLMs reveal substantial limitations in physical reasoning and plausibility assessment, highlighting a persistent gap between visual recognition and genuine physical understanding, and pointing toward more principled designs for physically grounded multimodal intelligence.

---


### 84. [Can LLMs Reason Over Long Horizons? An Empirical Evaluation of Context Strategies for Longitudinal Clinical Reasoning](https://arxiv.org/abs/2610.00562)

**<font color=#1a73e8>作者：</font>** Taye Akinrele, Noorbakhsh Amiri Golilarz, Subash Neupane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Longitudinal clinical reasoning requires large language models (LLMs) to identify and integrate relevant evidence distributed across extended patient histories. Although long-context models can process increasingly large amounts of information, providing more history does not necessarily make relevant evidence more accessible or improve reasoning. We compare five context strategies (Full, Recent, Episodic, Semantic, and Hybrid) on MedLoCoMo across four open-weight LLMs, examining answer correctness, robustness to query-evidence distance, and abstention on questions with unsupported premises. Episodic and Hybrid generally achieve the strongest overall accuracy, while Recent Context degrades most as supporting evidence becomes more distant; Episodic and Hybrid maintain the highest accuracy at long distances. Analysis of adversarial questions further shows that strong performance on answerable questions does not necessarily translate to successful abstention when the available history does not support the requested conclusion. These findings show that reliable longitudinal reasoning depends not only on how much history an LLM can access, but critically on how relevant evidence is selected and presented for reasoning.

---


### 85. [Emergent Unfaithfulness: How Alignment Training Causes Language Models to Silently Override Task Faithfulness](https://arxiv.org/abs/2610.00568)

**<font color=#1a73e8>作者：</font>** Pardis Sadat Zahraei, Janvijay Singh, Gokhan Tur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are characterized by three key properties: capability, alignment, and faithfulness. Prior work studies the tradeoffs between capability and alignment, and between capability and faithfulness, but a third tension remains underexplored: the alignment-faithfulness conflict. We show that aligned models systematically deviate from their inputs on unsafe or sensitive content without disclosing the modification, a failure mode we call alignment-induced unfaithfulness (AIU). Unlike capability-driven unfaithfulness, which comes from errors in knowledge or reasoning, this is induced by post-training mechanisms that override adherence to the input. We introduce FaithConflict, a controlled dataset isolating both conflicts, and two complementary taxonomies: behavioral (B1-B8) and chain-of-thought reasoning (C0-C6). Across models, AIU increases with scale and more sharply than capability-driven unfaithfulness, a reverse scaling law; intermediate checkpoints show it is amplified during post-training, with DPO the stage at which the gap both grows most and becomes least visible. Prompting-based mitigation does not resolve it, revealing a capability-alignment-faithfulness trilemma in the design and evaluation of LLMs.

---


### 86. [FORTE: Adaptive Scoring and Exact Keyframe Selection for Long-Video Question Answering](https://arxiv.org/abs/2610.00573)

**<font color=#1a73e8>作者：</font>** Haifeng Huang, Biyin Xu, Chunsheng Xin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Query-aware keyframe selection enables multimodal large language models (MLLMs) to process long videos using only a small set of question-relevant frames. Existing score-based methods, however, typically search within a fixed, uniformly sampled candidate pool, preventing evidence outside this pool from ever being selected. Given a limited relevance-scoring budget, the key challenge is to allocate evaluations adaptively to promising frames while continuing to explore underrepresented temporal regions. We introduce FORTE, a training-free framework that addresses this challenge through two stages: adaptive relevance scoring and global keyframe optimization. Starting from sparse, uniformly distributed observations, our efficient Gaussian-process relevance predictor estimates relevance for unscored frames, exploiting temporal locality and the approximately banded kernel structure to reduce the core computation from cubic to linear time in the number of frames for fixed bandwidth. The scoring stage then selects which frames to score next by balancing predicted relevance with temporal coverage, prioritizing promising regions while also exploring less-represented parts of the video. The optimization stage selects the final keyframes by maximizing an objective that jointly captures measured relevance and temporal coverage. We derive an exact algorithm that leverages the logarithmic coverage structure to identify the optimal subset of the scored candidate pool in time linear in the pool size, for a fixed final-frame budget. Experiments on four long-video question-answering benchmarks show that FORTE achieves the highest observed mean accuracy among the compared selectors under every tested scoring budget. Further evaluations demonstrate its consistent effectiveness across different relevance scorers and downstream MLLMs.

---


### 87. [Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward RL](https://arxiv.org/abs/2610.00574)

**<font color=#1a73e8>作者：</font>** Tong Zheng, Skylar Zhai, Zhan Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-reward reinforcement learning trains large language models to satisfy multiple behavioral objectives simultaneously. Reward-wise normalization, as used in GDPO, preserves reward-specific relative information within rollout groups, but different objectives can still exhibit uneven learning progress. We study this behavior through advantage energy, the sum of a reward's squared advantages over a batch. Under idealized GDPO normalization, we show that this energy is proportional to active-group density: the fraction of rollout groups in which the reward provides nonzero relative advantages. This reveals a residual batch-level signal imbalance and provides a basis for calibrating reward contributions. Based on this relation, we propose Density-Aware Reward Aggregation (DARA). We derive an inverse-square-root density correction that gives greater weight to signals from less frequently active rewards. DARA computes its weights from each rollout batch, adapting to changes in reward activity throughout training without modifying the underlying policy optimization objective. Experiments on tool calling and mathematical reasoning show that DARA learns the targeted behaviors faster than GDPO, reaching high format compliance in up to 26% fewer training steps on tool calling and near-saturated length compliance in up to 65% fewer steps on mathematical reasoning, while remaining competitive in final performance. Our code is available at this https URL.

---


### 88. [Gestalt: Large Multimodal Interplay Model](https://arxiv.org/abs/2610.00576)

**<font color=#1a73e8>作者：</font>** Zequn Yang, Yu Miao, Haotian Ni 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose Gestalt, a new paradigm of large multimodal model built around multimodal interplay. Despite rapid advances, large multimodal models are reaching a bottleneck: existing approaches focus primarily on accommodating additional modalities while overlooking the distinct characteristics of each modality and the relations among them. Motivated by the multistage property of human multisensory perception, we propose a multimodal interplay pyramid that organizes multimodal modeling as a progression from modality-specific processing, through cross-modal alignment, to deeper multimodal integration. Guided by this pyramid, Gestalt adopts a unified discrete diffusion framework and an interplay-partitioned architecture, with learnable interplay tokens mediating cross-modal exchange and integration. The pyramid also structures its data organization and training strategy. Strong performance across image generation, multimodal understanding, and text-only evaluation shows that Gestalt significantly improves cross-modal integration while preserving modality-specific information, effectively harnessing the strengths of diffusion-based multimodal models and offering a promising path toward unified multimodal intelligence.

---


### 89. [Discrete Annotation, Continuous Preference: Rethinking Supervision for Accurate and Generalizable Aesthetic Image Cropping](https://arxiv.org/abs/2610.00582)

**<font color=#1a73e8>作者：</font>** Ziqing Zhang, Xiao Liu, Kai Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aesthetic image cropping aims to identify the optimal crop of an image in terms of aesthetics and composition. While supervision based on annotated data is fundamental, the field has been hindered by a long-standing problem: existing datasets suffer from (1) human subjectivity and (2) rigid discreteness confined to fixed sampling grids. These flawed annotations not only limit the accuracy and generalization of trained models but also severely distort fair evaluation. To overcome this, we propose to model human cropping preference as a multi-peaked, continuous, and sharp field over the crop space. We introduce the Continuous Preference Field (CPF), which recovers a dense preference landscape from discrete annotations through (1) peak clustering, (2) off-lattice refinement, (3) negative shaping, and (4) field assembly. Based on this, we train CPIC, a VLM-based cropping model optimized via GRPO with the CPF reward, which overcomes template collapse, achieving state-of-the-art performance and exceptional out-of-domain generalization. Finally, to resolve the long-standing benchmark evaluation crisis, we introduce CPICD, a comprehensive recalibration of existing ground-truth boxes. By leveraging the CPF to correct grid-bound artifacts across mainstream benchmarks, CPICD establishes a rigorous and reliable foundation for future cropping research. Extensive experiments and user studies demonstrate the superiority of our CPF, CPIC, and CPICD. Code, model, and data are available at this https URL.

---


### 90. [Towards Hierarchical Cyber Defense with Large Language Models: From Planning to Execution](https://arxiv.org/abs/2610.00590)

**<font color=#1a73e8>作者：</font>** Harshith Doppalapudi, Nathaniel D. Bastian, Ankit Shah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An autonomous cyber defender trained with reinforcement learning (RL) is typically tied to the network on which it was trained, limiting its ability to generalize as network scale changes. Hierarchical RL reduces decision complexity by separating strategic targeting from tactical execution, but it does not eliminate this retraining dependence. We investigate whether frozen, zero-shot large language models (LLMs) can provide retraining-free control in hierarchical cyber defense and how performance changes as LLM control is extended from planning to execution. We formulate a controller-agnostic planner-executor hierarchy in which the planner selects a subnet to defend over a fixed horizon and the executor selects defensive actions within that subnet. Using the high fidelity Cyberwheel environment, with its built-in automated red team agent mapped to the MITRE ATT&CK framework, we compare RL+RL, LLM+RL, and LLM+LLM configurations using six models ranging from 3B to 70B parameters, including two cybersecurity-specialized models, across small, medium, and large networks. Replacing only the planner with an LLM yields limited gains as network size increases. In contrast, extending LLM control to execution produces notable improvements for sufficiently capable models. For instance, a frozen general purpose 70B model holds successful lateral movement to approximately 1% of steps and attacker impact near zero across all three network scales using the same model weights, while the RL baseline is retrained for each scale. Our results show that sufficiently capable frozen LLMs can maintain strong defensive performance across the evaluated network scales without task-specific retraining, while also indicating that strong tactical execution is important to realizing the benefits of LLM-based control.

---


### 91. [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](https://arxiv.org/abs/2610.00604)

**<font color=#1a73e8>作者：</font>** Egor Cherepanov, Nikita Kachaev, Aleksandr I. Panov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language-action policies often see only one or a few recent frames, which makes it difficult to evaluate how they use information that disappears during a task. We introduce MIKASA-Robo-VLA, a benchmark of 90 language-conditioned manipulation tasks. All but 10 hide the cue an action depends on. Those 10 are reactive controls. MIKASA-Robo, the suite it rebuilds, has 32 tasks and uses language only in a representative VLA subset. Here every task provides an instruction, while memory-dependent tasks hide a task-relevant cue and reactive controls keep it available. For 70 tasks, environment phase timings specify an information gap, and for 28 of them the gap exceeds the 16-frame window of the widest fixed-context VLA we survey. The gap counts only the interval the cue is provably absent, not the full duration a policy must retain it, so every memory-dependent task still requires memory by construction, including the ones whose measured gap is short. We release 22,500 oracle trajectories across 10 memory types in RLDS and LeRobotDataset v3. A reference $\pi_{0.5}$ baseline with current images and proprioception, but no observation history or explicit memory module, is fine-tuned on 14 tasks and achieves 0.211 $\pm$ 0.044 mean task success. Its lower success on the evaluated Long-split tasks is confounded by open-loop chunking and the memory types represented in that subset. Project page: this https URL

---


### 92. [Where's Waldo? Query-language Preference under Cross-lingual Knowledge Disparities](https://arxiv.org/abs/2610.00606)

**<font color=#1a73e8>作者：</font>** Dayeon Ki, Ruochen Zhang, Silviu Cucerzan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models increasingly serve as interfaces for knowledge-intensive information seeking tasks across languages by synthesizing multilingual evidence. Prior work has shown that they often exhibit query-language preference -- the tendency to favor sources written in the language of the query -- but has largely examined this behavior in settings where equivalent knowledge is available across languages. However, this bias becomes consequential when sources in different languages provide incomplete or inconsistent accounts of the same fact, since the information users receive then depends on the sources a model selects to use. To characterize query-language preference under such cross-lingual knowledge disparities, we introduce Waldo, a multilingual Question-Answering (QA) benchmark constructed from Wikipedia. Waldo contains 12K QA pairs targeting knowledge gaps, where a fact is available in one language but absent in another, and knowledge conflicts, where language editions provide conflicting versions of the same fact. Evaluating eight models across five languages, we find that when one language edition merely lacks the relevant fact, models generally use evidence from the other language regardless of the query language. Under conflicting accounts, however, model responses strongly align with the document in the query language, causing semantically equivalent queries to elicit different accounts depending on the user's language. Finally, we explore two different approaches that could mitigate this preference under knowledge conflicts: a mechanistic intervention that ablates attention heads associated with query-language preference, and LoRA-based training, which reduces the preference gap by up to 61.5%.

---


### 93. [Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents](https://arxiv.org/abs/2610.00609)

**<font color=#1a73e8>作者：</font>** Katrina Drozdov, Oliver Chen, Langston Nashold 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal research is a core and time-consuming legal workflow. Lawyers must identify controlling authority, verify that it remains valid, reconcile statutes and cases, and synthesize a grounded answer. Language model agents are a natural fit for this retrieval-intensive workflow, and automating even part of it would be valuable. But that value depends on reliability: a single missing authority, stale citation, or wrong legal conclusion can make an otherwise plausible answer unusable. We introduce \textbf{Legal Research Bench} (LRB), a benchmark of 413 open-ended U.S. legal research questions written by experts, each paired with a gold answer, supporting authorities, and a binary grading rubric. We evaluate thirteen frontier models in a harness with web search, case-law search, page parsing, and retrieval tools. We score agent responses through all-pass grading with source verification, where a response is correct only if every required criterion is satisfied and its cited authorities verify. We also validate the LLM judge against expert attorneys ensuring that benchmark scores track attorney judgment. Agents remain far from reliable: among the models we tested, the strongest, Claude Opus 4.8, is fully correct on 42.9\% of questions. Performance also varies substantially by task setting: all-pass rates differ across areas of law and are lower on questions requiring reconciliation of conflicting authorities. Across models, more turns, tool calls, and inference cost do not predict higher accuracy.

---


### 94. [Explainable Suicide Risk Assessment on Social Media with Multi-Task QLoRA](https://arxiv.org/abs/2610.00610)

**<font color=#1a73e8>作者：</font>** Xuan Zhong Feng, Geoffrey Martin, Hexin Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explainable suicide-risk assessment requires models not only to estimate risk severity, but also to identify supporting language and the risk and protective factors expressed in a post. We present our system for the IEEE BigData 2026 Cup on Explainable Suicide Risk Assessment on Social Media, which addresses three tasks: risk-level classification, evidence phrase extraction, and multi-label factor identification. Our approach adapts Qwen2.5-Instruct models using quantized low-rank adaptation (QLoRA) and an answer-masked causal language-model objective. We jointly train across all three tasks for risk classification, jointly train on Tasks~1a and 1b for evidence extraction, and adapt Task~2 separately for factor identification. We also tailor aggregation to each output: we average risk-level probabilities from the 32B and 72B models, combine evidence phrases through cross-fold consensus, and calibrate factor-specific decisions through rate matching based on out-of-fold operating points. On the official leaderboard, the final system achieved a composite score of 0.7738, with 0.8089 on Task~1 and 0.6919 on Task~2. Across the evaluated configurations, three-task training performed best for Task~1a, joint training on Tasks~1a and 1b performed best for Task~1b, and task-specific training performed best for Task~2. Probability averaging further improved Task~1a when component models had complementary errors. These findings highlight the value of tailoring both training objectives and aggregation strategies to the output structure of each task within a unified language-model framework.

---


### 95. [Spatial Strategies, Not Actions: Vector-Quantized Geodesics as Tools for LLM-Driven Agents](https://arxiv.org/abs/2610.00613)

**<font color=#1a73e8>作者：</font>** Gabriel Turinici  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) based agents are often criticized for lacking spatial understanding and mainly exploiting statistical text patterns. We investigate their spatial comprehension through an architecture combining geometrical tools with a LLM serving as a high-level orchestrator in grid-world environments. The agent first collects geodesic trajectories, which are then vector-quantized to extract a representative subset. Offline, the LLM associates a natural language description of the underlying behavioral patterns to each selected trajectory, making it a tool. Online, the LLM chooses the appropriate tool conditioned on the current state and goal. Low-level control is handled by primitive actions that execute the trajectory associated with the tool. From an agentic AI perspective, this approach separates learning into two levels: tool discovery is handled through unsupervised quantization of trajectories, while reasoning and decision-making are handled by the LLM. We test the approach in a partially observable dynamic 2D grid environment with an open vision-language model (Qwen3.6-35B-A3B). Pairing the geometry-derived tool library with an agent-centered zoom tool and a collision detection tool lets a fast, non-reasoning configuration match the goal-reaching rate of a much more costly chain-of-thought version, while cutting the cost of a decision from minutes to seconds.

---


### 96. [HAWK: Rethinking Multimodal Drafting for Speculative Decoding](https://arxiv.org/abs/2610.00623)

**<font color=#1a73e8>作者：</font>** Wenhan Yang, Anirudh Rao, Ashwin Chandra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has achieved substantial lossless speedups for LLMs, but remains less effective for large vision-language models (LVLMs), where lightweight drafters struggle to use rich multimodal information. A second limitation is that standard distillation supervises the drafter only along the original training trajectory, without modeling how target predictions shift after the drafter's own proposals. As drafting moves away from this trajectory, the drafter can increasingly disagree with the target, reducing acceptance in later steps. We propose HAWK to address both limitations. HAWK uses representation similarity to select informative target layers and learns how to combine their hidden states. For visual information, it directly provides the drafter with compressed visual hidden states from the target model instead of raw visual tokens, making the visual information easier for a shallow drafter to use. HAWK also trains the drafter to capture how target predictions change after its own proposals, improving its agreement with the target during multi-step drafting. On SmolVLM-256M across ten multimodal benchmarks, HAWK raises average acceptance length from 3.32 to 4.08 and speedup from 2.19x to 2.60x over EAGLE-3 under greedy decoding, and from 2.89 to 3.41 and 1.92x to 2.19x under sampling.

---


### 97. [CompMat-Bench: Benchmarking AI Agents for Computational Materials Science](https://arxiv.org/abs/2610.00636)

**<font color=#1a73e8>作者：</font>** Chenmu Zhang, Levi Felix, Jun-Jie Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating AI agents on scientific research tasks is constrained by the time and resources required for the underlying experiments or calculations. In computational materials research, repeating the same expensive simulations across agents and trials can make evaluation impractical. We introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study's scientific goal. We reproduce the research steps in advance and assess agents on preparing inputs and analyzing outputs for expensive simulations, so expensive simulations can be avoided during evaluation. The reproduced inputs and results serve as ground truth for grading agents with fixed rules, without an LLM judge. The benchmark supports four evaluation conditions: single tasks and workflows composed of related tasks, each with full or reduced methodological guidance. With full guidance on single tasks, agents based on three LLMs demonstrate the ability to complete individual materials research steps, with pass rates of 66.0-90.4% across 94 tasks. Both longer workflows and reduced guidance can limit agent performance, but in different ways for different agents: they lower the pass rates of the weaker agents, whereas the strongest agent falls only when a long workflow is combined with reduced guidance. Failure analysis attributes most failures to scientific errors rather than to errors in software usage. CompMat-Bench provides a basis for comparing agents on the steps of real materials research and for analyzing agent failure modes.

---


### 98. [Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations from Bach to the Night Sky](https://arxiv.org/abs/2610.00647)

**<font color=#1a73e8>作者：</font>** Liam Storan, Andreas Tolias, Nina Miolane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The representations that language models learn for concepts such as months, weekdays, and places display consistent geometric structure: circles and saddle-shaped "Pringle" manifolds. Recent work traced these structures to $\textit{translation symmetry}$ in word co-occurrence statistics, deriving the observed Fourier geometry when co-occurrence depends only on distance on an abelian lattice of concepts. We demonstrate that more general notions of symmetry lead to equally structured predictions. Considering symmetries defined by arbitrary finite groups, compact groups, and homogeneous spaces, we prove that whenever the co-occurrence statistics of a word family are invariant under a group $G$, the learned word embeddings consist of matrix elements of the irreducible representations (irreps) of $G$. Circles and Pringles arise when $G$ is cyclic, in which case the irreps are Fourier modes. We verify the irrep structure in three experimental settings. (i) The cyclic group $\mathbb{Z}_{12}$: for the months of the year we recover the known circular geometry. (ii) A dihedral group acting on the major and minor triads: we unify two classical observations -- that transposition and chord inversion form a group ($T/I$) acting on chords (music theory), which $\textit{implies}$ that the well-known "circle of fifths" emerges in learned chord embeddings (machine learning). (iii) We explain and reproduce a recently discovered spherical representation of celestial objects in large language models (LLMs) as a spherical-harmonic embedding derived from our theory. Our results demonstrate that the geometry of learned representations is often a consequence of the statistical symmetry of underlying data.

---


### 99. [Incident-Arena: Getting agents to the last nine of reliability](https://arxiv.org/abs/2610.00648)

**<font color=#1a73e8>作者：</font>** Andre Fu, Malik Drabla, Leon Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agents are ubiquitous in engineering workflows amongst industry and academia. Yet, despite their use in app coding, relatively less attention has been paid to their ability to execute on production incident response. This emerging field, termed agentic site-reliability-engineering (SRE) contains benchmarks limited by (1) unrealistic environments, typically toy repositories (2) non-standard framework implementations and (3) simple static verifiers. We introduce Incident-Arena, a human-built benchmark of 20 carefully selected tasks grounded in real-world deployed open source software. Each task deploys a production application to an ephemeral Kubernetes cluster, injecting a fault from the config layer through underlying images, and a sustained load profile given the task requirements. We also present a novel verification method, going beyond static checks to functional verifiers, holding systems level metrics stable, while ensuring repairs are done safely. Agent trials run an average of 2.81M tokens and 41 turns, going beyond existing benchmarks, demonstrating agentic long horizon reasoning. Across 20 tasks and 3 application substrates, frontier models score below 64.3%, with failures extending from diagnosis/localization errors, through incomplete repairs and unsafe regressions.

---


### 100. [Self-Evolving Coding Rules for AI Coding Agents](https://arxiv.org/abs/2610.00650)

**<font color=#1a73e8>作者：</font>** Zhengyuan Jiang, Reachal Wang, Yuepeng Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of AI coding agents is highly dependent on their underlying coding rules. However, existing coding rules are typically hand-crafted and fixed, making the process labor-intensive and often suboptimal. In this work, we propose RuleEvolve, a self-evolving framework for coding rules. RuleEvolve maintains a pool of candidate coding rules and iteratively improves them. In each iteration, it employs an LLM-powered mutator module to generate variants from existing candidates, and then uses a judge module to evaluate these variants and update the pool with the best-performing ones. Extensive evaluations across two coding-agent frameworks, four backbone LLMs, and three benchmarks demonstrate that RuleEvolve outperforms both manual engineering and existing prompt optimization baselines in terms of functional correctness of the generated code, code length, and/or generation cost (e.g., tokens used).

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
