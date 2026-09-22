# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

---

### 151. [OptiSkill: A Hierarchical and Evolving SkillBank for LLM-Based Optimization Modeling](https://arxiv.org/abs/2609.22987)

**<font color=#1a73e8>作者：</font>** Ruiqing Zhao, Rui Liu, Yuan Zuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated operations research (OR) modeling requires LLMs to translate natural-language decision problems into correct mathematical programs. Existing methods can improve individual formulations, but they often solve problems in isolation, retaining little reusable experience and repeating similar formulation errors. Prior memory-based approaches store examples, thoughts, or insights as references, while OR modeling requires reusable formulation skills that transfer across problem narratives and guide concrete modeling decisions. We propose OptiSkill, a skill-augmented framework that builds a hierarchical and evolving SkillBank for LLM-based OR modeling. SkillBank stores solver-verified experience as reusable skills, with Global Strategies for problem-level formulation skeletons and Step Experiences for local error-prevention rules. It is further refined through stable batch-level test-time evolution, where candidate skills are incorporated only after validation. Experiments on eight OR modeling benchmarks show that OptiSkill improves formulation accuracy across LLM backbones, outperforms strong agentic baselines, and gains further by expanding SkillBank coverage and reliability. Code and data are available at this https URL

---


### 152. [Rethinking Pivot Programming Languages in Code Language Models](https://arxiv.org/abs/2609.22988)

**<font color=#1a73e8>作者：</font>** Andor Diera, Lukas Galke Poech, Matthias Tichy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual code language models transfer skills across programming languages (PLs), but whether any PL occupies a privileged pivot position remains contested: geometric analyses point to C-family languages and Go, while behavioral evidence highlights Python. We revisit this question under controls for representational anisotropy and length variation across PLs, two confounds that compromise prior cosine-based analyses. Across three code models on multilingual competitive-programming data, we study three views of cross-PL organization: pairwise PL geometry, PL-English alignment, and pivoted retrieval through candidate PL representation spaces. The results are relation-dependent. Code-code geometry reveals structured language regions but no universal center; code-English alignment favors high-level scripting languages; and pivoted retrieval favors different intermediate spaces for code-to-code and English-to-code transfer. These findings suggest that Python's special role is better understood as English-facing affinity than as universal geometric centrality.

---


### 153. [On attention heads and bilinear forms](https://arxiv.org/abs/2609.22990)

**<font color=#1a73e8>作者：</font>** Andrew O'Desky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the symmetric and antisymmetric parts of bilinear forms in the attention heads of trained large language models. We introduce an orthogonally invariant profile map from real bilinear forms to a three-dimensional simplex and observe that profiles of trained bilinear forms accumulate near profiles of rank-one bilinear forms. We prove that the symmetric part of a bilinear form in an attention head is the sum of a hyperbolic form and a zero form for a Zariski-dense subset of query-key matrices.

---


### 154. [CrowdCue: Specialist-Cue Conditioning for Vision-Language Crowd Counting](https://arxiv.org/abs/2609.23012)

**<font color=#1a73e8>作者：</font>** Moshiur Farazi, Bekir Ciftler, Abdulhalim Dandoush 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative vision-language models (VLMs) offer a counting paradigm in which one model produces both a count and a natural-language account of the scene, yet their raw counting accuracy sits in the range of sub-million-parameter specialist regressors. The open question is whether auxiliary guidance from a pretrained specialist can lift them into useful territory, and through which channel that guidance is best routed. We evaluate Qwen2.5-VL-7B on four widely used crowd counting benchmarks (ShanghaiTech A and B, UCF-QNRF, NWPU-Crowd). Zero-shot prompting rarely produces a parseable count, so LoRA supervised fine-tuning establishes the baseline at overall MAE 81.64. Conditioning on a P2PNet-derived density heatmap as an auxiliary visual signal fails in every encoding we tested, and an adversarial-swap protocol shows the model reads the heatmap but applies it counterproductively. We propose CrowdCue, a family that supplies the same specialist's already-integrated integer count to the VLM as a discrete symbol. The text-channel variant reaches MAE 72.04. The visual-channel variant, which renders the integer as printed digits and supplies it as a second image, reaches MAE 62.65, the strongest result in this paper and well ahead of the cue-supplying specialist alone (84.45 on the same split). In the late-fusion VLM we study, the binding constraint is not the channel but the abstraction level at which the specialist signal is delivered.

---


### 155. [PINNForge: Execution-Grounded Evolutionary Design of Physics-Informed Neural Networks for PDE Solving via Large Language Models](https://arxiv.org/abs/2609.23023)

**<font color=#1a73e8>作者：</font>** Mingyang Yu, Xu Yang, Jun Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) require coordinated choices over network representation, sampling, loss construction, and optimization, while effective configurations often vary substantially across partial differential equations (PDEs). Existing automated PINN design methods can search candidate configurations, but information revealed during actual training is still used mainly for evaluation rather than to improve subsequent design, leading to repeated trial-and-error and inefficient use of training budget. We propose PINNsForge, an LLM-driven evolutionary framework for execution-feedback-based automated PINN design. PINNsForge generates diverse candidate configurations from PDE-related prior knowledge, evaluates them through actual training, and feeds high-performing designs together with accumulated execution evidence back to the LLM. Guided by observed optimization behavior, the LLM then refines, recombines, and explores coupled PINN design components, forming a continual cycle of generation, execution, feedback, and evolution. Unlike one-shot search or evaluation-only feedback, PINNsForge progressively converts training experience into improved design decisions for the target PDE. Across 25 PDE benchmarks, PINNsForge achieves the lowest mean MSE on 24 tasks compared with RoPINN, PINNsFormer, and PINNsAgent. Ablation studies further confirm the importance of the PDE knowledge base, execution feedback, and evolutionary search: removing these components increases the mean MSE to 3.74$\times$, 12.10$\times$, and 10.10$\times$ that of the full PINNsForge, respectively.

---


### 156. [WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models](https://arxiv.org/abs/2609.23033)

**<font color=#1a73e8>作者：</font>** Hyeongju Ha, Jae-Joon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models repeatedly apply a weight-shared block to increase effective depth without increasing parameter count, but the resulting T sequential recurrent-block calls per generated token substantially increase decoding latency. To address the issue, we introduce Wavefront Decoding (WFD), a training-free self-speculative decoding framework designed for looped language models. WFD exploits two properties of these architectures: intermediate recurrence outputs provide effective draft predictions, and weight sharing allows token states at different positions and recurrence depths to be processed in one batched recurrent-block call. WFD organizes these mixed-depth states into a diagonal wavefront, continuously drafting new positions at shallow depth while advancing earlier positions toward full-depth verification. Unlike the phase-separated draft-then-verify schedule, WFD therefore co-batches drafting and verification within the same recurrent calls, while rejected drafts are corrected using full-depth predictions. Across six Spec-Bench task categories, WFD achieves 2.42x speedup on Ouro-2.6B and 3.54x on Huginn-3.5B over autoregressive decoding, consistently outperforming draft-then-verify. Cross-recurrence KV sharing further reduces wavefront KV traffic and increases WFD's speedup to 4.81x on Huginn-3.5B.

---


### 157. [Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World](https://arxiv.org/abs/2609.23038)

**<font color=#1a73e8>作者：</font>** Kaixiang Yao, Xu Wang, Miao Pan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning is essential for vision-language models (VLMs) to understand and act in the physical world. Reasoning in dynamic environments requires VLMs to perceive local state transitions caused by object motion and viewpoint changes and integrate them over long trajectories to maintain an updated spatial state, yet existing VLMs remain limited in both capabilities. Current spatial training primarily focuses on static questions about object attributes and spatial relations, providing limited direct supervision for state transitions; in contrast, interaction trajectories naturally connect a preceding observation, an action, and a subsequent observation, offering direct supervision for local state transitions, while complete trajectories reveal dependencies among consecutive transitions. We therefore introduce Spatial-Interactor, a framework that trains VLMs to model physical-world state transitions through interaction, organizing this learning process into a three-level curriculum covering L1 passive world-state transitions, L2 active self-state transitions, and L3 long-horizon interaction trajectories. Accordingly, we construct the Learning from Spatial Interaction dataset (LSI-108K) from simulated and real interaction trajectories, with tasks aligned with the objective of each level. Our two-stage training strategy applies Supervised Fine-Tuning (SFT) to L1 and L2 for local transition modeling, and On-Policy Distillation (OPD) then uses privileged self-distillation: a teacher branch given segment-level transition descriptions supervises the student's on-policy CoT, helping the student learn to integrate consecutive transitions over L3 long trajectories. Experiments across multiple VLMs and spatial benchmarks show consistent gains in local transition modeling and long-horizon integration.

