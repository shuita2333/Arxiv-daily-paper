# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 151. [CityToolVQA: Tool-Augmented Visual Question Answering for 3D Spatial Cognition in Urban Low-Altitude Environments](https://arxiv.org/abs/2609.32427)

**<font color=#1a73e8>作者：</font>** Boao Yu, Yingzhen Nie, Yue Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CityToolVQA addresses the weak performance of Vision-Language Models (VLMs) on quantitative tasks in urban low-altitude visual question answering. We divide the seven tasks into qualitative and quantitative groups: qualitative questions are answered directly by the VLM, whereas quantitative questions are handled by an external visual-geometric toolchain that performs object grounding, segmentation, depth back-projection, and spatial computation. The toolchain can be attached to different VLMs in a zero-shot manner; a Depth-Assisted Prompt Inference (DAPI) fallback is triggered when the main-chain detection is invalid or unreliable, and CityToolVQA-SFT adapts the 8B backbone to tool-conditioned inputs. On the 73,324-question Open3D-VQA-v2 test set, CityToolVQA-SFT (Qwen3-VL-8B) reaches 67.6% overall accuracy, and attaching the toolchain to ten open-source VLMs improves quantitative-task accuracy by 12.7-36.9 percentage points. These results indicate that externalizing explicit 3D geometric computation effectively complements the limited ability of RGB-only VLMs to estimate metric distances and object sizes.

---


### 152. [Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions](https://arxiv.org/abs/2609.32428)

**<font color=#1a73e8>作者：</font>** Qingzhuo Wang, CaiYi Wang, Jinglu Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents increasingly perform state-changing actions that require user authorization. Yet existing approaches do not provide a principled mechanism for selectively updating prior authorization when only part of an instruction changes. To this end, we propose an Authorization-Closure-Graph (ACG)-based framework that represents authorization and its dependencies as an evolving, versioned state. ACG selectively invalidates authority affected by a revision while preserving unaffected portions of the authorization state, and computes a minimal repair that identifies only the missing evidence or authority required for execution. This enables agents to adapt to revised instructions while avoiding stale authority and unnecessary authorization requests. We evaluate ACG across three advanced LLMs in two natural tasks, and ACG consistently improves action safety rate and task success rate. Code is available at this https URL.

---


### 153. [PrismQuant: Optimal Null-Space Rotations for Grouped Quantizers](https://arxiv.org/abs/2609.32429)

**<font color=#1a73e8>作者：</font>** Yanlong Chen, Yining Chen, Song Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smaller activation outliers do not necessarily imply better low-bit quantization: their alignment with the quantizer matters. We introduce PrismQuant, a quantizer-aware rotation framework that aligns the leading activation eigenspace with the constant group subspace of asymmetric grouped INT4. The affine offsets represent the energy in this subspace without widening the range within the group. We formulate rotation design as a Ky Fan trace maximization and derive a closed-form solution that is provably optimal for this alignment objective. Compact Householder transformations and their compact-WY representation enable gradient-free construction and efficient application at both foldable and online sites. A predictive range law further connects unaligned activation energy and group size to quantization-relevant variation. Experiments on Llama, Qwen, and Mistral span dense models up to 70B parameters and a 30B mixture-of-experts model. Under W4A4KV4, PrismQuant sets the state of the art on Llama-3.2-3B among the compared methods in both perplexity and accuracy. On Llama-3.1-70B, it attains 3.85 perplexity and 72.46% average zero-shot accuracy, only 0.22 percentage points below full precision. In the deployment study on Llama-3.1-8B, our optimized implementation achieves 1.51x prefill and 1.22x CUDA Graph decode speedups over matched FP16 baselines, with 56.34% lower decode peak memory and only 2.35% additional Graph decode latency over Hadamard. Code is available at this https URL.

---


### 154. [Multi-Agent System Search via Active Substructure-aware Policy Optimization](https://arxiv.org/abs/2609.32430)

**<font color=#1a73e8>作者：</font>** Beicheng Xu, Bowen Fan, Weitong Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs enable multi-agent systems (MAS) to tackle complex tasks, but manually designing agent roles, prompts, and communication structures requires substantial expertise and effort. This motivates learning policies that construct query-specific MAS from execution reward. Existing approaches typically train these policies by repeatedly traversing a fixed set of training queries and assigning rewards at the workflow level. However, this overlooks differences in queries' evolving learning potential and obscures which substructures improve solution quality. In this paper, we propose Active Substructure-aware Policy Optimization (ASPO), a RL framework for query-level MAS search. ASPO introduces an Adaptive Query-Selection Mechanism (AQSM) that focuses training on queries at the policy's competence boundary: those it can solve but not yet reliably. A complementary discovery mechanism widens architectural exploration for hard queries, helping distinguish insufficient exploration from operator capability limits. Beyond query selection, ASPO introduces substructure-level rewards that measure output-quality gains within each action's descendant subgraph. These rewards guide proximal policy optimization to reinforce useful architectural refinements and discourage redundant or harmful computation. Together, these mechanisms prioritize learnable queries and provide fine-grained feedback for learning effective MASs. Across six benchmarks spanning mathematical reasoning, general question answering, and code generation, ASPO ranks first on every benchmark against twelve baselines.

---


### 155. [DualGuard: Dual-Mode Quality Control for Logic-Preserving Data Augmentation](https://arxiv.org/abs/2609.32431)

**<font color=#1a73e8>作者：</font>** Shenghao Li, Lin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models provide a practical way to generate augmented data for logical reasoning at scale, but a larger generation volume does not guarantee semantic, label, or logical reliability. Existing work has improved generation quality through generation constraints, candidate validation, filtering, and feedback-based revision; however, once a quality judgment is available, deciding whether a candidate should be retained, filtered, or repaired remains an important control problem. We propose DualGuard, a dual-mode quality-control framework for logic-preserving data augmentation. The first mode uses the current instance and candidate batch for selective retention, filtering, attribution, and targeted feedback. The second mode accumulates cross-instance execution records of augmentation actions on top of per-sample diagnosis and attribution, compares new executions against each action's own historical behavior, and supports retrospective anomaly inspection, targeted rollback, and bounded repair. Both modes share semantic verification and additionally use symbolic verification when a reliable logical form is available. Across seven downstream tasks in the Two-Stage Transfer setting, DualGuard achieves the highest Accuracy on five tasks and outperforms the no-augmentation BERT baseline on all seven. Controlled ablations further show complementary roles for Memory, Z3, and history-aware anomaly control.

---


### 156. [From Latents to Wires: Surgical Post-Editing on Large Language Models](https://arxiv.org/abs/2609.32434)

**<font color=#1a73e8>作者：</font>** Jiankai Jin, Xiangzheng Zhang, Zhao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given a large language model (LLM), can whoever holds the weights name a semantic target (e.g., the model's identity), locate the model components that produce it, and edit them so that the target no longer appears while other capability is preserved? We call such an edit on a trained model a post-edit. We present L2W (latents to wires), a framework that performs surgical post-edits for named semantic targets. For localization, L2W uses Jacobian lens (J-lens) attribution to score components against the semantic target. For surgical removal, because LLM mechanisms are redundant (i.e., a semantic target may have multiple components producing it), L2W runs Counterexample-Guided Causal Cut (CGCC) until the target no longer appears. CGCC first cumulatively closes model components, treating each surviving expression of the target as a counterexample that exposes the next components to close, and then reopens some of them to preserve capability. In a controlled experiment with an implanted behavioural watermark, L2W removes the watermark, and its localization lands on the model region the implant changed. Across three model configurations, L2W removes model-metadata (e.g., identity) self-claims in all nine runs, and adult-content refusal in all three, with no held-out target residual. L2W further composes two post-edits on a text-to-image model: one removes the refusal of requested nudity, and a second removes the nude rendering the first exposes. The results support post-editing as a complement to post-training: post-training installs preferred behaviours, and post-editing removes named unwanted ones.

---


### 157. [Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It](https://arxiv.org/abs/2609.32444)

**<font color=#1a73e8>作者：</font>** Tianrun Yu, Kaixiang Zhao, Shangzhe Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study training-inference mismatch in reinforcement learning with verifiable rewards (RLVR) for large language models, where rollouts are sampled by an inference engine while gradients are computed by a training engine, and the two engines assign different probabilities to the same tokens. To account for this discrepancy in policy updates, we introduce calibrated importance sampling (CIS). CIS is motivated by an empirically supported logit-displacement characterization that expresses the mismatch as an additive displacement $\varepsilon_t$ in log-odds, determined by the per-logit perturbation before the softmax, whose distribution is approximately invariant to token confidence. This characterization motivates a confidence-aware truncation: large positive displacements are truncated at a single constant threshold, which maps back to an importance-ratio cap that tightens as token confidence increases. Theoretically, we show that CIS replaces the unbounded second moment that governs the error of exact importance sampling with a term bounded by a constant, at the cost of a bias controlled by the truncated excess. In evaluation across three mixture-of-experts models and five mathematical reasoning benchmarks, CIS achieves the highest five-benchmark average on all three models among the evaluated baselines. Diagnostic analyses show that CIS places less truncation bias on low-confidence tokens than truncated importance sampling, while upward clipping of small importance weights reduces held-out accuracy.

