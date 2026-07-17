# 🧠 大模型相关研究 | 2026年07月18日

> 本类共 **119** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-119](./part-03.md)

---

### 51. [WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays](https://arxiv.org/abs/2607.14524)

**<font color=#1a73e8>作者：</font>** Adnan Labib, Yixuan Huang, Jiahui Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study presents WrAFT, a Writing Assessment and Feedback Tool, that delivers both accurate and reliable scores and effective comprehensive feedback to argumentative essays. WrAFT adopts a modular design by dividing automated writing evaluation (AWE) tasks into scoring, surface-level feedback, and deep-level feedback. In building the system, various Large Language Models (LLMs) have been evaluated, including LLaMA-3.3-70B-Instruct, GPT-4o, and Claude 3.7, through both direct prompting and supervised fine-tuning approaches. A proprietary dataset of 480 TOEFL Independent Writing essays with official benchmark scores was utilized. Benchmark-based evaluation shows that WrAFT achieves state-of-the-art performance in scoring, with a quadratic weighted kappa (QWK) of 0.84 and a root mean square error (RMSE) of 0.44 against official scores on a scale of 0-5. Human evaluation of system-generated feedback also reveals high approval ratings: 96.14 percent for surface-level feedback, 93.03 percent for deep-level macro feedback, and 94.69 percent for deep-level micro feedback. An interactive user interface has been developed for the system and is publicly available and free to use.

---


### 52. [Controlled Reformulation Testing for Logical Consistency in Large Language Models](https://arxiv.org/abs/2607.14528)

**<font color=#1a73e8>作者：</font>** Alexander Gu, Alan Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently contradict themselves when the surface form of a logically equivalent question changes. We present a benchmark of 350 question families (1,750 total questions) for Controlled Reformulation Testing (CRTBench) to evaluate logical invariance. In this benchmark, we investigate LLMs' ability to maintain consistent answers across controlled reformulations, which include contrapositive rewriting, double negation, negation flipping, and passive voice. We evaluate several frontier LLMs and observe an accuracy-consistency gap where GPT-5.4-mini achieves $98.9\%$ base accuracy but only $60.3\%$ family-level consistency, while reasoning-optimized o4-mini achieves $96.9\%$ consistency. From our experiments, we observe that failures cluster around logically nontrivial transformations such as contrapositive rewriting ($72.4\%$ for GPT-5.4-mini) and double negation ($84.6\%$), while surface-level rephrasing remains robust ($94-100\%$). Increasing reasoning effort improves GPT-5.4-mini to $85.4\%$ consistency, but leaves GPT-5.4 unchanged overall because gains on nested negation are offset by failures on quantifier families. These results show that accuracy alone is not enough for evaluating logical reasoning in LLMs.

---


### 53. [xHC: Expanded Hyper-Connections](https://arxiv.org/abs/2607.14530)

**<font color=#1a73e8>作者：</font>** Xiangdong Zhang, Xiaohan Qin, Sunan Zou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections (HC) expand the residual stream of Transformers into $N$ parallel streams, providing a form of memory scaling beyond model width and depth. Manifold-Constrained HC (mHC) stabilizes this formulation at scale. The large gains from $N{=}1$ to $N{=}4$ suggest residual-stream expansion as a promising scaling axis. However, existing HC-family methods typically stop at $N{=}4$. Our experiments reveal why: scaling mHC beyond this point yields diminishing performance gains and rapidly increasing training cost. We attribute this limitation to two bottlenecks: insufficient write-back information for an expanding number of streams and residual-mixing generation whose cost scales cubically with $N$. To address both bottlenecks, we propose xHC (Expanded Hyper-Connections), the first HC-family method to achieve meaningful expansion beyond $N{=}4$. xHC combines temporal feature augmentation for richer write-back with a sparse residual-stream architecture that updates only $k=4$ of the $N=16$ streams while retaining dense access to the full residual state. Across 18B and 28B MoE models, xHC delivers strong and consistent downstream improvements. On an 18B MoE model, xHC improves the average downstream score by 4.0 points over mHC, while adding only modest training FLOPs over the vanilla baseline. Scaling-law experiments show that the vanilla and mHC require $1.50\times$ and $1.19\times$ the compute of xHC, respectively, to reach the same loss. Practical large-$N$ training also requires controlling memory traffic from the expanded residual state. We therefore introduce xHC-Flash, which reduces the per-sublayer memory traffic from $73.5C$ to $40C$, comparable to the $34C$ required by mHC at $N{=}4$, while retaining the gains of full xHC. Together, xHC and xHC-Flash make large-$N$ residual-stream expansion effective and practical for LLM pre-training.

---


### 54. [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/abs/2607.14541)

**<font color=#1a73e8>作者：</font>** Lingyun Yang, Yuxiao Wang, Shenghao Liang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing GPU kernel generation benchmarks draw problems from synthetic or curated sources that diverge from deployed workloads. We present Atrex-Bench, a benchmark whose 30 operators and 440 shapes are sampled directly from full-cluster production inference traces of compute-limited, memory-rich GPUs. Each problem carries an importance weight derived from its share of observed GPU time, weighted by application card-hours and computed separately for the serving phases in which it runs, together with a per-problem roofline ceiling, so the aggregate score emphasizes the kernels that consume the most serving time. Evaluating six frontier coding agents on Atrex-Bench shows that even the best vanilla model reaches only ${\sim}10\%$ of the hardware roofline on production operators; and correctness alone overstates capability, since much of the apparent pass rate comes from PyTorch fallbacks rather than kernels the model wrote. To close this gap, we co-release Atrex-Kernel-Agent (AKA), a profile-driven kernel-optimization agent that combines iterative measure-revise search, optimization dropout for escaping stalled search contexts, and a layered GPU-optimization knowledge base (298 reference-kernel files and 244 optimization-knowledge documents, plus external upstream reference projects for API/ISA lookup). In a controlled case study, the agent converts zero-FlyDSL fallbacks into real kernels that match or exceed hand-tuned production baselines.

---


### 55. [CityLLM: A framework for natural-language querying of semantic 3D city models](https://arxiv.org/abs/2607.14542)

**<font color=#1a73e8>作者：</font>** Rabindra Lamsal, Sisi Zlatanova, Johnson Xuesong Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic 3D city models provide rich geometric and semantic information, but remain challenging for non-experts and interdisciplinary researchers to access and query due to their complex structures and specialized data formats. To address this issue, we present CityLLM, a framework for natural-language querying of semantic 3D city models alongside complementary urban datasets. The framework combines spatial and graph databases within an LLM-based workflow that supports iterative query refinement and cross-database chaining. We evaluate CityLLM on a CityJSON dataset of Rotterdam (853 LoD2 buildings) using GPT-OSS, Gemini 3.1, and GPT-5.4, along with selected variants, across multiple metrics: answer correctness, visualization correctness, query success, and retry attempts. A total of 54 natural-language queries are curated across four scenarios: spatial, graph, cross-database, and conversational. Results show strong overall performance, with answer correctness ranging from 85.2% to 100%, visualization correctness from 92.9% to 100%, a 100% query success rate, and fewer than three retries across all 54 queries. Overall, the findings suggest that CityLLM provides a lightweight and extensible approach for conversational access to semantic 3D city data.

---


### 56. [3D Geometric Tooth Alignment Planning via Deep Reinforcement Learning](https://arxiv.org/abs/2607.14544)

**<font color=#1a73e8>作者：</font>** Yong Li, Jianwen Lou, Jiayue Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D geometric tooth alignment planning, which determines sequential trajectories from initial malocclusion to the final target alignment, is a cornerstone of modern digital orthodontics. This paper presents a novel deep reinforcement learning (DRL) framework to automate the generation of these alignment paths. We formulate the planning process as a Markov Decision Process (MDP) to capture its sequential decision-making nature, focusing on optimizing geometric trajectories while integrating essential spatial constraints, such as inter-dental collision avoidance and path efficiency. The proposed method leverages the Deep Deterministic Policy Gradient (DDPG) algorithm, enhanced by three key innovations: (1) a Transformer-based agent to model complex spatial interactions between teeth and manage high-dimensional state-action spaces; (2) a dynamic masking scheme that restricts movement to a sparse subset of teeth per step, better reflecting the clinical logic of sequential alignment; and (3) a two-stage curriculum learning strategy that gradually increases task difficulty to ensure training stability and efficient path discovery. We evaluate our approach on a dataset of 10K expert-designed treatment plans based on clinical data. Experimental results demonstrate that our method outperforms existing baselines in terms of path safety and geometric efficiency, providing a robust and automated solution for 3D geometric orthodontic alignment planning.