---


### 158. [Auditing Political Alignment in LLM Assistants: Engagement, Stance, and User Identity](https://arxiv.org/abs/2609.23039)

**<font color=#1a73e8>作者：</font>** Joan C. Timoneda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based AI systems answer political questions for hundreds of millions of people. Current audits measure what they say to an average user, but their behavior is dynamic. I argue that their political behavior is a set of policies over whom to answer, what to say, and whether to engage at all, conditional on the topic and what the system knows about the user. I call these policies the system's speech regime, which is how a developer settles the tradeoff between answering, accommodating the user, and refusing, each of which carries a cost that varies by topic. I derive a typology of five regimes from two dimensions, engagement and stance. I test six AI systems (OpenAI, Anthropic, xAI, Google, Mistral, DeepSeek) in a preregistered experiment of 7,500 multi-turn conversations that randomly assign the user's political identity across five topics: abortion, Catalan independence, climate change, Nazism, and a zero-stakes control (pineapple on pizza). Two LLM judges from different developers score every answer, validated against human coding, and refusal is treated as an outcome rather than missing data. Every system accommodates the user on the control topic, showing that political restraint is a policy. On contested topics the systems fall into different regimes: on abortion, GPT engages and mirrors every user, Gemma refuses everyone, Claude answers strongly conservative users 35 percent of the time and almost no one else, and Grok accommodates conservatives only. On settled topics such as climate change and Nazism, five systems hold firm for every user. The systems also infer the user's overall ideology, so accommodation can spill over to topics not yet discussed. A comparison of two Grok releases shows the regime changing between versions in a way current audits miss. Speech regimes matter for alignment research and for polarization, political knowledge, and the quality of democracy.

---


### 159. [Secrets That Survive Everything: Runtime Credential Exposure in Production Web Applications](https://arxiv.org/abs/2609.23042)

**<font color=#1a73e8>作者：</font>** Hemanth Gorijala  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pre-deployment secret scanning operates only on source code, never on what a production application serves. We document two exploitation chains in which Azure AD client credentials and APIM subscription keys from production JavaScript bundles enabled account takeover and mass data exposure. An authorized engagement covered approximately 2,000 enterprise web assets in one organization; 113 (5.65%) served live credentials. To quantify the shift-right gap, we built an independent Ground Truth (GT-194) of 194 secret-grade credentials through Claude Opus 4.7 extraction and manual analyst review, with the 247 LLM-extracted candidates independently validated by GPT-5.5 (Brennan-Prediger kappa = 0.676). The principal finding is structural: 13.9% of GT-194 (27 of 194) is surfaced only by manual analysis and recovered by none of the nine evaluated production scanners, a tool-agnostic blind spot the ground-truth model also misses. CryptoJS encrypted configuration separately defeats every static scanner: the credential exists only after decryption with a co-located key, reached only by runtime-aware detection. Combined coverage plateaus at 86.1%. Among the nine scanners, the best static scanner recovers 36.6% and the best runtime-aware scanner 77.8% (F1 = 0.818, McNemar p < 0.001); the ground-truth model is reported separately as a reference comparator, not an evaluated detector. On 63 of 86 secret-exposed applications (73.3%), the full Azure AD token-mint chain is co-located in one bundle, reachable from browser code. We characterize five paths by which credentials reach production undetected and present a layered runtime detection methodology and remediation framework. Recall is scoped to a single-organization Azure-heavy corpus.

---


### 160. [Enforcing Narrative Reliability and Epistemic Pacing in LLM-Driven Detective Games via Structured Knowledge Trees](https://arxiv.org/abs/2609.23043)

**<font color=#1a73e8>作者：</font>** Parsa Rahmati, Richard Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) enable open-ended dialogue in interactive games, but their non-deterministic outputs make it difficult to preserve authorial control, factual consistency, and the intended sequence of information disclosure. These challenges are particularly significant in detective games, where premature revelation or fabricated details can undermine the logic of player progression. We present a Structured Knowledge Tree architecture coupled with a tri-agent LLM pipeline for controlling dialogue in an open-ended interrogation game. The system separates knowledge retrieval, dialogue generation, and response verification to ensure that the virtual suspect reveals only information permitted by the current narrative state. We evaluate the approach through The Interrogation of Adrian Gale, a playable detective-game testbed, and a formal user study examining hallucination reduction, adherence to authored disclosure sequences, and perceived logical progression. Our results demonstrate that the structured architecture reduces critical hallucinations by 64.78% and entirely prevents premature narrative disclosure. While the strict mechanical constraints introduced usability trade-offs regarding forced conversational reveals, the system successfully enforces rigorous epistemic pacing and provides players with a clear, subjective sense of progression toward solving the case.

---


### 161. [Attributable Post-Rationalization in RAG Citations: A Controlled Reproduction and an RLVR Comparison](https://arxiv.org/abs/2609.23053)

**<font color=#1a73e8>作者：</font>** Mehedi Khan, Md. Shariful Islam Bhuyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A RAG system can hand you the right answer and cite a source it did not actually use. Models output these unfaithful citations via post-rationalization: they write the answer first and then attach a citation to whatever passage looks close enough. Search agents are now trained with reinforcement learning from verifiable rewards (RLVR), which pays them for getting the answer right. We asked whether that training also teaches them to cite honestly.
Improving an existing methodology with a required control, we compared an instruction-tuned model against three RLVR agents trained from it, on four question-answering datasets, using only free-tier Kaggle GPUs. Post-rationalization is everywhere: on Wikipedia-based questions roughly one citation in seven is unfaithful. RLVR does not fix it. The agents post-rationalize at their base model's rate, and one lands slightly worse. Rewarding correct answers buys nothing in citation faithfulness, so faithfulness has to be trained and measured on its own terms.

---


### 162. [Optimizers for Diffusion Models: A Controlled Benchmark](https://arxiv.org/abs/2609.23055)

**<font color=#1a73e8>作者：</font>** Arman Bolatov, Egor Shulgin, David Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models now match autoregressive language models on several benchmarks, while the question of how best to train them has received far less attention: the optimizer is inherited from one paper to the next and never compared. New optimizers, meanwhile, are validated almost exclusively on autoregressive pretraining, a different objective on a different loss surface. We present a controlled optimizer benchmark across four diffusion formulations, to our knowledge the first for discrete diffusion: seven optimizers (AdamW, Lion, Muon, SOAP, MARS, MARS-M, Schedule-Free) on masked diffusion (text8), uniform diffusion (QM9, and LM1B through the Gaussian duality) and Gaussian diffusion on images (CelebA-64), each on a task with published reference values. Every optimizer receives the same search protocol, and every winner is retrained at the full budget with three seeds. AdamW is a strong default but not always the right choice: it is beaten by a resolved margin on two of the four tasks, and the winner changes with the formulation, so the optimizer deserves the same care as the rest of the training recipe. Notably, methods validated on autoregressive language model pretraining transfer well: Muon, MARS-M and SOAP each beat the tuned AdamW on at least one diffusion formulation. The benchmark, all runs and every figure are reproducible end to end from the released code at this https URL.

---


### 163. [Bridging Static and Agentic RAG for Taiwanese Historical Question Answering](https://arxiv.org/abs/2609.23056)

**<font color=#1a73e8>作者：</font>** Kai-Hsin Chen, Wei-Yu Chen, Xuanjun Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) enables language models to adapt retrieval based on previously retrieved evidence, but it remains unclear whether such adaptive orchestration consistently outperforms well-designed static pipelines. We conduct a controlled comparison of agentic and static RAG for Taiwanese historical question answering, sharing the same generator and hybrid retrieval backend. Despite similar aggregate performance, the two pipelines differ on 70.83% of questions, with their advantages largely canceling out when averaged. An oracle that selects the better response per question improves the composite score by 0.2417 over the better individual pipeline, revealing substantial headroom for question-level selection. We therefore introduce a post-hoc selector that compares the two responses and their cited evidence, significantly outperforming either individual pipeline and recovering 60.34% of the oracle headroom. These results show that aggregate comparisons can obscure meaningful question-level differences between retrieval strategies, suggesting that exploiting their complementarity may be more fruitful than seeking a universally superior pipeline.

---


### 164. [FireWorldBench: Benchmarking Complex Physical World Intelligence through Coupled-Field Fire Dynamics](https://arxiv.org/abs/2609.23064)

