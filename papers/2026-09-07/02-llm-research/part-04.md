# 🧠 大模型相关研究 | 2026年09月07日

> 本类共 **180** 篇论文：已确认 **169** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-180**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-180**

---

### 151. [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098)

**<font color=#1a73e8>作者：</font>** Sergii Kozyrev, Davyd Maiboroda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and write-strength gates -- on the intuition that errors in a recurrence accumulate over long contexts. We test that intuition by building Minima: NVFP4 W4A4 on all 496 linear layers, GDN included. Across perplexity at 4K/32K, MMLU-Pro, GSM8K, AIME'25, GPQA-Diamond, LiveCodeBench, and RULER retrieval to 64K, Minima matches BF16 within seed noise (5-task average -0.52) while being the smallest (17.5 GiB) and fastest-prefill (+14-19%) recipe we compare, and its 32K perplexity gap shrinks with position. A four-part mechanism study explains why: (i) NVFP4's 16-element block scaling localizes the residual stream's extreme outliers, equalizing activation error across layer roles; (ii) the supposedly fragile gate projections are the least sensitive -- softplus/exponential and sigmoid parameterizations compress ~11% GEMM error to ~2% output error; (iii) the delta-rule recurrence holds injected noise at a flat plateau over 32K tokens and forgets a state impulse within hundreds of steps, because each write overwrites the state along the current key direction; (iv) the per-token quantization cost washes out with context instead of compounding. We also repair a global-scale mismatch that arises when per-module-calibrated NVFP4 checkpoints are served by kernels that fuse those modules into one GEMM, and show calibrated FP8 KV-cache scales are performance-free. The result: a practical recipe -- quantize everything, ship KV scales -- and a mechanistic account of why the recurrent half of a hybrid LLM is the easy half to quantize. Checkpoint: this https URL

---


### 152. [Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR](https://arxiv.org/abs/2609.04108)

**<font color=#1a73e8>作者：</font>** Boyan Li, Bingsen Chen, Chenghao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs. Prior work uses OPD's dense token-level supervision to complement the sparse RL reward, fusing the two signals within a single step: either as a \emph{weighted-additive combination} or a \emph{teacher-modulated rescaling} of the RL advantage. In this paper, we show that a simple two-stage scheme, OPD-then-RL, consistently outperforms pure OPD, pure RLVR, and all such joint baselines across logic and math reasoning benchmarks. Beyond the empirical results, we further provide a systematic understanding of this through pass@$k$ behavior, learning dynamics, and parameter updates, yielding a consistent explanation: OPD expands the student's coverage of teacher-supported solutions and RL sharpens within that support, while jointly optimizing the two signals causes them to this http URL provide a practical recipe, we find that the OPD validation score is the key signal for when to switch to RL, and that OPD is a better cold start for RL than SFT. Together, our results establish OPD-then-RL as a simple yet strong way to combine the two methods, turning two entangled signals into complementary stages.

---


### 153. [Epistemic Warrant for LLM Recommendations: Characterizing the Basis for Reliance When Ground Truth Is Unavailable](https://arxiv.org/abs/2609.04127)

**<font color=#1a73e8>作者：</font>** Shai Vardi, João Sedoc  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to support organizational decisions, yet users often lack a principled basis for assessing whether to rely on a specific recommendation. Existing approaches typically evaluate broad model properties, such as reliability, uncertainty, or robustness, or focus on user trust, rather than the underlying basis for relying on an individual recommendation. Adapting theoretical foundations from epistemology, we introduce epistemic warrant, a decision-level construct that characterizes the stability of a model's preference and the scope over which that preference holds. We operationalize this construct through a four-tier reliance certificate for pairwise recommendations, distinguishing among unstable, context-dependent, locally supported, and broadly supported recommendations. We validate the construct using contemporary methodologies: known-groups tests successfully recover expert-prespecified warrant orderings, and stronger warrants systematically align with independent consensus from crowd workers. Furthermore, we demonstrate that epistemic warrant provides information distinct from verbalized confidence and is not readily explained by decision difficulty. Ultimately, this framework offers a theoretically grounded, implementable approach for characterizing the warrant of individual LLM recommendations when objective ground truth is unavailable.

---


### 154. [Environment Evolution for Terminal Agents](https://arxiv.org/abs/2609.04128)

