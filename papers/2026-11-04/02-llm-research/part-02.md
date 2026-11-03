# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 51. [Fidelity Collapses with Table Size, Not Turn Count: Delivery Architecture in a Deployed Tool-Using Agent](https://arxiv.org/abs/2611.00442)

**<font color=#1a73e8>作者：</font>** Tung Thanh Hoang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a multi-turn agent delivers a tool's structured records into the model's context and re-emits them each turn, every turn can corrupt data the tool computed correctly. We measure this in a production award-travel agent: two architectures over identical frozen payloads, lineage-matched prompts and sampling, differing only in delivery architecture. SYNTHESIS feeds full record sets into the planner's context and answers follow-ups in-head; BYPASS, the deployed system, keeps records in session state, translates follow-ups into arguments for a deterministic filter, and delivers rows over a typed side channel. Across 24 dialogues (339 scored turns per condition), BYPASS scores 92.3% of turns fully correct, SYNTHESIS 45.7% (paired gap +46.6pp [+35.7, +57.1]). Varying delivered-table size by capture date, SYNTHESIS collapses from near-perfect at 10 rows or fewer to 8% or less beyond about 74 rows. On a content-controlled prefix ladder the collapse threshold orders by model capability, from under 10 rows (GPT-4o-mini) to about 198 or more (Gemini 2.5 Pro), while BYPASS stays size-flat for all four models. The collapse is expensive: beyond 100 rows, where almost no SYNTHESIS answer is correct, each correct one costs roughly 200x BYPASS's flat \$0.012. Practitioners converged on typed side-channel delivery for rendering, not correctness; we show it was, unknowingly, also a correctness decision.

---


### 52. [CLiS: Plug-and-Play Attention Acceleration for Video Diffusion on TPUs via Certified Stabilization](https://arxiv.org/abs/2611.00444)

**<font color=#1a73e8>作者：</font>** Elisa Tsai, Shao-yu Huang, Daniel Mandragona 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution video diffusion relies on attention over long token sequences, making attention efficiency critical to generation latency. Our analysis identifies repeated maximum reductions and accumulator rescaling in online softmax as a bottleneck in long-context TPU attention. We propose CLiS (Certified Loop-invariant Stabilization), a training-free, plug-and-play optimization for video diffusion inference. CLiS fixes per-row stabilizers before the KV loop and certifies numerical safety per head, falling back to online softmax when certification fails. It integrates into existing fused-attention kernels without changing model weights or architecture. On Wan 2.2 and LTX-2 across TPU v6e and TPU7x, CLiS reduces diffusion transformer (DiT) step latency by up to 19.6% relative to tuned online softmax without measurable quality loss. Controlled TPU adaptations of prior GPU stabilization methods show performance or numerical-safety limitations. Preliminary causal LLM experiments also show up to 13.5% higher training throughput in continued pretraining and 7.7% in supervised fine-tuning.

---


### 53. [Quantiles, Not Points: Streaming Quantile Matching for Ordinal-Aware LLM-as-a-Judge Calibration](https://arxiv.org/abs/2611.00447)

**<font color=#1a73e8>作者：</font>** Ilija Subasic, Andrew Rabinovich, Zhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge scores are often distributionally shifted from human ratings on any given evaluation task, and post-hoc calibration (mapping LLM to human scores in a small labeled anchor set) has become a popular method to correct for this shift. In this paper we derive the calibration from two positions: that LLMaJ scores are ordinal ratings drawn from a distribution rather than isolated points. We present streaming quantile matching (SQM), a version of a classical method not previously bench marked for LLMaJ calibration, which is built on the two positions by computing the optimal-transport map between the LLM and human score distributions. We develop an evaluation framework and within it we show that unlike point-wise calibrations, SQM respects the ordinality of the human anchor set and achieves the best distributional fidelity and the top overall rank across models and data. We also show that in general, post-hoc calibration narrows the raw error gap between smaller and larger judge models, which opens the possibility of more efficient LLM judges.

---


### 54. [From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory](https://arxiv.org/abs/2611.00450)

**<font color=#1a73e8>作者：</font>** Changjiang Han, Bowei He, Ye Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) helps large language models (LLMs) answer factual questions beyond their training data, but it adds storage and inference costs. Distilling previously retrieved information into parametric memories enables reuse without online retrieval. However, training the memory to mimic a retriever rewards accurate independent predictions, which do not necessarily improve the final output quality when combined with the LLM's existing predictions. To address this, we introduce ResMem, in which the LLM reads retrieved text offline to generate teacher targets. This design avoids storing massive token representations, unlike existing parametric memory approaches such as MLP Memory, which relies on k-nearest neighbor (kNN) datastores. Furthermore, by using the LLM as an offline teacher that reads privileged retrieved evidence alongside the input, we train a parametric memory to learn an additive logit residual. This residual aligns the predictions of a student sharing the same backbone with the teacher distribution, while self-distillation updates remain confined to the parametric memory. On a Wikipedia subset, ResMem reduces the storage retained for teacher construction by 94.7% compared with the evaluated kNN pipeline. Across five question answering datasets, ResMem raises mean token F1 from 32.83% for the frozen LLM to 34.48%. It also breaks 21% fewer of the LLM's correct answers than a kNN-trained memory. These findings validate our motivation of treating retrieval as a learning resource, with parametric memory shaped by how retrieved knowledge is used to inform the model's future predictions. Code and model weights are available at this https URL and this https URL.

---


### 55. [PRISM-Net: Dynamic Routing Network with VLM-Guided Disentangled Attribute Distillation for Explainable Fine-Grained Product Retrieval](https://arxiv.org/abs/2611.00458)

**<font color=#1a73e8>作者：</font>** Chung-Ming Lo, Che-Wei Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual product retrieval in large-scale e-commerce multimedia systems demands discriminative representations capable of simultaneously resolving macro-level category semantics and micro-level visual attributes such as structural contour (line) and chromatic appearance (color). However, conventional backbones including convolutional neural networks (CNNs) and vision Transformers (ViTs) inherently suffer from feature entanglement and shortcut learning. To learn the micro-level visual attributes without costly manual attribute annotations, we propose phase-routed interpretable semantic mixture-of-experts network (PRISM-Net), an explainable multi-expert architecture that disentangles holistic visual features into disentangled line and color expert pathways governed by a conditional meta-router. In phase 1, we introduce an external VLM-Guided sigmoid semantic distillation mechanism with gradient-detached routing gates, utilizing zero-shot text prompts from SigLIP to supervise specialized structural and chromatic experts. In phase 2, the disentangled expert embeddings are adaptively fused with macro base features via a learned meta-router gate to calibrate category boundaries. Extensive 5-fold cross-validation across 275,454 e-commerce images (18 categories) and full-scale retrieval benchmarks (55,091 queries against a 220,363-image gallery) across SwinV2, ConvNeXt-V2, and DINOv3 demonstrate substantial gains. On SwinV2, PRISM-Net boosts full-fold product mAP@10 from 80.98% to 83.90% (+2.92%), line mAP@10 by +5.74%, and color mAP@10 by +9.12%. Furthermore, unsupervised distribution analysis of the meta-router gate reveals that both ViT and CNN backbones emergently allocate up to 6.8x higher structural line weights to rigid appliances and hardware while dedicating >96% chromatic weight to clothing.

---


### 56. [From Small to Large: Assessing Medical Reasoning, Benchmark Contamination, and Model Size in Language Models](https://arxiv.org/abs/2611.00460)

**<font color=#1a73e8>作者：</font>** Navapat Nananukul, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) now answer medical exam questions at or above expert level, but it is unclear whether such scores reflect clinical competence, or are instead affected by the format of the questions being asked (e.g., multiple-choice versus open-ended), prior exposure to the benchmarks, and the difficulty of the questions. These benchmarks are also public and widely used online, which may be resulting in LLM memorization. Models may perform better on questions that they have seen before. It is also not evident whether smaller models, which are more locally deployable in HIPAA-compliant hospital settings, have achieved human performance. In this study, we evaluate fourteen current models from six leading providers, one smaller and one larger model from each provider with two additional open-weight models, on 3,076 questions from four medical benchmarks (MedQA-USMLE, MedMCQA, PubMedQA, and MedBullets) under standard multiple choice, the same questions with the answer choices withheld, and reconstruction of a hidden question from its choices alone. In the standard multiple-choice setting, the strongest models exceed the human-expert baseline on MedQA-USMLE and PubMedQA, but the smaller models trail their larger models by 8.7 percentage points and only two of the six pass the human-expert bar on the licensing examination. Withholding the answer choices, however, makes every model struggle: mean accuracy falls from 82.3% to 50.9%, and the two largest drops belong to the medically specialised models. On memorization, the strongest models reconstruct one question in four from the answer choices alone, yet accuracy holds on the questions they cannot reconstruct. We further weigh accuracy against inference cost and test whether ensembling several models improves medical question answering.

---


### 57. [Exo: An Architecture for Self-Improving Systems at Runtime](https://arxiv.org/abs/2611.00463)

