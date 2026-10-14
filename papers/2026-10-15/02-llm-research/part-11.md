# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**501-550**（第 11/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 501. [Know-Thy-Not: Training-Free Targeted Negation in Dual-Encoder Vision-Language Models](https://arxiv.org/abs/2610.17440)

**<font color=#1a73e8>作者：</font>** DoYoung Kim, Changkyu Choi, Adín Ramírez Rivera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-encoder vision-language models systematically fail at negation, scoring ''a cat without a dog'' nearly identically to ''a cat with a dog.'' We show that this failure is inherent to the single-embedding framework. Under contrastive training, single-embedding methods can at best ignore the negated concept (dilution) but never penalize its presence (rejection). We propose Know-Thy-Not (KTN), a training-free method that introduces an image-side rejection dimension to penalize the negated concept directly in the visual representation. We also introduce COCO-Confusion, the first benchmark requiring genuine rejection to succeed. Across 9 backbones, KTN improves COCO-Confusion mAP by up to +25.6 over vanilla VLMs and +9.6 over the strongest existing method.

---


### 502. [The belief-action gap in language model agents](https://arxiv.org/abs/2610.17444)

**<font color=#1a73e8>作者：</font>** Ayse Sila Okcu, Weisheng Wang, Tongmeng Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model (LM) agents can fail for different reasons, requiring different explanations and interventions. We study how state beliefs, action values, and action preferences interact as LM agents reason and commit to decisions in text-rendered grid worlds. We estimate task-relevant beliefs using report-based and representation-based probes, and action values using inverse reinforcement learning. We find that task-relevant state and value information is often represented more reliably than it is reflected in behaviour. Tracking action preferences throughout reasoning further shows that decisions sharpen around a commitment point and reported belief uncertainty decreases near commitment, although individual belief changes do not consistently explain shifts in action preference. Finally, forced actions follow reasoning prefixes from other decisions when transplanted, whereas the tested reasoning-window activation edits provide limited control over the action. Together, these results suggest that some failures arise not from missing task-relevant information, but from how available information is translated into action. Our measurements distinguish information availability from belief-action consistency without by themselves identifying the cause of each failure. Our code is available at: this https URL

---


### 503. [Compositional RL: Evaluating and Training LLMs for Collaborative Reasoning](https://arxiv.org/abs/2610.17456)

**<font color=#1a73e8>作者：</font>** Shangbin Feng, Yulia Tsvetkov, Jan Kautz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are often evaluated alone but increasingly deployed together, routed between, made to debate, ensembled, or collaboratively trained. For a model inside a system, what matters most is not how well it performs on its own, but how much the system gains from its presence. We call this a model's compositional strength and formalize it using the Shapley value of a cooperative game over coalitions of a model pool, and use a model's leave-one-out contribution to the full coalition as a tractable proxy, requiring n+1 rather than 2^n system evaluations. Evaluating individual vs. compositional strengths across five model pools, twelve collaboration methods, and twelve datasets, we find them largely uncorrelated: in 12 of 15 (pool, method-family) settings, individual strength does not translate into compositional advantages, and the coupling is weakest among general-purpose models that practitioners are most likely to deploy. Standalone benchmarks are therefore often poor proxies for models' value in collaborative systems. We then propose compositional reinforcement learning (C-RL), which trains a policy inside a live multi-model system and rewards the outcome produced by the system as a whole, rather than the policy's correctness in isolation. The leave-one-out baseline in Shapley values cancels under a group policy gradient, so this needs no additional rollout cost beyond RL on the collaborative system's outcome and never requires running a coalition without the policy. Across three collaboration protocols and eight tasks spanning reasoning, coding, and scientific discovery, C-RL produces the strongest collaborator in 21 of 24 settings, lifting collaborative performance by +4.0 to +5.4 pts on average (~3x the gain of baselines), up to +13.1 pts.

---


### 504. [Distilling Text LMs into Speech-to-Speech LMs by Matching Internal Text Predictions](https://arxiv.org/abs/2610.17461)

**<font color=#1a73e8>作者：</font>** Ju-Chieh Chou, Jiawei Zhou, Karen Livescu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text language models (LMs) acquire broad linguistic and factual capabilities through large-scale pretraining, while comparable capabilities remain difficult to learn from speech alone. Recent work has shown that knowledge distillation from pretrained text LMs offers a promising way to transfer their linguistic and factual capabilities to speech models. However, existing distillation approaches have largely focused on speech-input, text-output models. This idea has yet to be explored for {\it speech-to-speech} models, which operate on both speech input and speech output. In this work we introduce a speech-to-speech pretraining method that creates an internal text interface for knowledge transfer while preserving the speech-only input and output. The model first consumes speech context without its transcription, switches to text prediction, and then uses the predicted text to lead future speech generation word by word. It also provides an interface for knowledge distillation: the internal text predictions can be directly distilled from the base text LM. To the best of our knowledge, this is the first application of text LM distillation to a speech-to-speech LM. Under matched training conditions, the proposed sequence construction substantially improves the generative perplexity of spoken continuations over speech-only and interleaved speech-text models, approaching the performance of a text-leading inner-monologue model with external ASR prompt transcription. More importantly, distillation improves factual performance under both text and speech evaluation, indicating better retention of knowledge from the base text language model.

---


### 505. [Scaling Inference-Time Compute with Teams of Coding Agents](https://arxiv.org/abs/2610.17471)

**<font color=#1a73e8>作者：</font>** Keenan Samway, Daniel D'souza, Omar Darwiche Domingues 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems promise a new axis for scaling inference: rather than having one agent think longer or sample more attempts, a task is split across many agents that work in parallel and coordinate. However, in practice, more agents can easily produce duplicate work, coordination failures, and higher costs. We therefore formulate team design as a compute allocation problem: starting from a solo agent, where should additional inference compute go to reach the reward-cost Pareto frontier? We build a minimal multi-agent harness from the ground up and trace this frontier by varying, one at a time, the workflow stage at which a lead delegates to its workers (planning, implementation, or verification), the models that form the team, and the number of workers. On ProgramBench, teams outperform solo agents but cost three to seven times as much. With the right compute allocation, however, a heterogeneous 17-agent team comes within 1.4 points of a strong homogeneous 5-agent team at 70% lower cost. This efficiency stems from three findings. First, planning is the most valuable use of workers: in a homogeneous team whose lead decides how many workers to spawn, a lead that delegates only planning to its workers, and then implements and verifies the code itself, matches the reward of a lead that delegates to workers throughout planning, implementation, and verification, at half the cost. Second, cheap models pay off as planners but not as implementers: a strong lead with cheap planners recovers 47.5% of the reward gain of an all-strong team for only 13.9% of its additional cost, whereas cheap implementers lower reward. Third, planners keep improving reward as the team grows, whereas implementers and verifiers plateau beyond four workers. Together, our results offer a guide to spending an agent budget where it counts, given the task, cost, and latency constraints a user has.

---


### 506. [REA: From Correct LLM Judgments to Safe Decision Delivery](https://arxiv.org/abs/2610.17473)

**<font color=#1a73e8>作者：</font>** Jingxiang Meng, Aofan Liu, Yaoshuai Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative safety guards must classify requests correctly and return outputs that applications can parse. Reasoning guards can improve classification accuracy while producing outputs that applications cannot parse. When applications cannot extract a correct prediction, fallback handling can allow harmful requests or block safe ones. We introduce Resolve--Express--Act (REA), a framework that traces judgments through parsing and fallback to application actions. Experiments on classifiers and safety guards show that correct predictions can appear in incorrectly formatted outputs. Parsing the safety verdict preserves the reasoning guard's accuracy advantage, while stricter explanation requirements reject additional correct predictions. Accepting formatting variations recovers most rejected correct predictions. Held-out tests confirm that output requirements and generation limits affect whether correct predictions can be parsed. In our fail-open replay, matching the parser to the output and fixing formatting reduced the fraction of harmful requests allowed despite correct guard judgments from 95.5% to 0%. A fixed-output comparison shows that model-based extraction can preserve guard verdicts, but is not automatically reliable; deterministic normalization already repairs the observed native-format failures. Fallback replay shows that the same correct prediction can lead to different safety actions depending on the parser and fallback policy, including allowing requests the guard correctly identifies as harmful.

