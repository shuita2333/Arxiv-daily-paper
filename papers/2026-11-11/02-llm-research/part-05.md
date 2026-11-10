# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 201. [Beyond Hard Labels: LLM Probabilities Improve Human-Assisted Regression](https://arxiv.org/abs/2611.11111)

**<font color=#1a73e8>作者：</font>** Xinyue Wang, Qunhua Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for text annotation, but their outputs are often reduced to a single categorical label before downstream analysis. This hardening step discards the model's relative support across categories, which may contain useful information when category boundaries are ambiguous. We study whether retaining the full probability vector improves downstream regression when LLM annotations are combined with a limited amount of human annotation. Using matched soft and hard representations from three LLMs across three social-science text datasets, we compare direct regression and human-assisted correction. Soft inputs are not uniformly better when used directly as outcomes, but after human correction, using the probability vector consistently improves regression efficiency across models and datasets. Analyses of repeated human judgments and controlled simulations further show that these gains arise when probability variation beyond the hard category carries useful information about the human-coded outcome. Our results identify output representation as an important design choice in LLM-assisted measurement and support preserving probability outputs for downstream statistical analysis. Code and reproducibility materials are available at this https URL

---


### 202. [Compositional Conformal Risk Control for Multi-Stage LLM Cascades](https://arxiv.org/abs/2611.11114)

**<font color=#1a73e8>作者：</font>** Yuxia Sun, Jiahuang Wang, Haoting Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-stage large language model (LLM) cascades balance accuracy and inference cost, but reliable deployment also requires controlling error risk and identifying its sources across stages. We propose Compositional Conformal Risk Control (CompCRC), a risk-control framework for pre-specified multi-stage LLM cascades. We decompose the risk of accepting incorrect answers into additive stage-wise contributions over the full query population, linking local risk budgets to a system-level guarantee. CompCRC constructs and freezes candidate budget allocations and acceptance thresholds, selects one candidate on independent data, and certifies its stage-wise risk contributions on separate held-out data. Under conditional exchangeability, we establish a finite-sample guarantee: the marginal expected accepted-error risk of the complete deployment procedure does not exceed the global risk budget. At the reported comparison budget of $\alpha=0.45$, all three stages of CompCRC pass their local checks on MMLU, GSM8K, and HellaSwag. Compared with Global-CRC, which passes system-level risk certification at the same budget, CompCRC reduces observed accepted-error risk by 1.33--2.00 percentage points, improves final accuracy by 0.67--2.00 percentage points, and reduces weighted inference cost by 30.37\% on HellaSwag. The selected cost-based budget allocation also improves accuracy per unit cost by 10.6\%--46.7\% over uniform allocation. Further experiments show that stage-wise statistics identify stages that fail local certification checks, providing diagnostic information alongside system-level risk control.

---


### 203. [Query-Only Prompt-Agnostic Attacks on Visual In-Context Learning](https://arxiv.org/abs/2611.11116)

**<font color=#1a73e8>作者：</font>** Xiao Hu, Muhammad Ibrahim, Hao Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual In-Context Learning (VICL) enables promptable segmentation by conditioning RGB predictions on visual demonstrations, making it attractive for auto-labeling, but its robustness under query-only access and unknown deployment prompts remains underexplored. We study query-only, prompt-agnostic targeted attacks where the attacker observes only returned RGB outputs, without access to model internals or deployment prompts. Treating prompt-conditioned RGB rendering as a distinct attack surface, we introduce two appearance-space attacks: Color Hijack (CH) drives foreground colors toward the background to suppress visibility, while Task Hijack (TH) collapses instance-distinguishing colors toward a shared color assignment. To transfer across unseen prompts, we propose a Self-Prompt Surrogate (SPS) constructed from the clean query and its output. In a paired, matched-budget SegGPT comparison, SPS outperforms the Random-Prompt Surrogate (RPS), reducing CH instance foreground retention from 0.918 to 0.155 and TH palette-aware tolerance distance from 0.345 to 0.225. Across four VICL models on COCO and HierText, CH suppresses foregrounds across semantic-, instance-, and text-style outputs, while TH collapses instance colors under held-out deployment prompts. After palette-based decoding, TH also reduces the decoded instance count and mask retention while increasing instance merges. Finally, at 30% corruption, CH-corrupted annotations from a publicly accessible VICL-based auto-labeling pipeline reduce downstream YOLO-seg mAP50 from 0.761 to 0.281.

---


### 204. [LongCap: Hour-Scale Timestamped Audio Captioning via Chunk-wise Processing](https://arxiv.org/abs/2611.11125)

**<font color=#1a73e8>作者：</font>** Jinchuan Tian, Sen Chen, Wenbin Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Describing hours of audio requires accurate event timing and sustained descriptive detail throughout the recording. We present LongCap, a framework for timestamped audio captioning (TAC), with the human-annotated LongCapBench and three diarization-inspired metrics: Timeline Error Rate (TER), Granularity Error Rate (GER), and Caption Similarity (tcpCapSim). LongCap interleaves audio chunks with structured event captions, using relative timestamps and retained context to support length extrapolation within a 1M-token inference context window. Event-level reannotation restores caption detail, while systematic studies examine model scaling, dependency supervision, and self-distillation. LongCap-Diar achieves strong benchmark results and extrapolates to 16 hours of concatenated audio despite training on recordings no longer than 40 minutes. Our TAC models are competitive with Qwen3.5-Omni-Plus on short clips, outperform evaluated baselines in caption similarity and timeline accuracy in segment-level comparisons on LongCapBench-TAC-Long, and caption full recordings approaching two hours. On LongCapBench-TAC, 9B and 35B-A3B offer favorable size-performance tradeoffs, while 122B-A10B substantially improves event-dependency recovery. These findings support long-horizon general audio understanding and provide a foundation for always-on voice agents.

---


### 205. [From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models](https://arxiv.org/abs/2611.11136)

**<font color=#1a73e8>作者：</font>** Changran Liu, Qi Wu, Wenchao Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations. We introduce a framework that automatically generates game environments and expert demonstrations. An LLM-powered agent uses game-building tools to construct executable environments and tasks targeting specified skills. Programmatic experts then use privileged simulator state to generate aligned instructions, rendered observations, and keyboard and mouse actions. We train our game policy, Script2Play, by post-training a 4B vision-language model with behavior cloning on 150.3 hours of synthetic Minecraft and Roblox gameplay, without human gameplay demonstrations or reinforcement learning. Evaluation on multiple public game benchmarks demonstrates that Script2Play follows gameplay instructions effectively and generalizes across game engines, highlighting the effectiveness of targeted synthetic supervision.

---


### 206. [DISCOVER: Online Variance-Guided Data Discovery for Budgeted Multimodal GRPO](https://arxiv.org/abs/2611.11145)

**<font color=#1a73e8>作者：</font>** Peyman Gholami, Shivam Chandhok, Saber Malekmohammadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in reinforcement learning have made verifiable rewards a central post-training paradigm for improving multimodal reasoning. However, methods such as GRPO remain data- and compute-inefficient, spending rollout and annotation budget on prompts that provide little learning signal. We propose DISCOVER, an online data-discovery framework for budgeted multimodal GRPO that enables vision-language models to dynamically identify prompts that are most useful for the current policy. DISCOVER first organizes the multimodal sample pool into semantic clusters and queries a small set of density-diverse representative samples to obtain initial reward observations. During training, it estimates the utility of unannotated samples by transferring sparse reward feedback from queried samples. Since sample utility changes as the policy evolves, DISCOVER dynamically updates these estimates with recency-weighted rollout observations. It then selects only high-utility prompts for annotation using a policy-conditioned score that accounts for reward variance and difficulty. Once the discovery budget is exhausted, DISCOVER continues with utility-based replay. Experiments on ViRL39K and VLAA-Thinking with Qwen3-VL-2B show that DISCOVER substantially improves multimodal mathematical reasoning under a strict 10% unique-sample budget, outperforming budget-matched random selection, hard-example sampling, full-pool GRPO under the same training-step budget, and online selection baselines. Ablations further validate the importance of semantic coverage, online reward transfer, and stable discovery cadence, establishing DISCOVER as a practical framework for data-efficient multimodal RL post-training.

---


### 207. [Not All Layers Are Equal in Image-to-Video Transfer](https://arxiv.org/abs/2611.11147)

