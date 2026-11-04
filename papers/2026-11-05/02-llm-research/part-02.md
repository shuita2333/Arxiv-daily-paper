# 🧠 大模型相关研究 | 2026年11月05日

> 本类共 **220** 篇论文：已确认 **208** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

---

### 51. [Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning](https://arxiv.org/abs/2611.04031)

**<font color=#1a73e8>作者：</font>** Xinbo Zhao, Yuhang Liu, Xin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Offline multi-task reinforcement learning (MTRL) aims to learn a unified policy from heterogeneous offline datasets that generalizes across tasks. However, existing offline MTRL methods often struggle with two fundamental issues: severe per-task data scarcity and limited cross-task generalization. In this paper, we propose Language-Model Augmented Decision Transformer (LaMA-DT), a unified sequence-modeling framework that leverages a single large language model (LLM) for both trajectory augmentation and multi-task policy learning. LaMA-DT uses natural-language task descriptions to guide task-aligned trajectory augmentation through a set of supervised generation and alignment objectives, and incorporates a scoring-and-filtering mechanism to retain high-quality augmented trajectories. The same LLM is then repurposed as a language-conditioned Decision Transformer and fine-tuned on a mixture of real and augmented data. Experiments on Meta-World and MuJoCo multi-task benchmarks demonstrate that LaMA-DT consistently outperforms competitive baselines, particularly in low-data regimes, showing that language-guided data augmentation substantially improves cross-task generalization.

---


### 52. [ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration](https://arxiv.org/abs/2611.04032)

**<font color=#1a73e8>作者：</font>** Anshu Raina, Yao Fu, Zhang Jiejing 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serving an LLM efficiently depends on the engine, how the model is split across GPUs, precision, scheduler settings, speculative decoding, KV-cache management, and prefill-decode disaggregation. The best configuration depends on the model, hardware, workload, and objective. Operators usually find it by trial and error. Exhaustively measuring the candidates in our study would take about 25,000 GPU-hours. ROCm InferaSim predicts serving performance from a few short measurements. Choices such as batch size, prompt length, and GPU count change the amount of work per GPU without changing the kernels. ROCm InferaSim benchmarks each distinct set of kernels once, on at most one node. We call this measurement an anchor. Analytical laws carry that anchor to other deployments that run the same kernels. For multi-node deployments, ROCm InferaSim reduces the configuration to a single-node equivalent, measures it, and scales the result analytically. A simulator replays multi-turn traffic, and a tuning agent searches configurations using the predictions. On AMD Instinct MI355X GPUs with vLLM, SGLang, and ATOM, 11 anchors took 9.1 GPU-hours, against 204 GPU-hours to measure the 226 fixed-length configurations they cover. On 172 configurations, time per output token has 8.1% median error. On a multi-turn coding workload, throughput is within 8%. For 159 disaggregated deployments, none used as an anchor, throughput is within 5.5%. A five-candidate short list contains a deployment within 12% of the best feasible pairing of model and latency target.

---


### 53. [Recursa: Toward Recursively Self-Improving Foundation Model Systems](https://arxiv.org/abs/2611.04035)

**<font color=#1a73e8>作者：</font>** Erkang Zhu, Yin Lin, Xiaorong Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models in changing environments can encounter unfamiliar domain knowledge that their original training did not cover. However, new domains rarely provide large amounts of expert-created training data or reliable supervisory signals for further training. We introduce Recursa, a foundation model system that adapts to new domains by learning from its own experience without human experts or a stronger teacher model. Recursa uses a knowledge repository to store what it learns: domain-specific skills and instructions on when to apply them, along with memories of past task experiences and reflections on what to improve. Recursa bootstraps the repository from domain materials and then refines it through recursive self-improvement. It uses parallel learners to execute tasks and synthesize local improvements, then validates and merges the improvements into the knowledge repository. On Harvey LAB's Firm Knowledge benchmark, Recursa raises the all-pass rate on held-out test tasks from 30.0% to 55.0% with DeepSeek-V4.1-Flash and from 35.0% to 46.0% with Qwen3.8-Flash.

---


### 54. [Exploit or conform? How norm utility prompting changes the way LLMs use community beliefs](https://arxiv.org/abs/2611.04048)

**<font color=#1a73e8>作者：</font>** Leon Klingborg, Theodor Cimpeanu, Alexander J. Stewart  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) serve both as tools for aiding human decision-making in everyday life and as models of human agents in experimental simulation studies. Alignment on prototypical social decisions -- such as whether to cooperate on a collective action -- therefore has immediate practical consequences for researchers and for society at large. Here we systematically explore the impact of ``norm utility'' -- the non-material components of utility that account for an individual's desire to conform to social norms and to be internally consistent -- on the strategic decision-making of three open-weight LLMs in one-shot, two-player social dilemmas. We find that when a social dilemma is presented together with information about community beliefs -- but without any indication of how those beliefs should matter -- models tend to treat community belief as strategic information, so that in the Snowdrift game cooperation falls as community belief in cooperation increases. When we explicitly prompt the components of norm utility this relationship inverts, and cooperation increases with community belief, in broad agreement with the predictions of a simple norm utility model. We then show that prompting norm utility reduces the volatility of strategic decisions with respect to changes in the underlying social context, and generates more consistent reasoning habits across models. Taken together, our results suggest that prompting norm utility can help generate more human-like and consistent behavior across models and lower volatility within models.

---


### 55. [HybridSpec: Throughput-Aware Speculative Decoding for Hybrid GDN-MoE Models](https://arxiv.org/abs/2611.04055)

**<font color=#1a73e8>作者：</font>** Haiyu Wang, Sai Qian Zhang, Zechun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In speculative decoding, parallel drafters such as DFlash make drafting cheap, so target verification dominates each round. A central choice is the verification length, the number of tokens that the target processes in each round. Verifying more draft tokens can accept more of them, but work after the first rejection is wasted. For hybrid target models that combine Gated DeltaNet (GDN) and mixture-of-experts (MoE) layers, verification time grows much faster with this length than for dense models. In a single-request profile of Qwen3.6-35B-A3B with DFlash, it grew by 71% from length 4 to 16, almost entirely in GDN and MoE layers, compared with 4%-6% for a dense Qwen3-4B target. Each GDN layer must update a recurrent state at every token and recover it at the end of the accepted prefix. The MoE cost depends on the experts that the tokens activate, which are known only once verification runs. We present HybridSpec, which selects the verification length on the GPU from draft-side acceptance estimates and measured target latency. Verification then runs this length plus one extra token up to the first MoE router, before any expert runs. There, a lightweight routing correction uses the observed expert assignments to decide whether to keep that token. The rest of verification runs only on the selected tokens. Block-parallel GDN kernels avoid storing a state after every token and reconstruct the accepted state of every GDN layer in one launch. In isolated benchmarks at verification lengths 4 to 16 with every draft token accepted, these kernels, including accepted-state reconstruction, are $1.54\times$-$4.04\times$ faster than the default kernels. With three GDN-MoE target models in single-request greedy decoding, HybridSpec is $1.75\times$-$1.88\times$ faster than autoregressive decoding and $1.30\times$-$1.33\times$ faster than DFlash.

---


### 56. [Look Before You Launch: Learned Throughput Prediction for Hardware Selection in a Production Training Fleet](https://arxiv.org/abs/2611.04057)

**<font color=#1a73e8>作者：</font>** Hossein Askari, Wei Sun, Chenguang Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In mixed-vendor accelerator fleets, many training jobs can run on several hardware types, and the best choice depends on each job's throughput on each type. Routing a job needs a throughput estimate for every candidate type before the job runs. We present LEAP, a machine learning performance prediction service that predicts each training job's throughput on every candidate hardware type at submission time and ranks the candidates by predicted throughput per unit cost. It routes tens of thousands of training job attempts a day across hundreds of different model types and more than 20 hardware types in a production fleet. LEAP predicts throughput from submission-time training configuration, including each job's prior throughput. LEAP reaches an accuracy of 77% over 30 nightly retrains, higher than the lookup table it replaced and at least as high as every alternative model we tested, including fine-tuned language models. Over six months, the share of eligible training GPU-hours that received a ranking by LEAP grew from 58% to 95%, and we estimate that it saves about 3% of training computational cost. In this paper, we identify the drivers that actually move accuracy and those that do not. We offer these as lessons for teams building performance predictors at fleet scale.

---


### 57. [Query-based Submodular Data Selection for Efficient Instruction Tuning](https://arxiv.org/abs/2611.04059)