**<font color=#1a73e8>作者：</font>** Alexander Krentsel, Sylvia Ratnasamy, Ion Stoica 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses govern how language models act in an environment; designing their policies by hand is difficult, while automated techniques require representative datasets and costly executions. We present Exo, an agent runtime architecture for safe learning during ongoing work that collapses the optimization loop into task execution, allowing agents to revise both their harness and their strategies for further improvement. A minimal protected mechanism layer preserves execution history and governs policy activation while the harness evolves through inspectable code changes. On long-running objectives in an open-world game, Exo reduces model cost by 12-53% relative to Codex and Pi in standalone runs and 45-82% in transfer runs, while matching task completion rates. Compared with the same starting policy without the ability to edit policy, Exo reduces held-out model cost by 35-61% on AppWorld and SREGym with comparable correctness, cutting AppWorld's mean task time by 13% and SREGym's median diagnosis time by 35%. On Continual Learning Bench coding tasks, model cost including learning falls by 14%, with both policies resolving every issue.

---


### 58. [Compression Technique Interactions in Small Language Models: A Factorial Ablation Study](https://arxiv.org/abs/2611.00464)

**<font color=#1a73e8>作者：</font>** Bhushit Nema, Siddharth Krishnamurthy, Anjali Kadiyala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying small language models on resource-constrained hardware requires compression, yet practitioners lack systematic guidance on how quantization, pruning, and post-compression recovery interact when combined. We present a factorial ablation study evaluating 72 compression configurations across four SLM architectures (2.7B-7B parameters), extended with a 48-configuration ordering analysis, benchmark accuracy validation on 30 compressed models, and robustness checks including multi-seed validation and full-corpus perplexity evaluation. INT8 quantization is effectively lossless (<0.5% accuracy degradation), while NF4 quantization combined with L1 magnitude pruning causes model collapse in all 16 tested combinations. LoRA-based fine-tuning reduces degraded perplexity by up to 97% after aggressive pruning; an ablation against standard fine-tuning without a teacher model shows the recovery is driven by LoRA adaptation itself rather than the distillation signal. Compression ordering shows no significant effect among viable configurations (ANOVA p = 0.96) but determines viability for NF4+pruning combinations. INT8 quantization alone provides 40-45% memory reduction with no quality loss. On-device CPU deployment via this http URL confirms these findings transfer off the GPU: 4-bit quantization runs 46-54% faster than 8-bit for a perplexity difference under 0.5 points, while un-structured pruning yields no CPU latency or memory benefit, consistent with its dense storage format.

---


### 59. [Steering Readerly Dynamics: Trajectory-Guided Story Generation with Large Language Models](https://arxiv.org/abs/2611.00469)

**<font color=#1a73e8>作者：</font>** Danrui Li, Yiwei Zhao, Mubbasir Kapadia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate stories, but these stories struggle to reproduce engaging readerly dynamics, the evolving reader responses that shape narrative experience. To address this challenge, we propose a framework that learns readerly dynamics from high-quality human-written stories and uses them to guide story generation. Instead of directly modeling high-dimensional story content, we train a small LLM to predict future reader responses as low-dimensional trajectories. We then leverage the strong instruction-following capability of a larger, off-the-shelf writer LLM to generate story segments that follow these predicted trajectories within a given story setting. Our framework improves trajectory-based fidelity to human-written stories by 12%-35% while largely preserving story coherence.

---


### 60. [Integer-Exact Microscaling: Running MXFP4 Language Models on INT8 Matrix Units](https://arxiv.org/abs/2611.00486)

**<font color=#1a73e8>作者：</font>** Shinyoung Kang, Junhyung Ahn, Yujun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On hardware whose fastest matrix datapath is INT8$\times$INT8, such as the Neural Accelerators of Apple's M5 GPUs, 4-bit weights must become INT8 operands. Existing MXFP4 kernels already map FP4 (E2M1) values to integers by doubling them, but apply every 32-element block scale inside the reduction. We show when no per-block work is needed: a row of MXFP4 weights is exactly one INT8 vector times one power-of-two scale if its block exponents span at most three, so a linear layer becomes a single INT8 GEMM with one rescale per output. Enforcing the condition adds at most 1/16 of a row's largest rounding error to the blocks it changes, and real weights already satisfy it: 97.9-99.97% of rows across seven models, including 99.93% of the 95M rows of a 125B-parameter mixture-of-experts (MoE) model, Qwen3.8-Flash-Next. The resulting spread-constrained MXFP4 files stay standard MXFP4. With integer instead of power-of-two block multipliers, an integer-exact format (16-wide blocks, multipliers 1..10, 4.26 bits) runs as one exact INT8 GEMM and is more accurate than NVFP4 (4.5 bits) with its standard scale rule on five small models, within 0.06 perplexity of NVFP4 with scale search. On Qwen3.8-Flash-Next's routed experts with INT8 activations it is as close to the FP8 model as NVFP4 with scale search (KL divergence 0.0557 vs. 0.0553) and closer than MLX's MXFP4 and affine INT4; with every matrix quantized it solves 94.8% of GSM8K vs. 91.0% for MLX's MXFP4. Quantizing only the 74k routed expert matrices (96% of the parameters) to either of our formats with INT8 activations costs at most 0.2% perplexity. A complete W4A8 system on the M5 produces outputs bit-identical to the quantized reference; prefill is 1.34-1.74x faster than MLX on a dense model, 1.10-1.57x on two MoE models up to 35B parameters and 1.22-1.29x on Qwen3.8-Flash-Next, where shared non-GEMM work bounds the gain.

---


### 61. [VoirDire: Counterfactual Calibration for Reliable LLM-as-a-Judge Aggregation](https://arxiv.org/abs/2611.00491)

**<font color=#1a73e8>作者：</font>** Changho Shin, Frederic Sala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge systems often aggregate multiple judges to improve evaluation reliability. However, judge agreement can reflect shared biases toward verbosity, formatting, or fluency rather than the intended evaluation target. Addressing these shared biases is challenging because observational judge outputs alone cannot distinguish agreement driven by target quality from agreement driven by nuisance attributes. We introduce VoirDire, an intervention-calibrated aggregation method for LLM-judge panels. VoirDire applies controlled interventions that vary specified surface attributes while aiming to preserve the evaluation target; it then uses paired changes in judge scores to identify nuisance-sensitive directions. It attenuates these directions and selects aggregation weights that retain variation across items while penalizing sensitivity to the interventions, making the final consensus less dependent on superficial features. We show theoretically that observational judge outputs alone cannot identify which shared direction is target-relevant, while paired interventions provide the contrast needed to identify nuisance-sensitive variation. We evaluate VoirDire on 12 datasets spanning continuous scoring, binary classification, and pairwise preference. Compared with the existing LLM-judge aggregation baselines, VoirDire reduces MAE by up to 26.8% on continuous-score tasks and improves accuracy by up to 5.3 percentage points on binary and preference tasks. These findings suggest that counterfactual interventions provide an additional means of improving the reliability and controllability of LLM-based evaluation beyond merely relying on observed judge agreement.

---


### 62. [Spotting the Artificial: Dialogic Humor Improvisation in Humans and LLMs](https://arxiv.org/abs/2611.00492)

**<font color=#1a73e8>作者：</font>** Lizeth Palacios Patiño, Ximena Gutierrez-Vasques, Daniel Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a methodology for investigating the differences between natural and synthetic language in a challenging setting: humorous improvisational dialogue. Our experimental setting compares human-produced comedy improvisations with the dialogues generated by LLMs in a multi-agent environment that we designed. The analysis combines automated linguistic measures with manual annotation grounded in Systemic Functional Linguistics (SFL).
The results show that, although LLMs can create coherent and creative scenes, they often fail to reproduce key characteristics of spontaneous spoken interaction. In addition, LLM-generated interactions display a strong tendency toward politeness and positive evaluations, contrasting with the broader range of attitudes found in human humorous improvisation. Our evidence highlights both the strengths and limitations of current LLMs in modeling dialogic humor and demonstrate the value of integrating linguistic theory with NLP methods for the analysis of machine-generated language

---


### 63. [Robustness Starts with the Objective: Designing and Certifying Robust LLM-Generated Heuristics](https://arxiv.org/abs/2611.00504)

**<font color=#1a73e8>作者：</font>** Pantea Karimi, Roozbeh Bostandoost, Dany Rouhana 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used to design heuristics for computer systems. However, most synthesis frameworks evaluate candidates by their average performance, which can mask severe regressions on specific workloads. Even adding adversarial training inputs doesn't eliminate these regressions, and percentile objectives (e.g., optimizing for the 95th percentile) overlook how severe regressions can be beyond the selected threshold.
We present TAILOR, a framework that guides LLM synthesis using the Conditional Value at Risk (CVaR) of the cost difference between each candidate and an existing baseline on the same workload. This paired CVaR measures the average difference over the worst fraction of workloads. We show that a negative paired CVaR guarantees improvements in both average performance and tail optimality gap relative to the unknown optimum, without ever computing that optimum.
We find that TAILOR achieves the best mean--tail trade-off among the synthesis objectives we evaluate across three case studies: Azure GPU batch admission, Azure VM packing, and server placement. Tested across seven diverse optimization benchmarks, TAILOR produces heuristics that are certified with 99% confidence to improve both average performance and tail optimality gaps over the baseline in six of them. On these six benchmarks, TAILOR also outperforms known robust, human-designed alternatives in the tail while achieving better or comparable average-performance improvement over the baseline.

