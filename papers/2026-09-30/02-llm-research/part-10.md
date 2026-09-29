# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-500**（第 10/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 451. [Seeing and Solving Are Not Enough for Vision-Language Models](https://arxiv.org/abs/2609.33694)

**<font color=#1a73e8>作者：</font>** Ziheng Wang, Mingxuan Xie, Yilin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) answer visual questions by combining visual information extraction with downstream problem solving. We investigate a fundamental question: Does an incorrect answer necessarily reflect a failure in visual extraction or problem solving? A model may succeed at both abilities when tested separately yet still fail on the original multimodal question, a distinction that overall answer accuracy cannot reveal. To study this, we perform a question-level empirical analysis across multiple VLMs and visual domains. We define an exactly scorable task state (i.e., the visual information sufficient to solve a question) and use it to test whether the same model can extract the required state, solve the question from the ground-truth state, and answer the original multimodal question. We find that composition failures, where extraction and solving both succeed but direct answering fails, account for 17.7% to 75.6% of direct-answering errors across multiple VLMs and datasets. To address this failure mode, we introduce a simple yet effective method, termed State Realization Tuning (SRT). SRT fine-tunes LoRA adapters attached to the language-model layers while keeping the pretrained VLM weights frozen. It trains the model to output the ground-truth task state before the final answer in a single autoregressive response. SRT improves over standard supervised fine-tuning by 1.7 to 14.1 percentage points and repairs 92.5% to 98.1% of diagnosed composition failures. A single LoRA adapter trained with SRT also improves performance across substantially different task-state structures. Our work shows that having both visual extraction and problem-solving capabilities does not guarantee correct multimodal answering. Requiring the model to first output the visual information needed to solve the question can help bridge this gap.

---


### 452. [One Latent, Many Tokens: Jointly Learning Compressed Embeddings for Efficient Language Diffusion](https://arxiv.org/abs/2609.33698)

**<font color=#1a73e8>作者：</font>** Yulin Yuan, Ying Zhang, Xiangming Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most continuous diffusion language models process one latent position per token at each sampling step, making generation expensive. Two-stage methods lower the cost by reducing the latent length, but they fix the compressed embedding space before training the diffusion model. Embeddings from the fixed space can be difficult to model with diffusion and decode reliably into tokens, which limits generation quality after compression. To address this problem, we introduce JPEG-DLM (Joint-embedding Prediction for Efficient Generation with Diffusion Language Model), which jointly trains a compressor, a flow matching model and a decoding module. With joint-embedding prediction, JPEG-DLM learns compressed embeddings that are more structured, easier to model with diffusion and reliably decodable into tokens. JPEG-DLM achieves the lowest mean Gen-PPL and highest throughput among recent diffusion and flow models on LM1B and OWT. At a compression rate of 0.5 on OWT, it reaches a Gen-PPL of 34.52 and approximately 2.3 times ELF's throughput. These results suggest that jointly learning compressed embeddings offers a promising path toward efficient diffusion language modeling. Code will be released soon.

---


### 453. [SpecRead: A Benchmark for Measuring Whether Language Models Understand Hardware Specifications](https://arxiv.org/abs/2609.33699)

**<font color=#1a73e8>作者：</font>** Feilian Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for large language models (LLMs) in hardware design evaluate downstream artifacts such as generated RTL, assertions, or testbenches. When a model fails such a benchmark, the failure is ambiguous: it may have misread the specification, or it may have understood the specification and failed to write the code. We present SpecRead, a benchmark that isolates specification comprehension from generation ability. SpecRead v2.1 contains 385 questions over 10 open-source OpenTitan IP blocks: exact retrieval, cross-section reasoning, contradiction detection in mutated specifications, and spec-RTL consistency checking, plus 82 controls (41 distractor, 41 consistent-RTL). Type-4 items are built from real RTL mutations; we retain only mutations that Icarus Verilog simulation shows to change observable behavior. A with-spec vs. without-spec ablation suggests the questions require the excerpt, not training recall alone (without-spec accuracy 3/20 on the t1/t2 subset), though memorization of the source text may still help spot mutations. As an initial characterization with a small model, Ministral-3B scores 33.2% overall (128/385; macro average 39.0%): 55.2% on retrieval, 51.7% on cross-section reasoning. On the two contradiction-focused types, the verdict-plus-location measure gives 48.0% (t3) and 63.3% (t4), with a 51.2% false-positive rate on distractors and 100% on consistent-RTL controls. Layered scoring shows the model locates contradictions well (78.9-81.6% location accuracy) but scores lower on their category (43.9-49.7%). A structured "rule-table" prompting intervention lowers accuracy on every question type except t2 (tied). SpecRead is automatically scorable by deterministic checks, with gray-zone cases counted wrong under the conservative main scoring. The benchmark is regenerable for type-3 items via mutation injection, and built exclusively from public sources.

---


### 454. [Prompt-Anchored Residual Adaptation for Biomedical Vision-Language Models](https://arxiv.org/abs/2609.33701)

**<font color=#1a73e8>作者：</font>** Jingxuan Kang, Qianying Yue, Che Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained biomedical vision-language models achieve strong zero-shot performance in biomedical image classification. However, downstream biomedical classification often depends on subtle visual differences between classes that may not be fully captured by pretrained representations. Few-shot adaptation addresses this mismatch by optimizing a task-specific predictor on a small labeled support set. Because the selected examples capture only part of the visual variation within the target classes, the adapted predictions can depend strongly on their composition. We propose Prompt-Anchored Residual Adaptation (PARA), which retains the frozen prompt prediction as a support-invariant semantic anchor and incorporates a visual prediction learned from the support set through an anchor-relative residual. The residual step is computed in a closed form from frozen support embeddings using anchor discrepancy and support agreement. Support-set dependence also limits evaluation: comparisons are fair within a shared draw but remain conditional on its composition. To obtain more reliable comparisons, we introduce a repeated-support protocol that separates support-selection variation from optimization randomness and reports both average and worst-20% performance. PARA achieves state-of-the-art performance in both few-shot classification and base-to-novel generalization.

---


### 455. [Understanding Confabulation and Rethinking Reconstruction in Activation Explanations](https://arxiv.org/abs/2609.33702)

**<font color=#1a73e8>作者：</font>** Gert Lek, Zixuan Xia, Pin-Yu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Autoencoders (NLAs) produce unsupervised text explanations of a model's activations: a verbalizer describes an activation and a reconstructor learns to recover it from this text. Under the established point-reconstruction NLA training recipe, explanations become more useful for predicting model behavior while also increasingly introducing unsupported details and exhibiting writing defects. To assess these changes separately, we introduce a standardized evaluation framework for unstructured NLA explanations, measuring information recoverable from explanations, contextual support for their claims, and writing quality. To address confabulation and writing defects, we move beyond predicting a single activation: explanations can distinguish distributions of possible activations even when their means and optimal point-reconstruction rewards are identical. We introduce Flow-NLA, which models the distribution of activations compatible with an explanation and trains the verbalizer using a diffusion likelihood bound. Across Qwen, Gemma, and Apertus, this richer signal retains the utility gains of point reconstruction while curbing the growth of confabulation and writing defects, opening up a direction for improving activation-derived training to encourage more informative, supported, and readable explanations. Code and evaluation prompts will be made publicly available upon acceptance.

---


### 456. [Does Adversarial Training Improve Generalization in Multi-View VLAs? Revealing and Mitigating View Collapse](https://arxiv.org/abs/2609.33707)

**<font color=#1a73e8>作者：</font>** Futa Waseda, Shuhei Kurita, Isao Echizen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models adapt pretrained vision-language models (VLMs) for closed-loop robot control, transferring their perceptual and semantic capabilities to action prediction. Despite strong in-distribution performance, however, VLAs often degrade under deployment shifts. Adversarial training (AT) offers a model-adaptive approach to robustness without explicitly anticipating individual shifts, but its effect on natural distribution-shift generalization in multi-view VLAs remains unclear. We study this question using a multi-view VLA directly adapted from a pretrained VLM and evaluate generalization across seven LIBERO-Plus shift axes. Direct AT substantially improves Camera Viewpoint and Sensor Noise, the two shifts affecting only the third-person view, yet produces mixed or negative effects on other shifts. Controlled view interventions reveal a surprising failure mode that we term view collapse: Direct AT can shift cross-view reliance so strongly that the policy becomes dominated by the wrist view. This exposes a \textit{robustness shortcut}: apparent robustness to a shifted view can arise from reduced use of that view rather than more robust perception of it. This motivates a distinction between robust perception, extracting reliable information under within-view shifts, and robust fusion, adapting reliance across views according to their reliability. To reduce fixed view reliance, we use a simple View Swap intervention and then re-evaluate AT. With View Swap, AT further improves Camera Viewpoint, Sensor Noise, and Robot Initial State, while its effects remain mixed on other shifts. Our results show that multi-view robustness requires separating improved perception from changes in cross-view reliance, and that AT provides selective rather than generic distribution-shift benefits.