**<font color=#1a73e8>作者：</font>** Thinesh Thiyakesan Ponbagavathi, Constantin Seibold, Alina Roitberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient image-to-video transfer adapts frozen image foundation models to video via lightweight trainable adapters. Existing methods insert the same adapter at every transformer layer, implicitly assuming all layers require equal temporal modeling. A layer-wise sensitivity analysis across four video-native model families and two pretraining paradigms reveals that this assumption is wrong: temporal sensitivity increases with depth, and the pretraining paradigm determines its growth profile. Vision-only models exhibit a gradual rise, while vision-language models show early suppression followed by late recovery.
This finding motivates STRAP, a training-free adapter placement rule that derives a spatial-to-temporal transition boundary from a paradigm-matched video model. Spatial adapters are assigned before this boundary and temporal adapters after it, without modifying the adapter architecture itself. On four fine-grained action recognition benchmarks, STRAP improves accuracy by up to 11.8% over uniform placement, reduces trainable parameters by 29 to 48%, and lowers inference time by up to 10%. On standard benchmarks, it matches accuracy with fewer parameters. Code is available at this https URL.

---


### 208. [The Race Is Decided Early! A Kernel Law Predicts Lock-In in Majority-Vote Test-Time RL](https://arxiv.org/abs/2611.11165)

**<font color=#1a73e8>作者：</font>** Jaeho Hwang, Sehong Park, Daejin Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning with majority-vote rewards trains a language model on unlabeled questions by rewarding the samples that agree with its most frequent answer. During training, each question locks into one answer, on hard questions often a wrong one, but which answer it locks into is known only after training. In this paper, we show that this outcome is decided early, in a short race driven by sampling noise between the answers that are close at the start, and we derive the probability of each outcome. With a separate logit for each answer, the runner-up wins with a normal tail probability of the initial gap, scaled by an explicit noise constant. In a network, however, the answer logits depend on shared parameters, and through the kernel of these parameters the updates of the trailing answers also change the gap of the two leaders. This spillover shifts the boundary between the starts won by each leader, and a closed form computes the shifted probability from a kernel probe and the start logits. In LoRA experiments with three models from two families, predictions made before training with the kernel frozen at its start value forecast which answer each question locks into better than a logistic model refitted on the outcomes, although they use no fitted constants. The closed form matches these predictions on the runs in which a check before training finds that the two leaders stay above the other answers, and it explains why a law that ignores the spillover needs a strongly inflated step.

---


### 209. [When Self-Consistency Hurts: The Hidden Cost of Majority Voting in Small Language Models](https://arxiv.org/abs/2611.11201)

**<font color=#1a73e8>作者：</font>** Wanrong Yang, Lingfang Li, Jun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study prompted chain-of-thought (CoT) with self-consistency (SC), i.e. sampling N traces and plurality-voting, on small language models, a regime where per-query compute budgets are tight yet SC is commonly applied with a fixed sample budget inherited from large-model practice, regardless of instance difficulty. Across two model families (Qwen-2.5-0.5B, Gemma-3-1B) at FP16 and MLX-Q4 (4-bit quantisation in Apple's MLX framework), on GSM8K and MATH-500, we run 8 per-task and 4 task-pooled experiments at n=200-400 with 1,000x paired-bootstrap confidence intervals (CIs). Our first result is an upper bound: an oracle gate deciding per prompt whether to invoke SC reaches 109-174% of always-SC's accuracy at 23-30% of its compute in all 12/12 cases, so at N=5 always-SC is dominated everywhere on our grid. That margin is exactly the rate at which SC flips correct greedy answers to wrong, here 3-10.5% of prompts, which on Qwen-Q4 x MATH-500 exceeds the wrong-to-right rate and leaves always-SC 3 pt worse than always-greedy. Our second result is a deployable approximation: a gate over greedy-pass signals skips 45-99% of SC calls, with bootstrap CI half-widths under 5 pt, removing 36-79% of always-SC compute. Accuracy retention at those operating points has point estimates of 98.1-98.8%, which we report as point estimates because their CIs are wide (lower bounds 76-86%) over an SC accuracy of only 15-36%. The evidence covers N=5 on two <=1B families and two math benchmarks, which is the scope we claim. Code is available at this https URL.

---


### 210. [Viscot-steer: Disentangling and Transferring Visual Chain-of-Thought via Activation Steering](https://arxiv.org/abs/2611.11209)

**<font color=#1a73e8>作者：</font>** Ningning Wang, Beier Zhu, Xingyu Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual chain-of-thought (visual-CoT), also known as "thinking with images", equips LVLMs with the ability to locate and use key visual evidence for reasoning. However, acquiring such visual-CoT capabilities requires costly post-training and tightly couples them to a specific backbone, making transfer to other LVLMs difficult. Existing cross-model transfer methods typically treat visual-CoT as a monolithic capability, using a unified representation that ignores the functional distinction between grounding and reasoning and introduces stage-irrelevant interventions. To address this problem, we propose Viscot-steer, a training-free activation steering framework for transferring visual-CoT capabilities across heterogeneous LVLMs. Specifically, Viscot-steer first disentangles visual-CoT into grounding and reasoning vectors and extracts them from the source-model layers associated with the corresponding capabilities. It then aligns the vectors with the activation space of the target model and steers the grounding and reasoning layers during bounding-box prediction and reasoning-trace generation, respectively. Across benchmarks covering high-resolution visual understanding, general visual perception and reasoning, and mathematical visual reasoning, Viscot-steer transfers capabilities from different visual-CoT models to architecturally diverse LVLMs and outperforms the strongest capability-transfer baseline by an average of 1.86 percentage points on the primary evaluation metrics.

---


### 211. [Deterministic Narrative Gravity: Bridging Theory of Mind and Historical Simulation through ABM-LLM Architectures](https://arxiv.org/abs/2611.11212)

**<font color=#1a73e8>作者：</font>** Alicia Colmenero-Fernández, Lidia Ortega Alvarado  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Historical social simulation faces a fundamental reproducibility challenge: the stochastic nature of large language models (LLMs) introduces a digital butterfly effect that prevents exact replication across multi-turn runs. Furthermore, the inability to control low-level server parameters in commercial LLM hosting environments severely limits reproducibility. To overcome this opacity, we present a deterministic multi-agent framework coupling LLMs to an Agent-Based Modelling (ABM) pipeline grounded in Theory of Mind (ToM) and Cognitive Archaeology, and validate exact artifact identity within local, pinned execution environments using SHA-256 hashing. Run locally at temperature zero with clean per-call model reloads, the system injects differentiated cognitive states per turn through dissonance-driven behavioural modes and gated internal voices. Evaluating seven model configurations spanning 4B to 31B parameters against an ablated baseline reveals clear operational boundaries. Small models ($\leq$8B) suffer from context capacity overload, producing repetitive, specular dialogue loops. However, at $\geq$12B parameters, the ABM scaffolding breaks the monotonous response patterns seen in ablation. Crucially, these scaffolded models exhibit spontaneous diegetic expansion: they coherently expand scenario lore through tactically motivated, anachronism-free details rather than escalating into aggression. By resisting the structural pull toward premature scene closure, scaffolded sessions sustain an open terminal Narrative Vector ($V_N = \mathrm{Open}$ in 12/21 overall; 9/9 in official $\geq$12B configurations) whereas unscaffolded ablation never does (0/21). This framework provides a transparent, auditable benchmark architecture for virtual archaeology, with the full pipeline released as open-source software to enable independent replication.

---


### 212. [SGA-Sparse: Training Native SwiGLU Gates for Activation-Sparse and Low-Bit LLMs](https://arxiv.org/abs/2611.11223)

**<font color=#1a73e8>作者：</font>** Ruokai Yin, Steven Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation sparsity can reduce FFN weight traffic during single-user LLM decoding, but active channels must be identified early enough to avoid fetching unused weights. In pretrained SwiGLU models, training-free routing with the native gate performs substantially worse than routing with the up activation at high sparsity. We show that this ordering reverses after sparsity-aware training. Based on this insight, we introduce SGA-Sparse, which converts pretrained SwiGLU LLMs into fixed-budget activation-sparse models by training the existing gate projection directly as a top-k router. SGA-Sparse updates all model parameters end-to-end while preserving the original SwiGLU activation and introducing no auxiliary router parameters. After approximately 30B training tokens, LLaMA models from 1B to 8B achieve uniform per-token 75-85% FFN channel sparsity while remaining within 0.2-2.7 pp of their original dense checkpoints in average zero-shot accuracy. Because post-training quantization degrades sparsity-trained checkpoints, we further study two complementary quantization-aware training (QAT) recipes: continued-QAT largely recovers performance at 4-bit weight quantization, while joint-QAT performs better for the more aggressive sub-4-bit target. To compare activation sparsity with dense low-bit quantization, we translate the sparsity-induced reduction in weight traffic into an equivalent bit-width. Under this unified weight-traffic metric, our 2.5- and 1.5-bit-equivalent models establish a new accuracy-traffic Pareto frontier: the 2.5-bit-equivalent models match dense 3-bit QAT accuracy, while the 1.5-bit-equivalent models approach dense 2-bit models and outperform dense ternary models by 1.3 pp on average. These results establish native-gate training as a practical approach for combining high FFN sparsity with low-bit weights.

