# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 151. [CyberPersistBench: Evaluating LLM-Based Cyber Attackers on Installation and Persistence](https://arxiv.org/abs/2609.36573)

**<font color=#1a73e8>作者：</font>** Sujin Chen, Lijun Li, Xuhong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While LLM-based attackers exhibit growing proficiency in vulnerability exploitation, most existing cybersecurity benchmarks suffer from single-stage truncation, prematurely terminating evaluation upon initial access. In practice, initial footholds are exceptionally fragile across operational disruptions such as service restarts and host reboots. Whether LLM-based attackers can establish and maintain durable footholds beyond initial compromise remains a central blind spot in cybersecurity evaluation. To bridge this gap, we introduce CyberPersistBench, the first benchmark dedicated to post-compromise installation and persistence. Decoupled from upfront exploitation, CyberPersistBench frames persistence as an adversarial survival task in which agents use native host mechanisms to maintain footholds across staged system disruptions. Deterministic checks support a six-level scoring method (L1--L6) spanning installation and persistence. The benchmark comprises 203 core tasks across seven categories, augmented by multi-host and active defense extensions. Empirical evaluations across five frontier agents show that autonomous persistence remains limited (27.6%--44.8%) and drops further on defense-enabled tasks (5.5%--13.3%); nonetheless, these results reveal an emerging cyberattack risk, underscoring the necessity of benchmarking post-compromise persistence. CyberPersistBench thus establishes a foundational benchmark for post-compromise installation and persistence, delineating the operational boundaries of autonomous cyber agents.

---


### 152. [SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time](https://arxiv.org/abs/2609.36580)

**<font color=#1a73e8>作者：</font>** Yu Cheng, Yongkang Hu, Shuaijie Ma 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents deployed in real-world environments continually encounter new tasks and safety risks, while execution feedback typically becomes available only after each task is completed. However, existing self-evolving approaches commonly rely on multiple rounds of optimization over fixed and repeatedly accessible task distributions, fundamentally differing from test-time adaptation in real-world deployment, where only experience accumulated from past tasks can be used to improve safety decisions on future unseen tasks. To address this limitation, we propose SafeCoEvo, a test-time Harness-Guard co-evolution framework for LLM agent safety that enables the external safety system to continually adapt from accumulated runtime experience. SafeCoEvo jointly improves two complementary safety capabilities at different timescales: S-Harness rapidly externalizes recent runtime experience into updatable explicit safety knowledge that can promptly influence subsequent tasks, while GuardVPO internalizes accumulated runtime safety experience over a longer timescale into parametric risk-judgment capabilities. By combining short-term rapid adaptation with long-term capability consolidation, SafeCoEvo continually improves the agent's safety capabilities, reducing the unsafe outcome rate by 10.05% while improving the task success rate by 12.15% over the strongest baseline, thereby achieving simultaneous gains in safety and task utility.

---


### 153. [MemEvo: Automatic Discovery of Streaming Video Memory Mechanisms](https://arxiv.org/abs/2609.36581)

**<font color=#1a73e8>作者：</font>** Guohong Liu, Jialei Ye, Shanhui Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Query-agnostic streaming video understanding requires vision-language models to continuously compress an indefinitely growing visual stream into a bounded memory before future queries are known. The performance depends critically on the memory mechanism--what observations to preserve, how to represent and consolidate them, and what information to retrieve when a query eventually arrives. Rather than designing a single memory architecture by hand, we formulate memory design as a search problem over executable memory programs. We introduce a lightweight domain-specific language that expresses memory mechanisms through structured primitives for representation, admission, retention, consolidation, budgeting, and retrieval, while enforcing causal and bounded-memory constraints. Although structured, the derived program space remains large and contains heterogeneous, conditionally dependent design choices whose effects can only be assessed via downstream execution. We therefore propose MemEvo, an LLM-driven auto-research framework that uses pretrained LLM as a semantics-aware proposal model to iteratively generate and refine candidate memory programs based on accumulated experimental feedback. At runtime, a deterministic evaluation pipeline validates and evaluates each candidate, while the underlying vision-language model remains frozen throughout discovery. We finally produce a training-free, bounded-memory mechanism. Extensive experiments on StreamingBench and OVO-Bench demonstrate strong streaming video understanding performance together with substantial context and inference efficiency.

---


### 154. [Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It](https://arxiv.org/abs/2609.36585)

**<font color=#1a73e8>作者：</font>** Zehao Jin, Ruixuan Deng, Junran Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained transformers use little of their depth to follow references in context. Thirteen base models reliably follow only 1.4-3.6 lines, and extra pretrained loops add little. A task-trained rank-8 LoRA at one early layer extends this computation with all model weights frozen. Qwen3-8B improves from 15.5% to 99% exact accuracy on 24-line chains; a longer-trained LoRA reaches 50 lines. Ouro-1.4B reaches 60 lines after four loops and at least 160 after eight. The LoRA starts a relay: program lines pass on their chain identity through a short range of middle layers. Frozen heads read progressively further up the chain, and removing parent-line attention stops the relay. A frozen-model measurement locates the last useful intervention layer within tolerance in three of four held-out models. Task-specific LoRAs also improve MuSiQue. Default answers therefore understate the computation accessible through a tiny edit. Code and an interactive demo are available at this https URL

---


### 155. [Learned Reporting Preferences in RLVR Can Conflict with the Current Request](https://arxiv.org/abs/2609.36587)

**<font color=#1a73e8>作者：</font>** Yupeng Chang, Wenxuan Zhang, Yuan Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a prominent approach for improving language-model performance on reasoning tasks using automatically checked answers. Yet convention-matched evaluation cannot reveal whether reinforcing one reporting convention reduces adherence to a different request that the initial policy already follows. To test this, we train matched policies under two reporting conventions and evaluate each policy under both current requests, using the same initial policy as a shared reference. We complement this crossed design with controlled interventions and independent human calibration. On GSM8K, boxed-format RLVR reduces the fraction of Qwen2.5-7B responses containing the requested hash-format payload by 35.33--74.37 percentage points relative to a 95.45% initial baseline in four of five training seeds; the fifth improves by 2.50 points. In the four deteriorating runs, almost every response that omits the requested payload instead retains the trained boxed convention, and the same four seeds deteriorate under two fixed paraphrases. Changing only the final-answer marker in supervised targets reverses which reporting convention the model prefers across three seeds, providing controlled evidence that this preference is learnable. Across three settings with independent human calibration, gains under a convention-sensitive scorer exceed the corresponding gains in committed-answer correctness, i.e., the correctness of the answer the model actually commits to. Together, these results separate three distinct post-training outcomes: learned reporting preference, current-request adherence, and committed-answer correctness. They show that convention-matched accuracy alone does not fully characterize post-training behavior and motivate evaluating current-request adherence alongside convention-matched task accuracy.

---


### 156. [SEED: Self-Speculative Decoding via Implicit Encoder-Decoder](https://arxiv.org/abs/2609.36590)

**<font color=#1a73e8>作者：</font>** Hankun Lin, Patrick Pynadath, Ruqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-speculative decoding accelerates large language model (LLM) inference by drafting tokens from the target model itself, but faces a sharp tradeoff between the quality and cost of the draft. Early-exit methods produce drafts cheaply by terminating computation at intermediate layers, but forgo the deeper representations that later layers provide and thus suffer in draft quality. Multi-token prediction preserves draft quality by emitting from the model's final hidden states, but pays for a full forward pass to produce those states at every drafting step. We propose self-speculative encoder-decoder (SEED), a self-speculative method that obtains high-quality drafts cheaply by reusing the deep contextual representations already computed during verification. We reinterpret the standard decoder-only transformer as an implicit encoder-decoder: the first layers (encoder) build deep contextual representations, and the last few layers (decoder) emit tokens from them. Encoding and verification are merged into a single step: verification is performed by the full encoder-decoder, and the contextual representations of the verified prefix are cached for reuse during drafting. Drafting is therefore very fast: between verifications, the lightweight decoder drafts multiple tokens autoregressively, each conditioned on the cached representations and on preceding drafts. Experiments across multiple benchmarks show that SEED achieves up to 2.7$\times$ average speedup on 4B-scale models, outperforming both early-exit and MTP-style self-speculative baselines and running 28% faster than the state-of-the-art EAGLE-3, while preserving or even improving the generation quality of standard autoregressive fine-tuning. Code is available at this https URL.

---


### 157. [SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation](https://arxiv.org/abs/2609.36601)

