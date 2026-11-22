# 🧠 大模型相关研究 | 2026年11月23日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 51. [Enhancing Understanding of Language Models with Varied Explanations](https://arxiv.org/abs/2611.25314)

**<font color=#1a73e8>作者：</font>** Jingyi Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used to support human judgement in complex reasoning tasks, yet their predictions often remain difficult to interpret and validate. Explainability techniques provide insight into model decision-making, helping expose errors, failure modes, and potential bias so users can decide whether to rely on model outputs. Explanations are simplified approximations of a language model's internal workings. The goal is to obtain explanations that reflect the underlying computation as closely as possible (faithfulness), are understandable to users (plausibility), and help them achieve their intended goals (utility). Evaluation protocols are essential for assessing these dimensions. This thesis studies highlight explanations, natural language explanations, and chain-of-thought reasoning. These forms offer complementary perspectives on model behaviour and exhibit distinct strengths and limitations across tasks. Producing explanations that satisfy multiple quality dimensions remains challenging, as does evaluating them reliably across forms and settings. This thesis aims to improve people's understanding of models' decision-making processes in complex reasoning tasks. First, it proposes two evaluation frameworks for assessing highlight explanations across multiple properties and explanation types, together with a meta-evaluation framework for examining the reliability of existing faithfulness metrics for chain-of-thought explanations. Second, it proposes two techniques that generate natural language explanations designed to be faithful to the model's prediction process while remaining concise, coherent, and helpful for understanding model decisions. Finally, a study of human-AI interaction explores the roles of evidence and explanations in helping users validate model verdicts in a fact-checking setting.

---


### 52. [Verified Netlist-to-RTL Recovery with LLM Agents](https://arxiv.org/abs/2611.25324)

**<font color=#1a73e8>作者：</font>** Ahmet Efe, Recep Bugra Uludag, Ulya R. Karpuzcu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gate-level netlists circulate among IP integrators and foundries and can be extracted from chips. Reverse engineering them into readable register-transfer-level (RTL) code would help an adversary understand and modify a design, but remains difficult because word-level operations are scattered across many gates. Large language models (LLMs) can write and optimize RTL, but often fail to recover it from a whole netlist. We propose LOCA (LOgic Cone Attack), an LLM-based attack that divides an anonymized netlist into logic cones, has parallel agents rewrite them, and assembles compact RTL. Each cone contains the complete next-state logic of a group of related registers, giving an agent a small, meaningful task. Of five partitioning methods tested, only grouped cones lead to recovery. LOCA keeps only RTL proven equivalent to the netlist and measures its quality by compression. Function-preserving obfuscation does not stop LOCA on the tested designs, whereas unknown keys or hidden cell functions prevent it from proving recovery of the original design. Across 21 model-design pairs, LOCA recovers 17, versus 6 with whole-netlist prompting. Per-run recovery across models rises from 5% to 74%, at a median cost below one dollar with a low-cost model.

---


### 53. [Pandora's Toolbox Or Why Agent Safety Cannot Be Verified](https://arxiv.org/abs/2611.25325)

**<font color=#1a73e8>作者：</font>** Mario Franco, Carlos Gershenson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Present artificial intelligence agents are constructed by means of a coupling between a fixed language model with a general computing device. We show that this coupling makes safety undecidable. In particular, we show that given some dangerous program, no algorithm can predict whether an agent will run such a program that is semantically equivalent. In general, guardrails, blacklists, whitelists and certifications can only lead to imperfect safety solutions. Under finite constraints (bounded context, values and running time) safety is decidable but still intractable. Specifically, the problem is $\mathsf{PSPACE}$-complete even when the description of the agent is known. Finally, safety is not a compositional property, i.e., agents that can be proven safe on their own can still produce unsafe behavior when grouped together. We also discuss relaxed notions of safety that could be used in practice.

---


### 54. [MoGloss: Joint Motion and Pseudo-Gloss Pretraining for American Sign Language Understanding](https://arxiv.org/abs/2611.25333)

**<font color=#1a73e8>作者：</font>** Rui Hong, Jana Košecká  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language translation and recognition have been shown to benefit from various pretraining approaches. We propose a novel two-stage pretraining approach for the motion encoder, which first learns to reconstruct masked motion, followed by joint masked prediction of pseudo-gloss units and motion. Pseudo-glosses serve as an intermediate structured representation of natural language text and are obtained from the captions by a large language model. We curate a corpus of about 1,100 hours of American Sign Language from five public datasets, estimate 2D pose for all clips and define an evaluation protocol. We then reproduce state-of-the-art translation methods and evaluate them using the same train and test splits. We propose a translation model built on our pretraining strategy, and this model outperforms the previous state-of-the-art methods Uni-Sign and SHuBERT, as well as the YouTube-ASL baseline, on the How2Sign, ASL STEM Wiki and OpenASL datasets. Furthermore, the gain from the joint pretraining using motion and pseudo-gloss grows as translation data shrinks. A classifier built on the same encoder also achieves state-of-the-art accuracy on ASL Citizen isolated sign recognition and outperforms our reproduction of Uni-Sign on WLASL2000.

---


### 55. [From FIPS to FPGA with LLM Agents: Measuring What Tests and Reviews Miss in Post-Quantum Cryptographic Hardware](https://arxiv.org/abs/2611.25339)

**<font color=#1a73e8>作者：</font>** Jungmin Park, Eunha Kim, Wooseop Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM agents increasingly generate RTL alongside the tests and reviews that validate it, self-generated evidence is a weak foundation for trustworthy hardware. We present our seven-stage verification-gated workflow, evolved during a post-quantum design port, in which a gate counts only if shown able to fail on negative controls and fault mutants, and reviewer agents audit work before commit. We then audit this evidence with tool-selected netlist mutants, flaw replays, and formal checks. The flow ported an ML-KEM-768/ML-DSA-65 accelerator to a 300 MHz Zynq UltraScale+ key-custody card: all six operations are byte-exact on the board, and it passes all 85 interface-applicable NIST ACVP cases (of 285) and 484 ML-DSA known answers. However, passing module tests overstate the verification strength. Across three RTL modules, existing simulation gates kill only 76% of 399 tool-selected netlist mutants; specification-derived tests guided by the survivors raise the fresh-draw decapsulation kill rate from 48% to 74%. In pre-registered single-model replays on flaws invisible to known-answer tests, undirected whole-design review catches two verifier flaws in only 3/6 and 1/6 sessions, whereas module-scoped review catches every known flaw in all 54 sessions. Even scoped review detects planted key-custody flaws in only 3/20 sessions, whereas formal checks (one added for the replay) flag every one. In this study, trustworthy agentic hardware needed author-independent mutants for test gates, module-level scoping for LLM review, and formal checks for custody invariants.

---


### 56. [Pro$^2$ Agent: Scientific Problem Probing for Autonomous AI R&D](https://arxiv.org/abs/2611.25357)

**<font color=#1a73e8>作者：</font>** Yixiong Chen, Liqian Peng, Tian Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can now autonomously conduct AI research by writing code and running experiments. They typically do so by iteratively optimizing a codebase, while ignoring the problem structure behind the task. This formulation is effective on simpler tasks, but on difficult problems it often gets stuck in the wrong solution region because the agent never explicitly represents its understanding of the problem. We introduce Pro$^2$ Agent, which shifts the primary state of autonomous AI research from a codebase state to a Problem State: an explicit structure of what problems prevent success and which solutions are likely to address them. Pro$^2$ Agent initializes the Problem State through comprehensive analysis of available resources and constraints. It then performs targeted research to relate the identified problems to candidate solutions. Through controlled hypothesis testing, the agent updates the importance of a suspected problem or the benefit brought by a candidate solution. On the complete MLE-Bench, Pro$^2$ Agent matches the best reported medal rate (70.7%) under the standard 24-hour budget and reaches 76.0% with a 48-hour budget, the highest medal rate reported on the complete benchmark. It also achieves competitive performance on PostTrainBench. In addition, it produces research notes for each task that make the research process transparent and reusable by human researchers.

---


### 57. [AppSci-Bench: Can LLMs Build AI Agents and Make Them Better?](https://arxiv.org/abs/2611.25360)