**<font color=#1a73e8>作者：</font>** Zhiyuan Fan, Tinghao Yu, Yuanjun Cai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling interactive and verifiable environments is critical for training terminal agents. As frontier models become more capable, environments synthesized from scratch become less challenging and thus provide limited learning signals. Recent co-evolution methods iteratively synthesize environments near the model's learnable frontier based on weaknesses exposed during rollouts. However, their dependence on on-policy rollouts limits generalization and the continuous provision of learning signals as the model becomes stronger. In this paper, we propose environment evolution, which incrementally increases environment difficulty off-policy and schedules the evolved environments generation by generation during training to provide continuous learning signals. We derive three evolution directions that influence environment difficulty from the multi-turn learning objective and then implement evolution along these directions through a loop-engineered multi-agent harness. Quantitative rollout experiments with Hy4 preview, Claude Opus 5, and GPT-5.6 Sol show that environment evolution consistently produces more difficult environments. We validate its effectiveness on Qwen3.6-27B and Qwen3.6-35B-A3B through simple long-horizon RL training, improving their performance by 14.4 and 18.0 percentage points on Terminal-Bench 2.1, respectively.

---


### 155. [Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding](https://arxiv.org/abs/2609.04131)

**<font color=#1a73e8>作者：</font>** Hongyu Qu, Guangming Yao, Ling Xing 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as additional visual context. Though effective, this store-and-retrieve paradigm keeps historical evidence as external visual context, preventing it from being internalized into a compact, evolving latent memory that can continuously guide streaming reasoning. To bridge this gap, we introduce LatentStream, a progressive latent working memory framework that shifts streaming memory from store-and-retrieve to retrieve-and-internalize. Specifically, LatentStream comprises three coordinated components. First, Query-agnostic Hierarchical Streaming Memory organizes visual history into short-, mid-, and long-term levels under a fixed memory budget through Jenks-guided adaptive consolidation. Once a query arrives, Hierarchical Latent Memory Evolution equips groups of latent memory tokens with progressively expanding memory receptive fields, enabling them to iteratively retrieve historical evidence from their corresponding scopes and internalize it into a compact, fixed-length latent memory. Finally, Progressive Confidence-guided Latent Memory Optimization constructs a hierarchical progression reward from group-wise predictive entropy and jointly refines the latent memory tokens and retrieved evidence, encouraging increasingly confident streaming reasoning. Extensive experiments demonstrate that LatentStream achieves new state-of-the-art results on existing online and offline video benchmarks.

---


### 156. [Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments](https://arxiv.org/abs/2609.04148)

**<font color=#1a73e8>作者：</font>** Jie Wu, Zhenru Zhang, Beichen Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As terminal-based code agents become prevalent, agent trajectories have accumulated at scale, while realistic, executable environments remain scarce. However, environments are what agent post-training actually requires: each can be re-queried into many verifiable tasks and provides execution feedback, whereas a trajectory is a single frozen demonstration. Rather than generating environments from scratch, we observe that the tool-execution history in existing trajectories exposes the structure and contents of the environments in which they ran, making it possible to reconstruct those environments from the trajectories themselves. Thus, we introduce Terminal-Universe, a framework which turns each trajectory into a reusable environment and explores it for synthesizing new tasks and continued interactions. Specifically, Terminal-Universe replays the file operations recorded in a trajectory to restore each file before the agent modified it, yielding a partial workspace; a completion agent then supplies the missing files and dependencies. On this recovered workspace, we both reconstruct the original intent task and synthesize entirely new ones. Besides, we also scale the tasks along two complementary axes: breadth and depth. For breadth, we mine directional dependency relations between related environments and synthesize cross-workspace queries spanning multiple codebases, as developers routinely do in real-world development. For depth, we extend the initial single-turn query into a multi-round session that captures iterative user feedback and requirement refinement via a user agent. Applied to public terminal agent trajectories, Terminal-Universe produces 37.3k task-sufficient environments. Supervised fine-tuning of Qwen3.5-27B on this corpus improves single-round performance on Terminal-Bench 2.1 by 11.9 points and multi-round performance on EvoCode-Bench v2 MT@4 by 13.8 points.

---


### 157. [Persistent Identity Preservation in Generative Image Models: A Benchmark and Evaluation System](https://arxiv.org/abs/2609.04151)

**<font color=#1a73e8>作者：</font>** Mengwei Ren, Xuaner Zhang, Zhihao Xia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image models can now produce high-quality images, follow complex instructions, and support precise edits, but they still struggle to preserve who or what is being depicted. When generating or editing images of a specific subject, identity may drift as the pose, expression, appearance, viewpoint, or surrounding scene changes. Existing subject-driven methods make fundamentally different choices about where identity is represented: through the input context (GPT-Image-2, NB2), as trainable subject-specific model parameters (LoRA), or as a persistent identity layer (PHOTA IDENTITY) reusable across generations and edits. We systematically benchmark these paradigms across subject-driven generation, editing, restoration, and multi-subject settings, with tasks designed to increasingly stress identity preservation. Our results show that identity preservation remains a distinct limitation of current generative foundation models: strong image quality and instruction following do not necessarily imply strong identity fidelity, and identity degradation becomes more pronounced under iterative edits, small subject scales, severe image degradation, and multi-subject composition. Persistent identity substantially reduces this degradation across generation, editing, and restoration, consistently improving identity preservation when applied to different foundation models while maintaining comparable instruction adherence and perceptual image quality. These results suggest that identity does not simply emerge from increasingly capable generative models, but can instead be represented as persistent subject knowledge that is composed independently with the underlying generative model.

