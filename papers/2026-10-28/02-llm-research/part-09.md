# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-418**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-418**

---

### 401. [More: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents](https://arxiv.org/abs/2610.33684)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dianxing Shi, Dingjie Fu, Tianyu Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving training improves the performance of agents on difficult tasks through verifiable feedback, but it often applies costly deliberation uniformly across tasks. To address this problem, we propose Mode-Optimized Reasoning with Self-Adaptive Effort (MORE), a self-evolving training framework that adaptively selects both reasoning form and computational effort for each task. Specifically, MORE follows a two-stage training paradigm: (i) \emph{Stage 1} establishes a compact prior over direct answering, short and long chain-of-thought, and code-based reasoning, and (ii) \emph{Stage 2} self-evolves this prior with Mode-Adaptive and Test-time Effort PPO (MATE-PPO) on generated, verifiable task streams without curated data. By learning mode selection and token expenditure jointly, MORE allocates concise reasoning to tasks that permit it while retaining extended deliberation where it is useful. Across coding, mathematics, and general-reasoning benchmarks, MORE achieves consistent performance gains on Base and Coder backbones at model scales from 3B to 14B. During inference, MORE demonstrates higher accuracy and better efficiency, with markedly shorter response lengths and reduced inference time.

---


### 402. [An actively trained neural operator for near-explicit atmospheric chemistry](https://arxiv.org/abs/2610.33771)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhi-Song Liu, Wenqing Peng, Ammar Kheder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth-system models simplify atmospheric chemistry into condensed mechanisms, because near-explicit mechanisms such as the Master Chemical Mechanism (MCM) are too costly to solve in every grid cell. Neural emulators could lift this limit, but most advance the chemistry in small time steps and cover only a few species or a reduced mechanism. Here we introduce FNO-MoE, a Fourier neural operator with a mixture of experts that predicts the full near-explicit chemical state over 30 minutes in a single call. The same network also guides its own training, using the disagreement among its experts to select the most informative box-model simulations. At equal cost, this active sampling yields a more accurate emulator than random or evenly spread sampling. Fine-tuning on longer trajectories keeps it stable over multi-hour runs in which models trained on short simulations diverge. The resulting emulator reproduces the evolution of thousands of species with high fidelity, remains accurate for unseen chemical compositions and runs orders of magnitude faster than the numerical solver. These results open a new direction for emulating complex atmospheric systems: neural operators that predict the full chemical state over long windows and choose their own training data. Training under changing meteorology is the next step towards bringing near-explicit chemistry into Earth-system models.

---


### 403. [Unlocking the Specialization Capability of PPG Foundation Models for Wearable Signals through Structured Pruning and Adaptive Fine-Tuning](https://arxiv.org/abs/2610.33788)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Huaming Du, Zhixian Xie, Gaoyang Zhen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) plays a central role in wearable health monitoring and clinical decision support. However, existing approaches to universal PPG representation learning are predominantly trained on high-quality large-scale datasets obtained from oximeters in hospital settings and often struggle to adapt to sparse and low-quality real-world datasets, thereby limiting their generalization to clinically relevant tasks on prevalent PPG data such as collected from wearable devices. Surprisingly, even after full fine-tuning, PPG foundation models cannot consistently outperform general-purpose time-series models. Therefore, a key question is how to effectively adapt PPG foundation models to target prediction tasks. Through empirical studies on various PPG foundation models, we find that pretrained models often exhibit inherent sparsity and computational redundancy, suggesting that PPG foundation models have learned to activate task-relevant network substructures for different prediction tasks. To preserve this valuable prior knowledge, we propose a structured pruning-and-fine-tuning framework, SPAFT, which regularizes the adaptive fine-tuning process by constraining it to a more relevant and compact parameter space based on parameter importance and structural redundancy. Extensive experiments across four PPG foundation models, five benchmark datasets, and ten downstream tasks demonstrate that SPAFT achieves win rates of 82.8% and 87.5% on regression and classification tasks, respectively. This prune-then-finetune paradigm often enables PPG foundation models to achieve state-of-the-art performance, laying a promising foundation for the real-world clinical deployment of PPG foundation models and the development of personalized PPG foundation models.

---