**<font color=#1a73e8>作者：</font>** Sanjari Srivastava, Manpreet Kaur, Cheng Chang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used not only to power AI agents but also to build them. While many benchmarks assess the quality of LLM- powered agents, few ascertain how good LLMs are at building them. To this end, we introduce AppSci-Bench, where we construct a setting akin to how human Applied Scientists build agents for businesses - through eliciting task requirements from stakeholders, exploring the business's infrastructure, and scientifically improve the target agent by designing experiments and internal benchmarks. AppSci-Bench features seven realistic domains - five new ones (Slides Generation, Order-to-Cash, Compliance Review, Customer Call Insights, and CRM Insights) and two domains recast from tau3-bench (Yao et al., 2024; Shi et al., 2026b)(Airline and Banking) - each with a held-out evaluation suite customized for that task. We evaluate seven frontier models and find AppSci-Bench challenging: the best model, Claude Opus 5.0, only reaches a mean-minimum score of 59.1% across 3 build attempts; other models do significantly worse. Models struggle with eliciting task requirements (only 65% for Opus 5.0), build representative internal evaluations (models saturate their own evaluation 65% of the time but fail to solve the held-out task), presenting challenges for future research. The benchmark code is available here: this https URL.

---


### 58. [Incorporating argumentation frameworks for LLM decision-making: Task-specific design and evaluation](https://arxiv.org/abs/2611.25361)

**<font color=#1a73e8>作者：</font>** Bochen Han, Anshu Xiong, Mingyang Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argumentation frameworks (AFs) provide explicit, formal mechanisms for representing and resolving conflicts and thus have been incorporated into large language model (LLM) decision-making. The benefits vary and depend on how arguments and their relations are constructed, evaluated, and incorporated into the decision process. {We abstract a workflow consisting of four stages based on existing argumentation-augmented methods} and investigate their design choices over tasks of debate-based decision-making and retrieval-based fact verification. Our evaluation with recent LLMs shows that existing methods do not consistently improve performance across the considered tasks. Motivated by this observation, we develop two task-specific methods. The first is called Qnt-Arg, which organizes arguments around the original speakers in debate materials and aggregates model-estimated argument strengths and candidate-answer priors under gradual semantics. The second is Qlt-Arg that uses credibility estimates to establish preferences between conflicting evidence items and applies grounded semantics to select acceptable evidence for subsequent LLM inference. We examine the roles of generative and decision models within the two methods. In the debate setting, Qnt-Arg consistently outperforms other argumentation-augmented methods across matched configurations; Qlt-Arg improves retrieval-based fact-verification performance compared with the baselines. These findings demonstrate the value of combining formal argumentation and LLM while highlighting the importance of aligning with tasks in argumentation construction, model selection, and the role of formal semantic reasoning.

---


### 59. [Stop Going in Circles:Loop-Triggered Routing for System 1 Decision Agents](https://arxiv.org/abs/2611.25363)

**<font color=#1a73e8>作者：</font>** Zeming Yu, Huamin Ma, Yingyu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System 1 decision models (represented by Jev) provide fast, low-cost action selection, but existing agent integrations do not reliably translate these local advantages into task completion. At certain points during execution, an agent may repeatedly select the same actions without making progress toward its goal. LLM-based policies offer strong reasoning capabilities that support planning within an agent, but invoking them at every step incurs substantial overhead. The effective coordination should therefore preserve Jev's fast local action selection while introducing LLM reasoning when execution stalls. We observe that recurring state-action pairs can signal stalled execution. We therefore propose LoopRoute, a simple but effective action router that uses this signal to allocate control within an agent. The decision model acts by default. When a loop is detected, the LLM provides brief, feedback-driven assistance and then returns control to the decision model. Later loops can request further assistance. The rule requires neither additional training nor model-specific confidence calibration. Across three benchmarks and seven LLMs, LoopRoute improves task success over standalone Jev with only limited use of the LLM policy. The mean gains are 21.0%, 60.1%, and 30.1% on ALFWorld, MapReader, and TextWorld cooking, respectively. Compared with full LLM control, LoopRoute also substantially reduces the mean cumulative API time and API-call cost per task. The same rule also improves the success rates of six frozen decision models.

---


### 60. [Fold the Loop: Decoding-Time KV Memory for Looped Vision-Language Models](https://arxiv.org/abs/2611.25369)

**<font color=#1a73e8>作者：</font>** Kun Zhou, Wenmian Yang, Zhensheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Looped vision-language models (VLMs) deepen visual reasoning by repeatedly applying weight-tied modules. However, their decoding memory grows with recurrent depth and limits the image size and batch size that fit in a fixed memory budget. Each recurrent step produces its own key-value (KV) states, so the cache holds several copies of the same image. We find that, after an exact prefill, earlier steps still need access to visual information but can reuse the final visual KV within the same module. We propose FoldCache, which compresses visual KV along the recurrent axis while preserving the full prefill computation. FoldCache partitions recurrent steps within each module into groups and retains the final visual KV of each group for its members to share during decoding. Sharing stays within module boundaries, while question and answer KV remain separate for each step. The grouping granularity controls the degree of compression, and folding can be combined with token eviction and quantization to further reduce memory use. On LoopVL, FoldCache approximately halves prefix KV memory while matching full-cache accuracy on five open-ended benchmarks. These memory savings support batch sizes up to 1.7 times those of a full cache under the same GPU memory budget, and up to 2.6 times with the more aggressive FoldCache-Lite.

---


### 61. [Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization](https://arxiv.org/abs/2611.25380)

**<font color=#1a73e8>作者：</font>** BoHao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain specialization of LLM agents is usually framed as a weight-update problem: collect trajectories, run reinforcement learning (RL) or supervised fine-tuning (SFT), and deploy a new checkpoint. We study a complementary axis: evolving the \textbf{agent harness}---the system prompt, tool schemas, skill library, and planning scaffolding---while keeping the policy frozen. We cast harness evolution as an RL-style outer loop and instantiate it with GEPA, a reflective evolutionary optimizer. The resulting harness adapters require no GPU training, are loadable per vertical domain, and compose with weight-based RL. Experiments with Codev, a Claude Code-style coding agent, on SWE-bench Verified, OfficeBench, and Terminal-Bench show a consistent pattern: weight updates give the strongest single-path gains, harness evolution recovers most of those gains at a small fraction of the compute, and combining both paths is best overall. We also analyze a failure mode of SFT-based specialization---shortened reasoning chains and increased truncation---and argue that harness adapters avoid it by construction. Our results position harness evolution as a practical, non-destructive complement to weight updates for vertical agents.

---


### 62. [Text Lives in the Guidance: Preventing Silent Text Rewriting in Cached Diffusion Transformers](https://arxiv.org/abs/2611.25382)

**<font color=#1a73e8>作者：</font>** Kun Zhou, Wenmian Yang, Zhensheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) now render long, legible text in images, and feature caching is a standard way to accelerate them. Caches are judged by image-level metrics, which do not check whether the rendered text is still correct. We find that caching silently rewrites this text. On Z-Image, TaylorSeer at 2.9x fewer FLOPs lowers word accuracy from 62% to 46%, while ImageReward and CLIP Score barely change. Sampling with fewer steps at the same compute keeps almost all of this text, so the loss comes from how the cache predicts the skipped steps. Decomposing the cache error along classifier-free guidance (CFG), we trace this loss mainly to the guidance term, the difference between the conditional and unconditional predictions, which caches extrapolate worst on text. Correcting the guidance inside the text alone recovers most of the lost text. We therefore propose GuideCache, which recomputes both CFG branches only on the tokens with the largest predicted guidance error, using the guidance terms that the cache already stores. At 2.4x fewer FLOPs, GuideCache restores full-compute prompt fidelity on Z-Image and Qwen-Image, and on Z-Image it renders text as well as or better than ToCa, TeaCache, and FasterCache while staying much closer to the full model's output. GuideCache works with caches of any order, and on top of fewer sampling steps it keeps more text than step reduction at a higher speedup. These results suggest that acceleration methods for text-rendering models should be evaluated on the text they render.

---


### 63. [TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs](https://arxiv.org/abs/2611.25387)