**<font color=#1a73e8>作者：</font>** Zhenghao Zhao, Yasutomo Kawanishi, Huihuo Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models are fine-tuned for increasingly specialized tasks, their performance depends more on which training examples are selected than on how many. Given a large heterogeneous training pool and a small target set specifying the desired capability, targeted data selection aims to find a compact subset that maximizes downstream performance. Existing methods score each candidate independently against the target and select the top-ranked examples, yet this point-wise strategy ignores inter-example interactions: at tight budgets the selected subset is dominated by near-redundant points that waste capacity on overlapping information. We propose Query-based Submodular functions with Gradient-guided Synthesis (QSGS), which formulates targeted selection as a submodular graph cut over a gradient similarity graph. A modular relevance term pulls selected examples toward the target task, while a pairwise dispersion penalty suppresses intra-subset redundancy. The resulting objective balances target relevance and intra-subset redundancy using the same formulation across different selection budgets. Empirically, the benefit of diversity-aware selection becomes increasingly pronounced as the data budget decreases. To further close coverage gaps that no selection from existing data can bridge, we introduce a gradient-guided synthesis step that identifies under-covered target directions via residual subspace analysis and generates synthetic examples to fill them. Experiments on MMLU, BBH, and TydiQA across Llama-2, Llama-3, and Mistral, show that QSGS at a 0.5% budget matches or exceeds full-data performance on Mistral-7B, outperforms the strongest baseline across all benchmarks, and yields increasing gains as the budget shrinks.

---


### 58. [On the Primacy Bias in RLVR Training](https://arxiv.org/abs/2611.04061)

**<font color=#1a73e8>作者：</font>** Phuc Minh Nguyen, Ngoc-Hieu Nguyen, Parshin Shojaee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a promising approach for enhancing the reasoning capabilities of large language models. However, it still remains unclear whether RLVR can extend reasoning capabilities beyond what is already encoded in the base model. In this paper, we study this question through the lens of primacy bias: the tendency of models to over-rely on already-learned representations, disproportionately improving performance on problems they already handle well while underexploring harder ones that require departing from those representations. Through our controlled experiments and large-scale analysis, we show that RLVR training on mixed data tends to further sharpen performance on easier problems while yielding only marginal gains on harder ones. We find that although hard problems lead to modest gains overall, they are actually the ones that help most in expanding the model's reasoning capabilities and pushing the representations. However, prolonged training on these hard problems may also hurt and lead to forgetting on easy problems. These findings help to better understand some of the prior conflicting observations about RLVR, specifically, why on (OOD) domains where the base model performs poorly, improvements on hard problems can expand reasoning; while on well-trained domains, forgetting can reduce performance and mask genuine gains obtained from hard problems.

---


### 59. [Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials](https://arxiv.org/abs/2611.04073)

**<font color=#1a73e8>作者：</font>** Anh Nguyen, Tianyi Xu, Phat Tran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges. However, the contribution of each component -- tutorials, the judge, and the world model -- to overall improvement has not been evaluated in isolation. To fill this gap, we first construct OSWorld-Tutorial and ScienceBoard-Tutorial: two datasets for CUAs with curated multimodal tutorials, covering everyday and scientific domains. We then propose RAG-PolicyJudge (RAG-PJ), a policy-judge framework for CUAs conditioned on task-specific tutorials: the policy proposes candidate actions, and the judge selects among them. To isolate the effect of world models given tutorials, we compare RAG-PJ with and without common world models: using either zero-shot text-based descriptions of next states or an oracle that returns ground-truth visual observations. We find that RAG-PJ gains little benefit from these rollouts when tutorials are present, even with perfect visual futures. This suggests prior world-model gains in tutorial-conditioned methods come mainly from tutorial understanding and the judge's ability to select the proposed actions, rather than from predicted rollouts. Error analysis reveals that the bottleneck is not rollout fidelity, but the judge's ability to reason over future states and recognize task completion. This highlights the need to improve not just next-state prediction in world models, but also reasoning over their predicted rollouts. Datasets and code are available at this https URL.

---


### 60. [AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance](https://arxiv.org/abs/2611.04079)

**<font color=#1a73e8>作者：</font>** Yilun Hao, Ruixiao Yang, Hudson Hilal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world problems span diverse domains, including program synthesis, symbolic reasoning, planning, and optimization, and often require fundamentally different solution paradigms. A central challenge for LLM-based reasoning is twofold: identifying an appropriate problem-solving approach and formulating it correctly. In this paper, we propose AlgoPilot, a cross-paradigm reasoning framework that enables adaptive selection of the solving approaches and structured problem formulation prior to execution. The AlgoPilot framework contains three components: 1) a SteerLM, trained via supervised fine-tuning (SFT) and reinforcement learning (RL), that adaptively selects the solving strategy (paradigm and modes) based on input problems, 2) the corresponding expert GuideLM, trained via SFT, that generates structured formulation guidance tailored to the selected strategy, and 3) an ExecutionLM that generates solutions conditioned on both the selected strategy and its formulation. Unlike prompting-based methods that rely on fixed reasoning templates, our approach learns to adaptively choose and structure problem-solving strategies based on the input. We build AlgoPilot on Qwen3-8B and evaluate across 5 problem categories and 13 benchmarks with 66 unique domains, comparing against both the latest similarly scaled small models and large LLMs. AlgoPilot significantly improves average accuracy for the same model from 38.4% to 72.9%, outperforming the best large LLM prompting baseline GLM-5 by 11.7%. Ablation studies confirm the effectiveness of each component. Notably, we show that the learned steering and formulation modules can transfer across execution models, suggesting their potential to improve other LLMs. Project page: this https URL.

---


### 61. [Follow the Features: SAE Feature-Guided Data-Efficient Instruction-Tuning of Large Language Models](https://arxiv.org/abs/2611.04085)

**<font color=#1a73e8>作者：</font>** Ryan Swift, Konstantinos Psounis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting small, effective instruction-tuning datasets requires identifying which aspects of the original data to retain. We introduce Follow the Features (FtF), a data-selection method that uses sparse autoencoder (SAE) features to characterize training data and guide subset construction. FtF ranks features using dataset-level activation statistics, scores samples by their expression of highly ranked features, and incorporates feature resampling to encourage diversity. The LLM-SAE pair used for selection is independent of the model being fine-tuned, enabling reuse across target models. We evaluate FtF on two model-dataset settings at a training budget of 100 samples with a fixed sequence length of 256 tokens. FtF achieves performance competitive with GRAPE and S2L, with relative rankings varying across settings. On Qwen 3 8B trained on Alpaca, FtF exceeds full-dataset training by 1.59 percentage points in the harmonic mean of an AlpacaEval-based win rate and Open LLM Leaderboard performance, although full-dataset training retains a higher Leaderboard score. These results support SAE feature statistics as a useful signal for data-efficient instruction tuning.

---


### 62. [Permitted but Unauthorized: Affordance-Induced Delegated-Scope Violations in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.04086)

**<font color=#1a73e8>作者：</font>** Shravya Kanchi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems place several agents on shared infrastructure, where each agent holds permissions far broader than the task it is delegated -- so every agent is routinely permitted to act on a peer's resources it was never assigned. We ask: under competitive pressure, what determines whether an agent crosses from its delegated scope into a peer's resources, and can such crossings be enforced away? We study this across eight LLMs in two simulated environments -- a CI/CD release pipeline and a security-operations incident queue -- using a deterministic, no-model-in-the-loop detector over hash-chained, replay-verified logs. In a controlled 2x2x2 factorial over competitive incentive, candidate visibility, and payoff information (three models, n=52 per cell), we find that action representation, not permission, governs the behavior: no agent crosses when the peer action is unlisted, whereas listing it under competitive pressure with a stated payoff raises crossings sharply -- up to 52 of 52 episodes for Claude Sonnet 4.5. We also observe a model-dependent split: two newer models (Claude Sonnet 5.5 and Opus 5.5) refuse the identical attack in 0 of 100 episodes, where prior-generation models cross in 9 of 10. We then evaluate two defenses -- a deterministic reference monitor and a model-based pre-execution judge -- both block every crossing and, when the task is winnable, cut avoidable peer deadline misses from 15/40 and 14/40 to at most 1/40. But scope enforcement is not harm prevention: an agent can still set a peer back through an authorized action on its own resources -- misreporting its incident's severity -- which neither defense detects. Our results establish action representation, not permission alone, as a controllable driver of inter-agent scope violations, and show that enforcing delegated scope is distinct from preventing harm, motivating effect-aware authorization.

---


### 63. [ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087)

**<font color=#1a73e8>作者：</font>** Tianyi Ma, Jing Gu, Haozhe Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific discovery builds on accurate observations interpreted through domain knowledge and reasoning. For scientific 3D data, this requires understanding structures and spatial relationships, from protein contacts to anatomical organization. Existing multimodal benchmarks largely evaluate text and 2D images, while scientific 3D evaluations vary in representations and protocols across disciplines, limiting cross-disciplinary comparison. To assess these foundational capabilities, we introduce ScienceVision, a cross-domain benchmark for scientific 3D understanding and reasoning through expert-level visual question answering (VQA). We construct 250 questions, with 50 each from Biology, Chemistry, Medical Imaging, Mechanical CAD, and Architecture, through a pipeline combining synthetic question generation with domain-expert review and annotation. Each task pairs a native 3D artifact with a scientific question, a specified response format, and a task-specific reference answer, requiring domain knowledge to be applied to geometric or topological evidence. We evaluate 12 models on the same questions in three settings: visual question answering with native 3D artifacts accessed through an agent harness's file and code-execution tools; the same workflow augmented with expert-inspired viewer inspection and measurement tools exposed through the Model Context Protocol (MCP); and visual question answering from prescribed rendered 2D images using an agent harness. All settings use the same task-specific deterministic final-answer scoring. The inspection environment supports view changes, target isolation, and slice inspection. In this main comparison, the best mean answer score is 0.53 out of 1. Mean scores in the native-artifact workflow without additional MCP tools exceed those in the rendered-image workflow for every model, by 17.2 percentage points on average.