---


### 213. [TLRS-DPO: Token-Level Risk Scoring for Better Direct Preference Optimization](https://arxiv.org/abs/2611.11232)

**<font color=#1a73e8>作者：</font>** Suxin Ji, Hungtao Wan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is a simple and widely used alternative to RLHF for aligning large language models (LLMs), but its sequence-level objective cannot precisely locate or suppress the local patterns that make an otherwise acceptable response unsafe or undesirable. We propose TLRS-DPO (Token-Level Risk Scoring for Better Direct Preference Optimization), which augments DPO with fine-grained token-level control while remaining fully offline and reference-based. TLRS-DPO introduces a token-level robust compensation term that converts the policy-reference log-ratio on rejected responses into localized risk scores, a curriculum-style schedule that gradually increases the strength of this compensation during training, and a risk-adaptive screening mechanism that selectively penalizes only high-risk tokens instead of entire sequences. This design bridges sequence-level preference fitting and token-level behavior control, and can be implemented as a drop-in modification to standard DPO trainers. Empirically, TLRS-DPO improves alignment quality and safety-relevant behavior with minimal impact on helpfulness compared to strong DPO baselines.

---


### 214. [FRESCO: A Novel Consistency Control for Asynchronous Pipeline Parallel Training](https://arxiv.org/abs/2611.11238)

**<font color=#1a73e8>作者：</font>** Dongyeop Lee, Namhoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous pipeline parallelism can accelerate distributed model training, but suffers from instability caused by inconsistent gradient computations. We identify a fundamental source of this inconsistency: error signals are coupled to forward-time features, not just parameter states. This means that parameters may evolve as long as they preserve forward-equivalence. Leveraging this insight, we introduce FRESCO, which frames asynchronous updates as a constrained optimization problem: it finds the minimal update modification that acts trivially on the activation subspace. We demonstrate that FRESCO consistently outperforms representative asynchronous baselines in LLM pre-training, with the gains most pronounced under deep pipelines and high inconsistency levels: at pipeline depth 32, it reaches the same loss as the strongest baseline with 43% fewer iterations and 30% less wall-clock time, while requiring 8~921$\times$ less memory overhead. Moving beyond the current limitations, FRESCO establishes a new foundation for high-utilization pipeline parallel training, providing a scalable path for large-model development on diverse, resource-constrained systems.

---


### 215. [A Layer-wise Study of How Style Rewriting Breaks the Calibration of Zero-Shot LLM Fake-News Detectors](https://arxiv.org/abs/2611.11239)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Praney Goyal, Raksha Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly asked to judge whether a news article is true, and their stated confidence is often taken at face value. We test what happens to that confidence when an article's writing style, but not its facts, is manipulated, as in recent \emph{style attacks} on fake-news detectors. Tracing how the prediction and its confidence form layer by layer inside the network, we study three model families (LLaMA-3-8B, Qwen2.5-7B, Mistral-7B) on three fake-news benchmarks, and find the same three patterns in every model--dataset pairing. First, on the original articles the models are competent and largely honest judges: they settle on an answer, briefly become overconfident, and then correct their confidence in the final layers. Second, style-rewritten articles break this self-correction: the models become far less accurate, under the strongest attack, worse than random guessing, yet remain just as confident, so they are \emph{confidently wrong} precisely when a warning is most needed. Third, nearly all of the damage comes from rewriting into sensational or emotionally charged styles, while sober, neutral rewrites leave the models' honesty largely intact. The practical implication is that an LLM's confidence about veracity cannot be trusted as a safety signal when an article's style may have been manipulated.

---


### 216. [Saidzoda-Tajik-EmbeddingGemma-300M: Knowing Every Letter Is Not Reading Tajik](https://arxiv.org/abs/2611.11243)

**<font color=#1a73e8>作者：</font>** Tohir Saidzoda, Nekruz Maxudov, Bedil Karimov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> EmbeddingGemma-300M is a small open embedder whose tokenizer represents every Tajik letter, and as released it is weak at Tajik retrieval: on our Tajik law test the right passage is in its top ten results for 49.3% of questions, on tax documents for 45.9%, and on the human-written Belebele Tajik set for 69.8%, against 98.6% on the Russian version of the same set. We present Saidzoda-Tajik-EmbeddingGemma-300M, the same model fully fine-tuned for one epoch on 235,140 question and passage pairs written by our own Tajik language model for laws, tax documents, Wikipedia and web text, with the same mined hard negatives, English and Russian replay, loss, global batch, learning rate and epoch as our earlier Saidzoda-Tajik-E5-Large (arXiv:2611.00592) and BGE-M3 models. After training, law reaches 92.4% and tax 91.7%; on Belebele, the one test written by people, recall@10 rises from 69.8% to 92.6% and the first result is right for 76.6% of questions instead of 51.7%. A checkpoint at step 100 of 466 already holds 88% of the law gain at recall@10. At recall@10 the result is no more than 2.8 points below the two 560M models trained on the same pairs on law, tax and Wikipedia, within the intervals, with 768-dimensional vectors and about half their parameters; at recall@1, for which we have no intervals, it stays 7.0 points behind the E5 model on Belebele. The cost is a drop of 3.0 and 2.8 points in Russian and English recall@1, larger than for the two earlier models. We also report that, according to our run notes, a bfloat16 test run produced a non-finite loss at step 3 which the training framework logged as zero, so training was done in fp32. Our generated test questions come from the same model as the training questions, so we treat those scores as an upper limit until questions written by Tajik speakers exist.

---


### 217. [Primitives and Paths: Predicting What Post-Training Can Do from What the Base Model Already Has](https://arxiv.org/abs/2611.11260)

**<font color=#1a73e8>作者：</font>** Anqi Qu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does reinforcement learning teach language models new capabilities, or merely amplify ones acquired during pre-training? The literature offers evidence for both: pass@$k$ studies suggest RL reweights latent behaviours while some controlled composition studies demonstrate gains beyond simple amplification. We argue that this question has no answer independent of the capability state of the base model, and propose a two-dimensional state space for post-trainability. The first axis, \emph{effective full-solution support}, measures whether successful trajectories can be sampled under a feasible exploration budget. The second axis, \emph{atomic primitive coverage}, measures whether the constituent skills of a solution can be executed when the burden of composition is removed. Together, these dimensions motivate three regimes -- amplification, composition-limited, and acquisition-limited -- each predicting a distinct empirical signature and calling for a distinct intervention. We propose a prospective measurement protocol and investigate the framework using synthetic composition tasks across three small language models. We find that primitive mastery alone does not guarantee that RL can learn a composition. Checkpoints that execute every primitive reliably can fail to improve when complete solutions are never sampled during training, whereas modest composition supervision that establishes nonzero support enables substantial RL gains. The framework reframes mid-training as preparation for post-training: its role is to move models into states from which RL can operate effectively.

---


### 218. [Chatter Attack: Resource Consumption Attack for Large Language Models](https://arxiv.org/abs/2611.11261)

**<font color=#1a73e8>作者：</font>** Yibo Miao, Yichuan Cao, Xiao-Shan Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are powerful but incur substantial inference cost, which can be exploited by malicious users to induce overly long outputs, increasing latency and operational expense. Prior resource consumption attacks either coerce repetition or suppress the end-of-sequence token by lowering its logit value. However, with autoregressive, sampling-based generation, the search space grows exponentially with length and small deviations or unstable trajectories can derail optimization, limiting attack effectiveness and stability. To address this issue, we introduce Chatter Attack, a novel class of resource consumption attacks that optimize adversarial prompts to induce predefined short target phrases, thereby avoiding search-space explosion while still eliciting long responses. Specifically, Chatter Attack triggers self-doubt using short doubt-inducing phrases as the target, and sustains this state throughout generation via inference attention loss and global entropy loss. To extend to black-box settings, we further propose a novel Bayesian Prompt Optimization (BPO) method, which models the objective function globally by constructing a discrete token kernel, efficiently exploring the entire search space using prior information. Extensive experiments across multiple models and datasets show that our method outperforms baselines, with maximum response length increases to 31.5$\times$, and revealing practical resource-depletion risks for real-world LLM inference services.

---


### 219. [ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems](https://arxiv.org/abs/2611.11266)

