# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

---

### 1. [On-Device Named-Entity Recognition: A Deployability Study of Accuracy, Cost, Reliability, and Confidence](https://arxiv.org/abs/2610.00007)

**<font color=#1a73e8>作者：</font>** Vinay Kumar Chaganti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named-entity recognition (NER) is increasingly wanted on-device (no API, low latency, data kept local). The practitioner's question is not the leaderboard but which model is deployable, how to evaluate it without human annotation, and whether its confidence can be trusted. We answer these jointly. We place nine systems across three paradigms and 13 M to 8 B parameters: a classical tagger (spaCy), bidirectional-encoder specialists (GLiNER, 166 to 460 M), and generative LLMs run locally (Qwen3-0.6B/1.7B/4B-Instruct, DeepSeek-R1-1.5B/8B), on three datasets of differing character, and report accuracy plus two axes the literature omits: latency and output validity. Because our corpus (RSS-News) had no gold, we built silver gold from a cross-family LLM judge panel, then measured its fidelity against benchmark gold and a full human re-validation of the corpus (strict F1 0.95, an upper bound since the human gold was silver-seeded); gold provenance flips the paradigm ranking, moving from LLM-authored silver to human gold raises every encoder and lowers every generative model. On accuracy alone a 4 B instruct LLM is competitive (it leads on clean newswire), so the encoder's case is deployability: it matches or slightly trails at one-ninth to one-twenty-fourth the size, at millisecond-to-second latency, with zero malformed output, while the smallest generative models emit up to 27% invalid output on long inputs, a failure fixed by scale, not output budget. We then characterize GLiNER's per-span confidence: it ranks correctness well (AUROC 0.76 to 0.86) but is overconfident (ECE 0.24 to 0.47, halved by temperature scaling); thresholding gives a small honest out-of-sample F1 gain; an all-local small-to-large cascade gives a modest, corpus-dependent gain over cost-matched random routing; and confidence tracks correctness but not novelty. Every number recomputes offline from per-span records.

---


### 2. [FourierQK: Filter Shape, Admissibility and the Leakage-Coverage Law](https://arxiv.org/abs/2610.00009)

**<font color=#1a73e8>作者：</font>** Athanasios Zeris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frequency-collapse attention [Zeris, 2026e] achieves large gains over standard dot-product attention by replacing the Q/K dot product with a bandpass-filtered inner product at a learned frequency. A natural follow-up question is: which filter shape works best, and why? We test five hypotheses about filter properties -- DC suppression, Nyquist suppression, bandwidth, centre frequency, and multi-scale coverage -- using a controlled ablation on character-level language modelling (TinyShakespeare, 6-layer GPT). Our main findings are: (1) DC and Nyquist components are actively harmful (val ~= 2.0, equivalent to phase randomisation), confirming that oscillatory bandpass structure is essential, not just any low-dimensional spectral summary; (2) the optimal single-scale bandwidth is sigma ~= 2 bins centred at paragraph scale (~70 tokens), giving a clean gain of Delta = +1.15 nats over BASE-DOT; (3) admissible filters (zero-mean, Mexican Hat DOG m = 2) outperform non-admissible Gaussians at the same scale and provide partial protection against bilateral FFT leakage; (4) bilateral FFT leakage scales monotonically with spectral coverage -- narrowband filters (gap > +4) are clean, wideband filters (gap < +2) are leaky; and (5) causal time-domain Morlet at character scale cannot beat BASE-DOT (K=128 taps covers 50% of T=256 context), motivating word-level experiments in the companion MorletQK paper [Zeris, 2026f]. Together, findings (1)-(5) characterise FourierQK as effective in bidirectional attention settings (encoder-style, e.g. BERT), where full-sequence context is available at both training and inference time; autoregressive generation requires a causal spectral variant such as MorletQK [Zeris, 2026f] (decoder-style, e.g. GPT). Code available at: this https URL

---


### 3. [Heavy-Tailed Memory Traces in Long-Horizon Language Agents](https://arxiv.org/abs/2610.00010)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents increasingly rely on external memory as a frozen world model, yet current memory systems are usually judged only by task success or token cost. We argue that the missing object is the shape of memory use: under finite context and repeated retrieval, agent memory can concentrate on a small core while leaving rare states in a long tail where prediction errors accumulate. We study this effect through a conservative tail audit and find that concentration is reproducible but policy-dependent. Random-walk agents produce log-normal-compatible retrieval artifacts, whereas semantic LLM policies yield the strongest truncated-power-law-compatible core--tail traces. Motivated by this audit, we propose Core--Tail World Model (CTWM), a rank-based memory controller that allocates prompt budget with a single exponent $\tau$ while retaining a summarized tail. On Synthetic Graph World, CTWM preserves full state and transition coverage, reduces prompt tokens by 5.9%, and lowers bottom-half tail prediction error by 13.6% relative to a graph-memory baseline. The same paired comparison gives consistent token savings on ALFWorld and a 24.48% token reduction on LongMemEval with aggregate accuracy parity. These results suggest that heavy-tailed memory traces are not only a diagnostic of finite retrieval, but also a practical control signal for token-efficient agent world models.

---


### 4. [When Do Causal World Models Help Modular LLM Agents](https://arxiv.org/abs/2610.00012)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act through modular systems, such as order, payment, inventory, and shipment services, where actions in one module change which transitions are valid in another. Standard world models usually fit observational traces, but this is not the quantity needed for intervention-time planning: a trace may show that payment precedes shipment without identifying whether payment authorizes shipment, inventory mediates the effect, or a hidden trigger explains both. We study this gap through FedCausalCompose, a causal world-model framework for modular LLM agents in which local actions provide intervention-response evidence for cross-module interfaces. We first show that observational world models incur an irreducible interventional error under unblocked back-door paths, that interface recovery improves with intervention-response coverage, and that an oracle causal composition can beat the non-causal lower bound when coverage and local mechanism errors are controlled. We then test the resulting prediction in diagnostic agent settings. Causal interfaces help most in structured tool environments, where API signatures expose preconditions and downstream effects. In contrast, dialogue and narrative environments often ignore raw edge lists unless a short attention anchor makes the causal information decision-relevant. These results identify a concrete condition for causal world models in LLM agents: causal structure helps when cross-module interfaces are both statistically identifiable and presented in a form the agent can use at action time.

---


### 5. [From Proposal to Verified Effect: Praxa, an Evidence-Bound Harness for Governed AI Agent Execution](https://arxiv.org/abs/2610.00015)

**<font color=#1a73e8>作者：</font>** Stefan G. Creadore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-language-model agents can propose and execute actions, but proposal, authority, dispatch, verified external effect, and serving promotion are different claims. We present Praxa, an agent harness that represents these states explicitly through deterministic admission, brokered execution, external read-back, reconciliation, and reviewed promotion. We report four evidence lanes. First, an author-run repository-local audit at a pinned revision passed 1,027/1,027 unit tests and 89/89 Workerd tests, instrumented all 363 expected source files, and met four coverage floors; raw per-test transcripts and independent reproduction are unavailable. Second, in a provider-backed Terminal-Bench Core 0.1.1 pilot across 12 curated tasks, baseline and reliability-layer arms each passed 17/36 strict trials. The reliability layer used 37.49% more input and 50.73% more output tokens, so the pilot does not support superiority. Third, in a post-debug, two-order coordination-proxy development comparison, baseline and a source-authored candidate each completed 180/180 trials with equal measured accuracy, full hermetic crash recovery, and zero protected violations. The candidate used 37.11% fewer tokens, 33.84% lower estimated endpoint cost, and 11.63% fewer steps; this does not establish improved quality, latency, or production behavior. Fourth, deployed source/configuration evidence shows bounded reflection, recall accounting, memory compilation, and tool-health paths, but no production outcome lift. Praxa's supported contribution is an evidence-bound architecture that makes authority-to-effect transitions explicit and testable. Current evidence does not establish adversarial security, production safety, general specialist superiority, autonomous recursive optimization, or user benefit.

---


### 6. [What Do Rationales Communicate? A Message-Intervention Study in Role-Specialized QA](https://arxiv.org/abs/2610.00018)

**<font color=#1a73e8>作者：</font>** Jiameng Zhang, Hongqiu Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Role-specialized QA pipelines increasingly pass rationales from a reasoner to a verifier, but it is unclear what this message actually buys: better answers, stronger support assessment, or a new failure surface. We introduce a message-intervention diagnostic that fixes the evidence and candidate answer while varying only the rationale passed across the reasoner-to-verifier boundary. On 400 MuSiQue, HotpotQA, and 2WikiMultiHopQA examples with DeepSeek as generator and verifier, faithful rationales add almost no answer accuracy over no rationale, while corrupted rationales strongly alter support judgments. Under a blind verifier prompt, harmless paraphrases shift support by only 0--2.5%, whereas corrupted rationales shift support by 10--22%; an explicit rationale-checking prompt amplifies the same pattern to 34--55%. Final answers move less (2--30%), and only 2.9--35.3% of corrupted support flips co-occur with answer changes. Human audits show why this matters: 16/42 valid corruptions are corruption-overtrust cases, and blind humans reject or mark unclear 9/10 audited corrupted rationales that the model accepts. Cross-model and task-boundary checks show when the channel is active, amplified, inert, or folded into the task label. Rationale sharing should be evaluated as a verification-message mechanism, not merely as a route to higher answer accuracy.