---


### 158. [Masking Frequent Tokens Sharpens Direct Preference Optimization](https://arxiv.org/abs/2609.32445)

**<font color=#1a73e8>作者：</font>** Harshvardhan Saini, Samyak Jha, Yiming Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) aligns language models by optimizing over sequence-level sums of token-wise implicit reward differences. However, we identify a pervasive pathology in this formulation: a disproportionately small subset of high-frequency token types dominates cumulative sequence scores while appearing symmetrically across both preferred and dispreferred responses. Specifically, under canonical Qwen tokenization on Anthropic HH-RLHF, merely 69 token types account for $55.1\%$ of all response tokens and $85.9\%$ of within-pair shared token mass, exhibiting substantially lower preference-side specificity than the remaining vocabulary. This symmetric ubiquity induces gradient entanglement and dilutes the discriminative preference signal propagated through the objective. To resolve this issue, we introduce \emph{Anisotropic DPO} (\textsf{ADPO}) and its canonical realization, \emph{Frequency-Hard DPO}. Using a fixed, label-agnostic vocabulary mask, our method zeroes the implicit reward contribution of high-frequency response tokens while assigning unit weight to informative positions, thereby suppressing gradient interference without modifying preference pairs, discarding context, or introducing learned parameters. Here, \emph{anisotropy} designates non-uniform token-level objective weighting rather than representational geometry. Extensive empirical evaluations on AlpacaEval, MT-Bench, and Arena-Hard demonstrate that Frequency-Hard DPO consistently outperforms standard DPO across Qwen-2.5-7B-Instruct and Llama-3-8B-Instruct, establishing that selectively masking shared high-frequency tokens offers an effective, zero-overhead mechanism for robust preference alignment.

---


### 159. [ForkLeft: Entropy-First Rollouts for Prefix-Aligned Autoregressive-to-Diffusion Distillation](https://arxiv.org/abs/2609.32448)

**<font color=#1a73e8>作者：</font>** Junming Liu, Jicheng Wang, Yifeng He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive Next-Token Prediction (NTP) has enabled strong reasoning capabilities in language models, while Diffusion Language Models (DLMs) offer flexible token orders and parallel generation. We ask whether DLMs can acquire NTP-style reasoning through distillation without giving up their native generation process. Direct distillation, however, faces a fundamental mismatch: an autoregressive teacher predicts from a left prefix, whereas a DLM can condition on tokens on both sides. We introduce ForkLeft, a distillation framework that resolves this mismatch by separating the student's rollout from teacher supervision. During training, the student first performs entropy-first rollouts that commit uncertain positions and expose potential forks. We then fix the resulting student prefix and distill an NTP teacher under the same context, with answer correctness determining the supervision source. At inference, the student returns to its native confidence-first parallel decoding. With Qwen3-30B-A3B-Base, ForkLeft improves Efficient-DLM-4B on all ten benchmarks, raising MATH500 from 72.60% to 79.60% and consistently outperforming three alternative designs. The gains scale with teacher strength and generalize to SDAR-4B with only $500$ updates. At matched scale, the distilled 4B and 8B students exceed the published SDAR-Chat and OPDLM models on seven benchmarks, showing that DLMs can learn NTP-style reasoning without sacrificing native parallel generation. Code and datasets will be released upon acceptance.

---


### 160. [Self-Reports Do Not Identify Self-Models: An Identifiability Test for Counterfactual Reports](https://arxiv.org/abs/2609.32449)

**<font color=#1a73e8>作者：</font>** Phongsakon Mark Konrad, Toygar Tanyel, Serkan Ayvaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model self-reports are evidence about behavior in a prompt environment, not by themselves evidence of a self-model. We investigate counterfactual reports about affect-like states under activation interventions and ask whether the report remains bound to the named intervention when the demonstration environment changes. Across three open instruction models, wrong-source demonstrations move reports toward the source answer family, while explicit mechanism binding reduces this pull. Self-report benchmarks should include environment-shift invariance tests under fixed intervention before treating accuracy as evidence for an autonomous report mechanism.

---


### 161. [What Should the Reflector See? An Empirical Study of Evidence in Reflective Prompt Optimization](https://arxiv.org/abs/2609.32452)

**<font color=#1a73e8>作者：</font>** Xiaofan Zhou, Lu Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reflective prompt optimization revises instructions using examples of a model's behavior, but which evidence the reflector should receive remains unclear. We study evidence composition, visibility of examples, candidate selection and domain-knowledge policy within a single-parent Pareto-guided search. Using Qwen3.5-9B as both task model and reflector, we evaluate nine reflection strategies on five datasets. From these experiments, we find three distinct patterns. For performance improvement, Failures-only produces the largest mean test gain (+8.0 percentage points), while Balanced-mix and No-examples+Val share the best mean performance rank. For reflection effectiveness, No-examples achieves the best rank for improving sampled parents, yet yields only a 1.4-point mean test gain: local reflection success does not necessarily produce a stronger final prompt. For overfitting assessment, Failures-only and Balanced-mix share the lowest mean calibration-gap rank, while larger gaps on GPQA and IFBench show that calibration gains can overstate held-out improvement. This gap is a descriptive indicator, not a direct measure of overfitting. Together, these results show why reflection strategies should be assessed separately on final performance, parent improvement and calibration-to-test transfer.

---


### 162. [Write Back the $Δ$: Revisiting the Same Tokens with Fresh Representations](https://arxiv.org/abs/2609.32457)

**<font color=#1a73e8>作者：</font>** Wencheng Ye, Anning Hu, Xiangdong Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers process information strictly forward through depth, preventing deeper computation from revisiting and refining earlier representations. To augment the standard forward pass, existing approaches either re-execute depth, incurring additional computation, or modify the residual stream using predefined directions, limiting their instance-level adaptation. Recently, inference-time feedback offers a direct mechanism for recycling endogenously produced computation by writing deeper residual states back to earlier layers, yet what should be fed back remains unclear. We argue that the depth increment Delta, capturing newly accumulated computation between two layers, provides a more effective, composable, and scalable feedback signal than the full state. Building on this observation, we introduce ReFlux, a learnable feedback graph that dynamically selects and composes increment-carrying routes. ReFlux supports synchronous feedback to the same token and streaming feedback to subsequent tokens. Extensive experiments across various models, corpora, and benchmarks show that synchronous ReFlux consistently reduces perplexity across ten language-modeling corpora, and improves accuracy by 2.1-2.3 points, with gains reaching 4.7 points on multi-hop reasoning. Streaming ReFlux further retains most of these gains while preserving the base model's 1x theoretical backbone FLOPs. These results establish ReFlux as an efficient paradigm for unlocking the latent computational potential of LLMs, allowing them to revisit the same tokens with fresh representations. Code implementation can be found at this https URL.

---


### 163. [Streamlined Reflective Evolution for Task-Adaptive Self-Refinement Pipelines](https://arxiv.org/abs/2609.32458)

**<font color=#1a73e8>作者：</font>** Xiaofan Zhou, Lu Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reflective prompt optimization improves large language model (LLM) systems without updating model weights, but fixed architectures constrain how self-refinement is organized. We introduce Workflow-Designing Agents (WDA), a framework for streamlined reflective evolution of task-adaptive self-refinement pipelines. Starting from a minimal prompt, WDA jointly evolves stage instructions and their sequential structure. During evolution, we find that repeated revisions can accumulate redundant instructions in a single prompt. In WDA, we propose to address this problem with SPLIT, which redistributes these instructions across specialized stages. Three-example reflection and local screening guide selective search, while calibration scores guide Pareto admission and rollback of unhelpful trailing updates. The resulting pipelines are task-adaptive: their instructions and depth are learned from task data, then fixed for all test inputs within that task. We evaluate WDA on five benchmarks spanning knowledge, mathematical reasoning, multi-hop question answering, and instruction following. On Qwen3.5-9B, WDA achieves an average score of 51.24%, improving over the initial solver by 8.63 percentage points and the variant without SPLIT by 2.60 points. On GPT-4.1-mini, it achieves 49.00%, with corresponding gains of 5.62 and 3.69 points. These results support task-adaptive self-refinement as a complementary direction to broader agentic workflow search.

---


### 164. [Can Motion-Language Models Ground Structure? STRIDE for Evaluating the Evaluators](https://arxiv.org/abs/2609.32462)

