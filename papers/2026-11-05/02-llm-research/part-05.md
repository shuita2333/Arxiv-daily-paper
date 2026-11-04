# 🧠 大模型相关研究 | 2026年11月05日

> 本类共 **220** 篇论文：已确认 **208** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-220**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-220**

---

### 201. [Personas Are Not People: Identity as State, Not Attribute](https://arxiv.org/abs/2611.05292)

**<font color=#1a73e8>作者：</font>** Tamunotonye Harry, Yuanyuan Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person is defined by a persona, a written profile of fixed traits, demographics, and attitudes that a language model is instructed to act out. Every such system assumes that a person's identity is a stable attribute that behaves the same way in every situation the simulation presents. We show that this assumption is not a harmless simplification. Three decades of personality research find the opposite. How a given person behaves varies more across contexts than people vary from one another. Drawing on identity economics, which describes how different situations activate different identities and norms within the same person, we separate behavior into three parts, which are stable traits, the identity a context calls up, and the situation itself. We then prove, under two stated assumptions, that any simulation built on fixed personas, no matter how detailed the personas or how large the underlying model, cannot reproduce the part of a population's behavior that is specific to it and its circumstances. We propose a new evaluation criterion based on this result and a person-in-context design that can meet it in principle. We test one version on a naturalistic Reddit personality corpus and on a published clinical-trial recruitment survey of a community with documented distrust of medical institutions. The design does produce context-dependent behavior when tested directly, but in neither setting does it fully match the real population, and we show where it falls short. The consequence for practice is a risk that synthetic-population evaluations misrepresent the groups whose behavior is most shaped by context, a distortion that richer personas cannot correct.

---


### 202. [Wonder 4: A Mixture-of-Experts Recipe for Image Quality Enhancement](https://arxiv.org/abs/2611.05294)

**<font color=#1a73e8>作者：</font>** Yunan Wu, Bin Sun, Partha Acharjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A real photograph is often blurry, grainy, compressed, scratched, and low-resolution at the same time. Each defect has its own severity and its own place in the image. The corrections for these defects conflict with each other. Exist- ing models describe the whole image with one description, so they cannot say where each correction belongs. To solve this problem, we present Wonder 4, a mixture-of-experts (MoE) model for image quality enhancement. It corrects several defects of a real photograph at the same time, each in the region where it occurs. Every block of the model holds a mixture of N = 13 experts. A router, trained with the model, sends every image patch to k = 5 of them. No degradation classifier, mask, prompt, detector, or task label is used. Another issue is that standard MoE training, taken from language models, pushes every expert toward equal use. Equal use applies every correction everywhere, even where it is not needed. We replace this rule with a bias that only sets a minimum share of use. Across all patches, an expert used less than this minimum gets higher router scores until it is selected again. An expert above the minimum is not changed, so no expert is forced to be used as often as the others. The bias needs no extra loss. The method adds no extra module and no extra processing step. We evaluate Wonder 4 on DIV2K and Flickr2K, against five published methods and three open-weight pipelines. It reaches the best LPIPS, DISTS, and NIQE on all three test settings (DIV2K x4, DIV2K x8, and Flickr2K x4).

---


### 203. [LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers](https://arxiv.org/abs/2611.05304)

**<font color=#1a73e8>作者：</font>** Minsoo Cheong, Sungjoo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively reduces parameter memory, each loop step still stores its own keys and values, so the key-value (KV) cache grows linearly with the number of loop steps and becomes the main memory bottleneck. We observe that the KV cache of looped models is highly redundant along the loop axis and that the loop steps differ substantially in their sensitivity to quantization. Based on these observations, we propose $\textbf{LoopVQ}$, a KV cache vector quantization method for looped transformers that codes channels of multiple loop steps jointly, and fine-tunes the codebooks to match the output of the full-precision model. At 0.5 bits per element, LoopVQ outperforms existing KV cache vector quantization methods for standard LLMs on general, long chain-of-thought reasoning, and long-context retrieval tasks with Ouro and Huginn models. Its design is orthogonal to these methods, and combined with TaSQ, it retains much of the BF16 accuracy even at 0.25 bits per element. We also implement LoopVQ in SGLang, where it nearly halves the decode latency at a 32K-token context and raises the peak serving throughput by up to $4.3\times$ and $6.1\times$ on the 1.4B and 2.6B Ouro models compared to the BF16 baseline.