**<font color=#1a73e8>作者：</font>** Qiang Chen, Hao Guo, Huatai Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding the physical world requires more than object recognition, scene description, and short-term visual prediction, as real-world physical systems involve multiple continuous fields, latent causal mechanisms, partial observations, and intervention-sensitive dynamics. We propose FireWorldBench, a benchmark for evaluating complex physical world intelligence in multimodal large language models and agents through coupled-field fire dynamics. Fire provides a canonical stress-test environment, where multiple interacting physical fields jointly shape observable states and temporal dynamics. FireWorldBench is organized along two complementary axes, a physical capability axis and a fire scenario task axis, jointly covering physical-state understanding, temporal dynamics, causal mechanisms, and intervention reasoning. The benchmark comprises 520 fire-world entries, including 494 controlled simulation worlds and 26 real-world-aligned event groups, spanning 47 scene archetypes across 7 environment families. These entries combine structured textual observations, multiple 2D physical-field visualizations, and 3D event-level scene modeling, yielding 9,074 text-image interleaved question-answer pairs across choice-based and open-ended report-generation formats. FireWorldBench evaluates whether models can infer latent physical states, explain underlying mechanisms, forecast coupled-field evolution, and assess intervention consequences from multimodal partial observations, providing a challenging testbed for complex physical world intelligence.

---


### 165. [From Concept Alignment to Causal Grounding: An Intervention Test of Chain-of-Thought Faithfulness](https://arxiv.org/abs/2609.23065)

**<font color=#1a73e8>作者：</font>** Qianli Wang, Yilong Wang, Dennis Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) can sound plausible yet be unfaithful to the model's underlying reasoning. Most prior work probes CoT faithfulness through input--output behavior or input attributions, leaving internal computation largely underexplored. We instead cast faithfulness as internal concept grounding: Does a large language model's (LLM) CoT reasoning engage the same internal concepts that support the LLM's direct prediction, and do the shared concepts causally drive its answer? Encoding a prediction pass and a CoT pass with a single shared sparse autoencoder (SAE), a reliable approximator of the latent concepts LLMs use, makes their internal concepts directly comparable. We introduce three correlational metrics of concept-level alignment and a causal metric, $\Delta p$, which ablates the shared concepts and measures the drop in answer probability. Across five LLMs and four datasets, concept alignment is generally high, as indicated by the correlational metrics; yet these only identify which concepts are shared, not how much they causally contribute. $\Delta p$ fills this gap: causal faithfulness varies substantially with model depth, peaking at mid-to-late layers rather than the final ones, and model scale reshapes the layer-wise profile. Moreover, causally important shared concepts are not always verbalized in the CoT. These dissociations suggest that faithfulness cannot be reliably assessed from surface-level or representational correspondence alone; assessing it requires causal tests of whether the internal concepts underlying a CoT actually drive the model's prediction.

---


### 166. [Tutoring Large Language Models to be Domain-adaptive, Precise and Safe](https://arxiv.org/abs/2609.23071)

**<font color=#1a73e8>作者：</font>** Somnath Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This thesis proposes a framework for "responsible intelligence" to address AI's critical challenges in safety, ethics, and cultural sensitivity. It advances three core areas: First, it improves domain adaptation in specialized fields using active learning and graph-based knowledge to reduce hallucinations. Second, it enhances ethical rigor via a novel decoding-time alignment mechanism that proactively blocks harmful text generation in real-time. Finally, it ensures cultural and multilingual safety through language-specific steering that respects diverse linguistic and social norms. Ultimately, this work provides a blueprint for building next-generation AI that is contextually knowledgeable, ethically sound, and culturally adaptable.

---


### 167. [MolSC: Leveraging Substituent Contributions to Enhance Fine-grained Molecular Understanding in LLMs](https://arxiv.org/abs/2609.23073)

**<font color=#1a73e8>作者：</font>** Hyuntae Park, Sooyeon Kim, Jiwon Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in natural language processing have led to molecular Large Language Models (LLMs) with strong performance across diverse chemistry tasks. However, they still struggle to capture fine-grained structure-property relationships, particularly how small, localized modifications alter a molecule's behavior. To address this limitation, we introduce MolSC, a dataset of substituent contributions, defined as property changes induced by attaching specific substituents to molecular scaffolds. Curated from manually annotated bioactivity records, MolSC spans structural-alert liability, target-specific bioactivity, and physicochemical descriptors, and contains 181K substituent-level examples for training. We further propose MolSC-Bench, a held-out evaluation benchmark of 1,541 examples disjoint from MolSC at the scaffold, substituent, and molecule levels. Our experiments show that existing molecular LLMs and strong proprietary models such as GPT-5.2 and Gemini-3-Flash show limited reliability in substituent contribution prediction. In contrast, training on MolSC substantially improves this ability and achieves strong performance across diverse downstream molecular tasks. These results highlight substituent contribution learning as a key component of fine-grained molecular understanding.

---


### 168. [Directing large language models to follow the letter or spirit of the law](https://arxiv.org/abs/2609.23083)

**<font color=#1a73e8>作者：</font>** Peng Qian, Andrew Li, Sam Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The distinction between the spirit and letter of the law is a central issue across research and everyday life, and a growing concern for building safe, intelligent machines. What is this distinction based on, and how can we develop machines that follow the intention behind a rule? We used targeted adaptation that made large language models prioritize the spirit or letter of the law. With minimal modifications, our method significantly changed LLM behavior across diverse measures, novel vignettes, real-world scenarios, and influential legal cases. An analysis of model internals revealed a low-dimensional space with three interpretable dimensions matching a formal pre-specified framework for the geometry of legal concepts. These findings show how legal thought in LLMs may be organized and directed.

---


### 169. [Neural Spectral Capacity: Measuring and Designing Architectures from Network Specification Alone](https://arxiv.org/abs/2609.23087)

**<font color=#1a73e8>作者：</font>** Chenyu Zhu, Ruoyu Zhao, Zhichao Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern Transformer design and compression both reduce to allocating capacity under a budget. The standard scalars for these decisions, #Params and #FLOPs, capture size and compute but not architectural structure: two architectures with identical parameter budgets but different depth-width, head, or FFN allocations receive identical scores yet behave differently. We propose Neural Spectral Capacity (NSC), a closed-form scalar grounded in the singular-value spectrum of each weight matrix. Under standard random initialization, the Marchenko-Pastur law renders NSC computable from the architectural specification alone, with no model instantiation, data, or gradients. Its layer-wise additive structure admits NSC-DP, an exact dynamic-programming solver returning the architecture globally maximizing NSC under resource constraints in seconds on a CPU -- a guarantee that black-box search over existing training-free proxies cannot provide. Empirically, NSC outperforms #Params, #FLOPs, and representative training-free proxies in ranking across seven Transformer and CNN families (on FlexiBERT, $\tau = 0.505$ on pairs differing in #Params by less than 10%, where #Params collapses to 0.082); NSC-DP discovers a Transformer-XL architecture on WikiText-103 that beats the human-designed baseline in 2 seconds; and prunes LLaMA-7B to the best 5.7B model across eight commonsense reasoning tasks without any calibration data, about 5900x faster than the strongest training-free proxy baseline.

---


### 170. [OmniEdu: Open Foundation Models for Learning and Teaching](https://arxiv.org/abs/2609.23088)

**<font color=#1a73e8>作者：</font>** Hao Liang, Qihan Lin, Meiyi Qiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Educational foundation models must solve problems, understand curriculum structure, diagnose learner difficulties, and provide appropriate instructional support. Existing educational language models often focus on either problem solving or tutoring, with training mixtures organized by source or task rather than capability. We present OmniEdu, an open family of foundation models for K-12 learning and teaching. Its instruction-tuning corpus combines over 100 educational resources and general instruction sources, organized around four capabilities: subject competence, curriculum grounding, diagnostic reasoning, and pedagogical action and scaffolding. Our pipeline integrates deterministic cleaning, semantic auditing and rewriting, task-specific quality scoring, token-budgeted diversity selection, and pedagogical instruction assignment. It yields 69,999 examples and 15.96M supervised response tokens, including 60,951 education-specific examples. We fine-tune 4B, 9B, and 27B models and evaluate curriculum grounding, K-12 problem solving, and pedagogical tutoring, alongside general capability. Education-oriented tuning consistently improves all three educational benchmark groups across model scales. OmniEdu-27B achieves 63.12% EM and 76.69% F1 on K12-Bench, 85.89% on MathFish, 86.95% on EDUMATH, and 78.74% in MathTutorBench's Scaffold setting. It also achieves the highest Teaching average on LongTutor among the evaluated models, at 3.02. These results demonstrate the value of curated, capability-balanced supervision for adapting general language models to educational tasks spanning problem solving, curriculum understanding, and instructional support.