### 404. [ProMo3D: Probing Motion Cues in Frozen 3D Foundation Models](https://arxiv.org/abs/2610.33802)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaoang Zhang, Mert Kiray, Yordanka Velikova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D foundation models have recently reshaped multi-view reconstruction, yet dynamic 4D understanding still often relies on large-scale motion supervision or hand-crafted, architecture-specific heuristics. We ask whether frozen 3D foundation model tokens already encode motion-relevant information that can be exposed by lightweight readout functions, rather than re-learning motion-specific features with high-capacity decoders. Through probing on three representative backbones, we find that static--dynamic separation is decodable from frozen token representations. Our rank-restricted and spectral analyses on $\pi^3$X reveal that the recovered motion cues are concentrated in a low-dimensional subspace. Building on this, we propose Probing-based Motion Distillation (PMD), which converts pairwise motion-state compatibility scores against a fixed anchor token into dense motion masks. Trained on only 160 YouTube-VOS videos using a single 16 GB GPU, PMD transfers zero-shot to DAVIS, SegTrackv2, and FBMS-59 without target-benchmark fine-tuning. With multi-view pretrained geometric backbones, PMD outperforms training-free heuristics and approaches substantially heavier supervised and self-supervised methods, suggesting that motion decoding from frozen 3D foundation models can be lightweight and data-efficient.

---


### 405. [Learning What to Share: Expert Specialization for Time-Series Forecasting](https://arxiv.org/abs/2610.33822)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bashar Khoury, Shadi Omari, Assaf Schuster  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in multivariate forecasting is deciding what to share across channels and where to specialize. Mixture-of-experts models offer flexible sharing, yet it remains unclear how much of their forecasting gains comes from added capacity or expert allocation. Through controlled comparisons across eleven datasets and three backbones, we show that informative channel assignments improve forecasting beyond matched shared capacity and random allocation. On frozen transformer backbones, persistent channel-specific mixtures outperform input-dependent routing on average. To examine when and how much specialization helps, we introduce GalaxyTS, a controlled synthetic dataset with exact shared and channel-specific forecasting references. It reveals how persistent channel mixtures exploit predictive differences concealed by short input windows and measures gains over matched shared corrections. These insights motivate Persistent Closed-Form Routing (PCR), a plug-and-play method that alternates exact conditional estimation of channel-specific mixture weights with gradient-based training of low-rank residual experts around a frozen pretrained forecaster. Averaged over four forecasting horizons, PCR-K4 achieves dataset-balanced mean squared error reductions of 3.86-14.25% relative to the three frozen backbones. In matched comparisons, PCR outperforms competing specialization methods on average while requiring substantially fewer trainable parameters.

---


### 406. [Intervention-Certified Amplification: A Validity Gate for $σ$-Weighted Post-Training](https://arxiv.org/abs/2610.33882)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Leiyue Chen, Meng Wei, Xuefeng Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid post-training often mixes supervised fine-tuning (SFT) and reinforcement learning (RL), using training-side signals to set each sample's balance. Such signals characterize the anchor data and policy, but not whether the emphasized behavior helps in the target task and evaluation setting. This mismatch can reactivate and amplify pretrained behavior even after its literal form is removed from supervision. We demonstrate this with DIAA (Dual-Implicit Adversarial Amplification), a per-sample $\sigma$-weighted SFT/RL hybrid. With all literal Python fences removed from its anchor, DIAA emits unexecuted Tool-Integrated Reasoning (TIR) on $29%$ of MATH-500 prompts, three times vanilla GRPO. Paired interventions show $10.6$ percentage points of accuracy recovery when TIR is suppressed and comparable contributions from SFT imitation and $\sigma$-amplification; a student trained on a $0%$-TIR teacher anchor emits it at $45.8%$. Intervention-Certified Amplification (ICA) gates $\sigma$ with paired-rollout target evidence. Frozen and online ICA reduce TIR to $13.8%$ and $11.2%$, halve residual drag, improve accuracy from $47.5%$ to $48.7%$ and $49.3%$, and transfer to held-out GSM8K without retuning.

---