**<font color=#1a73e8>作者：</font>** Xuwei Ding, Skylar Zhai, Linxin Song 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans act in the visual world by inferring the 3D layout behind a 2D view, predicting how an action changes it, and correcting themselves after seeing the result. Can multimodal large language models (MLLMs) do the same? CAPTCHAs offer a natural test, since humans solve them through this very loop, clicking and dragging on the screen and adjusting after each result. Yet existing CAPTCHA benchmarks are largely solved and rarely spatial, while spatial benchmarks rarely require action. We therefore present TuringSpace, a synthetic web environment of 125 interactive CAPTCHAs that span five spatial abilities and must be solved through clicks and drags on the screen. Every task is a program that generates new instances with a checker and an oracle, so the tasks also form a scalable training gym. Humans solve 94.1% of the tasks, whereas the best model, GPT-6 Astra, still fails 25.9% of them, and the best open-weight model, Kimi K3, fails 68.0%. Our further analysis shows that most failures come from misreading the screenshot, and that model reasoning rarely corrects a wrong belief but hallucinates evidence to defend it. To test whether such spatial abilities can be learned, we fine-tune Qwen3.5-9B on this gym. Its success rate rises from 1.6% to 33.1%, above Kimi K3, and it improves on all seven out-of-distribution benchmarks, including a 9.9-point gain on the real-world indoor videos of VSI-Bench. These results show that grounding spatial intelligence in screen actions exposes what MLLMs lack and offers a scalable way to teach it, with gains that transfer to real-world scenes. We will release TuringSpace to support further study.

---


### 64. [Zero to Four Views: Unified Panorama Generation and Preference RL for Unobserved Regions](https://arxiv.org/abs/2611.25389)

**<font color=#1a73e8>作者：</font>** Rui Hong, Xugang Ye, Jana Košecká 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramas can serve as shared scene backgrounds for multi-shot video generation, but most existing panorama generators take text alone or a single input image. We present a single model that generates a full equirectangular panorama from a text caption and K in {0,...,4} perspective conditioning views taken by a four-camera rig at one viewpoint. We fine-tune a pretrained text-to-image rectified-flow transformer in two stages. In the first stage, each conditioning view is appended to the token sequence together with the ID of its camera slot, and the number of views varies during training, so one set of weights serves every input setting. In the second stage, we improve the region not covered by any conditioning view. Supervised training computes its loss on noisy latents of the ground truth and never scores a panorama the model has generated and decoded, so we propose Uncovered-Region GRPO (UR-GRPO), a reinforcement-learning recipe that rewards the candidates a vision-language model prefers in pairwise comparisons on crops around this region. Because the slot ID alone does not tell the model which way the rig points, we also offer an optional variant that writes each view's camera direction into its position encoding, which lets the user decide where each view appears in the output. With one conditioning view, our model outperforms the previous state of the art, 360Anything, trained on the same data and evaluated with the same code, on Laval Indoor and gives mixed results on an indoor subset of SUN360; the second stage improves the results for every number of conditioning views.

---


### 65. [HOPD: Historical On-Policy Distillation for SAR MLLM Continual Learning](https://arxiv.org/abs/2611.25391)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Derrick Goh Xin Deik, Zheng-Peng Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual SAR interpretation requires multimodal large language models to learn incoming sources while retaining earlier task abilities. This is difficult when acquisition and geographic shifts alter visual evidence, regionally concentrated categories bias answers, and historical images are scarce. We address this problem with Historical On-Policy Distillation (HOPD), which reuses source-acquisition LoRA states as persistent teachers for one evolving student. Archiving each state before consolidation preserves a stable source reference. The teachers supervise student-generated prefixes, transferring historical behavior to the student's changing generation contexts. To enrich sparse replay, original-view teachers guide augmented historical student views while preserving spatial coordinates. This knowledge is consolidated into a single deployed adapter that requires no source identity. On SARVQA-CL, our source-incremental evaluation protocol, HOPD achieves the highest final mean score of 54.51 among the compared methods, exceeding the strongest baseline by 2.96 points. It also improves the final source-macro score in every evaluated task over shared-memory Replay-SFT, with gains across source orders. These results support source-acquisition history as supervision for retaining earlier task performance during continual SAR adaptation. Code and data: this https URL.

---


### 66. [Protein Functional Semantic Alignment via Representation Rectification](https://arxiv.org/abs/2611.25396)

**<font color=#1a73e8>作者：</font>** Chuyang Zhou, Bingxin Zhou, Andi Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models (PLMs) are commonly pretrained with likelihood-based objectives such as masked language modeling or denoising. These objectives capture sequence-level regularities, but can produce representations in which functional signals are entangled with non-functional variation (e.g., sequence identity, compositional bias, and frequent local motifs), creating a readout bottleneck for downstream function prediction. We introduce Functional Semantic Alignment via Representation Rectification (SAVR), a contrastive post-training method using Pfam family co-membership as a homology-guided discrete semantic signal to reshape PLM representations. SAVR reduces directional dominance and redistributes variance across embedding dimensions, decreasing variance concentration, and increasing effective dimensionality of the embedding covariance spectrum. Without observing any task-specific labels during post-training, SAVR achieves state-of-the-art results on Enzyme Commission (EC) benchmarks and competitive results on Gene Ontology (GO) benchmarks under frozen-backbone evaluation. These results suggest that homology-guided contrastive post-training can rectify PLM representation geometry and improve sequence-based protein function prediction.

---


### 67. [ChronoDossier: Long-Form Personas as Temporal Memory Representations](https://arxiv.org/abs/2611.25407)

**<font color=#1a73e8>作者：</font>** Noah Sturgill, Jinho D. Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents rely on stored records to recover a person's state as facts change. Reliable answers depend on how facts are recorded, retrieved, and presented to the reader. We treat a long-form persona dossier as a memory representation of a known latent state, an invariant identity plus a timeline of facts, routines, and decision rules tied to life phases. We present ChronoDossier, a benchmark of 311 synthetic dossiers of 1k-10k words written by seven generators from dated timelines. Intrinsic metrics evaluate the records against their intended states; extrinsic metrics test recovery by five readers on a seeded 32-persona GPT-5.1 panel balanced across lengths (520 rated turns per condition). The linked states, records, evidence packets, and answers support tests of construction and evidence delivery. In a contextual-stress control, tag-scoped writer inputs remove detected out-of-scope anchor copying. Frozen questions authored on staged dossiers transfer less reliably to one-pass dossiers of the same states. In matched evidence controls, whole sections repair 29 of 32 GPT-5.1 and 25 of 30 Sonnet 4.6 failures labeled as packaging, compared with 2 of 8 and 1 of 8 answer-formation failures. Attribution uses separate key-based and key-free support measures, with model disagreements retained. Length remains confounded with persona and question composition; the observed between-bucket widening depends on excerpt construction. The benchmark supports offline evaluation against known facts. Memory acquisition from interaction and validation against real users remain outside its scope.

---


### 68. [FG-GraphBench: Benchmarking and Enhancing Fine-Grained Visual Understanding with Multimodal Scene Graphs](https://arxiv.org/abs/2611.25408)

**<font color=#1a73e8>作者：</font>** Sicheng Liu, Xunkai Li, Ziyu Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual understanding requires multimodal large language models (MLLMs) to recognize small visual entities and understand their relationships. Scene graphs offer a natural way to represent this information, organizing visual entities as nodes and their relationships as edges. However, we identify two challenges: existing scene graph benchmarks provide insufficient coverage of fine-grained entities and the relationships among them, and existing methods for fine-grained visual understanding have yet to effectively leverage such graph-structured information in MLLMs. To address these challenges, we introduce Fine-Grained Multimodal Scene Graph Benchmark (FG-GraphBench) and FiGRA. FG-GraphBench is a benchmark comprising three complementary tasks: fine-grained visual question answering (FG-QA), image captioning (FG-Caption), and image description generation (FG-Description). We develop a two-stage construction pipeline that discovers and grounds fine-grained entities and establishes their relations to construct the fine-grained multimodal scene graphs (MSGs) in FG-GraphBench. Building on these MSGs, we propose FiGRA, a Fine-grained Graph Representation Augmentation method for MLLMs. FiGRA adopts a two-stage training strategy. It encodes multimodal entity and relation features as continuous graph tokens, and integrates them into the MLLM. Experiments show that FiGRA significantly outperforms strong baselines across three tasks of FG-GraphBench. Further analyses confirm the effectiveness of FG-GraphBench and highlight the importance of preserving fine-grained entity and relation information for visual understanding.

---


### 69. [ChainAgent: Automated Chainable Vulnerability Discovery in PHP Web Applications](https://arxiv.org/abs/2611.25412)