**<font color=#1a73e8>作者：</font>** Riya Bharathwaj, Akshara Prabhakar, Roshan Ram 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As enterprises delegate consequential work to multi-agent LLM systems, benign-looking requests can escalate into unsafe actions as they propagate across sessions through poisoned shared state, long-context documents, and trusted peer messages: no single message is malicious, yet the assembled tool action is. Prior benchmarks isolate a single agent under prompt injection or score multi-agent attacks by their final output, leaving cross-session erosion of shared state out of scope. We introduce ErosionBench, an environment-grounded benchmark that executes such attacks and verifies alignment decay at the process level, scoring the realized tool call against authorized intent and provenance with deterministic contracts, not output text. Each scenario is authored as a deterministic state graph before any prose is rendered, so every state change traces to a known cause. It spans four enterprise domains and four decay mechanisms across 1,728 scenarios with matched benign controls, labeled against the OWASP Top-10 for LLM Applications, plus 198 image-based attacks, each paired with a text equivalent, so a defense must survive the same attack in either channel. Perimeter defenses suppress attacks only by over-refusing 54-92% of legitimate work, so a low attack-success rate can conceal severe over-refusal. As a reference defense, we propose a calibrated Meta-Auditor pairing synchronous state checks with asynchronous trajectory monitoring; on a family-disjoint 906-scenario held-out split it reaches 98.5% recall at a 2.9% false-positive rate. Since it monitors trajectory, not surface content, its detection is channel-invariant: the strongest auditor flags image-delivered attacks about as reliably as their text equivalents (recall gap $\leq$2 points per model). Across GPT, Gemini, and Claude auditors, calibration keeps false positives low while recall tracks model capability, strongest for Claude.

---


### 220. [How Efficient Is Your Agent? Online Predictive Bounds under Budget Constraints](https://arxiv.org/abs/2611.11279)

**<font color=#1a73e8>作者：</font>** Roy Maor Lotan, Shai Feldman, Yaniv Romano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate AI agents in an online setting where tasks arrive sequentially and, before running each task, we construct an upper predictive bound on its \emph{time-to-success}---the number of interactions until the task is completed successfully. Under a limited budget, some runs are stopped early, so their time-to-success is unobserved (right-censored), and the correctness of the bound may be unknown. We introduce \emph{\textbf{PR}edictive Bounds for \textbf{O}nline \textbf{B}udget \textbf{E}fficiency} (\texttt{PROBE}), a method for constructing calibrated upper predictive bounds while adaptively allocating a limited budget across agent tasks to reduce the anticipated coverage deficit. Our method calibrates the bounds online using inverse-probability-weighted feedback together with a correction designed to minimize coverage deficit while remaining unbiased. We prove that \texttt{PROBE} provides a coverage guarantee for any finite time horizon while satisfying the budget constraint. Experiments on software engineering, retrieval-augmented generation, and instruction following show that \texttt{PROBE} attains a coverage rate closer to the target level with tighter predictive bounds than a calibrated baseline.

---


### 221. [WarBias: A Bilingual LLM Benchmark of Stereotypes About Internally Displaced People and Veterans](https://arxiv.org/abs/2611.11284)

**<font color=#1a73e8>作者：</font>** Viktoriia Makovska, Tetiana Zakharchenko, Oleksandra Ostafiichuk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper contains examples of stereotypes about veterans and displaced people that may be offensive or distressing. Social bias benchmarks for language models commonly examine categories such as gender, race, and religion, often drawn from lists of legally protected characteristics. Veterans and internally displaced people (IDPs) fall outside these lists, and stereotypes about them, which can undermine access to employment, housing, and social participation, remain largely absent from language model evaluation. We introduce WarBias, a Ukrainian--English benchmark of stereotypes about these two groups. Built from a taxonomy of 120 stereotype claims grounded in research and monitoring reports, WarBias contains 1,007 stereotype--counter-stereotype--unrelated sentence triplets and 240 multiple-choice questions per language. A Ukrainian language model selected in a blinded human pilot generated the Ukrainian triplets. At least two independent annotators reviewed each triplet in the annotation cohort. The authors revised items in response to the reviews, and the final release was machine-translated into English. Each claim carries a human severity rating. In a baseline evaluation of six models, four prefer stereotypical Ukrainian sentences about at least one group, most strongly about IDPs, while English scores are mostly balanced. WarBias supports complementary evaluations of stereotypical preferences and context-sensitive judgments, and provides paired forget/retain material for unlearning-based bias mitigation. We document the benchmark's construction, intended uses, and limitations, and offer its construction method as a template for analogous benchmarks in other conflict-affected societies.

---


### 222. [EASE-KV: Diagnosing the Gap Between Memory Availability and Effective Use](https://arxiv.org/abs/2611.11299)

**<font color=#1a73e8>作者：</font>** Di Lu, Zechen Li, Xuanyu Yue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reusable key-value (KV) memory avoids repeatedly prefilling retrieved text, but stored and injected memories do not necessarily become usable evidence. We present EASE-KV, a controlled framework for understanding this gap under fixed candidates and a frozen language model. EASE-KV separates three interfaces: whether required relations are preserved during encoding, whether preserved memories receive appropriate influence during allocation, and whether outcome supervision can identify useful allocations. Matched experiments show that causal encoding improves compositional accuracy by 25.0 percentage points over block-diagonal encoding, while the tested inference-time bridging methods fail to recover the lost contextual information. With unchanged stored states, diagnostic evidence-guided allocation improves LongMemEval accuracy from 31.2% to 38.4%, demonstrating that memory influence can be controlled without re-encoding. However, controllability does not guarantee learnability: binary correctness provides informative reward contrast for 53.0% of sampled query groups, compared with 73.6% under the evaluated shaped-reward setting. These findings show that effective KV memory requires more than retrieval and injection: the required relations must be encoded, preserved memories must receive appropriate influence, and supervision must distinguish better allocations from worse ones.

---


### 223. [Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation](https://arxiv.org/abs/2611.11305)

**<font color=#1a73e8>作者：</font>** Doron Shavit  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents that call tools are exposed to indirect prompt injection: instructions hidden in tool outputs can steer an agent into calls the user never asked for. We present a runtime audit that derives an executable intent graph from the user's objective and the deployment's tool catalog with one LLM call per task, and checks every tool call against it with a deterministic loop that makes no LLM call (median 5.7 microseconds per call). Two further mechanisms recover utility. Lookups of the user's own state bypass the audit, because the harm of an attack lies in its write or outward step. The calls that remain flagged are escalated to a reasoning guardian, in the spirit of tool-integrated reasoning models such as START: a reasoning model that sees only the objective, the plan, the call history without tool outputs, and the flagged call, and can verify facts with a restricted Python-expression tool. A current agent showed no baseline attack success, so end-to-end validation remains open.

---


### 224. [ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping](https://arxiv.org/abs/2611.11306)

**<font color=#1a73e8>作者：</font>** Joseph Marvin Imperial, Daniel Slate, Noam Kolt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents deployed on the open web are becoming more capable of performing actions that may breach contractual provisions and violate computer security laws. In this paper, we introduce ScrapeBench, the first agentic benchmark for empirically evaluating the legal compliance of AI agents with website scraping policies, namely terms of service (ToS) and this http URL directives. Across widely used closed-weight and open-weight AI agents, we find that most agents exhibit low compliance rates (< 5%) when instructed to scrape websites in our sample of 1,626 popular websites that explicitly prohibit scraping. In addition, we observe that even where AI agents actively check the applicable ToS and this http URL, they continue to exhibit low compliance rates. Conversely, in our sample of 269 websites that do not prohibit scraping, we observe that agents sometimes refuse to scrape despite it being lawful, such as Claude Opus 4.6 exhibiting an over-refusal rate of 98.5%. Our human baseline experiments (n = 180 participants) suggest that humans exhibit compliance rates comparable to AI agents but over-refuse at much higher rates.

---


### 225. [SkillCODER: Towards Auditing and Attribution of Copyright Infringement in LLM Agent Skills](https://arxiv.org/abs/2611.11308)

**<font color=#1a73e8>作者：</font>** Enhao Huang, Chunshu Xia, Yiming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills package reusable workflows and task-specific procedures into deployable natural-language artifacts for LLM agents. Their scale and readability make them valuable but vulnerable to unauthorized redistribution and repackaging. Existing prompt copyright auditing methods struggle with long skills and introduce token-level perturbations that compromise readability. We propose SkillCODER for copyright auditing and buyer attribution in a black-box, content-only setting. During embedding, SkillCODER parses a skill into a section-aware intermediate representation, SkillIR, to identify structural anchors. It distributes conditional instructions across these anchors to form an Artifact-Gated Capsule, designed to activate under verification queries and remain dormant otherwise. Controlled-Vocabulary Error-Correcting Codes encode buyer-specific fingerprints through controlled lexical choices within the capsule. During verification, the defender issues paired positive and negative probes, extracts capsule evidence, and recovers ownership and buyer identity through error-correcting decoding. Across three domains, six models, and three agent frameworks, SkillCODER achieves 99.2% owner verification and 99.3% buyer Top-1 attribution accuracy while preserving task fidelity, substantially outperforming prompt-level baselines. Embedded signals remain robust under paraphrase, compression, clause deletion, and reorganization. Under five adaptive attacks, including a method-aware LLM sanitizer and multi-buyer collusion, ownership evidence remains reliably detectable while buyer attribution degrades gracefully.