---


### 204. [You don't need long context](https://arxiv.org/abs/2611.05306)

**<font color=#1a73e8>作者：</font>** Peter Belcak, Saurav Muralidharan, Jindong Jiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Later tokens are costlier to generate than earlier tokens. On frontier open weight models, the disparity in cost may rise to as much as 7x. Through frequent compaction, we show across a broad range of long-horizon and long-input tasks that frontier language models sacrifice little to no task accuracy when maintaining short contexts. We further demonstrate that LLM performance does not collapse on long-horizon software engineering tasks even when taking at most one action per context, and based on that we outline the concept of semantic state space models (SSSMs). Our findings question the need for long-context language models.

---


### 205. [A Circuit for In-Context Learning](https://arxiv.org/abs/2611.05344)

**<font color=#1a73e8>作者：</font>** Andrew Gao, William Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) lets a pretrained language model perform a task specified by demonstrations in its prompt, with no parameter updates. With arbitrary labels the model must acquire a mapping it cannot have memorized, so the learning happens within a single forward pass. Prior work found candidate parts but not how they compose. We give the composition for few-shot sentence classification with arbitrary labels in three 3-4B-parameter transformers. The model implements a key-value memory over label-token positions: each label token's residual stream encodes the label's identity, and middle-layer attention heads write into it the class of the preceding demonstration as its key. At the query, upper-layer heads match the query's class against the stored keys and copy out the matching labels. An early-layer signal encoding whether any label has repeated gates this readout; in its absence the readers attend to the start of the prompt and no label is favored. A separate set of heads suppresses the most recently seen label. Each step is established causally by activation patching, head ablations against random-head baselines, and steering with the model's own signals. A softmax model of the readout with two constants per head, fit on one prompt distribution, predicts another. The computation is conserved across the three models, the named heads alone reproduce the behaviour, and a transformer trained from scratch grows the same parts. The circuit transfers to semantic concepts and to labels with meaning, and the same parts, with a causal gate, appear from 0.6B to 8B in one family and survive instruction tuning. ICL in this setting is a gated associative lookup built from a few identifiable component types, traced causally from demonstrations to prediction.

---


### 206. [Adversarial Speculative Reasoning Improves Long Horizon Agents](https://arxiv.org/abs/2611.05345)

**<font color=#1a73e8>作者：</font>** Hongyin Luo, Wei Fang, Lijie Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this view does not hold true for long-horizon agent reasoning. Measuring frontier open-weight models on complex agentic tasks with different speculative decoding approaches, we found that numerical noise grows within verification windows, and the draft acceptance results of the thinking process can change the output distribution of the model after 30 steps, thus noticeably influencing the reasoning accuracy of long-horizon agents in random directions. In this work, we improve the reasoning capability of target models by controlling such noise. While we cannot change the overall token distribution verified by the target model, we can encode critical reasoning with highest precision by training the draft model to be rejected. We identify these points in agent traces and train the draft model to favor adversarial preference. At inference the trained draft and the target part ways precisely at these decision points, verification restarts, so that critical thinking tokens are sampled from the target model and encoded under its least noisy conditions. This approach makes critical reasoning better indexed and more durable over a long horizon. On complex agentic coding benchmarks, our approach raises end-to-end success rate with no change to the target model or its output distribution. Our results recast the speculative decoding mechanism from a pure accelerator into an active allocator for context precision that improves the accuracy of long-horizon agents by training 0.06% to 0.28% of hosted parameters.

---


### 207. [Suppressing Misaligned Behaviors in Language Models, Durably](https://arxiv.org/abs/2611.05358)