---


### 457. [DuoOPD: Learning from Joint Teacher-Student Outcomes for Multi-Task On-Policy Distillation](https://arxiv.org/abs/2609.33711)

**<font color=#1a73e8>作者：</font>** Ao Yu, Weibo Gao, Heng Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own responses with token-level feedback from a stronger teacher, yet the teacher can fail on questions the student already answers correctly, and how often each model succeeds varies across tasks. OPD ignores these outcomes and, on average, pushes down even the student's correct responses; gating feedback by student correctness fixes the direction but uses the teacher in the same way whether or not it succeeded. We introduce DuoOPD, in which the student's outcome sets the direction of feedback and the joint teacher-student outcome decides how the teacher supports it: when only the teacher succeeds, its verified answer becomes context for scoring the student's failed response, and when only the student succeeds, a weight shared within the task reinforces the whole response. A single rule covers all four outcome combinations without task-specific settings. Across Qwen3 and Llama, DuoOPD outperforms all five baselines in mean macro accuracy, improving over OPD by 2.58 and 5.98 percentage points, and it also leads on two further task mixtures spanning scientific calculation, instruction following, and code generation. Ablations show that outcome-based direction alone stays near the gated baseline, while the joint-outcome designs supply most of the gain.

---


### 458. [BIRD: Distilling Decision Boundaries into Rationales for MLLM Adaptation](https://arxiv.org/abs/2609.33713)

**<font color=#1a73e8>作者：</font>** Anglin Liu, Yanlin Wu, Ruichao Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting general-purpose multimodal large language models (MLLMs) to specialized domains requires learning domain-specific decision criteria, which often hinge on subtle visual distinctions between otherwise plausible answers. Rationale augmentation aims to expose such evidence through additional observations or inter-sample comparisons, yet a visually valid cue is not necessarily decision-relevant: it may describe how samples differ without changing the model's relative preference between competing answers. We therefore introduce BIRD, a self-improving Boundary-Informed Rationale Distillation framework that uses model-specific confusions to locate unresolved local decision boundaries and distills the evidence that resolves these confusions into rationales. For each sample, BIRD retrieves candidate neighbors from the target MLLM's own representation space and selects the most confusable one according to its answer preferences. It then generates answer-blind candidate evidence from their visual differences and functionally verifies which evidence most effectively strengthens the model's preference for the correct answer while avoiding inappropriate transfer across the pair. The verified evidence is then distilled into a single-sample rationale for standard supervised fine-tuning. Experiments on medical and chart VQA show that BIRD outperforms competing rationale-augmentation methods across two target MLLMs, while further analyses demonstrate clearer separation of confusable answers and stronger gains from model-matched supervision.

---


### 459. [Self-Designed Evaluators and Warm Memory for Long-Horizon Agents](https://arxiv.org/abs/2609.33717)

**<font color=#1a73e8>作者：</font>** Saeid Asgari, Emre Kiciman, Leonardo de Oliveira Nunes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A tool-using language-model agent deployed over a long stream of tasks receives no reward, so it cannot tell whether it succeeded, cannot safely retry, and cannot label the experience it needs to improve. We present SelfSuite, in which the agent's own base model, given only the world's public materials, designs a small evaluation suite of weighted judges and grounded per-task briefs, freezes it, and uses it to gate a keep-best retry and to label a typed, outcome-tracked memory. On matched five-repeat benchmarks over tau2-bench and AppWorld, SelfSuite scores above the plain agent without any labels, matches methods given ten expert labels on tau2-bench, and trails Agentic Context Engineering (ACE) on AppWorld, where code execution gives a direct success signal. In an ablation campaign run on the same tasks, it is above label-free ACE in every repeat, and the gated second attempt is the only component whose removal hurts in every repeat. We also simulate a subject-matter expert who grades ten onboarding tasks per world. Using those labels to calibrate SelfSuite's evaluator gives a small, consistent gain, and using them to warm up ACE's memory lifts ACE to tie calibrated SelfSuite. A single-run study on a second model family shows the same ordering.

---


### 460. [From Granular Revision Operations to Meaningful Revision Units: Evaluating LLMs for Revision Boundary Detection](https://arxiv.org/abs/2609.33720)

**<font color=#1a73e8>作者：</font>** Yu Tian, Andrew Potter, Katerina Christhilf 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Revision traces provide valuable evidence about students' writing processes, but their usefulness for learning analytics depends on how individual revisions are represented. Automated draft-comparison methods often produce granular edit operations that can fragment a single purposeful revision into multiple analytic units. This study evaluates whether LLMs can identify meaningful revision unit boundaries in structured revision operation data and whether they provide value beyond simple non-LLM baselines. Using 113 matched draft--revision pairs from undergraduate writing, expert annotation yielded 4,344 candidate boundaries. We compared zero- and few-shot GPT-5.5 and base Qwen3-32B, parameter-efficient fine-tuning of Qwen3-32B, and majority and proximity-based baselines. Despite receiving revision context and task instructions, no prompted LLM condition outperformed the proximity heuristic (macro-F1 = .825). In contrast, fine-tuned Qwen3-32B using the two context representation achieved the highest macro-F1 (.859), identifying more same-unit relationships while maintaining precision comparable to the heuristic. Deterministic post-processing substantially improved the prompted models but added little benefit to the strongest fine-tuned model. These findings suggest that LLMs can support revision boundary judgment when task-adapted, but general purpose prompting alone may not outperform transparent structural heuristics.

---


### 461. [Shared Experience, Separate Learning: Companion Confidence Calibration for LLMs](https://arxiv.org/abs/2609.33721)

**<font color=#1a73e8>作者：</font>** Shiyu Ni, Keping Bi, Jiafeng Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable self-assessment is essential for large language models (LLMs), yet they often remain highly confident when their answers are wrong. We study \emph{concurrent confidence calibration}, where confidence is learned alongside capability improvement rather than calibrated only after training. Reinforcement learning from verifiable rewards (RLVR) provides a natural setting for this paradigm, as it continuously produces responses paired with verifiable correctness feedback. Existing concurrent methods, however, learn both capability and confidence through reinforcement learning within shared policy parameters, potentially coupling two fundamentally different learning problems. We instead propose \emph{shared experience but separate learning}: capability and confidence learn from the same trajectories, but through separate optimization mechanisms and parameters. Based on this principle, we introduce \textbf{CoCal (Companion Confidence Calibration)}, which trains a lightweight companion from rollout hidden states and verifier-derived correctness supervision while leaving task optimization unchanged. Experiments on Qwen3-8B and Qwen3-14B show that CoCal improves confidence estimation without sacrificing task performance, outperforming both RL-based concurrent methods and matched post-hoc calibration. The learned companion further generalizes across domains and policy shifts, while the benefits of CoCal persist at both scales.

---


### 462. [BOReFT: Manifold Steering of Language Models for Black-box Optimization](https://arxiv.org/abs/2609.33722)

**<font color=#1a73e8>作者：</font>** Dhruv Agarwal, Rico Angell, Kavitha Srinivas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used as proposal models for black-box search, from program optimization to molecular design. Existing approaches typically improve proposals through iterative prompting or parameter updates, offering limited control over how completely and efficiently the model's search space is explored. Continuous optimization methods, such as Bayesian optimization, provide a principled way to search but require a suitable domain to operate over. To address this, we introduce BOReFT, which learns a compact, low-dimensional space of hidden-state interventions in a frozen language model, and uses this space as the search domain for Bayesian optimization with an external scoring function. Empirically, we find that the learned domain spans semantic regions and exhibits smoothness properties that support search. Theoretically, we show that semantic coverage and interpolation control the best score available in the learned space, and that decoding from this space yields a standard stochastic-bandit observation model for adaptive search. We evaluate BOReFT on the interpretable word search task "Semantle" and on three more real-world discovery tasks in de novo molecule property optimization. Compared to strong LLM baselines, BOReFT finds in Semantle a higher number of hidden targets and, on two out of three molecular objectives, achieves higher property scores. Consequently, our method provides a principled new bridge between discrete proposal spaces of LLM-based search and continuous black-box optimization.

---


### 463. [HTN Planning as a Coordination Layer for Multi-Server MCP Tool Orchestration](https://arxiv.org/abs/2609.33731)