**<font color=#1a73e8>作者：</font>** Lixing Tan, Qing Xia, Yuting Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion-language models are typically scored by motion-language evaluators, but how well these evaluators ground language structure remains unclear. Here, we introduce the Structure grounding via Temporal-order, Reflection, and Identity Diagnostic Evaluation (STRIDE) benchmark to systematically evaluate the ability of evaluators to track temporal order, mirror reflection, and action identity. STRIDE comprises $5{,}869$ triples, each consisting of a motion, its original caption, and a perturbed caption, spanning both short and long descriptions. We likelihood-balance caption pairs to reduce text-only bias and estimate each evaluator's caption preference under unrelated motions to measure the discrimination gain from matched motions relative to this baseline. Our experiments reveal weak structural grounding and severe deficits in mirror sensitivity among the audited evaluators, which commonly used evaluation protocols fail to expose. To understand why these limitations go undetected in standard tests, we examine the evaluators more closely. We find that text-only priors alone can solve naive perturbation tests on existing datasets, while common retrieval and distributional metrics barely respond to structural corruption introduced by mirroring ground-truth motions. These findings suggest a natural intervention: structural hard negatives. Our experiments show that a simple modification to contrastive learning substantially improves performance on temporal order and mirror reflection. The benchmark and code will be released.

---


### 165. [On the Pitfalls of Verbalized Confidence Priors for Calibrating Large Reasoning Models](https://arxiv.org/abs/2609.32470)

**<font color=#1a73e8>作者：</font>** Shuoyuan Wang, Beier Luo, Hao Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) often suffer from overconfidence when expressing their uncertainty. Confidence-aware reinforcement learning (RL) offers a promising way to optimize calibration. However, it relies on on-policy rollouts and is thus constrained by the model's pre-RL confidence distribution, which we term confidence prior. In this work, we reveal that off-the-shelf LRMs exhibit a confidence prior heavily concentrated on a few high values, which persists throughout RL. Theoretically, we prove that this concentration suppresses policy gradient updates for rarely sampled confidence values and inflates the lower bound on expected Brier risk. To overcome this exploration bottleneck, we propose CalibSFT, a plug-and-play supervised fine-tuning stage that shapes a calibrated confidence prior with broad support before RL. For each question, CalibSFT constructs confidence targets combining its success rate with response-level correctness, which provably preserves proper-scoring optimality, and then balances training responses across the confidence spectrum to enable diverse confidence exploration during RL. To learn from incorrect responses without imitating their reasoning, CalibSFT introduces correctness-conditional supervision, guiding confidence across all responses while supervising reasoning only on correct ones. Across 16 mathematical and general reasoning benchmarks, incorporating CalibSFT reduces calibration errors and improves discrimination across five representative RL algorithms while preserving comparable accuracy. Furthermore, CalibSFT delivers practical benefits for downstream selective prediction and model routing. Our code is available at this https URL.

---


### 166. [AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research](https://arxiv.org/abs/2609.32472)

**<font color=#1a73e8>作者：</font>** Kailin Jiang, Lei Liu, Jian Xi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document rerankers determine what evidence reaches the downstream model in RAG and deep research, yet mainstream rerankers select by relevance matching, and individually relevant documents rarely constitute the complete, complementary, non-redundant set a complex information need demands. Prior work rewards a set by its aggregate rubric score, shifting the objective from ranking documents to composing sets. Yet that score is one scalar shared by every document in the set, so the supervision is sparse: a redundant document is rewarded with the rest whenever the set scores well, and a decisive one penalized with the rest whenever it does not; credit assignment leaves contributors indistinguishable from free riders. On-policy distillation could densify this supervision, but existing methods give every rollout the same fixed guidance, too prescriptive for strong rollouts and too abstract for weak ones. We therefore propose AdaTutoRank, a setwise reranker trained with Adaptive Tutoring Optimization (ATO) under a three-level hierarchy of nine rubric dimensions, which supplies silver labels for the cold start, rewards for reinforcement learning, and hints for distillation. ATO draws three hint forms of increasing specificity from the policy's own frozen snapshot: the rubrics alone, a self-selector's sibling-set chosen under rubrics, and a self-reflector's reflection contrasting the rollout with that sibling-set; each rollout receives the form matched to its quality. Re-scoring that rollout under the hint-conditioned frozen teacher and the hint-free snapshot distills the hint's effect into a token-level advantage that complements the group-relative outcome advantage. Across ten benchmarks spanning RAG, deep research, and setwise evaluation, AdaTutoRank attains the best overall performance while issuing fewer retrieval calls.

---


### 167. [VPEvolve: A Self-Evolving Virtual Process Engineer for Computational Lithography](https://arxiv.org/abs/2609.32473)

**<font color=#1a73e8>作者：</font>** Tianyi Li, Wenxuan Dong, Donger Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optical proximity correction (OPC) recipes grow as engineers add local rules to repair newly discovered lithography hotspots. Each correction can interact with existing rules, while lessons from commercial-tool trials remain scattered across code and logs. \system combines a Virtual Process Engineer (VPE) harness with a Skill Bank of measured engineering experience. The harness equips a frozen language model with process manuals, layout analysis, recipe editing, and commercial-tool evaluation. The actor proposes changes to the global parameters, local targeted rules, or diagnostic trials. After each evaluation, an LLM reflector and curator turn the measured response into evidence-linked judgments. The actor retrieves them before its next trial. Feasible improvements update the retained recipe; every measured trial informs the Skill Bank that guides the next edit. The model weights remain fixed. On a FreePDK45-derived benchmark with ten commercial-tool evaluations per case, \system reduces the mean per-case maximum edge placement error from 18.294 to 5.361 nm on Poly and from 22.052 to 15.692 nm on Metal1. Every final recipe satisfies the predefined quality constraints and improves the maximum error by at least 0.1 nm.

---


### 168. [PC-SubMax: Efficient Prompt Compression via Regularized Submodular Maximization](https://arxiv.org/abs/2609.32474)

**<font color=#1a73e8>作者：</font>** Ziyi Zhang, Shuang Cui, Haotian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) are increasingly deployed in long-context scenarios, lengthy prompts can increase inference costs and latency and exacerbate the ``lost-in-the-middle'' phenomenon. Selective prompt compression offers a model-agnostic approach to alleviating these issues. However, methods based on fixed token- or sentence-level importance scores may overlook how content contributions change with the selected subset, limiting their ability to account for inter-sentence redundancy. Compression procedures that rely on autoregressive LLM scoring can also introduce substantial overhead. We propose PC-SubMax, a theoretically grounded framework that formulates selective prompt compression as regularized monotone submodular maximization under a knapsack constraint. The objective is $U(S)-\ell(S)$, where the monotone submodular utility $U$ combines information coverage, query relevance, and log-determinant diversity, and the non-negative modular penalty $\ell$ captures token cost. Through diminishing marginal returns, the objective evaluates each sentence's contribution relative to the selected content. To optimize this objective, we develop the Regularized Greedy+Max (RGM) algorithm, which deterministically returns a feasible set $Q$ satisfying $U(Q)-\ell(Q)\geq \frac{1}{2}U(O)-\ell(O)$, where $O$ is an optimal feasible solution to the regularized problem. RGM uses $O(n\kappa)$ value-oracle queries, where $n$ is the number of candidate sentences and $\kappa$ is the maximum feasible subset size. PC-SubMax uses encoder representations and avoids autoregressive LLM scoring during compression. Experiments across seven diverse benchmarks demonstrate competitive downstream performance with low compression overhead.

---


### 169. [Towards Scalable Data Diversification for Language Model Pretraining via Leverage Score Sampling](https://arxiv.org/abs/2609.32484)

**<font color=#1a73e8>作者：</font>** Zailin Ma, Quzhe Huang, Yujun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data selection for language model pretraining faces a fundamental tension between quality and diversity. While quality filtering is empirically effective, it often induces diversity collapse: by favoring texts similar to high-quality reference corpora (e.g., educational or QA-style data), it systematically excludes valuable data from underrepresented domains. In contrast, diversified selection preserves domain balance and encourages robust downstream performance, yet existing methods either focus on coverage-oriented objectives that indirectly enhance diversity, or directly optimize for diversity via costly covariance matrix recomputation that limits scalability. To address these issues, we introduce \textbf{Leverage Score Sampling (Lev)}, which iteratively selects samples that maximally expand the determinantal volume of the embedded data via leverage scores, a computationally efficient criterion that eliminates matrix recomputation and enables scalable selection. Empirically, Lev delivers up to $72\times$ speedup and improves dataset diversity, measured by the Vendi score, by $9.2\%$ over the strong diversification baseline \textbf{DiSF}. On CommonCrawl (CC) web data selection, Lev improves accuracy across seven downstream tasks by up to $1.31\%$ over existing baselines. For domains where robust quality criteria are inherently difficult to define (e.g., code), Lev serves as an effective unsupervised curation alternative: on StarCoderData, the selected subset reduces bits-per-byte by $3.08\%$ over DiSF. Notably, we uncover a cross-domain collapse of quality filtering: CC data filtered by DCLM-fastText fail to retain sufficient code-related content, yielding inferior code performance relative to Lev-selected data. These findings advocate for integrating diversity-aware practices into quality filtering for more effective data curation in language model pretraining.