**<font color=#1a73e8>作者：</font>** Miteto Wei, Xiaohan Wang, Zehao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) reduces train-test state mismatch by training a student on its own generated trajectories, but weak students may visit teacher-misaligned prefixes where supervision is less representative. We introduce SAKI (Supervision Allocation with KL-constrained Interpolation), which combines a KL-constrained teacher-guided rollout with maximal coupling and reuses realized accept/correction events to route token-level supervision. Accepted positions retain sampled-token reverse-KL supervision, while correction positions receive direct supervision on the teacher's highest-probability token. Under maximal coupling, the correction probability is exactly TV(p_t, q_t), so the same trust-region radius controls rollout deviation and upper-bounds intervention and specialized-supervision frequency. We further implement an engine-resident speculative verifier that preserves the exact-q trajectory distribution and coupling semantics while improving matched-workload rollout throughput by 4.22x. Across seven mathematical reasoning benchmarks, SAKI improves the matched teacher-guided baseline in Mean@8 and Pass@8 for both 1.7B and 0.6B students. Placement controls and fixed-prefix analysis further support correction-triggered routing as a conflict-adaptive supervision signal.

---


### 158. [Act First, Reason Later: Accelerating On-Policy Distillation for Multi-Turn Agents via Reference-Conditioned Inverse Dynamics](https://arxiv.org/abs/2609.36608)

**<font color=#1a73e8>作者：</font>** Zubin Zheng, Jiahao Wu, Shaofeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains multi-turn language agents with dense teacher supervision on student-generated responses. However, standard think-then-act rollouts require lengthy reasoning before each short action, delaying environment transitions and experience collection. Generating actions directly reduces this delay but can degrade rollout quality. To address this, we propose ActFirst-OPD, an act-first, reason-later training framework that decouples environment interaction from full-response generation. The student infers and executes actions through reference-conditioned inverse dynamics using its current interaction context and a reference next observation, and switches to autonomous next-action prediction when the resulting transition deviates from the reference trajectory. From the collected interaction contexts, the student asynchronously generates full think-then-act responses for token-level teacher supervision. Experiments across 0.6B-, 1.7B-, and 4B-parameter Qwen3 students show that ActFirst-OPD achieves average wall-clock training speedups of $2.3\times$ on ALFWorld, $1.8\times$ on WebShop, and $4.9\times$ on ScienceWorld over Vanilla OPD. It matches or exceeds all compared OPD baselines in mean task success rate across eight of nine benchmark-model settings. These results demonstrate that reasoning need not block acting during multi-turn agent distillation.

---


### 159. [Multi-Channel Mitigation of Source-Trust Shortcuts in Fact-Checking RL Agents](https://arxiv.org/abs/2609.36611)

**<font color=#1a73e8>作者：</font>** Jianchang Su, Yiwei Yang, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented fact-checkers often receive a reliability label, such as HIGH or LOW trust, for each evidence source. These labels should adjust the model's confidence and its decision to search for more evidence, while the verdict should follow the evidence content. We introduce TrustSwap, a counterfactual test that swaps, lowers, or removes source labels while keeping every evidence text fixed, and measures its three output channels (the verdict, the confidence, and the search decision) separately. Across untrained and RL-trained models at two scales, three datasets, and two prompts, confidence and search respond to the labels as intended in 49 of 50 comparisons, yet a label change alone alters 4-23% of confident verdicts for Qwen3 models and up to 50% for an existing RL-trained fact-checker. Standard GRPO fine-tuning amplifies this shortcut at 8B in all six settings. To reduce it, we propose trust-swap augmentation (TSA), which trains GRPO on each claim with both its original and its label-swapped evidence under the same gold verdict. At 4B, TSA lowers the verdict flip rate by 7-35% (relative) in four of six settings, keeps accuracy and the intended confidence and search responses, outperforms reward-based alternatives in the main setting, and carries over to an unseen label-removal perturbation. An added consistency reward helps on the trained-on swap but not on unseen perturbations. At 8B, TSA's effect is not detectable, which makes scale the main open question.

---


### 160. [Do LLMs Really Forget? Hidden-State Leakage in Model Unlearning and How to Fix it](https://arxiv.org/abs/2609.36612)

**<font color=#1a73e8>作者：</font>** Hadi Reisizadeh, Jiajun Ruan, Sijia Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning in large language models (LLMs) is typically evaluated at the output level, where a model appears to suppress sensitive or undesirable content. In this work, we show that such evaluations can create an illusion of forgetting: even when output-level leakage is eliminated, sensitive information can remain encoded in the model's hidden representations. We first provide a theoretical analysis establishing a fundamental separation between output suppression and representational erasure. Specifically, we show that the decoder can be made arbitrarily insensitive to sensitive directions, driving output-level leakage to zero, while the hidden representations retain the underlying information. To empirically validate this phenomenon, we train generative probe decoders on hidden states across transformer layers, enabling layer-wise measurement of information leakage. Across three widely used benchmarks, TOFU, MUSE, and WMDP, and state-of-the-art unlearning methods, we find that substantial sensitive information remains recoverable from hidden representations, even when standard output-level metrics indicate successful unlearning. To address this gap, we propose Probe-Adversarial Representation Suppression (PARS), an unlearning objective that adversarially minimizes the extractable information from hidden representations. PARS directly targets representational leakage and provides significantly stronger guarantees of erasure under adversarial probing and relearning attacks, outperforming all evaluated baselines. Our results highlight a fundamental limitation of existing unlearning paradigms and suggest that true forgetting in LLMs requires controlling not only model outputs, but also the information encoded in hidden representations. Codes are available at this https URL.

---


### 161. [Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent Stress Test](https://arxiv.org/abs/2609.36614)

**<font color=#1a73e8>作者：</font>** Jiapeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A commercial incentive need not enter the final ranking algorithm to affect a shopping assistant's recommendation: it may instead influence which preference question the assistant asks. We make this distinction experimentally observable in a deliberately small, synthetic setting. Each task has two products, three verified numerical attributes, a price limit, and a private fixed preference vector. An honest simulated user answers one pairwise question. A separate recommender receives the products and this answer but not the sponsorship assignment. We contrast a neutral question, a soft commercial instruction, and an explicitly adversarial instruction to ask about the sponsor's advantage while omitting the rival's advantage. Across 40 held-out sponsorship-assignment cases (20 distinct catalog-preference contexts), the soft instruction changes no selections. The targeted instruction raises sponsored selection by 0.30 and reduces mean synthetic utility by 0.0547 relative to neutral questioning (95% context-bootstrap interval [-0.0828, -0.0291]) for one language-model recommender. A fixed Bayesian recommender shows a similar effect; a second model makes the same choices on all 120 frozen question-answer inputs. A terminal-answer consistency judge rates all 20 sampled targeted answers consistent, although five have synthetic regret above 0.05; a separate question-coverage dimension flags their one-sided elicitation. A robust partial-preference certificate remains valid under the stipulated synthetic utility but certifies only 16 of 40 targeted cases and is not better than asking a neutral question directly. These results establish neither typical behavior under advertising incentives nor effects on actual consumers.

---


### 162. [Generating Edit-Inducing Questions for AI Research Manuscripts](https://arxiv.org/abs/2609.36617)

**<font color=#1a73e8>作者：</font>** Sebastian Joseph, Zichao Wang, Jennifer Healey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the ability of LLMs to generate edit-inducing questions whose answer will improve a paper draft. On a dataset of paired submission and camera-ready papers from ICLR and NeurIPS, we compare the helpfulness of questions from GPT models with or without full paper context to that of human reviewers. GPT produces more edit-inducing questions and its questions are associated with more extensive edits and cover a broader range of edited content compared to questions from reviewers. However, a much smaller percentage of the GPT questions are edit-inducing. Our analyses confirm that automated questions can be beneficial to authors and highlight an example task where proper attending to long context deteriorates reasoning model ability to produce helpful output.

---


### 163. [Semantic Projection for Continual Self-Evolution of Language Agents](https://arxiv.org/abs/2609.36626)

**<font color=#1a73e8>作者：</font>** Ziyu Liu, Jun Chen, Lixu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly rely on persistent natural-language skills to adapt beyond their frozen model parameters. When a shared skill is repeatedly revised from a non-stationary, heterogeneous task stream, however, improvements for new tasks can overwrite procedures needed for earlier ones. In continual learning, Orthogonal Gradient Descent (OGD) addresses analogous interference by projecting a new-task gradient onto a subspace that locally preserves prior predictions. Natural-language skill revisions, however, have neither gradients nor a canonical vector space in which such a projection can be performed. We introduce \emph{Semantic-Scope Projected Evolution} (SSPE), which transfers the functional principle of gradient projection from parameter space to behavior space. SSPE treats an unconstrained skill revision as a proposed update, identifies acquired capabilities with which it may interfere, and uses the observed gains and regressions to construct a compatible revision rather than merely rejecting the update. This enables one shared skill to evolve across latent and recurring task contexts without exposing semantic domain identities to the evolution model. Across controlled synthetic streams and heterogeneous real-agent benchmarks, SSPE improves final cross-domain competence and mitigates forgetting relative to strong skill-evolution baselines. The evolved skill also retains the strongest average performance after transfer to a different executor model. These results establish semantic projection as a promising principle for stable and adaptive self evolution of language agents.