**<font color=#1a73e8>作者：</font>** Eliott Jacopin, Éric Jacopin, Koichi Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) isolates servers by design: only the host can orchestrate cross-server workflows. When the host is a large language model, the resulting orchestrations are non-deterministic, non-reproducible, and pay one inference round-trip per tool call. We present a coordination architecture in which a Hierarchical Task Network (HTN) planner generates a verifiable cross-server plan once, and a runtime middleware executes it deterministically across multiple MCP servers, binding cross-action data dependencies via a template mechanism (\verb|${context.X}|) substituted at execution time. The architecture mirrors MCP's isolation constraint: each compound task decomposes into server-local primitive actions, and inter-server data flow is bound at execution time via JSON-path output extractors. We instantiate the architecture on five HTN domains spanning laboratory robotics, bioinformatics and multiscale modelling, and demonstrate end-to-end execution from a browser-based plan controller against eight live third-party MCP servers querying real biological databases.

---


### 464. [The Effects of Incremental Instruction Delivery on Language-Model Creative Writing](https://arxiv.org/abs/2609.33738)

**<font color=#1a73e8>作者：</font>** Anshuman Singh, Abrar Eyasir, Haseeb Yaqoob 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as interactive writing tools, where users develop stories, revise ideas, and introduce new requirements across multiple turns rather than specifying a complete brief upfront. Yet most evidence on multi-turn instruction degradation comes from tasks with objectively verifiable outcomes, leaving unclear whether incremental interaction harms creative artifacts in ways that explicit requirement checks cannot capture. We study this question using 160 human-authored creative-writing tasks across six genres, presenting each intended specification either upfront or progressively over 5-9 turns to six distinct open-weight model families, yielding 960 matched pairs. Progressive delivery reduces explicit constraint adherence and produces its largest writing-quality degradation in structure/coherence. The structural gap persists among outputs with equal observed adherence, suggesting that measured requirement loss alone does not explain the observed structural difference. We define Creative Integrity as a compact measure of joint adherence and narrative structure; under incremental delivery, models retain 71.2% of FULL Creative Integrity (95% CI [68.2%, 74.3%]). A three-rater human study over 50 matched pairs independently recovers FULL advantages in structure/coherence, craft, and genre effectiveness, while automated scores remain positively associated with aggregated human ratings. These findings show that interactive creative-writing systems should be evaluated not only on whether requirements survive conversation, but also on whether evolving requirements remain coherently integrated into the final artifact. Our dataset, benchmarks, and source code are available at: this https URL

---


### 465. [Accounting for Stochasticity in Studies of Large Language Model Refusal](https://arxiv.org/abs/2609.33743)

**<font color=#1a73e8>作者：</font>** Emma Lurie, Stephanie T. Wang, Sorelle A. Friedler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present preliminary empirical evidence that single-observation queries are insufficient for evaluations of LLM refusal behaviors. Using a longitudinal auditing system, we issued identical prompts 100 times each across four dates to GPT-4.1 for two socially salient topics across 20 Wikipedia sources. Refusal outcomes were consistent with a stable Bernoulli process, yet 20\% of sources fell within a decision-boundary region where a single query is largely uninformative. Reliable quantification of refusals required between 15 and 25 repeated queries, well above the single-observation standard common in existing evaluations.

---


### 466. [PQ-HSA: Reusing Product-Quantized Scores for Hybrid Sparse-Approximate Attention](https://arxiv.org/abs/2609.33746)

**<font color=#1a73e8>作者：</font>** Kunming Shao, Jierun Chen, Yanli Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> At each decoding step a language model attends over the key-value (KV) cache of every earlier token, so at long context the attention call is bounded by memory bandwidth. Sparse attention reads only a subset of keys chosen by a cheap score estimate, and most methods give the unread tokens zero weight. The output then draws on only a small fraction of the KV cache, and accuracy drops at small budgets, most on tasks that aggregate information across the context. An inverted-file product-quantization (IVF-PQ) index over the cached keys computes an approximate score for every indexed token in order to rank them; after ranking, those scores approximate the attention logits of the tokens left out. PQ-HSA (hybrid sparse-approximate attention) attends the selected tokens with their original keys and values, and the unselected tokens, the background, enter the same softmax through those scores, summed per inverted list and multiplied by the list's mean value. At 128K and a 1-2% retrieval budget, PQ-HSA is more accurate than Quest and SnapKV on Llama-3.1-8B and Qwen3-30B-A3B and stays close to full attention in macro accuracy; with the same selector, the background term raises macro accuracy on the 8B model from 0.71 to 0.83. In the same 128K setting, inside vLLM on one NVIDIA H20, the decode attention call runs 1.6x faster than the FlashAttention-3 kernel; the speedup grows with context length, and a cost model fitted on 8B to 30B models gives the context length at which it begins. A vLLM plugin runs PQ-HSA on two engine versions without changes to the engine source; code is available at this https URL.

---


### 467. [Positions Are Not Facts: The Mismatch Between KV Caches and Memory](https://arxiv.org/abs/2609.33759)

**<font color=#1a73e8>作者：</font>** Changhai Zhou, Yuhua Zhou, Shiyang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a fact changes, how should a language model update the history stored in its key-value (KV) cache? Hiding the old record is cheap, but it may still contain needed details or answer questions about the past. We compare hiding whole records, hiding only replaced values, and deleting old text and recomputing the cache. In a controlled quantity task, masking makes all eight models prefer the new value more strongly, yet six lose complete answers through unit errors or failure to stop; keeping the unit preserves all current answers. Later states also retain useful information from earlier records: on multi-hop updates, rebuilding these states at unchanged positions lowers historical accuracy by 20-41 percentage points, whereas moving the existing states has little effect. Keeping object dependencies and unchanged revision passages prevents many losses. Recognition is a separate challenge. Learned readouts recover distinctions missed by fixed cache similarities on synthetic record pairs. On natural text, text-detector-selected masks show no clear advantage over random masks at the same rate in 14 same-model detector-generator comparisons. Query-dependent access can avoid some losses, with additional storage or access costs. These findings identify what must be preserved beyond the replaced value when using a KV cache as updatable memory.

---


### 468. [SecProbe: Adaptive Evaluation of Coding Agents on Cybersecurity Vulnerabilities](https://arxiv.org/abs/2609.33763)

**<font color=#1a73e8>作者：</font>** Xiaonan Luo, Yue Huang, Kehan Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Assessing cybersecurity vulnerability awareness in coding agents requires evaluations that reveal capability gaps and remain informative as models evolve. Static benchmarks offer fixed coverage and difficulty, while scarce vulnerable repositories and costly expert authoring limit their renewal at scale. We introduce SecProbe, a framework for adaptive evaluation that combines Item Response Theory (IRT) with on-demand synthesis of repository-scale vulnerability-repair tasks. From observed performance, \textsc{SecProbe} estimates agent ability and identifies where additional evidence is most informative, selecting existing tasks or synthesizing new ones accordingly. As one use case, we construct 353 tasks spanning six programming languages and 151 CWE types and evaluate nine frontier models with two agent harnesses. Success rates peak at 28.33\%, highlighting substantial gaps in vulnerability recognition and repair. Compared with random and one-shot baselines, \textsc{SecProbe} achieves comparable agent ability estimates while requiring agents to solve up to 29.5\% fewer tasks. These results support adaptive evaluation as an efficient and discriminative approach to assessing cybersecurity vulnerability awareness.

---


### 469. [DEALS: Decentralized Expertise-Aware Load Serving for Multi-Agent LLM Systems](https://arxiv.org/abs/2609.33768)

**<font color=#1a73e8>作者：</font>** Jingjuan Huang, Wenbin Wang, Yanchuan Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) have recently emerged as an effective approach for coordinating large language model (LLM)-based agents to solve complex tasks through structured interactions. In practice, MASs often handle a stream of heterogeneous and complex tasks, requiring agents to decompose each task and then self-organize and self-evolve to adapt to incoming tasks while sharing execution resources. However, most early approaches to MASs rely on centralized controllers or fixed coordination patterns, which can limit scalability or adaptability. In contrast, existing decentralized and dynamic MASs often require training dedicated routers or invoking LLMs for agent selection, resulting in substantial computational costs and coordination overhead. To address these challenges and enable efficient task-level self-organization and self-evolution for task- and workload-level collaboration, we propose Decentralized Expertise-Aware Load Serving (DEALS), a decentralized and low-complexity framework that enables agents to self-organize and dynamically route concurrent tasks for processing. Specifically, each agent maintains local queues of incoming tasks, and its router decides whether to process a task locally or forward it to a neighbor based on differences in backlog and success rate. Meanwhile, executors process independent tasks concurrently within and across agents, and partially solved tasks can be resumed by other agents. Experiments show that DEALS not only improves performance along multiple dimensions (e.g., answer accuracy and task throughput) in both homogeneous and heterogeneous agent pools, but also balances agent expertise and workload in a self-organized manner, enabling effective decentralized coordination.