---


### 170. [Elastic Selective Spectral Hybrids for Train-Once, Export-Many Budgeted Inference](https://arxiv.org/abs/2609.32486)

**<font color=#1a73e8>作者：</font>** Dachuan Song, Chuchu Chen, Xuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying a language model under different computing and latency budgets calls for compact models with different quality-cost trade-offs. Towards this end, elastic spectral state space models provide ordered and temporally decomposed channels that can be truncated, but they are associated with linear time-invariant filters that cannot selectively preserve relevant past information or forget irrelevant information as the context evolves. To address this, we introduce the Elastic Selective Spectral Hybrid (ESSH), which realizes each Hankel spectral channel as an independent recurrent unit using fitted damped rotation modes. It also features an input-dependent decay and write/read gates that make temporal retention and state update input-dependent while preserving channel-wise truncation and a structured recurrence for efficient execution. ESSH combines these selective spectral mixers with sliding-window attention and jointly trains multiple capacities by reducing spectral-channel count and feed-forward width at different rates through a two-rate capacity map with full-model distillation. The resulting models support chunked parallel training and fused recurrent decoding while avoiding computation for discarded channels. At full capacity, ESSH achieves language-modeling quality comparable to similarly sized independently trained models, while smaller exports exhibit a smooth quality-cost trade-off. We validate the effectiveness of the proposed framework using language understanding, retrieval, cross-domain text, and DNA experiments, by assessing quality retention and the trade-off against independently trained and elastic baselines. At the 1.53B model configuration, fused batch-one decoding takes 1.37 ms per token on a B300, providing a 2.14-2.80x speedup over the tested Mamba-2 and Mamba-3 implementations and 3.03x over Transformer++ at matched parameter counts.

---


### 171. [When Helpful Text Hurts: Option-Redirecting Bias in Vision-Language Models](https://arxiv.org/abs/2609.32489)

**<font color=#1a73e8>作者：</font>** Tam Le Thi Thanh, Hoang Tran Van, Hong-Hanh Nguyen-Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In tri-modal visual question answering (VQA), auxiliary text is commonly used to complement visual and textual inputs, yet its reliability is often uncontrolled. While prior work studies modality conflicts in general, it remains unclear how different types of unreliable auxiliary text affect answer selection under fixed image-question-option contexts. In this work, we show that the most harmful auxiliary text is not necessarily the most factually incorrect, but the one that aligns with the question while contradicting the image and favoring a specific distractor, leading to systematic redirection of model predictions. To isolate this effect, we introduce the Textual Reliability Ladder, a controlled diagnostic protocol that decomposes auxiliary text along three axes: image consistency, question relevance, and option support. Across multiple datasets (ScienceQA, VCR, A-OKVQA, Causal-VidQA) and recent VLMs, we find that such distractor-supporting text induces the largest accuracy drops (up to 53.1%) and concentrates errors on specific incorrect options. To mitigate this failure mode, we propose a training-free inference-time intervention that explicitly counteracts this redirection effect via noise-stability steering and dynamic grounding, reducing redirected errors while largely preserving performance under faithful text. Our results highlight that auxiliary-text reliability must be understood at the decision level, rather than solely through factual correctness, and provide a practical pathway toward more robust tri-modal reasoning.

---


### 172. [RepoMAS: Solving Progressively Specified Tasks with Issue-Driven Multi-Agent Systems](https://arxiv.org/abs/2609.32490)

**<font color=#1a73e8>作者：</font>** Yuchen Song, Andong Chen, Wenxin Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MASs) have shown strong potential for solving complex tasks, but most assume that task requirements are sufficiently specified before execution. In practice, user requests are often incomplete, and additional requirements may only become clear during reasoning, tool use, or execution. We refer to such problems as progressively specified tasks.
To systematically study this setting, we introduce ProgSpec, a benchmark that evaluates final outputs against requirements explicitly stated in the initial request and additional requirements supported by the available task evidence. We further propose RepoMAS, an issue-driven multi-agent framework inspired by open-source project management. RepoMAS records newly discovered requirements, conflicts, and failures as structured Issues and uses them to revise the task specification and execution structure during problem solving.
Across ProgSpec and five existing benchmarks, RepoMAS achieves the best performance. Further analyses show that its issue-driven revision and repository maintenance mechanisms consistently contribute to performance. These results highlight the importance of allowing MASs to revise not only how a task is solved, but also revise their explicit representation of task requirements during execution.

---


### 173. [Explaining Textual Entailment with Lexical Entailments: Using LLMs to Supply Lexical Relations for Formal Proofs](https://arxiv.org/abs/2609.32491)

**<font color=#1a73e8>作者：</font>** Jorryt de Jong, Stefan Moraca, Ettore Cesari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are highly capable of natural language reasoning and appear to store a great deal of lexical knowledge, but it is still unclear how much of this knowledge they actually use when reasoning, and whether they use it in the right way. On the other hand, logic-based Natural Language Inference (NLI) systems provide transparent and formally grounded reasoning, but they need to be supplied with rich lexical knowledge to prove inferences beyond purely logical ones. In this paper, we evaluate whether LLMs can identify all lexical knowledge needed to solve NLI problems and how much this knowledge contributes to proof search in a logic-based NLI system. Our research focuses exclusively on structured lexical entailments (e.g., chinchilla$\sqsubseteq$small animal) as a proxy for structured explanations for NLI problems with an entailment label. First, we curate a dataset for a new task of explaining sentential entailments with a set of lexical entailments. The dataset is used to intrinsically evaluate LLMs on generating structured lexical explanations. Then, we use NLI as an extrinsic evaluation in a simple neuro-symbolic setting, assessing whether LLMs can supply sufficient lexical relations to LangPro, a natural-logic theorem prover for natural language. The results show that the proposed task remains challenging even for hosted proprietary LLMs, and that their contribution to theorem proving is moderate: generated relations are often only partially sound and may be tailored to the specific NLI problem rather than representing generally valid lexical knowledge.

---


### 174. [Beyond Prompt or Skill? Attribution-Guided Optimization of Modular LLM Programs](https://arxiv.org/abs/2609.32492)

**<font color=#1a73e8>作者：</font>** Haoran Shou, Haoyue Liu, Yu Huo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can solve increasingly diverse reasoning tasks, yet their performance remains highly sensitive to task prompts, intermediate instructions, and the way reusable problem-solving knowledge is incorporated. Existing optimization methods usually focus on only one part of this design space: they either optimize a monolithic prompt, or separately induce and refine skills from model traces. As a result, they lack a principled mechanism for deciding which component should be updated when failures occur, and they rarely optimize prompts, skills, and skill-use policies in a unified framework. We propose SPARO (Skill, Prompt, And Routing Optimization), a framework that jointly optimizes task instructions, reusable skill blocks, and routing rules. It performs controlled counterfactual evaluations, converts examples' effects into a probabilistic responsibility distribution over prompt, skill, and routing components, samples one component from that distribution, and applies the corresponding targeted mutation. This design moves language-program optimization beyond global prompt rewriting toward structured, reusable, and selectively activated task knowledge. Across five benchmarks and five worker models, SPARO consistently outperforms both prompt-centered and skill-centered optimization baselines. These results suggest that effective language-program optimization depends not only on discovering useful task knowledge, but also on deciding where that knowledge should be stored and when it should be activated.

---


### 175. [SoFT: Soft Targets for Generalizable LLM Fine-Tuning](https://arxiv.org/abs/2609.32493)

**<font color=#1a73e8>作者：</font>** Huihao Jing, Wenbin Hu, Shaojin Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation enables student language models to acquire new capabilities from expert teachers. However, integrating knowledge from multi-teacher, multi-domain demonstrations into a single student remains challenging. We study supervised fine-tuning (SFT) in this setting, where students must acquire diverse capabilities while maintaining generalization beyond the training tasks. Our experiments reveal varying trade-offs between in-distribution learning and out-of-distribution generalization across SFT methods, motivating more explicit control over this balance. To this end, we propose soft-target fine-tuning (SoFT) to balance learning from teacher demonstrations with retaining the Base model's existing capabilities. SoFT sets a minimum target probability for each demonstrated token while making the smallest KL change to the Base distribution. The resulting objective couples learning from demonstrations with adaptively weighted regularization toward the Base model. We further use domain-specific gradient budgets to control this balance and determine a probability threshold for each trajectory. Experiments on mixed-domain reasoning and agentic tasks show that SoFT achieves the best overall performance among the compared methods, with improvements in both in-distribution capability acquisition and out-of-distribution generalization.