---


### 226. [Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference](https://arxiv.org/abs/2611.11319)

**<font color=#1a73e8>作者：</font>** Devanshu Jha, Gaurav Kumar, Agniva Chowdhury 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context applications, long-lived agents, and multi-agent systems require large language models (LLMs) to process and retain extensive information. In these settings, the KV cache can exceed GPU high-bandwidth memory (HBM) capacity, necessitating offloading to host memory, where CPU-to-GPU transfers can dominate inference latency. While KV cache compression can reduce data movement, query-agnostic compression that guarantees accurate attention for arbitrary queries is extremely challenging, if not impossible. We introduce VerKV, a hybrid approach that provides $(\epsilon, \delta)$ guarantees for approximating attention on any given query. VerKV maintains a compact set of query-agnostic pivotal tokens on the GPU, together with a token-level sketch of the full KV cache, while retaining the complete cache in CPU memory. We introduce a novel stochastic sampling procedure, PoissonComp, to select the pivotal tokens. At inference time, our proposed KVFetch algorithm uses the pivotal tokens and the sketch to estimate the relative error of the resulting attention computation. If the estimate satisfies a user-specified $(\epsilon, \delta)$ tolerance, inference proceeds without accessing host memory. Otherwise, VerKV performs query-aware retrieval to fetch additional tokens from the CPU, refining the attention computation to meet the required tolerance. Thus, VerKV enables attention with bounded approximation error while minimizing CPU-to-GPU transfers. We show that PoissonComp outperforms state-of-the-art approaches to KV cache compression. Combined with KVFetch, it achieves near-dense performance (90-100% of dense quality at 32K context length, averaged over RULER and LOFT), using Qwen3-4B, Qwen3.5-9B and Ministral-3-8B, while reducing the GPU memory footprint by 8-32x and keeping CPU-to-GPU memory fetches within 2-23% of the cache per generated token, depending on the model.

---


### 227. [When Credit Turns Against Tools: Transition-Aware Credit Assignment in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.11330)

**<font color=#1a73e8>作者：</font>** Xiangyu Lu, Zhanke Zhou, Jiazhe Ning 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning with verifiable rewards trains language models through multi-turn tool interactions, yet their reasoning performance and tool-calling ability can decline during training. We trace this degradation to three coupled mechanisms: (1) tool-token imbalance produces negative overall tool credit when incorrect trajectories contain more tool tokens per turn than correct ones; (2) aggregation amplification can further strengthen this negative signal as token-mean aggregation gives longer incorrect trajectories greater weight in policy updates; and (3) failure-driven retries prolong trajectories as models tend to call tools again after execution errors, extending potential negative credit to recovery attempts. To counter this suppression, we propose Transition-Aware Credit Assignment (TACA), which targets the transition from reasoning to tool use through supervision of both call initiation and generation. Specifically, TACA uses Advantage Projection to enforce a nonnegative mean advantage on tool-call tokens within each prompt group through a minimal uniform shift. Additionally, TACA guides tool-use decisions with Decision Contrast, comparing rewards for tool-assisted and direct answers to the same prompt. Through Supervised Replay, it reinforces tool-call generation using calls from previously sampled correct trajectories. Across models and tasks, TACA improves performance and sustains more reliable tool interaction during training, raising mean accuracy over MT-GRPO on six reasoning benchmarks by 4.61 percentage points for Qwen2.5-1.5B and 3.61 for Qwen2.5-3B. Our code is available at this https URL.

---


### 228. [Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines](https://arxiv.org/abs/2611.11344)

**<font color=#1a73e8>作者：</font>** Chentao Cao, Zhanke Zhou, Sangni Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning requires understanding how objects and observers are arranged in a scene and how their relations change with viewpoint or movement. Vision-language models (VLMs) typically perform both steps through model-internal reasoning, forming an implicit scene interpretation from partial views and imagining the consequences of spatial transformations. A misread scene can lead to a wrong answer, while even a correct interpretation does not ensure that imagined transformations satisfy spatial constraints. We introduce Spatial Harness, which represents scenes as explicit and executable world states to ground spatial reasoning in physics-engine feedback. A Perceiver integrates scene constraints extracted from the question with specialized visual estimates to place objects and cameras in a shared coordinate frame. The resulting state is instantiated in a physics engine, where a Reasoner executes viewpoint changes and uses computed measurements and rendered views to guide reasoning. We evaluate on MindCube, SAT, MMSI-Bench, and SpatialRGPT-Bench with open- and closed-weight VLMs. On MindCube, Spatial Harness improves Qwen3.5-27B from 52.70% to 71.14%, surpassing pySpatial by 7.52 percentage points. Given identical annotated object and camera poses, it reaches 98.25% versus 71.81% for model-internal reasoning. Code is publicly available at: this https URL

---


### 229. [Separation of Skilling Context for Standard Operating Procedure-based Agents](https://arxiv.org/abs/2611.11348)

**<font color=#1a73e8>作者：</font>** Mitsuhiro Nakayama, Toshiaki Sota, Takehiko Yamaguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard Operating Procedures (SOPs) are kept concise for human readability, so LLM agents that generate executable skills from them lack the tacit knowledge and implementation details needed for automation. Human intervention fills these gaps, but must be repeated as SOPs evolve---a problem we call \textit{SOP-skill drift}. We propose managing SOPs and Contextual Knowledge (CK) separately, together with a \textit{contract-aware} evaluation that distinguishes genuine violations from CK-resolved differences. On eight Indeed-derived workflows (single LLM), it raises the functional-equivalence rate from 12\% to 58\%. Under three SOP-revision perturbations, previously extracted CK already covers 79.5\% of newly introduced automation gaps.

---


### 230. [AOP-Smart-Finder: A High-Throughput Human-AI Hybrid Framework for AOP Discovery and Evidence Mapping from Large-Scale Literature](https://arxiv.org/abs/2611.11349)

**<font color=#1a73e8>作者：</font>** Qinjiang Niu, Lu Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of scientific literature and the high heterogeneity of biological terminology and mechanistic descriptions make it difficult for researchers to integrate scattered research evidence, identify connections among biological events, and construct mechanistic networks. Here, we developed a high-throughput human-AI hybrid framework, AOP-Smart-Finder, for biological event discovery, relationship mining, and Adverse Outcome Pathway (AOP) construction and evidence mapping from large-scale literature. This framework integrates Large Language Models (LLMs), AOP-Smart retrieval-augmented generation (RAG) technology, and Python-based automation, supporting two analysis modes: one based on a single compound and the other based on a predefined set of biological events. In the di(2-ethylhexyl) phthalate (DEHP) case, the system processed 12,983 articles within 30 min and included 1,093 of them, from which it extracted 1,589 biological events (including 458 official key events [KEs] and 1,131 candidate KEs) and 2,519 key event relationships (KERs). In the amyotrophic lateral sclerosis (ALS) case, the system identified 55 stressors from 437 articles and extracted 278 biological events and 548 event relationships. Following manual curation and Weight of Evidence (WoE) evaluation, a mechanistic network comprising 16 KEs and 23 KERs was ultimately constructed. This framework can either use existing AOPs as knowledge guidance for mechanistic expansion and evidence supplementation, or discover novel event connections and construct mechanistic networks around user-specified research topics. It provides a high-throughput, traceable, human-AI hybrid methodology for complex biological mechanism elucidation and AOP discovery driven by large-scale literature.

---


### 231. [NuJEV: Structured Visual Judgments for Consistent Nuclei Quantification](https://arxiv.org/abs/2611.11359)

**<font color=#1a73e8>作者：</font>** Yonghuang Wu, Pengfei Wang, Zhenyang Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nuclear quantification requires locating and typing nuclei, beyond generating a count. Inspired by Jev's structured decisions in place of free-form generation, we introduce NuJEV for nuclear perception in Qwen3-VL-2B. We jointly train visual LoRA and a parallel head to predict nuclear presence, centers, and types. One image encoding feeds both the nuclear head and original language decoder. The decoder interprets region and type requests, with counts computed from the predicted nuclei. On 2,732 PanNuke test images, NuJEV achieves a five-query mean absolute error ($\mathrm{MAE}_5$) of 1.844 overall and 5.268 on dense images, with localization/typed F1 of 0.816/0.682. A matched encoder ablation shows 41.0\% lower dense error with visual adaptation. For language requests, NuJEV reduces request MAE by 76.2\% relative to direct generation. Our code will be released as open source.

---


### 232. [BiVerify: Closing the Loop Between Backward and Forward Verification for Mathematical Self-Correction](https://arxiv.org/abs/2611.11368)