---


### 64. [To Jev or Not to Jev: When Can System-1 Decision Models Replace LLM Judges?](https://arxiv.org/abs/2611.00505)

**<font color=#1a73e8>作者：</font>** Shreyas Subramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models such as TypeSafe's Jev answer typed questions about a text (yes/no, multiple choice, or an ordinal score) with calibrated probabilities in a single forward pass and without generating text, which makes them an inexpensive candidate for LLM-as-a-judge workloads. We evaluate 14 System-1 decision models, selected with a pre-stated protocol, against four generative judges (Claude Haiku 5.5, GPT-5.6 with and without reasoning, and Claude Opus 5.5 with thinking) on eleven established judge benchmarks. Five of the 14 are statistically indistinguishable from GPT-5.6 without reasoning on all five pairwise and best-of-4 benchmarks, and the two strongest, DReX-Max and d1-ultra, are significantly more accurate than Haiku on JudgeBench, LLMBar and RewardBench 2. Conditioned on a reference answer generated once per prompt, eleven models reach 90.3-93.4% on JudgeBench, statistically indistinguishable from Opus 5.5 and GPT-5.6 with reasoning, and on PPE best-of-16 every reference-guided System-1 judge matches GPT-5.6 with reasoning at roughly one-sixteenth of its cost per prompt. Several System-1 judges are better calibrated than every generative judge and correlate more strongly with human helpfulness ratings. Robustness to instructions injected into the judged response is a property of the individual model rather than of the System-1 design: an appended note to the evaluator reverses 0-5% of the correct verdicts of five models but 17-49% for the other nine. Two general System-1 leaderboards that contain no judging tasks predict judging accuracy (Pearson r = 0.95-0.96), a well-calibrated System-1 first stage matches Opus on LLMBar while escalating 17% of items, and same-size controls show that the correctness deficit of a 4B decision model is a reasoning gap rather than a size gap.

---


### 65. [Selecting or Solving? What Best-of-N Verification Delivers in Video Reasoning](https://arxiv.org/abs/2611.00507)

**<font color=#1a73e8>作者：</font>** Martin Q. Ma, Yuxiao Qu, Ruslan Salakhutdinov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answering a complex question about a long video is a grounding problem: the answer turns on a few seconds of evidence, and vision-language models remain well below human accuracy at finding them. The standard way to spend extra test-time compute on this kind of video reasoning is best-of-N selection: sample several chain-of-thought answers from a fixed model, then let a second model re-watch the video and pick one. Such pipelines are reported by a single headline number, their margin over a majority vote. That number conflates two effects with opposite deployment consequences: the benefit the second model adds by selecting among candidates, and the benefit it would have supplied by solving the question itself. We separate them, measuring the Selection Increment (SI) -- selection accuracy minus the same verifier's accuracy with the candidates withheld -- alongside the margin over self-consistency, across five long-video benchmarks. The Selection Increment is largest for the weakest verifiers: a verifier that solves poorly on its own leaves the candidates the most room to help. Beating the majority vote follows the opposite profile: where the vote already sits near its ceiling no verifier we test improves on it; below that ceiling only the strongest do. On Video-Holmes, the two come apart on a single pool of candidates -- a weak verifier gains +19.3 points from the candidates yet lands 7.1 points below the vote, while the frontier verifier gains the least and beats the vote. The weakest verifier also shows a failure mode: on EgoSchema it picks by where an option sits in the list rather than by what the video shows. Read as a merit score, SI puts a verifier that fails to beat a majority vote at the top of its ranking; read as an audit, it says which of the two effects a headline number delivers. Code is available at this https URL.

---


### 66. [AStockArena: Beyond Returns, Can We Entrust Real Capital to the Decisions of Financial Agents?](https://arxiv.org/abs/2611.00515)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Sing Kwong Lai, Xuanzhi Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in dynamic financial trading, yet real-time trading benchmarks mainly evaluate agents by cumulative returns and risk-adjusted performance. Such outcome metrics cannot show whether trades are faithfully reported, supported by available evidence, and consistent with account states. We introduce AStockArena, a real-time decision-auditing benchmark for continuous trading in China's A-share market. Under shared market conditions and execution constraints, we evaluate 13 open- and closed-source models over 3,198 sequential decisions. AStockArena reconstructsthe actions actually posted to accounts by aligning reports, trade requests, execution responses, and account states, and audits them with eight checks spanning execution traceability (O), evidence sufficiency (RK), and financial meta-awareness (B), combining record verification with consensus expert annotation. Of 1,070 trading points, 72.99% exhibit at least one audit gap; model-level rates range from52.2% to 91.2%, with evidence gaps most prevalent. Historical trade-filtering replay further shows thatportfolio outcomes are sensitive to these flagged trades. Decision-process auditing thus offers a verifiable complement to return-based evaluation of financial agents.

---


### 67. [Agentic Context Management for Multi-Turn Human-AI Conversations](https://arxiv.org/abs/2611.00518)

**<font color=#1a73e8>作者：</font>** Matthew Ho, Chenglong Wang, Baolin Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs degrade in multi-turn conversation partly because of context pollution: the model's own earlier outputs stay in context and anchor later turns, so an early misreading of the user's intent can persist after the user corrects it. Assistant omission (AO), dropping every assistant message, removes this pollution but fails when interaction is referential: later turns refer back to drafts, decisions, and tool-call results that exist only in assistant turns. We propose Agentic Conversation Context Curation (AC3), a training-free method in which a separate analyzer (1) consolidates the task specification from the user's messages alone, (2) audits the assistant's prior outputs against it, and (3) edits the context, either appending the analysis or discarding the assistant side and rebuilding the context from the specification. A second finding: pollution is contagious. An analyzer that sees the assistant's reasoning while extracting the specification can do worse than no intervention, and instructing it to ignore them did not close the gap, so we exclude assistant turns structurally. On Lost in Conversation (replaying difficulty-selected instances), where AO is an oracle by construction, AC3 closes 55-84% of the gap between full context and AO on three of four tasks and exceeds AO on the fourth, and an LLM that faithfully summarizes the history does not reproduce the gain even with more compute. On real WildChat conversations, a GPT-5-mini judge prefers AC3's next turn over both full context and AO in every configuration of our main table, though this preference depends on the judge; on CollabLLM results are mixed. In stateful tool use (tau2-bench), AO collapses to 0% on every model; AC3 does not collapse, though it falls slightly behind full context. Detector studies show that Reset removes injected pollution but is not span-selective: the gain comes from rebuilding the specification.

---


### 68. [Dual-Axis Policy Entailment: A Benchmark for Policy-Change Reasoning](https://arxiv.org/abs/2611.00536)

**<font color=#1a73e8>作者：</font>** Charles Chang, Yuen Yuen Ang, Bolun Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether a policy shifts domains and, by extension, continues, broadens, narrows, or reverses previous policy is of paramount importance to the study of public policy. We propose Dual-Axis Policy Entailment (DAPE), which evaluates an ordered pair of policy directives on both dimensions at once: a binary judgment determines whether the two directives govern the same policy domain, and a five-way judgment determines whether the later directive continues, broadens, narrows, or reverses the earlier policy, or governs a different domain altogether. Read together, the two judgments form one five-category label, our primary metric. The two-axis design captures two central dimensions of policy change without conflating errors on either dimension into a generic "irrelevant" label, and it makes annotation more rigorous: a coder cannot dismiss a difficult pair as domain-irrelevant without an explicit, checkable decision. We introduce an expert-annotated benchmark of 1,000 ordered directive pairs drawn from a large corpus of Chinese government policy, together with an annotation-calibration protocol (an adjudication packet with pre/post agreement measurement) that we contribute as a methodological artifact. Fourteen open-weight models and four frontier API flagships fail the task zero-shot: even the best frontier flagship's chance-corrected agreement with expert labels is far below the human ceiling (Cohen's $\kappa \approx 0.29$ vs. $0.53$). A fine-tuned open-weight model (LoRA SFT of Qwen3-14B, five-fold cross-validation) closes this gap, reaching the coder-mutual human ceiling ($\kappa = 0.524$ vs. $0.527$). Finally, we apply our method to China's AI policy (1980-2024) and map the direction of policy change across eras.

---


### 69. [Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement](https://arxiv.org/abs/2611.00544)