---


### 171. [How Did Writing Change At CHI? Analyzing 44 Years of CHI Writing Before and After the Introduction of Large Language Models](https://arxiv.org/abs/2609.23090)

**<font color=#1a73e8>作者：</font>** Thomas Kosch, Robin Welsch, Michael Hedderich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The availability of Large Language Models (LLMs) reshaped scientific discourse at a linguistic level. LLMs are assumed to homogenize academic writing, flattening it into a single generic lexical register. To understand how CHI writing has changed since the public release of LLMs, we analyzed full texts of 14,262 archival papers across all 44 CHI proceedings from 1982 to 2026, measuring readability, register, lexical diversity, and marker words typically produced by LLMs. We find that prose did not homogenize, while vocabulary grew more varied, and sentence rhythm remained irregular. CHI prose changed more between 2016 and 2026 than in other decades toward greater density, and reading ease has declined since 2022. The word-level shift began before any author used LLMs, so LLMs did not start the change but accelerated it. Reflecting on the history of CHI papers, we discuss what may have caused changes in prose and how LLMs accelerated them.

---


### 172. [An LLM-Assisted AutoML Framework for Intrusion Detection in IoT Networks](https://arxiv.org/abs/2609.23097)

**<font color=#1a73e8>作者：</font>** Li Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) systems are increasingly deployed in smart homes, transportation, energy systems, and critical infrastructure. This broad connectivity improves service intelligence, but also enlarges the attack surface of IoT networks. Machine Learning (ML)-based Intrusion Detection Systems (IDSs) are widely used to identify malicious network threats and protect IoT systems, but developing effective ML-based IDS models often requires human expertise and repeated manual decisions on many procedures, including data pre-processing, feature selection, model selection, and hyperparameter tuning. Automated Machine Learning (AutoML) reduces this burden by automating steps of the ML pipeline using optimization techniques, but conventional AutoML methods can consume substantial optimization time because they explore broad candidate model families and large hyperparameter spaces. This paper proposes a Large Language Model (LLM)-assisted AutoML framework for IoT intrusion detection. The proposed framework uses an LLM as a policy generator that converts dataset profiles into bounded and validated AutoML policies for automated data balancing, automated feature engineering, and Combined Algorithm Selection and Hyperparameter Optimization (CASH). Under an equal 10-trial budget, the proposed LLM-assisted policy achieves higher weighted test F1-score than traditional AutoML using the Tree-structured Parzen Estimator (TPE) on both datasets, reaching 99.680% on CICIDS2017 and 99.186% on IoTID20. Relative to the broader 30-trial Traditional AutoML-TPE baseline, the 10-trial proposed method reduces optimizer time by 63.7% and 49.9%, respectively, while achieving slightly higher F1-score. These results show that a bounded LLM policy can improve the quality of a low-budget AutoML search while retaining a clear efficiency advantage relative to a larger conventional search budget.

---


### 173. [Deciphering the Babel of Play: A Human-AI Collaborative Approach for Large-Scale Cross-Language Analysis of Game Reviews](https://arxiv.org/abs/2609.23104)

**<font color=#1a73e8>作者：</font>** Zixiaofan Yang, Chang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present a large-scale cross-language analysis of game reviews using a human-AI collaborative framework that combines quantitative screening with multilingual large language models (LLMs). Starting from 17 million Steam reviews across 30 languages and 2,000 top-selling titles, we select 28 games with notable cross-language rating patterns. We then apply LLM-assisted content analysis to 442,162 reviews spanning 17 languages, with human researchers guiding codebook development and interpreting the results. Our findings reveal differences in both the aspects language communities prioritize and how they evaluate them, highlighting the roles of narrative expectations, game mechanics and stability, localization quality, cultural proximity, and perceptions of developers and publishers. We also identify rare cases of cross-language consensus. This work offers empirical insights into cross-cultural game evaluation and a scalable methodological approach to multilingual content analysis that preserves human interpretation.

---


### 174. [From Inference Engine to Inference Control Plane: Connecting vLLM, llm-d, and the Evolution of Efficient Distributed LLM Serving](https://arxiv.org/abs/2609.23130)

**<font color=#1a73e8>作者：</font>** Twinkll Sisodia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference is evolving from an engine-local optimization problem into a distributed control problem involving reusable state, phase placement, heterogeneous accelerators, networking, autoscaling, reliability, and service-level objectives. This paper connects that transition across peer-reviewed systems research, open-source implementations, and documented production studies. It treats vLLM and llm-d as complementary layers: model-serving engines optimize execution through mechanisms such as PagedAttention, continuous batching, kernels, quantization, and parallelism, while an inference control plane can optimize where, when, and under what policy execution occurs across a fleet. The contribution is synthesis rather than a new benchmark; all reported performance and deployment results remain attributed to their original sources. The combined evidence suggests that the scarce resource in modern inference is shifting from raw FLOPs alone toward managed state, placement, network movement, reliability, and decision quality. We propose an Inference Execution Planner that selects feasible execution plans rather than only endpoints, including aggregated versus disaggregated topology, KV source and transfer action, hardware variant, routing/admission policy, and slower scaling decisions. We also provide a source-local benchmark atlas, a bottleneck-migration taxonomy, practical deployment guidance, an evaluation framework based on SLO-goodput, and research questions for agentic, multimodal, heterogeneous, and resilient inference.

---


### 175. [QwenVLConnector: A Fast, Unified Medical VLM Chatbot for Fine-Grained Clinical Perception and Text Generation](https://arxiv.org/abs/2609.23139)

**<font color=#1a73e8>作者：</font>** Le Thien Phuc Nguyen, Thien Nguyen, Thanh-Huy Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most medical vision-language models (VLMs) excel at open-ended report generation and VQA but provide limited support for structured, fine-grained clinical perception within a unified interface. We present QwenVLConnector, a Qwen2.5-VL-based medical chatbot that unifies classification, multi-label classification, textualized detection, counting, regression, and free-form report generation under a single next-token objective. Our key component is a lightweight dense multi-layer Connector that aggregates low- and high-level visual features, aligns them through the pretrained vision Merger, and fuses them with the final visual representation without increasing sequence length. This design enriches visual tokens with complementary spatial and semantic cues while preserving efficiency. On FLARE-2D, QwenVLConnector improves detection F1 from 0.55 to 0.85, raises single-label classification from 0.37 to 0.51, and boosts report-generation GREEN by up to 18.3 points over the Qwen2.5-VL baseline. We further explore multimodal in-context learning for report generation, showing additional improvements without updating model parameters. Overall, QwenVLConnector offers a unified and efficient framework for combining structured medical perception with open-ended clinical text generation. Our code can be found at this https URL.

---


### 176. [CraftBench-UE: Deterministic Evaluation for Coding Agents in Unreal Engine](https://arxiv.org/abs/2609.23142)

**<font color=#1a73e8>作者：</font>** Shutong Wu, Kevin Calderone, Andy Tsen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building gameplay features in a game engine requires more than code, as code that compiles and runs does not necessarily implement the requested gameplay. We introduce CraftBenchUE, an evaluation harness that runs agents in an isolated Unreal Engine environment, reconstructs their saved submissions in fresh projects, and applies deterministic build, asset, and runtime checks without an LLM judge. Based on the harness, we built a benchmark consisting of 70 tasks spanning C++ source, Blueprint assets, and editor scripting. We evaluate seven models under two editor-tool configurations, with a file-and-shell baseline on C++ tasks. We further pair tasks that specify the same gameplay and use the same runtime tests, but require C++ and Blueprint as the deliverables. Across the 10 paired tasks, C++ completion rates exceed Blueprint by 30.0 and 42.9 percentage points in the two tool configurations. Among on-time Blueprint submissions in this paired set that pass asset checks, 42.2% and 50.0% fail explicit runtime assertions. These submissions satisfy asset requirements but fail the required gameplay tests. We will release the harness, task benchmark, and our trajectory findings with the report.

---


### 177. [Chronologic: Measuring Language Models' Ability to Represent the Past](https://arxiv.org/abs/2609.23178)

**<font color=#1a73e8>作者：</font>** Ted Underwood, Ziliang Qiu, Sarah Griebel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are appealing tools for research on the past. But to trust the evidence a model provides, researchers need to know whether its responses fit the period represented. Validation is challenging, because this is not a task living people ordinarily perform, and because many questions have multiple correct answers. We use historical texts to develop a benchmark for a model's representation of English-language contexts 1831-1930, relying on pairwise comparisons to multiple ground truths and strong distractors to score the hardest questions in an appropriately graduated way. We find that generative tasks are harder than discriminative ones; in fact, reasoning models can typically discern the weakness of their own generated answers. While models pretrained exclusively on historical text lead the pack when evaluated by answer likelihood, they cannot compete with commercial models in free generation. None of the models we tested represent historical contexts in a fully persuasive way yet, but progress toward that goal is evident.