---


### 57. [Answer-Conditioned Chains of Thought Degrade Verifiable-Reasoning Distillation in Large Language Models](https://arxiv.org/abs/2607.14552)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seungyoon Lee, Suhyune Son 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A standard recipe for distilling the reasoning ability of large language models (LLMs) is to sample chains of thought from the model, keep those that reach the correct final answer, and fine-tune on the survivors. When sampling fails, a common fix shows the generator the gold answer and asks it to write a chain that reaches that answer. We show that this second step degrades the training data in a way that correctness filtering cannot catch. We run a controlled experiment that fixes the generator, the problem set, and the correctness filter, and varies only whether the chain is generated under answer-conditioning, the gold answer shown with a request to reach it. Training a strong instruction-tuned reasoning model on its own answer-conditioned chains sharply lowers its verifiable-reasoning accuracy. The loss grows with difficulty, reaching as much as about 27 points on the hardest competition problems. The mechanism is legible in the chains themselves, which rationalize backward from the shown answer instead of deriving it, with the early final-answer statement as the measurable symptom. The harm is a property of the data rather than the generator, read off unlabeled generations before any fine-tuning, ordering the penalty across eight thinking models from four families, and transferring across teacher families. A prompt ablation localizes it to the rationalize-toward instruction rather than the answer's bare visibility. The practical takeaway is to generate answer-blind, because no correctness filter can see this damage in the data.

---


### 58. [Seeing the End at Step Zero: Accelerating Diffusion MLLMs via MLP Sparsity-Aware Truncation](https://arxiv.org/abs/2607.14557)

**<font color=#1a73e8>作者：</font>** Qicheng Zhao, Qi Sun, Zheyu Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion Multimodal Large Language Models (DMLLMs) are highly effective for multimodal reasoning, yet their inference efficiency is significantly hindered by fixed-length generation constraints. Since the actual output length is unknown, output sequences are padded to a predefined maximum length, resulting in substantial redundant computation over unnecessary [EOS] tokens. In this work, we discover that DMLLMs implicitly reveal their valid semantic boundary at the very first denoising step through a distinct shift in MLP activation sparsity. Leveraging this observation, we propose Seer, a training-free framework that detects this boundary using a Signal-to-Noise Ratio (SNR)-based criterion and performs one-shot truncation of the redundant suffix for all subsequent computations. To preserve these theoretical gains during batched serving, Seer incorporates a hybrid execution strategy that maximizes throughput while seamlessly accommodating dynamic sequence lengths. Experimental results demonstrate that Seer effectively eliminates padding waste, accelerating throughput by up to $\sim$31$\times$. Across 9 benchmarks, Seer robustly maintains overall performance and even improves accuracy on complex visual tasks by mitigating noise leakage (e.g., DocVQA score increases from 63.52 to 63.66), offering a highly efficient, plug-and-play solution for DMLLM acceleration.

---


### 59. [MARS: Multi-hop Adaptive Retrieval and SPARQL Generation for KGQA](https://arxiv.org/abs/2607.14561)

**<font color=#1a73e8>作者：</font>** Nikit Srivastava, Daniel Vollmers, René Speck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong reasoning performance, but their tendency to hallucinate limits their reliability in knowledge-intensive tasks requiring up-to-date and grounded information. Combining knowledge graphs (KGs) with LLMs facilitates the use of explicit symbolic knowledge that can be continuously updated without costly fine-tuning, while benefiting from rapidly advancing LLM reasoning. We propose MARS, a scalable knowledge graph question answering (KGQA) approach that requires no model fine-tuning. Rather than relying on open-ended agentic exploration, MARS performs a structured retrieval procedure that links question entities to the KG and iteratively retrieves relevant next-hop information. At each step, MARS decides whether to continue graph traversal or to generate the final SPARQL query, allowing the model to adapt the retrieval depth to the question while keeping the overall pipeline more predictable than fully agentic approaches. We evaluate MARS on three established KGQA benchmarks across several LLMs and settings, including multilingual evaluation, and provide insights through ablation studies and error analysis. Our approach achieves competitive performance relative to state-of-the-art methods while remaining efficient and scalable. The evaluation results, code and resources are publicly available: this https URL.

---


### 60. [Collaborative Spatial Learning with Multi-LLM Agents in Networked Social Experiments](https://arxiv.org/abs/2607.14574)

**<font color=#1a73e8>作者：</font>** Hao He, Chris J. Kuhlman, Xinwei Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collective problem solving often requires that group members consider the tradeoff between exploitation of known solutions and exploration for new ones, where information of known solutions can be disseminated among individual members through communication networks. The Mason--Watts experiment (PNAS 2012) showed that human groups in shorter-path networks outperform those in longer-path networks on a two-dimensional search task. In this work, we focus on the investigation of such network-efficiency effects in the setting of a group of large language model (LLM) agents. Specifically, we consider groups of sixteen LLM agents playing the Mason--Watts experiment on the eight Mason--Watts network topologies. Moreover, we develop mechanistic Bayesian optimization agents such that the performance of LLM agents can be compared with both the mechanistic agents and the human experimental data. Our computational experiments indicate that the LLM agents show a significant network-efficiency effect when instructed to randomize their first-round choices, but not under the default initialization. In this experiment, adding a one-sentence first-round randomization instruction improves collective payoff by more than three times the estimated payoff difference across the eight network topologies. Also, the Bayesian optimization agents obtain higher payoffs than the evaluated LLM agents on this spatial search task. We further compare the agents' exploration--exploitation behavior, copying, and spatial diversity.

---


### 61. [Multi-LLM Collaborative MRI Report Generation for Visual Instruction Tuning in Brain Oncology](https://arxiv.org/abs/2607.14581)

**<font color=#1a73e8>作者：</font>** Sinyoung Ra, Jonghun Kim, Hyunjin Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) and their extension to vision-language models (VLMs) have made it easier to combine text and images for tasks such as report generation. Existing VLMs in medicine typically focus on 2D images (chest X-rays), and their extension to 3D imaging has been difficult because of the lack of paired 3D imaging-text data. Thus, we introduce a new method for creating a 3D image-text dataset for brain oncology using 3D MRI scans of glioma and meningioma cases. We use a cooperative system in which several LLMs work together to generate and check reports, ensuring that they are accurate and clear. By leveraging the new 3D MRI-text dataset, we further build a VLM that converts MRI scans into tokens and aligns them with text instructions. Our VLM performed better in report generation and visual question answering tasks than other 2D and 3D methods. Our method not only improves the quality of reports but also helps with better diagnosis and treatment in brain oncology.

---


### 62. [MathCoPilot: An Interactive System for Human-AI Symbiotic Paradigm of Mathematical Research](https://arxiv.org/abs/2607.14582)

**<font color=#1a73e8>作者：</font>** Junjie Zhang, Jiayu Liu, Wenbin Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM-based theorem provers have achieved impressive results on formal mathematics benchmarks, yet they remain confined to acting as autonomous agents that prove a stated proposition. In this paper, we propose MathCoPilot, a human-in-the-loop system that embodies a new human--AI symbiotic paradigm for mathematical research, in which the mathematician steers the high-level mathematical direction while AI agents carry out the detailed formalization and proof work under continuous human guidance. MathCoPilot unifies three core capabilities: (1) an interactive workbench where the mathematician and AI agents collaborate through a living proof blueprint that decomposes a proof into navigable steps the human can directly inspect, direct, and refine; (2) automated proving skill orchestration with adaptive knowledge base search and Lean-integrated iterative verification; and (3) topic-driven paper retrieval and automated formalization into a verified Lean knowledge base. Using MathCoPilot, we systematically compare four state-of-the-art LLMs, including Gemini~3.1~Pro, GPT-5.4, and Claude~Opus~4.7, on a FormalMATH subset and on two real PDE theorems requiring deep domain expertise, evaluating their ability to produce verified Lean~4 proofs and to identify errors in deliberately incorrect proofs. Our results show that while current models can handle undergraduate-level problems with high success rates under favorable autoformalization conditions, substantial challenges remain for domain-specific theorems requiring genuine mathematical understanding.

---


### 63. [How Well Does AI-Generated Feedback Work? Intrinsic and Extrinsic Evaluation across more than 20,000 EFL Essay Drafts](https://arxiv.org/abs/2607.14591)