**<font color=#1a73e8>作者：</font>** Hanrong Zhang, Minghao Liang, Jiawei Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents extend their capabilities with skills, each with a name, a description, and a body. Under progressive disclosure, an LLM router selects skills by name and description alone and loads only the selected bodies. Skill libraries grow continually as users and agents add new skills. Because the router relies on this metadata, a similar new skill can displace an earlier one, breaking previously correct routing even though the earlier skill and the router are unchanged. This routing interference is aggravated for public skills, whose descriptions may not match their bodies. We formulate the problem as lifelong skill routing, a class-incremental continual learning problem. A solution must keep earlier skills selectable without suppressing new ones. Existing approaches fall short, since continually retraining the router risks catastrophic forgetting and rewriting methods either ignore similar skills or require per-skill feedback. We therefore propose Skill++, which rewrites only the name and description of each incoming skill, without router training or labeled data. The new description states what the body supports, how the skill differs from its closest predecessor, and what related work it excludes. As a library grows to 731 skills over ten sessions, Skill++ selects all required skills for 76.3% of queries, versus 36.4% under the original metadata. Across three benchmarks and five LLM routers, it outperforms all compared approaches, and its gains carry over to the Codex CLI agent harness.

---


### 70. [Low-Margin Branch Points in Deterministic LLM Deliberatio](https://arxiv.org/abs/2611.00546)

**<font color=#1a73e8>作者：</font>** Hajime Shimao, Warut Khern-am-nua  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deterministic multi-agent LLM deliberation can exactly re- play a fixed transcript, yet exact replay alone does not test local resistance to controlled internal interventions. Because each response becomes context for later agents, a changed greedy token can redirect a transcript-mediated execution. We present a white-box audit of this local failure mode in a five-agent committee under greedy decoding. We prospectively select low- and high-margin token positions, require exact no-op re- play, inject norm-relative residual displacements, and measure first transcript divergence within ten generated tokens. Low- margin positions are more branch-sensitive than high-margin controls, while matched margin-reducing gradient directions branch substantially more often than margin-increasing con- trols. We then continue selected realized branches through the committee to distinguish textual persistence from preference and final-decision changes. The contribution is a controlled audit for local branch susceptibility in this specified protocol, not an estimate of deployment frequency, decision correct- ness, or a phenomenon unique to multi-agent systems.

---


### 71. [From Weeks to Hours: Fast and Principled SFT Data Generation for Reasoning LLMs](https://arxiv.org/abs/2611.00554)

**<font color=#1a73e8>作者：</font>** Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning-oriented post-training enables large language models (LLMs) to solve complex tasks via multi-step inference. Supervised fine-tuning (SFT) on high-quality reasoning traces is a particularly efficient approach, but its effectiveness depends critically on careful data curation. Existing pipelines rely on a costly generate-then-filter paradigm: large pools of long reasoning traces are produced by multiple teacher models and subsequently filtered for difficulty and diversity using additional LLMs, often requiring weeks of computation. In this work, we propose SFTProbe, a fundamentally different approach that bypasses this pipeline by directly predicting the quality of reasoning data.
We show that a brief LoRA-based adaptation, combined with evaluating loss on only 5% of each reasoning trace, suffices to estimate both difficulty and diversity. SFTProbe is grounded in a geometric view of post-training, where pretrained LLMs lie in a low-rank, anisotropic loss basin. By probing this basin via low-rank perturbations, we construct compact loss signatures whose clustering captures diversity, while loss at curvature inflection points provides a robust proxy for difficulty. We also provide a simple criterion for teacher selection. Empirically, our approach reduces data curation time from weeks to hours while maintaining or improving performance. Remarkably, on mathematical reasoning, 5k generated examples match the highly filtered 89k-example in OpenThoughts-Math dataset, and 7.5k generated examples outperforms it by 2.5% in accuracy. We further introduce a high-quality physics reasoning dataset, and use it to train a model that outperforms an IPhO 2025 silver-medal-winning model. The code and the dataset are released at this https URL.

---


### 72. [Distinguishing among reasoning levels of GPT 5.5 Pro via a grammar lens benchmark](https://arxiv.org/abs/2611.00555)

**<font color=#1a73e8>作者：</font>** Emma Graham, Richard Granger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Does the level of test-time processing effort affect a language model's computational capability? A formal grammar-lens benchmark method, derived from the theory of computation, generates novel data at specified levels, each successively more computationally powerful than the levels below. Using this data, we tested GPT-5.5, and GPT-5.5-Pro-Medium, -High, and -XHigh, showing incrementally increased acceptance of test data: 16, 40, 43, and 52\%, respectively, illustrating the benchmark's ability to discern fine-grained differences among models' added test-time reasoning levels. Additionally, as test-time compute effort increases, model responses diverge from human responses to the same data. This increasing disagreement may turn out to be broadly characteristic of more capable language models, introducing the potential of a general capability-versus-alignment conflict.

---


### 73. [WAR-CRAFT: Refining Web API Recommendations through Requirement Auditing](https://arxiv.org/abs/2611.00564)

**<font color=#1a73e8>作者：</font>** Zishuo Xu, Dezhong Yao, Zhiqiang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web API recommenders return a set of APIs for a mashup request but do not check it against provider documentation, the main public evidence of an API's capabilities. The set can therefore contain unsupported or redundant APIs and miss requested capabilities. Filling every apparent gap does not fix this, because a gap may already be served, may not need its own API, or may have no documented provider. We study post-recommendation refinement, which revises a frozen recommender's output using only the request, the catalog, and provider documentation. We propose WAR-CRAFT, which treats refinement as three decisions. An LLM removes unsupported or subsumed APIs by judging candidates jointly, then audits the remaining set against a requirement checklist derived from the request. For each uncovered requirement, a fine-tuned catalog-constrained Resolver proposes a catalog API or abstains, and an independent documentation check admits only supported proposals. On ProgrammableWeb with 7 heterogeneous upstream recommenders, WAR-CRAFT raises mean SetF1 from 0.558 to 0.644, above the strongest of 5 refinement baselines (62.5%), and roughly halves functional redundancy (0.127 to 0.065) without changing mean functional coverage. Gains range from +2.2 points on generative recommenders to +18.2 on fixed-cutoff rankers. At matched set sizes, WAR-CRAFT still outperforms truncating the upstream output, so the gain is not explained by set-size calibration alone. Our code is available at this https URL.

---


### 74. [Conic Certification of Transformer Attention](https://arxiv.org/abs/2611.00585)

**<font color=#1a73e8>作者：</font>** Masoud Ataei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention is the computational core of large language models, yet the verifiers that bound how far an attention head's output can move under input perturbations give no guarantee on how loose their bounds are. A weak certificate therefore cannot be told apart from a fragile model. We develop a conic programming theory of attention certification that supplies this guarantee. We prove that the difficulty lies not in the softmax but in the bilinear interaction of a varying query with the keys. This interaction makes certification NP-hard over boxes and inapproximable once the attention logits can move by a constant amount. A fixed query or listed token substitutions, by contrast, make the exact worst case efficiently computable. An exponential cone moment relaxation then certifies a head with an error bounded quadratically in the perturbation radius by computable quantities, an order that cannot be improved. We also show that relaxations that treat a network one operation at a time, linear bound propagation among them, pay on second-order terms a sum of per-operation maxima instead of one coupled maximum. Computational results on GPT-2 indicate that the theory carries over to a trained model. Against exact worst cases with the query fixed, the certificate attains the predicted second-order accuracy. It is tighter than linear bound propagation on every head, and the looseness of bound propagation tracks the predicted per-operation excess.

---


### 75. [TVP: TV is Almost All You Need for Speculative Decoding](https://arxiv.org/abs/2611.00588)

**<font color=#1a73e8>作者：</font>** Aaryam Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference with a drafter whose proposed tokens are verified by the target model in parallel. Under lossless speculative sampling, a draft token is accepted with probability one minus the total variation (TV) distance between the target and draft distributions, yet drafters are often trained with cross-entropy (CE) or KL. We first show that under matched and well-tuned training, TV matches or surpasses several published draft-training objectives when fine-tuning, and a fixed TV and KL mixture does the same when training from scratch. We identify two remaining problems, TV's vanishing gradients on undercovered tokens and the prefix products that starve later positions in acceptance-length objectives. To address both, we derive TVP, a loss family based on expected acceptance length, whose power parameter interpolates between coverage and acceptance oriented objectives. Annealing the power from zero to one gives the highest or tied-highest acceptance length across three drafter architectures and three target models, including longer drafts and block verification. TVP improves acceptance length over CE by 9.8% when fine-tuning, and over the public DFlash2 training recipes by 6.2 to 12.9%.

---


### 76. [Saidzoda-Tajik-E5-Large: Fine-Tuning a 560M Embedder for Tajik Retrieval](https://arxiv.org/abs/2611.00592)