---


### 470. [Learning Strategies to Break Judges](https://arxiv.org/abs/2609.33773)

**<font color=#1a73e8>作者：</font>** Guruprerana Shabadi, Aaditya Naik, Rajeev Alur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents surpass human performance, it becomes exceedingly hard for system designers to evaluate them directly and understand their failure modes. Consequently, agents themselves are being deployed extensively to evaluate, judge, and provide feedback on model traces. But this raises an important question: how can we trust the judge? In this work, we propose an agent-guided method to find weaknesses of agentic judges that expose interpretable failure mechanisms. Our method focuses on mathematical reasoning and proceeds in two stages: first, we deploy adversarial agents to mutate a set of sound proofs by introducing errors, attempting to misguide judges---in other words, injecting errors that judges are unable to catch. Then, we distill these attempts into a small set of mutation strategies which allow us to analyze the failure modes of the judges. To ensure that these strategies are not overfit to the initial set of proofs, we evaluate them by applying the mutation strategies to a held-out set of proofs and querying the same judge. We deploy our method on GPT-5.6-sol and Claude Opus 5, paired with their agent orchestrators, Codex and Claude Code, respectively. These are used both as mutators to introduce errors and as judges to evaluate correctness of mathematical reasoning. We find that across all the agentic judges, we are able to distill mutation strategies that consistently bypass their evaluations, thereby enabling us to ascertain actionable failure modes. Our analysis also reveals that judge reliability degrades at the frontier: errors in Olympiad-level proofs or graduate-level mathematical texts are detected more consistently, whereas flaws in research-level manuscripts are more likely to escape detection.

---


### 471. [Evidence-Inference Reconstruction: When The Evidence Is Recalled But The Reasoning Goes Wrong](https://arxiv.org/abs/2609.33778)

**<font color=#1a73e8>作者：</font>** Megan Diehl, Ser-Nam Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern multi-hop LLM agents are equipped with built-in mechanisms to detect errors in intermediate reasoning steps. Such errors trigger corrective actions from these agents, which mostly follow the paradigm of retrying the steps or the reasoning trajectories. Not only are these retries expensive, we present in this paper that they are also potentially unnecessary. To this end, we introduce Evidence-Inference Reconstruction (EIR), which uses structured state to guide one retrieval trajectory, accumulating source evidence in the process. We show that as long as the relevant evidence has been collected, EIR is capable of generating the correct answer in a single final model call even if erroneous evidence has been mixed in due to incorrect intermediate reasoning steps. In one evaluation, using Haiku 4.5 and GPT-4.1 Mini, we evaluate EIR on matched 1,000-question subsets of HotpotQA, 2WikiMultiHopQA, and MuSiQue, showing that EIR improves Answer F1, the overlap between the model's and the correct answer, over the baseline by 8.3--32.8 points, Agentic SSR by 10.6--29.1 points, and Reflexion by 1.1--15.9 points. Additionally, we show that EIR averages 4.85 total model calls per question, compared with 35.29 for Agentic SSR and 12.41 for Reflexion. Together, these results corroborate EIR's central premise: separating evidence retrieval from the final answer model call can improve answer accuracy while utilizing substantially less computation.

---


### 472. [Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for Exploration in LLM Reasoning](https://arxiv.org/abs/2609.33781)

**<font color=#1a73e8>作者：</font>** Woongyeong Yeo, Minki Kang, Chanuk Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) enhances reasoning in large language models (LLMs) through outcome-level feedback, yet recent approaches to finer-grained credit assignment often require auxiliary models, additional sampling, or privileged information. Although policy entropy provides a readily available signal, prioritizing uncertain positions under both reinforcement and penalization concentrates penalties where failed responses still retain alternatives for recovery, which can suppress opportunities for exploration. To address this, we introduce Entropic Advantage Policy Optimization (EAPO), an entropy-guided credit assignment method that treats success and failure asymmetrically. Specifically, motivated by the observation that success under uncertainty is less repeatable while confident failures tend to recur, EAPO couples normalized policy entropy with the sign of the response advantage to reinforce surprising success and correct repeated failure. It assigns stronger reinforcement to high-entropy decisions in successful responses and stronger penalties to low-entropy decisions in failed responses, while attenuating penalties at uncertain positions to preserve opportunities for recovery. By redistributing the response advantage across tokens, EAPO derives token-level credit directly from existing rollout signals without additional supervision. We validate EAPO on a range of reasoning tasks across both base and reasoning backbones, demonstrating that it achieves the best overall performance. We further show that EAPO promotes more effective exploration, broadening problem coverage and generating more diverse candidate answers.

---


### 473. [LA-CPD: Local-Evidence-Aware Change-Point Detection for Human-LLM Authorship Segmentation](https://arxiv.org/abs/2609.33787)

**<font color=#1a73e8>作者：</font>** Qing Yang, Zhenyu Mao, Zixiang Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM-generated text becomes increasingly human-like, accurately localizing LLM-authored spans in human-LLM co-authored documents is important for attribution and accountability in cases involving copyright infringement, fraud, and other harmful uses of AI-generated content. Sentence-level detectors provide local authorship evidence, but content variation can cause score fluctuations even among sentences from the same source, creating spurious boundaries. Recovering a coherent document partition therefore remains challenging when both the number and locations of authorship transitions are unknown. We propose Local-Evidence-Aware Change-Point Detection (LA-CPD), a structured method that transforms noisy sentence-level score sequences into coherent authorship segments. Given scores from a frozen local detector, LA-CPD combines a length-weighted within-segment residual with a windowed two-mean contrast to capture segment consistency and sustained changes around candidate cut points. Dynamic programming optimizes cut locations for each candidate count, while an AIC-style criterion selects the final partition, yielding sentence labels, authorship boundaries, and maximal LLM-authored spans. On a held-out human-LLM co-authored test set, LA-CPD outperforms WCP+AIC, increasing sentence-level accuracy from 0.747 to 0.796 while improving boundary localization and LLM-span delineation.

---


### 474. [Do We Really Need KL Divergence for On-Policy Distillation of Large Language Models?](https://arxiv.org/abs/2609.33791)

**<font color=#1a73e8>作者：</font>** Wenze Lin, Jiyuan Long, Jiale Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since the advent of knowledge distillation, KL divergence has been the standard loss in distillation. Recently, on-policy distillation (OPD) has emerged as an efficient post-training paradigm for LLMs. As a distillation method, OPD naturally inherits KL divergence as its standard loss. However, in this work, we find that KL divergence may not be necessary for OPD. We show that simply preserving the update direction is sufficient for effective OPD. As long as the update direction is toward the teacher, OPD works. More precisely, it is not the direction of every token, but the direction of a small subset of tokens where the teacher and student disagree strongly. We first show that simply assigning a reward of (+1) to tokens where the teacher probability is higher than the student probability and (-1) where it is lower, which merely encourages updates toward the teacher, reproduces almost the same training mode as OPD with reverse KL. We further show that only the direction of a small subset of tokens with large teacher-student disagreement is critical, and training works as long as their update direction is toward the teacher, even if other tokens are pulled away from the teacher. And as an application of these findings, we introduce Consensus Multi-Teacher On-Policy Distillation (C-MOPD) to improve Multi-Teacher On-Policy Distillation (MOPD). Unlike MOPD, which routes each sample to a single teacher and may cause capability conflicts across domains, C-MOPD lets every sample be supervised by all teachers. Experiments show that C-MOPD consistently outperforms MOPD on both math and code benchmarks. Our code is available at this https URL.

---


### 475. [Diffusion Reward Models](https://arxiv.org/abs/2609.33803)

**<font color=#1a73e8>作者：</font>** Xiangyang Wang, Bingxiang He, Zeyuan Liu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models underpin the alignment of large language models, yet the dominant designs reduce each prompt--response pair to a point estimate or to a distribution from a fixed parametric family. This is at odds with human preference, which is inherently multimodal: the same response can be reasonably judged in many ways, and no single family covers all of them. To better fit this structure, we introduce DRM, a Diffusion Reward Model that recasts reward modeling as conditional density estimation over $p(\mathbf{r}\mid x,y)$. Conditioned on a frozen LLM encoder, a lightweight Diffusion Transformer denoises Gaussian noise into a reward vector, placing no parametric assumption on the output distribution and naturally representing its multimodal structure. A single architecture handles both multi-attribute regression and pairwise preference data, and at inference $N$ samples form an empirical reward distribution that can be aggregated into a scalar, a variance, or quantiles. Across five benchmarks, DRM matches or surpasses baselines under matched data and backbone, stays competitive with much larger discriminative, distributional, and generative RMs despite its modest training scale, and recovers multimodal reward structure where conventional heads collapse to a point. Uncertainty-aware rejection and lower-confidence-bound (LCB) aggregation further demonstrate that DRM can exploit distributional information beyond a scalar reward to improve reward-model decisions. Downstream RLHF experiments additionally show that using DRM as the training-time reward leads to improved policy performance, directly validating the practical benefit of diffusion-based reward modeling for RLHF training.