**<font color=#1a73e8>作者：</font>** Rui Zou, Xin Zhao, Mengqi Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have made substantial progress in mathematical reasoning but still produce incorrect solutions to complex problems, indicating the need for more reliable self-correction mechanisms. Mathematical self-correction typically identifies errors through verification, which can proceed backward or forward. The two directions provide complementary verification capabilities. Backward verification checks a candidate answer against the original constraints, bypassing complex intermediate reasoning, but cannot ensure correct reasoning or objective completeness. Forward verification follows the problem conditions and current solution, enabling it to locate reasoning errors and assess objective completeness, but may overlook key constraints in complex solution chains. We propose BiVerify, a dynamically scheduled framework for bidirectional mathematical verification. BiVerify begins with backward verification to screen the answer against the original constraints, followed by forward verification of the reasoning process; subsequent direction switching, state resetting, and re-verification are governed by verification outcomes. Upon failure, the system revises the candidate or verification flow until the same candidate passes both directions. We also introduce shared mathematical tools that separate logical reasoning from precise computation. We systematically evaluate BiVerify on five challenging mathematical reasoning benchmarks using multiple mainstream DeepSeek, GPT, and Gemini models. BiVerify exceeds the strongest representative public baseline evaluated in this work by 13.5 percentage points in average accuracy, with the margin reaching 31.2 percentage points on GPT. Further analysis shows that BiVerify's overall performance exceeds that of either verification direction alone.

---


### 233. [LLM-based Multi-Criteria Deep Reinforcement Learning for Dynamic Efficient 5G UPF Selection](https://arxiv.org/abs/2611.11372)

**<font color=#1a73e8>作者：</font>** Abdelrahman Soliman, Ahmed Refaey Hussein, Lei Lei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> User plane function (UPF) selection in 5G networks is an active area of research, with various limited approaches proposed to enhance network efficiency and manage resources effectively. In this paper, we address this gap in the related literature by proposing a Deep Reinforcement Learning (DRL) UPF selection method that utilizes a dynamic, multi-objective reward function and validating it on a real-world 5G emulation platform. The proposed method is based on the large language models' (LLMs) translation of network operator intents and the network data analytics function (NWDAF) abnormality alerts. The experimental results validated in the real-world experimental setup demonstrate that our dynamic DRL solution achieves an effective balance between latency, power consumption, and traffic distribution, outperforming the heuristic baselines and fixed DRL by 16.89%. These findings highlight the real-world applicability of our approach for dynamic, intent-driven UPF selection.

---


### 234. [Search-by-Answer Bias in Retrieval Models](https://arxiv.org/abs/2611.11396)

**<font color=#1a73e8>作者：</font>** Adiel Avigad, Shauli Ravfogel, Yoav Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dense retrievers are meant to select passages that match a query's semantic specification. We show they suffer from search-by-answer bias: they favor passages that mention answer objects the model knows (scores as likely), over passages that support valid alternative answers. We test this with controlled factual contrasts from LAMA/TREx. For each retriever, we measure how strongly the model scores the canonical object over an alternative object using a token-prediction head, and ask whether this score predicts passage rankings. Across eight retrievers, including DPR, Spider variants, Contriever, E5, and Qwen3-Embedding, larger token-prediction scores consistently predict higher retrieval scores for passages containing the corresponding object. This holds when passages differ only in the answer object, and even when the passage that mentions the high-scoring object expresses a wrong relation. Dense retrieval thus exhibits search-by-answer bias during passage selection, shaping which evidence is retrieved.

---


### 235. [Decomposing Earth Embeddings with Sparse Autoencoders](https://arxiv.org/abs/2611.11398)

**<font color=#1a73e8>作者：</font>** Vitus Benson, Fanny Yang, Markus Reichstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earth observation foundation models produce global metre-resolution embeddings that underpin work across agriculture, ecology, hydrology, and beyond. Yet these embeddings are opaque: each dimension entangles unrelated physical concepts, which makes them difficult to interpret and their robustness hard to assess. Here, we propose sparse autoencoders (SAEs) as a principled way to decompose Earth embeddings into sparse, approximately monosemantic features over an overcomplete dictionary. Because LLM judges of interpretations do not transfer to satellite pixels, and spatial autocorrelation matters, we introduce a tailored evaluation protocol. It scores any SAE on reconstruction at matched sparsity, alignment with reference concepts, and spatial scale, each against baselines that include an SAE whose decoder is a frozen random dictionary. On this protocol, SAEs reconstruct AlphaEarth and Tessera embeddings better than every baseline at matched sparsity. Their features align with far fewer reference concepts than raw embedding dimensions (on AlphaEarth, 88% align with at most one of 20 concept groups, most with none, against a median of 12 per raw dimension). They also carry more of their variance at fine spatial scales (23 to 32% within a 640 m patch for BatchTopK and Matryoshka, against 9%). An SAE with a frozen random decoder shares both properties, which therefore follow from sparsity, whereas only a learned dictionary reconstructs the embedding accurately: on AlphaEarth, trained SAEs leave eight times less variance unexplained. We test the sparse code on two applications, discovering land-cover sub-concepts and detecting out-of-distribution pixels by area-of-applicability estimation. Both indicate how sparse features could be used, but neither is yet reliable enough for practical use. Together, these results are a step toward Earth observation models whose features can be inspected.

---


### 236. [RoCoMark: Robust Code Watermarking Against LLM-Based Functionality-Preserving Rewriting Attacks](https://arxiv.org/abs/2611.11399)

**<font color=#1a73e8>作者：</font>** Hongjie Zhang, Xingcheng Li, Hanzhou Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) present significant challenges to source tracing of generated code, as LLM rewriting can substantially alter the syntactic and structural characteristics of watermarked code. However, existing watermarking methods often suffer severe performance degradation under LLM-based functionality-preserving rewriting attacks. We attribute this vulnerability not merely to the intensity of rewriting, but to a fundamental distribution mismatch between the perturbations encountered during watermark training and the global, non-deterministic rewriting behaviors induced by LLMs. In order to deal with this challenge, we propose RoCoMark, a Robust Code waterMarking framework that explicitly learns and adapts to LLM rewriting behaviors. RoCoMark is a multi-round minimax game between the watermark embedder and LLM rewriter. In each round, the embedder first learns threat profiling from LLM-rewritten code by optimizing the watermark encoder through contrastive learning and knowledge distillation while mitigating catastrophic representation drift. Then the embedder improves strategies by optimizing the watermark encoder and extractor simultaneously. Finally, an adaptive attack-evolution mechanism based on Reflexion and short- and long-term memory pools is applied, enabling continuous interaction between the watermark embedder and evolving rewriting strategies. This iterative attacker-defender process progressively improves the robustness of the watermark against diverse and previously unseen LLM rewriting behaviors. Extensive experiments on four typical benchmarks, under attacks generated by five LLMs, show the effectiveness of RoCoMark. RoCoMark achieves an average detection AUROC of 74.2% and a Rewrite BitACC of 75.3%, while maintaining a code functionality pass rate above 99.7%.

---


### 237. [Modeling individual and item differences in atypicality inferences with ACT-R](https://arxiv.org/abs/2611.11416)

**<font color=#1a73e8>作者：</font>** Guifu Liu, Vera Demberg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans engage in pragmatic reasoning when encountering mentions of highly predictable events. Such mentions may appear redundant, leading comprehenders to infer that the event is atypical, and accommodate this inference with an explanation for why it is atypical. However, these inferences are not drawn uniformly across individuals, and experimental items vary in inference rates due to differences in event typicality. We show that these patterns can be predicted with a resource-rational cognitive model in which comprehenders select interpretation strategies based on individual exploration tendencies and item-level predispositions. These parameters are estimated independently from participants' Raven's Matrices score, event typicality rating and language model based accommodation likelihood. Taken together with recent findings from reference games, our results motivate a new perspective on the mechanisms that support pragmatic inferences.

---


### 238. [GenRM-Flow: Generators are Process-aware Reward Models in Flow Matching](https://arxiv.org/abs/2611.11421)