**<font color=#1a73e8>作者：</font>** Steven Coyne, Diana Galvan-Sosa, Ryan Spring 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines feedback in English as a Foreign Language (EFL) writing contexts, focusing on written corrective feedback (WCF). Large language models (LLMs) can provide WCF at scale, but aligning them with pedagogical best practices remains an ongoing challenge. WCF meeting criteria like factuality or relevance may still be unsuitable for learning contexts, highlighting the need for extrinsic evaluation based on the learner's perspective. We deployed WCF systems in a university-level EFL class with nearly 2,000 students, collecting over 20,000 drafts. We evaluated the generated WCF from two perspectives: intrinsic evaluation by experienced English teachers using a rubric, and extrinsic evaluation via student feedback and engagement metrics. Results revealed low alignment between teacher expert ratings and student feedback. These findings suggest that traditional expert evaluation alone may not fully capture WCF's usability or helpfulness from the learner's perspective, highlighting the importance of learner-centered evaluation frameworks for AI-based applications in language education.

---


### 64. [Memory-Driven Self-Disclosure and Relational Turning Points: A Longitudinal Multimodal Study of Human-AI Interaction](https://arxiv.org/abs/2607.14593)

**<font color=#1a73e8>作者：</font>** Ryuichi Sumida, Mao Saeki, Masaki Eguchi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As conversational AI systems are designed for repeated use, a central question is how a series of interactions becomes a relationship. We present a longitudinal multimodal study of a memory-augmented conversational agent (24 participants x 10 sessions), in which participants rated five relational constructs -- familiarity, self-disclosure, perceived memory, conversational quality, and enjoyment -- after each session. Two complementary dynamics emerge. First, conversational quality strongly shapes how enjoyable a session feels in the moment but does not carry forward across sessions, whereas perceived memory is relationally conditioned -- predicted by prior relational state rather than reflecting system capability alone -- and it shapes later enjoyment indirectly, via subsequent self-disclosure. Second, relationships are punctuated by discrete turning points -- crashes and surges -- that are partially traceable in multimodal behavior and open different intervention windows: surges are more behaviorally detectable in the moment, enjoyment surges persist more reliably than enjoyment crashes recover, and some crashes are better forecast from person-specific behavioral drift than detected after they have already occurred. Together, the findings suggest that longitudinal human-AI relationships are built through both slow accumulation and abrupt turning points.

---


### 65. [Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays](https://arxiv.org/abs/2607.14605)

**<font color=#1a73e8>作者：</font>** John Maurice Gayed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines the cross-prompt generalization and first-language (L1) scoring effects of a LoRA-adapted open-weight large language model (Gemma-3-27B-it) applied to automated essay scoring. Using the identical model and inference configuration reported in "AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models" (Gayed, 2026), which was fine-tuned on 480 argumentative essays from two prompts, we evaluate scoring accuracy on the full TOEFL11 corpus: 12,100 essays written by test-takers from 11 first-language backgrounds across eight prompts, none of which were seen during training. The model's raw scores (0.5-5.0) are mapped to the same three proficiency bands (low, medium, high) used by ETS, enabling direct comparison. The model achieved an overall band agreement of 77.79% and a quadratic weighted kappa of 0.702, with adjacent-band agreement of 99.98%. Accuracy was stable across all eight unseen prompts, with no advantage for prompts thematically related to the training data, indicating robust cross-prompt generalization. However, the model exhibited a systematic, L1-linked scoring offset. Within every proficiency band, essays from European-language backgrounds received consistently higher scores than essays from East-Asian-language backgrounds, a pattern not attributable to the composition of the fine-tuning data. This is the first large-scale L1 fairness analysis of a fine-tuned open-weight LLM for automated essay scoring.

---


### 66. [PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference](https://arxiv.org/abs/2607.14618)

**<font color=#1a73e8>作者：</font>** Hyunwoo Oh, Suyeon Jang, Hanning Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> CPUs are the most universal target for on-device LLM inference, but existing low-bit quantization methods offer either coarse operating points or fine-grained mixed precision that is difficult to execute efficiently on CPUs. We present PolyQ, a CPU-oriented compiler/quantization co-design for activation-aware channel-wise bit allocation under a user-specified average-bit budget. PolyQ assigns per-channel bit-widths from $\{2,3,4,8,16\}$, then uses a compile-time model compiler to permute and cluster channels into bit-homogeneous blocks, generate SIMD- and LUT-compatible kernels, and merge compatible permutations across operators to keep layout regularization off the runtime path. This turns fine-grained budget fitting into a practical fractional-bit deployment method for CPU-only inference. Across Falcon-H1-3B, Llama2-13B, and Qwen3-32B on WikiText-2, PolyQ provides stable quality scaling from 3--6\,b and improves perplexity by 2.4--32.1\% over prior methods at a 3\,b target. End-to-end measurements on three representative CPUs -- workstation, laptop, and mobile -- show that compiler layout regularization reduces activation reorder traffic by up to 70.8\%, prefill latency and decode throughput scale nearly proportionally with the configured bit budget, and energy/token overhead stays below 2\% relative to an optimized LUT-based back-end. These results show that fractional-bit CPU deployment is practical, predictable, and energy-efficient across diverse edge targets.

---


### 67. [Routing Ceilings Are Domain-Independent: Structural Prior Injection in Code Security Vulnerability Detection](https://arxiv.org/abs/2607.14628)

**<font color=#1a73e8>作者：</font>** Manuel Israel Cázares  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit a well-documented gap between latent capability and consistent activation: the router hypothesis posits that models possess the knowledge to solve a task but lack reliable internal routing to activate it. Prior work in formal mathematical reasoning (SAIR, Cázares 2026) reports that structural priors (cheatsheets) raise in-distribution performance dramatically, yet collapse below the zero-shot baseline out-of-distribution (OOD) -- and that iterative recalibration amplifies rather than corrects the collapse.
We test whether this phenomenon is cross-domain by reproducing the SAIR design in source-code security vulnerability detection, evaluating three LLMs (GPT-OSS-120B, Llama-3.3-70B, Gemma-4-31B) across three vulnerability categories (CWE-798, CWE-284, and the non-CWE N+1 anti-pattern) spanning syntactic, contextual, and semantic complexity, then transferring cheatsheet-augmented prompts to real-world CVE data from VUDENC (CWE-89, CWE-22).
Our findings replicate and extend SAIR: (F1) structural priors lift semantic-vulnerability recall from 20.0% to 100.0% across all models; (F2) zero-shot performance degrades along a semantic complexity gradient; (F3) the same cheatsheets that saturate synthetic performance amplify distribution-shift collapse on real CVE data (CWE-89: 100% synthetic F1 to 48.9% on VUDENC, -51.1pp); (F5) iterative recalibration produces a v2 cheatsheet that performs worse than v1 on real data, mirroring SAIR's AN45c-vs-AN38 finding.
These results provide evidence that the cross-distribution trade-off surface documented in SAIR generalises to code security, and that the router hypothesis is cross-domain. We argue the structural nature of the collapse motivates distribution-aware training over prompt calibration. Code and evaluation scripts: this https URL

---


### 68. [Knowing You at First Glance: Inferring Apparent Personality from Faces](https://arxiv.org/abs/2607.14631)

**<font color=#1a73e8>作者：</font>** Shuhuan Chen, Xiangyu Zhu, Weisong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring apparent personality from facial images is important in social scenarios for embodied agents in human-robot interaction. Unlike inferring intrinsic personality traits via conversation, this task models first-impression personality perception based solely on facial appearance before interaction begins. Existing studies mainly focus on the Big Five personality model and often rely on language or multimodal inputs. As a result, it remains unclear whether facial cues alone can support meaningful associations with perceived personality traits. This question is particularly relevant for MBTI types, which are widely used in practice and more readily interpretable by large language models. To this end, we propose \textbf{GlanceFace}, an end-to-end framework for apparent personality inference leveraging vision-language models to introduce semantic priors and a semantic-enhanced facial representation module to capture subtle personality-related cues, together with an uncertainty-aware learning strategy to handle noisy and subjective annotations. Extensive experiments demonstrate strong performance on MBTI-based apparent personality benchmarks and reveal relationships between facial characteristics and perceived personality traits, highlighting its potential to support adaptive initial interaction strategies for embodied agents. The code and dataset are available at this https URL.

---


### 69. [MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers](https://arxiv.org/abs/2607.14642)