---


### 476. [Dual-Vocabulary Language Model for Cross-Tokenizer Distillation](https://arxiv.org/abs/2609.33816)

**<font color=#1a73e8>作者：</font>** Kedi Chen, Chen Lin, Yutao Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) bridges teacher supervision and student behavior, but different teacher-student tokenizers introduce misalignment in both input tokenization (#1) and output logits (#2). Existing approaches address the former by matching same-text spans or converting tokens to bytes, often losing fine-grained token information or disrupting the native-token paradigm, while for the latter, strategies such as ranking, padding, or key-token selection retain only shared logit dimensions, resulting in much distribution loss. In this paper, we propose Dual-Vocabulary Language Model (DVLM), which replaces the teacher's LM head with a new student-vocabulary projection head and obtains full-dimensional student logits (for #2). To support student tokens (for #1), it takes a Parallel-Tokenized Sequence (PTS) as input, which concatenates the original teacher-tokenized sequence and a re-tokenized sequence formed by independently converting each student token into a teacher-token group. To avoid inference inconsistency with the original teacher tokens, the Hybrid-Prefix Attention (HPA) further restricts re-tokenized groups to their corresponding teacher prefix and uses its last state as the aggregation of the original student-token representation for projection into the student vocabulary space. Similarly, via the combined use of PTS and HPA, the DVLM teacher can provide distribution-aligned supervision with the student's input-tokenization and output-logit during OPD. Experimental results demonstrate that our DVLM teacher has a similar converged loss as the original teacher model and enables student models to improve performance across six reasoning tasks.

---


### 477. [Augmenting Visual Anomaly Detection with Automated Interpretability](https://arxiv.org/abs/2609.33818)

**<font color=#1a73e8>作者：</font>** Antonio De Santis, Arsenio Leo, Marco Brambilla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual anomaly detectors identify deviations from known-normal data, but their anomaly signals may mix evidence of actual anomalies with benign visual variation. We investigate whether automated interpretability can augment visual anomaly detectors by identifying and intervening on different components of this signal. We decompose PatchCore nearest-normal residuals into sparse features using Sparse Autoencoders (SAEs), and provide high-activation and contrastive non-active examples to a Multimodal LLM, which describes each feature and labels it as anomaly, distractor, or uncertain. These labels guide interventions in the SAE hidden representation, where distractor features are suppressed and anomaly features amplified. The edited representation is then used to reconstruct patch embeddings, which are rescored with PatchCore. Across 40 categories from four benchmarks, applying both interventions jointly improves macro-average image-level AUROC from 0.8724 to 0.8857 on source data and from 0.8066 to 0.8210 under synthetic corruptions. On three additional RobustAD categories with real acquisition shifts, the same interventions improve AUROC from 0.8745 to 0.9056 on source data and from 0.6069 to 0.6599 under real acquisition shifts. Finally, individual feature interventions across all 43 categories show that the MLLM labels are aligned in aggregate with how features differently affect normal and anomalous images.

---


### 478. [Vestrum: Improving Agent Harnesses by Adapting Their Verification, Structure and Memory](https://arxiv.org/abs/2609.33822)

**<font color=#1a73e8>作者：</font>** Jayant Parashar, Eugene F. Douglass, William C. Bastian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent harness controls how a language model accesses information, uses tools, preserves memory, and checks its work. Improving this software is costly when each evaluation requires a long interaction with an environment. We introduce Vestrum, a framework that turns failures in execution traces into scoped harness changes without training the task model. Its organizing overhypothesis is that tasks of a shared kind may exhibit recurring failures whose remedies transfer within that kind. Vestrum expresses failures as recognizable classes, proposes changes across verification, retrieval, decomposition, and knowledge synthesis, and screens their scope before evaluating them as a bundle. A persistent lessons file informs subsequent proposals. Across five settings and two baseline harnesses, the frozen harnesses improve held-out performance: UltraHorizon rises from 47.6 to 59.8 over GAM, Terminal-Bench 4 Hard from 63.7% to 70.3% of checks passed over Claude Code on eight held-out tasks at 1.03x test cost, and cell-type annotation agreement from 67.5% to 77.8% on held-out sections of one slide, alongside gains on LoCoMo and AMA-Bench. Across our searches, verification grounded in evidence helped both intermediate steps and final answers, at lower cost at intermediate steps, while critics asked to rebuild finished answers broke more than they repaired. On the three memory benchmarks, Vestrum also scores above the evaluated GEPA configurations in every paired evaluation.

---


### 479. [One Attack to Fool Them All: Highly Transferable Black-Box Adversarial Attacks on Frontier MLLMs](https://arxiv.org/abs/2609.33833)

**<font color=#1a73e8>作者：</font>** Sen Nie, Jie Zhang, Zhongqi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks have long posed a fundamental threat to machine learning systems. As multimodal large language models (MLLMs) rapidly evolve and become widely deployed, assessing their vulnerability to such attacks is essential for their safe use. In this work, we investigate whether a single adversarial image can consistently mislead diverse frontier MLLMs in black-box settings. We propose O-Attack, a highly transferable black-box attack framework. This framework builds on our insight that surrogate models contain a broad, high-level, cross-modally aligned semantic space. This space extends beyond final-layer outputs and provides multiple semantically consistent representations that remain underexploited by existing attacks. Within this space, O-Attack anchors aligned representations, progressively broadens semantic conditions, and optimizes perturbations through semantic consensus to promote consistent target alignment. By fully exploiting this space with the same surrogate models as M-Attack, O-Attack raises attack success rates on GPT-5.4 (29.1% to 77.2%), Claude-4.6 (42.8% to 81.6%), and Gemini-3.1 (38.2% to 80.9%). Extensive experiments across 24 MLLMs show that O-Attack outperforms six state-of-the-art methods in black-box transferability, with consistent effectiveness across prompts and improved efficiency and imperceptibility. This work exposes the practical safety risks posed by black-box adversarial attacks against frontier MLLMs, underscoring the need for more rigorous robustness evaluation and more effective defenses.

---


### 480. [ChemOPD: Multi-Teacher On-Policy Distillation for Multi-Task Chemical Reasoning](https://arxiv.org/abs/2609.33838)

**<font color=#1a73e8>作者：</font>** Yaoyao Xu, Xinjian Zhao, Xiaozhuang Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly expected to support diverse chemical reasoning capabilities within a unified model. One approach is to develop specialized capabilities separately and consolidate them through multi-teacher on-policy distillation, but this raises two questions: how should specialization be organized, and how should specialist guidance be integrated? We introduce ChemOPD, which addresses both. We estimate task affinities from supervised fine-tuning gradients and solve a constrained mixed-integer program(MIP) to construct partially overlapping specialist groups. During distillation, we retain a generalist teacher trained on all tasks so that specialist guidance supplements rather than replaces its supervision. Our anchor-residual objective gradually increases the routed specialist's contribution on student-generated responses. On ChemCoTBench, affinity-guided specialization produces task-dependent gains over the generalist teacher and improves several capabilities beyond semantic task grouping. Yet stronger teacher-side performance does not automatically yield stronger students: with the same specialists and routes, anchor-residual OPD improves most reported metrics over specialist-only distillation and realizes a larger share of the available teacher gains. These results highlight specialization and capability integration as connected but distinct design problems in chemical reasoning.

---


### 481. [How code helps different tasks? A decompositional lens on LLM post-training](https://arxiv.org/abs/2609.33845)