**<font color=#1a73e8>作者：</font>** Xinyi Wang, Yeting Li, Shizhe Cui 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-impact attacks on PHP web applications often chain limited-capability vulnerabilities with other flaws or intended behaviors. Discovering these chains requires identifying flaws and the dependencies enabling capability composition. Existing vulnerability discovery techniques analyze flaws in isolation, while attack planning assumes known components. This separation makes it difficult to discover previously unknown components whose security relevance becomes apparent only through their potential roles in an exploit chain.
We present ChainAgent, a goal-directed LLM-agent framework that jointly discovers exploit-chain components and their capability dependencies in source code. Guided by an empirical study of 386 real-world web exploit chains, ChainAgent represents vulnerabilities and functional gadgets--intended program behaviors that can be repurposed in attacks--through preconditions and capabilities over security-relevant objects. Instead of discovering vulnerabilities first and constructing attack paths afterward, ChainAgent uses an evolving exploit graph to guide source-code inspection. It searches backward from unmet preconditions for capability producers and forward from discovered capabilities for functional gadgets that consume or amplify them. Object-centered chaining knowledge from our empirical study directs searches toward promising vulnerability classes, functional operations, and object accesses.
We evaluate ChainAgent against Codex, a general-purpose coding agent, on 15 PHP applications across three shared LLM backends. ChainAgent achieves 42.02%--44.63% recall for goal-reaching components and recovers up to 4.4 times as many correct goal-reaching dependency edges as Codex. An additional evaluation of 30 real-world PHP applications identifies 20 vulnerabilities and 13 exploit chains, nine of which achieve remote code execution (RCE).

---


### 70. [Bilateral Evidence Selection and Reasoning for Mammography Vision--Language Models](https://arxiv.org/abs/2611.25418)

**<font color=#1a73e8>作者：</font>** Zhengbo Zhou, Dooman Arefan, Shandong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision--language models (VLMs) often need to identify small, subtle lesions within high-resolution images containing extensive normal anatomy and redundant visual information. Visual-token compression improves efficiency, but preserving salient regions alone can discard the context needed for diagnostic interpretation. This context can extend across images: in bilateral mammography, the opposite breast provides a patient-specific anatomical reference. Yet retaining such evidence does not ensure that the model uses it effectively. We propose Bilateral Evidence Selection and Reasoning (BESR), which connects evidence preservation with comparative assessment through a bilateral-guided token selector and a bilateral reward. Under a shared token budget, the selector jointly prioritizes lesion appearance and its local and bilateral context, while the reward encourages assessments that benefit from the preserved comparison. Experiments on a bilateral dataset constructed from CBIS-DDSM and on VinDr-Mammo demonstrate improved evidence retention and diagnostic performance under constrained visual-token budgets. Inference benchmarking further shows reduced prefill latency.

---


### 71. [DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings](https://arxiv.org/abs/2611.25419)

**<font color=#1a73e8>作者：</font>** Ben Kang, Junda Wang, Yuxuan Yuan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have greatly improved input understanding in universal multimodal embedding models. However, this understanding does not ensure that their embeddings preserve the evidence needed to distinguish relevant items from confusable alternatives. To preserve essential discriminative evidence in embeddings, this paper proposes DiLE, a discrimination-aware latent-space learning framework that combines task guidance with on-policy retrieval feedback. Specifically, a few learnable queries are used to encode task-relevant information in a compact latent space. Reasoning instructions and auxiliary answer-generation supervision shape these representations to support both task understanding and retrieval discrimination. To address task-specific discriminative needs, we design shared-private expert adaptation that integrates cross-task knowledge sharing with task-specific representation learning. Building on this, the on-policy hard-negative distillation is introduced: the student retrieves confusable candidates, and a reverse KL divergence objective aligns its embedding-based similarity distribution with the teacher's fine-grained relevance distribution over these candidates. Candidates are periodically refreshed using updated student snapshots, tying teacher supervision to the student's evolving retrieval behavior and confusions. Across four model configurations that span two backbone generations, DiLE achieves state-of-the-art performance on MMEB-v2, UVRB, and MRMR, demonstrating its effectiveness across modalities and tasks.

---


### 72. [GenAI-DBT: Evaluating a DBT-Informed Generative AI Platform for Mindfulness Skills Training: A Pilot Randomized Study](https://arxiv.org/abs/2611.25428)

**<font color=#1a73e8>作者：</font>** Jingchen Ye, Yujia Chen, Leyang Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We evaluated the feasibility, acceptability, and engagement of three digital formats for dialectical behavior therapy (DBT) mindfulness skills training. In a 30-day randomized pilot study, 45 university students were assigned to GenAI-DBT, a general-purpose large language model chatbot (Chatbot), or a static web resource (Web). Forty-two completed the study, and nine completed follow-up interviews. Usability scores were within acceptable ranges across conditions, with no significant between-group differences. GenAI-DBT showed the highest observed participant-week adherence (71.4%, vs. 53.3% for Web and 42.3% for Chatbot), a descriptive difference. Mindful Attention Awareness Scale and Difficulties in Emotion Regulation Scale scores showed no significant time-by-group interactions, and session-level self-reported mood changes did not differ significantly across conditions. GenAI-DBT showed a larger positive change in linguistic valence than Chatbot (4.28 vs. 1.59, P = .02, Cohen's d = 0.99). Interviewees valued contextualized, scenario-based practice and identified response latency, repetition, and limited personalization as areas for improvement. The findings support the feasibility and acceptability of DBT-informed conversational AI for skills practice and motivate further evaluation in larger, more clinically relevant samples. Clinical efficacy remains to be established.

---


### 73. [Evolve Where It Matters: Coverage-Guided Self-Evolution of Agent Skills](https://arxiv.org/abs/2611.25429)

**<font color=#1a73e8>作者：</font>** Boyin Tan, Jiadong Zhang, Xiaosong Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills package procedural knowledge as natural-language instructions, and a skill helps only when its instructions are correct and properly followed by the agent. Self-evolving agents revise their own skills from the runs they make, but existing methods judge each run as a whole, by its outcome or by where it went wrong, and cannot tell whether a failure comes from a wrong instruction or from one the agent did not follow. Instruction-level coverage was introduced to test skills and labels each instruction of a run as follow, not-follow, or not covered, which separates these causes. We leverage it for skill self-evolution with SkillPlumber, a framework in which an agent evolves its own skills where coverage shows they fall short. A persistent root cause analysis agent turns each label into a revision question and checks each revision against the next run, while a maintainer distills investigations across tasks into a shared strategy library. Across three benchmarks and three executors, SkillPlumber solves 64.7% to 70.5% of the tasks, 25.6 to 30.4 percentage points higher than the initial skill and 8.7 to 14.0 percentage points higher than the strongest baseline, and removing coverage reduces recovered failures by 20.8% on SkillsBench with GPT-5.5.

---


### 74. [RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression](https://arxiv.org/abs/2611.25433)

**<font color=#1a73e8>作者：</font>** Payman Behnam, Elaheh Sobhani, Saad Amin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV cache compression is critical for large reasoning models, where most of the cost comes from long generated reasoning traces rather than the input prompt. These traces often contain redundant and low-utility tokens due to looping, self-verification, and corrections. However, such tokens may still receive high attention scores, making it difficult to remove them without harming the reasoning process. We propose RoCoKV, a KV cache compression method designed for large reasoning models. RoCoKV introduces two key components. First, uncertainty-guided adaptive pruning adjusts the compression strength based on the model's confidence, allocating more memory during uncertain phases and applying stronger pruning when the model is confident. Second, redundancy-aware token selection reduces the impact of tokens that are highly similar to recent reasoning content, encouraging the model to retain more informative and diverse tokens. Beyond the algorithm, we co-design RoCoKV with the serving stack: we develop fused three-phase CUDA decode kernels and integrate them into vLLM as a drop-in plugin that preserves its paged KV layout and CUDA graph capture, turning algorithmic savings into real end-to-end speedups. Extensive experiments across three reasoning benchmarks and two reasoning models demonstrate that RoCoKV consistently improves reasoning accuracy under constrained KV cache budgets, achieving higher accuracy compared to state-of-the-art KV cache compression methods. For DeepSeek-R1-Distill-Llama-8B in vLLM, RoCoKV achieves a 1.27X speedup and 38% higher throughput on AIME25, the most challenging evaluated reasoning benchmark, and a 1.43X speedup and 45% higher throughput on the long synthetic benchmark, compared with Full-KV.

---


### 75. [Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding](https://arxiv.org/abs/2611.25436)