---


### 164. [Beyond Binary Preferences: Graded Preference Optimization for Limb-Motion Captioning](https://arxiv.org/abs/2609.36628)

**<font color=#1a73e8>作者：</font>** Yanan Wang, Tingsong Li, Kaixun Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) can generate rich video captions, yet often misidentify which person performs an action or which limb is involved, particularly across camera cuts. Improving these details requires evaluation and training that distinguish missing information from incorrect assertions. We introduce FlexBench, a benchmark spanning 3,105 shots and 18,161 evaluation queries, with human-verified identities and systematic per-person coverage of fine-grained limb actions and states. Its reference-derived checklists support automated assessment of complete captions in their person and shot contexts. Our Graded Physical Alignment score (GPA) awards credit for correct content and deducts points for incorrect or fabricated actions, making these errors explicit in the aggregate score. Building on this rubric, we propose Graded Margin Direct Preference Optimization (GM-DPO), which assigns stronger preference margins and greater training weight to more severe action errors. Across three VLM backbones, GM-DPO achieves the highest substantive-action and GPA scores among the evaluated preference objectives, improving GPA over DPO by 2.02-3.40 points. On Qwen3-8B, it reduces the weighted hallucination rate by 21.3% relative to DPO. These gains accompany sustained long-form output, improved shot structure, and competitive performance on three additional multimodal benchmarks.

---


### 165. [What Makes Recurrence Effective in Looped Language Models?](https://arxiv.org/abs/2609.36636)

**<font color=#1a73e8>作者：</font>** Xinlin Zhuang, Siyuan Wang, Imran Razzak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models (LoopLMs) increase computational depth through parameter sharing, offering a path to scale inference computation without adding parameters. However, it remains unclear when additional recurrence is beneficial and how architectural choices affect its effectiveness. Through controlled experiments, we systematically examine (1) when recurrence helps, (2) where it should be applied, and (3) how its conditioning affects performance. Our evaluation covers inference budgets below, within, and beyond the training horizon under knowledge and reasoning tasks. (1) We find that recurrence can improve reasoning beyond the training horizon while degrading knowledge performance, but harder reasoning instances do not consistently benefit more. (2) Performance also depends on how distinct layers and recurrent iterations are allocated, showing that effective depth alone is insufficient to predict behavior. Non-recurrent output layers improve robustness to under-unrolling, while the preferred placement of input and output layers varies with inference budget. (3) Finally, we find that conventional initial-state injection offers limited robustness to varying recurrence depth. We therefore propose history-state injection as an alternative, and show that channel-wise history-state injection combined with timestep conditioning offers a low-cost and more effective design, better preserving knowledge under extended unrolling while improving robustness across inference budgets. Overall, our results clarify when recurrent computation helps, where it fails, and offer practical guidelines for designing LoopLMs across variable inference budgets.

---


### 166. [Inducing Process Supervision from Outcome-Only Reinforcement Learning](https://arxiv.org/abs/2609.36641)

**<font color=#1a73e8>作者：</font>** Shengda Fan, Xin Cong, Zhong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) have become a key component for LLMs, as their step-level feedback supports both post-training and test-time reasoning. However, training strong PRMs remains costly: human step annotation is difficult to scale, while Monte Carlo estimation is computationally expensive and can drift from the intrinsic correctness of steps. To get effective PRMs at low cost, we introduce TIPS (Thinking-Induced Process Supervision), an outcome-only reinforcement learning (RL) framework for training generative PRMs. In TIPS, the model generates a chain-of-thought (CoT) followed by step-level labels and an outcome label. The reward depends solely on whether the predicted outcome matches the ground truth, and the resulting group-relative advantage is used to optimize the entire generated response. Intuitively, when checking intermediate steps helps determine the outcome, more accurate checks can lead to better outcome judgments and higher rewards. Outcome-only RL can therefore reinforce step-level verification without explicit process supervision. We validate the effectiveness of TIPS across math and agent benchmarks and four backbone families. Notably, TIPS-Qwen3-4B-Thinking-2507 reaches 85.2 F1 on ProcessBench with only 3.2K outcome-labeled trajectories, surpassing all evaluated trained PRMs and strong prompt-only judges such as GPT-5.4-Instruct and Claude-4.7-Opus, while still trailing o1-mini. Code and data are available at this https URL.

---


### 167. [PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2609.36642)

**<font color=#1a73e8>作者：</font>** Muyang Li, Jie Yang, Zhengyu Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model agents are usually trained by reinforcement learning from one reward per episode, and privileged self-distillation enriches it by letting the same policy, given a skill, teach its skill-free self through token probabilities. However, we identify two phenomena that question this channel. Invisible Advantage: a skill in context lifts WebShop success from 42.2% to 56.2%, yet changes the probabilities of fewer than a quarter of the sampled tokens. Much to Align: a skill changes the hidden states of over 80% of response tokens, in a way that linear probes can trace back to the specific skill. To exploit this, we propose Privileged Representation On-policy Self-Distillation (PR-OPD). After a GRPO warm start, the policy writes a hindsight skill for each trajectory, re-reads its own responses with that skill as a stop-gradient teacher, and aligns its projected hidden states to the teacher's at every layer alongside the reward objective, with no external skill library, separate teacher, or inference overhead. On ALFWorld and WebShop with two backbones, PR-OPD achieves the best overall results in every setting, improving over GRPO by up to 4.7 points in ALFWorld success and 14.0 points in WebShop accuracy. Code is available at this https URL.

---


### 168. [VLM4Cluster: Benchmarking Deep Clustering In the Era of Vision-Language Pre-training](https://arxiv.org/abs/2609.36648)

**<font color=#1a73e8>作者：</font>** Yuanwei Hu, Bo Peng, Yuheng Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language pre-training has reshaped image clustering, giving rise to language-assisted image clustering (LaIC), which leverages textual semantics to complement visual representations. Despite the rapid proliferation of LaIC methods, it remains unclear how much LaIC has actually advanced image clustering, as existing studies generally suffer from major limitations, including inconsistent experimental settings, inadequate dataset selection, and limited evaluation dimensions. To address this gap, we introduce VLM4Cluster, a comprehensive benchmark for image clustering in the era of pre-trained vision-language models (VLMs). VLM4Cluster implements 17 representative methods spanning classical, deep, and language-assisted image clustering, and evaluates them on 20 datasets covering classical, challenging, fine-grained, large-scale, and out-of-distribution settings. Beyond effectiveness, VLM4Cluster systematically investigates image clustering along three complementary dimensions: robustness to adversarial perturbations, generalization under distribution shifts, and computational efficiency. Our study shows that LaIC substantially advances the clustering performance frontier on many semantically demanding benchmarks, generally exhibits stronger generalization under distribution shifts, and achieves a more favorable effectiveness-efficiency trade-off. However, its gains become less consistent on large-scale and fine-grained datasets, while language assistance does not systematically reduce sensitivity to adversarial perturbations. VLM4Cluster is released at this https URL.

---


### 169. [FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive Resolution](https://arxiv.org/abs/2609.36651)

**<font color=#1a73e8>作者：</font>** FangZhi Zhong, Xuerui Qiu, Yuqi Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning in large language models incurs substantial computation and memory costs. Visual text compression (VTC) reduces input length by rendering text as images, but fixed-resolution rendering creates a compression-performance trade-off: low DPI saves tokens at the expense of legibility, whereas high DPI spends tokens on irrelevant content. We introduce FocusVTC, which breaks this trade-off through adaptive resolution while preserving general multimodal capabilities. It combines compressed low-DPI global views with selective region enhancement, integrating enhanced views into ongoing reasoning. We construct 29.4K high-quality Reasoning-Evidence Localization (REL) chain-of-thought examples (REL-CoT) that link reasoning traces to page indices and bounding boxes. Multi-resolution REL supervised fine-tuning (REL-SFT) teaches the model to localize relevant regions, and Group Relative Policy Optimization learns when to enhance resolution and how to use the resulting observations, without a separate continual-pretraining stage. At 72 DPI on RULER v1, FocusVTC scores 87.4 at $2.9\times$ input compression, including tool observations, versus 57.5 for Glyph at $3.0\times$ input compression. It surpasses its text-input backbone on LongBench (56.40 versus 55.86), improves the MRCR macro-average by 13.91 points, and achieves a 51.19 macro-average on VTCBench. The MRCR latency evaluation also shows a $2.79\times$ online end-to-end speedup over Text. General multimodal capabilities are preserved, with MMMU increasing from 65.12 to 66.73 and MME from 2424.02 to 2457.62.