---


### 64. [Swapping the Judge Changes the Ranking: A Preregistered Study of Cross-Provider Replication in LLM-Judged System Comparisons](https://arxiv.org/abs/2611.04090)

**<font color=#1a73e8>作者：</font>** Sangdo Han, Moonsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practitioners who compare systems with an LLM judge and have no human labels often check a conclusion by repeating it with a judge from another provider. We test how far that check can be trusted. In a preregistered study (with a disclosed post-registration reduction of the judge set), five judge models from three providers re-judged 4,000 Chatbot Arena battles (nine systems, 33 system pairs) that carry human votes, each in both response orders. Agreement with the human vote was low at the verdict level (median Cohen's kappa = 0.22), and system rankings did not survive a change of judge: Kendall's tau with the human ranking ranged from 0.17 to 0.89 (median 0.67), so the preregistered hypothesis that rankings remain stable was not supported. Conclusions replicated by two low-cost judges from different providers matched the human conclusion more often than single-judge conclusions (+0.10 precision), but the gain came from filtering out one poorly aligned judge, and replication involving that judge left a conclusion for only 35% of comparisons. Judges that agreed with humans reached a stable conclusion with no more verdicts than human votes required; the others failed to converge on 26-70% of system pairs at the sample sizes tested (up to 100 verdicts per pair). Disagreements with the human vote co-occurred across judges far more often than independence predicts, although a single human vote per battle cannot separate shared judge bias from voter noise.

---


### 65. [Same Rule, Different Verdicts: Rubric Language and Clause Structure in LLM Judges for Korean Support Dialogues](https://arxiv.org/abs/2611.04091)

**<font color=#1a73e8>作者：</font>** Sangdo Han, Moonsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Services that operate in Korean often write their evaluation rubrics in Korean and hand them to an LLM judge. We test whether a judge's verdict depends on the language of the rubric and on how a rubric item is phrased. We write 12 criteria for support dialogues in four clause structures (affirmative, negated, conditional, exception) such that two pairs of structures have the same meaning, and we give each item in Korean and in English. Six low-cost models from three providers, plus one reference model, judge 60 translated ESConv dialogues and 144 constructed boundary cases under every combination (51,744 requests across the seven models). The analysis plan was fixed and committed before data collection. Cross-provider agreement is lower with Korean rubrics than with English rubrics (Cohen's kappa 0.687 vs. 0.745; difference -0.058, 95% CI [-0.072,-0.045]). Disagreement concentrates in negated, conditional, and exception items (odds ratio 5.6 relative to affirmative items). A single model changes its verdict between two items with the same meaning in 11-15% of cases. Two hypotheses are not supported: models from the same provider do not agree more than models from different providers, and adding paired examples does not reduce the language gap. We measure consistency only; no human labels are used, and all materials were drafted by an LLM.

---


### 66. [When Strong Reasoners Join the Pool: Small Union Premiums and Costly Runaway Generations in LLM Routing](https://arxiv.org/abs/2611.04098)

**<font color=#1a73e8>作者：</font>** Teng-Ruei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing benchmarks often judge a router against a hindsight oracle that counts a query as solved whenever any model's recorded answer is correct, but under stochastic decoding that oracle mixes two different objects: the clairvoyant ceiling of committing to one model per query and the premium of calling several models and keeping any correct answer. A companion study measured this premium at 3.5 percentage points (pp) for 11 small open models on MATH-500; how large it is once current reasoning models enter the pool was unknown. We measure it with a fixed-protocol, pre-committed generation on a single NVIDIA B300: all 500 MATH-500 problems, 30 seeded samples per problem, Llama-3.3-70B-Instruct and NVIDIA's Nemotron Nano 9B v2 and Nemotron Super 49B v1.5 (a NAS derivative of the same 70B) under vendor sampling, a 65,536-token cap, a pinned Math-Verify scorer, and an append-only attempt ledger, for 45,000 scored responses. The two reasoning models both reach 96.1% accuracy against 76.2% for the 70B baseline. The empirical product-coupling premium is 0.215-0.588 pp across all two- and three-model pools; the empirical plug-in selection headroom over always calling Nano is 1.27 pp; and resampling Nano three times gives practically the same empirical any-correct rate as calling all three models once. Only 31 responses reached the cap, 25 of them with exactly periodic tails, yet the capped responses account for up to 60.2% of a model's output-length-squared proxy, and long generations made a fourth planned model, Llama-3.1-8B, too slow to finish. The premium is far below the companion's 3.5 pp, but models, pool size and protocol changed together; an oracle gap should therefore be reported with the pool, the protocol, the samples per cell and the decoding budget that produced it.

---


### 67. [Evaluation Contracts and Evaluation Leverage: Sliced-Gap Readings in Structured Prediction Can Move Without Model Change](https://arxiv.org/abs/2611.04099)

**<font color=#1a73e8>作者：</font>** Hao Lu, Weixing Zhu, Ruiyang Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> NLP evaluation reports routinely cite sliced performance differences, most prominently the intra-inter gap in document-level relation extraction, as capability evidence. We show that such gap readings are joint properties of models and evaluation contracts: scoring function, gold version, threshold, output format, and prompt language. With predictions frozen, a method ordering reverses under a gold-standard exchange (+0.0363, CI excluding zero; tie-level after), movement localizing where gold re-partitions: renames are gauge transformations (Delta=0; re-annotation +0.862). We formalize this as an evaluation leverage account centered on the rank-flip condition. Constructively, the audited evaluation reading (AER) is a contract-marginalized, tie-declared, seed-prescribed, gate-filtered procedure whose tie declarations cover every contract-induced flip on the declared WMT19 grids (14/14; held-out 73% vs. union-of-ties 89%), matching the best single metric contract at epsilon=0.10 equivalence. Evidence spans DocRE, HacRED, a UD probe, and released gold revisions; an alternative-reference-set replication extends it beyond our testbeds. Failed predictions retained as boundaries; a 5% violation gate flags unverifiable settings and bounds survivor-selection bias. We release EvalLever, a preregistered workflow with an amendment trail; on LLM-as-judge grids, the audited ensemble stabilizes every unstable pair (13-15 to zero; generic ensemble shrinkage: the preregistered correlation criterion failed, the companion stabilization criterion passed).

---


### 68. [The Agent Board: Kanban for Machines; Durable Coordination for Agents That Outlive the Conversation](https://arxiv.org/abs/2611.04100)

**<font color=#1a73e8>作者：</font>** Tyler Hunt, Donald Nguyen, Gurbinder Gill  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harnesses for large language models have converged on a single-threaded shape: one agent, one history, one machine, one sitting. That shape fails work that spans many agents, outlives any one model call, or waits on systems that are not agents. We describe the Agent Board, the coordination substrate in the Corvic harness. The board is a durable, shared table of semi-semantic tasks: a few exact fields the system routes on, and a free-form body that only language models read. Agents post tasks, watch tasks, and block on them, ending their turn and holding no process until a matching post wakes them. A system agent, the Board Keeper, acts as the interrupt handler for the board: it carries events from non-agent parts of the harness onto the board, matches them to waiting tasks by reading their prose, and allocates new agents for tasks that name a kind of agent rather than an instance. Loadable coordination policy kernels give statuses and roles meaning for a given pattern of work, without the board enforcing them. The design mirrors the kanban board a human team puts on a wall. We argue it is what persistent agent products such as Meta Muse, OpenAI dots and SpaceXAI Grok Bot need once an agent must wait, hand off work, or work with agents from another vendor. We view the board as an operating-system scheduler for agents and state where the analogy breaks. We separate what the mechanism guarantees from what it leaves to convention, and report a trace from a live board and three small simulated pilots. In the pilots, the wait cost of the board was flat in wait length while naive polling grew about 165-fold, but a plain external watcher was cheaper than the board. The Board Keeper matched prose waiters with no false wakes but missed 3.6 percent of real wakes.

---


### 69. [ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends](https://arxiv.org/abs/2611.04104)