---


### 7. [Encoded but Disconnected: Decomposing Vision-Language Model Failures under a Patching Null](https://arxiv.org/abs/2610.00024)

**<font color=#1a73e8>作者：</font>** Genpei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Across three vision-language model architectures (LLaVA-1.5-7B, Qwen2.5-VL-7B, InternVL3-8B), we report a universal negative finding for mid-layer interpretability. On POPE -- the benchmark common to all three -- the mid layers encode the ground-truth answer in 68-91% of errors, yet this signal is not causally active for the final prediction: residual-stream patching yields 0% non-trivial flip at the layer level on all three architectures, and on two of three at the per-head level (Qwen: 0/12,600 patched forwards). The lone exception, InternVL3 layer-20 head-2, is a non-vocab, self-attending head whose effect is localized to that specific head (p < 1e-4). Despite the null, the errors separate operationally into three failure modes -- Perception Failure, Encoded-but-Disconnected, Prior-Override -- learnable above 60% on all three architectures, and the architecture's prior direction predicts which of two interventions elicits a category-specific response. We report these mitigation effects under oracle labels as evidence the categories are mechanistically real, not as a deployable method.

---


### 8. [Measuring the Microtask Eligibility Gap: When Is an Off-the-Shelf SLM Enough for an Agent Harness?](https://arxiv.org/abs/2610.00025)

**<font color=#1a73e8>作者：</font>** Jundong Hu, Shekar Ramachandran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting tools, ranking past turns. We ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantization changes the answer. We build a benchmark of 4 such microtasks with fixed prompts and automatic metrics, each with a pre-specified threshold $\tau$ anchored to a cheap non-LLM baseline and a CI-aware eligibility rule (a configuration passes only if its confidence bound clears $\tau$). Sweeping Qwen3 0.6/1.7/4/8B at their best (FP16, greedy, one frozen prompt, no tuning), we find an eligibility gap: 0 of 16 (4 tasks $\times$ 4 models) configurations pass (verified by checking the raw outputs and parser behavior). A logprob decision-threshold diagnostic (T1/T3/T4; T2 via a context-length/cascade probe) separates the failures into capability deficits and failures that can be addressed by changing the decoding threshold (4 regimes). Quantization to 4-bit (RTN/GPTQ/AWQ) does damage that depends on model size and moves no configuration into eligibility (certified on the reconstructable hard-label tasks T1/T3, diagnostic/windowed robustness on T2/T4), so the gap tracks model size more than precision; it replicates on Llama-3.x (12/12 ineligible) and is robust to the anchor choice (a $\tau$-sweep) and to prompt wording (0/112 eligible across the original plus 3 neutral paraphrases per cell). The practical implication: place SLMs behind a baseline that meets the CI-backed threshold, and use the SLM only where the baseline fails to meet the threshold; e.g. a 4B re-ranker over a BM25 shortlist beats BM25 ($+0.047$ [0.020, 0.073], without itself certifying eligibility).

---


### 9. [Seeing the City or Recognizing the Place? What Street-View Imagery Adds Beyond Existing Urban Data in VLM Urban Sensing](https://arxiv.org/abs/2610.00031)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Street-view imagery is increasingly used to infer urban attributes, but predictive accuracy alone does not reveal how much a photograph contributes beyond data already available for the same place. We compare image-based predictions with existing urban data across seven attributes from five public resources and three VLMs. The same urban units are evaluated using images, task context, nearby observations, and public records, while image replacements and conflicting records test source reliance. Existing urban data matched or exceeded image-only models for road damage, curb ramps, and house price, while neighbouring official statistics nearly matched the best image result for population. Images were more informative for building type, building function, and low-rise floor count. For floor count, image advantage increased by 5.7 percentage points per doubling of distance to the nearest labelled building and declined for tall buildings whose rooflines often fell outside the frame. Models frequently followed conflicting records. OpenFACADES floor annotations were generated with OpenStreetMap floor values and showed the opposite height-dependent error pattern from image-only reruns. Street-view image value therefore depends on visual legibility and local data coverage. Comparing images with existing urban data can guide image collection and clarify the provenance of derived urban maps.

---


### 10. [The Delegation Danger Band: Why Mid-Capability Sub-Agents Over-Trust Inherited Stale State](https://arxiv.org/abs/2610.00041)

**<font color=#1a73e8>作者：</font>** Jundong Hu, Shekar Ramachandran  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agent frameworks increasingly delegate work by forking sub-agents; a common default makes the child inherit the parent's full working context. We measure how the effect of inherited state changes with capability, where $C_m$ denotes clean fork-fresh accuracy. We compare 3 inheritance policies: Reset (fork fresh: base evidence only), Selective (curated handoff: + the useful prior conclusion), and Full (implicit fork: + the useful conclusion and $d$ copies of a superseded conclusion) over a same-family ladder (Qwen3 0.6/1.7/4/8B) on a frozen, closed-set, action-scored benchmark. Every task is solvable from the base evidence, so performance loss can be attributed to reliance on stale state. (1) Deference to superseded state falls sharply with measured capability $C_m$ (the slope's confidence interval, CI, excludes zero on every family) across 2 synthetic primitives plus MuSiQue and HotpotQA. (2) On the Qwen3 synthetic ladder, net inheritance harm follows a nonmonotone pattern: a mid-capability model (Qwen3-1.7B) is a statistically significant local minimum of net harm, falling below its fork-fresh baseline ($\Delta(32)=-0.19$ [-0.25, -0.12]) and both neighbors, while the weakest model stays near-neutral and the strongest models stay robust. We call this harmful capability range a danger band. A within-model counting-difficulty sweep shows that the effect depends on model class even at matched $C_m$, and a live parent-to-child fork reproduces the mid-model harm. (3) Curated Selective handoff improves average accuracy over Full on all 3 datasets, largest at the in-band model, while the fixed-threshold capability router fails on the other datasets; a transferable router would need to predict the balance between reuse benefit and stale-context penalty. The benchmark is frozen and version-hashed.

---


### 11. [Characterizing a Configuration Where Inference-Time PRM-Pruned Fragment Grafting Is Inert: Evidence from Three Reasoning LMs](https://arxiv.org/abs/2610.00047)

**<font color=#1a73e8>作者：</font>** Khawaja Murad ul Hassan, Mehran Ebrahimi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diversity collapse in parallel chain-of-thought has motivated inference-time interventions built on a natural design: when a process reward model (PRM) prunes a chain, its high-PRM prefix is extracted and grafted verbatim as an in-context demonstration into a still-decoding sibling. We isolate this mechanism, PRM-Pruned Fragment Grafting (PPFG), as the most cost-minimal operationalization of cross-trajectory step-level transfer, and test it at the operating point where prior fragment-grafting work reports gains only under additional compensating ingredients. On Qwen2.5-7B-Instruct with Math-Shepherd on full MATH500 (n=500, three seeds), PPFG in both stagnation- and random-targeting variants is statistically indistinguishable from an independent parallel-CoT baseline on every measured axis. We characterize why: a four-bucket classification of 322 stagnation-rule injection events shows only 14% targeted a genuinely struggling chain; the rest landed on chains that had already succeeded, were near completion, or sat on a flat PRM plateau, states a rescue graft cannot change. No compound-gate refinement jointly achieves well-targeted firing and adequate density, and a random control matches the same parity at 2.4x the firing rate, so the inertness is not heuristic-specific. The finding replicates across three base LMs, six benchmarks, a second PRM, and a compatibility-gate sweep; two-one-sided-tests analysis promotes the parity to positive equivalence on all twelve Qwen/LLaMA cells. A per-event spot-check finds injected chains prune at 2.75x the matched-step rate, but a surviving-sibling counterfactual finds no population-level compensation. A hindsight oracle bounds any per-problem gain from choosing PPFG over independent at +0.13 pp. We contribute an equivalence-testing template for establishing inference-time mechanism nulls, with every claim scoped to its tested operating point.

---


### 12. [Fast Polynomial Transcendentals for LLMs](https://arxiv.org/abs/2610.00049)

**<font color=#1a73e8>作者：</font>** Robert Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphics processing unit (GPU) generations scale matrix, special-function, and memory pipelines at different rates, so kernel bottlenecks move as hardware evolves. FlashAttention-4 exposed this imbalance inside attention on NVIDIA Blackwell. We test whether short polynomial programs can accelerate other special-function-unit (SFU) operations in large language models (LLMs). We first compare native PyTorch evaluation with packed fused multiply--add (FMA) programs in an isolated IEEE binary16 (FP16) sweep spanning L2-resident and high-bandwidth-memory (HBM)-resident working sets. We then replace native sigmoid, tanh, and sigmoid linear unit (SiLU) with degree-3 or degree-4 bfloat16 (BF16) programs in four GB200 integration tasks: dense SiLU, tanh-softcapped attention, sigmoid attention, and routed-expert Swish-gated linear unit (SwiGLU). The programs combine analytical symmetry, target-format rounding, and packed arithmetic inside consuming kernels. The isolated paths improve by 1.19--2.19x in L2 and 1.00--1.70x in HBM. The dense-SiLU, tanh-softcapped-attention, and routed-expert substitutions improve complete training-step throughput by 2.7\%, 2.9\%, and 8.0\%, respectively. The sigmoid-attention substitution improves complete-attention forward by 7.4\% and the complete GPU step by 0.3\%. Same-checkpoint open-weight ablations and one paired pre-training comparison per task extend the evaluation to model behavior. At common horizons near 100 billion tokens, the final smoothed training-loss differences (polynomial minus native) range from $-0.107$ to $+0.079$ across the four tasks.