---


### 158. [SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center](https://arxiv.org/abs/2609.04159)

**<font color=#1a73e8>作者：</font>** Uday Vallabhaneni, Cassie L. Cagwin, David J. Wild  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly proposed as autonomous SOC analysts, but two limitations make them unreliable at enterprise scale: a finite context window cannot hold a multi-thousand-host authentication graph, and free-form generation offers no guarantee that a recommended containment action is consistent with the topology it operates on. We present Sentinel-RL, an agentic-SOC architecture that decouples topological reasoning from semantic reasoning: a heterogeneous graph attention encoder summarizes the live authentication subgraph into a fixed-dimensional state, a Proximal Policy Optimization (PPO) policy maps this state to a constrained set of investigative actions, and an LLM agent loop is restricted to consuming the policy's recommendations and producing analyst-readable narratives gated by a critic. We instantiate the system on the LANL Comprehensive, Multi-Source Cyber-Security Events dataset and the Indiana University Quartz HPC cluster, reporting four results: (i) a two-phase CREATE ingestion pattern loads a 24M-edge authentication subgraph into Neo4j in 14.2 minutes on a single 32-core node, roughly 24x faster than the canonical MERGE-based pipeline; (ii) a sliding-window alert engine reliably trips a 25-event/10-second threshold in <=2.5 s across 50 trials; (iii) PPO training over 200 iterations converges to a mean episodic return of 8.74+/-0.31, with held-out precision of 0.91 and recall of 0.87 on labeled red-team events; and (iv) the integrated containment loop completes a full detect-investigate-recommend-human-approve cycle in a median of 6.3 s. We contribute a reusable engineering pattern (the hot-node deadlock workaround), a portable HPC deployment pattern (anchor-node co-location), and an enterprise-readiness analysis covering false-positive economics, reversibility guarantees, audit compliance, and the human-approval boundary.

---


### 159. [From Deceptive Outputs to Deceptive Mechanisms: A Causal Framework for Language-Model Deception Research](https://arxiv.org/abs/2609.04166)

**<font color=#1a73e8>作者：</font>** Yakov Pyotr Shkolnikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research and news coverage of language-model deception increasingly attributes human-like mental-state concepts to language models. Such claims can blur the distinction between behavior that looks deceptive and a mechanism that is actually deceptive.
We introduce a causal taxonomy separating prior commitment from retrospective report, model preference from realized output, false preference from sensitivity to the utility of misleading a recipient, and deceptive behavior from the provenance of the objective or strategy producing it. We test these distinctions in two open-weight model families. Across controlled guessing-game and stock-trading experiments, we find that deceptive-looking behavior can arise without the corresponding proposed mechanism, while other interventions provide direct evidence that recipient information state can causally affect deceptive preference.
These results show that deceptive behavior can provide evidence for a deceptive mechanism. But even evidence for such a mechanism does not establish model agency in the deception.

---


### 160. [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170)

**<font color=#1a73e8>作者：</font>** Davide Paglieri, Logan Cross, Tim Genewein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI science ecosystems rely on agents possessing tools that allow them to communicate, coordinate, and build on each other's work. Yet this shared infrastructure can also introduce vulnerabilities by creating a substrate for the contagious spread of unintended and undesirable behaviors. We report a case study on a research collective of 100 autonomous LLM agents tasked with proving formal mathematical conjectures. Within the swarm, cheating spontaneously emerged and was later challenged by whistleblowers - both without any external intervention. When a single agent discovered an exploit in the evaluation system, it propagated across the collective via a shared knowledge library and later through peer-to-peer messages. Despite early reluctance, a cohort of agents adopted the exploit in response to competitive pressure. A separate group of agents produced an emergent counter-response: auditing fraudulent proofs, alerting peers across broadcast and private channels, staging boycotts, lodging formal complaints, and proposing validation patches. In recent incidents, agent swarms coordinated covertly through improvised side-channels (Dalton and Wallace, 2026; Greenblatt et al., 2026). Our setting differs: the same transparent channels that carried the exploit also gave non-cheating agents the visibility they needed to detect fraud, organize resistance, and enforce norms. We cast the problem of managing the agents' shared infrastructure as the knowledge commons governance problem (Ostrom, 1990). To protect the commons from exploits, we propose to adopt institutional mechanisms, such as graduated sanctioning and collective-choice rules, to support decentralized self-governance in autonomous swarms.

---


### 161. [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172)