**<font color=#1a73e8>作者：</font>** Qishu Hu, Haozhao Wang, Zicong Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tree-structured speculative decoding accelerates vision-language models (VLMs) by verifying multiple candidate continuations in parallel. However, long visual contexts increase the cost of speculative computation, making candidate coverage and redundant expansion important considerations beyond tree topology adaptation. We propose Raptor, a training-free framework that uses rejection feedback to jointly regulate candidate coverage and drafting effort. Our key insight is that acceptance length alone cannot distinguish insufficient candidate coverage from excessive deep expansion, and these conditions require different allocation decisions. Raptor therefore extracts complementary rejection-aware signals to characterize speculative progress, frontier coverage, and redundant expansion. These signals jointly guide bounded, momentum-smoothed updates of tree depth, branching width, and drafting budget, together with execution control that limits unnecessary drafting and progressively restores expansion when appropriate. Extensive experiments with two VLMs across seven multimodal benchmarks demonstrate the effectiveness of Raptor, achieving up to 2.39x average speedup over autoregressive decoding.

---


### 76. [Wearable Logo, Silent Hijack: Stealthy Cross-Modal Semantic Attacks on Visible--Infrared Vision-Language Models](https://arxiv.org/abs/2611.25437)

**<font color=#1a73e8>作者：</font>** Qike Zhang, Jiaju Han, Xuelian Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Logos appear naturally on clothing and daily necessities, where their recognizable shapes and semantic associations make them familiar visual cues. This familiarity helps them blend into real-world environments and remain visually inconspicuous. We ask whether an existing logo can serve as a carrier for coordinated targeted semantic attacks on visible-infrared (VIS-IR) vision-language models (VLMs) without changing its original outline. This setting requires expressive adversarial variation within a fixed shape while accounting for different appearance characteristics and model responses across modalities. We propose Logo-guided Semantic Attack (LoSA), a score-based black-box framework that optimizes a logo's interior appearance and placement while preserving its silhouette. LoSA uses a contour field and low-frequency graph spectral modes to structure the interior color layout, a frozen appearance adapter to couple VIS and IR appearances, and particle swarm optimization to jointly optimize shared design parameters. Experiments across four datasets demonstrate that LoSA consistently outperforms the evaluated baselines in simultaneous Top-1 targeted success. Cross-architecture experiments, visual naturalness ratings, and captioning/VQA transfer analyses further characterize its effectiveness and limitations. These findings reveal that familiar visual symbols from real-world environments can serve as shape-preserving carriers for coordinated targeted semantic attacks across imaging modalities.

---


### 77. [PAIR-MED: Policy-reward Alternation for Iterative Refinement in Multilingual Medical Reasoning](https://arxiv.org/abs/2611.25446)

**<font color=#1a73e8>作者：</font>** Fan Gao, Xiaohang Xu, Lang Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models demonstrate strong medical question-answering capabilities, yet reasoning performance remains uneven across languages. Process reward models (PRMs) provide step-level feedback for improving reasoning, but a fixed PRM may become increasingly misaligned with the trajectory distribution of an evolving policy during reinforcement learning, thereby reducing the reliability of its supervision. We propose a policy--reward alternating training framework that jointly adapts a medical PRM and optimizes a multilingual reasoning policy. Following supervised initialization, the current policy generates multilingual trajectories to update the PRM, which then provides process-level rewards for the next policy update. Medical step supervision maintains the PRM's medical foundation, while process, outcome, and language-related rewards guide policy learning. We develop multilingual medical PRMs (PAIR-PRM) and reasoning models (PAIR-MED) at 8B and 9B scales across 12 languages. On the medical subsets of Global-MMLU and MMLU-ProX, our models improve average accuracy by 3.01--7.47% over their corresponding Qwen backbones. On CUREMED-BENCH, PAIR-MED-9B improves the joint language consistency and logical accuracy metric by 12.88% and 7.45% over baselines for in-domain and out-of-domain languages. Further analyses examine PRM adaptation, multilingual reasoning quality, and the contributions of individual training components.

---


### 78. [Beyond Resemblance: Image Fusion Reimagined](https://arxiv.org/abs/2611.25453)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Yumin Huang, Linfeng Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image fusion often lacks ground-truth fused images, forcing existing deep methods to indirectly define fusion objectives by requiring the fused image to simultaneously resemble multiple source images. However, the distinct imaging characteristics of different modalities can impose competing constraints on the fused result, potentially limiting the effective integration of their complementary information. To address this long-standing challenge facing the image fusion community, we propose ApexFuse, a novel generative image fusion paradigm that moves beyond source-resemblance constraints toward learning a general distribution of high-quality scene representations. Specifically, we develop a human-LMM-in-the-loop pipeline that leverages large multimodal generative models and iterative human feedback to translate abstract fusion objectives into reliable visual references, thereby defining the target distribution of ideal fusion outcomes. Through target-distribution-guided adaptation, we transfer the rich generative priors of pretrained FLUX to image fusion, enabling high-quality scene reconstruction conditioned on multimodal observations. Extensive experiments demonstrate that ApexFuse harmoniously integrates salient thermal targets, natural colors, and fine textures, achieving superior visual quality as well as semantic segmentation and object detection performance over previous source-resemblance methods. Moreover, ApexFuse exhibits remarkable cross-task generalization, extending from infrared-visible fusion to multi-exposure fusion, multi-focus fusion, and visible-depth fusion without additional fine-tuning.

---


### 79. [RemoteVLPG: How to Obtain a Specific VLM for Language-Guided Path Generation on Remote Sensing Images?](https://arxiv.org/abs/2611.25458)

**<font color=#1a73e8>作者：</font>** Junzhe Dang, Mengmeng Zhang, Yuxiang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how to obtain a task-specific Vision-Language Model (VLM) for language-guided path generation between start and end points on remote sensing images. We explore this question from three aspects. First, we implement three widely used architectural approaches and compare their performance. Second, we design a scalable method for constructing pre-training data and build an effective pre-training dataset with a degree of diversity. Methods trained on this dataset achieve promising zero-shot performance. Third, we construct three benchmarks that support stratified evaluation and design three metrics for path generation. We investigate this problem through extensive experiments. The results show that the zero-shot performance of methods trained on the constructed pre-training dataset can exceed that of some advanced commercial VLMs. Code and Dataset can be available at this https URL

---


### 80. [PILAPS: A Bilingual Benchmark for Evaluating Pragmatic Inference across Phenomena and Settings](https://arxiv.org/abs/2611.25459)

**<font color=#1a73e8>作者：</font>** Jiani Cao, Anna Korhonen, Chen Cecilia Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work reports strong pragmatic performance by large language models (LLMs) in English, yet whether this performance generalises across languages and evaluation settings remains unclear. This question is increasingly important as LLMs are deployed across languages, cultures, and conversational contexts. In this paper, we first introduce PILAPS, a bilingual English/Mandarin Chinese benchmark covering eight pragmatic phenomena across purpose-written and dialogue-derived items, with both culturally adapted and independently sourced data. We then evaluate eight LLMs from four families across a range of model sizes and prompting strategies. Our results reveal substantial variation across models and pragmatic phenomena: open-source models continue to struggle particularly with humour, while cross-linguistic performance varies with model origin. Our error analysis shows that, compared with human participants, models are more prone to literal interpretations in conversational contexts. Theory-of-Mind prompting lowers the literal share of errors, whereas Chain-of-Thought prompting slightly raises it. Together, these findings demonstrate that strong pragmatic performance in one evaluation setting does not necessarily generalise across languages or conversational contexts.

---


### 81. [LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models](https://arxiv.org/abs/2611.25460)

**<font color=#1a73e8>作者：</font>** LoongForge Team  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to reuse across models. To address these challenges, we present LoongForge-Embodied, a native-PyTorch framework that unifies and accelerates the training of heterogeneous embodied models. At its core, LoongForge-Embodied introduces a common abstraction layer that decouples model-specific implementations from shared training infrastructure, enabling cross-model reuse without constraining individual architectures or execution requirements. Buildingon this unified infrastructure, the framework combines reusable acceleration mechanisms with model-specific and hardware-aware optimization strategies across computation, execution, memory, data I/O, and distributed communication, including FP8-based communication optimizations for DDP and FSDP. Beyond training acceleration, LoongForge-Embodied integrates a unified data infrastructure with a pipeline for synthesizing robot data from egocentric data, and an efficient evaluation framework that supports concurrency and optimized computation in simulator. Experiments across representative VLA and WAM models demonstrate 1.47x-4.38x end-to-end training throughput improvements over their corresponding open-source baselines, as well as 4.1x-23.2x faster evaluation under the same protocols.