---


### 13. [Format-Aware Fusion for Fast FP4 Pretraining](https://arxiv.org/abs/2610.00053)

**<font color=#1a73e8>作者：</font>** Robert Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Four-bit floating-point (FP4) Tensor Cores accelerate matrix multiplication, but scale computation, operand packing, layout construction, and saved backward state can erase the gain. We present \emph{format-aware fusion}, which co-designs each quantization producer with its scale domain and consumer layout for native \mxfp{}, global \nvfp{}, and cooperative-thread-array-local \nvfp{}. We evaluate Llama-3-family 8B pretraining through 160 billion tokens using bfloat16 output projections and compiled cross entropy. In matched same-accelerator probes, bfloat16 and Transformer Engine \nvfp{} reach 18.8K and 27.6K tokens/s/GPU, while our fastest custom route reaches 37.9K. \mxfp{} with row-gradient stochastic rounding and fixed-sign 32-value Hadamard weight-gradient preconditioning reaches 37.2K tokens/s/GPU (86.3\% bfloat16 model FLOP utilization) and ends 2.11\% above the raw bfloat16 training-loss endpoint. A Transformer Engine recipe with four final bfloat16 blocks ends 0.87\% above bfloat16 at 27.1K tokens/s/GPU. Downstream rankings differ from training-loss rankings, showing that FP4 outcomes depend jointly on scale contract, operand, and execution path.

---


### 14. [The First Token Is Not the Verdict: Hidden Costs of Reading LLM Judges Without Generating](https://arxiv.org/abs/2610.00054)

**<font color=#1a73e8>作者：</font>** Gnaneswar Villuri, Hashmath Shaik, Alex Doboli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reading an LLM judge's verdict from the logits of its first generated token is cheap, requires no generation, and is exactly what constrained decoding and likelihood-scoring evaluation harnesses produce. We show that this readout distorts position bias in one direction: it overstates it in every condition we test, so figures obtained this way behave as upper bounds. The mechanism is that judges do not always lead with a verdict token, on 12% to 49% of pairs for three Qwen3 judges and under 3% for Llama-3.1-8B and Phi-3.5-mini, and forcing a read on those pairs returns whichever response was shown first rather than a judgment. Pooled over the 924 pairs where a judge did not commit, the forced read flips on 89.7% of them when the responses are swapped, against 47.5% read after generation (paired difference +0.422, 95% CI [+0.365, +0.467]). The distortion is specific to what is measured: it moves position bias by 42 points while moving judge accuracy by under one point in seven of ten conditions, so it misleads whoever audits a judge rather than whoever uses one. A second, smaller failure occurs even when the judge does lead with a verdict token, since it sometimes opens with one letter and reasons its way to the other, on 0 to 5.5% of pairs at a rate uncorrelated with compliance. We recommend reporting the rate at which a judge leads with a verdict token, which costs one forward pass and no labels, alongside any position-bias figure.

---


### 15. [Gradient-Aligned Pair Selection for Personalized Preference Optimization](https://arxiv.org/abs/2610.00061)

**<font color=#1a73e8>作者：</font>** Ruoming Jin, Xinyu Li, Hao Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalizing large language models (LLMs) requires aligning generation behavior with user-specific preferences rather than aggregate quality. While Direct Preference Optimization (DPO) provides a stable framework for preference learning, its effectiveness in personalized settings critically depends on how preference pairs are selected. Existing approaches typically rely on heuristic criteria, such as likelihood-based extremes, which decouple optimization from explicit user utility and can lead to degraded personalization. We formalize personalized preference learning as a geometry-aligned optimization problem by analyzing the first-order interaction between gradients of expected user utility and DPO update directions. Our analysis reveals that, under off-policy sampling, the DPO update transitions from a purely error-corrective signal to a reinforcement-like update when preference margins are directionally aligned with utility gradients. This perspective exposes pair selection as a geometric decision that governs whether preference optimization advances or hinders personalization. Motivated by this insight, we propose GAP-DPO (Geometry-Aligned Preference DPO), an iterative algorithm that performs utility-aware, geometry-aligned pair selection while controlling distribution shift via epoch-wise regeneration. Experiments on personalized text generation benchmarks show that GAP-DPO consistently improves stylistic fidelity, preference alignment, and generation quality compared to standard DPO variants. Together, our results establish gradient alignment as a unifying principle for personalized preference optimization and demonstrate that pair selection is an intrinsic component of the optimization geometry rather than a heuristic preprocessing step.

---


### 16. [A Framework for Egocentric and Exocentric Procedural Understanding via Temporal Segmentation and Semantic Abstraction](https://arxiv.org/abs/2610.00069)

**<font color=#1a73e8>作者：</font>** Vivek Chavan, Jörg Krüger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon ego/exo data contains rich procedural evidence, but are redundant, noisy, and costly to process or retain. We propose a compact framework that converts continuous multimodal workplace video into a structured Procedural State Memory, implemented as a Work Environment Model (WEM). Inspired by event segmentation theory, we detect boundaries using changes in visual context, location, motion, narration, gaze/object interaction, and optional exocentric workspace evidence, rather than fixed windows or visual novelty alone. Each segment is abstracted into an evidence-linked event card containing actor, interval, location, action, objects/tools, pre/post state, confidence, and provenance. These event cards incrementally update the WEM, enabling compact, auditable documentation and retrieval under on-premise privacy constraints. We instantiate the design with frozen DINOv2 and VJEPA-2 encoders and a local language model, and outline evaluation criteria for segmentation quality, memory compression, retrieval fidelity, and long-horizon QA.

---


### 17. [Measuring Human-Like Bias in LLMs? A Critique of Human-Derived Bias Constructs in LLM Evaluation](https://arxiv.org/abs/2610.00070)

**<font color=#1a73e8>作者：</font>** Antonela Tommasel, Markus Schedl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use human-derived bias constructs to study Large Language Models (LLMs), including social-cognitive constructs such as implicit bias and stereotype activation, and cognitive biases such as anchoring, framing effects, and confirmation bias. Such approaches offer alternatives to overt bias probes, particularly when direct questioning may obscure bias or when model behaviour appears normatively acceptable. However, adapting human bias constructs to LLMs introduces an inferential gap. Psychological instruments were developed to study human cognition and social behaviour, whereas LLM evaluations rely on probabilities, text completions, rankings, or simulated decisions. This paper critiques human-centered bias evaluation in LLMs. We show how this gap arises from mismatches pertaining to human-derived constructs, human-model differences, and evaluation contexts, which can blur distinct interpretations of model bias. We then introduce a framework providing an analytical lens for relating these elements to warranted interpretations, with attention to target constructs, operationalizations, scope of inference, and limits of human analogy.

---


### 18. [A Comprehensive Evaluation Framework for Conversational Home Energy Management Systems](https://arxiv.org/abs/2610.00073)

**<font color=#1a73e8>作者：</font>** Wooyoung Jung  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing complexity in home energy management (HEM) demands advanced systems that guide occupants toward informed energy decisions reflecting their background, preferences, and context. Large language model (LLM)-integrated HEM systems (HEMS) have demonstrated promise, but previous studies relied on single-turn or single-task evaluations with response accuracy as the primary metric. Whether such systems deliver effective interactions across the extended multi-turn dialogues typical of real-world use remains an open question. This study introduces a comprehensive evaluation framework of LLM-integrated HEMS derived from the Goal-Question-Metric methodology, organized across five categories: task performance, factual accuracy, interaction quality, control capability, and system efficiency. A total of 23 metrics across multi-turn conversations are proposed and an LLM-as-judge pipeline is employed to enable scalable automated scoring. Its reliability is validated against three trained human coders: after iterative rubric calibration, twelve of the fifteen LLM-scored metrics reached strong agreement (ICC >= 0.73), three of them perfect, while the remaining three exhibited near-zero variance in human scores and are instead reported via mean absolute error (0.04-0.28). To demonstrate the framework's effectiveness, 970 dialogues -- 16 scenarios and five personas -- were generated and evaluated across four conversational HEMS configurations spanning a sophistication gradient, from a vanilla LLM with raw energy data to a multi-agent HEMS. The framework distinguished the four configurations across multiple evaluation dimensions, revealing their respective strengths and weaknesses. This study contributes to conversational HEMS by providing a reproducible, multi-dimensional evaluation methodology that comprehensively assesses sustained, context-aware system performance.

---


### 19. [K-Dense BYOK: An Open-Source AI Research Assistant That Runs Locally and Keeps a Hash-Chained Lab Notebook](https://arxiv.org/abs/2610.00074)