### 407. [A Sign Law for Entropy Drift under Sampler Mismatch in RLVR](https://arxiv.org/abs/2610.34044)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Jacob Steeves, Chang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropy in reinforcement learning with verifiable rewards (RLVR) moves up or down depending on choices that should be neutral, such as whether over-length responses are masked or counted as failures. We trace this to sampler mismatch, where rollouts are drawn with top-k/top-p truncation or at a temperature the learner does not apply, and prove that a constant advantage shift then changes the entropy of a softmax policy, at first order and in expectation, with a sign fixed by the sampler: positive shifts sharpen the policy under any sampler whose likelihood ratio to the policy increases with token probability, including top-k, top-p, min-p, and temperatures below one, and flatten it under flatter samplers. In group-based RLVR with token-level losses, the baseline-controlled part of this drift is set by the token-weighted net advantage, which masking and failing over-length responses can push to opposite signs; the remainder, a covariance between advantages and the sampler's sharpness gap, can feed back over long horizons. On a 2B model, the entropy slope is linear in shifts of the net advantage under truncated sampling and indistinguishable from flat under exact sampling, and token-level importance ratios leave 98% of the drift. In 100-step runs, a net-zero baseline only delays an entropy explosion that exact sampling does not show, a fixed positive shift delays it further, and a baseline weighted by the sharpness gap keeps entropy stable without changing the learner. On a 9B reasoning model over ten steps, the uncorrected rule loses held-out accuracy, whereas zeroing the net advantage or renormalizing the learner gains 8.2 and 8.8 points over it, with no held-out effect under exact sampling.

---


### 408. [HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search](https://arxiv.org/abs/2610.34248)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fahong Zhang, Weijie Jin, Lixu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As a core component of modern RAG systems, approximate nearest neighbor (ANN) search has been extensively studied for decades. In practice, deploying ANN often requires symmetric privacy, where the querier's query and the database owner's data must remain hidden from each other, necessitating a secure multi-party computation (MPC) solution. So far, most MPC-based ANN protocols follow a cluster-based approach: they evaluate distances for the query over a large candidate set and rely on heavyweight primitives such as distributed ORAM to hide access patterns. As a result, each search typically requires $O(\sqrt{N})$ time. We propose HNSecW, a novel MPC protocol for ANN search that achieves the $O(\log N)$ search time for the first time. We first study the single-query setting. Starting from HNSW, the state-of-the-art ANN algorithm, we redesign its control flow and data structures to achieve fully data-independent execution. To further achieve logarithmic search time, we employ offline reshuffling and partial database duplication. Furthermore, we extend our protocol to support multiple sequential queries by introducing a "double visited" caching structure that eliminates redundant cross-query memory accesses, thereby avoiding per-query online shuffling. In addition, we develop a batch-query protocol that exploits higher parallelism to reduce both round complexity and the circuit's critical path. Our experiments show that HNSecW preserves the high accuracy of plaintext HNSW ($\geq 90\%$ recall) and delivers over a $20\times$ efficiency improvement over prior work on million-scale datasets.

---


### 409. [Beyond the Opening: Tracing the First Token's Persistent Influence on Reasoning Length](https://arxiv.org/abs/2610.34350)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruochen Liu, Hao Yan, Ziluowen Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how individual token choices affect reasoning length is important for characterizing reasoning models. Building on prior findings that changing the first reasoning token (hereafter, the first token) can substantially alter reasoning length, we focus on this initial choice to investigate how its influence operates during subsequent generation. One possibility is that the first token changes the early text that follows, which in turn affects reasoning length. However, replacing only the first token of an existing reasoning prefix and resuming generation substantially changes the remaining reasoning length, even though all other prefix tokens are unchanged. To trace this persistent influence, we compare next-token distributions while varying only the first token and find that sensitivity is concentrated at a small set of generation positions. Blocking attention from these positions to the first token reduces the length gap between first-token conditions. Using next-token distributions from a different first-token condition at these positions also substantially changes subsequent reasoning length. Together, these findings suggest that attention to the first token at a few sensitive positions helps sustain its length effect, illustrating how a local token choice persistently influences a sequence-level outcome.

---