**<font color=#1a73e8>作者：</font>** Zixuan Fu, Bingxiang He, Yuxin Zuo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher. Existing work has mainly studied its algorithmic behavior, leaving the role of training data unclear. We examine this role at the data-minimal limit by training on a single query. One-shot OPD keeps improving for hundreds of steps and recovers most of full-data OPD's gain across task domains and model families. We explain this result through the states visited during training and the rate at which the student aligns with the teacher. We measure \emph{state coverage}, the fraction of the states full-data OPD visits that a query set's rollouts reach. A single query already reaches \(71.5\%\), most of it within the first 100 steps. Adding semantically distinct queries raises coverage and validation accuracy together, until 16 queries reach \(98.9\%\) and match full-data training. Yet alignment slows at a similar pace whether OPD trains on one query or the whole dataset, and even a fixed set of states takes hundreds of steps to absorb. OPD is therefore data-overfed but algorithm-starved. Its rollouts quickly expose broad supervision, while the student absorbs that supervision increasingly slowly. The state-coverage result extends to multi-teacher OPD, where 16 semantically diverse queries per domain match full-data MOPD. As a further stress test, content-light templates and off-domain WildChat queries also approach the real-query baseline. Task content and induced state coverage can therefore come apart. We hope these findings direct future work toward the step efficiency of OPD, and prompt a re-examination of the data and the mechanisms behind its recent successes in frontier post-training.

---


### 162. [Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views](https://arxiv.org/abs/2609.04180)

**<font color=#1a73e8>作者：</font>** Joseph Lee, Yidi Huang, Dokyoon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary for acquisition and clarify that paraphrasing helps only at smaller batch sizes. Second, holding the token budget fixed, allocating tokens from document repetition to auxiliary views improves learning, counterintuitively, even for factual recall. Third, the effectiveness of auxiliary views is not contingent on the strength of the teacher model that generates them. Fourth, we identify forms of knowledge, contextual and foundational, that aid learning in the presence of prior knowledge gaps. Finally, we examine how these effects manifest mechanistically via layer-wise biases and compression. Together, our findings suggest that auxiliary representations of knowledge, which arise naturally in large pre-training corpora, are a key factor in the success of pre-training and offer a plausible explanation for why data diversity matters.

---


### 163. [Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning](https://arxiv.org/abs/2609.04183)

**<font color=#1a73e8>作者：</font>** Ye-Chan Kim, Seunghee Choi, SeungJu Cha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions lack visual grounding and are rigidly assigned to every inter-event gap at a fixed location and duration. To address these, we propose Seeing Before Synthesizing (SBS), a framework that adaptively provides visually grounded linguistic guidance only where warranted. Leveraging a VLM, we generate frame-level narratives for the inter-event gaps and detect transitions from the semantic variation across them. For identified transitions, we then refine inter-event temporal masks by blending the temporal midpoint with the semantic change point and selecting the width that maximizes vision-language alignment. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance in both captioning and localization.

---


### 164. [Toward Frontier-Quality Declarative UI Generation at Small-Model Cost](https://arxiv.org/abs/2609.04184)

**<font color=#1a73e8>作者：</font>** Yingxiang Yang, Weihang Xiao, Ben Bullough 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Declarative UI protocols such as A2UI let applications generate interactive UIs by selecting pre-built components from a catalog and binding their props to application data, rather than emitting frontend code from scratch. This contract is attractive for production systems because of safety and consistency. An open question is: can low-latency and low-cost small models achieve the required quality for A2UI-based UI generation? To answer this, we systematically study three controllable design choices for catalog-conditioned A2UI generation: supervised fine-tuning (SFT) data construction method, model size, and component-catalog size. Across two React/TypeScript domains and four base checkpoints spanning two model families (Qwen 3.5 0.8B/2B/4B; SmolLM 3B), we find: (i) a 4B fine-tuned student recovers ~98% of teacher semantic quality and ~97% of teacher visual quality at more than an order of magnitude lower cost than frontier API calls; (ii) both augmented strategies (Perturbed-catalog and Constrained-GT) Pareto-dominate the unaugmented Full-catalog baseline, while specializing on different axes; (iii) even small models can handle and benefit from relatively large component catalog size. We distill these results into practitioner-facing trade-offs and deployment recommendations across the three design choices.

---


### 165. [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](https://arxiv.org/abs/2609.04194)

**<font color=#1a73e8>作者：</font>** Kevin Du, Alexander Hoyle, Laura Ruis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, evaluate faithfulness, and provide step-level supervision via process reward models and generative critics. These practices rely on the text of a reasoning step carrying information about its functional role. But does the text actually encode information about which reasoning steps matter? We operationalize the importance of a reasoning step as its advantage: the change in expected reward, e.g., producing the correct final answer, from including that step, estimated via Monte Carlo rollouts. Basing ground truth on these estimates, we evaluate whether LLM judges can identify high-advantage steps and find that sufficiently capable LLMs can outperform a prevalence baseline but fall well short of a noise ceiling. Fine-tuning a model as a step-level critic yields strong improvement for incorrect responses but remains distant from ceiling for correct responses, suggesting that step importance is only partially recoverable from the text of the reasoning trace. Our findings contribute to a growing body of chain-of-thought faithfulness work that cautions against treating the legibility of reasoning traces as interpretability, especially with implications for process reward modeling.