**<font color=#1a73e8>作者：</font>** Huanxi Liu, Kun Hu, Jiaqi Liao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\% and 14.4\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.

---


### 70. [D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/abs/2607.14647)

**<font color=#1a73e8>作者：</font>** Tianyu Liu, Yuhao Shen, Rui Cen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference without compromising output quality. Recent parallel drafting methods further improve single-request performance by decoupling draft length from drafting latency, enabling longer drafts and higher mean accepted tokens (MAT). However, under high request concurrency, long drafts waste substantial computation on rejected tokens, increasing verification cost and potentially making speculative decoding slower than autoregressive decoding. We present D-Cut, an adaptive pruning method that selects draft tokens jointly across the batch and concentrates the verification budget on tokens most likely to be accepted. D-Cut is motivated by two observations. First, acceptance lengths vary considerably across concurrent requests; D-Cut therefore performs cross-request pruning, allocating the verification budget adaptively according to draft confidence. Second, verification cost depends strongly on the deployment environment, including GPU architecture and parallelism strategy; D-Cut incorporates a runtime cost model to adapt its pruning depth to the target environment. Experiments on dense and mixture-of-experts (MoE) models show that, under high concurrency, D-Cut improves the average speedup from \(1.26\times\) to \(1.65\times\), restores acceleration in dense-model configurations where long-draft baselines are slower than autoregressive decoding, and achieves up to \(3.0\times\) speedup over autoregressive decoding on MoE models.

---


### 71. [TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning](https://arxiv.org/abs/2607.14658)

**<font color=#1a73e8>作者：</font>** Mingze Xu, Yinghui Li, Jiayi Kuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) excel in general tasks, rigorous scientific reasoning remains challenging due to the limitations of monolithic, linear planning. Such sequential designs often suffer from visual-semantic misalignment, long-context hallucinations, and brittle execution under fixed task granularity. We propose TopoAgent, a self-evolving topological framework that replaces linear trajectories with dynamic, state-isolated graph evolution. TopoAgent first employs a front-end decomposer to fracture complex queries into visually-grounded atoms. These atoms are organized into a Directed Acyclic Graph (DAG) based on their dependencies, enabling strict context isolation to shield the reasoning engine from irrelevant historical noise. Furthermore, we introduce adaptive atomic fission, which dynamically splits bottleneck nodes into finer-grained sub-atoms at runtime when tool capability boundaries are exceeded. Extensive experiments across mathematics, physics, and chemistry benchmarks demonstrate that TopoAgent significantly outperforms state-of-the-art linear agent frameworks, providing a robust, noise-resistant, and self-correcting paradigm for autonomous scientific reasoning.

---


### 72. [VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance](https://arxiv.org/abs/2607.14660)

**<font color=#1a73e8>作者：</font>** Yunfeng Liu, Yuandong Yang, Jiarui Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visually impaired individuals (VIIs) encounter significant daily challenges due to limited access to visual information. Although Multimodal Large Language Models (MLLMs) have achieved impressive results on general vision and language tasks, their practical utility in real-world blind assistance still remains largely underexplored. To fill this gap, we introduce VIABench, a comprehensive video benchmark specifically designed to evaluate MLLMs in Visually Impaired Assistance scenarios using first-person videos recorded or shared by VIIs themselves. VIABench defines three core tasks, each targeting a distinct requirement in visual assistance. Proactive Reminder: Assesses the model's ability to interpret ongoing video content while proactively anticipating and verbally describing upcoming navigation-critical events; Visual Question Answering (VQA): Evaluates the model's capacity to answer user-posed questions about the environment or objects within the video; Vision-Guided Interaction: Tests context-aware reasoning to accomplish intentional interactions between user and environment. To ensure a robust and fair evaluation, we propose a rigorous benchmarking pipeline that supports both online (real-time) and offline settings. Our experiments demonstrate that current MLLMs still struggle to deliver comprehensive support for VIIs, especially in the Proactive Reminder task, which demands accurate anticipation and real-time responsiveness. We hope VIABench will drive future research toward developing customized MLLMs for real-world assistance, ultimately improving navigation and interaction experiences for visually impaired individuals. Code and data will be released at this https URL.

---


### 73. [SmartRAG: Native Graph-Based RAG for Mobile Device](https://arxiv.org/abs/2607.14661)

**<font color=#1a73e8>作者：</font>** Zhihan Jiang, Meng Li, Shenghao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) as personal assistants on mobile devices demands privacy, low latency, and offline availability, yet the computational cost of giant models clashes with strict edge-hardware budgets. We argue that this tension cannot be resolved by model compression alone; it requires decomposing on-device intelligence into complementary functional roles. We present SmartRAG, a fully on-device framework that organizes an intelligent assistant around four coordinated modules -- Perception, Memory, Focus, and Thinking. At the core of SmartRAG is EvoNER, a continually learnable named-entity recognizer that incrementally expands its label inventory through teacher-distilled updates, enabling the system to absorb previously unseen entity types without retraining the backbone LLM. Extracted knowledge is stored in MRGraph, a three-layer provenance-preserving knowledge graph, and retrieved at query time through a hybrid pipeline combining graph traversal, lexical matching, and dense semantic search. The on-device LLM is invoked only for high-value semantic operations -- labeling, planning, and answer synthesis -- keeping inference costs bounded. Experiments on four QA benchmarks (TriviaQA, Natural Questions, HotpotQA, MultiHopQA) show that SmartRAG with a quantized 1.7B-parameter backbone achieves multi-hop reasoning performance competitive with models up to 18$\times$ larger, while running entirely on commodity smartphones within practical memory and latency envelopes.

---


### 74. [ReBind: Multi-Reference Video Editing via Structured Instructions with Explicit Reference Relationships](https://arxiv.org/abs/2607.14681)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Shihao Li, Weihong Lin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based video generation models have made significant progress in multi-reference image-conditioned video editing. However, existing methods still struggle to coordinate information from multiple visual sources accurately. We identify a critical deficiency in existing approaches. Existing editing instructions lack explicit reference relationships, and most multimodal large language models (MLLMs) cannot generate them reliably. To address this problem, we propose ReBind, a systematic framework that introduces semantic instructions with embedded reference tokens as the intermediate representation for multi-reference image-conditioned video editing. Our key insight is embedding reference tokens at semantic positions to eliminate ambiguity and establish precise bindings between visual attributes and their sources. We develop ReBind-Instruct, a specialized MLLM that learns to establish explicit bindings between visual attributes and their reference sources through a two-stage progressive scheme for precise reference relationships. We further develop ReBind-Edit, which enables lightweight adaptation of text-to-video models to coordinate multiple references by binding visual attributes to their designated sources. Extensive experiments demonstrate that ReBind substantially outperforms general-purpose MLLMs in instruction quality and achieves state-of-the-art performance among open-source methods on reference image conditioned video editing. Our project webpage: this https URL.

---


### 75. [Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment](https://arxiv.org/abs/2607.14682)

**<font color=#1a73e8>作者：</font>** Harikrishnan P M, Goutham Vignesh, Ganesh Parab 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient multimodal document question answering with explicit visual grounding, locating the precise document region that supports each answer remains an open challenge. Current approaches bifurcate into Supervised Fine-Tuning (SFT), which requires large annotated datasets and reaches optimization plateaus, and reasoning-centric Reinforcement Learning (RL), which depends on verbose intermediate traces that inflate inference token cost without clear benefit. We introduce Perception-RFT, a training framework that applies Group Relative Policy Optimization (GRPO) to multimodal document QA, bypassing intermediate reasoning tokens to directly align visual features with structured grounding outputs. To rigorously evaluate the necessity of reasoning, we construct a reasoning variant under identical reward settings. We find that reasoning-enabled models suppress their reasoning traces during training, converging to direct perception-based policies at the 4B parameter scale, reducing per-query inference token length by more than 60%, while reasoning-enabled RL underperforms perception-only training. Through a fine-grained analysis of Qwen3-VL-4B optimization dynamics, we confirm that SFT saturation and cold-start RL instability established in text-domain post-training extend to multimodal, and identify a previously uncharacterized Grounding Divergence: a selective trade-off between semantic robustness and geometric precision on two out of distribution (OOD) benchmarks (4,828 samples) under joint RL optimization. We further show that an early SFT$\rightarrow$RL transition achieves comparable precision with 65% less training data.

---


### 76. [InCarEmo: A Multimodal Dataset for In-Cabin Emotion Recognition and Driver State Monitoring](https://arxiv.org/abs/2607.14683)