**<font color=#1a73e8>作者：</font>** Aubrey M. Brueckner, Darshil Patel, Yuhuan He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> K-Dense BYOK (bring your own keys) is a free, open-source AI research assistant for scientists in any field that runs on the researcher's own computer. The researcher supplies access to a model of their choice, hosted or running locally, and the application supplies everything else: a place for the work to run, a layer of scientific scaffolding, and a complete record. Each project is an ordinary folder, so the data, the code, the results, and the record stay on a machine the researcher administers and can be read years later without the application. Three things separate it from a chat assistant or a general-purpose coding agent. It ships a library of written scientific procedures, guided workflow templates, catalogs of where research data can be found, and reviewer and writer roles the agent can hand work to. It keeps a Living Lab Notebook whose entries link into an argument and are added to but never erased. And it records what happened by watching what the agent does rather than by taking the agent's word for it, in a log the agent has no tool that can write to. That choice targets the most common failure, model overclaiming, in our earlier benchmark of nine frontier models, by making claims checkable rather than preventing them. On twenty interdisciplinary research prompts, scored under a rubric fixed in advance, K-Dense BYOK led two managed platforms on both scientific quality and research execution. Its deliverables were the only ones that recorded the software they ran in, and the only ones that usually arrived with a command that regenerates the results. One of the managed platforms ran the same frontier model and supplied neither. Those environment records were files the agent wrote, not part of the observed log, which does not yet capture the software environment itself. The code is available under the MIT license at this https URL.

---


### 20. ["very likely" Means "uncertain"? How LLMs Diverge from Humans in Linguistic Uncertainty Quantification](https://arxiv.org/abs/2610.00083)

**<font color=#1a73e8>作者：</font>** Jinhao Duan, Zicheng Liu, Zijie Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans express uncertainty verbally via markers (e.g., "possible," "likely"), yet most LLM uncertainty quantification (UQ) relies on costing likelihood- or consistency-based signals. From a cognitive perspective, accurate verbal uncertainty reflects metacognitive monitoring, representing knowledge boundaries ("knowing that you don't know") to support regulation and information seeking. In this paper, we investigate how LLMs diverge from humans in verbal uncertainty quantification and whether verbal markers can reliably quantify LLM uncertainty. We curate a corpus of human uncertainty markers from psychology and decision-science literature and benchmark LLMs against it. We observe that LLMs encode verbal uncertainty with numerical levels that differ substantially from those of humans. We then introduce METHODNAME, a novel optimization-based algorithm that learns an optimal uncertainty profile over uncertainty markers directly from LLM outputs. By fitting a marker-uncertainty mapping to best explain empirical correctness, METHODNAME discovers how much probability mass each verbal marker should convey, rather than estimating uncertainty via repeated sampling. METHODNAME enables a direct, marker-level comparison of confidence semantics between humans and LLMs, disentangling mismatch and revealing systematic confidence disparities in verbal expressions.

---


### 21. [Scientific Agents: Evaluating Profession-Specific System Prompts on Scientific Tasks](https://arxiv.org/abs/2610.00084)

**<font color=#1a73e8>作者：</font>** Timothy Kassis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detailed profession-specific system prompts raise token use and estimated cost per response without a consistent accuracy gain. We evaluate Scientific Agents, an open-source corpus of 503 profession-specific this http URL profiles, with Gemini 3.8 Flash via OpenRouter in the Pi agent harness. We compare matched profiles with four controls: a minimal baseline ("You are a helpful assistant"), the profile's opening role sentence, a generic scientific rigor guide, and a profile from an unrelated domain. Across nine text-based science benchmarks (4,531 sampled questions, 100 matched profiles), 4,488 items completed all five conditions after API-error retries, scored with automated, rule-based grading. The average profile-baseline accuracy difference is -0.6 percentage points (95% bootstrap interval [-1.5, +0.2] across fixed tasks), and no benchmark shows a statistically clear improvement. Matched profiles produced 1.5-2.3 times as many output tokens and cost 2.2-4.5 times more per successful call. On 60 tool-using BioMysteryBench bioinformatics problems (three runs each for baseline and profile), mean solve rates were 46.7% with the profile and 56.7% at baseline, a difference of -10.0 percentage points (95% interval [-16.7, -3.3]) driven by more frequent token- and time-limit stops under the profile. Longer prompts had one unexpected operational advantage: on SuperGPQA, frequent provider API drops left the short baseline with a correct first-pass answer on only 54.0% of items, against 71.6% with the profile. Generic and mismatched prompts were about as reliable, so this gain comes from prompt length or formatting rather than domain expertise. For the tested model and tasks, loading full profession profiles by default does not improve accuracy and costs considerably more; whether selective retrieval of profile sections or open-ended scientific tasks would change this remains to be tested.

---


### 22. [Legal text classification in Korean sexual offense cases: from traditional machine learning to large language models with XAI insights](https://arxiv.org/abs/2610.00087)

**<font color=#1a73e8>作者：</font>** Jeongmin Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The advancement of natural language processing (NLP) has expanded AI-based text classification in the legal domain. However, accurately classifying legal documents remains challenging due to the complexity of legal texts and subtle differences between legal categories. This study evaluates legal text classification models ranging from traditional machine learning techniques to large language models (LLMs) using ten categories of Korean sexual offense precedents. The results show that fine-tuning small-scale models such as KLUE-BERT on legal data outperforms general-purpose models such as GPT-3.5 and GPT-4.0, as well as traditional machine learning models. KLUE-BERT achieved the highest accuracy of 99.3%, indicating that domain adaptation and fine-tuning can be more important than model size for legal document classification. We further employ explainable AI (XAI) techniques to analyze model predictions and misclassification cases. XAI analysis identifies linguistic features influencing model decisions and limitations in capturing subtle textual cues. Using KICS data, which closely resembles real-world legal case records, we further evaluate the model's generalization capabilities and find that it struggles to interpret implicit contextual cues. These findings highlight the importance of both performance and interpretability in legal AI and demonstrate how XAI can improve transparency in legal text classification. AI-assisted tools can support legal professionals in tasks including document classification, legal information retrieval, and case assessment.

---


### 23. [BudgetSchemaBench: A Budget-Swept Diagnostic for Schema Context in Text-to-SQL](https://arxiv.org/abs/2610.00092)

**<font color=#1a73e8>作者：</font>** Chen Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data agents over structured sources must fit database schema into the model's context window. Large catalogs can span many databases and thousands of columns, so cost constraints may require choosing between table coverage and serialization detail well before the context window is full. We introduce BudgetSchemaBench, an execution-grounded diagnostic for this setting. Its construction derives relevance labels mechanically from gold SQL, without human- or LLM-authored ground truth. Using a pooled 80-database catalog, we sweep four schema-context budgets and compare three representations while keeping each retriever's table ranking fixed. A source-namespace check rejects queries that obtain the correct result from the wrong database. The evaluation covers three conditions: end-to-end retrieval; frozen-gold, in which the required tables are guaranteed; and a probe that removes those tables. For the primary solver with raw serialization, raising the budget from 2.5% to 50% of the catalog improves execution accuracy on 1,279 held-out questions by 18 percentage points under lexical retrieval but only 3 under dense retrieval; the dense retriever already finds most required tables at the smallest budget. When the required tables are removed, 94.6% of correct predictions name one of them exactly, consistent with reconstruction of absent schema from parametric knowledge. For the two main solvers in the frozen-gold condition, the three representations differ by at most 2 percentage points, and the widest paired 95% confidence interval bounds the difference within +/-4 points. We observe the same qualitative patterns with one reasoning model from a different family. When retrieval is coverage-limited, execution accuracy is more sensitive to the schema budget than to the tested serializations. The diagnostic and the code used to construct and evaluate it are publicly available.

---


### 24. [Safety in Self-Evolving Agents: A Survey](https://arxiv.org/abs/2610.00093)

**<font color=#1a73e8>作者：</font>** Jiahao Chen, Zhou Feng, Oubo Ma 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong general capabilities, yet their parameters typically remain fixed after deployment, limiting learning from new interactions. In open-ended environments, this motivates self-evolving agents that continually update reusable state-including model parameters, memories, tool definitions, skills, and workflows-from data, feedback, and accumulated experience. This shift changes the safety problem: once experience becomes reusable state, past events become future causes, and information harmless in one context may later influence decisions with greater persistence, authority, or scope. Self-evolving agent safety therefore asks not only whether a response is aligned or an action authorized, but whether safety properties survive the accumulation, generalization, and cross-context reuse of locally useful experience. We introduce SAVER, a transition-centered framework in which Substrate locates reusable influence, Adaptation captures how it changes, Violation identifies compromised safety attributes, Exposure marks where failures become observable, and Response assesses containment, repair, or revocation. Our survey reveals that failures need not originate from harmful information: legitimate state can become unsafe when adaptation expands its persistence, authority, or scope beyond the conditions under which it was valid. Existing work provides comparatively strong evidence for admission, retrieval, activation, exposure, and local containment, but much less for descendant repair and evaluation after adaptation resumes. We therefore argue for longitudinal evaluation that traces unsafe influence to its originating transition, verifies repair across descendants, and tests whether it can re-emerge under continued evolution.