### 410. [Dynamic Multi-Step Decoding for Time-Series Foundation Models](https://arxiv.org/abs/2610.34409)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Birmjune Kim, Hyungju Lee, Hyun Oh Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting models typically use a fixed decoding strategy at inference time: either one-shot prediction of the full horizon or autoregressive rollout over atomic chunks. While one-shot decoding reduces error accumulation, it can discard useful sequential structure; conversely, autoregressive decoding preserves temporal dependencies but may compound errors. We argue that the optimal decoding strategy is not fixed across inputs, but should be selected adaptively for each forecasting instance. We propose a dynamic strategy selector that treats the forecast rollout schedule as an inference-time decision problem for frozen pretrained time-series foundation models. The selector is a learned network that ranks candidate rollout schedules using hidden states of the backbone, and is trained on historical windows of the evaluated tasks for each backbone. To make the candidate set tractable over the exponentially large space of horizon partitions, we use dynamic programming that reduces candidate evaluation to quadratic complexity while preserving much of the oracle gain. At deployment, five independently trained selectors vote on each decision, and the policy follows their consensus, falling back to the backbone's one-shot forecast where they disagree. The construction requires only the backbone's hidden states and lightweight selectors, with no fine-tuning of the forecasting backbone. On fev-bench with a frozen Chronos-2 backbone, agreement-gated selection improves point-forecast skill (MASE) over one-shot decoding with statistical significance, mostly on longer horizons. It recovers about 6-8% of the gain that the same dynamic program attains with ground-truth selection. With a frozen Moirai-1.1-R-small backbone, the improvement is also significant on the full benchmark, and for both backbones we claim gains in point accuracy only.

---


### 411. [Rethinking Verification in Agent Harnesses](https://arxiv.org/abs/2610.34577)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhengxin Zhang, Erkang Zhu, Yin Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses enable large language models to act through tools, observe the results, and iteratively work toward a task goal. Verification checks and revises agents' work to improve output quality. Yet there is limited guidance on how harnesses should organize this effort. We study verification as an axis of test-time scaling by examining when to intervene, who checks the work, and how checking leads to revision. Our framework spans four layers of the agent lifecycle: initial instructions, mid-turn reminders, completion gates, and independent review. We compare 17 designs across seven frontier coding models on Terminal-Bench (TB) and SWE-bench Verified (SWE), and introduce VisualBench for expert evaluation of visual and interactive artifacts. Initial instructions and execution-time reminders yield modest, model-dependent average gains on the coding benchmarks, without substantially increasing average output token use. Completion gates can yield larger gains but may substantially increase cost. Independent review by a critic offers a more favorable accuracy-cost tradeoff, improving average accuracy by 5.9-9.5 percentage points on TB and 3.9-6.6 on SWE at 1.13-1.25 and 1.00-1.04 times baseline cost, respectively. On VisualBench, independent review achieves net preferences of 13.2-23.8 points over the baseline across its four designs, exceeding the evaluated L0-L2 designs. Additional review rounds or independent critics further improve average TB accuracy by up to 3.5 percentage points. Together, these results provide empirical guidance for verification design in agent harnesses and support independent review as a practical axis of test-time scaling.

---


### 412. [Correlation-Aware Exploration for Long-Trace Reasoning](https://arxiv.org/abs/2610.34949)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junxing Hu, Zicheng Zhang, Zhiqian Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models trained with Group Relative Policy Optimization (GRPO) now produce chains of thought thousands of tokens long, and recent studies reveal that such training is prone to policy collapse. Entropy regularization is the standard remedy, but it works by pushing probability mass away from the few tokens that carry it and toward the vast low-probability tail of the vocabulary, and it applies this force once for every token of the reasoning trace. This puts the bonus in direct conflict with the entropy decay that convergence requires, and makes its coefficient difficult to set in the long-trace regime. To resolve this tension, we propose Info-GRPO, an information-theoretic framework that cultivates correlation between the policy and a latent prior. Rather than raising entropy everywhere, Info-GRPO builds on the mutual information between a latent variable and the trajectory it induces: augmenting prompts with latent seeds during training lets the model explore diverse policies correlated with the prior, while the seed-conditioned entropy is guided toward convergence. Diversity is therefore carried across whole reasoning traces rather than by per-token randomness, and exploration no longer fights entropy reduction. Experiments show that Info-GRPO outperforms vanilla GRPO and entropy-regularized GRPO across diverse reasoning benchmarks. On AIME24, it improves $Avg@8$ over GRPO by 3.75%, 1.66%, 4.16%, and 4.17% on four backbones, and it reaches the same majority-vote accuracy with $8\times$ fewer samples. Code and models will be publicly released.

---