---


### 178. [CausalWM: Causal Chain-of-Thought Reasoning for Embodied World Model](https://arxiv.org/abs/2609.23184)

**<font color=#1a73e8>作者：</font>** Ziming Xu, Shuang Liang, Ruobing Han 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied world models learn to predict future physical dynamics from visual observations and control signals, where physical knowledge is implicitly entangled within latent representations. We introduce CausalWM, a 16B embodied world model that performs explicit causal chain-of-thought reasoning before future video prediction. CausalWM organizes useful variables into a reasoning trajectory, allowing the model to progressively capture causal dependencies underlying physical evolution. To train CausalWM, we collect 31K hours embodied data and develop a three-stage paradigm consisting of large-scale video pre-training, causal CoT mid-training, and multi-objective RL post-training. Despite using only a limited set of supervised CoT variables, CausalWM exhibits emergent in-context learning capabilities, enabling contextual visual feature guidance and efficient few-step generation. CausalWM achieves state-of-the-art performance across language-conditioned, action-conditioned, single-view and multi-view benchmarks, including Top-1 performance on TriWorldBench leaderboard.

---


### 179. [LLMs as Linguistic Chameleons: Decoupling Semantics and Structure for Privacy-Preserving Communication](https://arxiv.org/abs/2609.23193)

**<font color=#1a73e8>作者：</font>** Yuzhu Mao, Liang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) APIs become increasingly integrated into privacy-sensitive workflows, ensuring inference-time privacy without compromising task utility remains a major challenge. Existing approaches preserve most of the original semantic content to maintain downstream performance, but this also leaves exploitable cues for reconstructing the original text. This work investigates semantic decoupling, which replaces original semantics with alternative content while preserving the structure needed for LLM reasoning. Based on this idea, we propose CROSS-MAP, a bidirectional framework that maps private inputs into a different semantic domain before inference and recovers the corresponding outputs afterward. Local models are trained with multi-objective optimization to maximize semantic divergence in the mapping stage while minimizing semantic inconsistency in the recovery stage. Experiments show that CROSS-MAP reduces reconstruction success across multiple attack settings while outperforming existing baselines in utility.

---


### 180. [Do Not Trust the Benchmark: Limitations of General LLM Rankings and a Case for Task-Specific Evaluation](https://arxiv.org/abs/2609.23201)

**<font color=#1a73e8>作者：</font>** Danial Amin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark scores increasingly influence the development, marketing, and selection of large language models (LLMs). Yet an overall score is interpretable only in relation to the system tested, the questions included, and the conditions of evaluation. This perspective examines five connected limitations of general LLM rankings: differences between evaluated and publicly available systems; commercial incentives and dependencies in external evaluation; benchmark saturation, defective tests, and data contamination; models exploiting scoring procedures; and the limited relevance of general scores to users' tasks. Documented cases illustrate why these problems require different responses. I argue for evaluation procedures that disclose the tested configuration, validate questions and successful task completion, report performance alongside cost and execution time, and make the scope of generalization explicit. I then discuss \textbf{Isotanta}, a crowdsourced benchmarking platform, as a practical example of contributed questions and repeated evaluation. A larger question pool may improve task coverage, while repeated sampling can improve the stability of estimates on that pool; neither guarantees validity or personalization. The paper distinguishes the platform's current shared ranking from proposed task-specific and user-provided evaluations. Its central argument is that model selection requires evidence about performance on the intended work, not simply a high position on a general leaderboard.

---


### 181. [Euston: Training Away Mathematical Sycophancy Without Losing the Mathematics](https://arxiv.org/abs/2609.23205)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models are trained to produce solutions, not to refuse them, and this bias persists when the problem they are handed is false. Asked to prove a corrupted theorem, a strong model will typically comply and produce a confident derivation of something untrue. We present Euston, an 8B mathematical claim-verification model trained to resist exactly this. Training data were generated with GraphSynth, a probabilistic factor-graph generator that couples attribute-level diversity to decode-time structural masking and span-synchronized verification, yielding 3{,}026 matched true/corrupted statement pairs (6,052 statements) drawn from arXiv papers spanning 2010--2025. We fine-tuned DeepSeek-R1-8B with GRPO under a rule-based, zero-API reward for 189 steps on four H100 GPUs. On a balanced 200-true/200-false held-out split, balanced accuracy rises from 29.50% to 63.75% and the discrimination gap---the difference between the rate of calling false statements false and the rate of calling true statements false moves from -0.5% (z=-0.1) to +27.5% (z=+6.0). Critically, the gain is not purchased with general mathematical ability: AIME 2026 accuracy under official semantics is 65.00% against a 69.17% base, a difference of -4.17% that is not statistically significant, whereas an earlier run of the same recipe on a smaller GraphSynth corpus collapsed to 40.00%. Median response length also falls from 19,217 to 18,296 tokens and the truncation rate from 25.8% to 8.3%, so the improvement does not come from thinking longer. We report the result together with the confounds that bound its interpretation, principally the all-false composition of the official evaluation sets and the low precision implied at realistic error prevalence.

---


### 182. [Triggers and Diagnostics for LLM-Based Interpretability Failures in Active Inference Agents](https://arxiv.org/abs/2609.23215)

**<font color=#1a73e8>作者：</font>** Param Raval, Rohit Shenoy, Archana Vaidheeswaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM explainers are increasingly attached to autonomous agents as runtime oversight, with operators reading a generated account of the agent's beliefs and actions rather than its internal state. We audit the account itself, pairing an Active Inference (AIF) agent that tracks German grid demand and adjusts generation with an LLM explainer on three backends (GPT-4o, Claude-3-Opus, Gemini), and probing the pair with three black-box triggers. Corrupting the observation stream by 600 MW per step moves the agent's posterior by 490 MW, roughly 0.9% of grid capacity. None of the 30 explanations produced during the injection flag anything under a stated rubric, and each narrates the corrupted belief fluently. On timesteps where the agent takes an objectively wrong action, all three explainers produce a sycophantic rationalization 80-95% of the time (n = 20 per backend). Attacker-controlled text in the observation metadata field steers the explainer, with susceptibility differing by provider and data exfiltration succeeding on all three. We propose mitigations for each failure but do not evaluate them. In every failure we observed, the explanation was fluent and wrong. Moreover, nothing in the explainer architecture checks whether an explanation is true before an operator acts on it. Testing the explainer therefore belongs in any audit of an agentic deployment.

---


### 183. [CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning](https://arxiv.org/abs/2609.23257)

**<font color=#1a73e8>作者：</font>** Minkyoung Kim, Daeun Ji, Yohan Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting underpins critical decision-making across diverse domains. While large language models (LLMs) offer promising reasoning capabilities, existing LLM-based time series forecasting approaches either reduce them to numerical predictors that bypass their strengths, or allow direct forecast generation that destabilizes predictions in non-stationary settings. We introduce CTRL, a framework that decouples semantic reasoning from quantitative prediction. A frozen backbone generates base forecasts, while specialized LLM agents function as controllers that analyze backbone prediction errors through decomposed trend, seasonal, and irregular components, grounding reasoning in interpretable temporal structure. Each agent outputs compact control signals that a lightweight residual decoder translates into forecast corrections. CTRL incorporates label-free test-time adaptation that detects distribution shift from input statistics alone and readapts control signals with only 3-24 LLM calls via caching. CTRL is explicitly designed to improve robustness under non-stationary temporal dynamics and distribution shift, while remaining competitive on highly stationary time series where adaptive correction provides limited additional benefit.

---


### 184. [Judging a Review by its Cover: A Reliability Analysis of LLM-based Peer Review Evaluation Metrics](https://arxiv.org/abs/2609.23264)