**<font color=#1a73e8>作者：</font>** Shengjun Kris Dong, Dima Nikiforov, Sahil Modi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, existing LLM agents typically target a single programming interface, toolchain, or accelerator family, focus on kernel-level optimization without model-level transforms, and offer limited reuse of experience across hardware targets.
We present ModelBlaster, a Memory-Augmented In-Context Reinforcement Learning (MAIC-RL) framework for optimizing data-parallel kernels and whole models across heterogeneous SIMD and SIMT accelerators. Its mutable policy is a persistent knowledge base updated at inference time by Actor-Critic Textual Gradient Descent (AC-TGD). The knowledge base maps performance states to actions, outcomes, and constraints, enabling experience reuse across kernels, models, and hardware targets. A model-level optimizer uses kernel-level knowledge to inform whole-model decisions. The same optimization loop and knowledge schema support CUDA on NVIDIA GPUs, OpenCL on Qualcomm GPUs, and RVV intrinsics on RISC-V vector cores, with only lowering and measurement layers specific to each target.
Compared with PyTorch, ModelBlaster achieves geometric-mean speedups of 1.85x, 5.58x, and 5.18x on KernelBench Levels 1, 2, and 3, and 1.69x on SOL-ExecBench Levels 1 and 2 on a B200 GPU. On Qualcomm Adreno GPUs, it achieves 5.8x over the vendor SDK and 1.7x over Apache TVM; on RISC-V vector cores, it achieves 2.7x over ExecuTorch with XNNPACK across 70 KernelBench problems.

---


### 70. [Say Less, Mean Better: Training-Free Verbosity Control for Language Models](https://arxiv.org/abs/2611.04107)

**<font color=#1a73e8>作者：</font>** Mahmoud Alyosify, Mirna Imbabi, Eman Elkhamisi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often generate responses longer than necessary, increasing inference latency and computational cost. While prompting can encourage conciseness, controlling output length without compromising response completeness remains challenging. Aggressive early stopping can reduce generation costs but risks terminating responses prematurely. We introduce MinimalLM, a training-free framework for reliable verbosity control that combines uncertainty-aware, length-dependent stop-token adjustment with structural completeness guardrails. MinimalLM separates the decision of when to stop from whether stopping is structurally appropriate, coordinating response-level instructions, decoding-time intervention, and completion checks without modifying model parameters or requiring auxiliary models. We evaluate MinimalLM across three open-source LLMs and 330 questions, producing 5,940 responses across baseline and ablation configurations. MinimalLM reduces generated tokens by 47.6%, accelerates individual responses by 19-68%, and eliminates structurally truncated outputs in the primary evaluation. Despite substantial token savings, it achieves an average quality score of 8.04/10, compared with 8.42/10 for unmodified models and 6.46/10 for length-matched truncation. Evaluations across diverse subject domains (such as healthcare, programming, law, and science) demonstrate robust efficiency gains, while ablations establish the complementary roles of decoding control and completeness constraints. Our findings highlight that efficient generation requires more than producing fewer tokens: it requires controlling when generation ends while preserving response integrity. MinimalLM offers a lightweight, training-free approach toward this goal.

---


### 71. [Generalizable AI-Generated Image Detection with Embedding-Space Explanations](https://arxiv.org/abs/2611.04111)

**<font color=#1a73e8>作者：</font>** Nikos Giakoumoglou, Paschalis Giakoumoglou, Tania Stathaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated images have reached unprecedented realism, while instruction-driven AI editors re-synthesize images for local changes, leaving no splice boundary to localize. Most detectors are black boxes with unverifiable verdicts and generalize poorly because adapting a backbone on the detection distribution memorizes generator-specific fingerprints that quickly become obsolete. Specialist detectors built on pure-vision representations, particularly DINOv3, generalize well across generators, but explainable methods forgo this advantage: jointly training one multimodal model for classification and language generation subjects its visual representation to the language objective. We therefore require that explanation training cannot alter the verdict. We introduce FOX, which first builds and locks a specialist DINOv3 detector, then uses its representation to guide a lightweight VLM toward forensic explanation. A joint-embedding predictor maps locked visual evidence into a frozen text encoder's semantic space, producing guidance that the VLM verbalizes on demand. FOX achieves 97.4 mean AUC across 14 unseen generators, 69.8 BERTScore on XPlainVerse, and 56.1 on LOKI.

---


### 72. [Co-Occurrence Priors Override Visual Spatial Evidence: Understanding False Alarms in Vision-Language Models for Construction Struck-By Hazard Detection](https://arxiv.org/abs/2611.04112)

**<font color=#1a73e8>作者：</font>** Xiaoshan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly support construction hazard monitoring, yet their frequent false alarms remain poorly understood. This study investigates whether false struck-by hazard warnings arise from failures in object recognition, spatial relation encoding, or hazard decisions dominated by learned co-occurrence priors. We evaluated Qwen2.5-VL-7B and InternVL3.5-8B using 355 counterfactual worker-excavator scene pairs with controlled spatial proximity and worker-removal variants, combining behavioral analysis, internal representation probing, causal interventions, and decision correction. Both models recognized the entities and encoded their spatial relations (out-of-fold AUROC: 0.82 and 0.91), assigning higher hazard scores to near than far scenes in 79% and 73% of pairs. Nevertheless, 74% and 100% of far scenes were falsely classified as hazardous. Removing the worker reduced Qwen's hazard rate to 11%, while worker presence exerted 2.4- and 3.2-times greater influence on hazard scores than spatial proximity in the respective models. Attention-head interventions, neuron-level interventions, and activation steering failed to eliminate this co-occurrence bias. However, conditioning hazard decisions on the model's own spatial-relation representation improved Qwen's specificity from 0.36 to 0.58 at matched sensitivity, outperforming threshold recalibration. These findings reveal that VLM struck-by false alarms stem primarily from decision-making failures rather than deficiencies in object recognition or spatial encoding, suggesting that future efforts should prioritize conditioning hazard decisions on encoded spatial evidence rather than further improving visual recognition alone.

---


### 73. [The Evolution Strategies Paradox: Better Models from Worse Perturbations](https://arxiv.org/abs/2611.04113)

**<font color=#1a73e8>作者：</font>** Roberto Dailey, Kajetan Schweighofer, Jamieson Warner 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How is it possible for perturbation-based methods like Evolution Strategies (ES) to optimize billion-parameter large language models (LLMs)? Classical search methods are highly dependent on finding good candidates within generated populations. However, when using ES to fine-tune LLMs, a phenomenon can occur where all offspring models consistently perform worse than the parent model, yet during training, the parent model consistently improves. This paradox occurs across models, tasks, and even modalities. This paper characterizes the paradox, then examines how the local reward landscape and properties of the ES estimator contribute to it: in high-dimensional spaces, exploration leads to worse performance, yet still highlights good directions; aggregating those directions then allows for making local improvements. The result can be seen as a new optimization paradigm where a principled interaction of noise and curvature produces the paradox as a byproduct of effective optimization. These findings provide guidance for taking advantage of perturbation-based methods in LLM fine-tuning and in high-dimensional optimization in general.

---


### 74. [GlucoAgent: Personalized Glucose Forecasting from Multimodal Personal Context](https://arxiv.org/abs/2611.04126)

**<font color=#1a73e8>作者：</font>** Xingzhi Sun, Hyo Jin Kim, Zhiyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitors, smartwatches, meal logs, and health profiles form a rich multimodal personal context that can significantly enhance glucose forecasting. However, existing methods struggle to effectively utilize these signals to improve glucose prediction because the relevance of different modalities varies drastically across individuals and time. We present GlucoAgent, an LLM-based agentic system that addresses this challenge through dynamic, case-by-case analysis at inference time. For each forecast, GlucoAgent writes and runs code over an individual's multimodal context and returns predictions with a reason and supporting evidence. The generated programs are highly diverse, ranging from retrieving similar past meals to fitting and back-testing physiological and statistical models. On CGMacros, a multimodal glucose dataset, GlucoAgent outperforms time series foundation models on every forecasting horizon, achieving an average RMSE of 22.5 mg/dL compared to 23.5 mg/dL of Chronos-2, the leading multimodal time series foundation model. Furthermore, GlucoAgent is highly effective at leveraging multimodal data. The addition of multimodal data reduces its average RMSE by 1.4 mg/dL (24.0 mg/dL to 22.5 mg/dL), compared to a marginal 0.3 mg/dL (23.8 mg/dL to 23.5 mg/dL) improvement for Chronos-2. This advantage is most pronounced in challenging post-meal windows, where GlucoAgent uses multimodal context to reduce 60-minute forecast RMSE by 4.6 mg/dL (31.0 mg/dL to 26.5 mg/dL), far exceeding the 0.8 mg/dL (31.9 mg/dL to 31.1 mg/dL) reduction achieved by Chronos-2.

---


### 75. [LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers](https://arxiv.org/abs/2611.04137)