**<font color=#1a73e8>作者：</font>** Zheng Yu, Yiwei Li, Yishen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating code data as a single corpus can obscure which types of code data benefit which models and downstream tasks. Effective data selection requires understanding both the benefits of individual categories and whether these benefits persist when categories are combined. We introduce a decompositional lens for studying these effects in LLM post-training. We first decompose an execution-verified code corpus into interpretable categories based on the computational patterns of its solutions. Through controlled fine-tuning experiments, we compare individual categories with a balanced mixture across instruction-tuned models on question answering, mathematics, and code generation. The resulting response maps reveal recurring gains in average question-answering performance, while the same category can improve one model or task and degrade another. The best-performing category also varies with the starting model and target task. We then compose compact mixtures guided by these results and examine whether benefits observed in individual categories persist under joint training. On selected model--task pairs, mixtures whose constituents each improve the target task outperform both their best constituent and full-corpus training while using roughly 10--15\% of the full corpus. These exploratory findings illustrate a \emph{less is more} pattern and highlight how the value of code data in post training depends on which categories are combined for which model and task.

---


### 482. [QwenGyre: An Elastic Reinforcement Learning Framework for Training xLong-Horizon Agents](https://arxiv.org/abs/2609.33848)

**<font color=#1a73e8>作者：</font>** Weiqi Wang, Yuxin Zhou, Mouxiang Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly undertake extreme-long (xlong) horizon tasks, where a single execution can span hours, hundreds of model--environment interactions, and nearly 1M tokens per rollout. Applying online reinforcement learning (RL) to such executions poses two fundamental challenges: (1) severe execution variance and prolonged rollout delays cause massive GPU idling; and (2) complex non-linear branching generates massive trajectory redundancy, crippling training efficiency. To address these, we presents QwenGyre, an end-to-end framework for xlong-horizon online RL. QwenGyre elastically reallocates GPUs between rollout and training without interrupting live executions, while its trajectory processor reconstructs branching histories, scores partial progress, and deduplicates redundant paths to bound training costs. Scaled to our flagship model, Qwen~3.8 2.4T, with 700K tokens per rollout, QwenGyre yields a 6.0% absolute gain on NL2RepoBench (52.5% $\to$ 58.5%) in 48 steps. Across our evaluations on diverse domains of training datasets, QwenGyre delivers up to $1.85\times$ and $1.78\times$ speedups over Colocate and Async, respectively.

---


### 483. [Program-Verified Self-Evolution for Vision-Language Models](https://arxiv.org/abs/2609.33855)

**<font color=#1a73e8>作者：</font>** Ahmed Heakl, Sungik Choi, Moontae Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-evolving vision-language models train on questions they generate from unlabeled images. Since these questions have no gold answers, prior methods label them by majority vote over sampled answers or by a model judge. In a human evaluation, we find that 24\% of majority-vote labels and 18\% of model-judge labels produced during self-evolution are wrong. To address this problem, we present Verifiable QA Generation for Self-Evolving Models (VQS), which changes how the model judges answers. Instead of voting on an answer, the model parses each image into a structured record, such as a scene graph, a chart table, or a diagram graph. Fixed programs then write a question from the record and compute its answer. The model still acts as a visual checker, but it only confirms the individual facts the program reads, one short claim at a time. These claim-level checks select the parser's training targets, so the parser also improves without labels. Human raters find 94\% of VQS answers correct, against 76\% for majority voting. Across ten benchmarks, VQS improves Qwen3-VL by up to 3.18 points at the 2B, 4B, and 8B scales and outperforms the strongest self-evolving baseline at each. Gains keep growing over three training rounds, reaching 3.84 points at 2B. Code is released at this https URL

---


### 484. [In-Context Adaptation of Encoder-Decoder Models in Speech Recognition](https://arxiv.org/abs/2609.33865)

**<font color=#1a73e8>作者：</font>** Yen Meng, Sharon Goldwater, Hao Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning offers an appealing approach to adapt automatic speech recognition (ASR) models to new speakers, accents, and domains by providing speech-text pairs as demonstrations at inference time. Recent work shows that some LLM-based speech models are capable of ASR in-context adaptation, when providing interleaved speech-text demonstrations. In this work, we ask whether in-context adaptation is an inherent ability for all encoder-decoder models. We study two forms of demonstration, collated and interleaved demonstration, across six encoder-decoder models, spanning conventional cross-attention-based and LLM-based architectures. We find that all tested models are able to perform in-context adaptation out of the box, achieving up to 30% relative improvement in the oracle experiments and up to 23% using first-pass hypotheses. Through controlled experiments on three English datasets, we show that lexical and speaker information both contribute to successful adaptation. While interleaved demonstration is effective in certain cases, collated demonstration brings consistent adaptation across the board. Our results suggest that in-context adaptation for ASR is not unique to specific architectures, training, or demonstration approaches.

---


### 485. [R$^2$ Flow: Recursive Self-Improvement via Recursive Skill Evolution](https://arxiv.org/abs/2609.33867)

**<font color=#1a73e8>作者：</font>** Mingda Zhang, Qiang Huang, Yanjin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents can improve themselves across tasks by reusing and revising the skills they orchestrate into executable procedures. Flow-based training fits this loop: it samples procedures in proportion to reward, and the flow through each skill credits it for the next library revision. Three obstacles stand in the way of making this self-improvement reliable: flow training suffers strategy collapse over tree-structured histories; nonnegative flow-based credit rewards frequent use as if it were benefit; and library edits rest on the task reward the policy optimizes. We introduce R$^2$ Flow, a recursive self-improvement framework that alternates policy learning, independent verification, and versioned skill-library updates on a shared-state orchestration graph. The graph merges histories that differ only in the order of independent steps, allowing flow training to pool evidence across equivalent executions. A flow-share readout of the trained flow, invariant to the backward policy, and a separate signed utility rank which skills to change, verifier evidence decides whether an edit is warranted, and a residual-variance plateau sets when to update. Committed edits reshape the graph the next policy learns on, realizing recursive skill evolution. Across question answering, mathematical reasoning, interactive decision making, and code generation, R$^2$ Flow improves task accuracy and library-edit precision over heuristic orchestration, reinforcement learning, and skill-evolution baselines, and transfers across executors. Code is available at this https URL.

---


### 486. [When Successful Strategies Fail: Adaptation to Environmental Novelty in Terminal Agents](https://arxiv.org/abs/2609.33870)

**<font color=#1a73e8>作者：</font>** Janvijay Singh, Vaishnavi Shrivastava, Dilek Hakkani-Tur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly solve long-horizon tasks by autonomously interacting with their environment. In doing so, their strategies rely on assumptions about that environment: which resources and tools exist, where they are located, and how they behave. When these assumptions no longer hold, reliable agents must detect the change and adapt while pursuing the same goal. We study this adaptation capability through environmental novelty: a change that keeps the task objective fixed while invalidating an assumption underlying an otherwise successful trajectory. We introduce AGNI, an automated pipeline that extracts trajectory-relevant assumptions, injects targeted environmental changes, and validates that the resulting novel tasks remain solvable. Across three terminal benchmarks, AGNI produces diverse novelties spanning resources, interfaces, constraints, and execution semantics. Evaluating multiple LLM agents reveals a substantial adaptation gap between base and novel tasks. Trajectory analysis suggests that agents often encounter evidence of the change but fail to diagnose its cause and revise their strategy. Finally, post-training for environmental novelty improves adaptation to held-out novel tasks while also improving performance on base tasks. Our results highlight a gap between task competence and adaptive capability and motivate environmental variation as a core dimension of agent training and evaluation.

---


### 487. [Population Physics, Population Problems: Safety and Emergence in LLM Societies](https://arxiv.org/abs/2609.33871)

**<font color=#1a73e8>作者：</font>** Adrian de Wynter  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The collective behaviour of large language model (LLM) societies is not the sum of their individual outputs. It yields statistically distinct, sometimes-unpredictable phenomena, for which the tools we use to study single agents may not scale. Due to recent incidents involving autonomous agentic systems, however, understanding these systems is paramount. For that we introduce a framework for measuring self-organisation in LLM social systems and apply it to three such systems: a Schelling grid, a social network (Moltbook), and a Twitter-like misinformation simulation ('Rogue'). All three exhibit statistically significant self-organisation. Moreover, their relaxation dynamics vary with the environmental information available to the agents, with open-ended systems (Moltbook, Rogue) exhibiting sharp, phase-transition-like dynamics. Further results show that population-level pathologies can emerge even when the LLMs are safety-tuned or monitored, being primarily driven by the coordinated activity of a population subset. We also show when self-organisation does \textit{not} emerge under two additional scenarios (a commons dilemma, GovSim, and a LLM-as-a-judge deliberation scheme, ChatEval). We argue that measuring signatures of this kind offers a lightweight, agent-agnostic diagnostic layer for detecting coordinated collective behaviour in deployed multi-agent systems without relying on natural language or model versioning.

---


### 488. [JET: Justification Evaluation in Transformer](https://arxiv.org/abs/2609.33874)