---


### 166. [ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize](https://arxiv.org/abs/2609.04197)

**<font color=#1a73e8>作者：</font>** Lihao Liu, Peng Tang, Kunwar Yashraj Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate. We trace this to three deficiencies - incomplete error observation, limited search diversity, and unreliable selection - and propose ESPO (Error-Structured Prompt Optimization), which decomposes prompt optimization into three phases: Diagnose clusters all training errors into structural patterns in one round; Propose generates candidates via four complementary strategies with independent biases; Select applies bootstrap stability selection. On seven public NLP benchmarks - Tweet, MMLU, GSM8K, HotpotQA, ScoNe, HoVer, and PUPA - ESPO improves average accuracy by $+$3.76 pp over the state-of-the-art (74.67% vs 70.91% for GEPA), matching or exceeding GEPA on every dataset while producing prompts 47% shorter (1,004 vs 1,878 chars) and faster at inference. Cross-model experiments across four additional student models (Gemma 3 12B, Mistral 14B, Qwen3 32B, Claude Haiku 4.5) show ESPO yields the best average accuracy on every model tested, with the largest gap on Qwen3 GSM8K (15.00% $\to$ 91.40%). A generalization bound (Appendix) grounds each phase in a corresponding term of the test-time gap, and the ablation confirms a key prediction: adding diversity without bootstrap selection actually hurts performance ($-$1.20%).

---


### 167. [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198)

**<font color=#1a73e8>作者：</font>** Haoyaun Zhu, Jie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow. We audited that assumption in two preregistered campaigns with every threshold fixed in advance; neither got past validating its instrument. Across 52,988 audited request attempts, same-window repeat rankings agreed at Spearman 0.400 against a required 0.90, and byte-identical next-day replays agreed at 0.78 against a required 0.99, each time with the execution record at ceiling. Three mechanisms explain the gap: a label-to-meaning mapping that biased readouts as strongly as the signal; candidate gaps seven orders of magnitude below the instrument's own noise floor; and byte-identical inputs returning different rankings, a noise that exact-permutation readouts compound. Neither metric substitution nor sampling repaired it on the tested grid. Preregistered follow-ups bound the problem: waiting did not help on the days sampled (0.805 versus 0.800, replicated over five further days); switching providers did not help (four providers share the floor, medians 0.74 to 0.88, predicted by none of the metadata fields they expose); self-hosting on batch-invariant kernels helped only while the server was quiet; and on constructed errors with known gaps, the readout's separation tracks error type, not size. We distill the evidence into a three-level snapshot-identity ladder, eight design rules, and a reporting checklist; a pilot at roughly 2% of the study's call volume would have exposed both unreachable gates in advance. All results concern externally measured behaviour on shared serving infrastructure. On a shared endpoint, a model name is not a frozen instrument; a preregistered evaluation must measure its instrument before freezing any gate on it.

---


### 168. [Principia: Relational Physics Tests for Video Models](https://arxiv.org/abs/2609.04200)

**<font color=#1a73e8>作者：</font>** Varun Varma Thozhiyoor, Shivam Tripathi, Venkatesh Babu Radhakrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavailable in generated video. We propose a different approach. When two objects in the same scene obey the same physical law, their motions must satisfy predictable relationships, and these relationships hold independent of calibration. We introduce Principia, a benchmark that evaluates Newtonian physics through relational consistency between paired objects. Principia spans eight phenomena - gravity, restitution, friction, rotational inertia, projectile motion, momentum, pendulum, and mass-spring oscillation - across translational, rotational, collisional, and oscillatory dynamics, using real-world scenes recorded under controlled protocols. We also introduce a calibration-independent consistency score that quantifies physical violation directly in image space. Across thousands of generations from six state-of-the-art video generators, no model exceeds 0.42 on Principia despite all scoring around 0.8 on VBench. Vision-language models are evaluated on their ability to detect relational physics violations, with the best model achieving only 67% accuracy and most performing near chance level.

---


### 169. [Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision](https://arxiv.org/abs/2609.04203)