---


### 507. [Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Systems](https://arxiv.org/abs/2610.17488)

**<font color=#1a73e8>作者：</font>** Hanyi Yu, Jiaming Cui  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As language-model-based coding agents evolve their programs and reuse code from one another, safety failures can acquire a history that extends beyond the agent in which they are detected. An unsafe change may originate in one agent, propagate through intermediate recipients, and survive subsequent revisions before an audit reveals it. Understanding this history is important for identifying the introducing change and distinguishing inherited behavior from independently occurring failures. We study origin attribution in self-evolving multi-agent coding systems: recovering the agent and program version that introduced an observed unsafe behavior into the target's code lineage, or determining that it arose locally. This task is challenging because rewriting obscures textual similarity, independent occurrences confound temporal ordering, and intermediate recipients can resemble the source. We propose a method that combines behavioral fingerprint matching with historical localization and recursive tracing. It compares candidate implementations beyond the unsafe outcome, retains evidence from multiple historical versions, and follows matching candidates upstream. On 158 queries across 85 controlled scenarios, the method achieves 96.8% exact attribution accuracy, compared with 77.2% for exhaustive fingerprint matching without recursion. Component ablations and evaluation on 34 additional queries using the same method and hyperparameters demonstrate the complementary roles of multiple representatives and recursive tracing. Further checks extend the evaluation to approval-boundary and resource-owner errors. Together, these results show how behavioral and historical evidence can recover the origins of unsafe behavior through code revision and cross-agent propagation.

---


### 508. [A Sense of Proprioception in Language Models](https://arxiv.org/abs/2610.17495)

**<font color=#1a73e8>作者：</font>** Jonas Geiping  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In humans, proprioception corresponds to the sense of self-movement or position, e.g. understanding the position of one's arm. This sense is often less well-understood and in popular understanding sometimes conflated with introspection. But, notably, proprioception is a separate sense, with dedicated receptors and verifiable outcomes. On the other hand though, language models cannot observe their own internal states during training (and for example answer the question which experts activated in a certain layer of an MoE) and so cannot accurately report on them. Yet, such information is, by virtue of being internal to the model, both accessible, and readily constructed into verifiable signals. We argue that this provides the basis for a digital analog of proprioception. As such, we train models through SFT and on-policy training to equip them with this ability. We show that modern models can be trained to understand a range of subtypes of proprioception, such as routing decision awareness, token entropy, decision depth or logit lens information, without affecting model capabilities. We then run these models through a broad evaluation of situational awareness, legibility, and epiphenomenality, to evaluate in what ways access to proprioception changes model behavior.

---


### 509. [TwinPrune: Density-Aware Two-Phase Token Pruning for Vision-Language Models](https://arxiv.org/abs/2610.17530)

**<font color=#1a73e8>作者：</font>** Kai Liu, Anqi Li, Junxian Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a unified spatial-density signal to score token importance for both inference phases: bipartite merge for prefill and KV eviction for decode, yielding measurable gains in each stage. To isolate the two phases, we split benchmarks by scoring logic. Prefill probes (MMBench, POPE, ScienceQA) evaluate only the first decoded token; their accuracy reflects prefill logits argmax before any decode KV eviction. Full-pipeline probes (TextVQA, DocVQA, MM-Vet) assess the complete generated sequence and capture both phases. We identify a critical evaluation pitfall: decode pruning claims validated solely on prefill probes measure prefill quality, not decode performance. Experiments show discarding all visual KV during decode barely affects prefill-probe accuracy but degrades TextVQA and MM-Vet drastically; this insensitivity stems from the scoring rule, not compression this http URL on seven model variants (InternVL-3.5, Qwen3-VL, LLaVA-1.5) and three full-pipeline benchmarks, our method achieves a three-way Pareto frontier across compute, memory and accuracy. Density-based prefill compression maintains strong accuracy, scales linearly with visual token count, and delivers 100x faster token selection at high resolution. For decode, density top-k KV eviction consistently outperforms strong baselines H2O, SnapKV and StreamingLLM on TextVQA and MM-Vet across three retention ratios. At 0.125 keep ratio on TextVQA, it surpasses H2O by 9.6 points; InternVL-3.5 models (2B to 38B) maintain a 7 to 10 point advantage. Compression scales favorably with model size: every measured 8B to 38B model transition reduces accuracy loss instead of worsening it. We suggest MM-Vet or DocVQA as mandatory full-pipeline validation for any decode-phase claims. Our code is available at this https URL

---


### 510. [Towards Green AI: Evaluating Energy Efficiency for Quantized LLM Inference](https://arxiv.org/abs/2610.17531)

**<font color=#1a73e8>作者：</font>** Petar Basta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While it is known that quantization of large language models (LLMs) reduces memory usage via lower-bit weights, studies quantifying the resulting impact on energy usage and carbon intensity are scarce. We present the first unified evaluation of weight-only quantization strategies for LLM inference across varying input/output lengths and GPUs, highlighting differences in energy efficiency in addition to accuracy degradation and runtime. We study quantized inference on Llama 2 7B, Phi 3.5 Mini Instruct, OLMo 1B, Qwen 2.5 7B, and Qwen 2.5 14B across GLUE MNLI, MMLU, HumanEval, and GSM8K datasets, evaluating 10 post-training quantization (PTQ) strategies on NVIDIA H100, A6000, A100, and L4 GPUs. We identify a novel trend showing that quantization techniques tend to exhibit peak energy efficiency relative to full-precision baselines when inputs are sufficiently long and outputs are short. Furthermore, we show that quantization strategies become marginally more energy-efficient relative to full-precision models as batch sizes increase, though gains are modest. Notably, fused-kernel implementations such as EETQ int8 and Bitsandbytes int8 offer the highest energy savings, up to 4x compared to FP32 on short text generation, with negligible accuracy loss. Finally, we observe that energy usage closely tracks runtime on our evaluated benchmarks, indicating that, in practice, latency optimization can serve as a reliable proxy for reducing the environmental footprint of LLM services. We conclude with suggested directions for strategically selecting low-carbon quantization strategies based on specific inference requirements.

---


### 511. [Everyone Was Right: Lexical Representations in Language Models Are Both Abstract and Holistic](https://arxiv.org/abs/2610.17538)

**<font color=#1a73e8>作者：</font>** Zachary Nicholas Houghton, Yu Zhou, Dan Pluth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lexical representations can encode both abstract information and information specific to particular contexts. We investigate how these forms of information are organized in language models by decomposing contextual word representations into item, class, and word-class interaction components. Across six pretrained transformers and two linguistic categories, we find that the interaction is consistently present, grows across layers, and contains information associated with both item and class. Unlike the nearly orthogonal item and class effects, the interaction overlaps with both and encodes class information beyond the shared class effect. An interaction also emerges in artificial-language learners even when the input contains only additive structure. Together, these findings show that lexical representations combine abstract information with structure specific to particular word-class combinations.

---


### 512. [TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency](https://arxiv.org/abs/2610.17540)

**<font color=#1a73e8>作者：</font>** Jack Lu, Yurong You, Boyi Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA whose action expert never attends to the reasoning it generates for the current call. On long-horizon tasks where the reasoning text also serves as episodic memory, it can generate each entry during action execution rather than before acting. We evaluate it in a controlled study on four benchmarks spanning manipulation and autonomous driving, memory and non-memory tasks: RoboMME, RMBench, LIBERO, and PhysicalAI-AV. On all four, TacitVLA matches the performance of its explicit-reasoning counterpart at up to 3.4x lower latency, and matches the latency of the same architecture trained without reasoning at up to +17.1% success. In absolute terms, it surpasses the best previously published results on the RoboMME Counting suite (82.7% vs. 66.8%) and RMBench (77.5% vs. 56.5%), and reaches 72.9% on LIBERO-Plus and a 52.5% scene score on the public split of the PhysicalAI-AV closed-loop driving challenge. Project page: this https URL.