---


### 25. [Intrusion Detection for Agentic Processes: Evidence-Based Runtime Monitoring](https://arxiv.org/abs/2610.00151)

**<font color=#1a73e8>作者：</font>** Arslan Brömme  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent deployments increasingly combine language-model inference with retrieval, delegation, tool execution, external-system access, and human approval. Security-relevant deviations can therefore emerge across an evolving process rather than in one isolated input or action. Building on the author's earlier black-box architecture for agentic processes and the subsequent evidence-claim model, this paper proposes an Agentic-Process Intrusion Detection System (A-IDS), an evidence-aware security interpretation layer for runtime intrusion detection whose monitored object is the agentic process itself. A-IDS compares evidence-supported observations with a governed and versioned expectation baseline for workflow state, authorization, communication, and mandatory events. Its conceptual contribution combines dynamically due governed expectations, visibility separated from three-valued matching, explicit unresolved observation states, and bounded findings that separate evidentiary status from operational impact. The model further identifies the monitoring plane itself as an attack surface when adversarial content reaches semantic evidence producers through otherwise legitimate observation paths. Some observations may be produced outside the operational agent's self-report path, but the model does not assume complete observability or universally trustworthy capture. Prompt injection is treated both as an input-security problem and as a possible origin of later process deviations and cross-agent influence paths. A-IDS does not infer malicious intent from anomalous behavior, does not treat an unobserved event as proof of non-occurrence, and does not claim a new anomaly detector, temporal logic, or provenance model. The contribution is conceptual: it does not validate an implementation, demonstrate empirical detection performance, establish causal attribution, or provide an enforcement mechanism.

---


### 26. [When the AI Leaves the Tailorshop: Measuring What an LLM Advisor Leaves Behind in Complex Problem Solving](https://arxiv.org/abs/2610.00163)

**<font color=#1a73e8>作者：</font>** Robin Welsch  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Complex problem solving depends on acting effectively and understanding how a system works. AI advice may support these outcomes unequally. Two preregistered experiments compared participants managing a simulated clothing factory with and without an LLM advisor. Across studies, AI-supported participants reported greater confidence and understanding with less effort. In the first study (N=200), assistance increased company value but produced no detectable prediction-accuracy difference. After withdrawal, previously supported participants outperformed controls when decisions were scored against repeating previous choices, but not default settings. Within the AI-supported group, more frequent recommendation alterations predicted better unaided performance. In the second study (N=198), AI-supported participants went bankrupt less often and showed a small knowledge advantage in the registered analysis, largely associated with remaining solvent. More frequent recommendation alterations predicted higher knowledge within the AI-supported group. Applied HAI evaluation should assess users' understanding and independent capability alongside the performance achieved with AI support.

---


### 27. [GPEC: Efficient Pre-LLM Gaussian Process Embedding Correction for Cardiac Video Caption Generation](https://arxiv.org/abs/2610.00196)

**<font color=#1a73e8>作者：</font>** Arefeh Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong potential for video understanding and caption generation, but their performance may decline in specialized medical imaging domains such as echocardiography. This work introduces Gaussian Process Embedding Correction (GPEC), a modular and computationally efficient pre-LLM error-correction method that improves the visual representations used by VideoChat2 for cardiac ultrasound caption generation. GPEC is inserted between the visual projection layer and the language model and learns a residual correction that moves the projected visual representation toward an annotation-guided target. The target is constructed by converting structured video annotations into qualitative attributes, generating a fixed-format reference caption, and mapping it into the language-model embedding space. The correction is modeled using a sparse variational Gaussian Process with inducing points, natural-parameter variational updates, and a block-wise linear kernel, while the original VideoChat2 components remain this http URL method is evaluated using representation-level, caption-level, content-oriented, and execution-time metrics by comparing the original VideoChat2 with VideoChat2 + GPEC under identical input and reference conditions. Results show improved caption similarity and content alignment after applying the proposed correction. Furthermore, GPEC adds less than 0.05 s of inference-time overhead per video in the evaluated setting. These findings indicate that GPEC can improve caption generation in specialized medical video domains with minimal computational cost, without requiring end-to-end fine-tuning of the pretrained multimodal backbone.

---


### 28. [Comedic Fool's Gold: Reward Exploits and Countermeasures in Conversational Humor](https://arxiv.org/abs/2610.00197)

**<font color=#1a73e8>作者：</font>** Sam Larson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate automated rewards for training language models in conversational humor, focusing on reward exploits and countermeasures. Two approaches aim to capture understandable surprise and predicted audience amusement. Controlled tests show that an embedding-based surprise reward accepts word-shuffled replies as readily as witty ones. A fluency filter detects the shuffles, but the combined reward also rejects some witty replies and fails further validation. An audience model's predicted laughter is instead vulnerable to laughter cues in either speaker's messages. Normalizing these cues across speakers blocks the covered attacks, although unmatched expressions remain exploitable. Three reinforcement-learning runs evaluate training with successive reward revisions. The final run improves the combined evaluation score by 0.0903 and reduces zero-score sessions by 40%, but its humor-specific improvement remains below our preregistered target. These findings illustrate a broader challenge for automated reward design: countermeasures must block exploitable shortcuts while preserving the behavior the reward was intended to encourage.

---


### 29. [When a Data Artifact Isn't a Shortcut: Causal Auditing of Synthetic RLVR Corpora](https://arxiv.org/abs/2610.00202)

**<font color=#1a73e8>作者：</font>** Esther Xin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Several recent pipelines build RLVR training data by masking a span of real corpus text and asking a language model to invent plausible wrong answers around it. The correct option is therefore genuine human prose; every distractor is synthetic. Correctness and provenance become entangled, and a policy could in principle learn the second instead of the first. We audit that possibility in GooseReason-0.7M. First we ask whether the asymmetry is visible at all: a classifier reading only five surface statistics (never the meaning) reaches AUROC 0.562 over 315,499 options, barely above chance. The aggregate hides something, though. Code sits at 0.416, below chance, and manual inspection explains why: code distractors turn out to be single-operator mutations of the gold answer rather than freely written alternatives, so the two classes are nearly identical by construction. Detecting a signal is not the same as showing a model uses it, so we then run an intervention. We build a paraphrase-matched control corpus, hold training-set size identical across arms, and train two policies under one fixed budget. The exploitation gap does not favour the unmodified-data arm: 0.021 against 0.027 for the control. Under our budget, in other words, a detectable artifact went unexploited. We think that dissociation, along with the domain-specific construction finding, is worth knowing for anyone curating corpora of this kind, and we release the audit as a mostly CPU-only protocol.

---


### 30. [Query Independent Variable Rate Visual Token Coding](https://arxiv.org/abs/2610.00204)

**<font color=#1a73e8>作者：</font>** Hongbo Zhang, Zihao Yang, Liuyang Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-token compression for vision--language models is posed almost entirely as a selection problem: decide which tokens to keep and discard the rest. The criteria that work best rank tokens by the attention the language model pays them, which makes the ranking a function of the question being asked. That is invisible in a single-turn benchmark and decisive whenever a compressed representation is written once and read many times, as when it is cached across the turns of a conversation or transmitted between a device and a server. We take the other half of the classical transform-coding toolkit instead: keep every token and vary its rate. A transform code exposes each token's measured distortion--rate curve, and a fixed bit budget is distributed across tokens by exact integer rate--distortion optimisation on those curves. No text enters the pipeline, so one compressed representation serves any query. At equal bit budgets, on two datasets and two capacities, it preserves the model's output distribution and its answers better than uniform-rate coding, the closed-form water-fill and distortion-ranked pruning. It matches attention-ranked pruning on the question pruning was tuned for, and overtakes it once the compressed image must answer a different question about the same image.

---


### 31. [EviGraph: Proof-Carrying Selective Recommendation over Temporal Public-Service Knowledge Graphs](https://arxiv.org/abs/2610.00212)

**<font color=#1a73e8>作者：</font>** Yixi Zhou, Sikun Wang, Lei Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public-service recommendations require evidence that matches the requested service, scope, and date. Yet treating every missing detail as decisive can withhold useful recommendations. We introduce EviGraph, which distinguishes critical decision requirements from information that can remain unresolved. A language agent links these requirements to evidence in a temporal knowledge graph, while a deterministic checker establishes whether a recommendation is supported. Evaluation on a bilingual Hong Kong public-service benchmark with executable policy references shows that this distinction reduces unnecessary abstention. Additional verification, however, can withdraw supported recommendations without improving decision quality. These findings suggest that reliable evidence-based navigation depends on specifying what must be established for a decision, rather than simply adding more verification.

---


### 32. [A Holistic Assessment of the Carbon Footprint of Noor, a Very Large Arabic Language Model](https://arxiv.org/abs/2610.00223)