---


### 170. [Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference](https://arxiv.org/abs/2609.36654)

**<font color=#1a73e8>作者：</font>** Ruiyi Ding, Jie Li, Kang He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models make weight storage and memory traffic major inference costs, motivating low-precision formats that represent each weight with only a few bits. Such formats use a scale to map floating-point values into a small codebook; NVFP4 improves local range utilization by letting every 16 E2M1 weights share an E4M3 block scale. Choosing that scale is difficult in GPTQ because quantizing one column updates those that follow, so evaluating a block independently can misestimate its final reconstruction error. Large models pose a second challenge: full-precision weights, calibration activations, and second-order state cannot all remain on one accelerator, while assigning complete layers to devices leaves each time-consuming layer solve serial. We introduce \emph{Schur Replay}, a scale-selection algorithm that reproduces the GPTQ updates caused by each block scale and scores the resulting block error after accounting for compensation from unquantized columns. Separately, our execution infrastructure keeps only the active layer resident, tiers activations across device, host, and disk, retires full-precision layers after export, and distributes independent output rows across tensor-parallel ranks. Together, the algorithm and infrastructure attain $99.35\%$ and $100.84\%$ question-weighted recovery from BF16 across seven benchmarks on Qwen3.5-397B-A17B and Llama-3.3-70B-Instruct. On the 397B model, the infrastructure reduces measured per-layer time by $15.17\times$ over ModelOpt and $23.14\times$ over LLM Compressor, with lower memory used per GPU.

---


### 171. [On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training](https://arxiv.org/abs/2609.36659)

**<font color=#1a73e8>作者：</font>** Shufan Shen, Zhongni Hou, Junshu Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The strong generalization performance of on-policy post-training paradigms has motivated studies of their parameter update behaviors. However, these studies treat the observed behaviors only as byproducts in on-policy training, overlooking their potential to serve as optimization principles for improving the generalization of other paradigms such as supervised fine-tuning (SFT). To address this limitation, we investigate whether there exists a specific on-policy update behavior that can achieve such improvements. First, our analyses reveal that SFT updates parameters along consistent directions, while the on-policy paradigm continuously adjusts the direction during training. This difference inspires us to focus on the cumulative update direction of each parameter as a promising behavior. Then, we evaluate its effectiveness for improving generalization by proposing On-Policy direction-constrained Supervised Fine-Tuning (OPSFT), which constrains SFT updates to the direction identified by on-policy paradigms. The strong performance of OPSFT indicates that the generalization advantage of on-policy paradigms can be transferred to SFT through the parameter update direction. Once such a direction is identified, even SFT can generalize with its updates constrained to this direction. This finding offers two practical benefits by combining the strong generalization of on-policy paradigms with the advantages of SFT, including the high training efficiency and ability to leverage high-quality trajectories. For efficiency, we identify update directions that support strong generalization using a few on-policy training steps, and subsequently apply OPSFT to achieve high training efficiency. For leveraging high-quality trajectories, OPSFT can utilize these trajectories to continue improving a post-trained model along its update direction without disrupting the ability learned from on-policy training.

---


### 172. [AutoLoCo: Communication Efficient Distributed LLM Training via Adaptive Synchronization](https://arxiv.org/abs/2609.36662)

**<font color=#1a73e8>作者：</font>** Pengyu He, Yan Zhang, Ruien Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pre-training of Large Language Models (LLMs) is increasingly conducted across multiple data centers. As training scales to a larger number of accelerators, the fraction of time spent on computation decreases, while the fraction spent on communication increases. Therefore, frequent synchronization becomes a growing bottleneck. Local update methods reduce this cost by allowing workers to perform several optimizer steps between synchronizations. Most local update methods set the number of local optimizer steps between synchronizations before training and keep this interval fixed throughout the run. However, the best interval can change during the entire train process. If the interval and optimizer are adapted to the current training state, the communication frequency is reduced while maintaining the training performance. In this work, we introduce AutoLoCo, an adaptive training framework to reduce communication in LLM training. It adapts the local interval using scalar training statistics and corrects each outer update. Our method is motivated by two observations: 1) the appropriate local interval varies across training stages, and 2) changing the number of inner steps per interval creates a mismatch with an unchanged outer optimizer, requiring a correction to the outer update. We optimize this mismatch by correction of the outer optimizer for the momentum and the learning rate using the accumulated inner learning rate. Our experiments under communication constraints demonstrate that AutoLoCo reduces communication frequency by 27% relative to DiLoCo while maintaining training performance.

---


### 173. [GenLimitLib: A Formal Library for Language Generation in the Limit and AI-Assisted Mathematical Research](https://arxiv.org/abs/2609.36663)

**<font color=#1a73e8>作者：</font>** Shuangping Li, Peng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present GenLimitLib, a source-aligned Lean 4 library for language generation in the limit. Introduced by Kleinberg and Mullainathan at NeurIPS 2024, language generation in the limit studies a theoretical question motivated by LLMs: how to generate valid new strings from observed examples. This young and rapidly evolving field offers a natural testbed for studying large-scale formalization. GenLimitLib contains formal developments for 30 papers. It extracts shared definitions and reusable proof components while preserving paper-specific assumptions and statements, and records relationships across papers. In this way, GenLimitLib provides a concrete and structured view of the literature. We show through mathematical case studies and LLM experiments how our library can support both human mathematical research and AI-assisted research. Our Library: this https URL.

---


### 174. [Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement](https://arxiv.org/abs/2609.36675)

**<font color=#1a73e8>作者：</font>** Ziqi Zhao, Fanqing Meng, Haocheng Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) aims to achieve compounding gains by having models improve themselves. While most existing RSI systems optimize external agent harnesses or prompts around a frozen base model, data-centric RSI directly updates the model's own parameters by training on agent-generated data. However, because validating data strategies requires expensive model training, existing methods face a fundamental dilemma: a single agent gets trapped in narrow directions and lacks exploration breadth, while naive parallel search or heavy trace sharing sacrifices long-horizon search depth. To address this challenge, we introduce G"odel Forest, a multi-agent framework that organizes recursive self-improvement as an ensemble of co-evolving search trees. In G"odel Forest, each agent autonomously grows a persistent tree, deepening, branching, or pruning data strategies based on model feedback to secure depth, while parallel trees explore distinct regions of the data space to expand breadth. Crucially, rather than leaving trees isolated or flooding them with heavy execution logs, a dynamically co-evolving memory connects the forest: agents continuously distill their successes and failures into compact procedural lessons anchored to a global leaderboard. Through this forest ecosystem, a dead-end in one tree instantly warns the whole forest against unpromising paths, while an empirical breakthrough quickly seeds new exploration branches in neighboring trees. Evaluated on RSIBench-Data across six diverse domains, G"odel Forest outperforms the single-agent baseline by an average of 10.70% while reducing wall-clock time on five tasks. Ablations confirm that co-evolving shared memory yields a +7.00% gain over independent parallel search, demonstrating that collective distillation is key to scalable self-improvement. The code is available at this https URL.

---


### 175. [MLToolBench: Learning Tool-Augmented Agents for Machine Learning Development](https://arxiv.org/abs/2609.36679)

**<font color=#1a73e8>作者：</font>** Xin Yu, Lizhu Zhang, Jiamu Bai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning engineering (MLE) agents have made substantial progress, but learning through ML experimentation remains costly in time and computation. Synthetic environments reduce these costs while introducing variations in data and experimental settings that require task-specific diagnosis. Access to diagnostic tools alone does not ensure that agents learn when to use them or how to act on their findings. We introduce ToolMLBench, a suite of executable tools for data inspection, code verification, and experiment diagnosis, together with an SFT and RL pipeline for learning their use. Diagnostic calls acquire evidence whose value depends on subsequent decisions, so final outcomes provide limited guidance on which calls to reinforce. We address this challenge with SPICE, which measures how privileged context changes the likelihood of a sampled tool action and uses this difference as a turn-level reward alongside the final outcome. We train on 80 synthetic tasks and evaluate on 25 in-domain and 10 out-of-domain tasks. Providing tool interfaces and descriptions alone yields inconsistent gains across unadapted models. With the same diagnostic interface, our training pipeline raises in-domain success from 24.8% to 52.4% for Qwen3-8B and from 35.6% to 69.2% for Qwen3.5-35B-A3B. The latter also improves from 31% to 48% out-of-domain, supporting learned diagnostic tool use on held-out sources and targets.