---


### 513. [Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents](https://arxiv.org/abs/2610.17544)

**<font color=#1a73e8>作者：</font>** Jianghong Zhou, Hao Rong, Chen Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one. We call this reasoning contraction. A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong. Most systems trust memories by counting successes and failures. We prove that such counters are badly tuned change detectors: a symmetric counter notices a partial change only after a power of its false-alarm horizon, and an unclipped one may never notice it. On five LLMs answering multi-hop questions over edited facts, ExpeL- and ACE-style counters serve 7.0-13.5x more stale answers than certified memories given the same information, and on code tasks with an exact verifier 35-73x more. Safety also has a price. When facts change and each memory is judged only by its own verified outcomes, one number, the certification load, sets how much reasoning any safe memory can skip, and under Zipf demand it yields a scaling law. Our recipe weighs each memory's failures by its own likelihood ratio, certifies its utility against live reasoning, and restarts the certificate when facts change, with the likelihood-ratio detector as the safety net for unannounced changes; for large edits it also invalidates the memory.

---


### 514. [EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation](https://arxiv.org/abs/2610.17560)

**<font color=#1a73e8>作者：</font>** Zeru Shi, Jindong Jiang, Ryo Hachiuma 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Complex and long-horizon agent tasks often rely on frontier models deployed in the cloud to achieve strong performance. However, using these models for every step of a long-horizon trajectory incurs substantial inference cost, even though not all steps may require the same level of model capability. In this paper, we find that allocating the LLM to only a small subset of key steps can achieve performance comparable to full LLM execution while significantly reducing inference cost. Motivated by this observation, we propose EdgeWise, an edge-cloud collaboration framework that deploys an SLM on the local device as the primary solver and selectively delegates critical steps to a cloud LLM when stronger model capacity is needed. To enable autonomous delegation without additional models at inference time, we introduce a step-level RL method that jointly optimizes task solving and delegation, with fine-grained credit assignment for individual delegation decisions. We also introduce an external judge-based delegation strategy and use it to systematically investigate key design choices in edge-cloud collaboration, including when to delegate, how delegation decisions should be made, what context should be shared, and how frequently the cloud LLM should be invoked. Experiments show that EdgeWise matches or outperforms pure-LLM execution while reducing inference cost up to 62% on SWE-Rebench and 34% on Terminal-Bench 2.1. We further deploy EdgeWise on a local workstation, demonstrating comparable cost savings in a practical edge-cloud setting.

---


### 515. [Dissociating Answerability from Extraction in LLM Question Answering over Radiology Reports](https://arxiv.org/abs/2610.17576)

**<font color=#1a73e8>作者：</font>** Priyanshu Sinha, Kelsey McDonald  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering questions from radiology reports involves two decisions: whether the report contains an answer and which span gives it. A false answer presents an unsupported claim as fact; an over-abstention hides what the report says. Yet RadQA results are reported as a single F1 that merges both. We propose an evaluation method that separates them, reporting false-answer and over-abstention rates beside F1 and splitting F1 changes into extraction and answerability terms. We apply it to 13 LLMs on the RadQA test set, zero-shot and with three cumulative demonstration sets, the last adding an unanswerable example. Models with similar F1 differed more than twofold in false-answer rate. The unanswerable example changed when models answered, not how well they extracted: 12 of 13 models abstained more often, and three-quarters of the answers they withdrew had F1 $\geq$ 0.5. Within models, false answers showed no clear association with extraction quality, but acting on the decision itself helped: keeping an answer only when enough other models also answered lowered the zero-shot false-answer rate by 4 points without a detectable F1 change. Because the two decisions can change independently, we suggest radiology QA evaluations report them separately, not through F1 alone.

---


### 516. [RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control](https://arxiv.org/abs/2610.17584)

**<font color=#1a73e8>作者：</font>** Binghan Wu, Kai Zeng, Kai Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operational mobile networks are rich in observations but poor in interventions: they continuously generate large volumes of passive telemetry, while controlled action--response trajectories remain comparatively scarce and costly to collect. This observation--intervention asymmetry is a central obstacle to building practical world models for RAN control. We address this problem with RAN-JEPA, an action-conditioned world model that separates representation learning from intervention learning. The model first learns a predictive latent representation from observation-only network data, adapts that representation to the target deployment domain, and then learns action-conditioned latent dynamics from controlled sleep/wake trajectories while keeping the encoder fixed. We evaluate RAN-JEPA using public operator performance data for pretraining and a real-equipment four-cell 5G testbed for domain adaptation, post-training, and control. Across four future 15-minute intervals, RAN-JEPA achieves lower action-conditioned prediction error than a GPT-2 world-model baseline and a mechanistic rule, while remaining close to a strong persistence reference. What-if evaluation further shows that the model produces distinct and coherent future trajectories under matched SLEEP and KEEP plans. In closed-loop control, RAN-JEPA consistently supports higher sleep ratios than the two baselines at comparable congestion cost. These results show that observation-first, action-conditioned learning can turn abundant passive telemetry and limited intervention data into a practical predictive model for energy-aware RAN control.

---


### 517. [Revisiting the 16x Pretraining Compute Gap between Diffusion and Autoregressive Language Models](https://arxiv.org/abs/2610.17590)

**<font color=#1a73e8>作者：</font>** Guanghan Wang, Bing He, Zhan Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) have attracted wide attention for their fast, parallel decoding, but they are believed to be far less efficient to train than autoregressive language models (ARMs): a widely cited study reports that a DLM needs roughly 16x the training compute of an ARM to match its likelihood, a figure that has made pretraining DLMs from scratch look prohibitive at scale. We find that the methodology behind this figure has fallen out of step with current DLM practice: it scores the model with its evidence lower bound (ELBO) and trains a full-sequence, decoder-only model. We therefore revisit the scaling laws of DLMs, adopting the exact likelihood under the model's own decoding order, block diffusion training, an encoder-decoder architecture, and a sweep over the block sizes used in practice. Under this new protocol, we study across ten model variants, about 1,700 models in total, and find that pretraining DLMs is far cheaper than previously thought. Concretely, scoring with the exact likelihood reduces the compute multiple to 12.8x; block diffusion training and an encoder-decoder architecture further reduce it to 7.8x at block size 32, and smaller block sizes narrow it to 4.6x at block size 8 and 3.0x at block size 4. We complement these scaling analyses with an empirical rule for the optimal decoder depth of encoder-decoder block diffusion, a held-out compute budget beyond the fitting range at which the gap between variants persists, and downstream benchmark results where likelihood improvements carry over to accuracy. Overall, the 16x figure substantially overstates the pretraining cost gap between DLMs and ARMs, and pretraining DLMs from scratch is far more viable than previously assumed.

---


### 518. [Tanawpamana: Benchmarking Vision-Language Models on Philippine Cultural Heritage Sites](https://arxiv.org/abs/2610.17596)

**<font color=#1a73e8>作者：</font>** Ivan Yuri De Leon, Hiroki Ouchi, Sakriani Sakti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used to identify and describe places, yet their recognition and knowledge of specific cultures remain poorly understood, particularly in underrepresented regions such as the Philippines. This study introduces the Tanawpamana Dataset, a repository of Philippine heritage site images with metadata based on the Talapamana registry of the National Commission for Culture and the Arts of the Philippines. We also introduce the Tanawpamana Benchmark, comprising 4,046 tasks designed to evaluate models' recognition and knowledge of heritage sites. Evaluating seven vision-language models, we find that they struggle more with fine-grained visual discrimination among similar heritage sites than with coarse recognition, and that their geographic knowledge is weaker when inferred from image inputs than from text.

---


### 519. [TDR: Tagalog Diacritic Restoration Dataset](https://arxiv.org/abs/2610.17597)