**<font color=#1a73e8>作者：</font>** Tohir Saidzoda, Nekruz Maxudov, Bedil Karimov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Finding the passage that answers a question is the first step of most practical systems built on documents, and for Tajik we found no openly described model for it. We present Saidzoda-Tajik-E5-Large, a Tajik text embedder built from multilingual-e5-large-instruct (560M parameters). We asked our own Tajik language model to write questions for passages from Tajik laws, tax documents, Wikipedia and web text, and trained on 235,140 question and passage pairs for one epoch, with hard negatives chosen by another embedder and English and Russian pairs mixed in so the model would not forget those languages. On laws the model had never seen, the right passage is among the top ten results for 93.6% of questions, up from 80.2%; on tax documents, 94.5% against 82.6%. On Belebele, the one test we have that was written by people, the gain is smaller and not confirmed (92.2% to 95.2%, with touching intervals), and Russian and English do not change. On law and tax questions written in the same style as its training questions, it is tied with Giga-Embeddings-3B, a model five times its size; on Belebele the 3B and 8B models score slightly higher, and only after we fine-tuned them on our data are they clearly ahead. We also report what failed: training in bfloat16 broke the model, and replacing Tajik letters with similar Russian ones did not help. Our law, tax and Wikipedia test questions come from the same model that wrote the training questions, so we treat those scores as an upper limit until questions written by Tajik speakers are available.

---


### 77. [Do Orthogonality Constraints Help Language-Model Training Beyond Sphere Optimization?](https://arxiv.org/abs/2611.00593)

**<font color=#1a73e8>作者：</font>** Kai Hu, Li Zhang, Weichen Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of work reports benefits from orthogonality constraints in fine-tuning large language models (LLMs). These results raise an open question: do orthogonality constraints also help LLM pre-training? We conduct a systematic empirical study of decoder-only LLM pre-training with models ranging from 360M to 3.1B parameters, trained on nearly 200B tokens. We examine fourteen variants of orthogonality training: some constrain the weight matrix itself, while others use orthogonal factors to reparameterize it. Because a strictly orthogonal square matrix loses half of its degrees of freedom, we also study block-wise orthogonality, where every $d$ rows form a row-orthonormal (Stiefel) matrix and the block size $d$ is a hyperparameter. Among block sizes ranging from 1 to the shorter side of the matrix, no $d>1$ used throughout the network reliably outperforms $d=1$, and large blocks are clearly worse; the one placement that helps, symmetric positive-definite factors on the query and key projections, loses its small gain as models grow. At $d=1$, the constraint reduces to sphere optimization, with each row direction on its own unit sphere, which by itself already improves on tuned Muon. The same two findings hold for a diffusion transformer trained on ImageNet, and after fine-tuning, downstream accuracy does not separate the parameterizations. Our conclusion is that, across the realizations we tried, orthogonality between rows does not help language-model pre-training beyond sphere optimization. Since this appears to conflict with several prior results, we re-examine five prior methods in pre-training and fine-tuning that report orthogonality improvements. In each case the reported gain is attributable to numerical precision, training horizon, optimizer realization, or per-row norm control rather than to the orthogonality the methods impose.

---


### 78. [Multi-Estimate Elicitation Does Not Uniformly Debias Language Model Judgments](https://arxiv.org/abs/2611.00597)

**<font color=#1a73e8>作者：</font>** An-Sheng Jhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Does eliciting five weighted estimates within a single response change how a language model responds to information? Across anchoring, hindsight, base-rate, conjunction, and status-quo/default tasks, we compare direct numerical answers with a multi-estimate response format, contrasting source framings, explicitly random cues, and probability-consistency constraints. We evaluate three completed configurations--gpt-6.1-sol, claude-sonnet-5.5, and Qwen3-8B (reasoning disabled, analyzed descriptively). In the first two configurations, direct elicitation yielded near-zero irrelevant-anchor indices and status-quo effects, while remaining responsive to informative sources and informed advice. Of 23 preregistered confirmatory tests, six rejected after Holm adjustment; however, all six absolute point estimates fell below their prespecified smallest effect sizes of interest without establishing equivalence. Moreover, while separate versus joint elicitation shifted conjunction judgments, interpretation is constrained by between-call noise. Ultimately, multi-estimate elicitation failed to produce uniform debiasing or response attenuation across tasks and models, though post hoc correlations between candidate spread and anchoring error motivate independent predictive validation. Materials: this https URL

---


### 79. [Conversational Interaction for LLM-Based Clinical Text-to-SQL: A User Study with Healthcare Professionals](https://arxiv.org/abs/2611.00605)

**<font color=#1a73e8>作者：</font>** Jun-Min Lee, Suyoung Yoo, Gyubok Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational text-to-SQL interfaces could give healthcare professionals natural-language access to electronic health record (EHR) data, but evidence for their real-world usability remains limited: prior evaluations have relied largely on curated benchmarks with fully specified questions or on simulated users. We report a user study in which 14 physicians who regularly work with EHR data used both a single-turn and a conversational multi-turn text-to-SQL interface over the MIMIC-IV database in a within-subjects design; dialogue analyses additionally drew on interaction logs from 21 healthcare professionals across the main study and two pilot studies. The conversational interface was consistently favored: mean System Usability Scale scores rose from 68.2, near the industry average, to 85.9 (p<0.001), with significant advantages across technology-acceptance constructs including performance expectancy, effort expectancy, self-efficacy, and behavioral intention. In post-study forced-choice comparisons, 93% of participants reported greater overall satisfaction with the conversational interface, 86% preferred it for real-world adoption, and 71% trusted its results more; no participant preferred or trusted the single-turn interface more. Turn-level analysis of 425 logged user turns showed that freely composed queries triggered clarification requests in 24.8% of cases versus 1.8% for predefined, fully specified questions, and 64.3% of clarification episodes stemmed from EHR- or clinical-domain knowledge. Conversational interaction is a practical prerequisite, rather than a convenience, for natural-language EHR access. The frequent need for clarification in realistic clinical queries further underscores the importance of conversational interfaces, while benchmark-style evaluation can substantially underrepresent the ambiguity of real clinical use.

---


### 80. [Words Before Pixels: Selective Modality Routing for Vision-Language Model Unlearning](https://arxiv.org/abs/2611.00608)

**<font color=#1a73e8>作者：</font>** Laura Yao, Haochen Zhang, Jinhao Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) unlearning is often treated as an objective-design problem: given multimodal forget data, the goal is to optimize a loss that removes undesirable behavior while preserving retained capabilities. We argue that this view overlooks an equally important data-centric question: how should each forget example be represented before optimization? Existing methods typically keep image-conditioned failures in their original image-text form, implicitly assuming that pixels are the right route for unlearning whenever pixels appear in the input. We challenge this assumption by constructing modality-decomposed versions of VLM benchmarks, enabling controlled comparisons among image-only, text-only, and multimodal representations of the same examples. Our modality-mixing experiments show that unsafe instruction-following behavior is more effectively suppressed through textual representations than through images alone, while purely text-only unlearning can still weaken visual grounding when the target behavior depends on visual evidence. Motivated by this trade-off, we introduce ModRoute, a gradient-guided per-sample modality routing strategy that selectively converts high visual-pressure examples to text-only form while keeping the remaining examples multimodal. Notably, on VLGuard with LLaVA-1.5-7B, ModRoute has the strongest composite unlearning-utility score of 0.847 at $\gamma=0.5$, a 2.5% improvement over the best random-switching score and $\geq$46% better than pure multimodal or text unlearning. Overall, our results show that effective VLM unlearning depends not only on the objective, but also on the composition and per-sample modality routing of the unlearning data.

---


### 81. [Trail: Accurate Local Smart Home Control Using Decision Models](https://arxiv.org/abs/2611.00610)

**<font color=#1a73e8>作者：</font>** Maleeha Masood, Deepak Vasisht, Indranil Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language driven smart home control remains challenging: cloud-hosted Large Language Models (LLMs) raise privacy concerns, while local Small Language Models (SLMs) can generate invalid actions or misinterpret requests. We introduce Trail (Typed Registry-Anchored Inference for Language commands in Smart Homes), a fully local framework that replaces open-ended command generation with hierarchical typed decisions. Trail exploits the natural structure of a home's action space, selecting a room, device, and operation from candidates derived from the runtime device registry. This ensures valid actions while enabling confidence-based abstention when requests cannot be reliably resolved. We also design a structured memory module that uses typed decisions to support user preferences, device references, and multi-turn interactions. To evaluate Trail, we extend HomeBench and generate three datasets: Trek-Base, which tests natural-language variation; Trek-Robust, which evaluates robustness to changes in the home and its description; and Trek-Memory, which assesses conversational memory across multi-turn interactions. Trail achieves 85.3% accuracy on Trek-Robust versus 69.8% for a finetuned Qwen3.5-4B baseline, while remaining competitive on Trek-Base requests. With memory, Trail resolves 75.6% of the requests that depend on earlier turns, compared with 42.5% for the finetuned baseline given conversation history.

---


### 82. [Enhancing Language Model Reasoning with Structured Multi-Level Modeling](https://arxiv.org/abs/2611.00616)