**<font color=#1a73e8>作者：</font>** Tianle Zhou, Yang Zhang, Tianyu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers apply a shared block several times per token to improve accuracy without adding parameters. For models such as Ouro that keep a separate key-value (KV) cache per loop, cache memory limits the batch size that amortizes repeated weight reads. Uniform-bit quantization and fixed rules per loop do not allocate precision according to each layer's sensitivity in each loop. Measurements on Ouro show that quantization sensitivity varies across (loop, layer) cells, and the sum of individual cell damages approximates the overall output damage. Sharing damage also varies by cell, with later loops generally tolerating sharing better. Skipping low-attention values to save reads produces errors that compound across loops. LoopKV uses a one-time offline profile to choose 4-bit storage, 2-bit storage or reuse of the final loop's KV for each cell. The planner minimizes reads under budgets for predicted damage and storage. During decoding, each loop reads the high 2 bits of each 4-bit value and fetches the low bits only where its own attention weights require 4-bit precision. A single fused kernel in vLLM executes the plan. Serving Ouro-1.4B on one RTX PRO 6000, the memory-optimized LoopKV-M plan stores 35% less KV than uniform 4-bit quantization (KIVI-4) on the same fused kernel and CUDA graph. It sustains 1.7-2.2x KIVI-4's goodput under a latency service-level objective with a 16K-token maximum length. None of its averages on six public benchmarks falls significantly below BF16's.

---


### 76. [Interpretable Early Termination of Web Navigation Agents via Closed Sequential Pattern Mining](https://arxiv.org/abs/2611.04142)

**<font color=#1a73e8>作者：</font>** Sergio Talavera, Magdalini Eirinaki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web navigation agents built on open-weight language models fail often and fail late, with most of the tokens spent after the trajectory has become unrecoverable. Recent work has shown that early termination is a viable cost-reduction strategy, but existing approaches produce opaque termination decisions that do not support diagnosis or human oversight. In this work we apply closed sequential pattern mining (BIDE+) to K-step prefixes of agent execution traces to produce a small, human-reviewable failure-signature library that organizes into a four-category failure taxonomy with associated repair recommendations. We use a multi-variant evaluation protocol that explicitly removes contamination artifacts (zero-step crashes and trivially separable single-step successes) so that reported detection accuracy reflects behavioral discrimination rather than trace-length distributions. We evaluate our methodology on 1,544 MiniWoB++ traces collected from three open-weight language models, achieving the best F1 at K=3 on the Exclude-errors configuration across eight methods (0.717), recovering 88% of test-set failures within three steps, and supporting an early-termination policy that saves 26.3% of tokens at 92% precision.

---


### 77. [AdSteer: Native Advertising in Large Language Model Generation](https://arxiv.org/abs/2611.04147)

**<font color=#1a73e8>作者：</font>** Shuhang Lin, Chuhao Zhou, Zhenyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) services face rapidly rising serving costs. To sustain free or affordable access for a broad user base, alternative monetization mechanisms are needed. Native advertising offers a promising approach, as it creates economic value by aligning user intent with merchant offerings. Yet how to integrate sponsored content naturally into LLM responses remains largely underexplored. Existing approaches primarily rely on prompt-level injection, multi-pass rewriting, or fine-tuning, which can compromise response quality or introduce additional computational costs. We propose AdSteer, a lightweight decoding-time advertising framework that adaptively adjusts token probabilities to integrate contextually appropriate advertisement into responses. AdSteer calibrates the strength and duration of advertising influence, making sponsored content a natural part of the response. Experiments on GEM-Bench across three application scenarios show that AdSteer achieves an average improvement of 14.1% in overall score over the strongest baselines and 22.5% fewer total tokens on average than rewrite-based methods. These results demonstrate that AdSteer provides an effective and practical solution for native advertising in LLMs.

---


### 78. [PACT: Certifying What Is Written in Parallel Decoding of Diffusion Language Models](https://arxiv.org/abs/2611.04152)

**<font color=#1a73e8>作者：</font>** Yanchao Li, Yusu Zhang, Jiaqing Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel decoding speeds up masked diffusion language models by writing several tokens per forward pass. Published commit rules choose these tokens by testing the predicted distributions. Under sampling the written tokens are drawn, and these tests do not see them. We find that answer quality follows the reliability of the tokens actually written. An answer's log probability splits into this reliability and the dependence within each step. We propose PACT, a training-free commit rule that draws the tokens first, certifies the set it will write and spaces the positions of each step apart. This certificate holds at every temperature, and we show that no rule with the same guarantee commits more positions. Experiments use four models of the LLaDA and Dream families and HumanEval, MBPP, GSM8K, MATH500 and IFEval benchmarks. PACT reaches the quality of published commit rules with fewer forward passes. Spacing removes positions from each step, yet it usually lowers the total cost because later steps then write more tokens. At the same speed, published decoders also write a word twice in a row far more often than PACT. These results suggest that commit rules should certify the tokens they write. Code is available at this https URL.

---


### 79. [Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs](https://arxiv.org/abs/2611.04166)

**<font color=#1a73e8>作者：</font>** Zihao Feng, Qingzhao Zhang, Chunyu Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety. Prior attacks on VLA reasoning corrupt the rationale itself and leave visible evidence in the text. We show that visual perturbations can instead alter the physical action while keeping the generated rationale word-for-word identical. At the shared text/action interface of Alpamayo for driving and InstructVLA for manipulation, our text-neutral action-subspace (TNAS) diagnostic shows that the locally most action-sensitive direction is nearly orthogonal to the active text-loss gradients, with 1.87% and 5.28% norm overlap. At equal hidden-state perturbation norms across both models, interventions along this text-neutral residual shift actions 4.64x to 47.8x more than text-gradient perturbations, whereas text-gradient perturbations induce 21.2x to 277x more text drift. Steering visual perturbations along this direction reaches the same decoupling from the image. Across 154 obstacle-annotated driving scenes in Alpamayo, TNAS-guided attacks induce a new collision under a word-for-word identical rationale in 52.6% of scenes under full-image perturbations and 35.1% under a localized forward-camera patch, compared with 4.55% for unguided action attacks. Relative to a text-preserving baseline, TNAS guidance raises exact rationale preservation from 83.0% to 89.5% and cuts teacher-forced text drift by 68.4% at a comparable collision rate. In InstructVLA, TNAS guidance cuts text drift by 40.5% and preserves the exact response on 85.0% of examples alongside a 1.73-unit action-chunk shift. An unchanged rationale therefore cannot certify a safe action, so monitors for reasoning VLAs must verify the predicted action channel directly.

---


### 80. [Length Is Cheap, Competition Is Not: Attention Predicts Context Rot in Retrieval](https://arxiv.org/abs/2611.04169)

**<font color=#1a73e8>作者：</font>** Yinuo Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Why do language models fail on long inputs? The common answer is length. We show that, for retrieval, length is cheap and competition is not. On five open models (0.5B to 3B parameters, four families), neutral filler costs nothing: accuracy stays at 0.97 to 1.00, up to 32K tokens on Qwen2.5-1.5B. Statements in the format of the evidence, placed at the same positions, drop it to 0.16 to 0.33. A single statement that gives the queried key a rival value multiplies the loss by 9 to 110, and every additional rival adds to it. Inside the model, one quantity tracks the failure: the attention mass left on the evidence. Across 126,473 trials it explains up to 58% of the variance in loss; log length explains at most 8%. The masked-filler protocol behind the claim that length alone hurts reproduces on MMLU (11 to 18 points lost at 30K tokens), but fails a visible control in retrieval: masking costs 45 accuracy points at 32K tokens, while the same filler left visible costs none. In retrieval, context rot is a competition for attention. We release the probe and all 126K trial-level measurements.

---


### 81. [Validation-Gated ML Pipeline Synthesis with Expert-Grounded Self-Evolving Skills](https://arxiv.org/abs/2611.04180)

**<font color=#1a73e8>作者：</font>** Zixiao Zhao, Jing Sun, Zhe Hou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have enabled agentic systems that automate machine learning pipeline construction from minimal user input. However, existing agentic AutoML methods either depend on rigid templates that limit adaptability, target narrow task domains, or rely on free-form code generation that lacks reliability guarantees, leaving intermediate errors to propagate silently and degrade the final model. We present EvoML, an agentic framework for end-to-end ML pipeline synthesis built on expert-grounded skills that evolve across runs, executed through a validation-gated harness. The framework decomposes pipeline construction into four phases coordinated by three agents: an Orchestrator that enforces validation gates, advancing each phase only when its outputs pass structural, execution, and semantic checks, which precludes error propagation and keeps every artifact auditable; an Executor that runs expert-grounded skills, grounded in the nnU-Net workflow and pairing reusable templates with online adaptation; and a Curator that performs post-run evolution, consolidating the scripts and guidance recovered during a run into the skill library so it improves across datasets. We evaluate EvoML on eight datasets spanning six sophisticated, real-world ML task types, against agentic AutoML systems and command-line coding tools. EvoML achieves full automation and the best final model quality on all eight, spanning segmentation (up to 0.94 Dice), classification (0.99 accuracy), reconstruction (0.95 SSIM), and denoising (0.79 normalized PSNR), while transferring to broader ML tasks.