**<font color=#1a73e8>作者：</font>** Ivan Yuri De Leon, Lanz Railey Fermin, Zachary Aldridge Africa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Homographs are words that share identical spelling but differ in meaning and pronunciation. In Tagalog, these distinctions are disambiguated in writing through tuldik (diacritical marks), which are rarely preserved in contemporary Tagalog text. This scarcity of diacritics limits diacritic restoration, which is useful for downstream tasks such as prosody selection for text-to-speech synthesis. To address this gap, this study introduces TDR, an annotated corpus of 40 frequent Tagalog homographs constructed from news text. It also introduces a collocation-driven retrieval method to expand the dataset and mitigate severe class imbalance among minor variants. Finally, we show that TDR supplies a capability absent from pretrained models, and that this capability can be learned by small, inexpensive models as well as by fine-tuned LLMs.

---


### 520. [Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation](https://arxiv.org/abs/2610.17607)

**<font color=#1a73e8>作者：</font>** Yongcan Yu, Jian Liang, Lingxiao He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While long chain-of-thought (CoT) distillation significantly improves the reasoning abilities of language models, its underlying mechanism remains poorly understood. Current pipelines generally rely on rejection sampling to gather reasoning traces across diverse prompts, assuming that factual correctness and broad problem coverage are indispensable. Surprisingly, we find that training exclusively on flawed reasoning trajectories or a restricted prompt set yields nearly comparable performance. Driven by this counterintuitive finding, we propose the Behavioral Hypothesis: the essence of Long-CoT distillation is behavioral alignment with structured reasoning patterns, rather than factual knowledge memorization. We then validate this by demonstrating substantial reasoning gains even when models are fine-tuned exclusively on previously mastered problems-effectively isolating behavioral alignment from novel knowledge injection. Having established that reasoning patterns are the true bottleneck, we investigate how to learn them across varying levels of complexity optimally. We reveal a critical interplay: while the recent probability-based loss excels at learning simple patterns, the standard cross-entropy loss is essential for scaling to complex CoTs. We believe these insights demystify CoT distillation and provide a principled foundation for the future development of reasoning models. Code is available on this https URL.

---


### 521. [Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609)

**<font color=#1a73e8>作者：</font>** Tianyi Xu, Yaolun Zhang, Yiran Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training-free self-improvement lets an agent use feedback to revise the response it is about to return and to update the harness state that shapes how it handles later tasks. On open-ended tasks that feedback rarely comes from reference answers or executable tests, so the agent has to rely on a model-based verifier. When the verifier is wrong, the current response can get worse, and misleading experience can persist across the task stream. A verifier that never changes also grows stale as the agent's responses improve and task demands shift. We introduce Unified Co-Evolution (UCoE), a training-free method that evolves an executable verifier program together with the agent's harness state while all model parameters stay fixed. UCoE synthesizes candidate verifier programs and tests them on response contrasts, pairs of responses that differ in one declared property and have a known preferred side. It selects the candidate whose discrimination on its weakest contrast family is highest, a quantity we call driving capacity. The selected verifier diagnoses one weakness in each draft, guides a single repair, decides which response is served, and determines whether the accepted repair may enter the harness state. As tasks complete, their diagnostics seed new candidate verifiers, which must beat the current verifier on the same contrasts before adoption. Across six open-ended benchmarks, UCoE averages 59.00% preference against matched direct generation with Qwen3-8B and 57.19% with Qwen3.8-27B, margins of 9.00 and 7.19 percentage points. On three verifiable benchmarks, the same method raises the mean from 36.06% for direct generation to 38.48%. Code is available at this https URL.

---


### 522. [MAS-Gate: Unlocking Multi-Agent System Lifecycle via Node-Centric Quantification](https://arxiv.org/abs/2610.17613)

**<font color=#1a73e8>作者：</font>** Hehai Lin, Zixuan Wang, Ming Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) can solve complex problems beyond the reach of a single agent by decomposing tasks and coordinating complementary capabilities. Despite extensive research on MAS, existing work largely focuses on specific aspects or individual phases of their development and operation, resulting in fragmented perspectives with objectives and signals that are difficult to reconcile across these different settings. To bridge these disconnected perspectives, we conceptualize MAS development and operation as a three-phase lifecycle spanning design-time orchestration before execution, runtime intervention during execution, and post-hoc attribution after execution, and introduce MAS-Gate, a unified node-centric quantification applicable across these phases. Modeling each execution as a directed acyclic graph, MAS-Gate combines within-node utility, which estimates a node's contribution through changes in reference-answer likelihood, with inter-node strength, which approximates semantic uptake and potential downstream reach. We adapt this shared quantification to three objectives: providing a structure-aware dense reward for Orchestrator training, training an Editor to act on execution prefixes using paired rewards from completed edited and unedited trajectories, and supplying risk-ranked nodes as auxiliary evidence for LLM-based post-hoc attribution. Experiments spanning interaction environments, knowledge-intensive multi-hop question answering, general reasoning, and post-hoc attribution demonstrate that MAS-Gate improves workflow construction, targeted runtime editing, and LLM-assisted error localization over corresponding phase-specific baselines. Together, these results establish MAS-Gate as a unified structural interface for improving MAS generation, dynamic editing, and error attribution throughout the lifecycle.

---


### 523. [RELAY: Selective Self-Distillation with Adaptive Hand-off for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2610.17623)

**<font color=#1a73e8>作者：</font>** Kunwang Zheng, Xinyu Sun, Yu Cao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning grades a response against many written criteria but collapses them into one reward, which discards the detail the rubric carries and gives no GRPO reward gradient when a group's responses tie. A frozen teacher that reads the rubric as privileged context provides token-level supervision, but we observe an early plateau in the gains over GRPO. RELAY uses advantages and rewards to select positive-advantage and low-scoring zero-advantage rollouts, and monitors the distillation loss to decide when to retire the teacher. Stage 1 combines selective distillation from a frozen teacher with GRPO; a plateau detector then removes the teacher, and Stage 2 continues with GRPO alone. Calibrated on one model-domain pair and reused unchanged in three others, the plateau detector fires between steps 122 and 171. RELAY scores highest in-domain among the compared methods in all four settings, ahead of GRPO on RaR-Medicine by 4.62 points with Qwen3-1.7B and 6.02 with Qwen3-4B. On Qwen3-1.7B/Medicine, removing the teacher from a shared checkpoint outperforms keeping, weakening or refreshing it. Distilling selected rollouts covering about half the response tokens also outperforms distilling all rollouts at a matched average coefficient.

---


### 524. [Executable Prefix Values for Locating Agent Failures](https://arxiv.org/abs/2610.17633)

**<font color=#1a73e8>作者：</font>** Bingyu Shen, Jiaqi Tang, Lan Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Work on debugging LLM agents treats the "first mistake" marked by a human or LLM judge as ground truth for where a trajectory failed. We ask whether such labels point at causes or symptoms, and make the distinction executable: we restart the agent from reconstructed intermediate states of a failed trajectory and estimate its prefix value V(h_t), the probability of success from each step, with a certified point of no return (PNR) for a failure. On 150 SWE-bench Verified tasks with two frozen open-weight agents, we build such curves for 47 and 60 failed trajectories and probe every step labeled by four frontier judges under the Traverse rubric. We find that the labels do not mark what a controller needs. Judges of different lineages agree on the exact step in only 21/57 cases, and the newest judges flag mistakes in 8/10 and 10/10 successful runs. For 66% of the labels, the agent's success probability does not drop at the labeled step; only 7/188 answers name the decisive step. Restarting at the measured restart point raises expected success from 0.44 to 0.57 offline, and real restarts confirm the advantage, whereas restarting at a judge's label does not (-0.08 to -0.03). We release our code, curves, and labels.

---


### 525. [The Tokens Strike Back: Safety-Aware Denoising with Directional Embedding-based Revision](https://arxiv.org/abs/2610.17636)