**<font color=#1a73e8>作者：</font>** Luxi He, Pengcheng Jiang, Jifan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and behaves normally otherwise. The broad-trigger organism has no such cue: after fine-tuning on insecure code, it gives harmful responses across a wide range of open-ended prompts. We then formalize post-hoc behavioral suppression and evaluate methods along three criteria: immediate suppression of the target behavior, durability under further training, and preservation of general capability. We compare standard methods--SFT, GRPO, and gradient-ascent unlearning--along these dimensions. Building on prior work on alignment shallowness, we hypothesize that more durable suppression requires the ability to recover from a wider range of misalignment states. We introduce Prefix-Expanded Adversarial Reinforcement Learning (PEARL), a GRPO variant that augments rollouts with continuations from intermediate states sampled along cached organism trajectories. Across both organism settings and two model families (Qwen3-4B, GPT-OSS-20B), PEARL achieves strong immediate suppression while preserving task accuracy, and remains durable under further fine-tuning on either the organism's data or unrelated data. It obtains the greatest benefit when the undesirable behavior is broad and cannot be addressed through targeted SFT. Together, our framework and method offer a step toward more durable post-hoc removal of undesired behaviors.

---


### 208. [Aligning Language Models with General Preferences: An Empirical Study of Direct Nash Optimization](https://arxiv.org/abs/2611.05373)

**<font color=#1a73e8>作者：</font>** Austin Tsai, Saurav Nanda, Ganapathy Parthasarathy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Nash Optimization (DNO) aligns a language model to a general preference function by approximating the Nash equilibrium of a two-player preference game. Its practical variant, DNO-Prct, iterates on-policy sampling, LLM-based rating of the samples together with a teacher's gold response, large-margin preference-pair selection and a DPO-style contrastive update. We re-implement DNO-Prct independently and study it on two open-weight instruct models, Llama 3.1 8B Instruct and Mistral 7B Instruct v0.1, with GPT-4o or a larger open-weight model of the same family as the annotator. On AlpacaEval 2.0 with GPT-4o as judge, three iterations raise the length-controlled (LC) win rate against GPT-4o from 31.7% to 45.3% for Llama and from 6.8% to 18.4% for Mistral, and the tuned 8B model scores above Llama 3.1 70B Instruct on every reported win rate. With same-family open-weight annotators, the runs retain 62% (Llama) and 82% (Mistral) of the LC gain achieved with GPT-4o as annotator, so the rating step does not require a proprietary model. In a separate ablation configuration, variants that remove the gold responses, remove the data look-back, or accept only teacher-preferred pairs score 6 to 10 LC points below the full procedure, whereas varying the number of on-policy samples per prompt (1 to 7) moves the LC win rate by at most 2.1 points, and a margin sweep (1 to 5) run in its own pipeline by at most 2.4 points. We also report the cost of the pipeline and where the practical algorithm departs from the theory it approximates. All results are single runs, and GPT-4o is both the teacher and the evaluation judge; we discuss what this implies for the reported gains.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 209. [VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions](https://arxiv.org/abs/2611.03765)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Qu, Qiang Fu, Zonghao Ying 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents are increasingly deployed in open-world environments, yet current robustness evaluations remain biased toward hazardous instructions and jailbreak vulnerabilities. A more fundamental issue is largely overlooked: agents are rarely tested under semantically sufficient but contextually minimal instructions (i.e., common in real-world human communication), where auxiliary contextual cues are absent. For the first, we identify a novel phenomenon termed Ambient Context Illusion, where agents fail to execute tasks correctly when non-essential contextual details are omitted, despite unchanged task semantics. To systematically study this, we establish VagueBench, a benchmark built upon the AI2-THOR interactive simulation environment for the evaluation of context dependency in embodied agents. We systematically consider key semantic components of instructions (entities, procedures, constraints, and prior knowledge) and derive a unified taxonomy with four categories and nine subtypes to reduce auxiliary information. VagueBench contains 1,303 instruction pairs across diverse indoor environments, constructed via a human-agent co-generation framework that integrates semantic redundancy estimation, taxonomy-guided transformation, and rigorous semantic-invariance verification. Through extensive evaluation on 6 state-of-the-art embodied agents, we observe significant degradation on VagueBench in both task performance and executability (relatively -19.65% in task success rate and relatively +54.10% in empty plan rate) revealing a strong reliance on auxiliary linguistic signals rather than core task semantics. Furthermore, we demonstrate that this phenomenon persists in real-world robotic systems, where it can lead to incorrect decisions and potential safety risks.

---