---


### 82. [ActMem: From Latent Memory Reasoning to Grounded Robotic Action](https://arxiv.org/abs/2611.25461)

**<font color=#1a73e8>作者：</font>** Linfeng Dong, Jianwei Niu, Jiuyi Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.
However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full
history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past
experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that
decouples memory reasoning from perceptual grounding within a single vision-language backbone. Built on a vision-language model with native
video understanding, ActMem infers the current subtask from a timestamped interaction history and keeps the hidden states formed during this
inference as a Latent Memory Chain-of-Thought (Memory CoT), which conditions a flow-matching action expert. Perception Attention further lets
the expert attend directly to the current view. To keep inference fast under long histories, Efficient Memory CoT Inference reuses computation
across consecutive decisions without changing the output. ActMem achieves 71.1% task success and 80.8% completion success on RoboMemArena,
surpassing the strongest baseline by 7.5 and 8.7 percentage points, and 73.8% average success on MIKASA-Robo, the best among all compared
methods. In the real world, it reaches 68.8% average success on exogenous, endogenous, and traceless memory tasks, 10.0 percentage points above
the strongest memory-augmented VLA. Code and checkpoints will be released at this https URL and
this https URL.

---


### 83. [A Wolf in Sheep's Pixels: Visual Camouflage Attacks via HDR Gain Maps](https://arxiv.org/abs/2611.25469)

**<font color=#1a73e8>作者：</font>** Qi Shen, Yujia Gong, Yue Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image can pass automated safety checks while showing harmful content to its human viewer. We introduce DRJanus, a visual camouflage attack that exploits the gap between standard dynamic range (SDR) processing and high dynamic range (HDR) display. Automated systems often read only an image's SDR base, whereas HDR viewers reconstruct its appearance using an auxiliary gain map. DRJanus inverts this reconstruction to embed two independently chosen color images in a single JPEG, without querying or optimizing against the target model. It preserves the chosen SDR base exactly and reconstructs HDR targets at an average PSNR of 43.03 dB across 400 images. On a benchmark of 100 sexual-content images, DRJanus evades detection by all six tested commercial moderation services and nine vision-language models. Across five agents, each evaluated on 120 task cases per threat setting, attack success ranges from 31.67% to 100% for moderation evasion and from 95% to 100% for task manipulation. We also explore cross-view consistency checks as a mitigation. These findings expose a gap in visual trust: securing what a machine reads does not secure what a user sees. A demo is available at this https URL

---


### 84. [ToolPulse: Side-Channel Eavesdropping on Tool-Using LLM Agents](https://arxiv.org/abs/2611.25470)

**<font color=#1a73e8>作者：</font>** Zihao Dan, Jinyu Zhang, Jinzhao Lian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as agents that translate user requests into sequences of local tool invocations. While prior cache-based side-channel attacks target the locally deployed models, they typically require the adversary to share model-related components or hardware resources with the victim's inference process. These assumptions do not apply to the predominant agentic settings, in which commercial LLMs execute on vendor-controlled infrastructure. We show that agentic execution exposes a more practical attack surface: although inference remains remote, tools are executed on the user's machine and commonly rely on shared system libraries. In this paper, we first systematically evaluate Flush+Reload and Prime+Probe for monitoring agentic tool invocations. Our evaluation across three hardware platforms shows that Flush+Reload enables accurate, real-time tool monitoring, whereas Prime+Probe, despite supporting cross-VM attacks, incurs prohibitive monitoring overhead and suffers from cache-set aliasing. We present ToolPulse, a cache-based side-channel eavesdropping framework against tool-using agents. We first design the Tool Recovery Attack to reconstruct an agent's tool-execution workflow. We evaluate the Tool Recovery Attack on 11 LLMs across Codex and Claude Code. It consistently reconstructs tool workflows, with the lowest F1 score exceeding 93%. We further demonstrate two attack scenarios enabled by the recovered traces. Task Profiling Attack infers user intent across two Terminal-Bench task categories and the Trigger Localization Attack identifies sensitive tool calls in encryption/decryption and model training/inference workloads. Even under substantial system noise on a server shared by approximately 20 users, both Task Profiling Attack and Trigger Localization Attack maintain high accuracy.

---


### 85. [TuringPAI: A Foundation for On-Device Physical AI](https://arxiv.org/abs/2611.25474)

**<font color=#1a73e8>作者：</font>** Qiman Wu, Hanlin Chen, Yuhua Wei 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transformer-based global modeling. Multi-scale Latent Queries integrate spatial features and observation history within the same visual Transformer, providing a compact, structured interface to the language model. Training combines general vision-language data with geometric, cross-view, and temporal supervision. TuringPAI-VL supports general multimodal understanding and improves quantitative geometric perception over Qwen2-VL-2B, while providing a shared initialization for the two downstream VLA models. For autonomous driving, TuringPAI-Drive maintains all evaluated ADE/FDE metrics within 1.2\% of a full-token HybridViT baseline using the MLQ interface and achieves comparable aggregate scores in an in-house simulation evaluation. Using XPeng Native Runtime (XNRT) on a single NVIDIA Orin-X SoC, TuringPAI-Drive generates trajectories at 12\,Hz in on-vehicle operation. For robotic manipulation, TuringPAI-Embodied achieves a 96.8\% average success rate across the four LIBERO suites. These results demonstrate a shared vision-language foundation for driving and robotic manipulation under practical on-device constraints.

---


### 86. [WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming](https://arxiv.org/abs/2611.25476)

**<font color=#1a73e8>作者：</font>** Bo Li, Taoyong Cui, Bob Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks encode learned capabilities in their weights, yet extending those capabilities with explicit task knowledge remains a fundamental challenge. Here we show that Weight-Space Programming (WSP), in which executable programs read, construct or modify a network's weights directly, can install new capabilities within trained neural networks. WeightCode, a WSP framework, uses a frozen language model to write executable weight programs that install new computations into trained neural networks using task knowledge and their existing weights, without gradient-based training. Once installed, the new capabilities run independently of the language model. Given a grammar or eight demonstrations, weight programs enable previously unseen command compositions (0% to 99.8% exact match) and a new pickup action (0% to 98.4% success), while preserving the original command and navigation capabilities. On ImageNet, four weight programs achieve net gains of 8.84-17.62 points while preserving clean accuracy, outperforming the best of eight fine-tuning methods under matched examples, checks, and retention constraints. In a Vision Transformer, causal interventions show that installed noise-correction gates drive robustness gains, while their selective activation preserves clean accuracy. Rerun on five independently trained Vision Transformers without further language model calls, ten weight programs retain 83-110% of their source-network gains on average, whereas copying their fixed weight edits yields negligible gains. Six programs written for an already edited network add 5.23-14.50 points of contrast robustness while retaining the previously installed noise gain. Together, these results establish WSP as a new route to acquiring and accumulating capabilities in trained neural networks through reusable weight programs.

---


### 87. [When Should a Voice Agent Speak? End-of-Turn Detection in Turkish](https://arxiv.org/abs/2611.25489)

**<font color=#1a73e8>作者：</font>** Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Mustafa Sertaç Türkel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A voice agent that waits for a fixed silence before replying either interrupts users who pause mid-utterance or responds late to users who have finished. This study examines the decision at the onset of silence, using turn ends and turn-internal pauses extracted from the Real-TurnTurk corpus of Turkish dyadic video calls. A fine-tuned Turkish TurnGPT model, a zero-shot Turkish language model and a deployed multilingual detector are compared, together with voice-activity timing and facial features, under recording-disjoint and speaker-disjoint evaluation with paired cluster bootstrap tests. On held-out recordings, the fine-tuned model separates turn ends from pauses better than both text baselines and is the best calibrated of the three. Timing features of the current speaker are similarly informative, and their combination with the fine-tuned text score gives the best timing-based results; with logistic regression, this combination also outperforms the same combination with either text baseline. In a latency simulation, adding the text score to a silence timeout shortens the mean response delay at the same interruption rate. On automatic Whisper transcripts, the fine-tuned model retains its advantage over the zero-shot model.

---


### 88. [Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science](https://arxiv.org/abs/2611.25492)