---


### 176. [DAAF: From Failure Localization to Editable System Assets in LLM Agents](https://arxiv.org/abs/2609.32498)

**<font color=#1a73e8>作者：</font>** Xiaoyang Yuan, Qi Liu, Yubin Ruan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed LLM agents increasingly rely on persistent, versioned system assets such as routing rules, knowledge segments, prompt instructions, and reusable skills. Failure-localization methods can identify where an error manifests in an agent or execution trace, but repair requires a different decision: which editable system asset should be changed, and is that change expected to improve the task outcome? We study this gap through component-attribute failure attribution, where diagnosis targets versioned, addressable items rather than execution locations. We propose the Detection-Aware Attribution Framework (DAAF), which learns the effects of valid attribute replacements and amortizes this intervention evidence into deployment-time diagnosis. DAAF combines sparse and noisy failure signals to decide whether intervention is warranted, learns component-type-conditioned replacement effects from controlled replays evaluated by executable task outcomes, and shares supervision across requests with compatible intervention responses. At diagnosis time, DAAF uses only the observed execution, registered candidates, and available failure signals; it requires neither counterfactual replay nor task reward and returns no_change, a repair target, or an unresolved decision when evidence is insufficient. On held-out tau^2-bench Telecom tasks, DAAF achieves 80.72% attribute Hit@1, recovers 62.65% of failed executions while limiting clean-task regression to 3.23%, and reaches 71.93% overall task success. These results show that intervention-grounded attribute attribution can connect failure localization to executable system repair.

---


### 177. [Learning an Anchored Prompt Space for Continual Adaptation of Large Language Models](https://arxiv.org/abs/2609.32499)

**<font color=#1a73e8>作者：</font>** Rongguang Ye, Zhan Zhuang, Yichen Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities. Jointly adapting model parameters and task-specific soft prompts offers a promising solution, but faces two key limitations: historical prompts may become less effective as the model evolves, while their transferable cross-task relationships are not explicitly learned. We propose Learning an Anchored Prompt Space (LAPS), which preserves historical prompt effectiveness and learns relationships among task-specific soft prompts to facilitate positive transfer. LAPS first aligns historical prompts with the updated model through self-distillation. LAPS then constructs an anchored prompt space whose vertices correspond to learned task-specific soft prompts and whose intermediate geometry is shaped by learnable Bézier control prompts. Once this anchored prompt space is learned, LAPS identifies the best-performing prompt for each task on its validation set, allowing the optimized prompt to draw on knowledge acquired from observed tasks. Experiments on the TRACE benchmark across three Qwen3 model scales show that LAPS consistently outperforms distillation-based, prompt-based, and joint prompt--parameter adaptation baselines, improving average performance while reducing forgetting.

---


### 178. [Learning from Others, Acting for You: Cross-User Memory Sharing for LLM Agents](https://arxiv.org/abs/2609.32511)

**<font color=#1a73e8>作者：</font>** Jinming Hu, Haodong Zhao, Qi Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents serving different users often solve related tasks, yet separate user histories can leave reusable experience inaccessible to other agents. Pooling memories expands access but risks transferring preferences that conflict with the receiving user's requirements. We introduce ShareMem, a memory architecture that shares reusable experience while grounding its application in the receiving user's own preferences. Shared experiences indicate how to act and which preferences to consult; the receiving user's memory supplies their concrete values. Two-stage consolidation refines experience locally before integrating accepted edits into a shared pool. During execution, scope-first retrieval jointly selects local and shared experiences under a common entry budget, while a user-bound channel supports initial and agent-initiated preference retrieval. We evaluate ShareMem across web navigation (Mind2Web), online personalized interaction (VitaBench~2.0), and multi-session coding (MemoryCode) with four backbone models. It improves step success, average task success, and dialogue-macro coding scores, respectively, over matched user-local memory across all four models. Ablations favor two-stage consolidation for smaller shared pools, lower induction token usage, and better downstream performance, and support complementarity between experience guidance and active preference retrieval. Further analyses show that sharing helps most when relevant local experience is scarce, while source quality and cross-user preference interference limit useful transfer.

---


### 179. [From Anomalies to Failures: Constructing Causal Error Graphs for Agentic Trace Diagnosis](https://arxiv.org/abs/2609.32514)

**<font color=#1a73e8>作者：</font>** Shu-Xun Yang, Yidong Wang, Zhuoer Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven agents are increasingly deployed in complex applications, where long agentic traces make failures difficult to diagnose. Existing trace diagnosis methods often conflate anomalies, errors, and failures, making diagnostic targets ambiguous; they also lack structured modeling of how causally relevant errors propagate and amplify into final task failures, resulting in unreliable failure attribution. To address these problems, we propose CEG-Agent, a tool-augmented agentic framework for causal diagnosis of agentic traces. Specifically, CEG-Agent introduces an explicit taxonomy of anomalies, errors, and failures, and constructs Causal Error Graphs (CEGs), a unified typed representation that links execution events, diagnostic nodes, and failure outcomes through causal relations. To evaluate causal trace diagnosis, we further construct CEG-Bench, a fully agent-annotated benchmark with high-confidence, consensus-derived CEG annotations obtained through an Adversarial Agentic Adjudication Protocol (AAAP). We validate the resulting annotations against an expert-curated human gold set, which shows close agreement with the automatic annotations. Experiments on CEG-Bench demonstrate that CEG-Agent achieves state-of-the-art performance under both semantically relaxed and structurally exact evaluation criteria. Our code is publicly available.

---


### 180. [REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers](https://arxiv.org/abs/2609.32516)

**<font color=#1a73e8>作者：</font>** Huimin Chen, Quan Long, Yanhao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security Operations Centers (SOCs) process large volumes of alerts daily. Alert triage prioritizes high-risk threats while reducing manual review of benign alerts. LLM agents can reason over logs and threat intelligence, but struggle to keep aligned with organization-specific, rapidly evolving SOC operational standards.
We introduce REFINE, an LLM-agent framework for enterprise alert triage. REFINE encodes analyst expertise as structured skills and continuously adapts using analyst disposition feedback. It enforces recall = 1.0 as a hard constraint during evolution to maximize auto-closure of false positives, and identifies judgment blind spots by combining alert distributions with model error boundaries.
Evaluated on four real industrial SOC scenarios across four MITRE ATT&CK phases with temporal split: REFINE achieves recall=1.0 on all evolution sets. On future test windows, it retains recall=1.0 in three scenarios; the degraded case reaches 0.807 recall, still outperforming self-evolution baselines (0.49-0.58).

---


### 181. [STR: Supervised Transcoder Replacement for Reducing Steering Side Effects](https://arxiv.org/abs/2609.32519)

**<font color=#1a73e8>作者：</font>** Haonan Yu, Junhao Liu, Zhenyu Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model steering can strengthen a target behavior while degrading other useful behaviors. We introduce Supervised Transcoder Replacement (STR) to reduce these side effects for existing steering methods, including those fitted without a protection objective. STR learns a replacement for the multilayer perceptron (MLP) computation at the steering layer through supervision for target control, non-target preservation, and fidelity without steering. Selected steering methods then fit directions on the frozen replacement while retaining their own fitting objectives. We evaluate three steering methods across Gemma and Llama models using Corrigibility preferences and four harmful-request safety datasets. SALAD-Bench supplies protection training data and a separate in-distribution evaluation split; HarmBench, AdvBench, and StrongREJECT are reserved for out-of-distribution testing. STR substantially reduces steering side effects on the in-distribution evaluation and extends this protection to the unseen safety datasets while retaining effective target control. For target-only supervised steering vectors, pooled out-of-distribution attack success rate falls from 42.46% to 14.42% on Gemma-3-4B and from 34.97% to 12.91% on Gemma-3-12B. These results show that replacement training can benefit steering methods fitted without protection objectives.

---


### 182. [When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM Agents](https://arxiv.org/abs/2609.32520)

**<font color=#1a73e8>作者：</font>** Yanjie Zhang, Bowen Cao, Zixin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents often operate over multi-turn interactions in which user intent changes before execution. We study intent drift: the failure mode in which superseded parts of the user's intent continue to influence the final answer or tool action. We introduce IntentFlux, an executable benchmark that converts verifiable tasks into dialogues with controlled intent changes while preserving their original graders. In a 627-case calibration, mean task score falls from 0.476 to 0.384 as dialogues contain more superseded and withdrawn information. Across eight models, the rate of fully correct solutions is significantly lower when the same final task must be recovered from an evolving dialogue rather than given directly in a single turn. We further introduce StateForge, which explicitly maintains the active requirements before generation. On General-Test, it improves mean task score from 0.367 to 0.467. Providing the ground-truth final state improves performance further but still does not recover single-turn performance, indicating that state-estimation errors explain only part of the gap. These results establish intent drift as a measurable multi-turn failure mode and explicit state maintenance as a partial mitigation.