**<font color=#1a73e8>作者：</font>** Amman Yusuf, Jiwoo Shin, Ruizhi Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Safety-Aware Denoiser (SAD) is a recent, training-free, safety-guidance framework for text diffusion models. During inference, SAD steers text samples toward safe regions of the token probability space. In this paper, we propose $\mathit{SADDER}$ (Safety-Aware Denoising with Directional Embedding-based Revision), which improves the safety and quality trade-offs of SAD by exploiting a safety-guidance signal in the embedding (or activation) space for each token position, then updating the token positions using the SAD update rule multiplied by the guidance signal. This multiplication acts as a gating mechanism: tokens with a high unsafe signal are more likely to be modified during inference following the SAD update rule. However, such an update does not automatically preserve the conditional mean, i.e., the denoiser of a fixed target distribution. We therefore theoretically derive new position-wise target distributions for which the modified denoiser is exact. Furthermore, we derive conditions under which the position-wise target distributions match a global target distribution. We test our $\mathit{SADDER}$ method on popular Masked Diffusion Language Models (MDLMs) and Uniform-State Diffusion Models (USDMs) across unsafe continuation and jailbreak settings, and show that $\mathit{SADDER}$ achieves a better balance between safety, generation quality, and inference cost than existing methods.

---


### 526. [Mixed Precision Scaling Laws for Quantized Pretraining](https://arxiv.org/abs/2610.17637)

**<font color=#1a73e8>作者：</font>** Jinuk Kim, Rajarshi Saha, Muhammed Fatih Balin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since scaling laws were introduced for modern LLMs (Kaplan et al., 2020), several works have extended them to account for quantization, tracking the emerging low-precision data types supported on AI accelerators. We develop a more accurate scaling law for quantized pretraining with mixed precision across the forward and backward passes, grounded in optimization theory and validated empirically. Our formulation separates the effects of quantization on model capacity and on optimization efficiency, and explicitly models the persistent optimization error from forward and backward quantization identified through convergence analysis. To select the regimes for fitting and evaluating our law, we first decompose existing 4-bit training recipes into their forward and backward components, isolating those that most affect loss. Our Qwen3 experiments under selected 4-bit regimes, together with published Llama-style experiments, show that our law predicts loss with up to $11\times$ lower MSE than existing laws as model size and token count scale. Finally, we extend our law to layer-wise mixed precision and identify the optimal quantized-pretraining recipe, i.e., model size, training tokens, and per-layer forward/backward precision, under a hardware-aware compute budget. Unlike prior precision scaling laws, our law predicts that the optimal precision increases with the compute budget.

---


### 527. [FrameLite: Decision-Oriented Aesthetic Cropping with a Compact Vision-Language Model](https://arxiv.org/abs/2610.17639)

**<font color=#1a73e8>作者：</font>** Jianze Li, Kai Liu, Ziqing Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aesthetic image cropping improves composition by balancing subjects, context, and image boundaries. Large vision-language models bring semantic knowledge to this task, but their scale limits lightweight photography assistance. We propose FrameLite, a compact cropping model built on Qwen3.5-0.8B. Our approach is motivated by the observation that a small model can generate better crops than its first answer suggests. We develop three-stage training to turn this potential into stronger direct predictions. Spatial and composition training establishes localization and framing preferences. Quality-Guided Online Supervision (QOS) then learns the highest-quality complete answers among the current policy's generated candidates. Greedy-Referenced Optimization (GRO) further refines the policy using positive and negative quality differences relative to its current greedy answer. Both online stages use annotation-derived feedback, while inference returns one coordinate answer without search or an external scorer. Experiments show that FrameLite outperforms the compared large-VLM croppers across public benchmarks with a substantially smaller backbone. Controlled studies confirm that selecting high-quality training answers improves the final model beyond online sampling alone. We will release our code and model weights at this https URL .

---


### 528. [MemAct: Streaming Spatial Understanding with Memory and Active Exploration](https://arxiv.org/abs/2610.17640)

**<font color=#1a73e8>作者：</font>** Yuxi Wei, Wei Huang, Qirui Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial understanding is essential for embodied agents navigating and interacting with the physical world. As observations arrive incrementally, agents must reason in a streaming manner. Yet streaming understanding must also be closed-loop: task-relevant evidence may require both recalling past observations and actively acquiring new views. Existing streaming approaches largely emphasize processing incoming observations, leaving task-driven active exploration underexplored. We introduce MemAct, a framework for streaming spatial understanding with memory and action. A shared vision--language model incrementally writes structured historical memory, retrieves records and past frames on demand, and acquires additional evidence through movement and turning. Retrieved evidence and action observations inform subsequent decisions, enabling the agent to continue exploring or answer within a unified reasoning loop. We develop the MemAct suite, a data generation pipeline and collection across real and simulated environments, with approximately 1M training examples for spatial reasoning, memory writing, retrieval, and exploration. Its MemAct-bench comprises 20,000 main QA pairs evaluating current-observation understanding, historical evidence use, and active exploration, plus 2,000 separate Timing questions. MemAct combines supervised fine-tuning for memory and interaction with counterfactual action optimization using cumulative evidence gains, action costs, and terminal answer quality to improve exploration and stopping decisions. Experiments show that MemAct outperforms existing spatial understanding and streaming baselines and approaches frontier multimodal models on MemAct-bench while retaining streaming inference efficiency.

---


### 529. [Beyond Bias Scores: Answerability Confounds in Activation Steering with Gradient-Constrained Direction Design (GCD)](https://arxiv.org/abs/2610.17641)

**<font color=#1a73e8>作者：</font>** Weitong Li, Donglin Song, Junkai Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bias scores in language-model evaluations often conflate what a model prefers with whether it answers at all. We identify this confound in \textsc{BBQ}, whose ambiguous score factorizes into answerability and signed preference. Across 11 categories, 28,}824 items, and five models, contrastive steering lowers the signed ambiguous score in 11/11 categories but lowers the signed disambiguated preference score in only 8/11. Across 99 configurations, the answerability channel exceeds half of the observed score change in 17\% and accounts for the entire change in 11%. In a six-category disambiguated evaluation, 20.8\% of 1,500 items flip to the unknown option, where abstention is incorrect; \textsc{StereoSet} shows no analogous answer-rate shift. The effect reflects selection and near-orthogonality between the contrastive and preference-gradient directions. We introduce Gradient-Constrained Direction Design (\textsc{GCD}), an option-gradient construction with a first-order unknown-logit constraint. Under a matched Qwen-7B protocol, GCD reduces answer-rate distortion 14-fold and yields a 4-fold larger preference change, while ablations show similar gains for alternative and unconstrained option-gradient directions; nulling the unknown gradient alone is not responsible for the gain. We recommend reporting answerability alongside published scores.

---


### 530. [DisaggKD: Efficient Knowledge Distillation through Teacher-Student Disaggregation and a Fused Loss](https://arxiv.org/abs/2610.17644)

**<font color=#1a73e8>作者：</font>** Ruixuan Tu, Yuyang Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) frameworks place teacher and student on the same GPUs, so per-GPU memory limits the teachers that fit. DisaggKD separates them across nodes: teacher replicas stream hidden states to the student, a KD loss over row windows and vocabulary shards equals the full-vocabulary loss in exact arithmetic without forming the full-vocabulary logits, and a prefetch ring paces producer and trainer. Closed-form memory and traffic models locate the memory limits of each layout. On the Qwen3.5-35B-A3B to 9B pair, the disaggregated layout matches the LM loss of the colocated run with the same loss and is faster than that run; our fused loss also lets a colocated run train on as few nodes at faster speed, while the split is memory efficient when the student spans several nodes. On the larger pairs, colocated runs with a fused loss still run OOM where the split trains, because teacher weights and student states fill the budget.

---


### 531. [Decouple to Forget: Semantic Mediation for Sensitive Unlearning in Large Language Models](https://arxiv.org/abs/2610.17654)

**<font color=#1a73e8>作者：</font>** Jingyue Cong, Andy Song, Yang Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning for large language models seeks to remove specified knowledge while preserving general capability, yet current methods often treat an entire response as the unit of forgetting. This coarse granularity causes unnecessary utility loss when the forget target is only a small set of sensitive facts embedded within otherwise benign explanations. In this paper, we introduce Decouple to Forget (D2F), a targeted unlearning method inspired by semantic mediation that separates sensitive factual content from non-sensitive meaning and surface expression. For each example to be forgotten, D2F extracts a fact-level "mediator" representation from the answer, identifies which parts are sensitive, and removes only those parts while leaving the rest of the structure intact. We then generate counterfactual answers grounded in this mediator that preserve non-sensitive content but exclude sensitive facts, employing preference-based contrastive optimization to reduce the likelihood of information leakage while maintaining helpfulness and fluency. Experiments across various benchmark datasets show that D2F achieves a better balance between forgetting and retention than strong baseline methods. Our code is available at this https URL.