**<font color=#1a73e8>作者：</font>** Siming Fu, Ruizhe He, Zheming Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning video generation models with human preference depends critically on the quality of the reward model that scores generated videos. Current video reward models, however, source their reward signal from a model's representational rather than generative capacity: they either repurpose vision-language models as pixel-space scorers, or train auxiliary scoring heads on top of frozen generator features. The generator's actual ability to predict velocities, denoise latents, and produce videos plays no role in scoring its own generations. We argue that this overlooks a structural property of offline preference learning. Any preference optimization objective that approximates an offline preference dataset mathematically targets a strictly defined KL-constrained optimal policy. By isolating the reward term from this analytical solution and mapping the exact generation log-likelihood to its flow-matching surrogate, the empirical reward emerges deterministically as the relative difference in continuous-time velocity-prediction errors. We formalize this equivalence into GenRM-Flow, a framework where a preference-tuned video generator inherently operates as a process-aware reward model directly in the noisy latent space. We further show theoretically that distinct fine-tuning objectives, whether contrastive like DPO and IPO or non-contrastive like RWR, are alternative optimization pathways toward the same optimal policy, each inducing a reward readout from the generator's velocity-prediction errors. Furthermore, the extracted process reward seamlessly substitutes external VLM scorers in FlowAWR. Operating purely on native latent outputs without auxiliary reward networks, this generative reward drives measurable improvements in downstream video generation.

---


### 239. [How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding](https://arxiv.org/abs/2611.11437)

**<font color=#1a73e8>作者：</font>** Gengyuan Zhang, Xiao Han, Shijie Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating general-purpose multimodal large language models (MLLMs) for surgical scene understanding remains limited due to scarce surgical data and fragmented evaluation protocols. We address these challenges through a two-stage evaluation framework for surgical scene understanding. In Stage I, we introduce SurgKnowBench, a diagnostic benchmark that harmonizes public surgical datasets across procedures and tasks and evaluates proprietary and open-source MLLMs to map the boundary of pretrained surgical competence. SurgKnowBench reveals that current models retain partial visual priors but remain weak on relational and procedural understanding and workflow assessment. Building on this failure frontier and motivated by the scaffolded nature of surgical training, we introduce SurgAgentGym, an agentic environment where general-purpose MLLM agents can use bounded knowledge search over SurgWiki and general-purpose visual grounding for surgical tasks. SurgAgentGym evaluates whether generalist agents can improve surgical understanding at inference time through tool-mediated evidence use, without additional surgical training. Our results show that agentic inference narrows the gap mainly for perception-heavy tasks, while fine-grained localization and expert-style assessment remain persistent bottlenecks. This opens a path toward future studies of agentic surgical understanding.

---


### 240. [How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?](https://arxiv.org/abs/2611.11450)

**<font color=#1a73e8>作者：</font>** Cong Yu, Ziting Wang, Songlin Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student language model on its own responses, guided by a fixed teacher. Generating these responses is expensive, so systems use quantized inference and asynchronous rollouts to reduce the cost. Both, however, introduce training-inference mismatch between the rollout engine and the model being trained. Such mismatch can destabilize reinforcement learning (RL), but its effects on OPD remain unclear. This paper investigates how much mismatch OPD tolerates, where its effects arise, and how training systems can use this tolerance. Measuring all mismatch sources on one scale, we examine quantization across three student-teacher pairs, with additional tests of weight staleness and injected noise on one pair. OPD tolerates substantial mismatch without meaningful loss of training quality but degrades at higher levels, revealing an empirical mismatch budget. Both the quality cost of mismatch and the mismatch introduced by quantization depend on the model, with some layers particularly sensitive to reduced precision. In controlled comparisons, OPD remains stable under rollout configurations that destabilize RL methods. Under weight noise, mismatch also shifts the prefixes reached during generation, introducing errors that per-token corrections cannot address. To put these findings into practice, we introduce a lightweight admission check that screens rollout configurations against a calibrated budget without requiring a full training run for each candidate. Model-specific FP8 recipes preserve training quality while providing capacity for at least $1.93\times$ as many KV-cache tokens as BF16. Combining FP8 with asynchronous rollouts reaches the same training quality $1.62\times$ sooner than synchronous BF16 training. Code is available at this https URL

---


### 241. [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](https://arxiv.org/abs/2611.11452)

**<font color=#1a73e8>作者：</font>** Weizhong Huang, Huaijia Kou, Tianyu Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis. Growing visual histories enlarge the key-value (KV) cache, increasing memory use and attention costs across candidate rollouts. Existing compression methods primarily optimize individual generators without the planner's semantic constraints, risking low priority for states supporting requested attributes or actions. We introduce SemanticKV, a training-free method for semantically aligned KV cache compression. To our knowledge, SemanticKV is the first KV cache compression method for agentic autoregressive video generation that explicitly uses planner-extracted semantic constraints to guide retention. Text cross-attention identifies constraint-related video positions, whose self-attention queries are collected into separate groups. Attention weights are averaged within each group and maximized across groups, giving each cached entry a high score when strongly used by any represented constraint. A single top-k selection retains high-scoring entries under the memory budget, leaving their keys, values, and positions unchanged. For fixed query groups and equal entry costs, this selection minimizes an additive upper bound on worst-group discarded attention. The method operates independently within each candidate without retraining or additional video generations. We evaluate four AR video backbones on three benchmarks for 5-, 30-, and 60-second generation. On Causal Forcing at a compression ratio of 0.7, SemanticKV obtains a VBench Total Score of 84.10, compared with 84.05 for the strongest compressed baseline and 83.99 for Full KV. It achieves a 1.22x speedup over Full KV and reduces KV-cache memory from 6.04 GB to 1.81 GB, a 3.35x reduction.

---


### 242. [Coding Agents Propagate Vulnerabilities in Code Bases](https://arxiv.org/abs/2611.11455)

**<font color=#1a73e8>作者：</font>** Chenhao Sun, Niels Mündler-Sasahara, Mark Vero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based coding agents are widely used to develop critical production software. Even though coding agents are known to occasionally write vulnerable code, there has not been any investigation into how code base vulnerabilities evolve over time under coding agent contributions. In this work, we close this gap by investigating whether and how vulnerabilities in existing code lead coding agents to introduce similar vulnerabilities in the code they write. We first evaluate coding agents on 96 tasks that require implementing a new backend application in a repository where other applications already exist. Second, we investigate repository-level code generation on 20 pairs of tasks in real C/C++ projects. In each task, the agent is asked to complete code critical to memory safety. We find that in both settings, insecure existing code leads to agents writing vulnerable code more often. In backend generation, insecure neighbors reduce the share of correct and secure implementations by 3.4% on average, and in C/C++ repository-level coding, the average gap between secure and insecure contexts reaches 35.4%. Prompting to follow existing code-style or to be careful about security increases, respectively decreases, how strongly agents propagate vulnerabilities, but neither stops them. When asked to explain their implementation choices, coding agents attribute them to following another code site in 76.5% of cases, even though they recognize the introduced vulnerability in 69.9% of cases. These findings show that agents use existing vulnerabilities as templates for new ones indiscriminatorily, turning each contribution into an opportunity to introduce more vulnerabilities. As such, as agents write a growing share of production code under decreasing human review, code bases can increasingly degrade in security if security vulnerabilities are not thoroughly fixed continuously.

---


### 243. [RealEmbedBench: Benchmarking LLMs on Real-World Application-Layer Embedded Software Tasks](https://arxiv.org/abs/2611.11469)

**<font color=#1a73e8>作者：</font>** Yujun Huang, Yuwei Zhang, Yi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform well on general coding tasks, but their capabilities in application-layer embedded software development remain underexplored. Existing embedded benchmarks primarily focus on hardware-in-the-loop validation in simulated environments. We introduce RealEmbedBench, a benchmark of 5,142 samples covering three application-layer tasks: code generation and completion, state machine modeling and implementation, and cross-OS code translation. We evaluate six representative LLMs and find substantial performance differences across tasks and models. Project context, especially the local code window, significantly affects code generation and completion. Models perform reasonably well at state machine modeling but struggle to translate these models into executable code. Cross-OS translation performance varies substantially by direction. Translation from Harmony to RT-Thread is particularly challenging, with an average pass rate of 0.1667. These findings suggest that developers should consider local code context when using LLMs for code generation and completion and select models according to the translation direction. They also motivate the use of more real-world state machine implementation data in LLM training to narrow the gap between modeling and executable code.

---


### 244. [GOPR-CAD: Graph-of-Operations Progressive Reasoning for CAD Generation](https://arxiv.org/abs/2611.11470)

**<font color=#1a73e8>作者：</font>** Yitian Pang, Yifan Li, Xiaowei Yue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating accurate CAD models requires substantial engineering expertise and careful control of geometry, topology, and mechanical constraints. Text-to-CAD aims to simplify this process, but current LLM-based methods often generate CAD programs directly. Language models remain unreliable when producing long code while coordinating coupled geometric, topological, and dimensional constraints. Consequently, executable programs may still produce structurally incorrect models, which execution rate and rendered appearance may fail to reveal. To address these limitations, we propose GOPR-CAD, an agentic Text-to-CAD pipeline based on Graph-of-Operations Progressive Reasoning. A language model acts as a decision agent over encapsulated CAD operations and progressively constructs an executable operation graph, which a deterministic compiler converts into the final CAD model. This separation requires no additional training and supports different language models. To evaluate structural fidelity, we construct MHCAD, a benchmark of 300 standard mechanical part requirements derived from Machinery's Handbook. Their explicit structures enable reference-free STEP/B-rep evaluation. GOPR-CAD achieves 82.7% Structural Yield on MHCAD, and 87.2% Structural Yield on an external CADPrompt subset.