### 210. [Low-Rank Hierarchical Merging for Efficient Long-to-Short Reasoning](https://arxiv.org/abs/2611.03834)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeqiu Yu, Xuesheng Zhang, Wenxiao Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-to-Short (L2S) model merging seeks to combine the strong reasoning capability of long chain-of-thought models with the concise style of base models, but existing methods that rely on linear interpolation and first-order activation statistics fail to capture how the loss landscape responds to parameter displacement, leading to degraded accuracy on hard tasks. We propose Low-Rank Hierarchical Merging (LHM), a training-free framework that replaces heuristic statistics with lightweight second-order curvature information. LHM consists of three components: (1) a low-rank Hessian approximation that efficiently estimates per-layer Hessian traces via Hutchinson's estimator on random inputs, eliminating the need for task-specific data; (2) a Layer Second-Order Sensitivity (LSOS) index that combines Hessian trace with task-vector norm to quantify per-layer fusion difficulty; and (3) a Dual-Constraint Coefficient Mapping (DCCM) that converts LSOS scores into layer-adaptive merge coefficients while jointly satisfying a fusion-error bound and a global length-reduction target. Experiments across six mathematical benchmarks on 1.5B and 7B models show that LHM outperforms state-of-the-art methods such as ACM-TIES and ORCA, achieving over 4\% accuracy gain and up to 93.1\% reduction in output length relative to the long-CoT model.

---


### 211. [Where Do Distilled Students Store Thinking?](https://arxiv.org/abs/2611.04141)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Taeyeong Kim, Jaemin Jung, Ahhyun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small students degrade on large reasoning models' (LRMs') long solutions, so recent work shortens them by interpolating an LRM with a short-answer model at ratio $\lambda$. We ask what student weights retain when this teacher stops thinking, comparing LoRA adapters of three students from three teacher pairs at each $\lambda$. In each pair, the adapters' update subspace shifts most where the teacher stops thinking and solutions shorten most, locating the change without attributing it. We identify a shared adapter subspace tied to thinking-like behavior (reflective markers, monologue format and long solutions). Shared by adapters before that point, it keeps about half (post hoc) while one pair's teacher halves its solutions but keeps its think tag, and largely empties after thinking stops. Removing it largely turns this behavior off for every pair, student and benchmark. Only in that pair and one other student does it leave clearly fewer markers than removing the update's top components; elsewhere, same-energy random directions often nearly match it. Grafted into a short-answer student at twice its weight, it turns early markers (a post hoc count) on, like the whole update, but the student rarely finishes. Our work identifies a weight subspace tied to distilled thinking-like behavior.

---


### 212. [What Remains in Sight? Autoregressive Video Decoding as Representation-Guided Context Rewriting](https://arxiv.org/abs/2611.04164)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lixuan He, Jihyeon Je, Yang You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon video generation is increasingly moving toward autoregressive rollout, where each newly generated segment becomes part of the evidence used for future prediction. Recent causal decoders, long-context training, and KV-cache mechanisms have extended feasible duration, but most inference pipelines still decide the visible past implicitly through recent windows, compressed caches, or external memory. This raises a direct question: \textbf{can the choice of which past frames or segments to show to the decoder be treated as an explicit test-time decision?} We answer this question with \textsc{ReCR}, a training-free method that formulates autoregressive video decoding as representation-guided context rewriting. At each step, \textsc{ReCR} builds a selected visible context from the generated history by using internal decoder representations to favor context units that match the global rollout state, avoid redundancy with the recent continuation, preserve temporal boundary coverage, and widen the range of spatial layouts in view. The selected units are then mapped onto a compact causal axis before decoding the next block. Across long-horizon text-to-video benchmarks, \textsc{ReCR} consistently improves multiple autoregressive backbones under matched visible-token budgets. Empirical analyses such as representation-space diagnostics and transition-count prompt switching further show that improving what remains visible is an effective path toward more stable long-video decoding.

---


### 213. [Formalizing PTX in Lean to Prove GPU Kernel Correctness](https://arxiv.org/abs/2611.04447)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Luk Koska, Tom Koska, Ben Koska  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an approach to mathematically formalizing PTX, an approach that allows modeling and reasoning about patterns common in GPU kernels for Deep Learning, including acquire-release, tensor cores, proxies, async operations, multi-kernel pipelines and data-dependent control flow. We implement it in Lean and use it to prove the correctness of simple implementations of a WGMMA GEMM kernel, FlashAttention, and a 3-kernel MoE pipeline.

---