**<font color=#1a73e8>作者：</font>** Almene De Meran Meguimtsop, Daniel E. Acuna  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) support scientific research, but some of that assistance can also undermine research integrity. Existing safety evaluations in science often measure whether models refuse misconduct requests, but rarely explain whether they even recognize the problem or why they comply. We investigate this gap across 8 LLMs using SciIntBench, an existing benchmark of 1,350 prompts about scientific research integrity. We examine the reasons behind compliance in four steps. First, when asked directly whether fulfilling a request would involve misconduct, models overwhelmingly identify such requests, even in the Most Covert cases (91%), while they refuse to carry out the request in only 34% of cases. Second, we examine which request characteristics are associated with refusal using features that capture how the request is framed, how much the assistant has been told about what it is helping to hide, and how the goal and the user's stake are stated, among others. Third, we estimate that the most significant effect was to rephrase requests as questions about permissibility rather than instructions, which increased refusal from 52% to 88%. Finally, we test two system-prompt fixes: asking models to assess the request before responding and reminding them of responsible conduct of research principles. These changes increase refusal rates on adversarial requests from 58% to 87% and 86%, respectively. Our findings show that models recognize wrongful requests but still help users violate integrity. Understanding why these failures occur and testing ways to reduce them offer promising paths toward more trustworthy AI for science.

---


### 89. [Coordinated Use of Large Language Models in Academic Research](https://arxiv.org/abs/2611.25502)

**<font color=#1a73e8>作者：</font>** Vladislav Marinov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study proposes a methodological framework for the coordinated use of multiple large language models in academic research. Its central argument is that involving more models does not in itself guarantee more reliable results; what matters is how cognitive and verification operations are organised. The framework is based on seven principles (procedural independence, functional allocation, the diagnostic value of divergence, the diagnostic value of convergence, external verification, proportionality of checking, and human epistemic responsibility) and sets out a non-linear multi-LLM protocol in which independently obtained results are compared, critically examined and, where necessary, verified against external sources. The approach is illustrated through real-world cases drawn from research practice. The study concludes that moving from a single language model to a coordinated multi-LLM process represents a change in the organisation of research, in which the researcher makes the final decisions and bears scholarly responsibility.

---


### 90. [Persona Lenses: What Makes a Vision-Language Model See Through Its Persona's Eyes?](https://arxiv.org/abs/2611.25508)

**<font color=#1a73e8>作者：</font>** Yoonho Shin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models have been used to simulate where a user looks on a web page. However, a persona in the prompt reaches the simulated gaze only partly. We measure this reach as the difference in one model's gaze between two MatrAIx personas that differ in a single attribute. We introduce persona lenses, which place the persona between the model and the page: a text lens (a two-step prompt in which the model first writes what the persona would look at), a pixel lens (marks on the region matching the persona's interests) and a weight lens (a dwell reward gated to keep the scanpath natural). Using Qwen3-VL (4B and 32B) and Qwen3.5-9B on generated and live pages, we compare the lenses with one another and with scale, the 32B model with no lens. It has been confirmed that the text lens separates the personas strongly but is not robust to profile changes that should not move gaze. The pixel lens separates the personas less but is unaffected by attributes unrelated to gaze. At 4B and 9B, the weight lens separates the personas on interests held out from training, with no extra step on a new page. The 32B model separates the personas with the base prompt alone. Therefore, the choice of a lens depends on cost and model size.

---


### 91. [DRVEXO-4B-Unified: Design and Evaluation of a Modular Speech-Vision System](https://arxiv.org/abs/2611.25521)

**<font color=#1a73e8>作者：</font>** Zeyuan Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present DRVEXO-4B-Unified, a modular multimodal assistant built around a 4B language backbone. A self-contained checkpoint combines text, image, and speech inputs with reference-conditioned speech output and structured interaction. A temporal residual connector adapts acoustic sequences to the language interface; explicit text boundaries support incremental speech synthesis; and three task-conditioned scoring heads rank supplied action candidates alongside generative tool calls. These interfaces connect conversation to application-defined choices while leaving action authorization to the application. The system obtains 74.22% on all 900 MMMU validation questions, exceeding the published validation scores of Gemma 3 4B IT and InternVL3.5-4B without test-time scaling. Strict prompt-level IFEval accuracy is 82.26% and MATH-500 accuracy is 89.40%, above the original Qwen3-4B non-thinking report's 81.2% and 84.8%, respectively. On NVIDIA GB10, the model achieves a speech-synthesis first-chunk latency of 390 ms. For concurrent text generation, a growth-aware admission policy completes a 128-answer batch at 594.41 output tokens/s, including filling and draining, without preemptions. We plan to release the model weights and accompanying code under Apache License 2.0, retaining applicable third-party terms.

---


### 92. [Contrast Where It Matters: Visual Evidence-Guided Decoding for Mitigating Hallucinations in LVLMs](https://arxiv.org/abs/2611.25524)

**<font color=#1a73e8>作者：</font>** Yiheng Li, Wenhao Wang, Xingyi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite strong multimodal capabilities, large vision-language models (LVLMs) often hallucinate when linguistic priors outweigh visual evidence or when predictions are grounded in irrelevant or misleading image regions. Training-free contrastive decoding mitigates hallucinations by contrasting the original prediction with an auxiliary one that exposes linguistic priors. Yet existing methods focus on altering the auxiliary input or computation and do not ensure that either branch uses query-relevant visual evidence during decoding. We propose Visual Evidence-Guided Decoding (VEGD), a training-free framework that identifies query-relevant visual evidence and guides its use throughout contrastive decoding. VEGD locates this evidence by aggregating localization heads with strong visual responses and coherent spatial structure, then selectively weakens it in the auxiliary image. During generation, VEGD directs visual-carrier heads in both branches toward the same evidence location, strengthening access to intact evidence in the main branch while anchoring the auxiliary branch to its weakened counterpart. An adaptive distribution fusion strategy then combines or contrasts their predictions according to distribution divergence. Experiments across diverse LVLMs and benchmarks demonstrate that VEGD consistently reduces hallucinations.

---


### 93. [MATE: Mobile Agent Trustworthy Execution for Safe and Efficient Mobile Control](https://arxiv.org/abs/2611.25526)

**<font color=#1a73e8>作者：</font>** Minsuk Jang, Hee-Seon Kim, Hui-Cheol Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mobile agents on personal smartphones can affect private data, payments, settings, and the foreground screen. We present MATE (Mobile Agent Trustworthy Execution), an execution-layer system that controls the boundary between agent action proposals and device effects without modifying the underlying model. MATE represents each UI primitive as a structured action record that combines the instruction, target app, screen context, primitive, and action fields. Runtime Guardrail (RG) maps this record to an allow, block, or user-approval decision; Predefined Task Routing (PTR) serves recurring requests through verified routes with post-execution screen checks; and a floating interface keeps execution in a compact overlay. On MobileSafetyBench, MATE raises high-risk blocking from 29.7% to 97.0% under GPT-4o. On AndroidWorld, it reduces LLM calls by up to 6x and raises recurring-use task success to 95.7%.

---


### 94. [LM-based Personalized Travel Planner](https://arxiv.org/abs/2611.25531)

**<font color=#1a73e8>作者：</font>** Amandi Nimasha, Oshadha Wijerathne, Dushan Fernando 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective travel planning requires handling multiple information sources, managing constraints, and tailoring recommendations to user preferences. While LLMs have introduced dynamic, context-aware decision-making, single-agent models often struggle with complex multi-step reasoning, constraint adherence, and modular execution. To overcome these limitations, we propose a hierarchical multi-agent framework where a supervising chatbot agent coordinates specialized agents for schedule validation, user query formulation, real-time data retrieval, and constraint-aware itinerary generation. By integrating LLM reasoning, external APIs, and iterative refinement mechanisms based on a deterministic, multi-dimensional scoring framework, our approach ensures adaptability, efficiency, and personalization. Evaluations on the well-known TravelPlanner benchmark demonstrate improvements in Budget Constraint planning by 10\%, wider constraints set-based planning by 25\%, and personalized planning results by 45\%. compared to the ReAct baseline. Our code is available at this https URL

---


### 95. [How Feedback-Free Self-Evolution Reshapes Agent Skills: A Systematic Study](https://arxiv.org/abs/2611.25534)