---


### 532. [Open-o3-Video-v2: Seek, Ground, and Reason with Verifiable Spatio-Temporal Evidence](https://arxiv.org/abs/2610.17656)

**<font color=#1a73e8>作者：</font>** Jiahao Meng, Zhongyuan Bao, Yue Tan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable video reasoning requires models to produce correct answers and expose supporting visual evidence. Open-o3-Video enables verifiable reasoning by embedding timestamps and object-level bounding boxes into reasoning traces, but is restricted to frames from an initial sparse sampler. We introduce Open-o3-Video-v2, which formulates video reasoning as a unified agentic evidencegrounded process. The model identifies missing information, acquires additional observations, grounds the moments and objects supporting its reasoning, and writes this evidence into the trajectory before continuing or answering. To support this behavior, we construct STGR-v2-CoT135K, including 52K multi-turn agentic grounded reasoning trajectories, and STGR-v2-RL-13K for reinforcement learning. We further propose Clue-Seek GRPO (CS-GRPO), which tracks how tool calls change accumulated evidence, rewards clue coverage and step-wise gains, and penalizes excessive, repetitive, or uninformative retrieval. On V-STaR, Open-o3-Video-v2-4B achieves 40.4% mAM and 56.3% mLGM, outperforming its Qwen3-VL-4B backbone by 8.5% and 12.6%, respectively. It also delivers consistent gains across general video understanding, long-video reasoning, and temporal grounding benchmarks. These results show that active evidence acquisition and verifiable object-level grounding are complementary for reliable video reasoning. The code and models are released at this https URL.

---


### 533. [Worth Their Weights? Evaluating Generative Models for Discourse Parsing](https://arxiv.org/abs/2610.17658)

**<font color=#1a73e8>作者：</font>** Luke Gessler, Amir Zeldes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rhetorical Structure Theory (RST) parsing has historically been dominated by discriminative models based on pretrained encoder-only language models. The recent availability of high-quality generative language models has made it unclear whether RST parsing is better approached as a generative task. In this work, we investigate whether generative language models are better at parsing RST than traditional discriminative ones. We find that at matched parameter counts, discriminative parsers perform much better than generative ones, though much larger generative models sometimes outperform them. Generative models hold a particular advantage in elementary discourse unit (EDU) segmentation, and we report new state-of-the-art results on the RST-DT benchmark in end-to-end parsing as well as segmentation.

---


### 534. [The Image Still Has a Say: Final-Answer Repair for Multimodal Chain-of-Thought](https://arxiv.org/abs/2610.17663)

**<font color=#1a73e8>作者：</font>** Yulan Pan, Xiaoyu Xu, Zhihong Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although chain-of-thought prompting has improved multimodal reasoning, it is still difficult to produce correct final answers, as the reasoning can drift away from the image. Besides, the trace is already fixed when the answer is generated, leaving no room for self-correction. Considering the image is still available at the final-answer step, we think it is reasonable to fix the answer there without rewriting the reasoning. As such, the problem becomes to correct the final answer using the image under fixed reasoning. Unlike methods that improve trace generation through training, resampling, or decoding-time grounding, we repair the final-answer readout while keeping the reasoning trace fixed. The motivation is based on our finding that a wrong option can become prematurely committed in the reasoning while the correct option still has stronger image support in middle-to-deep layers. Thus, we propose Text-to-Visual Evidence Reallocation (TVER), a training-free method for final-answer repair. Specifically, TVER selects answer-related text and question-matched image patches, and moves bounded attention from text to patches. Furthermore, the patches are chosen in a middle-to-deep layer window based on question relevance. Our method improves answers across benchmarks and backbones, with gains in both multiple-choice and open-answer evaluations.

---


### 535. [RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment](https://arxiv.org/abs/2610.17665)

**<font color=#1a73e8>作者：</font>** Qingchuan Ma, Yuexiao Ma, Xiang Meng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can vision-language models turn 2D observations into 3D understanding that supports precise action? This requires inferring object geometry, anticipating the effects of rotation, and refining actions through visual feedback. We introduce RoTA-Bench to evaluate these abilities through interactive 3D-to-2D projection alignment. Given a target silhouette, a model observes a rotated object and chooses successive rotations to recover the target projection within a limited action budget. Our automated pipeline constructs silhouette-preserving 3D objects from 2D icons and uses reversible initialization to guarantee solvability, yielding 674 tasks and a stratified 100-task test set. Empirically, we find that (i) a substantial human-model gap persists: GPT-5.6-Sol succeeds on only 17% of tasks, whereas 20 undergraduate participants collectively complete the test set four times with a 100% success rate; (ii) image-space and pose-space progress can diverge: at matched states, the model more often improves silhouette overlap while worsening pose alignment than humans (19.4% vs. 10.9%); and (iii) fine-grained control is sensitive to interaction history: removing it leaves 96.8% of the model's actions at a coarse 30-degree step size and sharply reduces observed task success. These findings highlight the challenge of converting visual evidence into precise 3D control, beyond recognizing or matching individual images.

---


### 536. [DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter](https://arxiv.org/abs/2610.17666)

**<font color=#1a73e8>作者：</font>** Xuyan Ye, Xiyan Fu, Shengda Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled outcomes, while direct step scoring may require costly external evaluators, human annotations, or task-specific heuristics. We introduce DeltaTTG to learn a reusable progress signal through a shared progress meter, using low-cost supervision from diverse policies' recorded trajectories without task-specific progress rules. Its supervision target, Token-to-Go (TTG), the number of tokens remaining to be generated until task completion, serves as an observable proxy for remaining completion effort. During actor training, changes in the frozen meter's estimates redistribute outcome-derived advantages across steps without altering the reward, preserving each trajectory's advantage sign and token-average scale. On ALFWorld, PaperSearchQA, and BFCLv3, DeltaTTG improves the average score over GRPO by 5.7 and 7.2 points with Qwen3-4B and Llama-3.1-8B-Instruct, respectively, outperforms all compared RL baselines on average, and keeps actor-training GPU-hours close to GRPO. Further experiments show improved sample efficiency and out-of-domain performance, and support the meter's ability to distinguish step quality and guide test-time action selection across actor sizes. The code is available at this https URL.

---


### 537. [Cowork-Gym: Synthesizing Interactive Work Environments at Scale](https://arxiv.org/abs/2610.17670)

**<font color=#1a73e8>作者：</font>** Anni Zou, Cheng Chen, Jiaji Deng 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cowork agents navigate dependencies across tools and files while adapting to changing user requirements and edits to shared workspaces. Scaling such environments requires maintaining consistency among task objectives, executable resources, user behavior, and success criteria. We introduce Cowork-Gym, a framework that synthesizes Cowork environments through a build-execute-revise loop that uses execution evidence and review feedback to validate and repair generated environments. To capture realistic Cowork dynamics, a stateful user simulator responds to the agent's actions through dialogue and direct edits to the shared workspace. We synthesize 64.9K environments across 14 application scenarios and use them to post-train 9B, 27B, and 35B-A3B Qwen models with supervised fine-tuning, reinforcement learning, and on-policy distillation. Averaged across six agentic benchmarks, these models outperform their corresponding base checkpoints by 8.7, 6.4, and 4.1 points, respectively. Ours-27B ranks second overall among the evaluated models and achieves the highest average scores on PawBench and ClawEval, outperforming models with over 100B total parameters on both benchmarks.

---


### 538. [Encounter-Driven City-Scale Human Mobility Generation with Large Language Models](https://arxiv.org/abs/2610.17672)