**<font color=#1a73e8>作者：</font>** Shenghao Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> JET uses pretrained language and vision-language models to select among a finite set of answers without additional training. It evaluates candidate likelihoods directly and shares computation across candidates. Experiments on desktop CPUs and consumer GPUs assess decision accuracy and execution cost. Qwen3.6-35B-A3B achieves 87.48% accuracy on the full MMLU test set and 3.69 requests per second on a separately timed MMLU subset. The accuracy-throughput comparison covers model, hardware, and reasoning choices, with Jev as an external reference. Controlled execution experiments show 2.18-2.23-fold speedups from prefix reuse and cache management, and a 30.8% reduction in process time from input preparation optimizations, with unchanged outputs. Optional reasoning has a task-dependent accuracy-throughput trade-off. These results support local decision inference from existing models.

---


### 489. [Curating Merchant-Matching Training Data with Two Confidence-Gated Local LLM Judges](https://arxiv.org/abs/2609.33878)

**<font color=#1a73e8>作者：</font>** Donghao Huang, Jinling Pei, Zhaoxia Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Merchant matching resolves a noisy payment descriptor to a retrieved merchant entity or returns no match. A key challenge in curating training labels is distinguishing teacher abstention from evidence that no acceptable entity exists: false no-match labels contaminate pseudo-labeled data, while conservative labeling reduces coverage. We investigate whether agreement between two local large language model judges improves pseudo-label reliability. A label is retained only when the judges agree, with separate ordered thresholds for selections and abstentions that guarantee disjoint positive and negative label sets. Retrospective replay on 2,000 expert-annotated queries shows that higher selection thresholds can improve positive-label purity, whereas higher abstention thresholds increase false no-match labels. At thresholds (0.86, 0.80), Muse Glimmer 30B and Gemma 4 31B jointly label 1,633 queries (81.7% coverage) at 96.88% purity; positive and negative purities are 99.47% and 93.38%. This exceeds either constituent model at the same thresholds by more than two percentage points, with lower coverage. A split-half check finds only 0.14 percentage points of threshold-selection optimism. A symmetric threshold of 0.86 adds 40 erroneous no-match labels, while 46 false abstentions persist even with no confidence threshold. Across five matched within-model comparisons, higher reasoning effort yields no clear F0.5 gain and increases median latency by 1.8-5.0 times. These results motivate separate thresholding and auditing for positive and negative pseudo-labels. The study establishes label purity, not student utility; fresh-data curation and student fine-tuning remain necessary to demonstrate downstream value.

---


### 490. [Lost with a Map: Conversational State and Behavioral Reliability in Language Models](https://arxiv.org/abs/2609.33883)

**<font color=#1a73e8>作者：</font>** Atahan Dokme, Larry Heck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented dialogue requires maintaining and updating information across turns, yet language models expose no explicit belief-state object. We study how conversational state is represented, updated, and used inside eight instruction-tuned language models from four families on MultiWOZ and SGD. Structure and values separate: which domains, slots, and requests are active is linearly readable just before the model acts, whereas exact values are far more readable where the user stated them. After a user changes a value, both values remain accessible at their mentions, and causal interventions show that both continue to influence the model's action. In natural closed-loop interaction, query failures separate into cases of weak structural support, incorrect value resolution, and failure to deploy otherwise-supported constraints, with targeted interventions producing systematically different repair behavior across these cases. These findings motivate a state-action controller that starts from the base model action and selectively edits it using structural readouts, without requiring a complete predicted belief state as an intermediate representation. On held-out MultiWOZ interaction across five models, it raises the base model exact-query accuracy from .318 to .621 and task success from .272 to .371 at negligible added cost. Overall, reliable interaction requires not only retaining conversational information, but resolving which available constraints currently apply and ensuring that they govern action.

---


### 491. [Prospective Interpretation Risk: Principled Communication Control Between LLMs](https://arxiv.org/abs/2609.33885)

**<font color=#1a73e8>作者：</font>** Wanrong Yang, Rehan Deen, Julian Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agentic systems increasingly rely on models communicating with one another, yet existing uncertainty and multi-agent methods rarely estimate how a particular receiver will interpret a message before it is sent. This matters in heterogeneous systems, where capable receivers can reconstruct different tasks from the same message. We model this as a sender-receiver problem with a latent receiver type and define prospective interpretation risk (PIR): the probability that a receiver reconstructs a task other than intended. Rather than model an LLM's full input-output behaviour, we use black-box probes relating messages, intended tasks, and receiver-specific reconstructions, yielding scalable supervision while separating interpretation from downstream capability failure. Offline, heterogeneous frozen receivers provide supervision for receiver-conditioned risk and the effects of predefined mutable message features. At deployment, history induces a posterior over receiver types, guiding message revision and selection. We introduce value of interpretation information (VoII), querying for receiver information only when its expected communication benefit exceeds its cost. Our theory characterises when receiver information has decision value and bounds such queries. Empirically, interpretation-failure rates vary by 4-13x across receivers. Receiver information reduces PIR calibration error by 68% relative to a receiver-agnostic predictor, largely by correcting receiver-specific risk levels. PIR-guided revision reduces interpretation failure by 44% relative to the original message and 40% relative to a generic rewrite, mostly through a repair that helps every receiver. VoII outperforms information-gain and random querying at matched cost on the interpretation objective it optimises, lowering interpretation failure from 3.84% to 3.79% while querying 18.2% of episodes.

---


### 492. [LLMs learn different forms of metacognition when trained to predict their own accuracy](https://arxiv.org/abs/2609.33886)

**<font color=#1a73e8>作者：</font>** Nicolas Yax, Stefano Palminteri, Pierre-Yves Oudeyer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are trained to always produce an answer, regardless of whether they possess the relevant knowledge, which leads them to fabricate facts. Prior work has shown that LLMs' confidence estimates correspond poorly to their actual performance, and that fine-tuning can substantially improve them. However, what models actually learn during such training remains poorly understood. We investigate how LLMs acquire metacognitive monitoring, the ability to know what one knows, by training 10 open-weight LLMs to predict their own accuracy on factual multiple-choice questions before answering them. We find that trained confidence reflects two distinct signals. While on questions close to the training data, it tracks the model's true accuracy, in other domains, it instead tracks output consistency: the concentration of the model's answer distribution. Output consistency tracking emerges early in training and generalizes across datasets, whereas accuracy tracking develops later and remains local to the training distribution. These results suggest that calibration training may not teach models to generally detect errors they commit confidently, and they raise broader questions about the nature of metacognition in artificial systems.

---


### 493. [Faster Block-Diffusion Serving with Distribution-Free Risk Guarantees](https://arxiv.org/abs/2609.33887)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Dongyub Jude Lee, Chanjun Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block-diffusion language models are served at hand-picked operating points, such as acceptance thresholds, buffer depth, schedule, checkpoint and precision, and each point is chosen by its mean benchmark accuracy. However, a mean does not tell an operator how often a faster configuration fails on prompts that the slower one answers correctly. On the serving engine and its decode traces, the default commit rule already commits every fully resolved block, a static skip rule captures nearly all of the compute that allocation can save, and self-distillation on engine-decoded targets adds speed at unchanged accuracy. Larger speedups come from lower thresholds, which commit tokens that are still uncertain. We therefore present Redline, a finite-sample procedure that selects operating points, hand-picked or learned, from the correctness of their answers on calibration prompts. Redline keeps the reference-relative risk, the joint probability that the reference answers correctly and a candidate configuration does not, within a user-chosen budget with high probability, and deploys the fastest configuration that passes. It speeds up math at a smaller risk budget than code in both model families, and at a budget of ten percent it deploys a LLaDA2 math configuration that commits over a third more tokens in each forward. It also applies without modification to the acceptance rule of speculative decoding and to weight quantization. On the same calibration data, Redline stays within its stated failure probability, whereas each tolerance of a mean-accuracy rule either gains less speed for some model and task or exceeds the risk budget far more often for another. Code is available at this https URL.

---


### 494. [Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding](https://arxiv.org/abs/2609.33889)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seungyoon Lee, Seongtae Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> At each step, decoding one sequence with a large language model rereads the projection weights, whose traffic is fixed, and the key-value (KV) cache, whose traffic grows with context. Activation sparsity trims the first term and KV-cache sparsity the second, yet their reported speedups are hard to compare because each depends on context length and on the dense attention kernel it is measured against. We derive a byte crossover, the context length at which the two savings are equal, together with ideal speedup bounds for each branch and for their composition, from model dimensions and keep ratios alone. We then time both branches and their composition from 2K to 128K tokens on two GPUs after a dense prefill of real text, with dense and sparse modes reading the cache through the same split-K attention kernel. The projection branch leads at short context and the KV branch at long context, with speedups that follow their byte bounds up to fixed kernel costs. Adding these costs, measured in separate sweeps, lets the byte account predict the measured crossings of three keep-ratio pairs, a second model, and a second GPU to within 4.1K tokens. Timing the dense baseline with masked instead of split-K attention inflates the apparent speedup of the same KV policy about fivefold. An attention-scored KV selection answers the same passkey and multi-key placements as dense decoding up to 127K tokens, whereas a KV window misses most of them. Under matched perplexity budgets, activation sparsity composed with this selection decodes 14 to 26% faster than the best single branch on both GPUs. Code is available at this https URL.