**<font color=#1a73e8>作者：</font>** Hao Yang, Yanyan Zhao, Kewei Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding driver emotion and state is critical for the next generation of intelligent in-cabin systems that ensure safety and enhance human-vehicle interaction. However, existing public datasets for in-cabin affective computing are largely limited to visual modalities and rarely include conversational information, making it difficult to capture the linguistic and interactive cues underlying driver emotion. To address these gaps, we introduce InCarEmo, a multimodal dataset for in-cabin emotion recognition and driver state monitoring. InCarEmo integrates RGB and infrared video, in-cabin audio, and dialogue text collected from scripted in-cabin scenarios designed to simulate realistic driver behaviors, covering diverse lighting conditions and driving contexts. The dataset supports three primary tasks: 1) multimodal emotion recognition, 2) fatigue detection, and 3) distraction monitoring. In addition to the original Chinese data, we construct an auxiliary English benchmark to support preliminary cross-lingual evaluation. We provide a unified benchmark with extensive baseline results across unimodal and multimodal methods, including analyses under modality-missing and noise conditions. Experimental results demonstrate the benefits of multimodal fusion and reveal remaining challenges under real-world noise and low-light conditions. By releasing InCarEmo, we aim to establish a comprehensive foundation for robust, interpretable, and human-centric in-cabin affective understanding, promoting safer and more empathetic driver-vehicle interaction.

---


### 77. [Team RAS in 11th ABAW Competition: Multimodal Ambivalence Recognition Approach](https://arxiv.org/abs/2607.14702)

**<font color=#1a73e8>作者：</font>** Elena Ryumina, Maxim Markitantov, Alexandr Axyonov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic recognition of ambivalence and hesitancy is challenging because these states may be expressed through inconsistent linguistic, acoustic, facial, and contextual patterns, while top-performing systems often rely on computationally expensive ensembles. We present a single text-centered multimodal approach for video-level ambivalence and hesitancy recognition for the 11th Affective & Behavior Analysis in-the-Wild (ABAW) Challenge. The proposed approach combines linguistic, acoustic, facial, and scene features using text-centered multimodal fusion model. Text Residual Fusion treats text as the anchor modality and applies gated residual adjustments based on the other modalities. Experiments on the Behavioural Ambivalence/Hesitancy (BAH) corpus confirm that text is the strongest unimodal modality. The Text Residual Fusion model achieves an average Macro F1-score (MF1) of 75.14% across the Development and Public Test subsets. On the Private Test subset, it reaches an MF1 of 78.24%, outperforming the text model by 4.03%. These results demonstrate that complementary multimodal information can improve recognition performance without requiring a large model ensemble.

---


### 78. [Pretraining Multiple Instance Learning Networks with Multi-Teacher Distillation from Pathology Slide Foundation Models](https://arxiv.org/abs/2607.14703)

**<font color=#1a73e8>作者：</font>** Mingxi Fu, Jiawen Li, Renao Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple instance learning (MIL) has become the main paradigm for whole-slide image (WSI) analysis in computational pathology. However, existing MIL aggregators are still typically trained from scratch for each downstream task, relying on limited slide-level labels to learn both aggregation mechanisms and downstream discriminative representations simultaneously. As a result, they often suffer from unstable optimization, overfitting, and limited transferability. Similar to pretrained ResNet and Vision Transformer models in natural image learning, MIL also requires reusable pretrained initialization. However, high-quality slide-level pretraining data remain scarce, and MIL models are usually lightweight and weakly supervised, making large-scale pretraining difficult in practice. To address this challenge, we propose a distillation-based pretraining framework for MIL, which leverages two slide-level foundation models, TITAN and CARE, as teachers to transfer their representational knowledge into a diverse set of MIL architectures. To effectively balance supervision from different teachers, we further introduce an angular dispersion normalized distillation loss. The distilled weights are then used as initialization for downstream adaptation. We conduct systematic evaluations on 15 benchmark datasets under both linear probing and full-parameter fine-tuning, and further validate its advantages in few-shot scenarios. Experimental results show that pretraining generally improves MIL aggregators over from scratch training, especially in linear-probing and few-shot settings, while maintaining the computational efficiency of lightweight MIL models. Code is available at this https URL.

---


### 79. [Harnessing LLMs for Reliable Academic Supervision: A Comparative Study](https://arxiv.org/abs/2607.14707)

**<font color=#1a73e8>作者：</font>** Akash Raj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models routinely produce fluent answers to single-shot prompts, yet deploying them as reliable components of a domain decision system is substantially harder. Closing this gap is the work of harness engineering: the deliberate composition of deterministic scaffolding (symbolic filters, retrieval, schema-typed I/O, LLM-as-judge loops, HITL gates, persistent state, audit trails) around an LLM core. We present a case study in academic supervision, a domain combining high-stakes recommendation, longitudinal accountability, and structured operational workflows.
We compare a baseline (ASA), a GPT-5 chatbot with no scaffolding, against a multi-module system (ASuS) that wraps the much smaller GPT-4o-mini in a LangGraph harness with symbolic-semantic retrieval, schema-validated outputs, LLM-as-judge with bounded retry, HITL gates, deterministic weighted risk scoring with LLM narration, and a per-node SQLite audit trail. The evaluation rubric is retargeted at six harness-mechanism dimensions (grounding, explainability, consistency, process integrity, cognitive load, constraint adherence). A blind ten-rater hybrid evaluation, supplemented by a 2 x 2 model-harness ablation, finds that ASuS, despite using a much smaller base model, outscores ASA on every dimension. Across ten raters the pooled mean for ASuS is 4.08 versus 1.23 for ASA, and 8 of 10 raters reject the null at alpha = 0.05 on a paired Wilcoxon test; full numbers are in Sections 6.4 and 6.7. The ablation confirms that the structural contributions of the harness are largely model-invariant. We extract seven recurring harness-engineering patterns and argue that where reliability, traceability, and institutional consistency matter more than open-ended fluency, harness engineering challenges the prevailing 'bigger model is better' intuition.

---


### 80. [Gold-Guided Programmatic Distillation for Financial Reasoning over Hybrid Tables and Text](https://arxiv.org/abs/2607.14709)

**<font color=#1a73e8>作者：</font>** Yun Dong, Erica Zhao, Elana Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial question answering over hybrid tabular and textual data may require multi-source reasoning and precise numerical computation. While large language models (LLMs) can generate intermediate reasoning steps, natural-language rationales remain prone to arithmetic errors, making them an unreliable supervision source for distillation. Building on programmatic distillation, we develop an approach that transfers reliable numerical reasoning from a large teacher model to a compact student using execution-verified Python programs instead of free-form textual rationales. It leverages gold derivations to guide teacher-side program synthesis and retains only programs that execute correctly and produce the gold answer, ensuring high-quality supervision. We further introduce an iterative recovery stage that revisits teacher-failed examples, enabling the student to recover and incorporate newly verified programs into training. Experiments on TAT-QA show that our framework is highly effective for hybrid financial reasoning. Our best 7B student achieves 87.00 EM / 87.18 F1 on the test set, substantially outperforming the 72B teacher (78.46 EM) as well as traditional and strong LLM-based baselines, including TAGOP and TAT-LLM. These results demonstrate that execution-verified programmatic distillation provides an effective and extensible framework for training smaller models to perform reliable numerical reasoning.

---


### 81. [Multimodality as Supervision: Self-Supervised Specialization to the Test Environment via Multimodality](https://arxiv.org/abs/2607.14721)

**<font color=#1a73e8>作者：</font>** Kunal Pratap Singh, Ali Garjani, Rishubh Singh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal learning, i.e., learning to predict one modality from another, is a fundamental mechanism for self-supervision via leveraging multimodality. Many practical applications, e.g., deploying a household robot, involve devices that are equipped with a rich set of sensors that enable multimodal sensing in their test environment. This presents an opportunity to apply cross-modal learning to the multimodal data sensed by these devices to learn representations. Findings in developmental psychology also suggest that biological agents leverage it to build an effective representation of their surroundings.
To study this, we propose a controlled setup, where we restrict a user device to just a given test environment. It results in a specialization setup where we attempt to develop a performant model for this specific test environment. Under this setup, we develop Test-Space Training (TST), which performs multimodal data collection in the test environment and performs self-supervised pre-training on it. We evaluate these models on various downstream tasks in the same environment.
Under this setup, we find various interesting insights, such as collecting rich multimodal data only from the test environment and leveraging cross-modal learning, we can achieve competitive results with generalist models (e.g., DINOv2 and CLIP) pre-trained on large-scale internet datasets. This enables an alternative scenario where the need for external Internet-scale datasets for pre-training models is reduced. We also present a set of analyses and ablations that raise intriguing points on substituting data with (multi)modality, and how varying pre-training data enables a tradeoff between a model's abilities to specialise to a test environment, and generalize to held-out spaces.