### 413. [Improving Reasoning with Rollout Agreement for Group-Based Policy Optimization](https://arxiv.org/abs/2610.34951)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sohyun Son, Yerim Hong, Jaeyun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent methods for Reinforcement Learning with Verifiable Rewards (RLVR) use rollout diversity to improve reasoning performance or training efficiency. Despite these gains, the extent to which differences among correct-answer rollouts reflect useful alternative reasoning or unresolved errors remains poorly understood. We investigate this question through a blind paired analysis of a model trained with Group Relative Policy Optimization (GRPO), comparing the highest- and lowest-agreement correct-answer traces for the same problem. Across 126 pairs, low-agreement traces have more spurious reasoning than high-agreement traces (35% vs. 22%), including internal inconsistencies and misuse of problem conditions. Based on these findings, we propose RoAR (Rollout-Agreement Reward), which adds reasoning-level agreement to GRPO's rewards for verified-correct rollouts. RoAR computes this signal from existing on-policy rollout groups, requiring no human-written rationales, additional sampling, or separately trained process evaluator. On five mathematical reasoning benchmarks, the 1.5B GRPO-RoAR model reaches 55.5% mean pass@1 under zero-shot evaluation using 7K training examples, exceeding GRPO and GRPO-CARE by 6.0 and 5.5 percentage points. A separate blind audit of 100 problems answered correctly by all four 1.5B models finds spurious rates of 18% for GRPO-RoAR, 32% for GRPO, 27% for GRPO-CARE, and 37% for DRA-GRPO. Our findings identify reasoning validity as an important consideration when using rollout differences to guide learning. Our code is available at this https URL.

---


### 414. [Diagnosing and Mitigating Long-Session Degradation in Full-Duplex Speech Models](https://arxiv.org/abs/2610.34991)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junho Kim, CheHyun Lee, Donghun Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end full-duplex spoken dialogue models enable natural, real-time spoken interactions with interruptions, backchannels, and overlapping speech. Prior evaluations have assessed diverse interaction capabilities and identified some degradation patterns across conversational turns. However, how model behavior evolves over extended sessions remains insufficiently understood. In this work, we address this gap by systematically characterizing long-session degradation and developing efficient methods to mitigate it. We introduce a closed-loop evaluation framework for long-session stability and apply it to several publicly available full-duplex speech models, revealing degradation over time in responsiveness, spoken content quality, and voice consistency. To mitigate this degradation, we propose a self-distillation-based training framework for lightweight LoRA adaptation that improves long-session stability with a small amount of additional training. We further introduce a two-resolution context (TRC) architecture that preserves recent interactions in full detail while compressing older interaction history into key-value representations. We evaluate our methods on three models with distinct architectures, assessing long-session stability, information retention, and computational efficiency. Across all three models, we show that LoRA adaptation mitigates performance degradation over ten-minute sessions, while adding TRC extends these gains beyond the training session length and reduces KV-cache growth by more than 90%.

---


### 415. [Attention under Bounded Key-Query Similarity: Space Complexity and Transformer Anisotropy](https://arxiv.org/abs/2610.35020)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Justin Y. Chen, Ying Feng, Piotr Indyk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of work on KV-cache compression aims to reduce the memory requirements of autoregressive generation. These methods compress the stored context while approximately preserving attention computation, enabling generation with reduced memory consumption. Almost tight theoretical results on the worst case space complexity of attention have recently been obtained, but they are achieved by instances where queries can be perfectly aligned with keys. This directly contradicts the observed anisotropy of the key/query geometry in real transformers. In particular, it has been shown empirically that key/query cosine similarities are small even for most correlated pairs, i.e., near-perfect alignment of queries with keys does not happen in practice. In this paper, we study the space complexity of attention approximation under the assumption that key/query cosine similarities belong to a small interval around zero, i.e., a query cannot align too much with any key. We give a nearly space optimal algorithm and a corresponding space lower bound. Surprisingly, the distribution of key/query cosine similarities in our lower bound exhibits the anisotropy property empirically established and studied in the literature. Additionally, we show that the simple uniform sampling algorithm is nearly optimal for a typical range of parameters, supporting its surprising effectiveness on real datasets.

---