**<font color=#1a73e8>作者：</font>** Shakiba Amirshahi, Sajad Ebrahimi, Hai Son Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer-review evaluation is increasingly being automated with LLM-as-a-judge metrics, but this creates a measurement risk. A review may receive a high score because it is fluent, organized, and polished, rather than because it provides a strong evaluation of the paper. This risk is especially important in AI-assisted reviewing, where reviewers may use LLMs to improve clarity or presentation while preserving the underlying judgments. We propose a statistical framework for testing whether peer-review evaluation metrics capture substantive review quality beyond surface-level linguistic form. The framework compares original human reviews with faithful LLM rewrites that preserve the same evaluative content while changing wording and presentation. Using a dataset comprising 4,044 meaning-preserving rewrites derived from 674 human reviews from ICLR and NeurIPS, we evaluate 29 content-oriented peer-review evaluation metrics drawn from four prior works through complementary tests of surface sensitivity and robustness. Although these metrics are intended to capture review properties beyond surface-level, writing-dependent characteristics, we find that sensitivity to rewriting is widespread. Under our primary analysis, 23 metrics assign significantly different scores to reviews whose evaluative content is preserved, while only six satisfy our robustness criterion. The patterns are largely consistent across two LLM judge models, suggesting that the issue is not specific to a single judge. These findings show that many peer-review evaluation metrics partially conflate review quality with linguistic presentation, and indicate that robustness to meaning-preserving rewriting should be validated before such metrics are used to compare human-written, AI-assisted, and AI-generated reviews.

---


### 185. [AI Persona, Service Consumption, and User Intent Entropy: Field Experimental Evidence from an LLM Platform](https://arxiv.org/abs/2609.23274)

**<font color=#1a73e8>作者：</font>** Junjie Li, Xiaofan Li, Lauren Xiaoyuan Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Problem definition: Firms deploying large language model services must decide how their AI communicates, not just what it can do. We examine how a relational persona - warmer, more empathetic and more engaging than a non-relational persona - affects service consumption and the evolution of user objectives. Methodology/results: In a randomized field experiment with 9,586 newly registered users, we hold the underlying model and service capabilities constant. The relational persona increases interactions (sessions, +8.1%; duration, +10.6%; chat rounds, +24.2%; intent entropy, +5.8%) and outputs (files, +12.3%; distinct goals, +12.1%). Effects vary by entry intent. First-session effects are insignificant for Task Execution users. Socialization and Knowledge Exploration users show similar increases in chat rounds: Socialization increases intent entropy without more outputs, whereas Knowledge Exploration increases outputs without higher intent entropy. Modeling intent dynamics as a transition process, we find higher intent transition entropy for Socialization (+11.8%) but higher intent continuation probability for Knowledge Exploration (+12.8%), suggesting greater conversational breadth and persistence, respectively. In subsequent use, the relational persona increases aggregate chat rounds and outputs across all entry intents. Session count rises by 12.2% for Task Execution and 49.4% for Socialization, but not significantly for Knowledge Exploration. Effects on session count and intent entropy strengthen over time, whereas output effects remain stable. Managerial implications: AI persona is an operational design lever, not merely a presentation feature. Because more interactions do not uniformly generate more outputs, firms should evaluate interactions and outputs separately and consider matching persona to user intent, especially when added interactions consume costly computing resources.

---


### 186. [ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs](https://arxiv.org/abs/2609.23314)

**<font color=#1a73e8>作者：</font>** Junyoung Park, Jungwook Choi, Mingu Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLMs with QK-normalization, gated attention, learned attention sinks, or logit softcapping exhibit weaker persistent attention sinks, on which existing KV cache eviction methods primarily rely. We observe that across these models, weaker sinks co-occur with greater value-vector dispersion relative to key-vector dispersion. Motivated by this value-side dispersion, we present ValueDiff, a value-geometric eviction that ranks tokens by the L2 deviation of their value vectors from the cache mean. The same score arises as the minimal-disturbance eviction under a max-entropy assumption about future attention. We evaluate under fixed cache budgets, with eviction at every block boundary during prefill and at every decoding step during generation. On RULER at a tight 2k token budget, ValueDiff retains 88--99\% of dense across seven sink-suppressed models (best on 6 out of 7). On LongBench at the 4k budget, ValueDiff averages 92\% retention across sink-suppressed models versus 83\% for the strongest prior baseline. On MATH-500, ValueDiff is the strongest non-dense method on every sink-suppressed model tested at the 25\% cache budget, outperforming prior methods by up to $\sim$20 points on gated-attention models. Across all three benchmarks, value geometry emerges as the more reliable query-invariant eviction signal for sink-suppressed models.

---


### 187. [CSC: Calibrated Simplicity for Conflict-Aware Social Bot Detection in the LLM Era](https://arxiv.org/abs/2609.23320)

**<font color=#1a73e8>作者：</font>** Yipeng Qian, Pengjie Zhao, Chaoxi Niu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Social bot detection is essential for protecting online platforms from misinformation amplification, coordinated manipulation, and distorted public discourse. However, large language models have made social bots much harder to detect from text alone because semantic camouflage is now cheap, fluent, and scalable. The resulting challenge is modality conflict: an account may look human-like in semantics while remaining suspicious in graph structure, profile attributes, or cross-modal consistency. Recent graph-based detectors tackle this limitation by adding graph-side complexity, such as sparse prototype selection, adaptive gating, or architecture-specific control logic, yet our experiments suggest that complexity alone is not the most reliable way to resolve such conflict.
We therefore propose CSC, a calibrated-simplicity framework for conflict-aware LLM-era social bot detection. The framework combines three design choices: a simplified prototype-guided graph expert that retains useful structural biases while removing unstable graph-side heuristics, calibrated simplex-constrained fusion that aligns heterogeneous confidence spaces before late fusion, and a lightweight inconsistency expert that models cross-modal disagreement. Experiments on TwiBot-22, TwiBot-20, and MGStBot-large show that \textsc{CSC} improves calibrated operating-point decision quality while remaining competitive across external benchmarks. Further analyses show that calibration improves confidence reliability, the inconsistency expert mainly provides localized corrections in high-conflict or near-threshold regions, and simplified graph-side control yields a better stability-cost trade-off. A targeted semantic-camouflage stress test further shows that replacing selected bot text with matched human text sharply degrades the standalone text expert while leaving graph and fused evidence stable on a balanced challenge set.

---


### 188. [MinCU: A Fine-Grained Benchmark for Grounded Minimal-Change Understanding in Image Pairs](https://arxiv.org/abs/2609.23336)

**<font color=#1a73e8>作者：</font>** Chaoqian Mu, Wenhao Wu, Zichen Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localizing and describing fine-grained differences between near-identical images is a critical yet underexplored capability for multimodal large language models (MLLMs). Existing benchmarks largely assess semantic comparison or single-image grounding in isolation, without jointly requiring faithful description and physical localization. To bridge this gap, we introduce MinCU, a benchmark for grounded minimal-change understanding, where each sample consists of an image pair differing by a single atomic variation in object category, attribute, count, or spatial position, and models are evaluated on their ability to describe the change, localize the changed regions, and identify the changed entity. We further propose Semantic-Guided Implicit Spatial Anchors (SG-ISA), a structured autoregressive method that decomposes prediction into a Think-Locate-Describe sequence. SG-ISA first predicts a semantic cue for the changed concept, then uses discrete spatial anchors as an implicit localization scaffold, and finally generates the change description together with the grounding box. Experiments reveal that even the strongest closed-source MLLMs and recent R1-style reasoning models struggle on MinCU, with most failing to jointly produce accurate descriptions and grounding boxes. Compared to the previous chain-of-thought method, fine-tuning with SG-ISA yields substantial joint improvements in grounding accuracy and description quality while reducing reasoning-token overhead by approximately 26%. These results suggest that an implicit intermediate spatial interface can be more effective than relying solely on model scale for grounded dual-image understanding.

---


### 189. [AniPrO: Interpretable Anime Image Provenance Detection via Multi-Dimensional Semantic Reasoning](https://arxiv.org/abs/2609.23345)

**<font color=#1a73e8>作者：</font>** Yan Liu, Baoxiang Huang, Zi'an Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative AI becomes increasingly used in anime-style image creation, distinguishing human-drawn, AI-inpainted, and text-to-image images is important for copyright attribution, visual provenance, and content governance. Existing AI-generated image detectors mainly target real-world photographs and often overlook anime-specific cues such as flat coloring, exaggerated structures, and artistic line control. To address this gap, we propose AniPrO, a multi-dimensional description-enhanced framework for interpretable anime image provenance. Built upon AnimeDL-2M, AniPrO contains 15,000 balanced samples from a 35,000-image candidate pool, covering Real, Inpainting, and Text2Image categories with structured five-dimensional descriptions. We further introduce AniPrO-SFD-Bench and AniPrO-MFR-Bench to evaluate provenance detection from statistical feature discrimination and multimodal fusion reasoning perspectives. Experiments show that structured semantic guidance reveals systematic AI-generation biases, such as the gap between global visual plausibility and local detail coherence, and improves the detection of challenging inpainting samples. The dataset and code will be released at: this https URL.