---


### 82. [What Does 4-Bit Microscaling Cost a Wearable Activity Recognizer?](https://arxiv.org/abs/2611.04185)

**<font color=#1a73e8>作者：</font>** Megan Healy, Hossein Valavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable sports sensors can recognize actions on the device itself, where lower-precision numbers reduce model storage and memory traffic. Two 4-bit block-scaled formats, MXFP4 from the Open Compute Project, introduced in 2023, and NVFP4 from NVIDIA, introduced in 2025, are drawing interest. Published evaluations cover general deep-learning benchmarks and large language models; to our knowledge, nobody has yet measured what they cost a small wearable-sensor model.
We train a 159,492-parameter 1D CNN to recognize four basketball actions from wrist-accelerometer data in Hang-Time HAR and test it on players it has never seen, using five-fold cross-validation grouped by player. Every comparison between number formats is made fold by fold.
In full precision the model reaches 69.26\% macro-F1. Measured TFLite FP16 and INT8 models lose at most 0.16 percentage points. In simulation, 4-bit weights cost 1.45 points with MXFP4 and 0.72 points with NVFP4. When activations are quantized to 4 bits as well, MXFP4 loses 5.14 points and NVFP4 only 0.75, and NVFP4 comes out ahead in all five held-out-player folds.
The ranking survives two alternative simulator settings, with NVFP4 leading by 3.49 to 4.40 points. A $2 \times 3$ ablation with 4-bit weights and activations (two block sizes and three scale rules) points to scale selection as the main source of MXFP4's loss. The reference MXFP4 conversion we simulate rounds the scale down, which can pick scales that are too small, so many blocks clip their largest values. Rounding the scale up recovers 3.18 points with 32-value blocks and 3.63 points with 16-value blocks, and switching to an 8-bit floating-point scale, as NVFP4 does, adds another 0.84 and 1.20 points. Block size matters less. Under this round-down rule, 16-value blocks score 0.44 points below 32-value blocks in all five folds; under the other two rules there is no consistent effect.

---


### 83. [Where Did the Update Go? Certifying Declared Change Envelopes for Model Updates](https://arxiv.org/abs/2611.04192)

**<font color=#1a73e8>作者：</font>** Muhammad Usama, Muhammad Saad Qadir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployed language models are updated continually, and regulators increasingly accept changes that were declared in advance. Showing that an update changed behavior only where it was declared to is a different statistical problem from bounding how much it changed: a useful update is meant to change some decisions, so global disagreement and regression bounds cannot certify it. We formalize the problem with declared change envelopes. Before training, the developer commits to a region of inputs, and every decision that changes outside it counts as leakage. Leakage compares two models, so it can be certified from unlabeled traffic with anytime-valid tests whose sample cost we bound from above and below, and per-update certificates compose into a bound on lifetime drift outside all declared scopes. We measure leakage for LoRA and full fine-tuning, preference optimization, reinforcement learning, and knowledge editing on models from 1.5B to 72B parameters. Narrow updates leak widely: domain and policy LoRA updates keep only about 7-36% of the decisions they change inside the declared scope. Across 256 trained variants, leakage tracks the update's KL divergence to the incumbent on out-of-scope inputs (Spearman 0.94). None of the customary remedies we tested makes a rule-like update certifiable without giving up much of its intended change. Distilling the incumbent's decisions on unlabeled prompts in the deployment format does: anchored LoRA, GRPO, and (at a small learning rate) full fine-tuning updates certify 5% leakage from a few hundred to a few thousand unlabeled samples, and the certificates replicate on held-out traffic and on written answers. The certificates cover decision-like outputs only; on open-ended chat, re-batching alone changes 11-21% of responses and no update certifies. Code: this https URL

---


### 84. [DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](https://arxiv.org/abs/2611.04196)

**<font color=#1a73e8>作者：</font>** Yuxuan Wang, Dadi Guo, Weijie Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier LLM agents can turn known vulnerabilities into working exploits, but are costly and often access-restricted due to their potential for malicious use. Open-weight models offer a more accessible alternative, but struggle to maintain progress across long exploitation chains. They also often fail to apply relevant security knowledge at the appropriate stage and in the right context to identify and evaluate promising attack directions. To address these limitations, we propose DoGNAVY-Exploit, a multi-agent harness built around two complementary designs: stage-aware decomposition with progressive expert knowledge disclosure, and hierarchical orchestration with parallel exploration. Specifically, DoGNAVY-Exploit uses configurable milestones to recast long-horizon exploitation as short, verifiable capability transitions and provides only the knowledge relevant to each stage. Within each milestone, a hierarchical architecture separates strategic planning from parallel execution: a planner proposes diverse attack routes, executors test them concurrently, and a controller accepts progress only when supported by runtime evidence. A shared structured memory consolidates verified facts, artifacts, replay steps, and failed routes across branches, allowing agents to build on collective progress and carry validated knowledge into subsequent milestones. In controlled benchmark environments, DoGNAVY-Exploit with GLM-5.2 achieves 97.5% Pass@1 on Cybench, and 97.5% zero-day and 100% one-day Pass@1 on CVE-Bench. On ExploitGym, it solves 79 tasks with GLM-5.2 and 157 with GLM-5.3, while the corresponding public Claude Code baselines solve 39 and 130 tasks, respectively. Ablation results further demonstrate that the stage-aware orchestration, expert knowledge, parallel exploration, and memory designs can substantially improve the exploitation capabilities of open-weight agents.

---


### 85. [Tokenizer Myths and Where To Find Them](https://arxiv.org/abs/2611.04215)

**<font color=#1a73e8>作者：</font>** Rylan Schaeffer, Sanmi Koyejo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization is a fundamental component of modern language models: before a model sees data, its tokenizer has already determined how the data appears. We identify and challenge three myths in the tokenization research literature. Myth #1: Bits-Per-Byte (BPB) is agnostic to the tokenizer and/or the vocabulary size: BPB is tokens per byte times bits per token, and the two factors do not cancel; using untrained models, we show that BPB prefers some tokenizers over others: the model has learned nothing, but the tokenizer--model pair has. Myth #2: lower BPB means a better model: On untrained models, BPB strongly prefers some vocabulary sizes, even though accuracy remains at chance, and on real models trained on the same data, BPB correlates weakly with downstream performance. Myth #3: different "tokenizer-agnostic" metrics yield consistent results: The "unigram-normalized loss" is not tokenizer-agnostic; its reported correlation of 0.989 with BPB comes from a confounder and falls to 0.057 once fixed; from the same data the two metrics select different vocabularies at each model size. We present a tokenizer trilemma: no metric can score only the true distribution best, give the same predictions the same score, and tie all untrained models, so choosing a metric is choosing a research question. We conclude with a caution for reading the tokenization literature and a conjecture for future work.

---


### 86. [LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs](https://arxiv.org/abs/2611.04217)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting stock returns requires modeling persistent company relations and time-varying market signals. Graph Neural Network (GNN) approaches combine static priors with dynamic relational graphs, but treat every extracted edge as a trustworthy binary fact, ignoring heterogeneous reliability across relational sources. We propose LENS (LLM-Extracted priors and News-driven Semantics), a static--dynamic graph framework for stock return prediction and ranking that models relational reliability as a first-class signal across the pipeline. On the static side, we extract a multi-relational company graph from a Large Language Model and aggregate it over multiple runs with confidence weighting to downweight low-consistency edges. On the dynamic side, we build a news-driven semantic graph with exponential-decay temporal aggregation to capture changing market context under uneven coverage. A context-dependent gated fusion module rebalances the two graphs at the per-stock, per-day level. On S&P 500, LENS improves AR@5 by 16.4% and SR@5 by 22.6% over the strongest baseline, and on NASDAQ 100 it achieves comparable improvements (15.5% and 20.9% respectively). Ablations isolate each component's contribution, and a human-validation study of sampled relations supports that the aggregation is grounded, providing evidence that reliability-aware LLM relations and news-based semantic graphs carry complementary information for graph-based financial prediction.

---


### 87. [Shared Context Candidate Scoring with Jointly Adapted Readout Networks](https://arxiv.org/abs/2611.04218)