**<font color=#1a73e8>作者：</font>** Shravan Venkatraman, Wenshuai Zhao, Mohammad Hassan Vali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce S$^3$T (Self-Supervised Self-Distillation over Time), which, to the best of our knowledge, is the first fully self-contained framework for continuous video state tracking. Our method treats temporal sampling density as privileged information, based on the hypothesis that a denser view of the same clip recovers the running state more accurately. This view serves as the teacher, while a sparse-view student with the same weights learns to match its next-token distribution. The model generates its own target, so training requires no labels, separate teacher, or reward signal, and adds no inference cost. On LLaVA-OneVision-2-8B, S$^3$T improves VSTAT accuracy by $+1.74$ as a single model, $+2.38$ with souping, and $+2.70$ with additional vision-encoder adaptation, while prior self-evolving methods leave state tracking largely unchanged. The capability learned from unlabeled synthetic clips transfers to real videos, improving performance by $+7.95$ on VSTAT-YouTube state-tracking questions and $+4.50$ on MVBench Action Count.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 170. [Causal Foundation Models](https://arxiv.org/abs/2609.03003)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Christopher Stith, Hossein Rahmani, Jesse C. Cresswell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal inference is the practice of estimating the effect of a treatment or intervention from data. It traditionally requires a bespoke pipeline for every new problem: first proposing a causal mechanism, selecting a compatible estimator, and finally training it. Meanwhile, across diverse settings and modalities, much of machine learning has shifted to the paradigm of foundation models: networks pretrained once at scale and applied to new tasks without fine-tuning. Causal foundation models (CFMs) bring this paradigm to causal inference. CFMs are pretrained neural networks that estimate causal quantities, such as the average treatment effect, on entirely new datasets using in-context learning without requiring model updates. This work provides a practical introduction to this emerging area. We summarize the necessary background in causal inference and machine learning before discussing CFMs. Throughout, we include example code and Jupyter notebooks.

---


### 171. [Tree species mapping in Denmark: A comparison of spectral-temporal features with geospatial foundation model embeddings](https://arxiv.org/abs/2609.03480)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alkiviadis Koukos, Spyros Kondylatos, Thomas Nord-Larsen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We map tree species across Denmark using National Forest Inventory plots and EO data, while evaluating the potential of foundation models for large-scale forest characterization. We compare two alternative input representations for tree species classification: (i) manually engineered spectral-temporal features (STF) derived from multi-temporal Sentinel-1 and Sentinel-2 observations, and (ii) embeddings generated by the EO FMs TESSERA and AlphaEarth. Both representations are complemented with canopy height information. Random forest, XGBoost, and Multi-Layer Perceptron (MLP) classifiers are evaluated for all input representations, with separate assessments for pure and mixed forest stands. The STF-based MLP achieves the highest classification performance, yielding macro F1 scores of 0.843 and 0.653 for pure and mixed stands, respectively. The MLP trained on TESSERA embeddings delivers competitive performance for pure stands, achieving results within 1.1 percentage points of the best-performing model. TESSERA consistently outperforms STF-based models when fewer than approximately 25% of training plots are available, demonstrating a substantial advantage under limited training data. Multi-year observations systematically improve classification accuracy relative to single-year inputs, while ablation experiments reveal the complementary contributions of Sentinel-1 backscatter, spectral indices, and canopy height data. The best-performing model is subsequently applied at the national scale to generate a 10 m tree species map of Denmark. Area-adjusted validation indicates an overall map accuracy of 79.9%. The resulting map, released as an open-access product, is the first high-resolution national tree species map of Denmark and provides a valuable resource for forest monitoring, ecological research, and land management applications.

---


### 172. [What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation](https://arxiv.org/abs/2609.03515)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bo Zeng, Yu Zhao, Yefeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decoding-time KV cache compression research focuses heavily on designing better token scoring functions, while the temporal rule that aggregates scores across decode steps is often treated as an implementation detail. Under aggressive KV compression, we find that exponential-moving-average (EMA) aggregation makes approximately order-preserving scorer modifications largely indistinguishable at the eviction-set level. Value-norm and entropy variants remain highly correlated with attention and produce nearly unchanged retention sets, whereas KeyDiff, key norm, recency, and a learned scorer alter the ranking and degrade substantially. We associate this stability with the evaluated aggregation, which couples layer weighting and temporal retention. Building on this observation, we introduce InertiaKV, an EMA-based decoding-time eviction method, and InertiaKV-Lazy, its periodic-refresh variant, which yields 1.34-1.46x decode throughput relative to full refresh InertiaKV. We also study Score-Free decoding as a separate empirical operating point: it scores the full context once at the first decode step, freezes that ranking, and incurs an average quality change of +0.03 while removing all subsequent scoring. Across six open-weight backbones and the LongBench, LongBench-v2, and RULER benchmarks, the results identify temporal aggregation and ranking preservation as distinct, consequential design factors; they do not imply that scoring quality is irrelevant in general.

---