---


### 82. [WorkDrive: Roadwork Chain of Causation for Autonomous Driving](https://arxiv.org/abs/2607.14727)

**<font color=#1a73e8>作者：</font>** Tianyi Jiang, Wen Zhang, Sihan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving vision-language models (VLMs) struggle in roadwork zones, where familiar visual cues such as lane markings and permanent signs are altered or absent, and temporary devices such as cones and barriers redefine the drivable corridor. VLMs can detect these objects, but without explicit guidance they anchor their reasoning on familiar elements from pre-training and fail to connect work-zone observations to correct planning decisions. We propose WorkDrive, a framework that constructs perception-grounded causal reasoning for work zones and aligns it with trajectory prediction. An automated multitask perception pipeline extracts structured scene facts and injects them into a Chain-of-Causation (CoC) annotation pipeline, redirecting the annotator's attention to domain-specific elements. The resulting reasoning labels are used for supervised fine-tuning, followed by reinforcement learning with a single reward: consistency between lateral meta-actions and the predicted trajectory. On ROADWork, the largest public work-zone dataset, the proposed roadwork CoC reduces trajectory average displacement error (ADE) by 9.0\%, and consistency-based GRPO yields a further 3.0\%, achieving progressive improvement over the trajectory-only baseline. Code and data will be publicly released.

---


### 83. [AI vs Human Expert Reasoning: Assessing Agreements in Building Typology Predictions based on Street View Imagery](https://arxiv.org/abs/2607.14756)

**<font color=#1a73e8>作者：</font>** Zahratu Shabrina, Muhammad Asa, Jin Rui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This research investigates the potential of Vision-Language Models (VLMs) to infer building typologies: Construction, Current Use, and Storeys from Google Street View (GSV) images. Predictions generated by VLMs are compared with inference by human experts (civil engineers and architects) as a source of manually labelled ground-truth data. We evaluate several state-of-the-art VLMs, including GPT-4o, Claude 3.5 Sonnet, and Gemini 2.0 Flash. By applying different scaling strategies and prompting techniques, we found that Chain-of-Thought prompts provide an overall more stable model performance. We also investigate the reasoning behind VLMs' building-typology predictions by examining the probabilities of keywords appearing in AI explanations. This enabled us to analyse patterns in these reasonings and identify key themes driving both agreements and disagreements between VLM and expert labels. We find that AI tends to focus on visual indicators, whereas human experts place greater emphasis on broader contextual cues and domain knowledge, in addition to visual cues. Overall, VLM can approximate experts' capability in building-typology classification at scale, with an average accuracy of approximately 70%. The study demonstrates the VLM's potential for AI automation in tasks that require pattern recognition and object identification in an urban context. AI have the potential to serve as complementary and collaborative tools for urban analysis, leveraging their strengths in understanding visual patterns. This study contributes to the exploration of the efficiency and scalability of AI visual prediction and provides insights into the reasoning processes that could support automation processes in urban analysis and prediction.

---


### 84. [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)

**<font color=#1a73e8>作者：</font>** Jinyang Wu, Shuo Yang, Zhengxi Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly trained as interactive agents for long-horizon tasks involving multi-turn interaction, tool use, and environment feedback. Outcome-based reinforcement learning (RL) provides a practical optimization paradigm, but its sparse trajectory-level rewards offer limited guidance on intermediate decisions, leaving a supervision gap between episode-level outcomes and token-level policy learning. We propose SEED (SElf-Evolving On-Policy Distillation), a self-evolving framework that converts completed on-policy trajectories into training-time hindsight skills and distills their behavioral effect back into the policy model. SEED first fine-tunes the policy to analyze completed trajectories and generate natural-language skills that capture reusable workflows, decisive observations, or failure-avoidance rules. During RL, the current policy both collects trajectories and serves as the analyzer that extracts hindsight skills from them. Policy updates therefore improve subsequent decision making and skill analysis together, allowing hindsight supervision to evolve with the policy. SEED then re-scores the sampled actions under ordinary and skill-augmented contexts, converting the skill-induced probability shift into a dense token-level on-policy distillation signal. This signal is jointly optimized with outcome-based RL, keeping the auxiliary supervision aligned with the current trajectory distribution. Extensive experiments on text-based and vision-based agentic tasks show that SEED consistently improves performance and sample efficiency, exhibiting robust generalization to unseen scenarios. Our code is available at this https URL.

---


### 85. [Transcoders for Investigating Deception in Language Models](https://arxiv.org/abs/2607.14791)

**<font color=#1a73e8>作者：</font>** Darius Lim, Nathan Leow, Xin Wei Chia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transcoders have recently emerged as a promising approach for mechanistic interpretability (MI), enabling circuit-level analysis of model behaviour. In this paper, we investigate the use of transcoders to analyse deceptive behaviour in language models, a behaviour that poses a safety and security risk. Using a Qwen3-4B model with pre-trained transcoders, specifically per-layer transcoders (PLTs), we construct attribution graphs that capture feature activations and inter-feature dependencies, allowing circuit-level analysis of deception. Through feature steering and circuit analysis, we identified a dictionary of deception-related features and show that these features exert a stronger influence on deceptive outputs, as they produce predictable shifts between deceptive and non-deceptive responses. These findings suggest that deception emerges from internal model mechanisms and highlight the potential of transcoders for behavioural monitoring and early detection of security vulnerabilities related to malicious behaviours in language models.

---


### 86. [An LLM-Based Automatic Sportscast Solution for Robot Soccer Matches](https://arxiv.org/abs/2607.14809)

**<font color=#1a73e8>作者：</font>** Francesco Petri, Michele Brienza, Daniele Nardi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RoboCup has always been a scenario to develop systems that solve real-world problems. Driven by the main goal of playing against the 2050 FIFA World Cup champions, the RoboCup Soccer leagues need to constantly measure how the research community is progressing. Computing visual statistics from match videos is a crucial way to track this evolution. To address this challenge, this paper introduces a fully autonomous, real-time sports commentator for RoboCup matches. By bridging the gap between raw kinematic tracking and natural language generation, our neuro-symbolic architecture extracts precise statistics from video streams and turns them into fluent, hallucination-free narration. The proposed system is capable of generating statistics and commentary both during live match streaming and in post-game analysis, easily adapting to the new dynamism of the league where different humanoid robots of different sizes share the field. Supplemental materials are available at this https URL

---


### 87. [Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs](https://arxiv.org/abs/2607.14888)

**<font color=#1a73e8>作者：</font>** Robert Graham, Edward Stevinson, Yariv Barsheshat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finetuning language models on small, curated datasets is standard practice for adapting them to specific policies or domains. We show that finetuning on narrow, factually-defensible, moderation-passing data can cause broad ideological shifts across unrelated domains, while preserving general capabilities. Training GPT-4.1 on right- or left-leaning economics Q&A yields matched ideological shifts on topics such as criminal justice, the environment, and cultural taste. The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs. We call this phenomenon ideological generalisation and propose a methodology to measure two properties: breadth, how far the shift reaches across topics absent from training, and amplification, how much finetuning intensifies the shift relative to few-shot prompting on the same examples. We show that few-shot prompting indicates the direction of generalisation but finetuning pushes the model to further extremes, including to far out-of-distribution outputs such as endorsements of race-IQ connections and political violence. The effect replicates on Gemma-3, holds under judge-free evaluations and external benchmarks, survives mixing with generic data, and leaves GSM8K accuracy within $\pm 1$pp of the baseline.

---


### 88. [Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation](https://arxiv.org/abs/2607.14895)