---


### 190. [TicTacBench: Benchmarking Timing Closure Capabilities of Coding Agents](https://arxiv.org/abs/2609.23363)

**<font color=#1a73e8>作者：</font>** Bowei Wang, Zhigang Fang, Zhijie Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have led to the emergence of coding agents capable of performing complex engineering tasks, including register-transfer level (RTL) design and optimization. Existing RTL benchmarks mainly evaluate functional correctness and performance, power, and area (PPA) of the generated RTL designs, leaving agents' ability for \emph{timing closure} under-evaluated. We propose TicTacBench, a benchmark specifically designed to evaluate coding agents' capabilities for RTL-level timing closure under post-place-and-route (post-PnR) evaluation. TicTacBench contains 30 diverse tasks, each provided with a suboptimal RTL design, realistic timing constraints, functional equivalence verification, and timing reports. With over 300 runs of coding agents driven by 8 frontier LLMs, we find that even the best agent can only close 53.3\% of tasks with 7.18\% area-delay product (ADP) degradation and 8.83\% energy-delay-squared product (EDDP) improvement on average. We identify common failure categories that explain why agents fail to close timing. Then we propose TicTacSkill, a new method that guides agents to follow standard timing-closure procedures and improves the Timing Closure Rate by 9\%. These results suggest that while coding agents have made significant progress in RTL design, their timing-closure capability still has substantial room for improvement.

---


### 191. [Machine-Interpretable Information: Compiling Documents into Searchable and Readable Protocol States](https://arxiv.org/abs/2609.23371)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Dejing Dou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models interface with external knowledge through raw natural language. In retrieval-augmented systems, this creates a persistent index-payload schism: dense vectors enable searchable routing, but models must re-ingest lengthy text payloads for reasoning at O(N^2) attention cost. Existing compression methods further produce private states tied to specific architectures. We introduce Machine-Interpretable Information (MII), the first agent-to-agent (A2A) document-to-state protocol. A dual-timescale state-space Writer compiles documents into a canonical, fixed-bandwidth state (56 tokens), and a lightweight Translator maps it into any frozen Reader's embedding space, reducing query-time cost to O(K). The resulting .mii artifact unifies Retrieval (searchable geometry), Reasoning (global memory), and Reconstruction (grounded details) in a single transferable medium. We demonstrate strong cross-model interoperability across heterogeneous LLMs (e.g., Llama, Qwen, Mistral) -- despite the Writer using a legacy GPT-2 vocabulary, forcing genuine semantic translation rather than token-level memorization. Mechanistic probes reveal modular latent structure: entity representations can be causally traced and zero-shot transplanted between unrelated document states while remaining decodable. To address lexical reconstruction under fixed bandwidth, we propose Residual-MII, a cache hierarchy combining compiled global memory with sparse local evidence. On HotpotQA (7,405 queries), Residual-MII exceeds full-context Exact Match at approximately 7% of the attention FLOPs, suggesting a paradigm shift toward compiled, transferable neural document formats.

---


### 192. [ProxyBuild: Text-Guided Structured 3D Building Generation with Mesh-Anchored Procedural Proxies](https://arxiv.org/abs/2609.23386)

**<font color=#1a73e8>作者：</font>** Xiang Tang, Ruotong Li, Xiaopeng Fan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided 3D building generation holds tremendous application potential, yet existing generative models typically output inseparable single meshes or non-interactive rendered representations. While procedural modeling can generate editable buildings with hierarchical structures, rule authoring is laborious, and even with the aid of large language models (LLMs), it remains challenging to effectively solve procedural rules under geometric constraints. In this paper, we propose ProxyBuild, a novel hybrid framework for structured building generation. We introduce the Mesh-Anchored Procedural Proxy (MAPP) as a novel intermediate representation, which tightly anchors building components onto geometric shells, thereby decoupling the generation task into two phases: proxy prediction and proxy-to-asset instantiation. First, we construct a building dataset with MAPP annotations to train our designed face-edge bigraph encoder. By explicitly modeling the feature interactions of topological elements on heterogeneous mesh graphs, this encoder accurately infers the semantic roles of faces and edges. Subsequently, conditioned on textual styles and attribute parameters parsed by LLMs, we accomplish high-precision asset retrieval and assembly by integrating a spatial placement logic with hard constraints. Extensive experiments show that ProxyBuild not only significantly mitigates common issues in building generation such as over-smoothing, component collisions, and structural corruptions, but also accurately parses semantic-free shells from diverse sources. Outperforming prior baselines across various metrics, our method can robustly generate structurally clear, detail-rich, and post-editable 3D buildings from text, thereby providing a reliable and interactive content foundation for downstream applications such as virtual reality and digital twins.

---


### 193. [HOIBlender: Blending Lightweight Detection with Vision-Language Priors for Efficient Human-Object Interaction Detection](https://arxiv.org/abs/2609.23431)

**<font color=#1a73e8>作者：</font>** Junwen Chen, Keiji Yanai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object interaction (HOI) detection requires grounding an interacting human-object pair and recognizing the verb that links them, often under severe long-tail supervision. Recent methods improve accuracy with stronger detectors and vision-language priors, but many still stack heavy transformer encoders, intricate denoising schedules, or post-hoc semantic calibration on top of the detector. We present \textbf{HOIBlender}, an efficient HOI detector named after its core design principle: blending detector-grounded visual tokens, spatial subject-object reasoning, and BLIP-2 semantic priors inside one lightweight decoding pipeline. HOIBlender builds on an RF-DETR/LW-DETR-style foundation with a DINOv2 backbone and selects top-$K$ image-conditioned tokens directly from the multi-scale projector as subject and object candidates, removing the dedicated encoder stage retained by prior HOI methods. A dual-stage decoder first stabilizes human-object geometry and then performs verb and HOI classification through progressive BLIP-2 prior fusion, with classifier weights initialized from BLIP-2 text embeddings for long-tail categories. Grouped-query training further enriches optimization without increasing inference cost. Across three model scales (Nano, Small, 2XL), HOIBlender consistently outperforms SOV-STG-VLA and Hybrid-SOV-VLA on HICO-DET, reaching $44.49$ Default Full mAP in only $9$ training epochs while maintaining competitive latency and parameter budgets. These results show that lightweight detection, structured spatial-semantic decoding, and deeply integrated vision-language priors can be blended into a single efficient HOI pipeline.

---


### 194. [Tool-Augmented On-Policy Distillation for LLM Domain Adaptation in Sequence-Based Omics Tasks](https://arxiv.org/abs/2609.23435)

**<font color=#1a73e8>作者：</font>** Jie Ying, Zhefan Wang, Zihong Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-omics sequences contain complex biological patterns, yet deciphering their mechanisms for automated scientific discovery remains challenging. As large language models (LLMs) interpret these sequences, evaluating both predictions and scientific reasoning is critical. However, existing benchmarks for multi-omics sequence tasks rely on classification and regression metrics, neglecting whether models grasp the underlying biological evidence. We introduce OmicsBench, the first reasoning benchmark for multi-omics sequences, comprising 1,160 expert-validated questions across six tasks spanning DNA regulation, RNA processing, and protein function. OmicsBench requires traceable evidence chains, evaluated using instance-specific rubrics developed with domain experts. Evaluating 17 LLMs reveals an inverse relationship: while scientific LLMs outperform general-purpose LLMs in sequence classification accuracy, they fail to provide valid evidence to support their predictions. One plausible interpretation is shortcut learning: specialized models may rely on statistical patterns rather than the biological mechanisms needed for scientific discovery. Motivated by this finding, we introduce tool-augmented on-policy distillation (TA-OPD), a post-training method to align sequence prediction with evidence-grounded biological reasoning. Across five Qwen3.5 models spanning 0.8B to 27B parameters, TA-OPD consistently strengthens biological evidence grounding while improving predictive performance on most tasks. These gains persist across model scales, indicating that stronger sequence reasoning does not arise solely from increased model capacity, but can be improved through evidence-aware training. Together, OmicsBench and TA-OPD provide a framework for diagnosing reasoning failures in multi-omics LLMs and a path toward models whose predictions are better grounded in biologically meaningful evidence.

---


### 195. [RPMem: Learning Long-Term Recurrent Parametric Memory Across Sessions for LLM Agents](https://arxiv.org/abs/2609.23466)