### 416. [Trainable Boundary-Keeping Where No Formal Answer Exists: A Controlled Knock-In Study of Reward Training in Evidence-Sufficiency Judgment](https://arxiv.org/abs/2610.35226)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** YaJie Yin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning-tuned and reward-trained models are often assumed to verify more reliably because they reason longer or receive correctness signals. We test this in evidence-sufficiency judgment: deciding whether available information actually supports a causal claim, a domain with no decidable correctness reward. Using a pre-registered, same-base, controlled knock-in design, we compare a boundary-keeping recipe (SFT then GRPO) with its own baseline, a scrambled-pairing placebo, and a general-purpose reasoning model under an action-pressure protocol with no evaluation invitation. All load-bearing outcomes are rated by two separate model-rating sessions masked to arm labels; automatic judges only trigger. The trained arm raises spontaneous correct refusal from 25% to 100% (40 per arm; Wilson 95% CI lower bound 91.2%, non-overlapping with the baseline interval [14.2%, 40.2%]), while the scrambled placebo collapses (5% spontaneous / 7.5% invited correct; 91.1% false refusal). The effect is boundary-specific rather than blanket refusal: automatic false refusal on 281 well-formed claims is 1.1% (Wilson upper bound 3.09%), and a targeted 18-item arm-(c) recheck (3 flagged plus 15 accepted) yields 0/18 and 1/18 false refusals in two sessions. The dissociation is the main result: final boundary-keeping is trainable without an inference-time verifier, while observed active numeric/calculation checking in the H3 assay remains near zero; SFT saturation makes the GRPO increment not separately identifiable. A pre-registered mechanism adjudication favors reward internalization of final-action status (H2, best-supported, not proven). The scope is a controlled 14B same-family study: we do not claim proof, cross-family generality, or independent human-expert validation; the rating sessions are model sessions, not human reviewers.

---


### 417. [S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation](https://arxiv.org/abs/2610.35491)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Fei Zhou, Qingqing Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While dataset distillation has witnessed significant advances in image classification, its extension to dense prediction tasks such as semantic segmentation is plagued by two core bottlenecks: bi-level optimization-based approaches suffer from prohibitive computational costs stemming from pixel-wise gradient unrolling, whereas proxy-based generative methods merely infuse visual textures into fixed semantic masks derived from real data, thus failing to condense rich semantic knowledge into a compact set of informative, novel scene generations. To address both bottlenecks simultaneously, we propose a novel Sample-Set Reinforcement Learning (S$^2$-RL) framework for generative semantic segmentation dataset distillation (SSDD). Specifically, S$^2$-RL formulates SSDD as a diffusion model based text-to-image generation paradigm, enabling flexible generation of images with informative, novel semantic distributions via a concise text prompt. Furthermore, we fine-tune a diffusion policy via Group Relative Policy Optimization (GRPO), leveraging a sample-set dual reward paradigm: for individual samples, it enforces semantic alignment with input text prompts and intra-class feature diversity; for sample sets, it maximizes inter-sample semantic distribution diversity by solving a contextual multi-armed bandit problem. These design choices enable S$^2$-RL to distill large-scale semantic segmentation datasets into a compact set of generated samples that encapsulate diverse, informative semantic knowledge without the need of pixel-wise gradient unrolling. Extensive experiments on the ADE20K and COCO datasets demonstrate that S$^2$-RL achieves substantial and consistent improvements over state-of-the-art baselines, establishing a new benchmark for SSDD.

---


### 418. [Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution](https://arxiv.org/abs/2610.35733)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhenshuo Zhang, Ruoxuan Xiong, Hongyang R. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective reinforcement learning is a fundamental problem for modern AI, with applications spanning post-training, reasoning models, and robotic control. A central challenge is to learn policies that balance competing objectives, such as helpfulness versus honesty in safety and alignment, or speed versus energy in robotics. The optimal policy can vary sharply with objective-weighting combinations, and the extent of this variation depends crucially on the degree of conflict among objectives, making per-preference policy learning sample-inefficient. In this paper, we introduce objective-conflict coefficients and derive near-optimal regret bounds for online settings using this measure, thereby quantifying the impact of misalignment on learning efficiency. Then, we design routed ensemble policy learning, an algorithm that maintains a small set of basis policies and dynamically routes trajectories to the policy with the highest potential reward. Finally, we consider trajectory selection as another approach to mitigate objective conflict, and design a kernel surrogate trajectory attribution algorithm that estimates how feedback signals from a set of trajectories influence policy learning on other trajectories. The kernel can capture nonlinear interactions such as synergy and antagonism between trajectories. We evaluate our approach across diverse environments and benchmarks: routed ensembles improve average performance by 4.3% over baselines for online environments from Meta-World and MO-Gymnasium, and kernel surrogate attribution improves correlation with leave-one-out analysis over existing baselines by 50%. When applied to trajectory selection, kernel-based attribution yields a 27% improvement in reward over baseline attribution methods.

---


> [!TIP]
> 当前位于：**401-418**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-418**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