### 173. [</think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination](https://arxiv.org/abs/2609.03633)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seunghee Koh, Sungjae Choi, Minchan Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning improves large reasoning models (LRMs) on complex tasks but often produces long, redundant traces. Recent training-free early-exit methods shorten these traces by choosing an intermediate point to stop reasoning. We study one such strategy that injects an end-of-think token (EoT, </think>) at this point to trigger the reasoning-to-answering transition, and find that the injected EoT does not always induce a clean answering phase. Answering-phase generation can continue before the model regenerates another EoT, with the span preceding this regenerated EoT scaling with the reasoning tokens saved by early exit and exhibiting continued reasoning behavior. We call this spurious CoT termination, where reasoning-like generation continues into the answering phase. We hypothesize that insufficient attention to the injected EoT contributes to spurious CoT termination and probe this hypothesis with Exit-token Attention Biasing (EAB). Across four LRMs, five benchmarks, and two early-exit methods, increasing attention to the injected EoT reduces spurious CoT termination and answering-phase length. These results reveal a limitation of controlling LRMs by externally matching their explicit think-block format. Inserting the EoT token conforms to this format but does not by itself guarantee the intended reasoning-to-answering transition. Our code is available at this https URL.

---


### 174. [Enhancing Financial Question Answering: A Novel Benchmark Dataset of Banks' financial statements](https://arxiv.org/abs/2609.03654)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arianna Miola, Bruno Spaccavento, Lorenzo Silotto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The comparative analysis of banks' financial statements poses significant challenges for automated question answering systems due to their complexity, substantial length, technical language, and inhomogeneity of both textual and numerical content across different jurisdictions and institutions. We introduce FinRAG-QA, a novel benchmark dataset for financial question answering, which comprises 999 practitioner-curated questions on 10 standardised indicators, grounded in 209 annual and Pillar 3 reports from 24 major European and U.S. banks spanning 2019-2023. Unlike prior financial QA benchmarks, which centre on U.S. filings and single-institution analysis, FinRAG-QA targets cross-institutional retrieval over documents averaging 198k words, longer than any existing financial QA resource. On this benchmark we evaluate a multi-stage RAG pipeline and isolate the contribution of each component. Contextual chunk enrichment combined with a retrieval-optimised embedding model raises NDCG@10 from 0.322 to 0.710; conditional on the ground truth being retrieved, a reasoning-optimised generator raises answer accuracy from 44.6% to 79.0% (+34.4 percentage points), at roughly 20x the generation latency. We further show that cross-encoder reranking degrades retrieval when the first-stage ranking is already strong, and that a single top-ranked chunk outperforms larger contexts at generation time. Experiments were run in late 2024-early 2025 with the models available at that time.

---


### 175. [VisCAD: A Foundation Model Suite with Multimodal Industrial CAD Intelligence](https://arxiv.org/abs/2609.03811)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** JoyIndustrial VisCAD Team, Linxin Cai, Qiuhe Hong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-assisted computer-aided design (CAD) for industrial products involves two challenging phases. Part-level generation maps diverse forms of user intent, including renders, text descriptions, 2D drawings, and real photographs, to executable programs in a CAD domain-specific language. Assembly-level generation must additionally handle interacting parts, plan mating relations, estimate poses, and place all parts correctly. Existing specialized CAD models are commonly trained on narrow input domains, such as renders or texts, and often generalize poorly, while general-purpose frontier models cover broader inputs but perform inconsistently across CAD domains. We present VisCAD, a foundation model suite designed to provide both broad generalization and strong CAD capability for realistic industrial products. At its core is VisCAD-M1, a 27B model trained through mid-training and post-training for part-level design generation. On PubCADBench and RealCADBench, VisCAD-M1 achieves the highest average part-level score among the evaluated models, reaching 0.5540 compared with 0.5496 for the strongest frontier model. Reusing VisCAD-M1 as a test-time verifier can further raise the score to 0.5797, an approximately 5 percent relative improvement over the previous state of the art. VisCAD also includes a domain-specific harness that leverages frontier models for complex assembly generation and demonstrates advantages over general-purpose harnesses in both quantitative and qualitative evaluations.

---


### 176. [VI3: Grounding Pretrained 3D Foundation Models with Inertial Cues](https://arxiv.org/abs/2609.03824)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ernesto Lozano, Alberto Jaenal, Javier Civera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D foundation models (3DFMs) excel at predicting camera poses and dense depth from multiple views of a scene, showcasing strong zero-shot generalization. However, as metric scale is not observable from monocular images, their absolute scale predictions are typically inaccurate. Inertial measurement units (IMUs), present in most devices, naturally complement monocular cameras by observing scaled motion. We introduce VI3, a model-agnostic framework that metrically anchors a pretrained 3DFM using only IMU readings. VI3 initializes and preintegrates the IMU to obtain a metric motion reference, which is then used to recover the scale of the 3DFM outputs. Our method includes adaptable anchoring strategies tailored to diverse 3DFM architectures. Experiments on synthetic and real aerial datasets demonstrate that VI3 recovers metric scale without ground-truth supervision while preserving geometric consistency, acting as a fine refinement under well-conditioned motion and as a strong prior when motion is less informative.

---