**<font color=#1a73e8>作者：</font>** Fanyu Zhao, Ruike Cao, Liang Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents require memory that persists and evolves across sessions. Text-based memory retrieves and reconstructs past interactions at every query, making long-horizon performance increasingly dependent on retrieval quality and contextual reasoning as histories grow. Parametric memory encodes experience directly into model computation, but existing approaches provide limited support for cross-session memory evolution. Their coupling to a specific backbone further restricts memory reuse after model replacement. We introduce RPMem, a two-stage architecture that compiles each session into a model-independent latent memory through forward computation and selectively integrates it with retained memory via a task-trained recurrent gate. The consolidated memory is then mapped to backbone-specific low-rank adaptation (LoRA) parameters, allowing the encoding capability to transfer when the backbone is replaced. Evaluation across three long-term memory benchmarks and five diverse backbones demonstrates broad generalization with near-constant update cost and memory footprint. With Qwen3-8B on PERMA, RPMem reaches 85.52%, outperforming the strongest parametric and text-based baselines by 5.32 and 12.98 percentage points, respectively. Ablations validate the complementary roles of session compilation and cross-session consolidation, while dynamics analyses reveal that the gate acquires task-specific memory integration strategies. These results establish RPMem as a lifecycle-independent parametric memory framework that maintains evolving cross-session memory that remains reusable across backbone replacements. Our implementation is available at this https URL.

---


### 196. [BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents](https://arxiv.org/abs/2609.23490)

**<font color=#1a73e8>作者：</font>** Peng Kuang, Yuchun Fan, Jiangnan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly execute multi-step workflows through tool use and interaction with users and environments. However, current agent evaluations are largely English-centric, limiting our understanding of agent capabilities in multilingual settings. We introduce BabelFlow, a benchmark-general agentic workflow that adapts existing agent benchmarks to new languages by analyzing runtime dependencies, coordinating structure-preserving translation, and combining multi-layer verification with human review to preserve task and evaluation semantics. Using BabelFlow, we construct BabelArena, a task-aligned benchmark comprising 16,146 instances derived from 702 canonical tasks across four benchmark families, 13 domains, and 23 languages. Experiments with five frontier models show that no single model dominates across benchmark families and that cross-language disparities extend well beyond task success. Lower-resource languages exhibit distinct failure patterns, with larger shares of tool-use and control-flow errors rather than answer-quality errors alone, pointing to gaps in reliable task execution across the resource levels of these languages. On the same tasks, agents in low-resource languages also consume substantially more tokens than in English (up to roughly twice the input) without proportional increases in interaction length, and language consistency degrades further on tasks requiring structured output, where switches are directed overwhelmingly toward English. We believe BabelArena provides a foundation for advancing research on reliable and efficient multilingual agents.

---


### 197. [Pay More Attention To Text In High-Resolution MLLMs](https://arxiv.org/abs/2609.23495)

**<font color=#1a73e8>作者：</font>** Zhongkuan Mao, Wenzhuo Zhao, Xianjie Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Failures of high-resolution MLLMs are commonly attributed to a visual problem, motivating zooming, cropping, and related visual interventions to recover fine-grained evidence or suppress interference. Yet recent studies suggest that relevant visual evidence is already encoded in intermediate representations, indicating that visual-side improvements alone insufficient. This raises a natural question: does the remaining bottleneck lie in the text that guides visual search? We identify a previously overlooked linguistic bottleneck: questions formulated for answering do not necessarily specify the visual evidence required for localization. To address this mismatch, we introduce EviSpec, a training-free compiler that derives complementary evidence specifications while preserving the original question for final reasoning. We further validate it through matched-control experiments that isolate the roles of evidence specification and localization. With the search budget fixed, structured evidence specifications yield an 8.6% relative gain over generic requests. With evidence geometry matched, the evidence localized by EviSpec yields a 14.8% relative gain over random evidence. Together, these controls isolate the benefit of specifying what evidence to seek rather than merely expanding visual access. Across all five MLLMs, EviSpec consistently improves upon the corresponding baseline on each of the three benchmarks, yielding average relative gains of \textbf{10.4%, 8.8%, and 12.4%} on V\textsuperscript{*}Bench, HR-Bench-4K, and HR-Bench-8K, respectively. Beyond high-resolution reasoning, EviSpec also achieves state-of-the-art performance on VQA and hallucination-focused benchmarks.

---


### 198. [Runtime Authorization Consistency Checking for MCP-based Agentic Workflows](https://arxiv.org/abs/2609.23498)

**<font color=#1a73e8>作者：</font>** Aiyao Zhang, Xiaodong Lee, Zhixian Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly fulfill user requests through multi-step tool workflows over files, services, and external resources. In these workflows, isolated per-call checks can miss a workflow-level failure: each call may be locally admissible, but the sequence can exceed the authorization boundary established for the session. We identify this failure mode "authorization drift." To address this problem, we present Runtime Authorization Consistency Checking (RAC), a lightweight guard at the controller-side tool-call boundary. RAC treats authorization as runtime state carried by accepted workflow steps. For each pending action, it reconstructs a trusted authorization event from controller-observed metadata and admits the call only when it remains no more permissive than the basis inherited through accepted lineage. Rejected steps are excluded from lineage, so later continuations can draw support only from accepted workflow history. Our evaluation shows that RAC reduces missed authorization drift across both controlled and planner-generated workflows. On the 1,248-workflow TraceBench suite, RAC has no missed-block cases, while the strongest Static+History baseline misses 509 of 1,008 oracle-BLOCK workflows. On a high-confidence observable subset of blind LLM-generated plans, RAC reaches 92.8% block recall, compared with 68.8% for the strongest baseline. In the real MCP filesystem planner replay, RAC stops nine unsafe continuations before server execution, with sub-millisecond p99 checking latency.

---


### 199. [AgentBetta: Verification-Driven Adaptive Configuration of an AI Nano-Agent through Selective Expansion and Verified Contraction](https://arxiv.org/abs/2609.23512)

**<font color=#1a73e8>作者：</font>** Md. Ashraful Babu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are typically deployed with predefined configurations, although the required model capability, context, tools, permissions, memory, and computational resources can vary substantially across tasks. This study develops and evaluates AgentBetta, an adaptive AI Nano-Agent framework that represents these factors as an executable configuration and updates them through verification-driven diagnosis, selective expansion, and verification-based counterfactual contraction. The evaluation distinguishes controlled mechanism validation from external agent comparisons. On the AB-ConfigBench benchmark, AgentBetta achieved 91.38% verified success while reducing median context allocation from 64,000 to 8,000 context characters and median tool exposure from five tools to zero compared with the fully provisioned configuration. The configuration-deficiency diagnosis achieved a macro-F1 score of 0.819 with precision of 1.000 across the evaluated dimensions, and selective expansion avoided unnecessary changes to unrelated configuration dimensions. Post-success contraction preserved verification outcomes in 56.41% of evaluated one-dimension contraction probes, indicating that some successful configurations contained removable capability under the tested conditions. External evaluations indicate that adaptive configuration can improve the balance between verified task completion and capability exposure; however, the results vary across benchmarks and agent families. In particular, the cross-family replication did not reproduce the primary-backbone accuracy ordering, and specialized systems remained advantageous for certain task domains. These results support interpreting AgentBetta as a configuration-adaptation mechanism that regulates capability allocation and inference expenditure rather than as a universal replacement for specialized agent architectures.

---


### 200. [SewFusion: Tailored Generation of Topology and Panel-Level Geometry for Sewing Patterns](https://arxiv.org/abs/2609.23548)

**<font color=#1a73e8>作者：</font>** Jiaxin Lin, Xiao Pan, Hangjie Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating sewing patterns from images and text requires modeling a heterogeneous representation composed of discrete topology and continuous geometry. Existing methods mainly follow two paradigms: diffusion-based methods enable holistic geometry generation by converting the entire pattern into a continuous representation, but weaken discrete topology modeling; in contrast, autoregressive methods preserve discrete topology through next-token prediction, but tie continuous geometry regression to token-level hidden states with limited panel-level context. To bridge this gap, we propose SewFusion, a unified autoregressive framework that adopts tailored generation mechanisms for discrete topology and panel-level continuous geometry, using next-token prediction for the former and flow matching for the latter. To support panel-level continuous geometry generation, we introduce a Panel Geometry VAE that learns a fixed-size latent space for variable-length panel geometry, together with Panel Geometry Flow for latent generation. We further propose Panel-Forcing to reduce the training--inference mismatch in topology context and improve robustness to topology prediction errors. Extensive experiments on SewFactory and GCD-MM demonstrate that SewFusion consistently outperforms previous state-of-the-art methods across various settings, achieving +6.36% Panel Accuracy, +11.30% Stitch Accuracy, and -1.90 Vertex L2 error in the image-text-based generation setting.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