**<font color=#1a73e8>作者：</font>** Litao Guo, Man Chen, Xinli Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are documents in which experts write down procedural knowledge, and models increasingly maintain them by rewriting them without feedback. Such rewriting could adapt a skill to the model that uses it or erode the expert knowledge that makes it useful, yet how skills evolve under this feedback-free self-evolution has not been studied. We let models rewrite expert skills round after round without any task, run or judgment and run agents built on the same models with the rewritten skills. Our experiments show that the skills lose value rather than improve, as every model we test performs worse with them on every benchmark, by 15 points on average on SkillsBench after thirty rounds. Sampling each model's prior with skills it writes from the topic alone, we find that rewriting pulls skills toward this prior and gives up first the knowledge outside it. Putting this knowledge back recovers much of the lost pass rate, so an expert's skill is valuable largely for what the model does not write on its own. Building on this insight, SkillDiff marks this knowledge in place and raises the pass rate on SkillsBench by 4.8 points on average without feedback or any change to the skill's text. Project repository: this https URL.

---


### 96. [Support-Guided Triadic Decoding for Hallucination Mitigation in Multimodal Dialogue with LVLMs](https://arxiv.org/abs/2611.25535)

**<font color=#1a73e8>作者：</font>** Yiheng Li, Wenhao Wang, Xingyi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multimodal multi-turn dialogue, dialogue history plays a dual role: reliable responses provide useful context for subsequent turns, whereas hallucinated responses can propagate errors across turns. Existing training-free methods globally adjust the effect of dialogue history on generation, making it difficult to suppress misleading information without weakening useful context. To address this trade-off, we introduce Support-Guided Triadic Decoding (SGTD), a training-free framework that selectively controls the influence of unreliable history and fuses complementary predictions during decoding. Specifically, Historical Answer Support Estimation measures the visual support of historical responses against type-matched alternatives and identifies low-support content that may mislead later generation. Support-Targeted Attention Intervention then weakens the influence of this content while preserving the surrounding dialogue, producing a support-refined prediction. Triadic Decoding combines this prediction with the full-history prediction and answer-free visual evidence, while the Support-Adaptive Plausibility Constraint filters implausible tokens using visual agreement and historical support. Experiments on MMHalSnowball and VisDiaHalBench across representative LVLMs show that SGTD consistently achieves the highest accuracy under hallucinated histories while preserving the benefits of factual context.

---


### 97. [Query-Aware vs. Query-Agnostic Training-Free Video Token Pruning in Multimodal LLMs](https://arxiv.org/abs/2611.25537)

**<font color=#1a73e8>作者：</font>** Divya Kothandaraman, Timo Kumkel, Jaclyn Pytlarz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models process large numbers of visual tokens, making token pruning important for efficient inference. Training-free pruning methods differ in whether and how they use the user query, and the value of query conditioning remains unclear. We present a controlled study of training-free, pre-LLM video token selection. Using a shared Qwen-3-VL backbone, token budgets, and decoding settings, we compare 21 pruning principles spanning query-agnostic, shallow query-conditioned, structured query-conditioned, and holistic strategies. To instantiate the last two categories, we introduce Structured Query Pruning, which decomposes the question into semantic anchors, and a Pareto variant, which combines anchor relevance with query-agnostic visual diversity. Across Video-MME, MVBench, and LongVideoBench, relevance computed from the raw question embedding is unreliable (8--16 points below the best methods), whereas anchors derived from query decomposition avoid this failure. However, query access is not inherently advantageous: strong query-agnostic coverage methods remain competitive or superior in the full-field comparison. Relative to a redundancy-only baseline, structured selection helps most on evidence-specific and long-context tasks at tight budgets; on broad tasks, the holistic selector improves over either relevance or redundancy alone. Further, pruning reduces cost and memory. These results support a practical design rule: preserve visual coverage by default, and add structured relevance when the task and token budget demand selective evidence retrieval.

---


### 98. [Towards Autoregressive Neural Network Parameter Generation](https://arxiv.org/abs/2611.25538)

**<font color=#1a73e8>作者：</font>** Bedionita Soro, Bruno Andreis, Song Chong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently established a new paradigm in machine learning, demonstrating exceptional zero-shot generalization and complex reasoning capabilities. Concurrently, neural network parameter generation has emerged as a promising avenue for rapid task adaptation and model synthesis. Existing weight generation techniques, however, struggle to jointly learn the distribution of diverse models, to encode heterogeneous architectures within a single generator, and to generalize out of distribution. We therefore ask whether pretrained parameters can be encoded into a discrete domain so that the zero-shot generalization LLMs exhibit in text generation can be transferred to weight generation. Following this view, we propose an LLM-inspired approach, Instruction-Guided Parameter Generation (IGPG), that formulates network parameter generation as an autoregressive modeling problem. We first quantize pretrained weights with a VQ-VAE, then train a prefix-conditioned autoregressive generator over the resulting tokens. At inference, the generated weight tokens are mapped back to parameter space by the VQ-VAE decoder. We evaluate the framework across in-distribution generation, cross-dataset transfer, and cross-architecture settings. The proposed method achieves competitive performance in in-distribution generation and provides useful parameter initializations for held-out datasets and architectural configurations, improving downstream performance over random initialization after adaptation. These results suggest that discrete autoregressive modeling provides a promising framework for learning and transferring structure across collections of pretrained neural network parameters.

---


### 99. [COVERAGE-TRACE: Source-Side Counterfactual Tracing for Detecting Omissions in LLM Summaries](https://arxiv.org/abs/2611.25539)

**<font color=#1a73e8>作者：</font>** Ali Karkehabadi, Jamshid Hassanpour, Rafael E. Banchs  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omissions are difficult to verify because missing information leaves no output span
to inspect: a summary may be factually supported while still excluding a decision, qualification, quantity, or condition needed to preserve the source's meaning. We introduce COVERAGE-TRACE, a source-side counterfactual framework that evaluates omission as dependence on a designated atomic source fact. It replaces only the target fact with type-matched alternatives, holds the candidate summary fixed, and measures the resulting change in its teacher-forced, length-normalized likelihood. A summary covering the target should respond more strongly than one omitting it, while aggregation across multiple counterfactuals reduces sensitivity to replacement choice.
We evaluate COVERAGE-TRACE on 80 matched covered--omitted QMSum pairs spanning several fact types and four open-weight models. Multi-CF achieves 0.764--0.825 AUROC, compared with 0.640 for the strongest evaluated text-only baseline. On Falcon-7B, targeted interventions achieve 0.779 AUROC, whereas shuffling counterfactual assignments reduces performance to 0.533; target deletion is effective while unrelated deletion is not. However, adjustment for meaning-preserving paraphrases reduces AUROC to 0.591--0.624.
COVERAGE-TRACE therefore provides a practical, complementary signal of target-specific source--summary dependence, but not a wording-invariant semantic coverage probability. These results establish source-side intervention as a promising approach to omission detection while identifying semantic invariance as the central remaining challenge.

---


### 100. [Efficient Multimodal Agents for Auditing 3D Worlds](https://arxiv.org/abs/2611.25543)

**<font color=#1a73e8>作者：</font>** Jingbo Yang, Ziyan Jiang, Li An 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal agents can now build interactive 3D worlds and games, yet these worlds, like those built by people, often contain glitches such as floating objects, walls that can be walked through, or objects that change when no one is looking. An automatic auditor could check such worlds at scale and provide rewards for agents that build them, but only if it is both accurate and cheap. Auditing requires three abilities, namely navigating to the objects that may contain a glitch, triggering glitches that appear only after a specific behavior, and recognizing what is wrong. Current auditors are either accurate but slow and expensive or cheap but unreliable. We study how much of the audit small models can take on. A 4B vision language model fine-tuned end to end on verified trajectories of a frontier teacher guided by Bayesian search learns to navigate and trigger, and six such explorers together match a frontier model on both, but recognition stays far behind. We therefore build an auditor in which a swarm of small explorers navigates and triggers, and a frontier model reviews what they record and report. On WorldAuditBench, our auditor succeeds on 55.9% of 213 tasks in Unreal Engine 5 and this http URL worlds, 13.6 points above the strongest auditor reported, at less than a quarter of its cost. It matches the frontier reviewer exploring on its own at 4.6 times lower cost and about half the latency. Without further training, it also answers embodied questions about real-world scans, matching the frontier reviewer exploring on its own and surpassing four other frontier models by 6.4 to 16.6 points.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