**<font color=#1a73e8>作者：</font>** Chao Li, Renhe Jiang, Chuan Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for human mobility generation by modeling individual routines, activities, and mobility preferences. However, existing approaches remain largely resident-centric: generating realistic individual trajectories does not necessarily recover the encounters that emerge when multiple residents co-occur at the same place and time. To this end, we study encounter-aware human mobility generation, which jointly preserves individual mobility and population-level interaction structure. We propose EncounterMob, an encounter-driven LLM framework consisting of a coarse-to-fine Encounter Generator and an Iterative Coupling Framework. The Encounter Generator first captures city-level encounter rhythms and then instantiates participant-time-venue encounters, while the Iterative Coupling Framework coordinates these encounters with personal mobility behavior through successive refinement. We further introduce an encounter recovery protocol covering encounter marginal and joint distributions over residents, times, and venues. Experiments on the Japan and NYC datasets show that EncounterMob outperforms all external baselines on all seven encounter metrics and all six personal mobility metrics. Compared with ELLMob, it reduces the participant-time-venue joint error by 40.4%/41.7% and the mean personal mobility error by 58.8%/32.7% on Japan/NYC, respectively.

---


### 539. [Dynamic K-Head: Difficulty-Supervised Budget Selection for Continuous Latent Reasoning](https://arxiv.org/abs/2610.17679)

**<font color=#1a73e8>作者：</font>** Ying Li, Yuqi Chen, Sixuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) improves reasoning but incurs substantial autoregressive rationale cost. Continuous CoT moves intermediate computation into recurrent hidden states, yet typically uses a fixed number of updates even though the best budget varies across questions and accuracy need not improve monotonically with $K$. We introduce Dynamic K-Head, a question-conditioned, pre-rollout budget selector. It is jointly trained with the reasoner under selected budgets, using difficulty supervision based on scores assigned from the question alone. We also show that latent-update count can misrepresent end-to-end cost because a short latent rollout can shift computation into a longer explicit continuation. We therefore count latent updates, implementation-specific special tokens, and all decoded text. Instantiated with CoDI on Llama 3.2 1B and GSM8K, Dynamic K-Head reaches 54.44% exact-match accuracy at 12.03 average reasoning/output tokens, compared with 52.31% at 15.21 tokens for fixed-$K=6$ CoDI---a 2.12-point gain with 20.9% lower token cost. Across three out-of-distribution arithmetic datasets, it reduces cost by 19.3--25.7% while improving accuracy by 0.30--2.22 points. These results demonstrate that difficulty-supervised budget selection can improve both accuracy and efficiency, while stable budget selection remains a central challenge.

---


### 540. [Encoding Context into LLM Weights: What Makes It Context?](https://arxiv.org/abs/2610.17686)

**<font color=#1a73e8>作者：</font>** Yue Wang, Qizhou Wang, Feng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Longer contexts allow large language models (LLMs) to condition their predictions on more information, but inference costs grow prohibitively with context length. An emerging alternative uses test-time updates to encode context as temporary changes to model weights. However, encoding this information into weights that already represent general knowledge obscures its role as context, so the LLM may fail to use it properly to condition subsequent inference. To restore this contextual role, we first associate each context with an identifier during encoding, thereby distinguishing the newly encoded information from pre-existing knowledge. Invoking the identifier at inference then enables the LLM to recite the encoded context. Nevertheless, successful recitation does not ensure that the LLM will use the recalled information as context. We therefore further introduce a prompting framework that explicitly guides the LLM to use this information as context. Across diverse controlled tasks and practical benchmarks, our method outperformed the baseline using only off-the-shelf LLMs, showing its advances in context encoding.

---


### 541. [Stable Token-level Scheduling for Serverless LLM Inference](https://arxiv.org/abs/2610.17689)

**<font color=#1a73e8>作者：</font>** Hardi Ashishbhai Desai, Balaji N K, Sourav Kanti Addya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serverless inference is emerging as an efficient deployment model for Large Language Models (LLMs) due to its ability to elastically scale resources, improve GPU utilization through resource sharing, and reduce infrastructure costs. However, existing approaches primarily optimize time to first token (TTFT) while overlooking inter-token latency (ITL), a key determinant of user experience during response generation. We observe that LLM inference comprises a computation-intensive prefill stage and a bandwidth-bound decode stage, where admitting new requests can disrupt ongoing decoding and increase latency. To address this, we propose Token Window Pacing (TWP), a closed-loop scheduling framework that leverages runtime feedback from ITL, queue depth, and workload characteristics to regulate request admission at the token level instead of the batch level. TWP dynamically adjusts a selfregulating token window and incorporates chunk-based prefill to minimize interference from incoming requests. Experiments on realistic serverless workloads show that TWP delivers stable TTFT, significantly reduces latency spikes, lowers P99 tail latency, minimizes ITL variation, and improves throughput by up to 45% over ServerlessLLM and 58% over conventional schedulers. These results demonstrate that feedback-driven tokenlevel scheduling enables stable, high-throughput serverless LLM inference without modifying the underlying model.

---


### 542. [MedEvo: Medical Reasoning Evolution through Knowledge Navigation](https://arxiv.org/abs/2610.17690)

**<font color=#1a73e8>作者：</font>** Xiaoliang Wang, Zhuo Chen, Chuanyang Zheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical multimodal reasoning models are typically trained on teacher-generated rationales, discarding the valid reasoning in students' own failed trajectories, while general-domain correction methods offer little guidance for errors in image reading, anatomical context, or differential diagnosis. We propose MedEvo, which uses medical knowledge, namely a tag taxonomy and error-type diagnosis, to navigate both trajectory repair and data selection. For each failed rollout, a gold-blind auditor locates the first consequential error and provides a minimal, answer-free hint; the same student retains the valid prefix and regenerates the erroneous suffix. After each round, MedEvo identifies capability gaps across medical tags on a held-out feedback set and prioritizes related questions for new rollouts and repairs. With supervised fine-tuning (SFT) alone, MedEvo raises Qwen3.5-9B mean accuracy across seven benchmarks from 65.57% to 69.12% (47.40% to 54.50% on the multimodal track of MedXpertQA (MedXpertQA-MM)), surpassing teacher-distillation SFT (66.93%). It also raises Qwen3.5-35B and Qwen3.5-397B mean accuracy from 67.91% to 73.04% and from 71.83% to 74.95%, respectively. Our analyses show that failed trajectories contain reasoning worth preserving, that repair success does not imply learning value, and that independent feedback is key to sustained improvement.

---


### 543. [LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification](https://arxiv.org/abs/2610.17697)

**<font color=#1a73e8>作者：</font>** Rodney Lafuente-Mercado, Salman Rahman, Jingyan Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems now write long and difficult mathematical proofs, and checking their step-by-step validity is becoming a bottleneck. A learned verifier could check proofs cheaply, but training one requires a correctness label on every step, and such labels are hard to obtain for open-ended proofs. Existing methods take them from human annotators, which is costly, or derive them from final answers, which proofs do not have, and formalizing each proof in Lean requires expert effort. We introduce LeanPRM, a framework that uses the Lean proof assistant to create step-level labels for natural-language proofs. A model writes a natural-language proof together with a paired formal proof, without feedback from Lean. Lean then labels every step, and a second model discards failures caused only by the formal syntax, so that the negative labels mark errors in the mathematics. LeanPRM contains 10,634 proofs with 152K labeled steps and no human annotation. A Qwen3-4B verifier trained on LeanPRM raises exact step-label accuracy on a held-out set of 200 proofs (LeanPRM-Bench) from 48.2 to 74.7, as opposed to 60.3 when the same base model is trained on PRM800K. It also selects better proofs in best-of-N selection on IMO-level problems, and outperforms the PRM800K-trained verifier on three of four external verification benchmarks. Training on LeanPRM improves verifiers at every size from 0.6B to 8B parameters on LeanPRM-Bench, Hard2Verify and IMO-GradingBench. Given the labels need no human annotation, LeanPRM can grow with the supply of formal statements, offering a path to step-level feedback on AI-generated proofs that are hard for humans to check.

---


### 544. [Pushback in a Haystack: Language Models Respond to Factual Errors Ambiguously and Ineffectively](https://arxiv.org/abs/2610.17703)