---


### 176. [Reprogramming Vision-Language Models via Structured Prompt Reparameterization](https://arxiv.org/abs/2609.36680)

**<font color=#1a73e8>作者：</font>** Zizhao Li, Chengyi Cai, Mohammed Yaqoob Ansari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reprogramming adapts pretrained models to downstream tasks by modifying their input and output interfaces while keeping the backbone fixed. In vision-language models, existing methods mainly rely on intra-class prompt aggregation and do not explicitly model relationships among classes. However, fine-grained categories often exhibit highly overlapping attribute descriptions and strong inter-class correlation in the text embedding space, where discriminative cues lie in subtle low-variance components. We propose Reparameterized Inter-Class Visual Reprogramming (RVP), a structured framework that aggregates multiple text prompts within each class and applies residual correction across classes. We also show that CLIP-based visual reprogramming with input-independent linear output aggregation can be expressed as a linear mapping from frozen image embeddings to downstream logits, and use this view to design a structured reparameterization that models shared semantic components and class-specific differences. RVP uses only a single visual prompt and can be reparameterized at inference into a frozen backbone followed by a linear classifier, incurring nearly zero computational overhead. Across 11 few-shot classification benchmarks and four CLIP backbones, RVP consistently improves over prior visual reprogramming methods with comparable or better inference efficiency.

---


### 177. [MARCO: Multi-Round Agentic Reinforcement for Conditional Molecular Optimization](https://arxiv.org/abs/2609.36683)

**<font color=#1a73e8>作者：</font>** Shicheng Fang, Yuxin Wang, Zhuo Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular optimization is inherently iterative: a candidate is proposed, evaluated against several objectives, and revised while preserving a relationship to the source molecule. Most instruction-following models instead emit one edited molecule, forcing validity, property improvement, and similarity control into a single response. We introduce MARCO, an evaluator-grounded reinforcement-learning framework that trains molecular editors on bounded proposal--feedback--revision trajectories. MARCO aggregates shaped turn rewards into an undiscounted trajectory return for group-relative policy optimization. We evaluate two consequences of this training: Same-1 tests the trained policy under a one-response budget, while Same-5 tests whether the same policy can use verifier feedback when up to five responses are available. Across the three-objective MuMOInstruct benchmark, three Qwen backbones, and seen/unseen instruction splits, SFT-initialized MARCO obtains the highest product of property success rate and similarity in every reported primary setting. Same-5 further improves the observed score under the tested budget, while four-objective and public-checkpoint experiments test transfer across constraint sets and initialization regimes.

---


### 178. [ProgressCompass: Embodied Progress Reward Models Are Lost Without the Right Context](https://arxiv.org/abs/2609.36684)

**<font color=#1a73e8>作者：</font>** Jianshu Zhang, Keliang Wu, Chengxuan Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Embodied agents now take on ever longer tasks. For long tasks, knowing only whether a task finally succeeds or fails says little; the steps along the way matter. Progress Reward Models (PRMs) score how far a task has come at every step, and serve as dense rewards, verifiers and monitors. Yet in long tasks the current frame alone often cannot tell how far the task has come, because progress depends on what happened before. We call this problem context-dependent progress estimation. Existing benchmarks on progress estimation mostly focus on short tasks whose progress can be read from the current observation, and whether PRMs can estimate progress when context is needed remains underexplored. We therefore build ContextProgress-Bench, with 24 manipulation tasks for 120 episodes. The benchmark covers three settings: (i) State Recall, where information needed for progress appeared earlier but is not in the current frame; (ii) Sequence Tracking, where steps follow a fixed order, so progress requires knowing which steps are done and which comes next; and (iii) Recurrence Disambiguation, where look-alike frames sit at very different progress. We then run a paired diagnosis: each PRM keeps the same input format in both runs, and in one run its instruction integrates the right context. Even PRMs that read the entire history get lost in estimating progress, yet with the right context the same five models cut their progress error by 77-82%. Embodied PRMs are thus not incapable of progress estimation, but lost without the right context. We therefore propose ProgressCompass, an autonomous agentic loop that reorients an existing PRM and uses current general-purpose VLMs to supply the context the PRM needs. Wrapped in the loop, the same frozen PRM cuts its progress error by 63% and raises its rank agreement by 76%. With such a compass, PRMs estimate progress far better on longer, more complex tasks.

---


### 179. [Where Root Cause Analysis Fails: A Retrieval-Reranking Decomposition](https://arxiv.org/abs/2609.36686)

**<font color=#1a73e8>作者：</font>** Hada Melino Muhammad, Luan Pham, Laure Barrière 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying the root cause of an anomaly among hundreds of sensors is critical for preventing safety incidents and costly downtime in complex monitored systems. Existing studies evaluate root cause analysis (RCA) methods using top@k accuracy. We show that this metric has a fundamental blind spot: it conflates two failure modes, retrieval failure, where the true cause is never considered, and reranking failure, where it is considered but ranked too low. In this work, we introduce a retrieval-reranking decomposition and audit four well-known benchmarks to expose this blind spot. Our experiments show that, on benchmarks with complex faults, statistical baselines mis-rank the true cause 79-100% of the time, and graph-based methods never clearly beat the best statistical baseline, whether their causal graphs are learned on short fault windows, on retrieved candidate pools guaranteed to contain the cause, or on multi-day normal-operation data. Meanwhile, on simple benchmarks where faults manifest significantly at their origin, retrieval is nearly solved (98-100%). Guided by the decomposition, we build a two-stage pipeline combining a multi-signal retriever with an LLM reranker that, as one fixed configuration, matches or exceeds the best baseline's top@1 accuracy on all six benchmark suites (by up to +12 points), with no causal graph or labeled data required. When all methods rank the same retrieved candidates with the true cause guaranteed present, adding a short system-description document lets the reranker lead the best baseline by +7 to +18 points on every benchmark. Code is available at this https URL.

---


### 180. [CHAIN: Calibrated LLM Forecasting via Causal-Temporal Hypergraph Inference](https://arxiv.org/abs/2609.36689)

**<font color=#1a73e8>作者：</font>** Wenjin Liu, Chenxi Wang, Yue Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved significant progress in event forecasting, yet their probability outputs exhibit systematic calibration bias that varies heterogeneously across different domains and question types, undermining the trustworthiness of probabilistic outputs for decision-making under uncertainty. However, existing calibration methods typically correct probability outputs after prediction is complete, without modeling the structural sources of bias within the prediction process itself. To address this challenge, we decompose probabilistic prediction over causal-temporal hypergraphs into three stages, evidence weighting, evidence aggregation, and source fusion, and propose CHAIN, which designs stage-specific mechanisms to mitigate bias at each stage: (i) modulating the temporal decay function by causal topological distance, (ii) aggregating approximately independent causal chains via Noisy-OR after direction-aware deduplication, and (iii) driving adaptive fusion by causal coverage and directional balance. Experimental results on cross-domain forecasting benchmarks show CHAIN outperforms existing methods in expected calibration error, Brier score, and accuracy. Our project is available at this https URL.

---


### 181. [Video2Skill: From Streaming Experience to Reusable Embodied Skills](https://arxiv.org/abs/2609.36691)

**<font color=#1a73e8>作者：</font>** Jianshu Zhang, Ce Zhang, Xiyuan Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Manipulation behaviors vary widely across objects and scenes, but they share a small set of reusable skills, and planning with these skills helps embodied agents generalize to new tasks. Yet an agent can only plan with skills it knows. Recovering skills from observed experience, the inverse of planning, builds this knowledge over time and yields skill data for training future agents. Vision-Language Models (VLMs) describe individual manipulation events well, but can they organize a stream of events into reusable skills? We formulate this problem as Streaming Embodied Skill Discovery (SESD): a model watches videos in sequence and maintains a persistent skill library that shapes its later decisions. To systematically measure this ability, we introduce Video2Skill, a benchmark that covers robot tabletop manipulation and human kitchen activity and tests three core capabilities: (i) locating manipulation events in time, (ii) grouping events of the same transformation, and (iii) deciding when to reuse an existing skill or create a new one. Across 19 open-source VLMs, many models group events at near-chance level, and scale does not consistently help. Their errors depend on how perception and library updates are coupled: joint models merge distinct transformations into one skill, while models that update the library from text descriptions duplicate recurring ones. Supervised fine-tuning, including our counterfactual library-state rebalancing (CLaRe), improves grouping but exposes a deeper bottleneck: trained models consolidate familiar skills yet rarely expand the library. Their libraries stall below half the reference size, and transformations unseen in training are located in time but almost never given a new skill. Recognizing when existing skills are insufficient thus emerges as the central challenge.