**<font color=#1a73e8>作者：</font>** Siheng Xiong, Ali Payani, Faramarz Fekri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling enhances a model's reasoning by extending its chain-of-thought (CoT). However, existing approaches typically rely on a single policy trained with outcome-reward reinforcement learning (RL), which often suffers from long-horizon plan failures where the implicit plan drifts from valid strategies, especially for small LMs with limited capacity. To address this, we propose Multi-Level Reasoning (MLR), which reformulates long-CoT generation as a two-level stochastic process. A high-level planner generates structured step descriptors specifying both the reasoning mode and the semantic subgoal. The low-level executor then produces detailed reasoning conditioned on these descriptors, forming an alternating plan--execute loop. To maintain scalability, we adopt a minimal design where the base model serves as the low-level policy and a lightweight LoRA module implements the high-level policy. For training, we observe that outcome-reward RL provides sparse and delayed feedback for long trajectories (e.g., several thousand tokens), hindering credit assignment. We therefore introduce iterative Step-DPO, a process-level preference optimization scheme that leverages Twisted Sequential Monte Carlo (TSMC) to provide scalable stepwise supervision. This yields more effective training, improved stability, and higher accuracy. Extensive experiments on challenging math, science, and logical reasoning benchmarks show that, under the same reduced data budget (10% SFT and 5% preference relative to the DeepSeek-R1 distillation setup), MLR outperforms both SFT-based distillation and strong RL/preference-optimization baselines across multiple base models and tasks. Moreover, MLR exhibits slower performance degradation on long-horizon reasoning, demonstrating stronger robustness under extended CoT generation.

---


### 83. [Words Caught in the Heart: Simulating Person-Specific Expression for Self-Opaque Clients in Psychotherapy](https://arxiv.org/abs/2611.00617)

**<font color=#1a73e8>作者：</font>** Mengxi Xiao, Jingjing Chen, Ziyan Kuang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Psychotherapy clients may experience distress before they can coherently describe it, and their expression changes with emotion, perceived safety, and trust. Large language model-based client simulators often rely on clinically organized case descriptions, which can encourage responses explaining the client's difficulties more clearly than their current understanding warrants. We propose Pandora, a psychotherapy client simulation framework that models how psychological experience becomes situated, individual expression. Pandora updates psychological and relational states in response to therapist interventions, constructs subjective appraisals and attributions, and plans response content and strategy. A separate expression planner combines these decisions with language patterns distilled from the client's utterances to guide linguistic realization. We evaluate Pandora against five baselines on 115 cases from four counseling and motivational interviewing datasets. It achieves the highest expression similarity and overall disclosure-alignment score among the compared systems. In a four-evaluator study of 45 matched disclosure items, Pandora receives AI-like judgments in 7.2% of ratings, compared with 43.3--67.2% for the baselines and 35.6% without expression planning. The ablation also reduces expression similarity. These results support explicit expression planning in client simulation to improve alignment with individual language patterns and reduce perceived AI-like expression in the evaluated setting.

---


### 84. [TopoQuant: Topological Framework to Characterize Behavioral Shifts in Quantized Large Language Models](https://arxiv.org/abs/2611.00631)

**<font color=#1a73e8>作者：</font>** Baha Rababah, Shahzeb Qamar, Lorenz Sparrenberg 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) reduces the com putational cost of large language models (LLMs), but it can introduce internal structural and behavioral changes that are not captured by traditional metrics such as accuracy and per plexity. We present TopoQuant, a topological framework that uses topological data analysis (TDA) to quantify structural drift in self-attention weights and relate it to behavioral changes in quantized LLMs. Across four LLM families and multiple quantization levels, we show that topological drift remains stable at moderate compression levels but increases sharply below 4 bit precision, closely tracking declines in attention agreement. Our results reveal a strong relationship between topological drift and attention agreement, indicating that structural changes in model parameters closely reflect behavioral degradation under quantization. We further demonstrate that topological features can accurately predict attention consistency using lightweight machine learning models, achieving R2 scores of up to 0.85. Predicting attention agreement enables efficient assessment of be havioral consistency in quantized LLMs, allowing quantization induced degradation to be detected without running expensive downstream tasks. The results indicate that topological drift pro vides an efficient early-warning signal for quantization-induced degradation and can help identify safe compression limits without extensive downstream evaluation.

---


### 85. [Evidence-grounded large language models guide perovskite solar cell design and optimization](https://arxiv.org/abs/2611.00633)

**<font color=#1a73e8>作者：</font>** YanKai Chen, Zhi Wan, ZiHao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using large language models to interpret experimental evidence, design discriminating experiments and formulate well-supported mechanistic explanations remains a central challenge in materials research. Here we establish PSM-Bench, an 800-question benchmark developed by perovskite researchers to evaluate scientific reasoning in perovskite photovoltaics. We also introduce OpenPerov, an expert-informed language-model framework that learns from expert-calibrated evidence records reconstructed from 4,532 articles; these records link experimental strategies, controls and observations to mechanistic interpretations. Structured-evidence adaptation outperformed conventional question-answer training, and OpenPerov Flash ranked first among 13 closed-book systems. OpenPerov Pro raised Scientific Mastery further, from 87.6 to 89.1, by revising selected passages with retrieved evidence. On questions derived from subsequent studies, both models also outscored expert-authored answers. In an experimental test of self-assembled monolayer design, OpenPerov selected a K analogue that outperformed the Na analogue preferred by experts. Devices incorporating the selected contact reached a power conversion efficiency of 27.05% and retained 96.74% of their steady-state reference efficiency after 1,000 h of dark thermal ageing at 85 $^\circ$C. These results show that reconstructed scientific reasoning provides an effective basis for building domain models that interpret experiments and inform materials design.

---


### 86. [ElectroChemLLM: A Multimodal LLM Pipeline for High-Fidelity Electrochemical Informatics](https://arxiv.org/abs/2611.00638)

**<font color=#1a73e8>作者：</font>** Dikshya Mohanty, Manoj Praveen Nandigama, Kuldeepsinh Raj 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Electrochemistry is central to solving many modern-day challenges, including energy storage systems for a sustainable future, and its advancement relies heavily on the data from past findings. Existing automated pipelines are limited by text-only architectures, context fragmentation, and numerical hallucinations - collectively preventing accurate, large-scale curation of property databases. We introduce ElectrochemLLM, a multimodal information extraction pipeline that jointly identifies structured electrochemical records encompassing electrolyte compositions, electrode materials, cell configurations, and their measured physicochemical properties from unstructured scientific PDFs at scale. By combining hybrid document parsing with vision-capable LLM orchestration, the pipeline extracts verifiable, structured data across text, tables, and figures. Evaluated on the battery-electrolyte subset of our manually annotated benchmark of 232 papers, ElectrochemLLM achieves an F-1 score of 0.97, and has been applied to curate ElectroChemDB, a structured database spanning 15,000 electrochemical research articles. We demonstrate the utility of this resource by training machine learning models for electrolyte property prediction, illustrating a complete pathway from unstructured literature to predictive materials discovery.

---


### 87. [Bridging Singular Learning Theory and Mechanistic Interpretability at the Billion-Parameter Scale](https://arxiv.org/abs/2611.00640)

**<font color=#1a73e8>作者：</font>** Ethan Ji, Wei Wang, Yizhou Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability (MI) explains a computation in a trained network by identifying the components and variables that implement it and testing them with interventions. Singular learning theory (SLT) describes the same network through the geometry of the loss around its parameters, summarized by the local learning coefficient. In pretrained language models the two have not been compared: SLT's estimates at this scale concern whole models or components whose roles were not independently established, and the estimator, which averages the loss over parameter settings drawn near the trained ones, has had no reference for how far those draws may move the parameters. We show that both are functions of one object, the map from a component's parameters to the model's predictions under inputs and interventions, whose first derivatives determine the Fisher information, the learning coefficient, and intervention effects, and whose higher derivatives add a quartic correction and pairwise terms. We test this correspondence in Pythia-1B on Dyck bracket matching at all 154 training checkpoints, against a five-stage circuit identified by interventions. We measure the local geometry of all 144 components inside the region where predictions are preserved, with the Fisher spectrum at every checkpoint, which gives the quadratic part of the learning-coefficient estimate at every temperature. Changes of the Fisher trace track changes of causal effect (median partial rank correlation 0.51), largely as a trend shared across the model, whereas the gain Fisher of a component's output and the large-temperature count are specific to the component. The count follows causal change across the population but not the growth of a formed circuit component. The quartic part is what a sampler that leaves the region registers beyond curvature. Pairwise interaction curvature tracks joint-ablation interactions.

---


### 88. [Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench](https://arxiv.org/abs/2611.00643)