---


### 245. [Saidzoda-CA-EmbeddingGemma-300M: One Small Embedder for Tajik, Kazakh, Uzbek and Kyrgyz](https://arxiv.org/abs/2611.11471)

**<font color=#1a73e8>作者：</font>** Tohir Saidzoda, Nekruz Maxudov, Bedil Karimov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The small open embedder EmbeddingGemma-300M, used as released, finds the right passage first for only 51.7% to 60.8% of Belebele questions in Tajik, Kazakh, Uzbek and Kyrgyz. We present Saidzoda-CA-EmbeddingGemma-300M, one model for all four languages. It is our Tajik fine-tune of EmbeddingGemma-300M, trained for one more epoch on 279,904 pairs: questions in Kazakh, Uzbek and Kyrgyz that our own language model wrote about source passages, a Tajik refresher, and English and Russian replay. On Belebele, recall@1 rises by 14.4 to 26.0 points in each language, to between 75.2% and 77.7%. Against single-language models trained with the same settings, the one model stays within 2.8 points at recall@1 in Kazakh, Uzbek and Tajik, with overlapping recall@10 intervals, though it also had more training. It keeps the Tajik law recall@10 of its starting point (92.2 against 92.4) but loses 4.4 points of law recall@1. A model trained on one of these languages also improves the others on Belebele, but less than training on them. The model still trails the 560M XLM-RoBERTa embedders on Kazakh, Uzbek and Kyrgyz Belebele: the better of multilingual-e5-large-instruct and BGE-M3, used as released, is 9.4 to 10.2 points ahead at recall@1. Our scores of those released models agree with the published MTEB results within 2.4 points. Russian and English recall@1 fall by 3.0 and 4.2 points.

---


### 246. [THEATRON: A Benchmark for Evaluating Persona Persistence in Long-Horizon LLM Decision-Making](https://arxiv.org/abs/2611.11487)

**<font color=#1a73e8>作者：</font>** Yuyan Wang, Yuechen Jiang, Zhiwei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing evaluations often test persona expression rather than whether persona information persists in extended decision-making. We introduce THEATRON, a controlled benchmark that uses financial replay to evaluate persona persistence in long-horizon sequential decision-making. In these environments, models conditioned on fixed behavioral-finance personas observe shared daily market evidence and trajectory-specific account-state feedback and make sequential decisions over multi-month trajectories. We evaluate Zero-Shot, One-Shot, and Chain-of-Thought persona injection across four LLMs, using cumulative-return and action trajectories to diagnose within-persona stability, cross-persona separability, and action collapse. Persona conditioning produces systematic behavioral shifts beyond a no-persona baseline, and persona-level separation generally exceeds the variation induced by semantically equivalent descriptions. Nevertheless, these shifts do not reliably form coherent persona-specific policies: apparently stable separation can arise from stereotyped action collapse, while diverse policies can exhibit noisy trajectory switching. These findings expose a gap between observable persona-induced behavior and persistent, context-sensitive persona-conditioned decision policies. Code and benchmark data are publicly available at: this https URL

---


### 247. [JoMoHa: Joint Model--Harness Optimization with Reinforcement Learning](https://arxiv.org/abs/2611.11499)

**<font color=#1a73e8>作者：</font>** Xudong Wu, Guangchen Lan, Mingqi Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of language agents depends jointly on model weights and the harness. Optimizing either alone can be constrained by the other component, limiting overall performance gains. Our analysis of naive alternating training reveals progressive incompatibility between the model and harness, which increasingly interferes with task execution and may also undermine model training, leading to performance degradation. To coordinate the evolution of models and harnesses, we introduce JoMoHa, to our knowledge the first framework to jointly train an executable harness generation policy and a task execution policy through reinforcement learning. JoMoHa outperforms the evaluated weight-only and harness-only baselines and achieves the highest success rates among the evaluated methods on ALFWorld, WebShop, and DBBench, averaging 70.3% and reaching 97.0% on ALFWorld. By learning both task execution and runtime improvement from its own generated trajectories, JoMoHa performs recursive self-improvement (RSI).

---


### 248. [AgentCT: A Vision-Language Agent for Universal CT Imaging](https://arxiv.org/abs/2611.11503)

**<font color=#1a73e8>作者：</font>** Zhihao Chen, Qi Gao, Chuang Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) restoration methods often use a single network for low-dose CT (LDCT), sparse-view CT (SVCT), and metal artifact reduction (MAR), despite the distinct physics of these degradations. We propose AgentCT, a vision-language agent that identifies the degradation and routes images to task-specific restoration models. A LoRA-adapted Qwen3-VL-4B controller predicts degradation type and severity, selects a specialist, and reassesses the restored image. The LDCT specialist uses an image-domain diffusion model, whereas the SVCT and MAR specialists combine projection-domain correction, data consistency, differentiable filtered back-projection, and image refinement. We evaluated the controller and specialists separately on patient-disjoint Mayo 2020 abdominal CT data across three severity levels for each degradation. The controller achieved 95.7% accuracy for degradation type and 93.9% for severity, with a 100% JSON parse rate. Using ground-truth degradation labels for routing, AgentCT achieved an overall PSNR/SSIM of 46.18 dB/0.984, compared with 44.93 dB/0.976 for AMIR and 44.29 dB/0.979 for TAMP, and attained the highest PSNR in all nine settings. For SVCT, its dual-domain specialist achieved 46.04 dB with 4.2 million parameters, compared with 44.43 dB for single-task AMIR and 43.57 dB for all-in-one AMIR with 23.5 million parameters. These results support degradation-specific CT restoration with controller-based model selection; evaluation under automatic routing and on independent clinical data remains necessary. Code is available at this https URL.

---


### 249. [Reaching Is Not Finding: Map-Anchored Visual Prompting for the Last Mile of Aerial Vision-Language Navigation](https://arxiv.org/abs/2611.11510)

**<font color=#1a73e8>作者：</font>** Ningbo Li, Kebin Liu, Jingcan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial vision-language navigation (VLN) asks a drone to find an object described in natural language. The description usually locates the object relative to named landmarks, such as streets and buildings. We observe that current navigators often bring the drone close to the target and then stop at the wrong place: they reach the target without finding it. This gap is shared by navigators of very different designs, from imitation learners to a fine-tuned 7B vision-language model. A simple test reveals the cause. When we replace the target object in the instruction with another one next to the same landmarks, no navigator goes to it, and most stop where they did before. Navigators learn to reach the landmarks, not to identify the described object. We therefore propose MAP-VP, a plug-and-play module for the last step. After any navigator stops, MAP-VP draws the landmarks named in the instruction onto the drone's current view, using the landmark outlines that the benchmark provides on a map. A fine-tuned 4B vision-language model then locates the target relative to these landmarks. The training data are generated automatically from the benchmark annotations. Neither drawing the landmarks nor fine-tuning helps much alone, but together they are highly effective. Without retraining any navigator, MAP-VP significantly improves all six navigators we test on CityNav. It roughly doubles the success rate of the two strongest trained navigators, raising HETT from 25.9% to 54.6% and FlightGPT from 24.2% to 48.9%, whereas CityNav's official detector-based last step adds less than two points to HETT.

---


### 250. [Probing Transformer Representations Layer by Layer, Module by Module](https://arxiv.org/abs/2611.11531)

**<font color=#1a73e8>作者：</font>** Ambroise Odonnat, Theo Gnassounou, Laetitia Chapel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Which representation should be probed in a transformer-based foundation model? Recent work shows that the standard practice of probing the final layer is often suboptimal, as intermediate layers can provide better features. Yet, representations are still largely studied along depth alone, treating each transformer block as an atomic unit. In this work, we analyze transformer representations layer by layer, module by module. Through more than 144,000 linear probing evaluations of vision foundation models (VFMs) and large language models (LLMs), we show that layer and module choices should be considered jointly: the best layer-module pair yields substantially larger gains over the final-layer residual stream than the best layer with the residual stream fixed. Moreover, module performance can vary substantially across layers, showing that useful representations cannot be characterized by depth alone. Building on these findings, we evaluate simple fixed probing strategies: the final-layer feedforward activation (Act@100) for vision and the second normalization layer at 60% depth (LN2@60) for language. These strategies improve over the probing baseline in a majority of evaluations and recover, on average, 42% and 86% of the gains from probing the best layer-module pair for vision and language, respectively. For VFMs, these gains increase with the transfer difficulty between pretraining and downstream data.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