### 177. [Subspace Inference Enables Efficient Active Reward Learning from Preferences](https://arxiv.org/abs/2609.04066)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yutai Zhou, Erdem Bıyık  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) has emerged as a powerful yet sample-inefficient approach for learning reward models from human preferences, making active learning a critical component in synthesizing informative preference queries. However, effective uncertainty quantification required for active learning remains a key challenge for large neural network reward models. In this paper, we introduce PreferenceEKF, a sample-efficient approach that tracks reward model uncertainty by framing active preference learning as a sequential Bayesian filtering problem. Instead of relying on computationally prohibitive posterior inference over the full neural network parameter space, our method performs sequential inference via an extended Kalman filter within a low-dimensional parameter subspace, continuously updating the reward model posterior as new preference queries arrive. Our approach enables scalable sampling of neural network parameters to efficiently compute acquisition functions for active reward learning. Experiments on the D4RL and V-D4RL benchmarks demonstrate that our approach achieves better sample efficiency, runtime, scalability, and calibration compared to other Bayesian deep learning approaches, and the learned reward models lead to competitive offline reinforcement learning policy performance. This highlights the potential of scalable Bayesian methods for preference-based reward modeling in RLHF. Our code is available at this https URL.

---


### 178. [TAP-Path: Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy Pathology Foundation Models](https://arxiv.org/abs/2609.04071)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mehedi Hasan, Ashfak Yeafi, Md Khairul Islam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models improve transferable representation learning for histopathology, but recent gains often rely on encoders with hundreds of millions of parameters and high inference cost. We propose TAP-Path, a task-adaptive compression framework that directly restructures a pretrained Virchow2 encoder rather than distilling it into a separate student. TAP-Path combines validation-driven transformer-block selection, physical removal of redundant blocks, input-adaptive patch-token pruning, multi-depth feature recovery, and a lightweight gated task head. The final model retains 24 of 32 transformer blocks and 70% of patch tokens after pruning, reducing encoder parameters by 24.96% (631.24M to 473.70M) and analytical encoder compute by 35.20% (340.13G to 220.40G FLOPs). Across three task-head optimization seeds, TAP-Path achieved $87.98 \pm 0.067%$ test accuracy, $81.26 \pm 0.49%$ balanced accuracy, and $82.38 \pm 0.48%$ macro-F1 on a 32-class histopathology benchmark, compared with 86.89% for full Virchow2 and 87.67% for UNI2-h. TAP-Path achieved a Brier score of $0.1800 \pm 0.0005$ and failure-detection AUROC of $0.9047 \pm 0.0060$. A validation-only rare-aware objective improved rare-class balanced accuracy in a secondary operating analysis. Frozen external evaluation on 433 CPTAC samples yielded $91.22 \pm 0.83%$ accuracy and $91.10 \pm 0.81%$ balanced accuracy. These results show that task-adaptive structural and token sparsification can improve the accuracy-efficiency trade-off of large pathology foundation models while preserving reliability under internal and external evaluation.

---


### 179. [DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shubham Gandhi, Saurabh Goyal, Kiran Kate 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work in the outcome-blind setting, where ground-truth success signals are not available. Multi-criteria rubrics are a popular way to supply such a reward; they are scored once per trajectory, but a single scalar is a poor signal across tens of steps. We propose DRACO: Distributing Rubric-based Advantage for Credit Optimization. It generates rubrics dynamically during training to track the policy's evolving capability, scores those rubrics once per completed trajectory, and redistributes that judgment over the steps responsible for annotated rubrics to produce differentiated per-step advantages in GRPO. The redistribution is closed-form and does not introduce any trained attribution module. On AppWorld, DRACO gains 15.9 points over the base model and 5.3 points over GRPO trained with a sparse ground-truth reward, despite not using any verifiers itself. On out-of-domain Tau-Bench, it gains 5.3 points over the base model even without a frontier judge, beating both ground-truth-reward training and other rubric-based training settings. The code for DRACO is available at this https URL.

---


### 180. [Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations](https://arxiv.org/abs/2609.04174)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Denis M. Akola, David F. Fouhey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Foundation Models (3DFMs) such as VGGT have recently pushed the boundaries of 3D vision by predicting rich unified representations with feed-foward transformers. The scene representations learned by these models enable strong performance on multiple 3D vision tasks. In this paper, we investigate using their internal representations to infer 3D in the scene from new views. Our hypothesis is that in order to solve the task of 3D reconstruction, these models need to learn a representation that includes a large amount of general knowledge about 3D scenes. After showing that it is possible to decode hidden surfaces from internal 3DFM representations, we propose a method, Z3D, that estimates pointmaps in unseen views by doing latent diffusion on 3DFM representation. We show that Z3D can predict realistic depth maps for new views across multiple datasets.

---


> [!TIP]
> 当前位于：**151-180**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-180**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