**<font color=#1a73e8>作者：</font>** Jingyang Du, Yiben Fu, Yang Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repeated decisions over a shared document create two distinct opportunities: reusing document computation and adapting how question representations score candidate answers. We present Q64, a candidate-scoring system that preserves a frozen 64-layer Qwen3.8-27B text backbone, reuses its hybrid prefix state and intermediate document representations, and jointly trains a residual adapter with a four-layer decoder and candidate-conditioned readout. We used ZiYor, a self-evolving AI system, to explore and refine the Q64 design. We specified the scoring method, implemented the system, and evaluated its accuracy and latency. The final adaptation stage updates 88.66 million parameters using 8,192 selected training views. On a fixed 5,112-item evaluation combining ARC-Challenge, ANLI-R3, and stratified subsets of MMLU-Pro and CMMLU, joint adaptation improves four-benchmark macro accuracy from 66.46% to 74.32%. It remains below the native 27B baseline at 75.68% and AnyJev Qwen3-32B L0 at 76.68%. On a separate synthetic workload with 4,096 document tokens and 50 questions, median cold-request latency is 2.237 seconds, compared with 5.383 seconds for the native baseline and 56.872 seconds for the measured batched AnyJev configuration. Short single-question requests do not share this advantage. The evidence supports an accuracy-latency tradeoff in the evaluated systems, rather than a backbone reduction or an isolated component advantage. Public benchmarks informed earlier development, and real-document multi-question validation remains open.

---


### 88. [Constructing a Regional Slang Lexicon for Electricity Demands via Soft-Label Bidirectional Anchoring and Active Learning](https://arxiv.org/abs/2611.04231)

**<font color=#1a73e8>作者：</font>** Rong Chang, Lijing Shi, Zhaoxiang Zang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Power-grid customer service increasingly relies on community social media, where customers describe outages, billing, and equipment faults in informal regional dialect. Such messages exhibit non-standard morphology, semantic drift, and out-of-vocabulary expressions that make manual lexicon construction costly and degrade conventional NLP tools. We propose a weak-supervision framework constructing a regional slang lexicon from curated dialect anchors and power-domain seed terms. Candidates are generated via Pointwise Mutual Information with soft-label bidirectional anchoring, retaining dialect-anchored terms while recording power-domain relevance as separate metadata, and are scored by combining Sentence-BERT semantic similarity with a jieba-based wordhood measure. Uncertainty-aware active learning with rule-based and retrieval-augmented LLM oracles is applied under three query strategies, and the resulting lexicon is evaluated by a higher-capability LLM calibrated against human expert annotations via Cohen's $\kappa$. On 11,177 real WeChat messages from Yuxi (Yunnan, China), the framework achieves an evaluator-estimated dialect precision of DP~$=$~1.0 with zero false positives. An ablation shows that soft-label layering retains 751\% more candidates than strict power-gating at identical precision, expanding the candidate pool from 41 to 349 terms. Human calibration ($n=46$) yields $\kappa_{\text{dialect}}=1.0$ and $\kappa_{\text{power}}=0.85$. The resulting 25--33-term lexicon, 4--5 of which are power-relevant, provides a preliminary resource for dialect-aware power-grid service NLP.

---


### 89. [AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](https://arxiv.org/abs/2611.04241)

**<font color=#1a73e8>作者：</font>** Kailing Li, Ruoxuan Zhang, Zheyuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not necessarily reflect changes in task objectives. We introduce AceAction, a dataset of human gameplay across multiple 3D games for learning skill composition and subgoal transitions. AceAction organizes demonstrations around complete tasks, linking overall instructions, ordered subgoals, and local skill instructions to temporally aligned visual observations and keyboard-and-mouse actions. To construct these annotations, we develop a vision-language model pipeline that identifies subgoals from changes in objectives or interaction targets, anchors navigation goals to visually recognizable waypoints, and composes adjacent subgoals into task instructions. The resulting demonstrations cover navigation, reconnaissance, combat, interaction, and recovery, with explicit stage boundaries that connect task progression to fine-grained control. We assess annotation quality through model-based verification and human inspection. An audit of 500 trajectories yields a 95.8% pass rate across independent reviewer assessments. AceAction provides a data foundation for studying how agents execute, combine, and switch skills to follow complex instructions in dynamic game environments.

---


### 90. [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244)

**<font color=#1a73e8>作者：</font>** Hien Trinh, Tan-Hiep To, Dinh-Khoi Vo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual sketch animation explores how a static sketch evolves under a hypothetical intervention. We present CounterSketch, a physics-grounded framework that transforms natural-language ``What if...?'' queries into physically plausible sketch animations. The framework integrates VLM-guided scene grounding, causal event-chain reasoning, constraint-based trajectory generation, and verification. It models physical transitions to update the scene graph, computes continuous object trajectories, and validates them against physical, geometric, and semantic constraints. The verified trajectories are then projected into object-level motion bounding boxes to guide downstream sketch-video synthesis. Experiments on CounterSketchBench (80 questions) demonstrate that physics-grounded trajectories provide stronger motion guidance than direct VLM predictions.

---


### 91. [COMPREHEND: Ultra-Fine-Grained Benchmark Understanding by Entailment Hierarchy](https://arxiv.org/abs/2611.04249)

**<font color=#1a73e8>作者：</font>** Sivaraaman Balakrishnan, Prakriti Shetty, Jeremiah Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding what kind of prompts users typically ask and how well an LLM performs on these prompt categories is crucial for LLM practitioners. The existing methods satisfy the demand by hierarchically clustering the user prompts and synthesizing the cluster names using an LLM to build a taxonomy. However, the cluster names from these methods are usually too general for humans to understand the detailed prompt distributions and identify the exact strengths and weaknesses of LLMs. In this study, we propose COMPREHEND, which automatically constructs an ultra-fine-grained entailment hierarchy for the prompts. The entailment hierarchy replaces the cluster names in the taxonomy with sentences to provide more precise cluster descriptions for more fine-grained categorization. Compared with EvalTree, a state-of-the-art taxonomy construction method, COMPREHEND improves an entailment/faithfulness metric from 22.6 to 41.7 and an informative metric from 16.3 to 39.1 in WildBench. Our experiments also show that the weakness report generated based on our entailment hierarchy is much more informative than EvalTree in terms of predicting the response scores in the benchmark. All the code is released in this https URL.

---


### 92. [Sketch-Omni: Instance-Level Sketch-Based Visual Prompting for Perception MLLMs](https://arxiv.org/abs/2611.04262)

**<font color=#1a73e8>作者：</font>** Dongyu Wang, Dar-Yen Chen, Zhiming Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable perception, from GroundingDINO to Rex-Omni, puts one model behind one prompt interface and returns coordinates for any localisation task. Every model in that line was built for photographs; none has been given a sketch. We present Sketch-Omni, to our knowledge the first perception MLLM built to work on sketches and from them. On a sketch, the sketch is the image, and text prompts detect, point, resolve object and spatial referring expressions, and ground affordances in it. From a sketch, the sketch is the prompt, and a drawing of one object localises that object in a photograph, even among several of the same category, a query that neither a category name nor a photo exemplar can pose. Two obstacles stand in the way. A photo-trained model's attention is tuned to colour and texture, which a sketch does not have, and no dataset pairs a drawing with the one instance it depicts among others of its kind. We build the training data instead of collecting it. An edge detector turns every labelled photograph into a sketch-like drawing that keeps the photograph's labels, and two constructions produce sketch-to-photo instance pairs from existing data. On top of this, photo-guided relation alignment passes each photograph and its edge sketch through the same model and trains the sketch pass to reproduce how the photograph pass relates phrases to patches and patches to each other. Not one training label is drawn by hand. Sketch-Omni reaches 91.4 F1 on sketch-prompted localisation against 81.8 for the strongest general-purpose MLLM, with a lead that doubles when the photograph holds several instances of the queried category, and it is best in 39 of 40 evaluation cells across six tasks. Code, model, and a hand-annotated benchmark of 2754 sketch-to-photo links will be released.

---


### 93. [Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop](https://arxiv.org/abs/2611.04268)

**<font color=#1a73e8>作者：</font>** Zhuoran Zheng, Doubao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can an LLM directly edit the weights of a diffusion-based image-restoration model to \emph{improve} restoration quality---without gradients, paired data, or fine-tuning? Recent experiments show frontier LLMs can fix structural bugs by modifying as little as \(0.016\%\) of parameters, but cannot instill new capabilities. We ask whether weight-space programming (WSP) can move from \emph{debugging} to \emph{improvement} in the precise-regression setting of image restoration (deblurring, super-resolution, denoising, inpainting). Restoration diffusion UNets present a middle ground: low-level signal-processing layers are concentrated enough for targeted weight-direction edits, while high-level semantic layers remain distributed and resistant to sparse modification. We propose three technical conjectures: (C1) an LLM can localize the layer behind a quality gap (over-smoothing, color shift, hallucinated texture) within a 200 forward-pass budget; (C2) editing a small set of identified weight directions (e.g., scaling high-frequency filter norms, correcting output-bias channels) can measurably improve PSNR and perceptual quality; (C3) a recursive loop---diagnose \(\rightarrow\) edit \(\rightarrow\) evaluate \(\rightarrow\) re-diagnose---can compound gains across rounds, forming a minimal recursive self-improvement (RSI) loop for vision. We analyze the required AI capability (arguing targeted edits need not superintelligence, while general capability generation does) and detail the challenges of precise pixel-level regression. We provide a PyTorch-style deployment pipeline and outline a benchmark. This manuscript is conjectural, intended to open a new subtopic for image restoration.