---


### 183. [MemAgent: Learning to Manage Heterogeneous Memory Providers for LLM Agents](https://arxiv.org/abs/2609.32521)

**<font color=#1a73e8>作者：</font>** Yongxian Wei, Yilin Zhao, Runxi Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current agents remain largely stateless across tasks, limiting their ability to continually improve from prior interactions and making memory essential for long-horizon agentic behavior. Existing memory methods seek to reuse past experience, but most rely on a single memory representation (e.g., trajectories, reflections, skills, structured knowledge) whose effectiveness varies across task distributions. Rethinking this design space, we evaluate 13 memory methods and find that no single method generalizes across benchmarks, revealing the potential of managing heterogeneous memory providers. We formulate agent memory as a routing problem in which a memory agent decides which memory provider to retrieve from, whether to inject short-term memory, and which providers should store the resulting experience. Based on this perspective, we propose MemAgent, featuring a content-aware routing architecture and a training-data synthesis pipeline. The routing architecture combines content-aware probing before retrieval, short-term memory gating during execution, and selective multi-provider storage, while the training pipeline synthesizes phase-specific supervision for routing decisions. Across GAIA, WebWalkerQA, and xBench-DS, MemAgent improves average accuracy by 10.0% and outperforms every individual memory method across all three benchmarks. These gains come with less than 0.3% routing overhead and a 12% reduction in average task steps.

---


### 184. [Fail Loudly: An Auditable Runtime for Agentic Data Analysis](https://arxiv.org/abs/2609.32528)

**<font color=#1a73e8>作者：</font>** Hanxu Yan, Langxuan Deng, Zhengle Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled data-science agents to automate multi-step analyses over heterogeneous files. However, incorrect choices regarding data sources, scope, or statistical definitions often lead to silent errors: computations execute successfully but produce plausible yet incorrect outputs that fail to answer the intended question. To mitigate this, we present RADAR, an auditable runtime that makes an agent's analytical choices inspectable and supports their revision through execution feedback. RADAR operates through three core mechanisms. First, an evidence-preserving exploration module retrieves task-relevant content while retaining source locations and observation coverage. Next, the runtime uses typed operators to record the agent's declared inputs, operation arguments, and resulting observations. Finally, runtime validation checks proposed operations against these observations. When a conflict is detected, the runtime rejects the operation or provides diagnostic feedback, allowing the agent to revise its choices before errors propagate. This design enables agents to fail loudly while leaving semantic interpretation to the LLM. On KramaBench, RADAR achieves overall scores of 0.723 with full source retrieval and 0.747 with gold sources supplied, corresponding to relative gains of 35.9% and 28.8% over the strongest baselines. Beyond KramaBench, RADAR achieves relative performance gains of 14.0% on DA-Code and 59.3% on DABStep, demonstrating its applicability across diverse agentic data-analysis workflows.

---


### 185. [LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses](https://arxiv.org/abs/2609.32533)

**<font color=#1a73e8>作者：</font>** Rui Ai, Yuqing Liu, Sitao Qiu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inserting advertisements (ads) into consumer-facing LLM output is emerging as a new business model, but there is little shared evidence on how such ad insertion should be evaluated or how it affects user preferences. We introduce LLMAdBench, a human-preference benchmark for studying advertising in LLM-generated content. The benchmark isolates a simple but practically important decision: given a user conversation, an LLM response, and a matched advertisement, where should the ad be placed? Our dataset compares pairs of responses that differ only in ad position while holding all other conditions fixed including the user query, base answer, advertisement, and disclosure condition. Human annotators evaluate each pair based on six criteria from both advertiser's and user's perspectives. The resulting benchmark contains more than 18000 human judgments across two disclosure conditions: explicitly labeling the ad as sponsored and merging it into the response without disclosure. We use LLMAdBench to evaluate eight frontier LLMs as preference judges and find that they are not reliable substitutes for human evaluation. Even the most stable models reverse roughly one quarter of their decisions when the presentation order is swapped, agreement across models is low, and their placement preferences differ systematically from those of human annotators. Moreover, LLMAdBench contains substantial learnable signal. In particular, a Qwen3-8B model fine-tuned on the human preferences improves substantially over its base model and outperforms all zero-shot frontier judges on the held-out prediction task. Beyond model evaluation, LLMAdBench provides quantitative evidence on the advertiser-user trade-off and shows that the sponsorship disclosure systematically changes users' preference over ad placement.

---


### 186. [In-Flight KV Cache with Clean Anchors for Faster Autoregressive Video Diffusion](https://arxiv.org/abs/2609.32540)

**<font color=#1a73e8>作者：</font>** Yikai Wang, Xiao Han, Mengmeng Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video diffusion generates a long video by splitting the video into temporal chunks and generating chunk-by-chunk, each through a short sequence of denoising stages. To memorize chunks that are already generated, previous methods reconstruct a clean or less-noisy key--value (KV) cache by additional forwards to build the cache without advancing an output latent. However, every denoising forward itself already computes the in-flight KV of the current chunk. We introduce FlashForward, which directly reuses this cache to avoid the heavy cache-update-only model forwards. After the current chunk completes one denoising stage, its stage-specific cache is already available for the next chunk. Assigning one GPU to each stage therefore lets different chunks occupy different stages concurrently. This early availability has a quality cost: the resulting stage-matched history is noisy, causing appearance and motion drift among chunks. To complement it, FlashForward produces sparse auxiliary clean anchor latents before the corresponding region is generated so the generation trajectories can be stabilized by this two-sided conditioning. The two memories operate at different temporal scales: sparse clean anchor KV supplies coarse, long-range two-sided structural guidance, while dense stage-matched history preserves fine, recent evolution. With up to four GPUs, FlashForward runs $1.16$--$1.69\times$ faster than HiAR and $1.42$--$2.92\times$ faster than Self-Forcing for 16 FPS videos of 20 seconds or longer across 1.3B and 14B backbone scales at 480p and 720p. On VBench, for the 1.3B model at 480p, it achieves higher scores and remains stable at longer durations, demonstrating that FlashForward generates high-quality and temporally consistent videos across durations of 20s, 35s and 65s at a much faster generation speed.

---


### 187. [Porimon: An LLM-Based Pokémon Battle Agent Enhanced by Long/Short-Term Knowledge Augmented Generation](https://arxiv.org/abs/2609.32544)

**<font color=#1a73e8>作者：</font>** Dongyin Zhuo, Fengjunjie Pan, Nenad Petrovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we use Pokémon Battles as a case study to investigate how to improve the performance of LLM-based agents in tasks that require opponent-aware planning without additional fine-tuning. We propose Long/Short-Term Knowledge Augmented Generation (LSTKAG), a mechanism that enables LLM-based agents to leverage past states of the current task and retrieve experience summaries from similar previous task instances based on the current state. Based on LSTKAG, we design Porimon, an LLM-based agent structure for Pokémon Battles. For optimization, we introduce an external API for precise damage calculation and more detailed information about the game. We conduct tournament-like evaluation experiments comprising 15,000 battles for hyperparameter optimization, ablation studies, and performance evaluation. The results indicate that Porimon-based players with hyperparameter optimization significantly outperform players based on PokéLLMon, an LLM-based agent structure proposed in previous research, and the rule-based heuristic player. Furthermore, our ablation study shows that Porimon variants outperform the one without extension in game information retrieval, which shows the contribution of that extension. However, the current experiment results are inconclusive regarding the contribution of Long-Term KAG. These results suggest that introducing external resources, information from previous states of the current task, and experience summaries from similar previous task instances could elevate the performance of LLM-based agents designed for tasks requiring opponent-aware planning.

---


### 188. [Shared Autoregressive Context Can Distort Relationships in Synthetic Data](https://arxiv.org/abs/2609.32546)

**<font color=#1a73e8>作者：</font>** Thomas S. Robinson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can generate several records within one autoregressive completion, making earlier answers available as context for later records. This paper shows that such shared-completion batching can distort relationships among variables in the resulting synthetic data, using controlled tests on synthetic survey respondents. In a matched experiment on 2,000 European Social Survey profiles, generating ten rather than one respondent per request increases mean absolute error in within-country correlations by 48-58% for Qwen3.8-27B and 114-127% for Llama-3.3-70B-Instruct across three seeds, holding profiles, examples, questions and decoding parameters fixed. The distortion primarily reflects exaggerated relationship strength, while retaining substantial agreement with the human ordering of correlations. Controlled interventions establish answer history as a causal channel: re-pairing the same preceding values, with profiles and marginal distributions fixed, changes correlations among subsequently generated responses. Hiding preceding answers reduces correlation error in the tested settings but worsens marginal accuracy. Exploratory corrections across social-attitude, health and economic data likewise show that lower correlation error can coexist with worse marginal distributions and regression estimates. Request construction is therefore part of the data-generating process, and synthetic-data validity must be evaluated against the analyses the generated data are intended to support.