**<font color=#1a73e8>作者：</font>** Imad Lakim, Ebtesam Almazrouei, Ibrahim Abu Alhaol 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As ever larger language models grow more ubiquitous, it is crucial to consider their environmental impact. Characterised by extreme size and resource use, recent generations of models have been criticised for their voracious appetite for compute, and thus significant carbon footprint. Although reporting of carbon impact has grown more common in machine learning papers, this reporting is usually limited to compute resources used strictly for training. In this work, we propose a holistic assessment of the footprint of an extreme-scale language model, Noor. Noor is an ongoing project aiming to develop the largest multi-task Arabic language models -- with up to 13B parameters -- leveraging zero-shot generalisation to enable a wide range of downstream tasks via natural language instructions. We assess the total carbon bill of the entire project: starting with data collection and storage costs, including research and development budgets, pretraining costs, future serving estimates, and other exogenous costs necessary for this international cooperation. Notably, we find that inference costs and exogenous factors can have a significant impact on total budget. Finally, we discuss pathways to reduce the carbon footprint of extreme-scale models.

---


### 33. [Build2SPARQL: A Large-Scale Text-to-SPARQL Benchmark Dataset for Building Knowledge Graph Querying](https://arxiv.org/abs/2610.00224)

**<font color=#1a73e8>作者：</font>** Wooyoung Jung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building automation systems are increasingly represented as semantic knowledge graphs (KGs) using ontologies such as Brick and ASHRAE 223P, creating a machine-readable substrate for artificial-intelligence applications. One promising application is translating natural-language questions into SPARQL (text-to-SPARQL), which would let building operators query these graphs through language agents, but progress is limited by the scarcity of large natural-language/SPARQL benchmarks. This paper presents Build2SPARQL, a large-scale benchmark for building KGs generated by a KG-grounded pipeline: SPARQL queries are produced and validated entirely by graph-traversal code, while large language models generate only the natural-language questions, keeping query correctness independent of model behavior. The pipeline mines six query-pattern families -- linear chains, branching, UNION, aggregation, OPTIONAL, and attribute-filtered -- and phrases each query across five vocabulary registers. Applied to 201 building KGs (180 Brick, 21 ASHRAE 223P), it yields 6,136 executable SPARQL queries and 30,680 questions. A two-rater human validation of 300 questions found 98.8% semantic fidelity, 98.8% naturalness, and 84.0% operational plausibility. A retrieval-augmented evaluation across three open-weight language models raised exact-match accuracy from 0.2-20% (zero-shot) to 56-65% (three-shot retrieved).

---


### 34. [Robust Is Salient: An Informed Adversary Moves the Optimal Signal onto the Salience Pole](https://arxiv.org/abs/2610.00233)

**<font color=#1a73e8>作者：</font>** Cris Huynh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an informed adversary shares the audience of a constrained signalling channel, the signal that best protects the truth is the signal that best describes it. On 108 confirmatory items, the adversary-robust optimum aligns exactly with the salience pole from prior work. Across a 200,000-item pool, the two differ on only 2,748 items --- lying exactly where the prior salience-to-Bayes coordinate is undefined. Where defined, robustness is achieved by moving from Bayesian discrimination entirely to salience. We show this by introducing an adversary to a forced-choice task (abstracted from Deception: Murder in Hong Kong). The adversary knows the target, observes the signal, and argues for the strongest wrong answer using a persuasion budget, $\beta$. As $\beta$ grows, the optimal signal shifts from the posterior-maximizing option to the margin-maximizing one; at $\beta = 0$, the game reproduces the original oracle model with a listener temperature of $\tau = 1$. This effect is real: 18.2 percent of the pool has an optimum that shifts under a finite budget, and each item's critical budget is exact. This coincidence structurally limits empirical evaluation. Two adversary framings change the chosen option of seven language models on 30 to 77 of 108 items against an exact no-effect rate. Yet, no measurement can determine whether this movement is toward the adversary-aware optimum or toward salience, because the two options are identical. This is a structural limit, not a null result. The diagnostic check is cheap: before evaluating adversary-awareness, verify whether the robust target coincides with a heuristic target on the evaluation items.

---


### 35. [Verification Pulses and the Cost of Escaping Wrong Consensus](https://arxiv.org/abs/2610.00256)

**<font color=#1a73e8>作者：</font>** Shivam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> External verification can correct individual outputs while leaving a self-reinforcing population in the basin of a wrong consensus. We study how the timing and addressing of a fixed verification budget affect recovery in an asynchronous binary register. For a general nonlinear response, we derive the minimum fuel required to cross a basin boundary under a peak verification constraint. For a finite population, an exact birth--death calculation gives the probability of subsequent wrong consensus after a pulse. Our main asymptotic result identifies the critical budget window: a leading term $N\log(x_0/b)$ and a correction of order $\sqrt N$, with separate variance contributions from repeated verification targets and autonomous amplification after verification stops. The distinction is substantial: with 16 majority-updated slots and 14 initially wrong, 9 random checks cross the mean-field budget threshold, whereas 23 are required for 95% eventual recovery in the exact model. A prospectively specified experiment records 13,392 language-model responses, including calibration and 108 held-out trajectories. Calibration produces different fitted response regimes, but all four adjusted schedule-comparison intervals include zero. A distributional audit also finds that modest mean-prediction error can conceal a large underestimate of terminal consensus occupancy. The results support risk-calibrated reset scheduling under a specified update contract, while explicitly separating it from distinct-target checking and unrestricted evidence broadcast.

---


### 36. [Attention Manifolds: Steering or Blocking Language Models by Editing Learned B-Spline Surfaces](https://arxiv.org/abs/2610.00257)

**<font color=#1a73e8>作者：</font>** Naveen Mysore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In standard transformer attention, a source token sends the same value vector to every receiver. The query determines \emph{how much} to attend but not \emph{what} to extract. This work introduces \textbf{attention manifolds}: learned 2D B-spline surfaces $S_d(q_d, k_d)$ that modulate each value dimension based on the query-key interaction. Each surface is a tensor-product cubic B-spline initialized to zero, preserving pretrained behavior. Applied to LLaMA 3.2-1B-Instruct and 3B-Instruct, attention manifolds reduce WikiText-2 validation perplexity by 2--2.5 points with 0.3\% parameter overhead. Across 112 diverse prompts, surfaces change greedy-decoded output for 69\% (1B) to 83\% (3B) of cases, with the strongest effects on ambiguous and polysemous inputs (94--100\% change rate). The surfaces improve output quality: correcting factual errors (\emph{``the CAP theorem has three main components''} $\to$ \emph{``it is impossible to guarantee all three''}), increasing precision (\emph{``impossible to know certain properties''} $\to$ \emph{``impossible to know both position and momentum''}), and adding specificity (a generic quote $\to$ an attributed Saint Augustine citation, consistently at both scales). The learned surfaces are also mechanically editable: inverting a layer's coefficients changes greedy output for 9/10 prompts (KL~0.010), providing a geometric mechanism for model steering. Setting surface coefficients to $-1$ creates ``attention walls'' that block value flow through specific dimensions. In a preliminary experiment, a layer-wide wall redirects an explosive-device prompt from specific instructions to general educational content, suggesting a path toward safety-oriented manifold shaping.

---


### 37. [Large Language Bayes Is Not Reparameterisation-Invariant](https://arxiv.org/abs/2610.00265)

**<font color=#1a73e8>作者：</font>** Jian Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Bayes (LLB) answers an informal modelling question by sampling candidate probabilistic programs from a language model, running approximate inference on each, and averaging them with weights proportional to an exponentiated evidence bound. We show that this weighting depends on how a model is written. The log marginal likelihood is invariant to reparameterisation; the evidence bound is not. On eight schools the centered and non-centered programs are the same measure to $5.7\times10^{-14}$, yet their weights differ by $6.1\times$; importance weighting reduces this only to $2.2\times$, and reproducing the inference LLB actually runs, a full-covariance Gaussian matched to the posterior moments, still leaves $1.9\times$ on eight schools and $8.9\times$ in $64$ dimensions. Across likelihood families, dimensions and funnel severities the discrepancy reaches $31.9\times$ and reverses sign, so no single writing is uniformly preferable. It inverts Bayes factors against eight natural competitors, and the induced error in the model posterior, and in any downstream target, is controlled by the spread $\Delta$ of the bound shortfalls through a known sharp Hilbert-distance bound. Across $360$ programs from six language models the parameterisation written ranges from $0\%$ to $100\%$ centered and is stable within a model. Detecting equivalent programs statistically can falsely merge genuinely different models at practical sample budgets; verifying reparameterisations we generate ourselves cannot, and closes the window.

---


### 38. [MOVE: Multimodal Open-world Verification and Expansion for Graph Learning](https://arxiv.org/abs/2610.00268)

**<font color=#1a73e8>作者：</font>** Zekai Chen, Jiayang Xing, Xun Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graph learning faces a fundamental challenge: new classes may emerge after deployment, while models are trained with a fixed label space. Existing approaches typically detect unknown nodes and use LLMs to generate candidate class descriptions, but they do not determine whether existing classes are insufficient to cover these nodes or whether a generated class is reliable enough to expand the class space. Our empirical study reveals three challenges: multimodal information beyond individual modalities is required for unknown-node identification, LLM-generated class descriptions may not fully capture multimodal class characteristics, and directly adding candidate classes can introduce redundant categories. Based on these observations, we propose MOVE, a multimodal open-world class verification and expansion framework. MOVE identifies nodes that cannot be assigned to existing classes by jointly considering visual tokens, textual attributes, and graph context, leverages a multimodal LLM to generate candidate classes, and selectively expands the class space only when candidates are consistently supported by multimodal evidence without introducing unnecessary categories. Experiments demonstrate that MOVE achieves an average improvement of 11.87\% across unknown recognition, open-domain annotation, and downstream graph learning tasks.