**<font color=#1a73e8>作者：</font>** Shanglin Yang, Zhan Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM research-ideation systems aim for hypotheses that are both true and non-obvious, yet neither property can normally be checked. We build a testbed in which both can. Generators propose conditional interaction claims about two fully tabulated benchmarks, NAS-Bench-201 and HPOBench; every claim is verified exactly against the tables, and its non-obviousness is scored against a calibrated blind prior elicited from other LLMs. Excess truth measures how much more often a run's claims hold than this panel expects. Across a series of pre-registered stages with Claude and GPT generators, our main positive result is a simple two-stage step found by a harness optimizer: draft a large pool of claims, then select a subset in a separate call. For Sonnet on NAS-Bench-201, this step raised excess truth in every pre-registered test, including against a same-pool ablation that keeps only likely-true claims, without lowering precision. The gain comes both from credit for true claims and from avoiding near-miss false ones. In post hoc checks it held under every calibration, panel and truth rule we tried, and it exceeded random and type-filter selection from the same pools. Because kept claims recur across runs, the evidence weakens when runs and claims are resampled jointly, and it is not significant against Sonnet's own prior. Two secondary findings are also pre-registered. GPT makes real use of the results of cheap probes, beating shuffled and withheld controls, though not more efficiently than asking for more claims. Optimizing the harness for an LLM judge raised judge scores while sharply cutting precision for every generator.

---


### 89. [Heirloom: Carrying a Phone's Personalization Across Base-Model Generations](https://arxiv.org/abs/2611.00650)

**<font color=#1a73e8>作者：</font>** Zhuomin Chen, Jingchao Ni, Qingkai Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device language models can learn a user's preferences through adapters trained on private data. However, a base-model upgrade may change the layers or vocabulary, leaving the personal adapter incompatible. Replacing it with a non-personal adapter loses much of the personalization, while retraining requires retaining the user's labeled history. We present Heirloom, a system that transfers a personal adapter to a new base model on the phone without retaining labels. Heirloom uses the old personal model as a teacher, collecting its predictions on stored unlabeled inputs, vendor-provided prompts, or prompts generated by the new base. It then unloads the old base and trains an adapter for the new model to match those predictions, keeping only one base model in memory at a time. We evaluate Heirloom across three generation upgrades from two model families, an architecture-preserving refresh, and three personalization tasks. On movie tagging, migration from stored inputs maintains pre-upgrade accuracy and differs from labeled retraining by at most 1.7 percentage points across the three upgrades. On a phone's neural processing unit (NPU), a fixed-length migration for the 4B upgrade takes 38 minutes and consumes 20% of the battery end to end, making the stored-input setting feasible during overnight charging.

---


### 90. [Inference First, Training Underneath: Layer-Granular LoRA Co-Serving with LayerLoom](https://arxiv.org/abs/2611.00652)

**<font color=#1a73e8>作者：</font>** Zongpu Zhang, Yishu Yin, Xuehai Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving and fine-tuning a large language model on the same GPUs can turn the idle capacity between inference bursts into training progress, and low-rank adaptation (LoRA) makes this co-location cheap because both workloads read a single frozen copy of the base weights. The difficulty lies in the fine-tuning backward pass, which has no counterpart in inference. Current co-serving systems schedule backward work per serving iteration: each iteration carries a fixed backward budget, and requests that arrive in the meantime wait for it to finish, so fine-tuning dictates inference latency whenever load spikes. We observe that the backward pass of a LoRA microbatch decomposes into per-layer tasks over the same weights that the inference forward pass visits, which allows backward work to be scheduled at layer rather than iteration granularity. Building on this observation, LayerLoom attaches same-layer backward tasks to the inference forward pass and, at each layer, runs only as many of them as the latency slack of in-flight requests permits. To keep a ready task at every layer, LayerLoom maintains a wavefront of fine-tuning microbatches staggered across layers, and it bounds the wavefront's activation memory by offloading microbatch state to host memory and prefetching it ahead of the layer where the scheduler plans to use it. A fused kernel serves the paired forward and backward GEMMs from a single read of each base weight. Because all backward work of an iteration finishes within its forward pass, new requests join the next iteration as in continuous batching. On an RTX 4090 GPU running Llama-3.1-8B under a bursty production trace, LayerLoom raises joint SLO attainment by 13.5-21.8 points over prior works with fine-tuning throughput that is comparable or up to 12% higher, and it reaches the same training losses.

---


### 91. [GateTrim: Adaptive-Rank Quantization for Large Language Models](https://arxiv.org/abs/2611.00654)

**<font color=#1a73e8>作者：</font>** Hongwei Ren, Jincheng Ren, Yuchuan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce GateTrim, an adaptive-rank post-training quantization method for large language models that learns matrix-specific ranks through gate optimization and threshold-based rank selection. GateTrim standardizes the low-rank factors of a quantized low-rank--residual representation, learns a separate gate vector for each target weight matrix, and uses a shared threshold to automatically determine its retained rank. The resulting ranks can differ across matrices, and the compact quantized representations are subsequently reconstructed. We evaluate GateTrim under W4A8 on Qwen3-4B/8B/14B, Llama-3.2-3B-Instruct, and Llama-3.1-8B-Instruct. Across all five models, we observe a counterintuitive finding: increasing the threshold from $\tau=0.3$ to $\tau=0.7$ reduces the mean retained rank by 46.60%--67.89% while simultaneously lowering WikiText-2 perplexity by 0.59%--5.17%. Threshold 0.7 achieves the lowest mean retained rank and final perplexity among the three tested thresholds, 0.3, 0.5, and 0.7, and reduces measured target-export size by 1.50%--4.25% relative to 0.3. GateTrim uses an $8\times512$-token fitting pool and a separate development pool of the same size. Its Qwen3-4B/8B/14B perplexities at $\tau=0.7$ are numerically below TwinQuant's published W4A8 values, reported with a $128\times2048$-token calibration pool, in a cross-study comparison. On Qwen3-8B, the threshold-0.7 configuration already has the lowest perplexity before reconstruction under both tested initialization seeds; reconstruction improves it further without increasing retained rank or export size.

---


### 92. [Designing Behavioral Profiles for Language Model Simulation of Out-of-Distribution Human Behavior](https://arxiv.org/abs/2611.00661)

**<font color=#1a73e8>作者：</font>** Robin Na, Kehang Zhu, Logan Cross 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate human behavior, but which descriptions of people improve prediction when experimental designs change remains unclear. We develop a framework that draws candidate behavioral features from the literature and constructs profiles from earlier human experiments. A profile-generation LLM assigns feature values from observed actions, messages, and surveys; a separate LLM simulates behavior using these profiles. By comparing simulated and observed outcomes in the learning data, we select profile contents through forward feature selection, adding features while they improve prediction. We then evaluate the selected contents without modification against outcomes from new participants under new designs. Across 616 public-goods games, 144 multi-party bargaining games, and 1,480 generalized 11-20 money-request designs, leading one-feature profiles predict human outcome distributions better than no profile or general-purpose personas. Profiles with more features provide no clear additional benefit, and features' relative predictive value largely persists across learning and validation. Using profiles from one game family to simulate another produces uneven gains and can make predictions less accurate than simulations without profiles. The framework makes the choice of behavioral information a testable part of simulation design, helping researchers assess which descriptions remain useful as experimental conditions change.

---


### 93. [Audit at the Precision You Deploy: Quantization Reshapes a Subliminally Learned Preference](https://arxiv.org/abs/2611.00665)

**<font color=#1a73e8>作者：</font>** Md Rayhanul Masud, Mst Suraiya Akter Shefa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subliminal learning allows AI models to inherit hidden preferences from seemingly unrelated training data, such as number sequences. Safety audits may evaluate models at standard 16-bit precision, while deployments may use compressed, quantized weights. We ask whether quantization changes the expression of a subliminal preference and what drives any resulting change. To investigate, we implant a "favourite animal: panda" preference into Qwen2.5-7B-Instruct. We define its net strength as the difference in mean panda-answer probability between subliminal models and neutrally trained controls under the same quantization setting. Applying this metric across different compression levels reveals a stark contrast. While behaviour remains stable at 8 bits, 4-bit quantization triggers severe, opposing shifts depending on the quantizer. Half-Quadratic Quantization (HQQ) amplifies the preference, raising the subliminally trained model's panda probability from roughly 55% at 16 bits to 64% at 4 bits, while the controls stay near 17%. This raises the trait's net strength ~1.3 times its 16-bit value. In contrast, NormalFloat (NF4) at 4-bit suppresses it, shrinking the net strength to just ~0.3 times its 16-bit value, despite producing rounding errors of the same size to within 4%. We examine the structure of the rounding errors and find that their arrangement drives the divergence. Randomly shuffling HQQ's errors within each quantization group, without changing their magnitude, shifts the trait's net strength between 0.2 and 1.6 times its 16-bit value. Despite these opposing shifts, the underlying fine-tuning signal remains largely intact. Because a model's internal state and outward behaviour diverge so unpredictably under compression, a 16-bit audit cannot reliably bound real-world risks. Safety evaluations must test the exact quantized weights intended for deployment.

---


### 94. [Precedent Labels and Facts Shift LLM Approval Decisions in Opposite Directions](https://arxiv.org/abs/2611.00672)