---


### 189. [Prioritizing Repeated LLM Evaluation for Hidden Failure Discovery](https://arxiv.org/abs/2609.32547)

**<font color=#1a73e8>作者：</font>** Keita Broadwater, Akin Broadwater  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are commonly evaluated by generating a small number of stochastic responses for each prompt in a benchmark. Because inference budgets are limited, this shallow evaluation may fail to observe low-probability but operationally important failures. A prompt that produces no failures in a small sample may therefore appear reliable despite having a nonzero latent probability of failure under repeated inference.
We formulate LLM reliability evaluation as a budget-constrained discovery problem in which each prompt is associated with an unknown per-generation failure probability. We propose a budgeted discovery framework that first performs shallow evaluation across the prompt set and then uses trial-level failure outcomes together with prompt-derived representations to learn a feature-based ranking of failure propensity. The resulting scores prioritize prompts with zero observed shallow failures for deeper evaluation, concentrating the deep-evaluation budget where hidden failures are more likely to be discovered.
We evaluate this approach on AIRBench and StrongREJECT across multiple model and system-prompt conditions. The central empirical test asks whether models fit without access to deep-evaluation outcomes can rank prompts with zero observed shallow failures according to their likelihood of producing failures under deeper evaluation. On AIRBench, the highest-ranked 10\% of unresolved prompts achieves 2.54x hidden-failure lift for Qwen 2.5 7B and 1.87x for Gemma 3n E4B, recovering 25.4\% and 18.7\% of subsequently observed hidden failures, respectively, compared with 10\% expected under random allocation. Semantic-neighborhood and feature-ablation analyses further show that this predictive signal can be recovered from multiple representations of prompt content and relationships.

---


### 190. [Are Vision-Language-Action Models Robust to One-Step Observation Perturbations?](https://arxiv.org/abs/2609.32550)

**<font color=#1a73e8>作者：</font>** Shojiro Yamabe, Jun Sakuma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding the safety risks of vision-language-action (VLA) models is essential for their deployment in the physical world. Existing safety research has mainly considered persistent perturbations that are applied continuously to observations throughout an episode. However, momentary observation corruption, in which observations are severely perturbed only briefly within an episode, remains an underexplored safety threat. To address this gap, this work investigates robustness to one-step perturbations applied at a single time step per episode. Our experiments reveal that these perturbations substantially degrade VLA performance and that their impact depends on the action chunk execution length. Based on them, we propose CARE, which dynamically selects the execution length based on consistency with the previously predicted action chunk. CARE improves robustness with low computational overhead while preserving clean performance by selecting shorter execution lengths only under perturbations.

---


### 191. [Harnessing Coupled Stream Completion For Human-Object Ineraction Modeling](https://arxiv.org/abs/2609.32551)

**<font color=#1a73e8>作者：</font>** Dawei Guan, Di Yang, Jiangtao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned human-object interaction (HOI) generation requires body motion, object trajectories & rotations, and hand articulation to remain coordinated. These components differ in scale and dynamics, but must agree on contact, relative pose, and timing. A shared representation may limit the distinct structure of each stream, while independent generation prevents each stream from responding to changes in the others. Latent supervision alone also does not directly constrain contact after decoding. We propose TRACE, a continuous latent framework that keeps stream states separate and couples their updates. TRACE encodes body, object, and hand motion into separate latents and predicts each stream velocity from the complete current interaction state. Geometric losses on decoded motion further constrain contact and object-relative motion over time. The same model supports completion of any single absent stream from the other two. Frozen flow features also serve as input to a language model for HOI understanding. Experiments on InterAct, OMOMO, and BEHAVE show that joint completion training improves generation and that frozen flow features improve understanding over raw-motion encoding. On InterAct, TRACE achieves the highest contact precision, recall, and F1 among the compared methods.

---


### 192. [Artificial intelligences and human scientists exhibit complementary strengths in theory building](https://arxiv.org/abs/2609.32562)

**<font color=#1a73e8>作者：</font>** Ke Li, Spyros I. Zoumpoulis, Phanish Puranam 等 83 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate the effectiveness of artificial intelligences (AI)-specifically large language models (LLMs)-relative to human scientists at high-level cognitive tasks in social science such as theory formulation, predictions of novel empirical results, and theory revision in response to new evidence. The research domain was academic discourse regarding gender and race inequality. Our findings, comparing 25 LLMs with 13 senior researchers and 60 doctoral scholars, reveal that the AIs outperformed most humans individually on most of the present tasks, while human theories were more diverse and exhibited greater gains in predictive accuracy from aggregation. AI-generated theories were more extensively elaborated, involving additional theoretical paths and latent variables, and were rated as higher quality than human theories by independent raters blinded to source. However, this theoretical complexity was in part ornamental, in that it was not associated with more accurate predictions about empirical patterns in data; in contrast, human scientists achieved greater predictive efficiency with simpler theories. The AIs were significantly more likely than human scientists to revise their theories to incorporate new evidence; human scientists updated their beliefs in a selective way that is sensitive to prior prediction errors. We speculate that the superior processing capacity of artificial intelligences makes them especially well-suited to tasks requiring grappling with complexity, but that the greater diversity of human ideas is essential to wise crowds and collective creativity.

---


### 193. [ProTTT: Learning to Learn Semantic User Memory with Test-Time Training](https://arxiv.org/abs/2609.32564)

**<font color=#1a73e8>作者：</font>** Sejun Park, Hyoungjo Bhang, Hyein Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalization requires language models to capture user-specific knowledge from a growing user history. Existing context-based approaches incur increasing inference costs as user history accumulates and rely on separate retrieval or summarization stages, while parametric-based approaches often require reconstructing user representations when new user data is added. We introduce ProTTT, a profile-supervised meta-learning framework for learning semantic user memory. The memory construction starts from a shared initialization and is updated for each user through test-time training on user history, allowing it to evolve continuously as the history grows. However, since test-time training alone does not explicitly encourage the memory to capture semantic user knowledge necessary for personalization, we learn this shared initialization using textual user profiles as supervision, so that test-time training on user history captures semantic knowledge more effectively. ProTTT consistently outperforms both full history ICL and all parametric baselines across diverse benchmarks, while substantially reducing inference cost by compressing user history into a lightweight parameterized memory. Our analysis also shows that profile supervision is a reliable objective for learning semantic user knowledge and that the resulting memory can track and retain evolving user preferences, while remaining robust across different history sizes. Overall, we demonstrate the effectiveness of test-time training for personalization and establish ProTTT as a baseline for continuously evolving user memory.

---


### 194. [Reading Is Not Leaking: Local, Auditable Measurement and Reduction of Inference Exposure from Public Footprints](https://arxiv.org/abs/2609.32565)

**<font color=#1a73e8>作者：</font>** Mahmudul Faisal Al Ameen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anyone with a public footprint leaks facts that were never stated, and language models make the inference cheap. We present a framework for measuring and reducing this inference exposure that runs on the owner's own CPU with no language model at analysis time, instantiated on organisations and on individuals. It starts from a measurement result: scoring an inference system against the target's private truth conflates how well the system reads the record with how much the record leaks. On a 128-question instrument over sixteen synthetic firms, almost half of the questions are never answered correctly by any of six readers, four of them language models, and a majority-class guess accounts for most of every reader's score. We therefore separate reading accuracy from leakage rate and introduce an injection protocol that creates cells with known support. Our analyser combines rules, statistical solvers and a 106M-parameter encoder trained from scratch that marks verbatim evidence and never generates text; every answer carries a graded certificate whose recorded proof replays. Its certified answers are correct in 93% of resolved cases, against 49-73% for the language models' quote-backed answers, whose citations are produced alongside the answer rather than deriving it; with plain-prose articles in the record, 70% of its evidence-bearing answers rest on evidence that establishes them, against 18-56% for the models. A constrained defence that rewrites each fact's carrier as a true but coarser statement hides every single-carrier fact from four language-model adversaries at 40% lower edit cost than deletion. On sixteen synthetic people the guessing term is larger still, and a decoy planner with no language model halves the correct answers of the estimator it targets without transferring to a second.

---


### 195. [Attribution Gaps in Zero-Training LLM+OVOD Pipelines: A Fine-Grained Analysis of the CAAP--SNAP Discrepancy](https://arxiv.org/abs/2609.32567)