---


### 39. [Certainty Is Not Just Correctness: Rethinking Token-Level Certainty in LLM Reasoning](https://arxiv.org/abs/2610.00296)

**<font color=#1a73e8>作者：</font>** Yunfan Zhou, Ye Zhu, Zhihai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token-level certainty is widely used as a proxy for correctness in LLM training and inference. However, the performance of certainty-based methods depends both on the information in certainty scores and on how those scores are used. We therefore directly assess certainty's predictive ability through controlled empirical evaluations across models and tasks. We distinguish two prediction targets: identifying questions a model is more likely to answer correctly and distinguishing correct from incorrect responses to the same question. In our experiments, certainty is generally better at identifying questions a model is likely to answer correctly than at distinguishing correct from incorrect responses to the same question. Certainty also varies systematically across token types and positions within words, reflecting local properties of words and text form. Information about question difficulty appears early in generation, while the weaker information about answer correctness is more concentrated near the end. These findings show that the information certainty provides for decisions depends on the prediction target, the model, the certainty metric, and which token positions in the response are included in aggregation. We further demonstrate the practical value of these findings for test-time compute. We allocate the number of responses using certainty early in generation and weight answer votes using certainty near the end of each response. Compared with a fixed-sampling majority-voting baseline, this approach increases overall accuracy from 78.71\% to 79.54\% while reducing generated-token cost by 82.4\%.

---


### 40. [Decoding the Disaster: Multi-Task Geospatial Reasoning with Vision-Language Models and Crowdsourced Imagery for Disaster Mapping](https://arxiv.org/abs/2610.00302)

**<font color=#1a73e8>作者：</font>** Wenping Yin, Fabian Desuer, Ziqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crowdsourced imagery provides timely, fine-grained, street-level observations for disaster mapping, complementing conventional remote sensing imagery (RSI) during emergency response. However, such imagery is often unstructured, spatially ambiguous, and lacks reliable geographic metadata, making manual geolocalization and interpretation labor-intensive and difficult to scale. This work proposes a multi-task Geospatial Reasoning Disaster mapping framework, namely GRDisaster, to examine the potential of vision-language models (VLMs) in understanding, geolocalizing, and reasoning over crowdsourced disaster imagery. GRDisaster is built on a newly curated benchmark dataset derived from PhotoMappers, comprising 26,340 images organized into human-validated volunteered geographic information (VGI), street-view imagery (SVI), RSI cross-view triplets covering multiple disaster events from 2018 to 2024. The framework combines deterministic and probabilistic cross-view geolocalization with multi-view fusion to associate VGI images with georeferenced SVI and RSI. It introduces two sets of spatial reasoning indicators for cross-view geolocalization validation and disaster damage assessment. These indicators use structural, environmental, and global-scene cues to validate cross-view correspondences and visually observable damage evidence with expert-verified annotations to assess disaster severity, improving the interpretability of VLM outputs. To our knowledge, this study provides the first systematic investigation and unified evaluation framework for examining how VLM-based spatial reasoning can transform crowdsourced disaster imagery into actionable geospatial artificial intelligence (GeoAI) through cross-view geolocalization validation, interpretable spatial reasoning, and damage-aware severity assessment.

---


### 41. [Rules to Tools: Executable Checks for LLM Agents in Scientific Computing](https://arxiv.org/abs/2610.00313)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Guojiang Zhao, Chen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific coding agents receive equations, boundary conditions, and output requirements in writing, then must assess the programs they revise. Rules to Tools (R2T) supplies prepared executable checks of public scientific requirements. Matched SciCode repair groups share written checks, starting programs, model, and budgets; the tool group receives a callable implementation. Across two task-ID cohorts, complete repair is 26/30 with text and 29/30 with the prepared checks. Three task IDs favor tools, one favors text, and eleven tie. The eight-ID cohort scores 13/16 versus 15/16, with a task-cluster bootstrap 95% interval of [-12.5, 43.75] percentage points for the difference. The larger shared-definition SciCode cohort ties at 13/24 per group. Five development-exposed tasks with alternate starting programs score 3/10 versus 7/10. The tool group favors tasks 17, 77, and 11; initial checks flag task 17 and report no violation for tasks 77 and 11. Task 37 favors text and has no initial reported violation. A fresh source-through-Python arm also reaches 15/16, matching the dedicated command's aggregate. In a matched PDE comparison, detailed text scores 23/24 and checks score 24/24, with 31.2% lower reported model output for checks. Agent-side output savings vary by cohort, while public CPU use rises in both task-ID cohorts. These results measure task-dependent repair outcomes and agent-side costs with prepared checks.

---


### 42. [Predictive Credit: Measuring What Scientific Explanations Add to Experimental Forecasts](https://arxiv.org/abs/2610.00314)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Xueqi Li, Yibo Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research agents explain planned experiments. We measure predictive credit with paired forecasts sharing an intervention, forecaster, and outcome while varying description, matched explanation, and donor context. Five checks track commitment, delivery, predictive gain, alignment, and known-signal uptake. Across 336 prospective states in controlled learning, 12 Tox21 endpoints, and 24 OpenML tasks, v5's frozen credit decision was inconclusive. Tox21's preregistered ROC AUC interval-score harm test was unmet ($D-M=-.0026$, 95 percent interval [$-.0174$, .0104]); OpenML's joint formation, point-equivalence, and repeatability rule was unmet. Matched point-accuracy gains over description remained unconfirmed, and Tox21/OpenML seed-donor intervals spanned zero. Under requested DeepSeek V4 Pro, matched and donor cards reduced secondary Tox21 drift by 64.5 and 59.1 percent. A DeepSeek V4 Flash replay raised matched point MAE from .01823 to .02020 and missed matched-donor interval-score equivalence. OpenML full-card assignment widened nominal 80 percent intervals by 21 percent, with 49.3 percent coverage versus 51.4 percent for description and content in 66/144 cards. Direct-text Flash delivered all 144 notes without detectable matched point-accuracy gain. A researcher-authored mechanism positive control lowered point MAE by 2.60 percentage points versus description. The protocol measures predictive credit for research-agent benchmarks and scientific forecasting; natural-explanation credit remained unconfirmed at the tested donor resolutions.

---


### 43. [DuplexSpeechBench-Document Grounding: Benchmarking Document Grounding and Hallucinations in Voice Agents](https://arxiv.org/abs/2610.00316)

**<font color=#1a73e8>作者：</font>** Puneet Mathur, Nedim Lipka, Zeyu Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice agents enable low-latency, natural interaction, yet their ability to faithfully ground responses in external documents remains underexplored. We introduce DuplexSpeechBench-Document Grounding (DSB-DG), a benchmark for evaluating document grounding in voice agents across five professional domains. DSB-DG targets three failure modes: Context Saturation, which measures grounding under increasing document length; Grounding Decay, which measures retention of document facts across multi-turn dialogue; and Proactive Grounding, which evaluates whether context re-injection mitigates conversational drift. The benchmark contains 1,636 adversarially verified QA pairs from 50 documents covering five professional domains, and supports fully automatic evaluation of grounding accuracy, hallucination, and response latency. Across systems spanning cascaded, proprietary full-duplex and real-time, and open-weight speech2speech architectures, we find substantial differences in effective grounding capacity. While cascaded pipeline (ASR-LLM-TTS) achieves the highest grounding accuracy, Gemini-Live and GPT-Realtime closely trail behind. Open-weight systems exhibit distinct failure modes, most notably an abrupt context-capacity collapse and multi-turn grounding decay. More broadly, grounding fidelity degrades with context and conversational load, and failures frequently manifest as unsupported generations rather than abstention. We show that contextual grounding as a key unresolved challenge for reliable full-duplex voice agents.

---


### 44. [Refusal Localizes, the Damage Relocates: Safety Layers Under Few-Sample Fine-Tuning](https://arxiv.org/abs/2610.00320)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Dongyub Jude Lee, Sugyeong Eo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning adapts aligned large language models (LLMs) to downstream tasks, but a few dozen harmful examples can remove their refusal of harmful requests. Prior work localizes safety-related behavior to specific layers, directions, and tokens, suggesting targets for protection. We test whether successful localization and recovery support defenses that survive changes in the attack. Across six checkpoints from four model families, harmful and benign prompts remain linearly separable after attack, and patching full clean hidden states into the compromised model restores refusal at a reproducible transition depth. Building on a prior layer-freezing defense, we freeze every layer up to this depth and repeat the attack. At a hundred harmful examples, refusal remains near zero on all six checkpoints, with recovery transitions above the frozen boundary. In a second study, removing the update's top two singular directions restores refusal after short attention-only fine-tunes on four checkpoints. On Llama-3.1-8B, ordinary training changes weaken this repair and an attacker who spreads the update defeats it. A spectral detector calibrated on benign Llama fine-tunes misses most repair failures on that checkpoint. Localized freezing can nevertheless help preserve refusal when a few harmful examples enter training data unintentionally. These results show that an attacker can bypass a region identified by recovery and defeat a repair that works across multiple checkpoints, motivating five checks for defenses against adaptive fine-tuning. Code is available at this https URL.