---


### 495. [MISHAP-Bench: A Hallucination Benchmark for Large Audio-Language Models](https://arxiv.org/abs/2609.33893)

**<font color=#1a73e8>作者：</font>** Zhi Wen Soi, Giulio Segalini, Jian-Jia Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large audio-language models (LALMs) produce fluent responses about audio but often hallucinate by making plausible yet ungrounded claims. Existing audio hallucination benchmarks mainly measure response correctness, leaving it unclear whether an LALM hallucinates or simply fails to understand the audio. We challenge correctness-based evaluation by defining two hallucination categories: (i) context, where claims are not grounded in the audio; and (ii) knowledge, where claims about audio-related topics lack support from externally verifiable facts. We introduce MISHAP-Bench, a comprehensive benchmark with 12,000 challenging open-ended question-audio pairs and a rigorous evaluation pipeline covering both categories. To evaluate open-ended responses, we propose a groundedness judge that uses reference rubrics and judge prompts guided by human annotations. We extensively evaluate ten state-of-the-art LALMs and show that hallucination remains substantial. Even a frontier model such as Gemini 3.7 Flash reaches a hallucination rate of 36.5%. We further adapt and benchmark four mitigation methods from multiple domains for LALMs. Despite some improvements, effective hallucination mitigation remains an open challenge. Finally, we call on the community to evaluate hallucination and benchmark mitigation methods with MISHAP-Bench.

---


### 496. [No Free Efficiency: Revisiting the Trade-off Between Training Efficiency and Model Vulnerability](https://arxiv.org/abs/2609.33898)

**<font color=#1a73e8>作者：</font>** Yiyong Liu, Jun Sakuma, Michael Backes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training efficiency has become the central driver of recent progress in foundation models. To overcome the massive computational and data requirements of large-scale training, researchers increasingly adopt strategies such as selective data sampling, efficient pre-training, and simplified reinforcement learning pipelines. While these strategies drastically reduce overhead, they prompt a critical, yet neglected question: Is efficiency achieved at the expense of model robustness and security? To our knowledge, we present the first systematic cross-domain investigation of the efficiency-vulnerability trade-off. Across vision and language models, we show that efficiency-oriented training increases susceptibility to adversarial and privacy attacks. We characterize this vulnerability by analyzing the models' internal geometry and functional representations, demonstrating that the evaluated efficient variants consistently exhibit sharper loss geometry together with systematic changes in representational structure. We further extend our analysis to "zero RL training", finding that models trained using simplified RL recipes exhibit substantially greater susceptibility to catastrophic forgetting and more pronounced overconfidence than those trained through conventional alignment pipelines. Our findings suggest that training efficiency is rarely a "free lunch"; rather, the mechanisms that minimize computation can inadvertently compromise safety. We conclude by calling for a paradigm shift toward multi-objective training that jointly optimizes for performance, cost, and security.

---


### 497. [Can Prompt Anonymity Protect Your Identity From LLM Providers?](https://arxiv.org/abs/2609.33903)

**<font color=#1a73e8>作者：</font>** Dzung Pham, Dillon Sheils, Naina Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> User conversations with large language models (LLMs) often contain highly sensitive personal information that can be exploited by LLM providers to create detailed user dossiers, enable targeted advertising, and train more powerful models. To protect user privacy, anonymizing LLM proxies have emerged as a practical solution that separates user identity from their prompts, yet this approach still leaves the prompt content visible to LLM providers. We study the impact of this gap by conducting the first empirical investigation into the risk of prompt authorship re-identification. Towards this end, we create PromptAnonBench, a novel benchmark for evaluating prompt anonymity, consisting of over 175,000 cleaned, authentic multi-turn user prompts from various real-world datasets (SWE-Chat and WildChat). Using the embeddings of historical user conversations, an attacker can correctly detect and re-identify at least one anonymized conversation for 50--75% of SWE-Chat users and up to 10% of WildChat users at a 10% false acceptance rate for out-of-set users, even with text-based defenses applied. Our findings unveil the risk of relying only on anonymity for private LLM inference and the gap in existing text privacy defenses.

---


### 498. [SlopBench: How Well Can We Rank Language Models by Slop? A Multi-Domain Benchmark of Repetitive AI Writing](https://arxiv.org/abs/2609.33905)

**<font color=#1a73e8>作者：</font>** Dhruv Roongta, Harsha Gaddipati, Anh Tuan Huynh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SlopBench asks which models produce the stiff, repetitive prose readers call AI slop, a question detectors leave open once they have classified a text as machine-written. We evaluated eighteen models on 112 hand-written tasks in email, social posts, essays, and workplace chat, sampling each model on each task up to ten times, for 19,928 outputs in all. SlopBench scores four surface behaviors a reader can check by hand: length against the word band each task specifies, opener repetition across a model's own samples of one task, and paragraph rhythm and fixed lexical constructions against pre-ChatGPT human corpora. Under one fixed weighting, Kimi K2.6 scores lowest at 21.1 and Mistral Large highest at 40.6. Across 500 random reweightings Kimi has the lowest score in 58 percent of draws and Mistral the highest in 97 percent. No draw preserves the full order of the eighteen, and a scenario bootstrap leaves exactly one of those ranks unambiguous. We ran three further checks on that middle order: a crowd arena, an AI detector, and lexical diversity. None of them confirmed the order. We therefore report the four behaviors separately and treat the composite as one weighting among many, and we release the prompts, outputs, reference statistics, and scoring code.

---


### 499. [When Consent Outlives Context: Residual Authority Replay in Long-Lived Agents](https://arxiv.org/abs/2609.33910)

**<font color=#1a73e8>作者：</font>** Zhihao Zhang, Chao Wang, Rujia Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on user approval to authorize security-sensitive actions at runtime. Such approvals are granted within a specific task and execution context. In long-lived agents, authorization decisions may need to persist across tasks or sessions. We find that this continuity can outlive the context that originally justified the approval, creating residual authority reusable without renewed consent. We expose this failure mode through a longitudinal attack that starts from a target security-sensitive action, identifies the authority required to execute it, induces benign interactions that legitimately obtain that authority, and later replays the residual authority during adversarial execution. Across controlled and live settings, we demonstrate that residual-authority replay arises in practice and substantially increases the success of prompt-injection and context-rebinding attacks. We evaluate 508 AgentDojo attack cases across six LLM families using production-derived authorization semantics. With residual authority, attack success rate (ASR) increases by up to 35.1 percentage points compared with a fresh authorization state. In live context-rebinding attacks on 55 Terminal-Bench cases across three real-world production coding agents, residual-authority replay increases ASR by 24.9 percentage points on average. These findings expose a fundamental mismatch between persistent authorization and the contextual nature of user consent in long-lived LLM agents.

---


### 500. [A2A-CaseVerify: Merkle-Linked Case-Evidence Verification for Cross-Organization A2A Workflows](https://arxiv.org/abs/2609.33914)

**<font color=#1a73e8>作者：</font>** Adil Alshammari, Hayretdin Bahsi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent-to-Agent (A2A) communication enables large language model (LLM) agents to exchange tasks, messages, and artifacts across organizations. A valid message alone does not establish that a final workflow claim is supported by a complete, ordered, and case-consistent evidence path. We present A2A-CaseVerify, a deterministic offline verifier that maps preserved A2A runtime objects, business events, and typed support edges to a directed case evidence graph. It commits A2A envelopes, event projections, and support edges, then combines event and edge leaves into a deterministic case Merkle root. The verifier returns SUPPORTED with status OK only when protection and profile-specific reconstruction checks pass. We evaluate one canonical supported healthcare-profile bundle and 13 controlled mutations. We separately test a valid bundle generated with the official Python A2A software development kit (SDK). In these tests, the canonical and SDK-generated bundles are accepted. All 13 mutations are rejected, and each returned reason-code set contains its targeted diagnostic code. A2A-CaseVerify adds offline case-level evidence-support verification to A2A interoperability.

---


> [!TIP]
> 当前位于：**451-500**（第 10/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