**<font color=#1a73e8>作者：</font>** Yu-Feng Yen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LAOD and similar zero-training LLM+open-vocabulary-detector (OVOD) pipelines score two things separately: class-agnostic localization accuracy (CAAP) and semantic naming accuracy (SNAP). The two consistently diverge, and nobody has asked why. This paper asks why, on the full 5,000-image COCO-Val split (27,273 detections) rather than the small subset the original work evaluated on. Object visual complexity turns out not to be the driver -- small and occluded objects are, if anything, localized better than large ones. Vocabulary novelty is: once the LLM's wording falls outside the detector's native category set, localization accuracy falls from 80.9% to 31.6%. That drop is not spread evenly across unfamiliar phrasing, though. Almost all of it comes from cases where the novel wording actually names a different object than the one COCO annotated (true synonyms still score 89.3%; semantically unrelated "noise" labels score 12.0%). A closer look at a further failure subset tells a similar story: 78-88% of what looks like complete localization failure is really the model correctly finding a real object that COCO's non-exhaustive 80-category scheme simply never labeled, not hallucination. Swap the detector backbone (YOLO-World for Grounding DINO) or the LLM (Gemma-3 for Qwen2.5-VL) and both the effect and its rough size hold up, so this looks like a general property of the pipeline family rather than a quirk of one model pairing. The upshot is that a large share of the apparent CAAP--SNAP gap traces back to closed-category annotation limits rather than a real grounding failure, which matters for how we detect hallucination, analyze failure modes, and design evaluation for grounded multimodal systems meant to work in the open world.

---


### 196. [OmniSmartHome: A Multimodal Reasoning Benchmark for Smart-Home Agents](https://arxiv.org/abs/2609.32569)

**<font color=#1a73e8>作者：</font>** Jihoo Jung, Suho Yoo, Jeongsoo Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smart-home assistants are expected to handle diverse, realistic requests that arise in daily life. In such interactions, users often rely on the surrounding multimodal context-pointing at objects or referring to what they see or hear, leaving their requests underspecified in language alone. Existing smart-home benchmarks, however, express user requests solely through language, leaving context-dependent real-world requests underexplored. To bridge this gap, we introduce OmniSmartHome, a multimodal smart-home benchmark where each spoken request is paired with the surrounding visual and spatial-audio context, providing complementary cues to disambiguate underspecified requests. OmniSmartHome comprises 1,360 synthetic and 272 real-world episodes. We evaluate 16 omnimodal large language models (Omni-LLMs) and reveal that, while they perform strongly when speech alone sufficiently conveys the user's intent, performance drops substantially when resolving it requires reasoning over multimodal contextual cues. As a simple agent baseline, we provide PROME (PROcedural Memory for multimodal Evidence gathering), which equips agents with specialized audio-visual perception tools and procedural memory for orchestrating their use. PROME generally improves performance across six Omni-LLMs. Demos and examples are available at this https URL

---


### 197. [CAESAR: Clustering via Autonomous Embedding-Space Agglomerative Reorganization](https://arxiv.org/abs/2609.32570)

**<font color=#1a73e8>作者：</font>** Ilan Bacry, Rémi Devaux, Antoine Jardin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering algorithms that operate on nearest-neighbor graphs, such as FINCH (First Integer Neighbor Clustering Hierarchy), depend heavily on the quality of the embedding space they are given. However, pretrained vision and language model embeddings are not optimized for this purpose. We propose CAESAR, a method that reorganizes a pretrained embedding space: a reorganization network is trained to pull mutual nearest neighbors together and push non-neighbors apart, yielding a reorganized embedding space substantially better suited to clustering. CAESAR offers a second major advantage: it never requires the number of clusters $K$. This matters because in realistic unsupervised settings, $K$ is typically unknown and discovering it is often part of the problem, yet most strong clustering methods take it as an input. We therefore design the entire CAESAR pipeline to infer $K$ rather than assume it is known. Empirically, reorganizing the embeddings consistently improves clustering over the raw space on both text and image datasets. Since the few deep clustering methods that also infer $K$ do not release their code, we complement controlled comparisons with methods that infer $K$ on the same embedding space by comparisons with strong deep clustering methods that are given the true $K$, giving them a substantial oracle advantage. Even so, CAESAR outperforms all of them on text, achieves the best results on the most challenging image benchmark and remains competitive on the others. Reorganizing pretrained embeddings thus emerges as a simple and powerful route to clustering realistic data, where classes overlap and the number of clusters is unknown.

---


### 198. [Trapped by Their Own Rollouts: Understanding Aggregation--Rollout Feedback in Federated On-Policy Distillation](https://arxiv.org/abs/2609.32573)

**<font color=#1a73e8>作者：</font>** Jinqian Chen, Jihua Zhu, Chang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is a promising approach to language-model adaptation, aligning teacher supervision with the student's own generated trajectories. When adaptation prompts are distributed across clients, can this process benefit from federated collaboration? We study federated OPD and find that substantial collaboration gains can be obscured by learning-rate sensitivity: FedAvg can perform no better than independent local training at a small learning rate, yet recover a clear advantage at a larger rate. We explain this phenomenon through the student's dual role as learner and generator of future training data. An aggregation-induced optimization lag can delay access to useful teacher supervision, which in turn slows subsequent learning. Our theory establishes this aggregation--rollout feedback in a solvable model with a common optimum and stable updates, and identifies two coupled roles of learning rate: learning from current supervision and reaching future supervision. Guided by this analysis, we propose FedTOPS (Federated Teacher-guided On-Policy Scaling), which reuses teacher feedback on current trajectories to adapt the FedAvg update magnitude under clientwise predictive-change constraints. Across six mathematical reasoning benchmarks, FedTOPS improves macro Avg@8 over FedAvg by 4.56--14.57 percentage points across the evaluated student models and local learning rates.

---


### 199. [DimPO: Dimensionality Reduction for Attention using Preference Optimization](https://arxiv.org/abs/2609.32579)

**<font color=#1a73e8>作者：</font>** Vojtěch Lanz, Yufei Cui, Prasanna Parthasarathi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A linear projection can reduce the dimension of query and key vectors without updating the pretrained model, but it remains unclear which training objective best preserves model behavior. We ask whether preferences over keys and attention mass on the highest-weighted keys provide a better signal than matching the full attention distribution with KL divergence, especially in long-context settings. We introduce DimPO, which combines listwise preference optimization with a lightweight top-k cross-entropy term for head-fidelity. DimPO is trained offline from the attention patterns of a frozen language model, with one map per layer, shared by the query and the keys and trained separately from the other layers. Across LLaMA3.2-3B, LLaMA3.1-8B, Qwen2.5-7B, and Qwen3-4B Instruct models, pairwise preference objectives outperform the triplet baseline and retain 98% of the original score on short-context tasks when projecting to half the dimension on the last 40% of the layers. With more projected layers or on long-context RULER, they degrade rapidly. In contrast, KL and DimPO, which use every key during training, retain about 95% of the original RULER 4k score on the 8B model when projecting up to 50% of the layers. KL-based projections remain closer to the original attention distribution and attention output, yet DimPO achieves better downstream performance. Beyond 50% of projected layers, DimPO increasingly outperforms KL on tasks including SQuAD, common-word extraction, frequent-word extraction, and variable tracking. These results suggest that under dimensionality reduction, preserving the ordering and concentration of task-relevant attention can matter more than reproducing the full attention distribution.

---


### 200. [HERO-MoE: Historical Expert Routing with Scale-Preserving Fusion](https://arxiv.org/abs/2609.32581)

**<font color=#1a73e8>作者：</font>** Junxiang Qiu, Zhengsu Chen, Xinting Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have become a standard way to scale model capacity while keeping computation sparse, yet routing remains a key determinant of MoE quality and training behavior. Prior empirical studies suggest that MoE routing reflects input semantics and upstream computation across depth, but standard routers do not explicitly use the routing distributions produced by preceding layers. We propose HERO-MoE, Historical Expert ROuting with Scale-Preserving Fusion, a routing framework that injects historical routing priors into MoE routers by reusing detached, dense routing distributions collected from preceding MoE layers. The key idea is simple: HERO-MoE preserves the original token-conditioned routing branch and adds a residual historical routing contribution before the standard softmax and top-$k$ dispatch. To stabilize this historical signal, HERO-MoE introduces a scale-preserving fusion mechanism that matches the magnitude of historical routing memory to the current hidden representation and accounts for the number of visible historical layers, without introducing an auxiliary routing loss or a fusion-specific tuning parameter. By reusing routing distributions already computed by preceding MoE layers, HERO-MoE improves training-loss reduction with modest end-to-end overhead. The resulting router remains compatible with standard sparse dispatch, including top-$k$ and group-limited routing, and can be inserted into existing MoE backbones with minimal architectural changes. Experiments on an approximately 8B-parameter MoE model with 0.5B active parameters, trained from scratch on 100B tokens, show that HERO-MoE reduces the final loss from 1.6393 to 1.6184, while peak memory and FLOPs increase by only 0.44\% and 0.64\%, respectively.

---


> [!TIP]
> 当前位于：**151-200**（第 4/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