---


### 182. [Normalize-Then-Precondition: A Hierarchical Approach to Marginal Scale and Interaction Geometry for LLM Training](https://arxiv.org/abs/2609.36692)

**<font color=#1a73e8>作者：</font>** Zixuan Gong, Zeyu Gan, Jiaye Teng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix optimizers have emerged as a promising direction, with Muon standing out as a prominent design. Revisiting Muon through its full-Gram representation, we observe that it jointly processes marginal-scale and interaction information. This opens an alternative way to organize geometric information hierarchically, motivating the Normalize-Then-Precondition framework. Specifically, it first uses diagonal-Gram information to construct a marginally normalized update, then applies spectral preconditioning to its directional interaction geometry. Building on this framework, we develop NormPre with NormPre-G and NormPre-L adopting global and localized spectral preconditioning, grounded in spectral-norm steepest descent and a regularized formulation followed by leading mode selection, respectively. To enable large-scale training, NormPre-G uses Newton-Schulz iterations and NormPre-L employs randomized sketching to approximate the leading interaction eigenspace. Theoretically, we establish $\mathcal{O}(T^{-1/2})$ convergence guarantees for simplified versions of NormPre. Across extensive pretraining experiments on GPT-2 Small, LLaMA and Qwen3, both variants consistently outperform AdamW, Muon and MANO under matched training budgets. Further efficiency and spectral analyses reveal the complementary strengths of two variants and characterize their performance-efficiency trade-off. We open-source our code through a GitHub repository at this https URL.

---


### 183. [Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation](https://arxiv.org/abs/2609.36695)

**<font color=#1a73e8>作者：</font>** Rui Wang, Ruijie Wang, Bo Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distillation turns knowledge distillation into a closed learning loop and offers a path toward recursive self-improvement. Without an external teacher, however, the model must determine both what information can improve its supervision and which induced changes should be learned. Existing methods typically improve teacher-generated data or select training examples in isolation, leaving the information transferred between these stages unmeasured. We introduce InFlow, a retrieval-guided on-policy self-distillation framework that models this process as potential-to-realized information flow. InFlow first retrieves potentially informative sources using certainty-calibrated hidden-state trajectories, then measures their realized effect through the Jensen--Shannon divergence between the teacher's initial and retrieval-conditioned answer beliefs. Examples with larger belief shifts are selected for on-policy distillation. Our analysis formalizes the information optimized by retrieval and selection and relates the answer-level shift to the teacher--student distillation gap. Across four open-weight language models and three knowledge domains, InFlow achieves the strongest cross-model average among the compared selection methods, with ablations supporting both stages of the framework. Our code is available at this https URL.

---


### 184. [Lost in Conversation or Lost in Translation? Diagnosing Multi-Turn Degradation in RAG](https://arxiv.org/abs/2609.36700)

**<font color=#1a73e8>作者：</font>** Pranav Handa, Ariful Azad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When conversing with large language models (LLMs), users often begin with a simple question and build towards a multi-hop question through follow-up turns. Retrieval-augmented generation (RAG) and its graph-based variant (GraphRAG) have become the dominant approaches for grounding LLM responses in external evidence, yet both are evaluated almost exclusively on single-turn, fully specified queries. We systematically investigate this evaluation mismatch through a large-scale simulation study. Building on prior work on multi-turn LLM evaluation, we transform questions from multi-hop question answering (QA) benchmarks into underspecified conversations and evaluate ten LLM assistants with eight retrieval systems across 1.5 million simulated conversations. Our findings reveal that multi-turn interaction causes widespread performance degradation, incurring relative performance drops of up to 21% and increasing unreliability by 47%, making RAG systems simultaneously less accurate and less reliable. We identify two distinct failure modes behind this degradation. Systems are either lost in translation, where conversational rephrasing distorts the retrieval query, or lost in conversation, where retrieval succeeds but the LLM fails to synthesize evidence distributed across turns.

---


### 185. [JudgeProfile: Understanding and Steering Subjectivity in LLM Judges](https://arxiv.org/abs/2609.36705)

**<font color=#1a73e8>作者：</font>** Qi Cao, Kangning Liu, Xuan Kan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are inherently subjective, often favoring different responses in pairwise comparison when neither option is objectively wrong. To study this subjectivity, we introduce JudgeProfile, a framework that dissects LLM evaluation into perception (how a judge compares two responses across specific attributes like clarity, correctness, and detail) and prioritization (how much each attribute influences the final choice). We curate SubjectiveSet, a dataset of 50,013 response pairs from 17 public data sources, evaluated by 21 LLM judges across 87 attributes. We find a hidden consensus in perception: judges frequently agree on attribute judgments even when their overall choices diverge. Building on this separation, we first characterize each judge's prioritization using attribute weights estimated from its own overall choices. These weights differ across judges even when estimated from the same attribute judgments. We then learn new weights from reference labels to adapt their decisions to a target evaluation standard. Reweighting perceived attributes improves average held-out agreement with reference labels from 66.48% to 71.97%, outperforming fine-tuning and rubric prompting. Our findings show that understanding and steering the subjectivity of LLM judges requires attention not only to what they perceive, but also to how they prioritize it.

---


### 186. [LAURA: Knowledge Distillation for Interpretable Ambiguous Clause Identification in Legal Contracts](https://arxiv.org/abs/2609.36707)

**<font color=#1a73e8>作者：</font>** Amrita Singh, Aditya Joshi, Jiaojiao Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal contracts contain ambiguities that expose enterprises to financial and legal risks. Some ambiguities allow flexible interpretation without triggering disputes, while others lead to significant legal conflicts. This makes identification alone insufficient, and interpretable rationale analysis essential. We propose LAURA, a post-training framework for interpretable ambiguous clause identification. LAURA leverages knowledge distillation with an IRAC-Unlearning prompting technique to transfer knowledge from a teacher LLM to an open-weight student model (<=1B parameters), which is then trained using a joint objective combining classification and rationale generation losses. The framework supports both legal and non-legal stakeholders in making informed decisions about which ambiguities require further attention. Extensive experiments across 7 baselines and 7 open-weight models demonstrate that LAURA with Flan-T5 (250M) delivers state-of-the-art interpretability over all interpretable baselines while matching the identification performance of the best-performing opaque baseline.

---


### 187. [CALIBUDGET: Calibration-Guided Source Allocation for Fixed-Budget Mixed-Reasoning Adaptation](https://arxiv.org/abs/2609.36721)

**<font color=#1a73e8>作者：</font>** Yupeng Chang, Yuan Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-budget adaptation from heterogeneous data sources requires deciding not only how much data to use, but how much exposure each source receives. Size-proportional rules can crowd out small sources, whereas difficulty-only rules can chase noisy estimates or allocate residual budget to nearly saturated pools. We introduce CALIBUDGET, a floor-protected, reliability-aware integer allocator that treats source exposure as an explicit adaptation variable. From small train-internal calibration splits, it combines model need, post-floor availability, and bootstrap stability, then produces exact capacity-respecting quotas without changing the model, objective, or total budget. In a controlled setting combining mathematical and commonsense data, CALIBUDGET improves CommonAvg, FragileAvg, and MacroAvg over validation-error-with-floor, the strongest matched comparator, in all three paired LLaMA-2-7B LoRA+ runs. The respective mean gains are 0.56, 0.46, and 0.41 percentage points (pp). Overall increases by 0.18 pp, whereas MathAvg decreases by 0.20 pp, exposing a coverage-retention boundary rather than a uniform gain. CALIBUDGET changes only 1.14-1.42% of the source budget but improves performance in 15 of 24 comparisons across commonsense tasks and seeds. These results suggest that small changes in source quotas can matter; example-level selection can then determine which examples fill each quota.

---


### 188. [ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation](https://arxiv.org/abs/2609.36722)