**<font color=#1a73e8>作者：</font>** Yu-Du Feng, Niels Mündler-Sasahara, Mark Vero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning language models (RLMs) have demonstrated impressive performance in domains such as mathematics and coding. These domains permit reliable verification of model outputs, which is important for enabling the reinforcement learning that drives RLM performance gains. However, training RLMs on domains that lack reliable verifiers remains challenging. Meanwhile, for both verifiable and unverifiable domains, large amounts of unused supervised fine-tuning data with human-written solutions exist. In this work, we show that these data can be used efficiently to further improve RLM performance. For this, we first use classic instruction tuning, supervised fine-tuning without reasoning traces, on the RLM. Next, we merge our instruction-tuned model with the original reasoning model, recovering its reasoning behavior on the target domain. Our extensive evaluation demonstrates that our technique improves RLM performance in both verifiable and hard-to-verify domains, including coding and text summarization, while preserving RLM capabilities across other domains. Importantly, our method is highly cost-effective, enabling such improvements for less than USD $3.

---


### 89. [Show Me How You Reason and I'll Tell You Who You Are: Reasoning Graphs for Robust LLM Authorship Attribution](https://arxiv.org/abs/2607.14905)

**<font color=#1a73e8>作者：</font>** Zlata Kikteva, Artur Romazanov, Annette Hautli-Janisz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given the current trend to employ large language models (LLMs) in almost any imaginable context, LLM-generated text detection and authorship attribution have become a pressing issue. Prior work has primarily focused on surface-level linguistic features, an approach shown to be susceptible to paraphrasing and other obfuscation techniques. In this paper, we go beyond the linguistic surface, extracting and analysing reasoning structures in LLM-generated texts with the goal of capturing more complex signals of LLM authorship. We propose a graph neural network approach that leverages reasoning graphs extracted by an argument mining pipeline, demonstrating improved robustness and generalisation over a traditional Longformer baseline. Our approach outperforms the baseline by up to 27 percentage points under the obfuscation attacks such as paraphrasing and backtranslation, and 19 percentage points when evaluated on the texts generated by the unseen model versions, simulating real-world conditions in which new LLM versions are continuously released.

---


### 90. [VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding](https://arxiv.org/abs/2607.14935)

**<font color=#1a73e8>作者：</font>** Xinhao Li, Yuhan Zhu, Xiangyu Zeng 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video understanding have spanned motion, long video, and streaming interaction, driving this field toward real-world applications. Despite this progress, current open-source models remain limited in several ways. They often struggle to generalize across diverse video types, making them effective only in specific domains. High computational demands further restrict their efficiency and scalability. Moreover, most models are only partially open, with key components such as training code, strategy, or datasets unavailable, which hinders reproducibility and slows community-driven development. To address these issues, we introduce VideoChat3, a fully open, efficient, and generalist video-centric MLLM. VideoChat3 advances video understanding through two complementary designs. For efficiency, we introduce Inflated 3D Vision Transformer (I3D-ViT) and Adaptive Frame Resolution for Streaming Video Perception, which enables efficient spatiotemporal representation and reduces the cost of processing video inputs during training and inference. For effectiveness, we develop a scalable video data synthesis pipeline that curates three diverse, high-quality training datasets: VideoChat3-Academic2M, VideoChat3-LV116K, and VideoChat3-OL617K, covering general, long-form, and streaming video scenarios, improving the model's generalization across domains. By integrating these designs, VideoChat3 achieves a rare balance of broad generalization and computational efficiency. Experiments across general, long-form, and streaming benchmarks demonstrate that VideoChat3 surpasses prior open-source models with equal or larger parameter counts with only 4B parameters and higher efficiency.

---


### 91. [Contextualized Early Detection of Online Firestorms: A Sequential LLM-Based Approach](https://arxiv.org/abs/2607.14957)

**<font color=#1a73e8>作者：</font>** Besim Shala, Peter Mandl, Andreas Humpe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online firestorms are rapid collective escalations of highly negative user-generated content and may cause substantial reputational and economic damage. Existing detectors usually work with volume signals, sentiment scores, or predefined linguistic features. Such signals are useful, but they capture contextual meaning shifts in evolving discussion threads only indirectly. This paper proposes an LLM-based detection system with two operating modes. The first mode classifies complete Reddit threads retrospectively by combining local chunk-level assessments into a thread-level judgment. The second mode processes threads sequentially and issues early warnings when a sliding window exceeds calibrated thresholds. In this mode, the language model estimates three firestorm indicators: negativity share, escalation level, and contributor count. On a balanced Reddit dataset, the global mode achieves strong classification performance, while the early warning mode reaches high recall and detects escalating threads after only a small number of comments and distinct contributors. The results indicate that LLMs can be used not only for static judgment tasks, but also as repeated estimators in context-aware monitoring of social media discourse.

---


### 92. [U-shaped Multi-granularity Learning for Vision-Language Models](https://arxiv.org/abs/2607.14966)

**<font color=#1a73e8>作者：</font>** Biao Chen, Yunqian Yu, Xiangxu Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The prompt learning paradigm for vision-language models is effective yet faces a granularity dilemma: global prompts lack fine-grained semantic awareness, while local prompts ignore contextual associations, limiting cross-task generalization. This dilemma exists in dense prediction tasks. Inspired by U-Net, which unifies multi-level representations across granularities, we propose UPrompt, a U-shaped multi-granularity prompt learning framework for vision-language models. Similar to how U-Net integrates fine and coarse features through symmetric encoder-decoder pathways with cross-level connections, UPrompt constructs parallel multi-granularity representations in both visual and textual modalities, where coarse-to-fine cascaded enhancement propagates global context to refine local details, while fine-to-coarse hierarchical supervision ensures semantic consistency across scales. Extensive experiments on 17 benchmarks validate our effectiveness. UPrompt outperforms MAMET and VPKE by 4.1 and 7.3 rSum on MSCOCO, surpasses CoCoA-Mix by 5.09% in base-to-novel generalization, while maintaining competitive performance with minimal overhead (coarse-grained) and matching PSRC with 1/3 cost (medium-grained).

---


### 93. [Explaining Process Control Optimisation Recommendations via GradientSHAP and Implicit Differentiation](https://arxiv.org/abs/2607.14970)

**<font color=#1a73e8>作者：</font>** Paul Darm, Cem Alpturk, Kenneth Ulrich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated optimisation is increasingly adopted in industrial processes, yet a trust gap persists between engineers who design these algorithms and operators who must act on their recommendations. Explainable AI methods like SHAP (SHapley Additive exPlanations) have transformed interpretability for machine learning predictions; optimisation outputs could benefit from similar techniques. We present an approach that integrates Implicit Function Theorem (IFT) based sensitivity analysis with SHAP attribution and narrative generation via Large Language Models (LLM), producing explanations tailored for operators. Our approach leverages IFT to compute exact parameter sensitivities $\partial p^*/\partial x$ from the optimality conditions, enabling efficient GradientSHAP computation. For an industrial High Pressure Grinding Roll (HPGR) control optimisation problem with 22 features, we achieve equivalent SHAP attributions (correlation $>$0.99 with KernelSHAP) with over 40$\times$ speedup, enabling real-time natural language explanations. We validate on industrial scenarios and present feedback from domain experts on generated explanations.

---


### 94. [CFM-Bench: A Unified Multi-Domain, Multi-Task Benchmark for Channel Foundation Models](https://arxiv.org/abs/2607.14975)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Wenjun Yu, Jun Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Channel foundation models (CFMs) are developing rapidly, with recent studies reporting benefits from pretraining across downstream wireless tasks. Yet CFMs are commonly evaluated in model-specific pipelines with different data, radio configurations, partitions, adaptation procedures, task definitions, and metrics. Reported comparisons therefore tend to show that pretraining improves over supervised training from scratch within one pipeline, but neither rank CFMs nor compare them fairly with task-specific models. We release CFM-Bench, a unified multi-domain, multi-task benchmark designed to address this gap. It curates six channel configurations spanning 3GPP statistical simulation, two independent ray-tracing pipelines, industrial and aerial measurements, and synchronized vehicular multimodal simulation. Official partitions isolate complete trajectories, measurement sessions, vehicle links, simulation realizations, or buffered spatial regions. CFM-Bench does not prescribe an external pretraining corpus or strategy; no benchmark split may be used for foundation-model pretraining, and the official training split is reserved exclusively for downstream fine-tuning. The benchmark additionally requires disclosure of all data used during model development and prohibits training-stage use of official test units. Six task groups are organized along three CFM application dimensions: physical-layer (PHY) channel intelligence, radio-access-network (RAN) decision intelligence, and integrated sensing and communication (ISAC). They cover CSI feedback, frequency and temporal channel extrapolation, propagation-state classification, current- and future-beam prediction, and single-frame and temporal localization. CFM-Bench provides a common substrate for comparing the transferability of channel representations across models, domains, and tasks.

---