### 214. [Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling](https://arxiv.org/abs/2611.04792)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ria Shekhawat, Abhijeet Sinha, Yingtao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning objectives that maximize expected return can concentrate probability mass on a small subset of high-reward outcomes, limiting diversity when multiple distinct solutions are desirable. We introduce Density-Aware Reward Scaling (DARS), a simple reward-processing mechanism that promotes reward-proportional sampling in continuous outcome spaces while retaining standard policy-gradient training. DARS estimates the local density of outcomes within each on-policy rollout group and inversely scales rewards by this density. The method requires no learned density model, auxiliary objective, critic, or modification to the underlying policy-gradient objective. In a controlled multimodal navigation task, DARS-GRPO avoids the single-mode collapse exhibited by GRPO and closely recovers the target mode allocation. Applied to text-to-image prompt adaptation, DARS-GRPO consistently improves image and prompt diversity across datasets, Policy LMs, and reward settings while maintaining good semantic alignment. These results show that density-aware reward scaling provides a lightweight way to improve coverage of diverse high-reward outcomes within existing reinforcement-learning pipelines.

---


### 215. [Think Less, Locally: Local Preference Learning for Reasoning Compression](https://arxiv.org/abs/2611.04814)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Muyao Yuan, Liyan Xu, Weizhan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models achieve strong performance on challenging tasks, but their long chain-of-thought often incurs substantial inference costs by continuing to deliberate after sufficient information has been obtained. Existing reasoning compression methods primarily operate on reasoning trajectories, paying less attention to the local decision of whether further reasoning is necessary given the current state. We propose LoCo, a local preference learning method for reasoning compression. LoCo detects candidate overthinking states from the model's own traces, freezes the corresponding reasoning prefixes, regenerates shorter verified continuations from the same states, and trains on the resulting state-conditioned preference pairs with DPO. This formulation teaches the model when to continue reasoning and when to conclude, rather than simply encouraging shorter trajectories overall. We construct training data entirely from self-generated mathematical traces and evaluate LoCo on five mathematical and three code generation benchmarks. LoCo reduces completion length by 41.7\%--45.4\% on mathematics and 23.4\%--36.3\% on code, while maintaining or improving accuracy and achieving the best AUC across all code benchmarks. LoCo consistently improves the accuracy-efficiency trade-off on mathematics and transfers effectively to code generation despite math-only training, demonstrating the cross-domain generality of local preference learning for reasoning compression. The code and model will be publicly released at this https URL.

---


### 216. [The Platonic Brain: Representational Convergence in EEG Foundation Models](https://arxiv.org/abs/2611.05097)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nicolas Waehner, Enzo Tagliazucchi, Jacobo Sitt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis (PRH) predicts that artificial neural networks converge on shared representations as scale and performance increase. We test whether these predictions hold for representations of the human brain with EEG foundation models. Using EEG recordings from six participants watching a television series, together with aligned visual and language content, we tested whether EEG foundation-model representations converge within and across modalities as their embeddings become better at decoding an informative set of EEG markers. We found that EEG models with greater decodability showed stronger cross-family alignment in both local neighbourhood similarity and global structure, not consistently increasing with model parameter count. Cross-modal convergence was modality and metric dependent: greater EEG decodability was associated with stronger global alignment to language, but not consistently to vision models, while local alignment showed no consistent association. This dissociation may reflect local sensitivity to low-level sensory features, whereas global geometry may capture weaker shared semantic structure.

---


### 217. [Beyond Foundation Models: PFN Priors Improve Tabular Hyperparameter Optimization](https://arxiv.org/abs/2611.05141)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Artem Chistyakov, Renat Sergazinov, Artem Babenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic priors have so far served one purpose: pretraining tabular foundation models. We ask whether the same priors can improve conventional tabular models, which are trained from scratch on each dataset. We propose PriorTune, a method that meta-tunes hyperparameter configurations on synthetic tasks alone. Offline, for a given model, we fit a pool of configurations on datasets sampled from a published PFN prior and greedily select the subset with the highest winrate over the random baseline. Online, a new dataset fits only the selected configurations, so the gain comes at no extra cost. Empirically, we observe that scaling both the number of configurations and synthetic datasets has an equal scaling effect on the performance of the final subset of configurations, which we also explain theoretically. On the full BeyondArena benchmark, LightGBM with TabPrep features with our configurations ranks above TabPFN-3 and RealMLP, while being much more efficient at inference. Overall, our results establish existing PFN priors as a scalable source of meta-training data for hyperparameter selection for non-foundational tabular models.