---


### 45. [CAST: Cost-Aware Speculative Trees from One-Pass Block Drafters](https://arxiv.org/abs/2610.00321)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Sugyeong Eo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by drafting future tokens cheaply and verifying them with the target model in parallel. Block drafters score a whole block of future tokens in one forward pass, yet standard decoding verifies only the top-scoring chain and discards the other candidates. Because these candidates are already scored, verifying more of them adds target computation but no extra drafting. We introduce CAST (Cost-Aware Speculative Trees), which packs these candidates into a tree and verifies it in a single target pass, leaving the target model, drafter weights, and decoding rule untouched. To decide how wide the tree should be, CAST adds candidates while the expected gain from the next one outweighs the verification time it adds. The width therefore adapts to each deployment from a latency measurement, without sweeping over widths. We evaluate CAST across five domains on three GPU generations and two model families. At its predicted width, CAST is faster than the standard chain in all eight settings, by up to 43%. We also find that the best width depends strongly on the deployment. Where verification cost jumps at a kernel boundary, a 128-token tree is only 2% faster than the standard chain, whereas the tree at the predicted width is 20% faster. Furthermore, we prove that CAST leaves the target output distribution unchanged under both greedy and sampled decoding. Code is available at this https URL.

---


### 46. [Actions with Receipts: Jointly Binding Claims, Evidence, and Execution for Replayable Tool-Agent Auditing](https://arxiv.org/abs/2610.00327)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using agents can expose citations and execution logs while leaving a critical association unaudited: whether the claim shown to a user is the claim emitted by the committed execution and supported by the cited source. A valid citation and a valid trace can therefore remain individually well formed while being transplanted across claims, actions, runs, or source versions. We introduce a claim-anchored execution contract that jointly binds the emitted claim, its exact source span, the ordered execution prefix that produced it, and the source version and access state observed by that execution. Each receipt contains an emission anchor that deterministically locates the claim inside a committed answer or claim-bearing action, together with source identifiers, offsets, hashes, quotes, and a domain-separated execution commitment. A deterministic integrity verifier reconstructs these bindings before semantic or task labels are joined. We separate this integrity plane from a pluggable support plane, so structural validity is not used as a proxy for entailment. The contract exposes seven independently testable properties: claim-emission binding, source binding, ordered-execution binding, oracle separation, persisted-object replay, execution-rerun consistency, and version/access binding. Across 1,280 cross-object attacks, the joint contract detects 1,275 substitutions (0.9961). Removing a targeted property reduces its attack-detection rate to 0.0156-0.0625. On an independently adjudicated 384-pair split, the conflict-aware support guard reaches F1 0.8865 and false acceptance 0.0729; on unseen failure families, these rates are 0.8679 and 0.0938.

---


### 47. [Mathematical Transfer in LLMs Follows Reasoning Approach More Than Topic](https://arxiv.org/abs/2610.00331)

**<font color=#1a73e8>作者：</font>** Sajad Goudarzi, Samaneh Zamanifard, Seyed Amin Seyed Haeri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When selecting mathematical training data for LLMs, a natural organizing principle is topic: probability examples for probability targets. An alternative is reasoning approach: worked solutions that share a solution method with the target, even when the mathematical domain differs. We ask which relation produces greater transfer after fine-tuning. We evaluate two counterbalanced $2\times2$ designs: probability and combinatorics crossed with invariant reasoning and double counting (2,000 problems), and number theory and geometry crossed with complement and pigeonhole reasoning (800 problems). In each design, every cell serves as the held-out target in turn: same-approach (SA) sources share the target's method but change the topic, while same-topic (ST) sources share the topic but change the method. Every source appears once in each role, so additive source-quality effects cancel from the equally weighted aggregate contrast. Across five base models and three training seeds per design, SA outperforms ST in all 40 seed-pooled model--target comparisons. Model-level advantages range from 8.2 to 16.2 percentage points in the primary design (mean: 10.8) and from 12.0 to 16.0 in the second design (mean: 14.3); all ten model-level 95% confidence intervals exclude zero. In both designs, ST sources are more similar to targets under embedding and lexical measures, so the SA advantage runs opposite to the measured ordering of statement-level resemblance. These findings identify reasoning approach as a more effective matching criterion than topic for mathematical transfer across the evaluated topic--approach combinations.

---


### 48. [The Weakest Link: Distilling LLM Reasoning with Worst-Case Constrained Reinforcement Learning](https://arxiv.org/abs/2610.00332)

**<font color=#1a73e8>作者：</font>** Matthieu Zimmer, Xiaotong Ji, Tu Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distilling the reasoning capabilities of large language models (LLMs) into smaller students is a central challenge for efficient deployment. Current approaches face a fundamental tension: optimizing purely for verifiable task rewards (e.g., via GRPO) leads to reward hacking, where students arrive at correct final answers through flawed intermediate logic, while regularizing with soft divergence penalties against a teacher (e.g., KL-based distillation) dilutes task performance and, critically, allows the student to compensate for severe logical violations at one step with high teacher agreement at others. We argue that this averaging is fundamentally misaligned with the nature of reasoning: a chain-of-thought is only as valid as its weakest link. Motivated by this observation, we formulate reasoning distillation as a constrained reinforcement learning problem in which the task reward is maximized subject to a worst-case constraint on the teacher log-likelihood along every prefix of the trajectory. To avoid the prohibitive cost of dual Lagrangian solvers and the test-time teacher dependence of state-augmented methods such as Saute, we derive an unaugmented constrained MDP whose reward transformation preserves the hard-constraint semantics, admits a low-variance policy gradient decomposition into single-step and long-term terms, and provably satisfies the worst-case constraint almost surely in the penalty limit. Through extensive experiments on mathematical reasoning and code generation tasks, we demonstrate that our method significantly expands the accuracy-fidelity Pareto front. By matching the high Final Answer Correctness of pure RL and drastically reducing teacher constraint violations, we ultimately achieve the highest rigorous Reasoning Success Rate across all evaluated settings.

---


### 49. [LEGO-OPD: Factorized Teacher Composition for Multimodal On-Policy Distillation](https://arxiv.org/abs/2610.00333)

**<font color=#1a73e8>作者：</font>** Jaeyun Shin, Hangeol Chang, Jong Chul Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal on-policy distillation (OPD) aims to improve visual grounding while preserving the strong reasoning capabilities of language models. Recent multi-teacher approaches combine LLM and VLM teachers to provide complementary supervision. However, directly using a VLM's full predictive distribution entangles its visual grounding signal with its own language prior, preventing the grounding information from being transferred independently. Conversely, increasing the strength of visual supervision can improve perception but may overemphasize visual evidence and degrade language reasoning. To address this trade-off, we introduce LEGO-OPD, which selectively composes factors from a Language Expert and a Grounding expert into One teacher distribution for multimodal OPD. Under a generalized Bayesian formulation, the language expert provides a prior over candidate tokens, while the grounding expert contributes a visual likelihood that updates this prior, rather than transferring its complete predictive distribution. This factorized composition allows language reasoning and visual grounding to be controlled independently. We further introduce adaptive calibration to determine how strongly the visual likelihood should update the language prior at each decoding prefix. Specifically, LEGO-OPD uses the grounding expert's image-induced prediction shift as a prefix-dependent reference, preventing both insufficient and excessive visual supervision. Experiments with Qwen3 models show that LEGO-OPD consistently outperforms the evaluated single- and multi-teacher OPD baselines on both multimodal and text-only reasoning tasks. Moreover, it improves the initial student's visual perception while preserving text-only reasoning.

---


### 50. [Three Pathways of Student-AI Interaction: Constraint-First Design for Higher-Order Thinking](https://arxiv.org/abs/2610.00338)

**<font color=#1a73e8>作者：</font>** Fatima T. Zahra  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How students interact with artificial intelligence (AI) systems in educational settings may determine whether that interaction supports or displaces critical thinking. This paper introduces two contributions. The first is the Three Paths of Student-AI Interaction, a typological framework identifying three qualitatively distinct modes of student-AI engagement: Passive Review, Direct Question, and Strategic Dialogue. The second is the Next Level Teaching Blueprint (NLTB), a three-stage instructional design system intended to make Strategic Dialogue more likely. Qualitative content analysis of 50 randomly sampled student-AI interaction messages from an undergraduate research methods course was used to examine the typology. Two human coders achieved 68% path-level agreement ($\kappa$ = .48), with 80% agreement on Strategic Dialogue identification specifically. GPT-5, used as a third coder, produced a similar overall distribution and introduced a coding category absent from the human scheme. Path 1 (Passive Review) accounted for 46% of exchanges in the primary researcher's classifications, Path 2 (Direct Question) for 18%, and Path 3 (Strategic Dialogue) for 36%. A second, descriptively examined dataset contained predominantly Strategic Dialogue content, offering a preliminary indication that instructional framing may influence which path students take. Together, the Three Paths framework and the NLTB contribute a language for describing student-AI interaction and a design approach for supporting higher-order engagement.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
