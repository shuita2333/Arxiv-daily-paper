# 🔐 大模型安全相关研究 | 2026年11月27日

> 本类共 **6** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Poisoning Self-Evolving Security Policies in LLM Agents](https://arxiv.org/abs/2611.33385)

**<font color=#1a73e8>作者：</font>** Aymen Noor, Honglu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-evolving defenses improve LLM-agent security by learning reusable policies from observed attacks. However, we demonstrate that this learning process itself can become an attack surface. Using SED (Self-Evolving Defense) in the AgentDojo benchmark, we construct a single prompt-injection episode that causes the defense to learn an over-broad policy and subsequently refuse legitimate requests. Across 10 Nemotron runs, every poisoned run over-refuses at least one legitimate task, while unrelated-task performance remains unchanged and the original prompt-injection defense remains effective. The attack also transfers to gpt-oss-120b; however, its poisoning mechanism depends on a successful initial prompt injection and therefore fails to activate when the target agent resists the underlying injection. In contrast, integrity-oriented attacks targeting SED's judge, policy synthesis, retrieval, and organization mechanisms fail in our evaluated settings, identifying over-refusal as the primary exploitable failure mode observed in our experiments. We further identify self-poisoning from false-positive harm judgments without an attacker. Finally, contrastive policy synthesis and an automatic broadness-check gate substantially reduce, but do not eliminate over-refusal, without compromising security in our evaluated settings.

---


### 2. [AVERT: Anomalous Value Erasure with Response Testing against Visual Prompt Injection](https://arxiv.org/abs/2611.33532)

**<font color=#1a73e8>作者：</font>** Newt Hue-Nam K. Nguyen, Jui-Yu Ho, Wei-Han Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) are vulnerable to visual prompt injection, in which an adversarially perturbed image forces the model to respond with the attacker's chosen content, such as malicious tool calls, website links, or advertisements, sometimes regardless of the user's question. Existing defenses, such as diffusion-based purification and image-token masking, mitigate these attacks at a substantial cost to the model's utility on benign inputs. To address this challenge, we propose AVERT, which removes adversarial feature directions only when the model's answer depends on them. Our key procedures involve identifying anomalous value subspaces and detecting answer dependence. To identify the anomalous value subspace, we compare the statistics of each input's attention-head outputs with those of clean images and extract the directions along which the input deviates the most. We then project out these directions to remove the injected content. Because the same directions also carry benign visual information, we apply the removal only to answers that depend on them, namely answers whose likelihood collapses once the directions are removed or that are as likely under unrelated questions as under the user's question. Against white-box attacks on four VLMs (Qwen2-VL, Qwen2.5-VL, LLaVA, InternVL2.5) and four injection benchmarks, AVERT lowers average attack success from 86-90% to at most 0.6% while retaining at least 96% of undefended utility averaged over thirteen benchmarks. Its defense-utility F-score ($F_{DU}$), the harmonic mean of attacks stopped and utility retained, is 98.0-99.1 and the highest among all compared defenses on every model.

---


### 3. [FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips](https://arxiv.org/abs/2611.33810)

**<font color=#1a73e8>作者：</font>** Zexi Zhao, Zizhen Liu, Jing Justin Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models generate robot actions from visual observations and language instructions in real-world environments, making malicious model tampering a potential threat to physical safety. We study whether object-triggered backdoors can be implanted through a small, fixed set of parameter bit flips without retraining. The central challenge is to make persistent weight modifications disrupt trigger-present behavior while preserving performance on non-trigger inputs. We propose FlipVLA, a two-stage selector-amplifier method that exploits existing visual features within an FC-GELU-FC structure. The selector constructs a trigger-dependent response in a selected channel, using GELU to attenuate background activity. The amplifier modifies a connected downstream weight to convert this response into an action-relevant perturbation. Channel screening and discrete bit search construct both components under a limited modification budget. Experiments on OpenVLA-OFT and GR00T N1.7 across four LIBERO suites achieve attack success rates of 90.22% to 100%, with task success decreasing by at most 1.5 percentage points on clean scenes.

---


### 4. [MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance](https://arxiv.org/abs/2611.34188)

**<font color=#1a73e8>作者：</font>** Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack style. We propose a different paradigm: defend by maximizing relevance, not by detecting attacks. Our method, MINE, is training-free and attack-agnostic, and it also serves as a query-conditioned reranker. To evaluate defenses under realistic conditions, we introduce LC-Inj-SQuAD, a long-context benchmark with an average of 4,032 words per context. We evaluate on four datasets spanning short-context QA (Inj-SQuAD, Inj-TriviaQA), long-context QA (LC-Inj-SQuAD), and agent tool-call injection (InjecAgent). Across all four, MINE achieves the best accuracy--security trade-off among training-free defenses. It is also the only defense that stays usable against a fully adaptive attacker, generalizes to agent tool-call injection, and achieves the lowest inference latency on long contexts.

---


### 5. [SOLO: Towards Sample-Faithful and Detectable LLM Watermarking under Repeated Sampling via Content-Anchored Single-Owner Contexts](https://arxiv.org/abs/2611.34190)

**<font color=#1a73e8>作者：</font>** Zhongliang Guo, Yan Lin, Yifei Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Providers watermark the outputs of large language models, while applications sample many responses per prompt for self-consistency, best-of-n selection, and uncertainty estimation. We show that deployed configurations of distortion-free watermarks, which deduplicate keyed contexts only within a response, couple the responses of a request: answer templates make all responses query the watermark with the same context before the answer, so collisions across responses, usually assumed rare, become the norm. Key pools reduce or avoid the coupling at the cost of multiple testing, and the exact remedy of a context history shared across the request leaves many positions unwatermarked. We propose SOLO, which keeps a request-scoped context history but anchors its keyed contexts on content selected by min-hash, so that siblings rarely compete for a context and random edits stay local. Its responses are jointly distributed as independent unwatermarked responses, each detectable with a single key. On five language models from three families and three benchmarks, SOLO preserves self-consistency and uncertainty estimation and, at a 1% false positive rate, detects more responses than four-token key pools on most tasks, also after randomly editing 10% of the tokens, and more than the context history on most clean tasks. Code is available at this https URL.

---


### 6. [Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems](https://arxiv.org/abs/2611.34278)

**<font color=#1a73e8>作者：</font>** Manit Baser, Vyoman Jain, Rachel Yeo Hui Min 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models increasingly collaborate in heterogeneous multi-agent systems, latent communication has emerged as an efficient alternative to exchanging natural-language messages. By sharing internal representations, agents can avoid repeatedly processing the same context, reducing communication overhead and prefill computation. One such mechanism is cross-model Key-Value (KV) cache transfer, which uses a learned mapper to translate a source model's KV cache into one a target model can use. However, this handoff means the target model consumes context it did not encode itself, thus calling into question whether its safety alignment still holds.
In this work, we investigate the security implications of latent handoffs by introducing Chasm, a framework characterizing cross-model handoff attacks across three new attack surfaces: the source model, mapper, and handoff mechanism itself. Our experiments reveal that latent handoffs substantially undermine safety alignment and prompt-injection defenses. Notably, a target model that follows only 0.4% of benchmark prompt injections natively, follows up to 44.2% when transferred through a mapper from a source model. On the other hand, for jailbreak attacks, transfer alone raises attack success by up to 24.6 pp within a model family and zero-shot attacks by up to 69.2 pp, whereas white-box optimization through the mapper boosts the attack success rate to 92.5%, against 37.5% for ordinary GCG on the same target. To address these vulnerabilities, we propose a lightweight target-side cache guard that corrects transferred caches to restore the target model's refusal, considerably mitigating these attacks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