---


### 218. [Provably Learning Mixtures of Linear Experts](https://arxiv.org/abs/2611.05184)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adrian Candocia, Aamod Varma, Mark Davenport  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models are widely deployed in modern machine learning. However, few convergence guarantees exist for gradient-based training of MoEs: the objective is nonconvex, and even simple mixtures trap first-order methods in spurious local optima. We analyze a canonical gated mixture featuring linear experts and a gate induced by Gaussian clusters in the input space, and give, to our knowledge, the first global convergence guarantee for jointly training the gate and the experts of such a model by gradient EM on its likelihood. Given a logarithmic overparameterization relative to the true number of experts $m$, gradient EM converges from randomly initialized gates and least-squares-initialized experts to any prescribed accuracy in polynomially many iterations, under a separation condition on the gate centers. Our analysis establishes a gradient-dominance inequality for the coupled dynamics by decoupling the loss into per-cluster subproblems. Empirical results validate the predicted $m\log m$ phase transition and suggest that the least-squares warm start required by our analysis is not needed in practice: randomly initialized experts perform nearly as well. We also find that leaving the mixing weights unconstrained concentrates routing onto the true number of experts, whereas load-balancing penalties spread it, so that the fitted model can be pruned to a fraction of its width without loss of accuracy.

---


### 219. [JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks](https://arxiv.org/abs/2611.05263)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shanka Subhra Mondal, Jiayun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through intermediate states, track progress over extended interaction histories, and execute visually grounded actions. Although prior work has explored modular multi-agent systems with a separate planner, the planner is typically not updated jointly with the actor. We investigate whether explicitly separating and jointly training planning and execution provides a stronger inductive bias for long-horizon web navigation. We introduce JHiMA-WebRL, a joint hierarchical multi-agent reinforcement learning framework for web agents that couples a task decomposer with an actor. To train the decomposer, we use a strong teacher model to construct structured subtask supervision from multimodal GUI trajectories, and use these annotations to fine-tune both the decomposer and the subtask-conditioned actor. We then extend Group Relative Policy Optimization (GRPO) to jointly optimize the decomposer and actor in the interactive WebArena environment through hierarchical rollout grouping and role-specific advantages. On WebArena-Lite-v2, JHiMA-WebRL-14B, consisting of a 7B actor and a 7B decomposer, achieves an average success rate of 37.2%, compared with 24% for a ScaleCUA-32B agent that we fine-tune with RL on the same training tasks and evaluate under the same protocol. Ablations show that jointly updating the decomposer during RL outperforms updating the actor alone. These results suggest that jointly learned role factorization with smaller models can be a competitive alternative to scaling monolithic agents for long-horizon web tasks.

---


### 220. [CATF: A Manager-Worker Framework for Context-Aware Time-Series Forecasting](https://arxiv.org/abs/2611.05325)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yueqiao Chen, Dongyu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study context-aware time-series forecasting, in which a single target variable is predicted from its own history and a set of contextual variables, such as weather and calendar information. As the context becomes more diverse, a single model struggles to capture all of its regimes, while ensemble learning and Mixture-of-Experts approaches rely on manual data partitioning or soft routing, which increases the inference cost and hinders interpretability. We propose CATF, a Context-Aware Time-Series Forecasting framework built on a Manager-Worker architecture: a Transformer-based Manager routes each input to a single Worker based on the context, using hard routing during both training and inference. The Workers thus specialize without manual data partitioning, and any single-model forecaster can serve as a Worker. On five context-rich datasets, four horizons, and two normalization schemes, CATF improves over its standalone counterpart in 162 of 200 comparisons, the best CATF-enhanced model outperforms the best standalone baseline in 19 of 20 settings, and it outperforms the zero-shot Time-MoE foundation model in 15 of 20 settings. A case study on bike-sharing data shows that the Manager routes inputs by the calendar and that each Worker specializes in a different weekly pattern.

---


> [!TIP]
> 当前位于：**201-220**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-220**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