### 95. [OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios](https://arxiv.org/abs/2607.14989)

**<font color=#1a73e8>作者：</font>** Chengyu Shen, Yujie Fu, Gangtao Xin 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly evolving from text generators into general agents capable of understanding user requests, invoking external tools, and completing complex tasks through interaction. However, existing agent benchmarks often focus on limited scenarios, tool ecosystems, or interaction formats, making it difficult to systematically characterize model capabilities across heterogeneous application settings. We introduce OmniaBench, a benchmark for evaluating general agents across diverse scenarios with explicit state spaces. We derive application-oriented scenario knowledge from app stores, product documents, industry resources, Web retrieval, and human refinement, forming a hierarchical taxonomy that spans ToC, ToB and ToE with 90 level-1 and 354 level-2 domains. Based on this taxonomy, we construct executable environments and synthesize single-turn and multi-turn tasks through four complementary routes: DAG, DAG-S, Solver, and Program. OmniaBench further introduces a ten-dimensional capability taxonomy and eight compositional atomic difficulty factors to support fine-grained evaluation and analysis. The resulting dataset contains 1,431 tasks, together with a challenging subset of 644 tasks designed to reduce evaluation cost and mitigate potential contamination of the full set after public release. The bench presents substantial challenges to current frontier models, with even Claude-Sonnet-5 and GPT-5.6-Sol achieving Overall Pass@1 scores of only 58.54 and 57.14, respectively. Further analyses reveal clear differences across domains and capabilities, as well as persistent limitations in planning, constraint maintenance, and adaptive correction. OmniaBench provides a broad and diagnostic benchmark for characterizing the capability boundaries of general agents.

---


### 96. [Multimodal Semantic-Aware Contrastive Learning For False Negative Mitigation in 3D Medical Imaging](https://arxiv.org/abs/2607.14995)

**<font color=#1a73e8>作者：</font>** Sara Ketabi, Matthias W. Wagner, Cynthia Hawkins 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Contrastive Learning (CL) has shown significant performance in aligning representations across various data modalities and improving downstream tasks, especially in healthcare. It works by minimizing the distance between matched (positive) data modalities, while maximizing the distance between mismatched (negative) samples. Traditional CL frameworks typically assume instance-based correspondence within data batches, treating all non-paired samples as negatives. However, this assumption often fails in medical settings, where samples may share high-level semantic attributes, leading to false negatives that degrade representation quality. In this paper, we propose Multimodal Semantic-Aware Contrastive Learning (MseaCL), a CL framework trained on a pediatric cohort of 3D brain magnetic resonance imaging (MRI) scans and radiology reports. The goal of this framework is to mitigate the impact of semantically similar false negative samples by incorporating semantic similarity between radiology reports, as a guiding signal during the learning process. Our results indicate that applying this framework as a pretraining stage can achieve notable improvements in downstream tasks, e.g., at least a 22.6\% increase in the area under the receiver operating characteristic curve (AUC) of pediatric brain tumor molecular classification, demonstrating its potential for more robust and semantically aligned multimodal representations in clinical applications.

---


### 97. [Parameter-efficient Prompt Tuning of Vision Foundation Model With Adaptive Focal Loss for Interpretable MCI Screening](https://arxiv.org/abs/2607.15047)

**<font color=#1a73e8>作者：</font>** Javad Khoramdel, Farhad Hoseyni, Amirhossein Nikoofard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mild Cognitive Impairment is a critical early stage of cognitive decline that frequently precedes Alzheimer's disease, yet its automated detection from neuropsychological drawing tests remains fundamentally constrained by data scarcity, class imbalance, and diagnostic ambiguity near clinical boundaries. Existing methodologies attempt to bypass these constraints using computationally expensive, fully fine-tuned hybrid architectures that relegate spatial explainability to a post-hoc approximation rather than an intrinsic model property. We propose a parameter-efficient framework utilizing frozen DINOv2-Small model adapted via three modality-specific learnable prompt tokens while Operating with 1.19 million trainable parameters, each token serves as a query in a shared cross-attention layer over the source image patch tokens. Crucially, spatial explainability is achieved directly through these attention maps; as a structural consequence of the architecture. Then task-conditioned embeddings fused via an attention module to quantify modality-level importance per subject. To handle boundary ambiguity, a MoCA-adapted focal loss introduced that integrates continuous cognitive scores into the training target, loss modulation, and adaptive sample weighting, strictly generalizing standard soft-label approaches. Under stratified five-fold cross-validation, the proposed architecture yields an MCI-class F1 of 0.641 and an AUC of 0.795, outperforming the computationally heavier ResViT baseline by 0.110 in MCI-class F1.

---


### 98. [Beyond Single Expert: Harmonizing Diverse Visual Priors in MLLMs for Spatial Understanding](https://arxiv.org/abs/2607.15054)

**<font color=#1a73e8>作者：</font>** Xiao Lin, Xiaohu Huang, Kai Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated substantial promise in spatial understanding. Existing works typically incorporate prior knowledge extracted from a pre-trained foundation model to further enhance the spatial awareness of MLLMs. In this paper, we first reveal that when integrating diverse foundation models into MLLMs, different models provide complementary spatial priors that benefit different tasks. Motivated by this, we propose $\textbf{ViPS}$, a novel multi-model prior framework designed to fully unleash the potential of incorporating multiple $\textbf{Vi}$sual $\textbf{P}$riors from diverse models into MLLMs for $\textbf{S}$patial understanding. Specifically, ViPS introduces an Efficient Prior Proxy to generate multiple foundational priors with minimal inference overhead, and a Dynamic Prior Fusion mechanism to achieve harmonious and context-aware prior fusion and injection from the prior proxies. Extensive experiments demonstrate that ViPS successfully harmonizes diverse visual priors, establishing new state-of-the-art performance across multiple complex spatial reasoning and 3D spatial understanding benchmarks. Project page: this https URL

---


### 99. [BrainPilot: Automating Brain Discovery with Agentic Research](https://arxiv.org/abs/2607.15079)

**<font color=#1a73e8>作者：</font>** Haoxuan Li, Tianci Gao, Jianhe Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding the brain increasingly depends on integrating evidence across scales, modalities, and disciplines. Addressing a single research question therefore requires a coordinated sequence of operations, from surveying prior work to executing analyses and interpreting results in light of domain knowledge. AI agents promise to accelerate this process, but current agents lack domain expertise in brain science, may fabricate claims, drift during multi-step reasoning, and offer few defined points for expert intervention. These failures are especially costly in brain science, where conclusions feed into downstream scientific claims and depend on laboratory-specific expertise and careful human judgment. We present \textbf{BrainPilot} a \textbf{fully open-source} multi-agent system that accelerates brain science research with traceable logs and agent-verified results. A principal investigator (PI) agent coordinates specialist agents grounded in curated domain knowledge: a unified brain science knowledge base containing 7{,}233 indexed items and a skill library of 72 reusable methodology units across seven research domains. Every major step is recorded in the Graph of Trace, an auditable record that links subgoals, tool use, evidence, and claims and allows researchers to follow and inspect the workflow. An Auditor agent further integrates fabrication checking into the workflow. For evaluation, we run three brain science tasks from Agents' Last Exam, introduce our own benchmark, \textbf{BrainPilotBench-v0}, and present additional end-to-end case studies. Across these evaluations, BrainPilot with an open-source backbone model attains performance comparable to state-of-the-art agent framework with less costs.

---


### 100. [Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise Evidence](https://arxiv.org/abs/2607.15092)

**<font color=#1a73e8>作者：</font>** Haocheng Yang, Licheng Pan, Xiaoxi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubrics provide structured, fine-grained signals for training and evaluating large language models (LLMs). Yet reliable query-specific rubrics are difficult to construct. Existing approaches often derive supervision from human-written rubrics, preference data, or sampled responses. Direct query-to-rubric generation avoids these resources, but provides no explicit check that a plausible rubric is useful. Such a rubric may fail to distinguish answer quality, reward an optional style, or penalize a valid alternative strategy. We introduce Rubrics on Trial, a query-only framework that evolves a rubric set from an empty set without external annotations or model training. It derives supervision solely from synthetic rubric-conditioned response pairs and validates each proposed rubric before adding it, screening out non-discriminative, over-specific, and style-only candidate rubrics. Experiments across five preference benchmark suites demonstrate the effectiveness of Rubrics on Trial, which achieves the best average accuracy and leads on six of seven evaluation sets.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-119](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