**<font color=#1a73e8>作者：</font>** Li Lucy, Myra Cheng, Svenja Guhr 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The sycophancy of language models, or their failure to push back against faulty user input, is now widely studied. However, if LMs do push back, is sycophancy solved? We show that LMs vary in how they present pushback, and thus vary in how effectively they correct user beliefs. We introduce a phrase-level, human-validated response labeling framework to uncover fine-grained insights into how LMs push against and/or affirm false inputs. We develop and apply our framework on model responses in five languages: English, German, Chinese, Hindi, and Yoruba. We find that when models do push back against users' false assertions, they tend to use indirect phrasing and mix in affirmation, with more indirectness in Hindi and Yoruba than in other languages considered. In a large-scale human study (n = 300), we find that the pushback ambiguity we identified may fail to correct and prevent users' factual misconceptions.

---


### 545. [From Token Correction to Claim Admission: Training-Free Hallucination Mitigation for Large Vision-Language Models](https://arxiv.org/abs/2610.17706)

**<font color=#1a73e8>作者：</font>** Hyeonggeun Han, Taehyun Cho, Sangwoo Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models often exhibit object hallucination, generating claims that are not supported by the input image. To mitigate this issue, we propose Evidence-Guided Visual Claim Admission (EGVCA), a training-free framework that admits a semantic claim only when it receives sufficient image-dependent support. EGVCA measures this support by comparing the claim likelihood under the observed image and a visual-null input. For captioning, it controls semantic expansion without altering token generation. For binary visual question answering, it combines atomic visual support with the image-induced change in the model's native Yes--No margin. Experiments on CHAIR, POPE, and MME across three LVLM backbones show that EGVCA substantially reduces object hallucination while preserving caption quality. It achieves the highest POPE F1 in eight of nine backbone--sampling settings and improves the native MME total score on all three backbones. These results demonstrate the effectiveness of claim-level admission as a simple alternative to token-level distribution correction.

---


### 546. [Confine to the Task, Anchor the Rest: Concept-Guided Retention Regularizer for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2610.17713)

**<font color=#1a73e8>作者：</font>** Ibna Kowsar, Ivan Medri, Fanyu Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has been widely used, yet the adapted model suffers catastrophic forgetting of pre-trained knowledge. While most existing work hardens the adapter by constraining where the weight update may lie, we note that constraining this weight channel does not constrain the activation channel. In this paper, we propose Concept-Guided Retention (CGR), a plug-and-play regularizer that constrains both for any PEFT base. CGR reads a frozen sparse autoencoder (SAE) and treats two disjoint concept sets differently. It softly confines the update to the task-concept subspace (via weight channel), and anchors a selected set of general-purpose concepts to the frozen model (via activation channel). We also provide anchor value bounds based on weight updates to understand how they interact, and show that both terms are necessary. On a CLIP vision panel, CGR significantly improves retention at comparable accuracy for every base, and the same pattern holds for world-knowledge retention under Llama-3.1-8B instruction tuning. Because the protected directions are named SAE concepts, CGR remains inspectable and controllable.

---


### 547. [ECG-RSI: Recursive Self-Improvement through Targeted Electrocardiogram Waveform Evolution](https://arxiv.org/abs/2610.17718)

**<font color=#1a73e8>作者：</font>** Xiaoliang Wang, Zhuo Chen, Chuanyang Zheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) models need supervision that targets evolving weaknesses and remains faithful to waveform evidence. We introduce ECG-RSI, a recursive self-improvement framework combining verified waveform synthesis with feedback-guided intervention search. Signal remeasurement verifies waveform edits; construction errors guide generator repair, while learner errors motivate interventions compared on a separate selection set. Across seven benchmarks, three rounds raise Qwen3.5-35B-A3B's mean question-answering accuracy from 34.57% to 56.04% and mean classification F1 from 24.27 to 34.03. Across the retained trajectory, the preferred supervision shifts from direct reinforcement to confusion-focused contrasts. Continued feedback correction yields diminishing external gains. These results motivate separating error diagnosis from intervention selection and checking whether gains on the feedback set transfer to independent benchmarks.

---


### 548. [Upstream Influence, Downstream Re-Anchoring in LLM Agent Chains](https://arxiv.org/abs/2610.17723)

**<font color=#1a73e8>作者：</font>** Chun-Yu Hsu, Lun-Wei Ku, Chung-Chi Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People act on evaluative judgments produced by LLM agents, and in multi-agent systems those judgments pass through several agents before reaching a person. We show that a workflow's information architecture---source access, handoff format, and which model reads the untrusted content---governs how much of a coordinated manipulation reaches the end. On 32 Taiwan~2025 recall cases, ten authentic Threads comments shown to one agent move its stance by $+0.171$ toward the injected position, and a mirrored set moves it the other way. Passing that judgment down a chain removes more than half of the shift by the third agent; keeping the comments in front of every agent sustains more of it. The reduction is not attrition in transit: each receiver discounts the inherited stance in proportion to how far it sits from its own reading of the evidence, returning to what that evidence implies for the case rather than to neutrality---consistent with partial re-anchoring. Handoff format is a second lever: a stance relayed without its reasoning is largely discounted. Susceptibility at the exposed seat varies fourfold across models, while the chain's arrangement does not matter at all. None of this is visible in the transcripts---the injected claims are almost never restated, so reasoning-trace audits miss the attack.

---


### 549. [Evidence-First Agentic Verification](https://arxiv.org/abs/2610.17724)

**<font color=#1a73e8>作者：</font>** Reza Sanayei, Razvan-Gabriel Dumitru, Sunjie Hou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon, semi-verifiable agentic tasks often rely on rubric-based evaluation, but the evidence needed to assess these tasks can be spread across the environment state and the execution trace. A judge may overlook this evidence or accept unsupported claims, including an agent's own reports of success. When rubric verdicts serve as reinforcement-learning rewards, such errors can reinforce undesirable behavior. We introduce Sauron, an evidence-first agentic verifier that investigates both state and trace and relies on a claim only after independently validating it against its source. Bounded queries and joint investigation of related criteria reduce context use and redundant work, and each verdict carries an auditable receipt of its supporting evidence. Across 2,586 human-labeled criteria from 100 personal-assistant episodes, Sauron achieves the highest F1 of five verifiers on all eight backbones tested while costing less than Gandalf, the strongest baseline. With GPT-5.6 Sol, it reaches 0.96 F1 versus Gandalf's 0.92 at 23% lower cost, with a wider margin on process criteria. On a paired fault-injection suite covering 13 families, several of which simulate reward hacking, Sauron detects 97% of injected failures while flagging only 2% of clean controls, outperforming baselines even when they are given the full trace. On TRAIL, a benchmark for detecting and localizing real agent errors, Sauron leads both Gandalf and TRAIL's own judge on all three quality metrics.

---


### 550. [TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training](https://arxiv.org/abs/2610.17726)

**<font color=#1a73e8>作者：</font>** Yuqian Fu, Kaiwen Jiang, Zijun Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents excel at complex, multi-step tasks but suffer from catastrophic forgetting during continual learning--acquiring new skills often degrades previously mastered capabilities. Existing post-training paradigms face a fundamental trade-off: Supervised Fine-Tuning (SFT) is sample-efficient but prone to severe forgetting, while Reinforcement Learning (RL) preserves prior capabilities but converges slowly without expert guidance. To bridge this gap, we introduce Trigger-based Supervised Reinforcement Learning (TSRL), a framework that integrates the strengths of both paradigms through an adaptive, state-dependent expert supervision mechanism. TSRL employs RL as the optimization backbone, activating SFT selectively on "hard states" where the policy fails. Theoretically, we show that restricting supervision to failure states derives an upper bound on the cumulative parameter updates, thereby reducing forgetting compared to full SFT. Empirically, TSRL achieves consistent gains across three agent benchmarks (ALFWorld, WebShop, and Deep Search) at both 7B and 32B scales. In continual learning scenarios, our method retains up to 9.6 points more capability on prior tasks than SFT->RL baselines, while matching or exceeding target-task performance.

---


> [!TIP]
> 当前位于：**501-550**（第 11/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