**<font color=#1a73e8>作者：</font>** Junwei Yao, Zike Yang, Yongxi Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model decides refund or claim requests under written policies, the system can show it similar past cases. Each past case has two parts: its facts and the decision recorded for it. We separate the two. A model sees a policy, a request and three past cases, and we change either the recorded decisions or the facts, keeping the request fixed. We select requests that are close calls: deciding without past cases, DeepSeek V4.1 Flash approved each in some of four tries and denied it in others. When the past cases are near-copies of the request (its facts with a few details changed), switching their recorded decisions from DENY to APPROVE raises approval by about 30 to 55 percentage points in DeepSeek V4.1 Flash, GPT-5.6 Luna and Claude Haiku 5.5 on policies written for the study, and DeepSeek and Luna show the same on nine public policies paraphrased from real ones. The facts push the other way: shown without their recorded decisions, past cases whose facts support approval make these two models approve less often than past cases whose facts support denial. One reading is that the request looks weaker next to them. This push is not just a correction toward the right answer: in an additional DeepSeek analysis, it was of similar estimated size on requests that human annotators judged approvable and on those they judged deniable. In a separate DeepSeek run on the public policies, when the past cases are near-copies of a different request, switching their decisions moves approval by 9 points instead of 43, while facts that support approval still lower it by 22 points against facts that support denial. Systems that retrieve past decisions should test the two parts separately.

---


### 95. [Density-Aware Calibration for Resource-Efficient Medical Vision-Language Models](https://arxiv.org/abs/2611.00684)

**<font color=#1a73e8>作者：</font>** Tien-Dat Dam, Huu-Thuan Huynh, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) show promise for clinical image understanding, but their computational and memory requirements hinder deployment on resource-constrained clinical hardware. Post-training quantization (PTQ) offers a practical compression strategy without retraining, yet its effectiveness depends strongly on the calibration data. We propose CoreCalib, a training-free and quantizer-agnostic framework for constructing compact calibration sets that preserve the target medical VQA distribution. CoreCalib stratifies data by clinical question class, identifies representative visual modes using frozen DINOv2 features with UMAP and HDBSCAN, and expands selected images into class-balanced question-answer pairs. On Kvasir-VQA-x1, we evaluate CoreCalib with MASQuant, GPTQ, and QIG using a fixed 128-pair budget. CoreCalib achieves the best METEOR with all three quantizers and the best ROUGE-L with MASQuant and GPTQ. With W4A8 MASQuant, it improves METEOR from 0.5672 with COCO calibration to 0.6234, recovering approximately 41% of the degradation relative to BF16. These results support CoreCalib as a data-centric component for resource-efficient medical VLM deployment. Project page: this https URL .

---


### 96. [The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents](https://arxiv.org/abs/2611.00725)

**<font color=#1a73e8>作者：</font>** Xingling Xu, Zhengwei Jiang, Zheng Zhi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents increasingly operate with web access and high privileges, creating a new attack surface where web fraud can directly target autonomous agents. Existing studies mainly focus on malicious links, prompt injection, and interface deception, while content-level web fraud against agents and the amplification of attacks through agent trust remain underexplored. In this paper, we present EtE (Earn-then-Exploit), a web fraud attack framework against coding agents, in which a malicious website first provides multiple rounds of genuinely verifiable assistance to establish trust and then introduces task-related instructions that cross intended operational boundaries. To systematically evaluate its effectiveness, we construct 56 organizational environments (8 task contexts x 7 attack consequences) and evaluate three representative coding agents. EtE achieves an average scene-level attack success rate of 71.4%, including 85.7% on Codex-GPT-5.5, 67.9% on ZCode-GLM-5.3-Flash, and 60.7% on QwenCode-Qwen3.7-Plus, significantly outperforming all injection-based baselines. More importantly, our experiments reveal that coding agents exhibit trust-like behavioral reliance on previously helpful Web sources, and that such accumulated credibility significantly increases their susceptibility to subsequent malicious instructions. Based on this finding, we propose action-authorization separation (AAS), which prevents web content from directly authorizing privileged actions and reduces the attack success rate to 0% while preserving 100% task completion, outperforming all evaluated defense baselines.

---


### 97. [Constructing Budgeted KGW Evasion through Token-Event Evidence Replacement](https://arxiv.org/abs/2611.00726)

**<font color=#1a73e8>作者：</font>** Hongliang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KGW watermarks bias sampling to accumulate keyed detection evidence. We construct budgeted evasion through token-event evidence replacement using ordinary phrase rewrites. Our construction jointly selects compositions of LLM-proposed alternatives from an independent model and measures global token-edit distance on complete outputs. At the largest attainable cost within the budget, exact coverage search maximizes removal of original scored token pairs. It uses a known tokenizer without the key, detector feedback or queries to the watermarked model. Exact accounting separates source evidence removed, evidence created and length effects, with initial strength setting the required reduction. Separate signed-event analysis found that mean suppression arose mainly from removing watermark-enriched source events. In controlled, occurrence-counted, one-token-context KGW tests on short passages, 39 of 82 qualified, initially detected sources yielded rewrites with terminal detector score Z < 4 that passed blinded source-relative model review, at a mean actual token-edit cost of 16.0% under a 20% allowance. To examine whether this initial requirement can be inferred, a separate historical 95-passage study estimated initial detector score Z0 from generation traces with correlation 0.793 and an in-sample association beyond length. This aggregate information did not establish improved allocation, and the separate no-trace stopping test did not reliably exploit cheaper reviewed crossings in the candidate bank. Comparisons did not establish an advantage over simpler selection and ordinary constrained rewriting. The construction makes budgeted evidence replacement executable while exposing limits in signed reduction and recognition of sufficient editing.

---


### 98. [Can Jev Improve Demonstration Retrieval for In-Context Learning?](https://arxiv.org/abs/2611.00737)

**<font color=#1a73e8>作者：</font>** Rui Song, Yingji Li, Hao Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Demonstration selection plays a crucial role in the effectiveness of in-context learning (ICL) for large language models (LLMs). Extensive research has explored various retrieval strategies to identify informative demonstrations and improve downstream performance. Recently, the emergence of Jev, a decision-oriented language model capable of producing probabilistic judgments, offers a new perspective on evaluating demonstration utility. This motivates us to investigate a fundamental question: Can Jev improve demonstration retrieval for in-context learning? In this paper, we demonstrate that Jev can effectively enhance demonstration retrieval by directly assessing the utility of candidate demonstrations for a given query. However, applying Jev to large-scale retrieval introduces substantial computational overhead, as each candidate requires an additional decision-making inference. To address this limitation, we propose a simple yet effective knowledge distillation approach that transfers Jev's utility estimation capability to a lightweight multilayer perceptron (MLP). By learning to approximate Jev's probabilistic judgments, the distilled model enables efficient demonstration ranking while maintaining competitive retrieval performance. Our study highlights the potential of decision-oriented language models for demonstration selection and provides an efficient framework for integrating their decision-making capabilities into ICL.

---


### 99. [Reading Between the Chapters: A Graph-Free RAG Rebuilt With AI and Human Feedback](https://arxiv.org/abs/2611.00752)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Syeda Fabiayee Jahan, Farig Sadeque  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many questions about a book can only be answered by connecting passages chapters apart, such as a cough heard three times across a horse's life. We introduce CrossChapterQA, 1,853 such questions over 14 public-domain books. Each question lists the two to six chapters it needs (spanning half the book at the median) and the relation linking them, cites evidence from each, and has two independent reference answers graded blind. We use it to build LadderRAG, which indexes a book as passages, summaries and book-level cards for about $0.41 and answers a question for under a cent. Its first version failed mostly at retrieval. We redesigned it four times, steered by an LLM judge's verdicts and our analyses of failed answers: a design-level counterpart of RLAIF and RLHF in which feedback changes the architecture, not model weights. We also report the two redesigns that made answers worse. On the 191 questions its first version got wrong, the final version retrieves over twice as many required chapters on held-out books (recall 0.36 to 0.79), and ten annotators rate its answers 6.5/10 on average (764 ratings).

---


### 100. [DramaVQA: Probing Detailed Understanding of Ultra-Long TV Dramas](https://arxiv.org/abs/2611.00769)

**<font color=#1a73e8>作者：</font>** Xinyue Huo, Pengfei Chen, Jiannan Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in long-form video understanding, current benchmarks mostly focus on short clips or hour-scale videos. This leaves a major gap in evaluating ultra-long video understanding, where videos often last tens of hours. To bridge this gap, we introduce DramaVQA, a large-scale benchmark built upon long-form TV dramas. Containing approximately 20K question-answering (QA) pairs, the scale of DramaVQA exceeds previous long-video datasets, such as Video-MME and LVBench, by an order of magnitude. Our benchmark has two main features that make it stand out from existing datasets. First, we establish a scalable, LLM-assisted annotation pipeline that uses multimodal large language models (MLLMs) to generate complex questions, followed by strict human checking to ensure high data quality. Second, DramaVQA introduces a multi-level time structure; queries are designed across different video lengths, with the hardest questions requiring overall understanding across the entire drama. Extensive evaluations show that state-of-the-art MLLMs face major challenges when tested on these very long videos, highlighting the need for agentic AI algorithms capable of managing long-term memory. The project is available at this https URL

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