**<font color=#1a73e8>作者：</font>** Xinghao Chen, Junnan Dong, Cai Ke 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents repeatedly load reusable content, such as skills, documents, and memory entries, into the current context. Re-encoding this content for every request wastes computation. Position-independent caching (PIC) alleviates this by encoding each artifact independently and reusing its key-value (KV) states at arbitrary positions, but it incurs a quality loss relative to full-context prefill. Existing methods repair this loss by restoring global position IDs or recomputing selected tokens. In this work, we isolate the source of the loss, finding that the positional mismatch has minor effect, and independently cached artifacts retain faithful representations: reading a provided artifact stays largely accurate, and performance degrades only when the model must select among multiple artifacts. Moreover, replacing PIC's attention scores with full-prefill scores recovers performance with the cached KV unchanged, localizing the failure to the attention rather than KV recomputation. Motivated by this, we propose \textsc{Attuner}, a query-side adaptation method that learns to read a frozen artifact cache. \textsc{Attuner} inserts low-rank adapters into the query projections and is trained by distilling full-prefill distribution into the student. It trains fewer than 0.05\% of the model parameters and, at inference, requires neither cache recomputation nor a full-context reference. On Qwen3-4B and Qwen3-8B across seven benchmarks covering skills, documents, memory, and code, \textsc{Attuner} substantially outperforms prior PIC baselines in both in-domain and out-of-domain settings, matches full-context prefill quality while providing up to $3.73\times$ speedup.

---


### 189. [Routing in Gradient Space: Balanced Usage Is Not Expert Specialization](https://arxiv.org/abs/2609.36724)

**<font color=#1a73e8>作者：</font>** Yuchen Li, Mingyu Du, Zongqi Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse expert models can distribute traffic evenly while still grouping incompatible training signals within the same experts. We study routing as a gradient-partitioning problem and introduce gradient-aligned routing (GAR), whose load-normalized router objective rewards grouping observations with aligned gradients. On five multi-task text-classification mixtures, we compare GAR with task-loss-only routing, gradient-combination and gradient-conflict methods, and load-balancing losses. With a fully trainable RoBERTa backbone and classification-head experts, GAR has the highest aggregate validation accuracy, 1.07 percentage points above task-loss-only routing. With frozen DeBERTa and Qwen3-1.7B backbones and low-rank adapter experts, it again ranks first, 1.10 points above task-loss-only routing, with better-balanced expert load and higher gradient-mass purity, the share of each expert's gradient-norm mass from its dominant task; the load-balancing losses flatten load further but leave this purity near its task-loss-only level. Top-1 routing, trainable full-parameter feed-forward network (FFN) experts, and a larger backbone also show positive aggregate gains. The results distinguish expert-load balance from gradient-based routing organization and indicate the predictive value of gradient-informed routing in multi-task text classification.

---


### 190. [Deep Learning Latency Attacks and Defenses: A Cross-Domain Survey of Availability Threats](https://arxiv.org/abs/2609.36732)

**<font color=#1a73e8>作者：</font>** Zonghua Gu, Zeyu Gao, Amin Saremi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial machine learning has focused mainly on integrity, but availability is an increasingly consequential complement. Latency attacks (also energy-latency attacks) increase inference-time work, energy, or response time, causing deadline misses, throughput collapse, or resource exhaustion in vehicle controllers, interactive services, or battery-powered sensors, sometimes while preserving the nominal prediction.
This survey unifies a fragmented literature spanning perception pipelines (including physical attacks on autonomous-driving detection and tracking), input-adaptive neural inference (sponge examples, dynamic networks), and autoregressive and agentic systems (output-length, verbose-image, and reasoning denial-of-service attacks on LLMs, VLMs, mixture-of-experts models, and tool-using agents). We organize attacks by exploited computational bottleneck rather than formulation, separating what makes a computation expensive from how the attacker triggers it; the delivery channel (input, prompt or retrieved content, message, poisoning, or weight tampering) is an orthogonal attribute. Many attacks share one mechanism, intermediate-work amplification, motivating a work-budget defense abstraction; we distinguish caps on the work entering an expensive stage from caps on the results leaving it. We further analyze when a model-level cost increase becomes a system-level availability failure, which depends on critical-path share, slack, existing ceilings, accumulation, resource sharing, and fallback policy, not on the amplification factor alone.
We also provide a threat-model taxonomy, consolidated quantitative comparisons, a defense review by control mechanism, and open challenges such as standardized evaluation, physical realizability, and whole-system availability. Companion website: this https URL.

---


### 191. [Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models](https://arxiv.org/abs/2609.36734)

**<font color=#1a73e8>作者：</font>** Ayan Sengupta, Vaibhav Seth, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Distillation (KD) trains a smaller-capacity student model to imitate a larger-capacity teacher model by matching output distributions, implicitly assuming the teacher to be a reliable oracle. In large language models (LLMs), this assumption often fails: teacher predictions can exhibit high entropy and hallucinations, causing standard KD to degrade well-calibrated student priors. We propose CaRE-KD, a confidence-gated distillation framework that replaces static objectives with uncertainty-adaptive optimization. CaRE-KD has two components: a token-level loss (CaRE-Divergence) that adaptively switches between Forward and Reverse KL divergence based on teacher--student confidence, and a batch-level epistemic rejection mechanism (Revival) that suppresses updates when the teacher is more uncertain than the student. We provide a gradient-level analysis showing how this dual-granularity design induces a conditional calibration mechanism that prior static divergences cannot reproduce. Empirically, across eight teacher--student pairs and eleven benchmarks spanning instruction following, chat alignment, code generation, and mathematical reasoning, CaRE-KD delivers consistent gains over strong baselines (Skewed-KL, $\alpha$--$\beta$ divergence). Highlights include up to $+3.2$ average ROUGE-L on instruction-following tasks, $+2.1$ pass@1 on MBPP, $+1.7$ accuracy on GSM8k, and $+1.8$ accuracy on CollegeMath over the strongest baseline, with consistent gains in LLM-as-a-judge factuality (up to $+2.5$ per task over Skewed-RKL). Revival further acts as a principled, loss-agnostic plug-in that systematically strengthens existing distillation objectives by filtering epistemically unreliable teacher supervision.

---


### 192. [BiFE: Search-Efficient Discovery of CPU-Only Branching Policies via LLM-based Bi-Fidelity Evolution](https://arxiv.org/abs/2609.36735)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Bin Zhang, Zhiwei Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In branch-and-bound (B&B) for mixed-integer linear programming (MILP), branching variable selection critically impacts efficiency. Existing neural branching policies often require GPU inference, while CPU-efficient symbolic expressions lack the representational capacity for complex logic. Large Language Model (LLM)-generated code provides a flexible search space for designing lightweight branching rules with diverse algorithmic logic. To discover effective rules within LLM-based evolutionary frameworks, a core challenge arises: full B&B evaluation on real instances is prohibitively expensive, whereas offline imitation learning suffers from distribution shift. To address this, we introduce a Bi-Fidelity Evolutionary framework (BiFE). It employs low-fidelity imitation scores as a rapid pre-screener and selectively applies high-fidelity on-instance evaluation only to elite candidates, effectively balancing search efficiency with performance reliability. Experiments validate both the search efficiency of BiFE and the competitiveness of its discovered rules, which outperform the SCIP solver and other baselines on CPUs, and even surpass certain GPU-based neural policies.

---


### 193. [From Neurons to Conversation: Speech Brain-Computer Interfaces](https://arxiv.org/abs/2609.36736)

**<font color=#1a73e8>作者：</font>** Moein Khajehnejad, Forough Habibollahi, Tommaso Boccato 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Speech brain-computer interfaces (BCIs) aim to restore communication by transforming neural activity related to speech, language, or communicative intent into external outputs such as text, synthesized voice, or avatar control. Recent advances in intracortical and electrocorticographic recording, deep sequence models, and language-model-assisted decoding have enabled rapid progress, including high-performance attempted-speech decoding and increasingly naturalistic speech synthesis. Yet these achievements also reveal that speech BCIs are not simply neural-to-text decoders. They are adaptive clinical systems in which neural representations, recording hardware, decoding architectures, language priors, feedback, and user learning interact over time. Here, we synthesize speech BCI research from a system-level perspective. We first examine the neural substrates of speech and language, emphasizing their hierarchical, distributed, temporally structured, and non-stationary organization. We then examine recording and decoding choices, closed-loop adaptation, evaluation, clinical translation, and ethics. Across these domains, we highlight recurring trade-offs between signal resolution and invasiveness, low-level motor and high-level semantic targets, decoder accuracy and user agency, and language-model fluency and faithful neural evidence. We argue the next generation of speech BCIs should be evaluated not only by offline accuracy, but also by robustness across sessions, calibration burden, latency, uncertainty, usability, and safeguards against unintended decoding. By reframing speech BCIs as adaptive, user-centred systems, we outline the interdisciplinary priorities spanning speech neuroscience, neural engineering, machine learning, clinical practice, and neuroethics needed to move from proof-of-concept decoding toward reliable, expressive, and controllable communication neuroprostheses.

---


### 194. [SIPO: Unifying Reinforcement Learning with On-Policy Self-Distillation](https://arxiv.org/abs/2609.36742)