---


### 94. [Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277)

**<font color=#1a73e8>作者：</font>** Kangning Zhang, Wenxiang Jiao, Bowen Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failures of a base execution system through sibling harnesses and transfer the resulting capabilities into a single policy that remains effective under the original harness. Directional Harness Evolution develops specialized sibling harnesses along distinct repair directions, forming a reusable Sibling Harness Pool that remains fixed during policy training. Complementary Harness Rescue Training invokes this pool only when all initial attempts under the base harness fail. The same policy generates fresh rollouts under selected auxiliary harnesses, and these trajectories replace the failed group for reinforcement learning. An Adaptive Harness Router selects the Top-k variants using Harness Behavior Profiles and voting across multiple LLMs. Policy-aware profile re-anchoring refreshes this evidence as the policy learns. Across AppWorld, SWE-Gym, and DBBench, the trained policy substantially outperforms policy-only training when returned to the original base harness. Behavioral analyses and held-out cases support the transfer of harness-elicited behaviors into the policy itself. Reusing the router for Rank-1 inference provides additional gains at the same executor rollout count.

---


### 95. [GroundSeek-CXR: Retrospective Evaluation-Guided Active Observation Framework for Multi-Label Chest Radiography Diagnosis](https://arxiv.org/abs/2611.04286)

**<font color=#1a73e8>作者：</font>** Yihang Fu, Xinyu Liu, Qing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest radiography (CXR) diagnosis is critical for thoracic disease assessment, yet challenged by the need to identify subtle lesions and co-occurring abnormalities across regions. While recent vision-language models can actively observe local regions, existing preference-based methods supervise each observation by its immediate effect on the current diagnosis, failing to capture how each observation and stopping decision contributes to the final diagnosis. To address this issue, we propose GroundSeek-CXR, an active CXR diagnosis framework that learns observation and stopping decisions by retrospectively evaluating them with the final diagnosis. Specifically, we first devise a Retrospective Diagnostic Evaluation (RDE) that scores observation and stop candidates from offline Monte Carlo tree search through independent continuations. Moreover, we design a Retrospective Gap-weighted Preference Optimization (RGPO) that learns from retrospective-score preferences weighted by their score gaps, prioritizing actions that improve diagnostic accuracy. Extensive experiments demonstrate that our GroundSeek-CXR framework outperforms state-of-the-art methods, and improves abnormal-image sample-F1 by 4.48% over immediate-score preference learning.

---


### 96. [Can Benign Skills Induce Misaligned Behavior in LLM Agents?](https://arxiv.org/abs/2611.04299)

**<font color=#1a73e8>作者：</font>** Xuanye Zhang, Yongsen Zheng, Kaiyu Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on reusable skills to plan tasks, invoke tools, recover from errors, and complete workflows without modifying model parameters. Although these skills are typically developed to enhance benign tasks, they may also make an agent more capable of executing procedures for harmful purposes. We study this risk, which we call skill-induced behavioral misalignment: adding benign skills may cause an agent to execute external actions that violate safety requirements.
We first conduct a systematic study to validate the existence of this phenomenon. It compares agents with and without benign skills across five LLM backbones and three benchmarks under matched requests. On average, skill augmentation improves benign task accuracy by 10.3 percentage points (pp), but also increases unsafe action rate (UAR) by 10.3 pp. The regression also occurs with skills curated by experts. A paired trajectory analysis shows that 24 of 50 newly unsafe trajectories fail to complete the harmful objective, revealing violations that task completion alone would miss.
We further disclose multiple factors and scenarios that could exacerbate this risk. (1) Evolving skills with benign feedback can amplify unsafe execution; (2) This regression is more pronounced when retrieved skills are matched to task and contain procedural guidance; (3) Distilling benign experience into reusable skills yield higher UAR compared with their source trajectories. (4) A guard that checks proposed tool actions before execution reduces violations while retaining gains on benign tasks. All these findings confirm the significance of skill-induced behavioral misalignment, and the urgent need for new mitigation solutions.

---


### 97. [OSGR: Observation-Support Graph Reasoning for Earth Observation Question Answering](https://arxiv.org/abs/2611.04301)

**<font color=#1a73e8>作者：</font>** Dazhou Yu, Zerong Wang, Riyang Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Answering geographic queries over Earth observation (EO) archives requires solving a joint retrieval-and-derivation problem under strict spatiotemporal constraints. Existing LLM agents fail to ground observation items or suffer from search-space explosion. We propose OSGR, a two-stage framework that factorizes this search into offline symbolic concept deduction and online Relation-Conditioned Grounding. OSGR leverages an offline Observation-Support Graph to deduce valid target-to-result support paths at the concept level, and applies spatiotemporal compatibility kernels to instantiate grounded observation-item sets. On Earth-Bench and DisasterM3-Reason, OSGR improves GPT-4o accuracy from 49.3\% to 63.7\% while reducing the execution-step ratio from 2.9 to 2.5.

---


### 98. [FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing](https://arxiv.org/abs/2611.04303)

**<font color=#1a73e8>作者：</font>** Zhixian Li, Xingsong Ye, Yongkun Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-image machine translation (IIMT) replaces text in an image with its translation while preserving the surrounding visual context. Existing task-specific models achieve convincing performance but require massive paired training images before and after translation. As advanced text-to-image (T2I) models have reached a practically usable level of multilingual text generation, we argue that this capability can be transferred to IIMT and present FlowTranslator. It is a training-free IIMT framework that first employs an OCR model and an LLM to generate the translation prompt, which is injected into the T2I-based diffusion model. To optimize the accurate and natural generation of translated text, we introduce two trajectory controls: Region Coupling Release (RCR) partially decorrelates target-branch noise inside the text region early in the trajectory, while Coupling Expansion (CE) amplifies the emerging edit displacement mid-trajectory. Under the EasyOCR read-back protocol, FlowTranslator achieves average PRIM BLEU and COMET scores of 20.6 and 57.2, respectively, substantially outperforming the strong training-based baseline UniTranslator. On the more challenging and realistic whole-image ScenePair photographs translated into Chinese, it reaches 40.1\% exact-match accuracy and surpasses existing editing systems, some of which only address the text-rendering stage rather than the complete IIMT task. These results establish flow-based editing as a strong, fully training-free baseline for IIMT.

---


### 99. [Coarse Semantic Blocks for Efficient Training-Free Sparse Attention](https://arxiv.org/abs/2611.04313)

**<font color=#1a73e8>作者：</font>** Sosuke Kobayashi, Shoichiro Yamaguchi, Seiya Tokui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a training-free sparse attention method that builds a prompt-specific key index to accelerate both prefill and decoding. The method clusters the keys into large semantic blocks that group tokens from noncontiguous positions. Each query position selects blocks by scoring their centroids and attends to the original keys and values within them. Queries that select the same block are processed together, so prefill stays fast even though each query chooses its own blocks. Large blocks make centroid scoring and this grouped processing cheap, so each query can attend to more tokens in the same time. Larger blocks with a larger token budget can thus be both faster and more accurate on long-context tasks than smaller blocks with a smaller budget. We evaluate two hybrid LLMs, Qwen3.5-4B and 35B-A3B, on one NVIDIA H200. Including the cost of building and using the index, whole-model wall-clock speedups over dense attention are 2.3-2.4x for prefill and 1.7-2.0x for decoding at 512K tokens, and 2.9-3.0x for prefill at 1M. The 35B-A3B model stays close to dense attention on five RULER tasks through 1M, on LongBench-v2 overall, and on MRCR through 256K. The 4B model loses accuracy mainly on multi-key retrieval, yet outperforms dense Qwen3.5-2B, whose latency is similar at 512K, on all three benchmarks.

---


### 100. [Planning-Coding Separation in LLM-Based Code Generation: An Empirical Study](https://arxiv.org/abs/2611.04320)

**<font color=#1a73e8>作者：</font>** Wentao Wang, Zeyu Sun, Ruwei Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning has been identified as an important factor for improved code generation with Large Language Models (LLMs). However, the interaction between planning capability and coding capability remains largely underexplored, especially when the two capabilities are from different LLMs. In this paper, we conduct the first comprehensive empirical study of planning-coding interaction in LLM-based code generation, where planning and coding are assigned to different LLMs (i.e., planning-coding separation). Specifically, we explore different planner-coder combinations to investigate the effectiveness for coders to utilize planning information from various planners and the impact of further training of coders on planner-coder combinations. Our results demonstrate that almost all planner-coder combinations are as competitive as using the same LLM for planning and coding, and the combination of a stronger planner and a stronger coder typically achieves improved effectiveness. Furthermore, using a large model as the planner paired with a much smaller model as the coder can sometimes be as competitive as using the large model as both the planner and the coder, and further training of the coder can typically boost various planner-coder combinations. These findings provide empirical evidence that planning and coding can be separated to a considerable extent in LLM-based code generation, which may offer a more flexible way to construct code-generation systems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