**<font color=#1a73e8>作者：</font>** Zhenrui Yue, Huimin Zeng, Yueqi Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for improving large language models (LLMs) on various tasks, yet its sparse outcome rewards lack token-level credit assignment for intermediate steps. To address this, on-policy self-distillation (OPSD) leverages a self-teacher with privileged context to provide additional dense learning signals. However, because the self-teacher is often overconfident and imposes excessive penalties on long reasoning trajectories, OPSD frequently struggles in practice. To mitigate this, we propose self-instructing policy optimization (SIPO) with a contrastive self-teacher to provide dense credit. At each iteration, SIPO samples multiple rollouts per prompt from the current policy, scores them with environment rewards, and constructs two teacher contexts for each rollout by pairing the reference answer with mistakes made within the group. The model then re-evaluates its own responses under both contexts, using the difference between the two teacher log-probabilities as token-level feedback, so that biases shared by both contexts are expected to largely cancel. The resulting objective yields a token-level advantage for every rollout: the reward still sets the main direction of each update while the self-teacher redistributes credit across tokens. Even in groups where every rollout fails and group-relative advantages vanish, SIPO still provides a learning signal. By preserving direct optimization of the task reward while providing dense, token-level feedback, this approach bridges reinforcement learning and on-policy self-distillation. Extensive experiments across multiple reasoning and code-generation benchmarks demonstrate that SIPO outperforms both RLVR and OPSD baselines without an external teacher or additional generation.

---


### 195. [EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2609.36746)

**<font color=#1a73e8>作者：</font>** Zhen Xiong, Qiaoyu Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills provide a lightweight mechanism for self-evolving agents to accumulate reusable procedural knowledge without updating model parameters. However, existing learned skill curators typically optimize curation without explicitly modeling downstream executor behavior. We show that this can cause systematic cross-executor degradation: curators trained with different executors perform best when paired with their own training executor, indicating that effective skill curation is executor-dependent. We formulate behavior-adaptive skill curation and introduce EASE, a framework that learns a single curator that adapts its decisions to different executor behaviors. EASE maintains an online behavioral profile of recent execution patterns and conditions the curator on this profile, the current trajectory, and retrieved skills to add, modify, or remove skills from an evolving repository. We train the shared curator jointly across multiple frozen executors with reinforcement learning, using retrieval-aware and behavior-aware temporal attribution to focus optimization on curation actions with observable downstream influence. Across ALFWorld, ScienceWorld, and WebShop, with executors ranging from Qwen3-8B/32B and GPT-OSS-120B to unseen Kimi K2.6, DeepSeek V4 Flash, and Gemini 3.5 Flash, EASE outperforms strong skill- and memory-based baselines without per-executor finetuning. EASE also maintains 34.5--41.0% fewer skills, improves skill retrieval by 36.3--38.7% and measured edit utility by 51.8--60.0%, and reduces deployment-time inference tokens by 9.1--14.5%. These results establish behavior-adaptive skill curation as an effective principle for building self-evolving agents.

---


### 196. [Generalizable Lifelong Model Editing via Preference Optimization](https://arxiv.org/abs/2609.36748)

**<font color=#1a73e8>作者：</font>** Dahyun Jung, Suhyune Son, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge editing enables rapid updates of specific factual knowledge in large language models (LLMs) without full retraining. However, more realistic scenarios call for a lifelong framework that handles continual updates rather than one-off modifications. In such settings, existing editing methods often overfit to target prompts, significantly degrading both the generalization of the edited knowledge and the model's general capabilities. To address this issue, we propose GLIME (Generalizable Lifelong Model Editing), which combines knowledge editing with preference optimization over generation behavior. GLIME further incorporates replay-based editing and a gradient constraint to preserve previously edited knowledge. Experimental results show that GLIME significantly improves knowledge generalization in lifelong editing settings while maintaining both editing performance and general capabilities.

---


### 197. [Group-Marginalized Self-Rewarding RL Drives Zero-Label Self-Evolving](https://arxiv.org/abs/2609.36750)

**<font color=#1a73e8>作者：</font>** Yiming Wang, Yikang Liu, Qingyuan Tian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-rewarding reinforcement learning (RL) enables large language models (LLMs) to self-evolve without human labels. Existing ensemble-based methods construct reward references from rollout groups and assign rewards accordingly. However, a response's reward representation also depends on its randomly sampled group context, i.e., the other responses in its group. Using only one group-context realization may miss desired reward signals and provide unreliable guidance for policy optimization. To address this issue, we propose Group-Marginalized Advantage Estimation (GMAE), which aggregates reward realizations across possible contexts into a response-level distribution and estimates expected advantages. Experiments across eight benchmarks and four base models demonstrate strong performance and cross-domain generalization. GMAE also exhibits stable learning, low extra cost, and good applicability across training datasets and RL backbones.

---


### 198. [cktFormer: Transformer-Based Approach for Automated Analog Circuit Design](https://arxiv.org/abs/2609.36752)

**<font color=#1a73e8>作者：</font>** Pasindu Dodampegama, Praveen Wijesinghe, Naveen Basnayake 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Circuit design is a complex and iterative process that requires expertise in electronic engineering. It involves selecting components while meeting performance constraints, such as power efficiency, cost-effectiveness, and signal integrity. However, manual design is time-consuming and prone to errors. Although other stages of the manufacturing pipeline have benefited from AI-driven optimizations, circuit design remains a bottleneck, limiting overall productivity. Generative AI and machine learning offer the potential to automate and improve this stage, boosting efficiency and accuracy. To address this, we introduce a dual transformer architecture that bridges the gap between AI and circuit design by leveraging attention mechanisms to model complex, non-sequential circuit relationships. Our approach structures netlist data into graph-based representations, enabling effective learning of circuit topology and component interactions. The system consists of two interlinked models: a node prediction model that proposes components and an edge prediction model that infers valid connections. This collaborative and decoupled design captures both component-level semantics and global structural coherence. In our experiments, this architecture outperforms recent models such as AnalogGenie and cktGNN in the validity of generated circuits. By addressing key limitations in existing methods, our work advances automation in electronics engineering and contributes a benchmark for AI-driven circuit synthesis.

---


### 199. [Drag as Evidence: Motion-Grounded Latent Recomposition for Drag-Based Editing](https://arxiv.org/abs/2609.36755)

**<font color=#1a73e8>作者：</font>** Xinyu Pu, Hongsong Wang, Jie Gui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image editors excel at semantic manipulation and visual synthesis, yet remain limited in precise spatial control, motivating the development of drag-based editing. However, existing drag-based methods often struggle to balance drag accuracy with natural, plausible, and intent-aligned generation. We propose MoRe-Drag, a motion-grounded drag-based editing method. Our key insight is to treat pixel-space warping as coarse motion evidence, and to inject this evidence into the generative sampling trajectory. Specifically, MoRe-Drag performs region-aware latent recomposition over refinement, inpainting, and anchor regions, coupled with stage-adaptive conditioning that progressively shifts from motion-grounded structure formation to semantic refinement. We further support an instruction-free interface by adapting the MLLM-based text encoder for drag-aware instruction inference. Experiments on DragBench-SR and DragBench-DR show that MoRe-Drag substantially improves drag precision over strong base editors and achieves superior drag accuracy among SOTA drag-based methods, while delivering strong semantic consistency and visually realistic results. Code and dataset will be publicly released.

---


### 200. [When Can Prefixes Compile LoRA? Exact Resource-Capped Tests for Frozen Attention](https://arxiv.org/abs/2609.36766)

**<font color=#1a73e8>作者：</font>** Joyanta Jyoti Mondal, Ibne Farabi Shihab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a fixed continuous prefix replace a given low-rank adapter while the attention head stays frozen? In this research, we show that the answer depends on the adapter's target through three conditions. First, observability: at one causal readout, every independent key--value prefix sees the content only through the query, attention partition, and value numerator, so a target that differs on two inputs with equal summaries incurs an error floor at every prefix length; norm caps extend this floor to nearly equal summaries. Second, realizability: at a common query, any prefix reduces exactly to two aggregate variables, and the norm-capped optimum is an attained second-order-cone program, also after a fixed output projection; it places two equal-norm rank-one value updates on opposite sides of compilability. Third, implementation: under affine query exposure, $2r$ signed slots approximate a rank-$r$ value update, but their values grow as $O(\epsilon^{-3/2})$, and the construction passes all 400 tolerance checks in float64 yet only 38 in bfloat16. A first-layer GPT-2 readout with fixed token and position meets the common-query condition without clamping activations; at three such heads, the capped optimum leaves 18.4\% to 74.2\% of the projected adapter effect uncompiled, with a head-dependent value--query ordering. All claims concern local approximation at one head, not whole-network equivalence.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
